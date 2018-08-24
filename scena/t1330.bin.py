from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t1330.bin",                # FileName
        "t1330",                    # MapName
        "t1330",                    # Location
        0x00B7,                     # MapIndex
        "ed7160",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x01,                       # PlaceNameNumber
        0x1A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, -16000, 0, 0, 1, 183, 0, 1, 0, 2],
    )

    BuildStringList((
        "t1330",                  # 0
        "Elie",                   # 1
        "Tio",                    # 2
        "Randy",                  # 3
        "Noｱl",                  # 4
        "Wazy",                   # 5
        "KeA",                    # 6
        "Fran",                   # 7
        "Cecil",                  # 8
        "Sully",                  # 9
        "Melson",                 # 10
        "Corona",                 # 11
        "Rimah",                  # 12
        "MWL Staff",              # 13
        "Tourist",                # 14
        "Tourist",                # 15
        "Tourist",                # 16
        "Tourist",                # 17
        "Tourist",                # 18
        "Miichie",                # 19
        "Dummy",                  # 20
        "Man",                    # 21
        "Woman",                  # 22
        "To Wonderland Entrance", # 23
    ))

    AddCharChip((
        "chr/ch00100.itc",                   # 00
        "chr/ch00200.itc",                   # 01
        "chr/ch00300.itc",                   # 02
        "chr/ch02900.itc",                   # 03
        "chr/ch03000.itc",                   # 04
        "chr/ch08200.itc",                   # 05
        "chr/ch08500.itc",                   # 06
        "chr/ch07500.itc",                   # 07
        "chr/ch10100.itc",                   # 08
        "chr/ch26200.itc",                   # 09
        "chr/ch22700.itc",                   # 0A
        "chr/ch20700.itc",                   # 0B
        "chr/ch44600.itc",                   # 0C
        "chr/ch22100.itc",                   # 0D
        "chr/ch24500.itc",                   # 0E
        "chr/ch22000.itc",                   # 0F
        "chr/ch20500.itc",                   # 10
        "chr/ch32300.itc",                   # 11
        "chr/ch03002.itc",                   # 12
        "chr/ch45400.itc",                   # 13
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

    DeclNpc(8600,    9,       4294951626, 25,   389,  0x0, 0,   0,   0,   0,   0,   0,   3,   255,  0)
    DeclNpc(2970,    3549,    4294933546, 25,   389,  0x0, 0,   1,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(4294959816, 9,       4294951916, 205,  389,  0x0, 0,   2,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(7869,    9,       4294951237, 295,  389,  0x0, 0,   3,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(11350,   200,     4294954496, 225,  389,  0x0, 0,   4,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(10130,   9,       4294950296, 115,  389,  0x0, 0,   5,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   6,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(9850,    9,       4294952286, 205,  389,  0x0, 0,   7,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(4294963306, 2309,    4294938356, 250,  389,  0x0, 0,   8,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(4294965936, 0,       4294949487, 295,  389,  0x0, 0,   9,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(4294964876, 0,       4294949647, 25,   389,  0x0, 0,   10,  0,   0,   0,   0,   13,  255,  0)
    DeclNpc(4294965017, 0,       4294950856, 160,  389,  0x0, 0,   11,  0,   0,   0,   0,   14,  255,  0)
    DeclNpc(4294966347, 0,       4294952597, 160,  389,  0x0, 0,   12,  0,   0,   0,   0,   15,  255,  0)
    DeclNpc(4294964126, 4619,    4294929377, 115,  389,  0x0, 0,   13,  0,   0,   0,   0,   16,  255,  0)
    DeclNpc(4294965146, 4739,    4294928896, 295,  389,  0x0, 0,   14,  0,   0,   0,   0,   17,  255,  0)
    DeclNpc(4294961396, 9,       4294954166, 295,  389,  0x0, 0,   15,  0,   0,   0,   0,   18,  255,  0)
    DeclNpc(4294960467, 9,       4294954746, 115,  389,  0x0, 0,   16,  0,   0,   0,   0,   19,  255,  0)
    DeclNpc(4294962266, 9,       4294949577, 25,   389,  0x0, 0,   17,  0,   0,   0,   0,   20,  255,  0)
    DeclNpc(9819,    0,       4294956736, 315,  389,  0x0, 0,   19,  0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 56,  -0.23999999463558197,  -12.220000267028809,   0.0,                   144.0,                 [0.125,                -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000001788139343,   0.0,                   0.029999999329447746,  4.073333740234375,     -0.0,                  1.0])

    DeclActor(8730,    0,       4294955966, 1000,    9820,    1500,    4294956736, 0x007E, 0,  51, 0x0000)
    DeclActor(4294961346, 0,       4294955256, 1200,    4294961346, 2000,    4294955256, 0x007C, 0,  55, 0x0000)

    PlaceName(-0.38999998569488525, 0.0, -83.0999984741211, 0x0000, 0x0000, "To Wonderland Entrance")

    ChipFrameInfo(1300, 0)                                       # 0

    ScpFunction((
        "Function_0_514",          # 00, 0
        "Function_1_5CC",          # 01, 1
        "Function_2_658",          # 02, 2
        "Function_3_6B3",          # 03, 3
        "Function_4_786",          # 04, 4
        "Function_5_843",          # 05, 5
        "Function_6_A4D",          # 06, 6
        "Function_7_B1A",          # 07, 7
        "Function_8_C4E",          # 08, 8
        "Function_9_D26",          # 09, 9
        "Function_10_EAB",         # 0A, 10
        "Function_11_F72",         # 0B, 11
        "Function_12_106A",        # 0C, 12
        "Function_13_111D",        # 0D, 13
        "Function_14_11D6",        # 0E, 14
        "Function_15_1289",        # 0F, 15
        "Function_16_13B7",        # 10, 16
        "Function_17_1410",        # 11, 17
        "Function_18_1467",        # 12, 18
        "Function_19_1530",        # 13, 19
        "Function_20_15ED",        # 14, 20
        "Function_21_1716",        # 15, 21
        "Function_22_17BC",        # 16, 22
        "Function_23_187B",        # 17, 23
        "Function_24_1942",        # 18, 24
        "Function_25_1B4B",        # 19, 25
        "Function_26_25B1",        # 1A, 26
        "Function_27_25EE",        # 1B, 27
        "Function_28_262B",        # 1C, 28
        "Function_29_2736",        # 1D, 29
        "Function_30_2798",        # 1E, 30
        "Function_31_2807",        # 1F, 31
        "Function_32_287E",        # 20, 32
        "Function_33_28E9",        # 21, 33
        "Function_34_2954",        # 22, 34
        "Function_35_299F",        # 23, 35
        "Function_36_2A10",        # 24, 36
        "Function_37_2B4F",        # 25, 37
        "Function_38_2B8D",        # 26, 38
        "Function_39_2BD5",        # 27, 39
        "Function_40_2C15",        # 28, 40
        "Function_41_3650",        # 29, 41
        "Function_42_41A6",        # 2A, 42
        "Function_43_4D8B",        # 2B, 43
        "Function_44_576D",        # 2C, 44
        "Function_45_630E",        # 2D, 45
        "Function_46_6D8F",        # 2E, 46
        "Function_47_77B7",        # 2F, 47
        "Function_48_828B",        # 30, 48
        "Function_49_8E80",        # 31, 49
        "Function_50_9891",        # 32, 50
        "Function_51_A360",        # 33, 51
        "Function_52_AB69",        # 34, 52
        "Function_53_BD60",        # 35, 53
        "Function_54_BDF6",        # 36, 54
        "Function_55_BE8C",        # 37, 55
        "Function_56_BEC7",        # 38, 56
    ))


    def Function_0_514(): pass

    label("Function_0_514")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_554"),
        (1, "loc_560"),
        (2, "loc_56C"),
        (3, "loc_578"),
        (4, "loc_584"),
        (5, "loc_590"),
        (6, "loc_59C"),
        (SWITCH_DEFAULT, "loc_5A8"),
    )


    label("loc_554")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_5B4")

    label("loc_560")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_5B4")

    label("loc_56C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_5B4")

    label("loc_578")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_5B4")

    label("loc_584")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_5B4")

    label("loc_590")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_5B4")

    label("loc_59C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_5B4")

    label("loc_5A8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_5B4")

    label("loc_5B4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5CB")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_5B4")

    label("loc_5CB")

    Return()

    # Function_0_514 end

    def Function_1_5CC(): pass

    label("Function_1_5CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_5DA")
    Jump("loc_648")

    label("loc_5DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 7)), scpexpr(EXPR_END)), "loc_5E8")
    Jump("loc_648")

    label("loc_5E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_5F6")
    Jump("loc_648")

    label("loc_5F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_607")
    Call(0, 24)
    Jump("loc_648")

    label("loc_607")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_615")
    Jump("loc_648")

    label("loc_615")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_623")
    Jump("loc_648")

    label("loc_623")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_631")
    Jump("loc_648")

    label("loc_631")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_63F")
    Jump("loc_648")

    label("loc_63F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_648")

    label("loc_648")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_657")
    ClearScenarioFlags(0x22, 0)
    Event(0, 52)

    label("loc_657")

    Return()

    # Function_1_5CC end

    def Function_2_658(): pass

    label("Function_2_658")

    OP_50(0x51, (scpexpr(EXPR_PUSH_LONG, 0xFF032877), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_F0(0x1, 0x1C2)
    Call(0, 28)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 5)), scpexpr(EXPR_END)), "loc_679")
    OP_24(0x335)
    Jump("loc_67F")

    label("loc_679")

    Sound(821, 1, 50, 0)

    label("loc_67F")

    Sound(126, 1, 80, 0)
    OP_65(0x0, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6B2")
    OP_66(0x0, 0x1)

    label("loc_6B2")

    Return()

    # Function_2_658 end

    def Function_3_6B3(): pass

    label("Function_3_6B3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6CC")
    Jump("loc_782")

    label("loc_6CC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6E2")
    Jump("loc_782")

    label("loc_6E2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_75B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_705")
    Call(0, 21)
    Jump("loc_756")

    label("loc_705")


    ChrTalk(
        0x8,
        (
            "#00102F*giggle*, I'll go buy\x01",
            "the drinks, so please,\x01",
            "take it easy and relax.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_756")

    Jump("loc_782")

    label("loc_75B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_771")
    Jump("loc_782")

    label("loc_771")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_782")

    label("loc_782")

    TalkEnd(0xFE)
    Return()

    # Function_3_6B3 end

    def Function_4_786(): pass

    label("Function_4_786")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_79F")
    Jump("loc_83F")

    label("loc_79F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_802")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7C2")
    Call(0, 22)
    Jump("loc_7FD")

    label("loc_7C2")


    ChrTalk(
        0x9,
        (
            "#00204FAs expected from Fran...\x01",
            "She catches on quick.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7FD")

    Jump("loc_83F")

    label("loc_802")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_818")
    Jump("loc_83F")

    label("loc_818")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_82E")
    Jump("loc_83F")

    label("loc_82E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_83F")

    label("loc_83F")

    TalkEnd(0xFE)
    Return()

    # Function_4_786 end

    def Function_5_843(): pass

    label("Function_5_843")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_85C")
    Jump("loc_A49")

    label("loc_85C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_872")
    Jump("loc_A49")

    label("loc_872")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_888")
    Jump("loc_A49")

    label("loc_888")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A38")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_997")

    ChrTalk(
        0xA,
        (
            "#00300FSome time ago, I tried chatting up\x01",
            "a lady coming from the Ferris wheel\x01",
            "I thought was my type, but...\x02\x03",
            "#00306FIt seems she came as a couple.\x02\x03",
            "#00302FMan. Maybe it's more difficult to\x01",
            "pick up girls at the park than I\x01",
            "thought.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_A33")

    label("loc_997")


    ChrTalk(
        0xA,
        (
            "#00306FThinkin' about it,\x01",
            "there's lots of couple\x01",
            "and family visitors...\x02\x03",
            "#00302FMaybe it's more difficult\x01",
            "to pick up girls at the\x01",
            "park than I thought.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A33")

    Jump("loc_A49")

    label("loc_A38")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A49")

    label("loc_A49")

    TalkEnd(0xFE)
    Return()

    # Function_5_843 end

    def Function_6_A4D(): pass

    label("Function_6_A4D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A66")
    Jump("loc_B16")

    label("loc_A66")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A7C")
    Jump("loc_B16")

    label("loc_A7C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A92")
    Jump("loc_B16")

    label("loc_A92")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AA8")
    Jump("loc_B16")

    label("loc_AA8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B16")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_ACB")
    Call(0, 23)
    Jump("loc_B16")

    label("loc_ACB")


    ChrTalk(
        0xB,
        (
            "#10100FOh, Lloyd. Have you\x01",
            "decided which attraction\x01",
            "you'll ride last?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B16")

    TalkEnd(0xFE)
    Return()

    # Function_6_A4D end

    def Function_7_B1A(): pass

    label("Function_7_B1A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BF7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BB3")

    ChrTalk(
        0xC,
        (
            "#10304FPeople watching like\x01",
            "this isn't bad either.\x02\x03",
            "#10302FHehe. I might find the\x01",
            "man inside Mishy\x01",
            "somewhere.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_BF2")

    label("loc_BB3")


    ChrTalk(
        0xC,
        (
            "#10302FHehe. I might find the\x01",
            "man inside Mishy\x01",
            "somewhere.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BF2")

    Jump("loc_C4A")

    label("loc_BF7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C0D")
    Jump("loc_C4A")

    label("loc_C0D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C23")
    Jump("loc_C4A")

    label("loc_C23")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C39")
    Jump("loc_C4A")

    label("loc_C39")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C4A")

    label("loc_C4A")

    TalkEnd(0xFE)
    Return()

    # Function_7_B1A end

    def Function_8_C4E(): pass

    label("Function_8_C4E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C67")
    Jump("loc_D22")

    label("loc_C67")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C7D")
    Jump("loc_D22")

    label("loc_C7D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CFB")

    ChrTalk(
        0xD,
        (
            "#01102FI knew it, this lake is\x01",
            "pretty.\x02\x03",
            "#01109FIt seems like it's clear\x01",
            "all the way to the\x01",
            "bottom.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D22")

    label("loc_CFB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D11")
    Jump("loc_D22")

    label("loc_D11")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D22")

    label("loc_D22")

    TalkEnd(0xFE)
    Return()

    # Function_8_C4E end

    def Function_9_D26(): pass

    label("Function_9_D26")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D3F")
    Jump("loc_EA7")

    label("loc_D3F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DB7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D62")
    Call(0, 22)
    Jump("loc_DB2")

    label("loc_D62")


    ChrTalk(
        0xE,
        (
            "#06409FLike Tio says, I'm sure\x01",
            "that sun face is the key\x01",
            "to its popularity!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DB2")

    Jump("loc_EA7")

    label("loc_DB7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DCD")
    Jump("loc_EA7")

    label("loc_DCD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DE3")
    Jump("loc_EA7")

    label("loc_DE3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EA7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E06")
    Call(0, 23)
    Jump("loc_EA7")

    label("loc_E06")


    ChrTalk(
        0xE,
        (
            "#06402FIt seems the view from the\x01",
            "Ferris wheel is amazing at\x01",
            "this hour.\x02\x03",
            "#06409FIf you haven't decided\x01",
            "what to ride, why not ride\x01",
            "that with someone, Lloyd?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EA7")

    TalkEnd(0xFE)
    Return()

    # Function_9_D26 end

    def Function_10_EAB(): pass

    label("Function_10_EAB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EC4")
    Jump("loc_F6E")

    label("loc_EC4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EDA")
    Jump("loc_F6E")

    label("loc_EDA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F47")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EFD")
    Call(0, 21)
    Jump("loc_F42")

    label("loc_EFD")


    ChrTalk(
        0xF,
        (
            "#05909FHaha. In that case, I\x01",
            "think I'll accept your\x01",
            "suggestion.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F42")

    Jump("loc_F6E")

    label("loc_F47")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F5D")
    Jump("loc_F6E")

    label("loc_F5D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F6E")

    label("loc_F6E")

    TalkEnd(0xFE)
    Return()

    # Function_10_EAB end

    def Function_11_F72(): pass

    label("Function_11_F72")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F8B")
    Jump("loc_1066")

    label("loc_F8B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FA1")
    Jump("loc_1066")

    label("loc_FA1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FB7")
    Jump("loc_1066")

    label("loc_FB7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1055")

    ChrTalk(
        0x10,
        (
            "#14006F*sigh*, because I played\x01",
            "around too much, I'm tired\x01",
            "now for some reason.\x02\x03",
            "#14000FI guess I'll enjoy the\x01",
            "breeze for a while.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1066")

    label("loc_1055")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1066")

    label("loc_1066")

    TalkEnd(0xFE)
    Return()

    # Function_11_F72 end

    def Function_12_106A(): pass

    label("Function_12_106A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1083")
    Jump("loc_1119")

    label("loc_1083")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10DC")

    ChrTalk(
        0x11,
        (
            "Haha, it looks like that\x01",
            "Rimah really liked the\x01",
            "Ferris wheel.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1119")

    label("loc_10DC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10F2")
    Jump("loc_1119")

    label("loc_10F2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1108")
    Jump("loc_1119")

    label("loc_1108")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1119")

    label("loc_1119")

    TalkEnd(0xFE)
    Return()

    # Function_12_106A end

    def Function_13_111D(): pass

    label("Function_13_111D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1136")
    Jump("loc_11D2")

    label("loc_1136")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1195")

    ChrTalk(
        0x12,
        (
            "My my, Rimah... There's\x01",
            "still a lot of other\x01",
            "attractions, you know?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11D2")

    label("loc_1195")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11AB")
    Jump("loc_11D2")

    label("loc_11AB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11C1")
    Jump("loc_11D2")

    label("loc_11C1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11D2")

    label("loc_11D2")

    TalkEnd(0xFE)
    Return()

    # Function_13_111D end

    def Function_14_11D6(): pass

    label("Function_14_11D6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11EF")
    Jump("loc_1285")

    label("loc_11EF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1248")

    ChrTalk(
        0x13,
        (
            "Papa, let's do another\x01",
            "round! I wanna see\x01",
            "Orchis Tower again!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1285")

    label("loc_1248")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_125E")
    Jump("loc_1285")

    label("loc_125E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1274")
    Jump("loc_1285")

    label("loc_1274")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1285")

    label("loc_1285")

    TalkEnd(0xFE)
    Return()

    # Function_14_11D6 end

    def Function_15_1289(): pass

    label("Function_15_1289")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13B3")
    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "This is the "Sunshine\x01",
            "Mole" Ferris Wheel!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "From one slow revolution of your\x01",
            "gondola, you can relax and take\x01",
            "in the best scenery in Michelam.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F(I'm playing hide-and-seek with\x01",
            "Mishette... I'll refrain from\x01",
            "visiting the attractions for now.)\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Jump("loc_13B6")

    label("loc_13B3")

    Call(0, 25)

    label("loc_13B6")

    Return()

    # Function_15_1289 end

    def Function_16_13B7(): pass

    label("Function_16_13B7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_140C")

    ChrTalk(
        0x15,
        (
            "Let's ride the Ferris\x01",
            "wheel! The view will be\x01",
            "amazing!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_140C")

    label("loc_140C")

    TalkEnd(0xFE)
    Return()

    # Function_16_13B7 end

    def Function_17_1410(): pass

    label("Function_17_1410")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1463")

    ChrTalk(
        0x16,
        (
            "I told you no! I'm\x01",
            "really not good with\x01",
            "high places!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1463")

    label("loc_1463")

    TalkEnd(0xFE)
    Return()

    # Function_17_1410 end

    def Function_18_1467(): pass

    label("Function_18_1467")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14C9")

    ChrTalk(
        0x17,
        (
            "*burp*... I've gotten\x01",
            "completely sick from the\x01",
            "gondola's swaying...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_152C")

    label("loc_14C9")


    ChrTalk(
        0x17,
        (
            "H-Hey... Can't we ride\x01",
            "something else for last?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "I really don't want to\x01",
            "get sick again...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_152C")

    TalkEnd(0xFE)
    Return()

    # Function_18_1467 end

    def Function_19_1530(): pass

    label("Function_19_1530")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1588")

    ChrTalk(
        0x18,
        (
            "Honestly, it's our long\x01",
            "awaited date, get a grip\x01",
            "already.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15E9")

    label("loc_1588")


    ChrTalk(
        0x18,
        (
            "It's fine, fine! When we see the\x01",
            "evening sun from the top,\x01",
            "getting sick won't be a problem!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15E9")

    TalkEnd(0xFE)
    Return()

    # Function_19_1530 end

    def Function_20_15ED(): pass

    label("Function_20_15ED")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1678")

    ChrTalk(
        0x19,
        (
            "You need quite a bit of\x01",
            "courage to ride the\x01",
            "Ferris wheel alone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "...I should've come with\x01",
            "a male friend.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1712")

    label("loc_1678")


    ChrTalk(
        0x19,
        (
            "The view from the top was\x01",
            "great. Mustering my courage and\x01",
            "riding it was the right choice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "Well, riding alone was\x01",
            "sad for some reason,\x01",
            "though...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1712")

    TalkEnd(0xFE)
    Return()

    # Function_20_15ED end

    def Function_21_1716(): pass

    label("Function_21_1716")

    OP_4B(0x8, 0xFF)
    OP_4B(0xF, 0xFF)

    ChrTalk(
        0x8,
        (
            "#00100FThen, I'll go buy\x01",
            "something to drink.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#05905FOh, but no. I'll go\x01",
            "instead.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#00102F*giggle*, Cecil, please\x01",
            "take it easy here.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    OP_4C(0x8, 0xFF)
    OP_4C(0xF, 0xFF)
    Return()

    # Function_21_1716 end

    def Function_22_17BC(): pass

    label("Function_22_17BC")

    OP_4B(0x9, 0xFF)
    OP_4B(0xE, 0xFF)

    ChrTalk(
        0x9,
        (
            "#00204FAs expected, the Ferris\x01",
            "wheel seems popular.\x02\x03",
            "#00200FThe sun face at its\x01",
            "center... Could that be\x01",
            "the decisive factor?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#06409FAhaha, it must be!\x02",
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)
    OP_4C(0xE, 0xFF)
    SetScenarioFlags(0x0, 1)
    ClearChrFlags(0x9, 0x10)
    ClearChrFlags(0xE, 0x10)
    Return()

    # Function_22_17BC end

    def Function_23_187B(): pass

    label("Function_23_187B")

    OP_4B(0xB, 0xFF)
    OP_4B(0xE, 0xFF)

    ChrTalk(
        0xE,
        (
            "#06400FAccording to the guide book,\x01",
            "the view from the Ferris wheel\x01",
            "at this hour is amazing!\x02\x03",
            "#06409FNoｱl, let's ride it later!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#10100FHaha. I guess we should.\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0xE, 0x10)
    SetScenarioFlags(0x0, 2)
    OP_4C(0xB, 0xFF)
    OP_4C(0xE, 0xFF)
    Return()

    # Function_23_187B end

    def Function_24_1942(): pass

    label("Function_24_1942")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_19A7")
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
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)

    label("loc_19A7")

    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x10)
    ClearChrFlags(0x16, 0x80)
    SetChrFlags(0x16, 0x10)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    SetChrFlags(0x18, 0x10)
    ClearChrFlags(0x19, 0x80)
    SetChrFlags(0x1A, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A05")
    ClearChrFlags(0xC, 0x80)
    SetChrChipByIndex(0xC, 0x12)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    Jump("loc_1B4A")

    label("loc_1A05")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A5E")
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x10)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 3970, 3590, -33910, 25)
    SetChrFlags(0xE, 0x10)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x10)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x10)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x10)
    Jump("loc_1B4A")

    label("loc_1A5E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A8D")
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x10)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x10)
    Jump("loc_1B4A")

    label("loc_1A8D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B05")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x10, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1AE5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 1)), scpexpr(EXPR_END)), "loc_1AD7")
    SetChrFlags(0xA, 0x80)
    Jump("loc_1AE5")

    label("loc_1AD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 1)), scpexpr(EXPR_END)), "loc_1AE5")
    SetChrFlags(0x10, 0x80)

    label("loc_1AE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1B00")
    ClearChrFlags(0x1A, 0x80)

    label("loc_1B00")

    Jump("loc_1B4A")

    label("loc_1B05")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B4A")
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x10)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 6760, 10, -15090, 115)
    SetChrFlags(0xE, 0x10)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x10)

    label("loc_1B4A")

    Return()

    # Function_24_1942 end

    def Function_25_1B4B(): pass

    label("Function_25_1B4B")

    EventBegin(0x0)
    Fade(500)
    OP_68(-950, 1300, -15300, 0)
    MoveCamera(45, 24, 0, 0)
    OP_6E(1000, 0)
    SetCameraDistance(8500, 0)
    OP_4B(0x14, 0xFF)
    SetChrPos(0x101, -950, 0, -16000, 0)
    Call(0, 26)
    OP_0D()

    ChrTalk(
        0x14,
        (
            "This is the "Sunshine\x01",
            "Mole" Ferris Wheel!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "From one slow revolution of your\x01",
            "gondola, you can relax and take\x01",
            "in the best scenery in Michelam.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "If you like, how about\x01",
            "taking someone along?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#12P(Who should I\x01",
            "invite...?)\x02",
        )
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
    MenuCmd(1, 0, "Cancel")
    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_1D46")
    MenuCmd(3, 0, 0x0)

    label("loc_1D46")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_1D58")
    MenuCmd(3, 0, 0x1)

    label("loc_1D58")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_1D6A")
    MenuCmd(3, 0, 0x2)

    label("loc_1D6A")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_1D7C")
    MenuCmd(3, 0, 0x3)

    label("loc_1D7C")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_1D8E")
    MenuCmd(3, 0, 0x4)

    label("loc_1D8E")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x20), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_1DA0")
    MenuCmd(3, 0, 0x5)

    label("loc_1DA0")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x40), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_1DB2")
    MenuCmd(3, 0, 0x6)

    label("loc_1DB2")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_1DC4")
    MenuCmd(3, 0, 0x7)

    label("loc_1DC4")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x100), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_1DD6")
    MenuCmd(3, 0, 0x8)

    label("loc_1DD6")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x200), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_1DE8")
    MenuCmd(3, 0, 0x9)

    label("loc_1DE8")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x400), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_1DFA")
    MenuCmd(3, 0, 0xA)

    label("loc_1DFA")

    MenuCmd(2, 0, -1, 55, 0)
    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2545")
    OP_D2(0x5, (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1E80"),
        (1, "loc_1EBD"),
        (2, "loc_1EF9"),
        (3, "loc_1F37"),
        (4, "loc_1F74"),
        (5, "loc_1FB1"),
        (6, "loc_1FED"),
        (7, "loc_202A"),
        (8, "loc_2068"),
        (9, "loc_20A5"),
        (10, "loc_20E3"),
        (SWITCH_DEFAULT, "loc_2121"),
    )


    label("loc_1E80")

    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        (
            "#00000F#12P(Alright... I'll invite\x01",
            "Elie.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2121")

    label("loc_1EBD")

    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        (
            "#00000F#12P(Alright... I'll invite\x01",
            "Tio.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2121")

    label("loc_1EF9")

    OP_50(0x67, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        (
            "#00000F#12P(Alright... I'll invite\x01",
            "Randy.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2121")

    label("loc_1F37")

    OP_50(0x68, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        (
            "#00000F#12P(Alright... I'll invite\x01",
            "Noｱl.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2121")

    label("loc_1F74")

    OP_50(0x69, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        (
            "#00000F#12P(Alright... I'll invite\x01",
            "Wazy.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2121")

    label("loc_1FB1")

    OP_50(0x64, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        (
            "#00000F#12P(Alright... I'll invite\x01",
            "KeA.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2121")

    label("loc_1FED")

    OP_50(0x6E, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        (
            "#00000F#12P(Alright... I'll invite\x01",
            "Fran.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2121")

    label("loc_202A")

    OP_50(0x6D, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        (
            "#00000F#12P(Alright... I'll invite\x01",
            "Cecil.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2121")

    label("loc_2068")

    OP_50(0x6C, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        (
            "#00000F#12P(Alright... I'll invite\x01",
            "Ilya.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2121")

    label("loc_20A5")

    OP_50(0x6A, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        (
            "#00000F#12P(Alright... I'll invite\x01",
            "Rixia.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2121")

    label("loc_20E3")

    OP_50(0x6F, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        (
            "#00000F#12P(Alright... I'll invite\x01",
            "Sully.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2121")

    label("loc_2121")

    FadeToDark(500, 0, -1)
    OP_0D()
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch05100.itc", 0x20)
    LoadChrToIndex("chr/ch05200.itc", 0x21)
    LoadChrToIndex("apl/ch51356.itc", 0x22)
    LoadChrToIndex("chr/ch10000.itc", 0x23)
    SoundLoad(148)
    ClearChrFlags(0x1B, 0x80)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_219E"),
        (1, "loc_21AD"),
        (2, "loc_21BC"),
        (3, "loc_21CB"),
        (4, "loc_21DA"),
        (5, "loc_21E3"),
        (6, "loc_21F2"),
        (7, "loc_2201"),
        (8, "loc_2210"),
        (9, "loc_221F"),
        (10, "loc_222E"),
        (SWITCH_DEFAULT, "loc_223D"),
    )


    label("loc_219E")

    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    SetChrChipByIndex(0x1B, 0x0)
    Jump("loc_223D")

    label("loc_21AD")

    LoadChrToIndex("chr/ch00202.itc", 0x1F)
    SetChrChipByIndex(0x1B, 0x1)
    Jump("loc_223D")

    label("loc_21BC")

    LoadChrToIndex("chr/ch00302.itc", 0x1F)
    SetChrChipByIndex(0x1B, 0x2)
    Jump("loc_223D")

    label("loc_21CB")

    LoadChrToIndex("chr/ch02902.itc", 0x1F)
    SetChrChipByIndex(0x1B, 0x3)
    Jump("loc_223D")

    label("loc_21DA")

    SetChrChipByIndex(0x1B, 0x4)
    Jump("loc_223D")

    label("loc_21E3")

    LoadChrToIndex("chr/ch08202.itc", 0x1F)
    SetChrChipByIndex(0x1B, 0x5)
    Jump("loc_223D")

    label("loc_21F2")

    LoadChrToIndex("chr/ch08502.itc", 0x1F)
    SetChrChipByIndex(0x1B, 0x6)
    Jump("loc_223D")

    label("loc_2201")

    LoadChrToIndex("chr/ch07502.itc", 0x1F)
    SetChrChipByIndex(0x1B, 0x7)
    Jump("loc_223D")

    label("loc_2210")

    LoadChrToIndex("chr/ch05102.itc", 0x1F)
    SetChrChipByIndex(0x1B, 0x20)
    Jump("loc_223D")

    label("loc_221F")

    LoadChrToIndex("chr/ch05202.itc", 0x1F)
    SetChrChipByIndex(0x1B, 0x21)
    Jump("loc_223D")

    label("loc_222E")

    LoadChrToIndex("chr/ch10002.itc", 0x1F)
    SetChrChipByIndex(0x1B, 0x8)
    Jump("loc_223D")

    label("loc_223D")

    SetChrSubChip(0x1B, 0x0)
    SetChrPos(0x101, -950, 0, -16000, 0)
    SetChrPos(0x1B, -250, 0, -16700, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x14,
        (
            "I'll hold on to your\x01",
            "ticket, then.\x02",
        )
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
            "Gave the staffer a\x01",
            "ticket.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x14,
        "Two people, coming in!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrChipByIndex(0x101, 0x1E)
    Jc((scpexpr(EXPR_23, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2334")
    SetChrChipByIndex(0x1B, 0x12)
    Jump("loc_2338")

    label("loc_2334")

    SetChrChipByIndex(0x1B, 0x1F)

    label("loc_2338")

    SetChrFlags(0x101, 0x4)
    SetChrPos(0x101, 999000, 200, 0, 90)
    SetChrPos(0x1B, 1001000, 200, 0, 270)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_23AB"),
        (1, "loc_23B3"),
        (2, "loc_23BB"),
        (3, "loc_23C3"),
        (4, "loc_23CB"),
        (5, "loc_23D3"),
        (6, "loc_23DB"),
        (7, "loc_23E3"),
        (8, "loc_23EB"),
        (9, "loc_23F3"),
        (10, "loc_23FB"),
        (SWITCH_DEFAULT, "loc_2403"),
    )


    label("loc_23AB")

    Call(0, 40)
    Jump("loc_2403")

    label("loc_23B3")

    Call(0, 41)
    Jump("loc_2403")

    label("loc_23BB")

    Call(0, 42)
    Jump("loc_2403")

    label("loc_23C3")

    Call(0, 43)
    Jump("loc_2403")

    label("loc_23CB")

    Call(0, 44)
    Jump("loc_2403")

    label("loc_23D3")

    Call(0, 45)
    Jump("loc_2403")

    label("loc_23DB")

    Call(0, 46)
    Jump("loc_2403")

    label("loc_23E3")

    Call(0, 47)
    Jump("loc_2403")

    label("loc_23EB")

    Call(0, 48)
    Jump("loc_2403")

    label("loc_23F3")

    Call(0, 49)
    Jump("loc_2403")

    label("loc_23FB")

    Call(0, 50)
    Jump("loc_2403")

    label("loc_2403")

    SetChrFlags(0x1B, 0x80)
    OP_49()
    OP_D7(0x1E)
    Jc((scpexpr(EXPR_23, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_241B")
    OP_D7(0x1F)

    label("loc_241B")

    OP_D7(0x20)
    OP_D7(0x21)
    OP_D7(0x22)
    OP_D7(0x23)
    Switch(
        (scpexpr(EXPR_23, 0x5), scpexpr(EXPR_END)),
        (0, "loc_246E"),
        (1, "loc_247C"),
        (2, "loc_248A"),
        (3, "loc_2498"),
        (4, "loc_24A6"),
        (5, "loc_24B4"),
        (6, "loc_24C2"),
        (7, "loc_24D0"),
        (8, "loc_24DE"),
        (9, "loc_24EC"),
        (10, "loc_24FA"),
        (SWITCH_DEFAULT, "loc_2508"),
    )


    label("loc_246E")

    OP_D2(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_2508")

    label("loc_247C")

    OP_D2(0x3, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_2508")

    label("loc_248A")

    OP_D2(0x3, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_2508")

    label("loc_2498")

    OP_D2(0x3, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_2508")

    label("loc_24A6")

    OP_D2(0x3, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_2508")

    label("loc_24B4")

    OP_D2(0x3, (scpexpr(EXPR_PUSH_LONG, 0x20), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_2508")

    label("loc_24C2")

    OP_D2(0x3, (scpexpr(EXPR_PUSH_LONG, 0x40), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_2508")

    label("loc_24D0")

    OP_D2(0x3, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_2508")

    label("loc_24DE")

    OP_D2(0x3, (scpexpr(EXPR_PUSH_LONG, 0x100), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_2508")

    label("loc_24EC")

    OP_D2(0x3, (scpexpr(EXPR_PUSH_LONG, 0x200), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_2508")

    label("loc_24FA")

    OP_D2(0x3, (scpexpr(EXPR_PUSH_LONG, 0x400), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_2508")

    label("loc_2508")

    OP_D2(0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2540")
    StopSound(821, 1000, 40)
    StopSound(126, 1000, 70)
    StopBGM(0xFA0)
    WaitBGM()
    SetScenarioFlags(0x22, 1)
    NewScene("t1300", 0, 0, 0)
    IdleLoop()

    label("loc_2540")

    Jump("loc_2596")

    label("loc_2545")


    ChrTalk(
        0x14,
        (
            "Oh, did you change your\x01",
            "mind?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "We'll be waiting for\x01",
            "your next visit!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_2596")

    Call(0, 27)
    OP_4C(0x14, 0xFF)
    SetChrPos(0x0, 0, 0, -16500, 180)
    EventEnd(0x5)
    Return()

    # Function_25_1B4B end

    def Function_26_25B1(): pass

    label("Function_26_25B1")

    SetChrFlags(0xC, 0x8)
    SetChrFlags(0x9, 0x8)
    SetChrFlags(0xE, 0x8)
    SetChrFlags(0x8, 0x8)
    SetChrFlags(0xD, 0x8)
    SetChrFlags(0xF, 0x8)
    SetChrFlags(0xA, 0x8)
    SetChrFlags(0x10, 0x8)
    SetChrFlags(0xB, 0x8)
    SetChrFlags(0x11, 0x8)
    SetChrFlags(0x12, 0x8)
    SetChrFlags(0x13, 0x8)
    Return()

    # Function_26_25B1 end

    def Function_27_25EE(): pass

    label("Function_27_25EE")

    ClearChrFlags(0xC, 0x8)
    ClearChrFlags(0x9, 0x8)
    ClearChrFlags(0xE, 0x8)
    ClearChrFlags(0x8, 0x8)
    ClearChrFlags(0xD, 0x8)
    ClearChrFlags(0xF, 0x8)
    ClearChrFlags(0xA, 0x8)
    ClearChrFlags(0x10, 0x8)
    ClearChrFlags(0xB, 0x8)
    ClearChrFlags(0x11, 0x8)
    ClearChrFlags(0x12, 0x8)
    ClearChrFlags(0x13, 0x8)
    Return()

    # Function_27_25EE end

    def Function_28_262B(): pass

    label("Function_28_262B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_26CC")
    SetMapObjFrame(0xFF, "sky01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky_y", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky01_y", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky_in", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky01_in", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky_y_in", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky01_y_in", 0x1, 0x1)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xD5, 0x8F, 0x7B, 0x26, 0x1F4, 0x0)
    Jump("loc_2735")

    label("loc_26CC")

    SetMapObjFrame(0xFF, "sky01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky_y", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky01_y", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky_in", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky01_in", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky_y_in", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky01_y_in", 0x0, 0x1)

    label("loc_2735")

    Return()

    # Function_28_262B end

    def Function_29_2736(): pass

    label("Function_29_2736")

    Sleep(500)
    FadeToBright(1000, 0)
    OP_68(-11850, 18700, -640, 0)
    OP_68(-11850, 21700, -640, 5000)
    MoveCamera(35, 22, 0, 0)
    OP_6E(1000, 0)
    SetCameraDistance(26940, 0)
    OP_0D()
    Sleep(3000)
    StopSound(126, 1000, 70)
    StopSound(821, 1000, 40)
    VolumeBGM(0x46, 0x1F4)
    Return()

    # Function_29_2736 end

    def Function_30_2798(): pass

    label("Function_30_2798")

    StopSound(148, 500, 70)
    Sound(821, 2, 50, 0)
    Sound(126, 2, 80, 0)
    VolumeBGM(0x64, 0x1F4)
    FadeToBright(1000, 0)
    OP_68(1020, 38900, 2930, 0)
    MoveCamera(330, 11, 0, 0)
    OP_6E(1000, 0)
    SetCameraDistance(31100, 0)
    SetCameraDistance(28100, 5000)
    OP_0D()
    Sleep(3000)
    StopSound(126, 1000, 70)
    StopSound(821, 1000, 40)
    VolumeBGM(0x46, 0x1F4)
    Return()

    # Function_30_2798 end

    def Function_31_2807(): pass

    label("Function_31_2807")

    StopSound(148, 500, 70)
    Sound(821, 2, 50, 0)
    Sound(126, 2, 80, 0)
    VolumeBGM(0x64, 0x1F4)
    FadeToBright(1000, 0)
    OP_68(11580, 21300, -1090, 0)
    OP_68(11580, 18300, -1090, 5000)
    MoveCamera(331, 30, 0, 0)
    OP_6E(1000, 0)
    SetCameraDistance(26940, 0)
    OP_0D()
    Sleep(3000)
    StopSound(126, 1000, 70)
    StopSound(821, 1000, 40)
    VolumeBGM(0x46, 0x1F4)
    Return()

    # Function_31_2807 end

    def Function_32_287E(): pass

    label("Function_32_287E")

    Sound(148, 2, 80, 0)
    Fade(1000)
    SetMapObjFrame(0xFF, "Null_in", 0x2, "loop00")
    OP_68(1000000, 1350, 0, 0)
    Jc((scpexpr(EXPR_23, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_28CA")
    MoveCamera(30, 23, 0, 0)
    Jump("loc_28D5")

    label("loc_28CA")

    MoveCamera(45, 23, 0, 0)

    label("loc_28D5")

    OP_6E(600, 0)
    SetCameraDistance(11000, 0)
    OP_0D()
    Return()

    # Function_32_287E end

    def Function_33_28E9(): pass

    label("Function_33_28E9")

    Sound(148, 2, 80, 0)
    Fade(1000)
    SetMapObjFrame(0xFF, "Null_in", 0x2, "loop01")
    OP_68(1000000, 1350, 0, 0)
    Jc((scpexpr(EXPR_23, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2935")
    MoveCamera(30, 23, 0, 0)
    Jump("loc_2940")

    label("loc_2935")

    MoveCamera(45, 23, 0, 0)

    label("loc_2940")

    OP_6E(600, 0)
    SetCameraDistance(11000, 0)
    OP_0D()
    Return()

    # Function_33_28E9 end

    def Function_34_2954(): pass

    label("Function_34_2954")

    Sound(148, 2, 80, 0)
    Fade(1000)
    SetMapObjFrame(0xFF, "Null_in", 0x2, "goal")
    OP_68(1000000, 1350, 0, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(11000, 0)
    OP_0D()
    Return()

    # Function_34_2954 end

    def Function_35_299F(): pass

    label("Function_35_299F")

    Sleep(500)
    SetChrPos(0x101, 400, 0, -15500, 90)
    SetChrPos(0x1B, 1600, 0, -15500, 270)
    FadeToBright(1000, 0)
    OP_68(1100, 1700, -15500, 0)
    OP_68(1100, 1300, -15500, 2500)
    MoveCamera(45, 24, 0, 0)
    OP_6E(1000, 0)
    SetCameraDistance(7500, 0)
    OP_6F(0x79)
    OP_0D()
    Return()

    # Function_35_299F end

    def Function_36_2A10(): pass

    label("Function_36_2A10")

    Fade(250)
    Sound(812, 0, 100, 0)
    ClearChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2A74"),
        (1, "loc_2A7D"),
        (2, "loc_2A86"),
        (3, "loc_2A8F"),
        (4, "loc_2A98"),
        (5, "loc_2AA1"),
        (6, "loc_2AAA"),
        (7, "loc_2AB3"),
        (8, "loc_2ABC"),
        (9, "loc_2AC5"),
        (10, "loc_2ACE"),
        (SWITCH_DEFAULT, "loc_2AD7"),
    )


    label("loc_2A74")

    SetChrChipByIndex(0x1B, 0x0)
    Jump("loc_2AD7")

    label("loc_2A7D")

    SetChrChipByIndex(0x1B, 0x1)
    Jump("loc_2AD7")

    label("loc_2A86")

    SetChrChipByIndex(0x1B, 0x2)
    Jump("loc_2AD7")

    label("loc_2A8F")

    SetChrChipByIndex(0x1B, 0x3)
    Jump("loc_2AD7")

    label("loc_2A98")

    SetChrChipByIndex(0x1B, 0x4)
    Jump("loc_2AD7")

    label("loc_2AA1")

    SetChrChipByIndex(0x1B, 0x5)
    Jump("loc_2AD7")

    label("loc_2AAA")

    SetChrChipByIndex(0x1B, 0x6)
    Jump("loc_2AD7")

    label("loc_2AB3")

    SetChrChipByIndex(0x1B, 0x7)
    Jump("loc_2AD7")

    label("loc_2ABC")

    SetChrChipByIndex(0x1B, 0x20)
    Jump("loc_2AD7")

    label("loc_2AC5")

    SetChrChipByIndex(0x1B, 0x21)
    Jump("loc_2AD7")

    label("loc_2ACE")

    SetChrChipByIndex(0x1B, 0x23)
    Jump("loc_2AD7")

    label("loc_2AD7")

    SetChrSubChip(0x1B, 0x0)
    SetChrPos(0x101, 999300, 0, 0, 90)
    SetChrPos(0x1B, 1000700, 0, 0, 270)
    OP_0D()
    BeginChrThread(0x101, 3, 0, 37)
    BeginChrThread(0x1B, 3, 0, 38)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    WaitChrThread(0x101, 3)
    WaitChrThread(0x1B, 3)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x1B, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    StopSound(148, 500, 70)
    Sound(821, 2, 50, 0)
    Sound(126, 2, 80, 0)
    VolumeBGM(0x64, 0x1F4)
    Return()

    # Function_36_2A10 end

    def Function_37_2B4F(): pass

    label("Function_37_2B4F")

    OP_93(0xFE, 0xB4, 0x1F4)

    def lambda_2B5B():
        OP_96(0xFE, 0xF4240, 0x0, 0xFFFFF9C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2B5B)
    Sleep(500)

    def lambda_2B78():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2B78)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_37_2B4F end

    def Function_38_2B8D(): pass

    label("Function_38_2B8D")

    OP_93(0xFE, 0xE1, 0x1F4)
    Sleep(600)
    OP_93(0xFE, 0xB4, 0x1F4)

    def lambda_2BA3():
        OP_96(0xFE, 0xF4240, 0x0, 0xFFFFF9C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2BA3)
    Sleep(500)

    def lambda_2BC0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2BC0)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_38_2B8D end

    def Function_39_2BD5(): pass

    label("Function_39_2BD5")


    def lambda_2BDA():
        OP_93(0xFE, 0xB4, 0xC8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2BDA)
    OP_93(0x1B, 0xB4, 0x1F4)

    def lambda_2BEE():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_2BEE)
    Sleep(500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    WaitChrThread(0x1B, 1)
    EndChrThread(0x101, 0x2)
    Return()

    # Function_39_2BD5 end

    def Function_40_2C15(): pass

    label("Function_40_2C15")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu00101.itp")
    Call(0, 29)
    SetChrSubChip(0x1B, 0x2)
    SetChrSubChip(0x101, 0x1)
    Call(0, 32)

    NpcTalk(
        0x1B,
        "Elie",
        (
            "#00105FThe gondola keeps going\x01",
            "higher and higher...\x02\x03",
            "#00102F*giggle*, I've somehow\x01",
            "gotten tense.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7FF), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D74")

    ChrTalk(
        0x101,
        (
            "#00002F#6PYeah. This is my first time\x01",
            "on a Ferris wheel too, and\x01",
            "my heart is pounding.\x02\x03",
            "#00005F...Wait, haven't you been\x01",
            "to the theme park before,\x01",
            "Elie?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E20")

    label("loc_2D74")


    ChrTalk(
        0x101,
        (
            "#00000F#6PYeah. This isn't my first time\x01",
            "on the Ferris wheel, but my\x01",
            "heart's pounding just the same.\x02\x03",
            "#00005F...Wait, haven't you been to\x01",
            "the theme park before, Elie?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E20")

    SetChrSubChip(0x1B, 0x0)

    NpcTalk(
        0x1B,
        "Elie",
        (
            "#00104FI have, but...\x02\x03",
            "#00100FI visited other\x01",
            "attractions the last\x01",
            "time I came.\x02\x03",
            "#00106FThere really are too\x01",
            "many attractions to see\x01",
            "in just one day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#6PI see, so that's why.\x02\x03",
            "#00009FHaha. Then let's enjoy\x01",
            "this.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Elie",
        (
            "#00102FYes. I wonder how the\x01",
            "view is at the top...\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 30)
    SetChrSubChip(0x1B, 0x2)
    SetChrSubChip(0x101, 0x1)
    Call(0, 33)

    NpcTalk(
        0x1B,
        "Elie",
        "#00102FMy... Look, Lloyd.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#6PYeah... What an amazing\x01",
            "view.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_31C1")

    NpcTalk(
        0x1B,
        "Elie",
        (
            "#00109FIt really is. The lake\x01",
            "is dyed in the red of\x01",
            "the sunset...\x02\x03",
            "#00104F*sigh*... It makes you\x01",
            "sigh unconsciously.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#6PYeah... It seems we rode\x01",
            "at the perfect time.\x02\x03",
            "#00009FSaving my last ticket\x01",
            "for this was the right\x01",
            "choice.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("Elie")

    AnonymousTalk(
        0xFF,
        (
            "Haha. Thank you for inviting me,\x01",
            "Lloyd.\x02\x03",
            "This was a view I won't forget\x01",
            "anytime soon.\x02",
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
        "#00000F#6PHaha, you're welcome.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3271")

    label("loc_31C1")


    NpcTalk(
        0x1B,
        "Elie",
        (
            "#00102FYes, indeed. The sun is\x01",
            "reflecting off the lake,\x01",
            "and it's sparkling...\x02\x03",
            "#00104F*sigh*... It makes you\x01",
            "sigh unconsciously.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#6PHaha, it really does.\x02",
    )

    CloseMessageWindow()

    label("loc_3271")

    SetChrSubChip(0x1B, 0x0)
    Sleep(300)
    OP_63(0x1B, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    NpcTalk(
        0x1B,
        "Elie",
        "#00105F...Ah...\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x1B, 0x2)
    OP_63(0x1B, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)
    SetChrSubChip(0x101, 0x0)
    OP_63(0x101, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005F#6PElie, what's wrong?\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Elie",
        (
            "#00112FN-No, I mean...\x02\x03",
            "#00113FThe couple riding in the\x01",
            "next gondola...\x02\x03",
            "They're, umm, kis...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#6PHuh?\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    Sleep(500)
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x101, 0x0)
    OP_63(0x101, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00012F#6PH-Haha... Um. They're in\x01",
            "love, huh.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x1B, 0x0)

    NpcTalk(
        0x1B,
        "Elie",
        (
            "#00109FA-Ahaha... right. I heard\x01",
            "this attraction was\x01",
            "popular with couples.\x02\x03",
            "#00106F#1SM-Maybe it looks like we\x01",
            "have that kind of\x01",
            "relationship...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#6PHuh?\x02",
    )

    CloseMessageWindow()
    OP_63(0x1B, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    NpcTalk(
        0x1B,
        "Elie",
        (
            "#00109FN-No, nevermind.\x01",
            "Ohohoho...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#6PA-Ahaha... (Somehow the\x01",
            "mood became awkward.)\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    Call(0, 31)
    Call(0, 34)
    Sleep(3000)

    ChrTalk(
        0x101,
        "#00000F#6P...We're almost there.\x05\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Elie",
        "#00100FYes. Shall we get off?\x05\x02",
    )

    CloseMessageWindow()
    Call(0, 36)
    Call(0, 28)
    Call(0, 24)
    Call(0, 35)

    NpcTalk(
        0x1B,
        "Elie",
        (
            "#00100F#11P*giggle*, thank you\x01",
            "Lloyd. I had fun riding\x01",
            "with you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#6PYeah. I'm glad I invited\x01",
            "you.\x02\x03",
            "Ok, see you later.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Elie",
        "#00100F#11PYes, later.\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x1B, 3, 0, 39)
    WaitChrThread(0x1B, 3)
    Return()

    # Function_40_2C15 end

    def Function_41_3650(): pass

    label("Function_41_3650")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu00201.itp")
    Call(0, 29)
    SetChrSubChip(0x1B, 0x2)
    SetChrSubChip(0x101, 0x1)
    Call(0, 32)

    NpcTalk(
        0x1B,
        "Tio",
        (
            "#00203FHmm. What kind of\x01",
            "situation is this, I\x01",
            "wonder.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x101,
        "#00005F#6PHuh? What is it?\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x1B, 0x0)

    NpcTalk(
        0x1B,
        "Tio",
        (
            "#00203FMy first trip to a theme\x01",
            "park, all alone with you\x01",
            "on the Ferris wheel...\x02\x03",
            "#00200FI was thinking it's a\x01",
            "very special situation.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7FF), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3840")

    ChrTalk(
        0x101,
        (
            "#00012F#6PHaha, sorry. It's my first\x01",
            "time on a ferris wheel, so\x01",
            "I'm a little nervous.\x02\x03",
            "#00006FNow that you say that, it\x01",
            "might have been fun to\x01",
            "invite more people.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38B0")

    label("loc_3840")


    ChrTalk(
        0x101,
        (
            "#00003F#6PHmm. It is, now that you\x01",
            "mention it.\x02\x03",
            "#00012FWell, it might have been\x01",
            "fun to invite more\x01",
            "people.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38B0")


    NpcTalk(
        0x1B,
        "Tio",
        (
            "#00211FThat's not what I meant,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    NpcTalk(
        0x1B,
        "Tio",
        (
            "#00202FWhatever. We don't get\x01",
            "chances like this often, so\x01",
            "let's talk about some things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#6PHaha, yeah.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 30)
    Call(0, 33)

    NpcTalk(
        0x1B,
        "Tio",
        (
            "#00203F...In short, Mishy's cuteness is\x01",
            "summarized in those 8 points... and\x01",
            "that's no exaggeration.\x02\x03",
            "#00201FIn this day in age, I'm sure it's only\x01",
            "a matter of time before people begin\x01",
            "to specialize in this as a career.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00012F#6PU-Uh, Tio? We're almost\x01",
            "at the top.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1B, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    NpcTalk(
        0x1B,
        "Tio",
        (
            "#00205F...I lost track of time.\x02\x03",
            "#00204FThen, I'll give you the\x01",
            "rest later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#6P(When did this become a\x01",
            "lecture!?)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1B, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3DA5")
    SetChrSubChip(0x1B, 0x2)

    NpcTalk(
        0x1B,
        "Tio",
        (
            "#00205F...How pretty... That vast\x01",
            "Elm Lake is dyed a deep\x01",
            "red.\x02\x03",
            "#00204FI feel it has a different\x01",
            "character than what can be\x01",
            "seen from Waterfront Area.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)

    ChrTalk(
        0x101,
        (
            "#00000F#6PYeah... It seems we rode\x01",
            "at the perfect time.\x02\x03",
            "#00009FSaving my last ticket\x01",
            "for this was the right\x01",
            "choice.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("Tio")

    AnonymousTalk(
        0xFF,
        (
            "Thank you for inviting me, Lloyd.\x02\x03",
            "I think this scenery will make a\x01",
            "very nice memory.\x02",
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
        "#00000F#6PHaha, you're welcome.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3F23")

    label("loc_3DA5")

    SetChrSubChip(0x1B, 0x1)

    NpcTalk(
        0x1B,
        "Tio",
        (
            "#00205FLloyd, look towards the\x01",
            "central square.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    ChrTalk(
        0x101,
        (
            "#00005F#6POh, you can see Mishy's\x01",
            "face in the flower bed.\x02\x03",
            "#00009FHaha. Seeing that makes\x01",
            "me feel like we're\x01",
            "really here.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Tio",
        (
            "#00202FHaha, that's true.\x02\x03",
            "#00204FI want to plant a garden\x01",
            "just like that it on the\x01",
            "Support Section's roof.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#6PG-Give me a break. I\x01",
            "don't think we're that\x01",
            "unique a post.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F23")

    SetChrSubChip(0x1B, 0x0)

    NpcTalk(
        0x1B,
        "Tio",
        (
            "#00203F...Ahem, then while I'm in the mood,\x01",
            "let's return to the second half of\x01",
            "the lecture, shall we?\x02\x03",
            "#00201FIt was said not too long ago that\x01",
            "Mishy's cuteness is in his eyebrows,\x01",
            "but according to current research...\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00006F#6P(Looks like I'll have to\x01",
            "put up with this until\x01",
            "we get off...)\x02\x03",
            "#00012F(Well, it seems fun, so\x01",
            "why not.)\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    Call(0, 31)
    Call(0, 34)
    Sleep(3000)

    ChrTalk(
        0x101,
        "#00000F#6P...We're almost there.\x05\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Tio",
        "#00200FYeah, let's get off.\x02",
    )

    CloseMessageWindow()
    Call(0, 36)
    Call(0, 28)
    Call(0, 24)
    Call(0, 35)

    NpcTalk(
        0x1B,
        "Tio",
        (
            "#00200FThanks, Lloyd. That was\x01",
            "fun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#6PYeah. I'm glad I invited\x01",
            "you.\x02\x03",
            "Ok, see you later.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Tio",
        "#00200FYes, later.\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x1B, 3, 0, 39)
    WaitChrThread(0x1B, 3)
    Return()

    # Function_41_3650 end

    def Function_42_41A6(): pass

    label("Function_42_41A6")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu00301.itp")
    Call(0, 29)
    SetChrSubChip(0x1B, 0x2)
    SetChrSubChip(0x101, 0x1)
    Call(0, 32)
    Sleep(500)
    SetChrSubChip(0x1B, 0x0)

    NpcTalk(
        0x1B,
        "Randy",
        (
            "#00306F*sigh*. Never thought\x01",
            "I'd be stuck on a Ferris\x01",
            "wheel with another dude.\x02\x03",
            "#00301FLloyd, seriously... You\x01",
            "aren't aimin' for me,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7FF), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_43A5")

    ChrTalk(
        0x101,
        (
            "#00006F#6PHey now... I don't swing that\x01",
            "way.\x02\x03",
            "#00000FIt's just, you've been here\x01",
            "before, so you must know many\x01",
            "things about the theme park.\x02\x03",
            "#00002FI was thinking I'd be able to\x01",
            "100% enjoy my first view from\x01",
            "the top of a Ferris wheel.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_448B")

    label("loc_43A5")


    ChrTalk(
        0x101,
        (
            "#00006F#6PHey now... I don't swing that\x01",
            "way.\x02\x03",
            "#00000FIt's just, you've been here\x01",
            "before, so you must know many\x01",
            "things about the theme park.\x02\x03",
            "#00002FI was thinking I'd be able to\x01",
            "make a new discovery in the\x01",
            "view from the top.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_448B")


    NpcTalk(
        0x1B,
        "Randy",
        (
            "#00305FWhat am I, some kinda\x01",
            "guidebook substitute?\x02\x03",
            "#00308FSo in the end, a guy\x01",
            "like me is just\x01",
            "convenient, huh...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00011F#6PAaargh, don't say it so\x01",
            "indecently!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Randy",
        (
            "#00309FGwah ha ha, that was a\x01",
            "joke.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 30)
    Call(0, 33)
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x101, 0x1)

    ChrTalk(
        0x101,
        (
            "#00002F#6P...We're almost at the\x01",
            "top.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x1B, 0x2)

    NpcTalk(
        0x1B,
        "Randy",
        (
            "#00304FYeah, almost there.\x02\x03",
            "#00300FIt's not like Orchis Tower, but it's\x01",
            "still pretty high up. The view from here\x01",
            "is superb.\x02\x03",
            "On top of that, with the outstanding\x01",
            "mood inside this airtight gondola, the\x01",
            "capture success rate increases manyfold.\x02\x03",
            "#00309FThis is the ideal place for a man and a\x01",
            "woman to advance to the next step.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00006F#6PCapture success rate?\x01",
            "What are you talking\x01",
            "about?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrSubChip(0x1B, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4A29")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("Randy")

    AnonymousTalk(
        0xFF,
        (
            "Haha. Just a little instruction in\x01",
            "the ways of love.\x02\x03",
            "But even so... You invited ME on a\x01",
            "perfect evening like this one.\x02\x03",
            "This is the best time for makin'\x01",
            "girls fall for you. What are you\x01",
            "doin'?\x02",
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
        (
            "#00012F#6PW-Who do you take me for?\x02\x03",
            "#00000F...Well, because of how things\x01",
            "turned out, there's so many girls\x01",
            "this time.\x02\x03",
            "I don't think making time for us\x01",
            "to talk like this is so bad every\x01",
            "now and then.\x02\x03",
            "#00009FStill, being able to see a sunset\x01",
            "like this... Saving my last ticket\x01",
            "for this was the right choice.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4BE9")

    label("loc_4A29")


    NpcTalk(
        0x1B,
        "Randy",
        (
            "#00309FHaha. Just a little\x01",
            "instruction in the ways of\x01",
            "love.\x02\x03",
            "#00303FStill, who'd have ever\x01",
            "thought you'd invite me on\x01",
            "a Ferris wheel with you.\x02\x03",
            "#00301FIt's a perfect place to\x01",
            "make girls fall for you.\x01",
            "What's wrong with you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#6PW-Who do you take me for?\x02\x03",
            "#00000F...Well, because of how\x01",
            "things turned out, there's\x01",
            "so many girls this time.\x02\x03",
            "#00004FI don't think making time\x01",
            "for us to talk like this is\x01",
            "so bad every now and then.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4BE9")

    OP_63(0x1B, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    NpcTalk(
        0x1B,
        "Randy",
        (
            "#00306FJeez, that's why you're\x01",
            "a natural gigolo...\x02\x03",
            "#00300FWell, I'll at least\x01",
            "accept your thoughts.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 31)
    OP_CC(0x1, 0xFF, 0x0)
    Call(0, 34)
    Sleep(3000)

    ChrTalk(
        0x101,
        "#00000F#6P...We're almost there.\x05\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Randy",
        "#00300FYeah. Let's get off.\x05\x02",
    )

    CloseMessageWindow()
    Call(0, 36)
    Call(0, 28)
    Call(0, 24)
    Call(0, 35)

    NpcTalk(
        0x1B,
        "Randy",
        (
            "#00300FThanks for invitin' me.\x01",
            "It wasn't bad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#6PYeah. I'm glad I invited\x01",
            "you.\x02\x03",
            "Ok, see you later.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Randy",
        "#00300FYeah, later.\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x1B, 3, 0, 39)
    WaitChrThread(0x1B, 3)
    Return()

    # Function_42_41A6 end

    def Function_43_4D8B(): pass

    label("Function_43_4D8B")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu10101.itp")
    Call(0, 29)
    SetChrSubChip(0x1B, 0x2)
    SetChrSubChip(0x101, 0x1)
    Call(0, 32)

    NpcTalk(
        0x1B,
        "Noｱl",
        "#10101F............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#6P............\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Noｱl",
        "#10106F............\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x101,
        (
            "#00006F#6P...Umm, Noｱl. Why have\x01",
            "you been silent this\x01",
            "whole time?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1B, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x1B, 0x0)

    NpcTalk(
        0x1B,
        "Noｱl",
        (
            "#10105FAh, no! It's... It's my\x01",
            "first time riding the\x01",
            "Ferris wheel with a man.\x02\x03",
            "#10100FI rode it with Fran\x01",
            "before, though.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7FF), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4FAE")

    ChrTalk(
        0x101,
        (
            "#00009F#6PO-Oh... So that's what it was.\x02\x03",
            "#00000FWell, this is my first time\x01",
            "riding too. I was wondering if\x01",
            "you could teach me some things.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5047")

    label("loc_4FAE")


    ChrTalk(
        0x101,
        (
            "#00009F#6PO-Oh... So that's what it was.\x02\x03",
            "#00000FWell, I haven't ridden them that\x01",
            "much myself... I was wondering if\x01",
            "you could teach me some things.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5047")


    NpcTalk(
        0x1B,
        "Noｱl",
        (
            "#10102FS-Sure! Please leave it\x01",
            "to me!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 30)
    SetChrSubChip(0x1B, 0x2)
    SetChrSubChip(0x101, 0x1)
    Call(0, 33)

    NpcTalk(
        0x1B,
        "Noｱl",
        (
            "#10100FWe're pretty high up.\x02\x03",
            "#10104FHmm. I think you can get\x01",
            "the best view from here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009F#6PYeah, it really is a\x01",
            "nice view.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1B, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x1B)
    SetChrSubChip(0x1B, 0x0)

    NpcTalk(
        0x1B,
        "Noｱl",
        (
            "#10106FUmm, Lloyd, are you sure\x01",
            "it was okay to invite\x01",
            "me?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x101,
        "#00005F#6PHuh, why?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_53A7")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("Noｱl")

    AnonymousTalk(
        0xFF,
        (
            "Well, the sunset is so pretty...\x02\x03",
            "Maybe you should've enjoyed it with\x01",
            "a more beautiful girl like Elie or\x01",
            "Cecil...\x02",
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
        (
            "#00003F#6PHmm. I don't think you\x01",
            "have to devalue yourself\x01",
            "like that.\x02\x03",
            "#00000FYou have your own cute\x01",
            "points too, Noｱl.\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    NpcTalk(
        0x1B,
        "Noｱl",
        "#10114F#4SEH.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009F#6PEven so, this sunset...\x01",
            "Saving my last ticket for\x01",
            "this was the right choice.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_54C1")

    label("loc_53A7")


    NpcTalk(
        0x1B,
        "Noｱl",
        (
            "#10108FI mean, you don't ride the\x01",
            "Ferris wheel that often,\x01",
            "you see.\x02\x03",
            "Maybe you should've enjoyed\x01",
            "it with a more beautiful\x01",
            "girl like Elie or Cecil...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#6PHmm. I don't think you\x01",
            "have to devalue yourself\x01",
            "like that.\x02\x03",
            "#00000FYou have your own cute\x01",
            "points too, Noｱl.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_54C1")

    OP_63(0x1B, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x1B)

    ChrTalk(
        0x101,
        (
            "#00005F#6PH-Huh? Did I say\x01",
            "something weird?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Noｱl",
        (
            "#10109FN-No... Umm, thanks.\x02\x03",
            "#10106F(It's like those words\x01",
            "had no special\x01",
            "meaning...)\x02\x03",
            "#10101F(I get the feeling that\x01",
            "Lloyd is a more dangerous\x01",
            "person than I thought.)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1B, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x1B)
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00006F#6P(H-Hmm... She fell silent\x01",
            "again. I guess I did say\x01",
            "something weird.)\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    Call(0, 31)
    Call(0, 34)
    Sleep(3000)

    ChrTalk(
        0x101,
        "#00000F#6P...We're almost there.\x05\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Noｱl",
        (
            "#10100FAh, yes. Shall we get\x01",
            "off, then.?\x05\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 36)
    Call(0, 28)
    Call(0, 24)
    Call(0, 35)

    NpcTalk(
        0x1B,
        "Noｱl",
        (
            "#10100FThank you for inviting\x01",
            "me. I had a great time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#6PYeah. I'm glad I invited\x01",
            "you.\x02\x03",
            "Ok, see you later.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Noｱl",
        "#10100FYes, see you!\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x1B, 3, 0, 39)
    WaitChrThread(0x1B, 3)
    Return()

    # Function_43_4D8B end

    def Function_44_576D(): pass

    label("Function_44_576D")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu10301.itp")
    Call(0, 29)
    SetChrSubChip(0x1B, 0x2)
    SetChrSubChip(0x101, 0x1)
    Call(0, 32)
    Sleep(500)
    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x101,
        (
            "#00000F#6PBy the way, Wazy, have\x01",
            "you ridden the Ferris\x01",
            "wheel before?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x1B, 0x0)

    NpcTalk(
        0x1B,
        "Wazy",
        (
            "#10309FHehe. Actually, I haven't.\x02\x03",
            "#10300FWhen I come to Michelam with club\x01",
            "clients, I usually meet them in\x01",
            "quiet places like the bar.\x02\x03",
            "#10304FIn that sense, the theme park\x01",
            "itself is quite new to me.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7FF), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_59CB")

    ChrTalk(
        0x101,
        (
            "#00000F#6PWow... I didn't expect that.\x02\x03",
            "#00003FIt's my first time riding the\x01",
            "Ferris wheel, so I'm quite\x01",
            "nervous.\x02\x03",
            "#00002FNow that I think about it, that's\x01",
            "a strange thing to say since it's\x01",
            "not even a thrill-type attraction.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5ABF")

    label("loc_59CB")


    ChrTalk(
        0x101,
        (
            "#00000F#6PWow... I didn't expect that.\x02\x03",
            "#00003FI rode the Ferris wheel earlier,\x01",
            "but I'm nervous since I'm still\x01",
            "not used to it.\x02\x03",
            "#00002FNow that I think about it, that's\x01",
            "a strange thing to say since it's\x01",
            "not even a thrill-type attraction.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5ABF")


    NpcTalk(
        0x1B,
        "Wazy",
        (
            "#10300FWell, I think the Ferris wheel is\x01",
            "unexpectedly classified as a scary\x01",
            "ride.\x02\x03",
            "#10304FThere are people who are scared of\x01",
            "heights alone...\x02\x03",
            "#10302FIt's unlikely, but if the gondola\x01",
            "suspension linkage broke, it would\x01",
            "turn into a horrible accident.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00006F#6PDon't suddenly say stuff\x01",
            "to make me uneasy...\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Wazy",
        (
            "#10309FHehe. What's wrong with\x01",
            "some thrills?\x02\x03",
            "#10304FWell for now, let's\x01",
            "enjoy the Ferris wheel.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 30)
    SetChrSubChip(0x1B, 0x2)
    SetChrSubChip(0x101, 0x1)
    Call(0, 33)

    ChrTalk(
        0x101,
        (
            "#00000F#6PWe're almost at the top,\x01",
            "huh...\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Wazy",
        (
            "#10304FWe're high up as expected, but\x01",
            "the gondola's movements\x01",
            "themselves are unexpectedly slow.\x02\x03",
            "Maybe it's so people can enjoy\x01",
            "the view longer, but...\x02\x03",
            "#10302FHehe. Maybe we can think of it as\x01",
            "the suspension bridge effect.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x101,
        (
            "#00005F#6PYeah. When your heart beats faster due\x01",
            "to fear, they say it can be mistaken for\x01",
            "love... I've heard a little about it.\x02\x03",
            "#00009FThey say a lot of couples ride this, so\x01",
            "it's probably more effective than we\x01",
            "think.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrSubChip(0x1B, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_606C")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("Wazy")

    AnonymousTalk(
        0xFF,
        (
            "Hehe. You're even showing me such a\x01",
            "beautiful sunset.\x02\x03",
            "It wouldn't be the least bit\x01",
            "strange if love sprouted between\x01",
            "us.\x02",
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
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00012F#6PN-No no no no...\x02\x03",
            "I thought it was the right\x01",
            "choice to save my last ticket to\x01",
            "see a sunset like this, but...\x02\x03",
            "#00003FNo, no, that won't happen.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6151")

    label("loc_606C")


    NpcTalk(
        0x1B,
        "Wazy",
        (
            "#10304FHehe. With us all alone\x01",
            "in a locked room...\x02\x03",
            "#10309FIt wouldn't be the least\x01",
            "bit strange if love\x01",
            "sprouted between us.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00012F#6PN-No no no no...\x02\x03",
            "#00003FNo, no, that won't\x01",
            "happen.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6151")


    NpcTalk(
        0x1B,
        "Wazy",
        (
            "#10304FHehe, how cold. My\x01",
            "feelings are real, you\x01",
            "know?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00011F#6PJ-Just cut that out\x01",
            "already!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Wazy",
        (
            "#10309FHehe. Teasing you is\x01",
            "worth it.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    Call(0, 31)
    Call(0, 34)
    Sleep(3000)

    ChrTalk(
        0x101,
        "#00000F#6P...We're almost there.\x05\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Wazy",
        "#10300FYeah, shall we get off?\x05\x02",
    )

    CloseMessageWindow()
    Call(0, 36)
    Call(0, 28)
    Call(0, 24)
    Call(0, 35)

    NpcTalk(
        0x1B,
        "Wazy",
        (
            "#10300FHehe, that was pretty\x01",
            "fun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#6PYeah. I'm glad I invited\x01",
            "you.\x02\x03",
            "Ok, see you later.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Wazy",
        "#10300FYeah, later.\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x1B, 3, 0, 39)
    WaitChrThread(0x1B, 3)
    Return()

    # Function_44_576D end

    def Function_45_630E(): pass

    label("Function_45_630E")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu01102.itp")
    Call(0, 29)
    SetChrSubChip(0x101, 0x1)
    SetChrPos(0x1B, 1000260, 0, 970, 0)
    SetChrChipByIndex(0x1B, 0x5)
    SetChrSubChip(0x1B, 0x0)
    Call(0, 32)
    OP_63(0x1B, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    NpcTalk(
        0x1B,
        "KeA",
        (
            "#01105F#11PWah, we're going higher\x01",
            "and higher!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_9C(0x1B, 0x0, 0x0, 0x0, 0x12C, 0x7D0)
    OP_82(0x0, 0x32, 0x5DC, 0x12C)
    Sleep(100)
    OP_9C(0x1B, 0x0, 0x0, 0x0, 0x12C, 0x7D0)
    OP_82(0x0, 0x32, 0x5DC, 0x12C)
    OP_63(0x101, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00012F#6PK-KeA. It's dangerous if you\x01",
            "shake it, so please stay\x01",
            "seated inside the gondola, ok?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x1B, 0xE1, 0x1F4)

    NpcTalk(
        0x1B,
        "KeA",
        (
            "#01105F#11POh, you're right.\x02\x03",
            "#01109FEhehe, KeA got carried\x01",
            "away.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    OP_95(0x1B, 1000610, 0, 40, 2000, 0x0)
    OP_93(0x1B, 0x10E, 0x1F4)
    Fade(250)
    SetChrChipByIndex(0x1B, 0x1F)
    SetChrSubChip(0x1B, 0x0)
    SetChrPos(0x1B, 1001000, 200, 0, 270)
    OP_0D()

    NpcTalk(
        0x1B,
        "KeA",
        (
            "#01100FHey Lloyd.\x02\x03",
            "#01109FIs there an amazing view\x01",
            "at the top?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7FF), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_65E0")

    ChrTalk(
        0x101,
        (
            "#00004F#6PWell, it's my first time\x01",
            "riding so I don't know\x01",
            "yet, but...\x02\x03",
            "#00000FI'm sure we can look\x01",
            "forward to it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_664B")

    label("loc_65E0")


    ChrTalk(
        0x101,
        (
            "#00004F#6PYeah. When I rode\x01",
            "before, it was a great\x01",
            "view.\x02\x03",
            "#00000FI'm sure you can look\x01",
            "forward to it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_664B")

    OP_63(0x1B, 0x12C, 1300, 0x36, 0x39, 0xFA, 0x0)
    Sleep(1000)

    NpcTalk(
        0x1B,
        "KeA",
        (
            "#01109FSo excited... I can't\x01",
            "wait!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrChipByIndex(0x1B, 0x5)
    SetChrSubChip(0x1B, 0x0)
    SetChrPos(0x1B, 1000610, 0, 40, 270)
    OP_0D()
    OP_9C(0x1B, 0x0, 0x0, 0x0, 0x12C, 0x7D0)
    OP_82(0x0, 0x32, 0x5DC, 0x12C)
    Sleep(100)
    OP_9C(0x1B, 0x0, 0x0, 0x0, 0x12C, 0x7D0)
    OP_82(0x0, 0x32, 0x5DC, 0x12C)
    OP_63(0x101, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00011F#6PI know that already.\x01",
            "Just calm down.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 30)
    SetChrSubChip(0x101, 0x1)
    SetChrPos(0x1B, 1000260, 0, 970, 0)
    SetChrChipByIndex(0x1B, 0x5)
    SetChrSubChip(0x1B, 0x0)
    Call(0, 33)
    OP_63(0x1B, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_693E")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("KeA")

    AnonymousTalk(
        0xFF,
        (
            "Waaah! It's so high!!\x02\x03",
            "And the sky is deep red and super\x01",
            "pretty!!\x02",
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
        (
            "#00004F#6PYeah... It seems we rode\x01",
            "at the perfect time.\x02\x03",
            "#00009FSaving my last ticket\x01",
            "for this was the right\x01",
            "choice.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "KeA",
        (
            "#01102F#11PEhehe, thanks for\x01",
            "inviting me.\x02\x03",
            "#01110FAh, look Lloyd! Look! A\x01",
            "fish jumped!!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6996")

    label("loc_693E")


    NpcTalk(
        0x1B,
        "KeA",
        (
            "#01110F#11PWaaah! It's so high!!\x02\x03",
            "#01109FAh, look Lloyd! Look! A\x01",
            "fish jumped!!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6996")


    ChrTalk(
        0x101,
        (
            "#00002F#6PYeah, I wonder what fish\x01",
            "it was. I didn't get a\x01",
            "good look at it, though...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1B, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x1B)
    OP_93(0x1B, 0xE1, 0x1F4)

    NpcTalk(
        0x1B,
        "KeA",
        (
            "#01105F#11PBy the way...\x02\x03",
            "#01100FHey, this scenery or\x01",
            "that from Orchis Tower.\x01",
            "Which is better?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F#6PHuh? Hmm. Orchis Tower is far\x01",
            "taller for sure, but...\x02\x03",
            "#00003FThis scenery is totally\x01",
            "different. I guess I can't\x01",
            "definitively say which is better.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "KeA",
        (
            "#01103F#11PMmm, I see...\x02\x03",
            "#01109FThat's deep, Lloyd!\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x1B, 0x0, 0x1F4)
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00012F#6PYou're certainly\x01",
            "hyper...\x02\x03",
            "#00004F(...Well, at least she's\x01",
            "happy. I guess I can\x01",
            "relax for now.)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1B, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    NpcTalk(
        0x1B,
        "KeA",
        (
            "#01110F#11PAh, there's that fish\x01",
            "again!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    Call(0, 31)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x1B, 0x1F)
    SetChrSubChip(0x1B, 0x0)
    SetChrPos(0x1B, 1001000, 200, 0, 270)
    Call(0, 34)
    Sleep(3000)

    ChrTalk(
        0x101,
        (
            "#00000F#6PLooks like we're\x01",
            "arriving soon. Let's get\x01",
            "off, KeA.\x05\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "KeA",
        "#01100FYeah, okay!\x05\x02",
    )

    CloseMessageWindow()
    Call(0, 36)
    Call(0, 28)
    Call(0, 24)
    Call(0, 35)

    NpcTalk(
        0x1B,
        "KeA",
        (
            "#01109FEhehe, that was a great\x01",
            "view. I had a super good\x01",
            "time!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#6PYeah. I'm glad I invited\x01",
            "you.\x02\x03",
            "Ok, see you later.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "KeA",
        "#01100FYeah! See you, Lloyd!\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x1B, 3, 0, 39)
    WaitChrThread(0x1B, 3)
    Return()

    # Function_45_630E end

    def Function_46_6D8F(): pass

    label("Function_46_6D8F")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu06400.itp")
    Call(0, 29)
    SetChrSubChip(0x1B, 0x2)
    SetChrSubChip(0x101, 0x1)
    Call(0, 32)
    OP_63(0x1B, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    NpcTalk(
        0x1B,
        "Fran",
        (
            "#06404FThis sensation of the\x01",
            "ground getting farther\x01",
            "and farther away...\x02\x03",
            "#06409FWhen I ride the Ferris\x01",
            "wheel, my heart always\x01",
            "pounds, you know.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7FF), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6F11")

    ChrTalk(
        0x101,
        (
            "#00004F#6PYeah. It's my first time\x01",
            "too, and I'm really\x01",
            "nervous.\x02\x03",
            "#00000FIf I had to say though,\x01",
            "I'd say you're excited.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6F90")

    label("loc_6F11")


    ChrTalk(
        0x101,
        (
            "#00004F#6PI understand how you\x01",
            "feel. It really makes\x01",
            "you nervous.\x02\x03",
            "#00000FIf I had to say though,\x01",
            "I'd say you're excited.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6F90")

    SetChrSubChip(0x1B, 0x0)

    NpcTalk(
        0x1B,
        "Fran",
        (
            "#06402FOh, you can tell?\x02\x03",
            "#06404FAfter all, riding in a Ferris\x01",
            "wheel with a guy is an experience\x01",
            "you don't have too often.\x02\x03",
            "#06409FAnd it's with you of all people!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009F#6PHaha. That might be more\x01",
            "that I deserve, but...\x02\x03",
            "#00000FThinking about it, we\x01",
            "hardly ever get the chance\x01",
            "to be alone together.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Fran",
        (
            "#06409FHaha. Let's take\x01",
            "advantage of it and\x01",
            "talk, okay!?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 30)
    SetChrSubChip(0x1B, 0x2)
    SetChrSubChip(0x101, 0x1)
    Call(0, 33)

    NpcTalk(
        0x1B,
        "Fran",
        "#06400FAh, look!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#6PYeah, we're almost at\x01",
            "the top.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_734D")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("Fran")

    AnonymousTalk(
        0xFF,
        (
            "*sigh*, I can hardly stand it.\x02\x03",
            "With the deep red sunset, it's\x01",
            "incredibly romantic!\x02",
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
        (
            "#00004F#6PYeah... It seems we rode\x01",
            "at the perfect time.\x02\x03",
            "#00009FSaving my last ticket\x01",
            "for this was the right\x01",
            "choice.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Fran",
        (
            "#06402FHaha. Thank you for\x01",
            "inviting me!\x02\x03",
            "I did ride with Noｱl\x01",
            "before, but it really is\x01",
            "an amazing view!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_73C4")

    label("loc_734D")


    NpcTalk(
        0x1B,
        "Fran",
        (
            "#06402F*sigh*, I can hardly\x01",
            "stand it.\x02\x03",
            "#06409FI did ride with Noｱl\x01",
            "before, but it really is\x01",
            "an amazing view!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_73C4")

    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x101,
        (
            "#00005F#6PBy the way Fran, haven't\x01",
            "you dated guys before?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1B, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x1B, 0x0)

    NpcTalk(
        0x1B,
        "Fran",
        (
            "#06405FNo, I haven't... Why do\x01",
            "you ask?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#6PW-Well... There's no\x01",
            "special meaning in it.\x02\x03",
            "#00000FI always thought you're\x01",
            "really popular, you\x01",
            "know.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Fran",
        (
            "#06402FAhaha, me? Not at all.\x02\x03",
            "#06404FAnd, there's not many guys\x01",
            "who are as cool and\x01",
            "reliable as Noｱl, you see.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00012F#6PSo she's your standard,\x01",
            "huh...\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Fran",
        (
            "#06409FEhehe, but of course.\x02\x03",
            "Ever since we were kids,\x01",
            "Noｱl has always been my\x01",
            "number one!\x02\x03",
            "#06400FOh, but you might just\x01",
            "barely pass, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009F#6PHaha... Thanks for that.\x01",
            "(They really are very\x01",
            "close.)\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    Call(0, 31)
    Call(0, 34)
    Sleep(3000)

    ChrTalk(
        0x101,
        (
            "#00000F#6PWe're almost there.\x01",
            "Shall we get off?\x05\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Fran",
        "#06400FYes, let's.\x05\x02",
    )

    CloseMessageWindow()
    Call(0, 36)
    Call(0, 28)
    Call(0, 24)
    Call(0, 35)

    NpcTalk(
        0x1B,
        "Fran",
        (
            "#06400FEhehe. The view was\x01",
            "amazing, and I had a lot\x01",
            "of fun!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#6PYeah. I'm glad I invited\x01",
            "you.\x02\x03",
            "Ok, see you later.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Fran",
        "#06400FSure! Later, then.\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x1B, 3, 0, 39)
    WaitChrThread(0x1B, 3)
    Return()

    # Function_46_6D8F end

    def Function_47_77B7(): pass

    label("Function_47_77B7")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu05900.itp")
    Call(0, 29)
    Call(0, 32)

    NpcTalk(
        0x1B,
        "Cecil",
        (
            "#05900FWow... So this is what\x01",
            "it's like inside the\x01",
            "gondola.\x02\x03",
            "#05904FIt's just like a big\x01",
            "cradle.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7FF), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_78FE")

    ChrTalk(
        0x101,
        (
            "#00004F#6PYeah. It's my first time\x01",
            "riding too, but it does\x01",
            "feel just like that.\x02\x03",
            "#00000FI think it rocks quite a\x01",
            "bit, so please be\x01",
            "careful.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_795F")

    label("loc_78FE")


    ChrTalk(
        0x101,
        (
            "#00004F#6PYeah, it does feel like\x01",
            "that.\x02\x03",
            "#00000FIt rocks quite a bit, so\x01",
            "please be careful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_795F")


    NpcTalk(
        0x1B,
        "Cecil",
        (
            "#05900FHaha, thanks Lloyd.\x02\x03",
            "#05904FWe haven't been alone together since we\x01",
            "went to see the Arc-en-Ciel performance\x01",
            "during the anniversary festival.\x02\x03",
            "#05909FWe don't get chances like this often,\x01",
            "so let's have a nice chat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F#6PY-Yeah... Let's.\x02\x03",
            "#00003F(When I think about that\x01",
            "I get nervous for some\x01",
            "reason...)\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 30)
    Call(0, 33)

    NpcTalk(
        0x1B,
        "Cecil",
        (
            "#05904FHaha, but even so, the theme park is a\x01",
            "really fun place.\x02\x03",
            "#05902FYou are greeted by the cute Mishy,\x01",
            "there are many fun attractions... It's\x01",
            "like being lost in a dream world.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002F#6PHaha... For real.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00008F#6PWhen my brother was\x01",
            "alive... Did you come\x01",
            "here with him?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Cecil",
        (
            "#05904FHaha... Sadly, no. No\x01",
            "place like this existed\x01",
            "in Crossbell back then.\x02\x03",
            "#05900FBut, I did go on many\x01",
            "dates with Guy that were\x01",
            "no less fun.\x02\x03",
            "#05909FWhen we went out to eat,\x01",
            "he introduced me to his\x01",
            "favorite food carts.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00012F#6PF-Food carts on a date, huh...\x02\x03",
            "#00006FDates are special. It would've\x01",
            "been nice if he looked for\x01",
            "places a little more upscale.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Cecil",
        (
            "#05905FOh, but the food was\x01",
            "delicious and I really\x01",
            "liked them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#6P(Hmm... Cecil and my\x01",
            "brother were made for each\x01",
            "other, weren't they...)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1B, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x1B, 0x2)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8037")

    NpcTalk(
        0x1B,
        "Cecil",
        (
            "#05905FAh... We're almost at the top.\x02\x03",
            "#05909FThe red sunset is very pretty...\x01",
            "It's different than the scene\x01",
            "from atop the hospital.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)

    ChrTalk(
        0x101,
        (
            "#00004F#6PYeah... It seems we rode\x01",
            "at the perfect time.\x02\x03",
            "#00009FSaving my last ticket\x01",
            "for this was the right\x01",
            "choice.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrSubChip(0x1B, 0x0)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("Cecil")

    AnonymousTalk(
        0xFF,
        (
            "Haha, thanks for inviting me.\x02\x03",
            "This sunset will make a nice\x01",
            "memory.\x02",
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
    Jump("loc_8126")

    label("loc_8037")


    NpcTalk(
        0x1B,
        "Cecil",
        (
            "#05905FAh... We're almost at the\x01",
            "top.\x02\x03",
            "#05909FThe lake is really pretty...\x01",
            "It's different than the scene\x01",
            "from atop the hospital.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)

    ChrTalk(
        0x101,
        "#00002F#6PYeah... It really is.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x1B, 0x0)

    NpcTalk(
        0x1B,
        "Cecil",
        (
            "#05902FHaha, this will make a\x01",
            "nice memory.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8126")

    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x101,
        (
            "#00009F#6PHaha, I'm glad you\x01",
            "enjoyed it.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    Call(0, 31)
    Call(0, 34)
    Sleep(3000)

    ChrTalk(
        0x101,
        (
            "#00000F#6PIt looks like we're\x01",
            "almost there. Shall we\x01",
            "get off?\x05\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Cecil",
        "#05900FYes, let's.\x05\x02",
    )

    CloseMessageWindow()
    Call(0, 36)
    Call(0, 28)
    Call(0, 24)
    Call(0, 35)

    NpcTalk(
        0x1B,
        "Cecil",
        (
            "#05900FI had a lot of fun.\x01",
            "Thank you, Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#6PYeah. I'm glad I invited\x01",
            "you.\x02\x03",
            "See you later, then.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Cecil",
        "#05900FYes, see you later.\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x1B, 3, 0, 39)
    WaitChrThread(0x1B, 3)
    Return()

    # Function_47_77B7 end

    def Function_48_828B(): pass

    label("Function_48_828B")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu01700.itp")
    Call(0, 29)
    SetChrSubChip(0x1B, 0x2)
    SetChrSubChip(0x101, 0x1)
    Call(0, 32)

    NpcTalk(
        0x1B,
        "Ilya",
        (
            "#01704FHmm, hmm... This is a\x01",
            "little unsatisfying for\x01",
            "someone like me, but...\x02\x03",
            "#01700FA relaxing ride like\x01",
            "this isn't too bad every\x01",
            "now and then.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7FF), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8409")

    ChrTalk(
        0x101,
        (
            "#00002F#6PHaha. I'm glad to hear\x01",
            "you say that.\x02\x03",
            "#00004FI heard there's a nice\x01",
            "view from the top...\x02\x03",
            "#00000FI think you'll enjoy it\x01",
            "too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_848E")

    label("loc_8409")


    ChrTalk(
        0x101,
        (
            "#00002F#6PHaha. I'm glad to hear\x01",
            "you say that.\x02\x03",
            "#00004FThere's a nice view from\x01",
            "the top...\x02\x03",
            "#00000FI think you'll enjoy it\x01",
            "too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_848E")

    SetChrSubChip(0x1B, 0x0)

    NpcTalk(
        0x1B,
        "Ilya",
        (
            "#01709FIs it that great? Huhu,\x01",
            "I guess I'll look\x01",
            "forward to it.\x02\x03",
            "#01703FBut at this rate, it'll\x01",
            "be quite a while before\x01",
            "we get there.\x02\x03",
            "#01702FHaha. Since we're here,\x01",
            "shouldn't we be honest\x01",
            "with each other?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#6PY-Yeah, sure. (I have a\x01",
            "bad feeling about this,\x01",
            "but...)\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 30)
    Call(0, 33)

    NpcTalk(
        0x1B,
        "Ilya",
        (
            "#01709FAnd so, who are you aiming for little\x01",
            "bro?\x02\x03",
            "#01705FIs it Cecil? Or one of your\x01",
            "colleagues? Could it be me or Rixia?\x02\x03",
            "#01704FBut let me just say this. Sully is off\x01",
            "limits, you hear? As her guardian, I\x01",
            "have to wait until she grows up...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00006F#6PH-Hey, wait just a moment!\x02\x03",
            "#00011FThese rapid-fire questions\x01",
            "asking who I'm after...\x01",
            "It's too embarrassing!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Ilya",
        (
            "#01706FHuh, why not? Don't\x01",
            "think about it too hard\x01",
            "and just tell me.\x02\x03",
            "#01700FI'm Cecil's best friend,\x01",
            "so I'm basically another\x01",
            "of your sisters, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#6PT-That logic is weird...\x01",
            "After all, you're not\x01",
            "Cecil's real sister.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Ilya",
        (
            "#01709FHmph, you're no fun! In that\x01",
            "case, I'll make you spit it out\x01",
            "by tickling you, you know!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00011F#6P(T-This is bad. I have\x01",
            "to change the subject\x01",
            "somehow...)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x101, 0x1)

    ChrTalk(
        0x101,
        (
            "#00005F#6PA-Aah, Ilya! It looks\x01",
            "like we're almost at the\x01",
            "top.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1B, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x1B, 0x2)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8B9F")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("Ilya")

    AnonymousTalk(
        0xFF,
        (
            "Wow! It really is a nice view.\x02\x03",
            "Also, thanks to the lake dyed\x01",
            "vermillion by the sunset, it feels\x01",
            "very... Nostalgic, I'd say...\x02",
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
        (
            "#00004F#6PYes... It seems we rode\x01",
            "at the perfect time.\x02\x03",
            "#00009FSaving my last ticket\x01",
            "for this was the right\x01",
            "choice.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Ilya",
        (
            "#01709FHuhu. Honestly, it was better\x01",
            "than I thought it would be.\x01",
            "Thanks for inviting me.\x02\x03",
            "#01703FHmm, I wonder if I could\x01",
            "bring this image to life\x01",
            "onstage...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8C96")

    label("loc_8B9F")


    NpcTalk(
        0x1B,
        "Ilya",
        (
            "#01705FWow! It really is a nice\x01",
            "view.\x02\x03",
            "#01709FTo be able to see nature\x01",
            "like this in Crossbell,\x01",
            "a metropolis...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#6PHaha... It is rather\x01",
            "unexpected.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Ilya",
        (
            "#01703FHmm, I wonder if I could\x01",
            "bring this image to life\x01",
            "onstage...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8C96")

    OP_63(0x1B, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x1B)

    ChrTalk(
        0x101,
        (
            "#00006F#6P(*sigh*... I guess that\x01",
            "distracted her somehow.)\x02\x03",
            "#00002F(Even so, she really is thinking\x01",
            "about the stage all the time. I\x01",
            "guess that's Ilya for you...)\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    Call(0, 31)
    Call(0, 34)
    Sleep(3000)

    ChrTalk(
        0x101,
        (
            "#00000F#6PLooks like we're almost\x01",
            "there. Let's get off.\x05\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Ilya",
        "#01700FYes, yes.\x05\x02",
    )

    CloseMessageWindow()
    Call(0, 36)
    Call(0, 28)
    Call(0, 24)
    Call(0, 35)

    NpcTalk(
        0x1B,
        "Ilya",
        (
            "#01700FHuhu, that was quite\x01",
            "fun. Thanks, little bro.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#6PI'm glad I invited you.\x02\x03",
            "See you later, then.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Ilya",
        "#01700FYeah, see you later.\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x1B, 3, 0, 39)
    WaitChrThread(0x1B, 3)
    Return()

    # Function_48_828B end

    def Function_49_8E80(): pass

    label("Function_49_8E80")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu01800.itp")
    Call(0, 29)
    SetChrSubChip(0x1B, 0x2)
    SetChrSubChip(0x101, 0x1)
    Call(0, 32)

    NpcTalk(
        0x1B,
        "Rixia",
        (
            "#01802F*sigh*... The Ferris\x01",
            "wheel is nice.\x02\x03",
            "#01804FIt's quiet, calm and\x01",
            "very relaxing.\x02\x03",
            "#01802FI feel like I understand\x01",
            "why it's popular with\x01",
            "families and couples.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7FF), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8FF6")

    ChrTalk(
        0x101,
        (
            "#00004F#6PHaha, for sure.\x02\x03",
            "#00000FAnd based on what I've\x01",
            "heard, the view from the top\x01",
            "is something special too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_907B")

    label("loc_8FF6")


    ChrTalk(
        0x101,
        (
            "#00004F#6PHaha, you're certainly\x01",
            "right about that.\x02\x03",
            "#00002FAnd when I rode before,\x01",
            "the view from the top\x01",
            "was something special.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_907B")

    SetChrSubChip(0x1B, 0x0)

    NpcTalk(
        0x1B,
        "Rixia",
        (
            "#01809FHaha, I'll look forward\x01",
            "to it.\x02\x03",
            "#01802FThen, shall we chat\x01",
            "until we reach the top?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x101,
        (
            "#00002F#6PYeah. It'll be a while\x01",
            "before we get there, so\x01",
            "that might be nice.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 30)
    SetChrFlags(0x1B, 0x2)
    SetChrChipByIndex(0x1B, 0x22)
    SetChrSubChip(0x1B, 0x0)
    Call(0, 33)

    NpcTalk(
        0x1B,
        "Rixia",
        "#01804F...zzz... zzz...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#6P(Hmm, she looks sleepy.)\x02\x03",
            "#00006F(Her daily training is\x01",
            "probably tough, and she might\x01",
            "be tired from the beach, too.)\x02\x03",
            "#00002F(We're almost at the top.\x01",
            "Should I let her sleep?)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0x1B, 0x1F)
    SetChrSubChip(0x1B, 0x0)
    ClearChrFlags(0x1B, 0x2)
    OP_0D()
    OP_63(0x1B, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    NpcTalk(
        0x1B,
        "Rixia",
        "#01805FAh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#6PAh, I guess I woke you.\x02",
    )

    CloseMessageWindow()
    OP_63(0x1B, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    NpcTalk(
        0x1B,
        "Rixia",
        (
            "#01805FI-I'm sorry! I\x01",
            "unconsciously dozed\x01",
            "off...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009F#6PHaha, that's nothing to\x01",
            "apologize for. More\x01",
            "importantly...\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    Sleep(250)
    SetChrSubChip(0x1B, 0x2)
    Sleep(250)
    OP_63(0x1B, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9510")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("Rixia")

    AnonymousTalk(
        0xFF,
        (
            "Ah... We're already at the top.\x02\x03",
            "The light of the sunset dyes the\x01",
            "surface crimson... It's a very\x01",
            "pretty view.\x02",
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
        (
            "#00004F#6PYeah... It seems we rode\x01",
            "at the perfect time.\x02\x03",
            "#00009FSaving my last ticket\x01",
            "for this was the right\x01",
            "choice.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Rixia",
        (
            "#01809FThank you for inviting\x01",
            "me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_95A5")

    label("loc_9510")


    NpcTalk(
        0x1B,
        "Rixia",
        (
            "#01805FAh... We're already at\x01",
            "the top.\x02\x03",
            "#01802FWe're surrounded by this\x01",
            "vast lake... It's a very\x01",
            "pretty view.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002F#6PYeah, it is.\x02",
    )

    CloseMessageWindow()

    label("loc_95A5")

    OP_63(0x1B, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x1B)

    NpcTalk(
        0x1B,
        "Rixia",
        (
            "#01808F(...Still, to fall\x01",
            "asleep when we're all\x01",
            "alone like this...)\x02\x03",
            "#01803F(No matter how relaxed I\x01",
            "feel, if he was Yin's\x01",
            "target...)\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x101,
        (
            "#00005F#6P...Umm, Rixia?\x02\x03",
            "#00002FIf you're still sleepy, I\x01",
            "don't mind if you go\x01",
            "ahead and rest, you know.\x02\x03",
            "I'll wake you when we get\x01",
            "to the bottom.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x1B, 0x0)

    NpcTalk(
        0x1B,
        "Rixia",
        (
            "#01804F...No... The view is\x01",
            "really pretty so I\x01",
            "spaced out a little.\x02\x03",
            "#01802FHaha. Please don't worry\x01",
            "about it.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    Call(0, 31)
    Call(0, 34)
    Sleep(3000)

    ChrTalk(
        0x101,
        (
            "#00000F#6PIt looks like we're\x01",
            "almost there. Shall we\x01",
            "get off?\x05\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Rixia",
        "#01802FYes.\x05\x02",
    )

    CloseMessageWindow()
    Call(0, 36)
    Call(0, 28)
    Call(0, 24)
    Call(0, 35)

    NpcTalk(
        0x1B,
        "Rixia",
        (
            "#01802FUmm, I had a lot of fun.\x01",
            "Thank you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#6PYeah. I'm glad I invited\x01",
            "you.\x02\x03",
            "Ok, see you later.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Rixia",
        "#01802FYes, see you later.\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x1B, 3, 0, 39)
    WaitChrThread(0x1B, 3)
    Return()

    # Function_49_8E80 end

    def Function_50_9891(): pass

    label("Function_50_9891")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu04201.itp")
    Call(0, 29)
    SetChrSubChip(0x1B, 0x2)
    SetChrSubChip(0x101, 0x1)
    Call(0, 32)
    OP_63(0x1B, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    NpcTalk(
        0x1B,
        "Sully",
        (
            "#04211FW-Whoa, it's going up\x01",
            "steadily...\x02\x03",
            "#04206FH-Hey, will we be all\x01",
            "right? This box would fall\x01",
            "with just a tiny impact...\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x101,
        (
            "#00004F#6PHaha. Don't worry, it won't\x01",
            "fall or anything.\x02\x03",
            "#00002FIn your Arc-en-Ciel practice\x01",
            "you jump from high places. You\x01",
            "shouldn't be that scared...\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x1B, 0x0)

    NpcTalk(
        0x1B,
        "Sully",
        (
            "#04206FI-I'm not scared or anything,\x01",
            "but... This height is in a\x01",
            "whole other league, right!?\x02\x03",
            "#04201FJeez... If you think it's no\x01",
            "big deal, I'm gonna sock you.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7FF), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9BA7")

    ChrTalk(
        0x101,
        (
            "#00006F#6PI don't think that's\x01",
            "something girls should\x01",
            "be saying, but...\x02\x03",
            "#00002FAnyway, I heard the view\x01",
            "from the top is amazing.\x02\x03",
            "It has value enough in\x01",
            "just facing your fear,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9C70")

    label("loc_9BA7")


    ChrTalk(
        0x101,
        (
            "#00006F#6PI don't think that's\x01",
            "something girls should\x01",
            "be saying, but...\x02\x03",
            "#00002FWell, I rode it before,\x01",
            "but the view from the\x01",
            "top is amazing.\x02\x03",
            "It has value enough in\x01",
            "just facing your fear,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9C70")

    OP_63(0x1B, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    NpcTalk(
        0x1B,
        "Sully",
        (
            "#04206FI-I told you, I'm not\x01",
            "scared, jeez!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 30)
    Call(0, 33)
    SetChrSubChip(0x1B, 0x2)
    SetChrSubChip(0x101, 0x1)

    ChrTalk(
        0x101,
        (
            "#00002F#6POh... We're almost at\x01",
            "the top.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1B, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    NpcTalk(
        0x1B,
        "Sully",
        (
            "#04211FW-Whoa... R-Really, it's\x01",
            "too high!\x02\x03",
            "#04207FG-Get me down! Get me\x01",
            "down this instant!!\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x101,
        (
            "#00012F#6PThere there, calm down.\x02\x03",
            "#00002FYou're only scared because\x01",
            "you're looking down. Try\x01",
            "looking over there.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Sully",
        "#04205FO-Over there...\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    OP_63(0x1B, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A0B0")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("Sully")

    AnonymousTalk(
        0xFF,
        (
            "Ah...\x02\x03",
            "I didn't realize it on the water\x01",
            "bus, but this place is surrounded\x01",
            "by so much water, huh...\x02\x03",
            "And the entire lake, dyed red by\x01",
            "the sunset, is really pretty...\x02",
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
        (
            "#00004F#6PYeah... It seems we rode\x01",
            "at the perfect time.\x02\x03",
            "#00009FSaving my last ticket\x01",
            "for this was the right\x01",
            "choice.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1B, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    NpcTalk(
        0x1B,
        "Sully",
        (
            "#04203FH-Hmph... I won't thank\x01",
            "you, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#6PHaha... Now don't be\x01",
            "shy.\x02\x03",
            "#00000FBut, isn't your fear of\x01",
            "high places or whatever\x01",
            "gone?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A18C")

    label("loc_A0B0")


    NpcTalk(
        0x1B,
        "Sully",
        (
            "#04205FAh...\x02\x03",
            "I didn't realize it on the water\x01",
            "bus, but this place is surrounded\x01",
            "by so much water, huh...\x02\x03",
            "#04202F...What a pretty view.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#6PHaha... Isn't your fear\x01",
            "of high places or\x01",
            "whatever gone?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A18C")

    OP_63(0x1B, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x1B)
    OP_63(0x1B, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    NpcTalk(
        0x1B,
        "Sully",
        (
            "#04211FW-Whoa! It's too high!\x01",
            "Too high!!\x02\x03",
            "#04206FJ-Jeez!! Don't make me\x01",
            "remember!\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x101,
        "#00006F#6PS-Sorry.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    Call(0, 31)
    Call(0, 34)
    Sleep(3000)

    ChrTalk(
        0x101,
        (
            "#00000F#6PLooks like we're almost\x01",
            "there. Shall we get off?\x05\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Sully",
        "#04200F...Y-Yeah.\x05\x02",
    )

    CloseMessageWindow()
    Call(0, 36)
    Call(0, 28)
    Call(0, 24)
    SetChrChipByIndex(0x1B, 0x8)
    SetChrSubChip(0x1B, 0x0)
    Call(0, 35)

    NpcTalk(
        0x1B,
        "Sully",
        (
            "#14012FW-Well... That was\x01",
            "pretty fun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#6PYeah. I'm glad I invited\x01",
            "you.\x02\x03",
            "Ok, see you later.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Sully",
        "#14000FHmph, see ya.\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x1B, 3, 0, 39)
    WaitChrThread(0x1B, 3)
    Return()

    # Function_50_9891 end

    def Function_51_A360(): pass

    label("Function_51_A360")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(12330, 4300, -17760, 0)
    MoveCamera(336, 16, 0, 0)
    OP_6E(1000, 0)
    SetCameraDistance(3220, 0)
    SetChrPos(0x101, 7370, 0, -12510, 45)
    SetChrPos(0xEF, 8660, 0, -13430, 20)
    OP_4B(0x1A, 0xFF)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#00005FFound her!\x02",
    )

    CloseMessageWindow()
    OP_9C(0x1A, 0x0, 0x0, 0x0, 0x1F4, 0xBB8)
    Sleep(500)
    TurnDirection(0x1A, 0x101, 500)
    OP_63(0x1A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x1A,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "Eek! You found me☆\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(8240, 4300, -19760, 0)
    MoveCamera(356, 30, 0, 0)
    OP_6E(1000, 0)
    SetCameraDistance(3220, 0)
    SetChrPos(0x1A, 8450, 0, -12880, 200)
    SetChrPos(0x101, 7200, 0, -14240, 20)
    SetChrPos(0xEF, 8750, 0, -14780, 300)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x1A,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "Mishishi, you're really\x01",
            "good at this, mister.☆\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "It's unheard of for me\x01",
            "to be found when I'm\x01",
            "serious.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FI-I think that's an\x01",
            "exaggeration.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "Anyway, just two more\x01",
            "times and you win!\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "Mishishi, good luck!\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A5AB():

        label("loc_A5AB")

        TurnDirection(0xFE, 0x1A, 500)
        Yield()
        Jump("loc_A5AB")

    QueueWorkItem2(0x101, 1, lambda_A5AB)

    def lambda_A5BD():

        label("loc_A5BD")

        TurnDirection(0xFE, 0x1A, 500)
        Yield()
        Jump("loc_A5BD")

    QueueWorkItem2(0xEF, 1, lambda_A5BD)
    SetChrFlags(0x1A, 0x1000)
    OP_95(0x1A, 10920, 0, -15100, 5000, 0x0)
    OP_95(0x1A, 6460, 0, -18160, 5000, 0x0)

    def lambda_A5FC():
        OP_95(0xFE, 710, 0, -17500, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_A5FC)
    Sleep(800)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x101, 0x1)
    EndChrThread(0xEF, 0x1)
    OP_68(-3070, 5000, -23400, 0)
    MoveCamera(39, 36, 0, 0)
    OP_6E(1000, 0)
    SetCameraDistance(3220, 0)
    SetChrPos(0x101, -540, 0, -18390, 180)
    SetChrPos(0xEF, 530, 0, -18400, 180)
    SetChrFlags(0x1A, 0x80)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00012FHmm, I feel like she\x01",
            "likes us or something...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 7)), scpexpr(EXPR_END)), "loc_A71D")

    ChrTalk(
        0x102,
        (
            "#00100FHaha. Isn't that great?\x02\x03",
            "Anyway, let's find her\x01",
            "next hiding place.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AAF4")

    label("loc_A71D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 0)), scpexpr(EXPR_END)), "loc_A77B")

    ChrTalk(
        0x103,
        (
            "#00200FPersonally, I'm jealous.\x02\x03",
            "Anyway, let's find her\x01",
            "next hiding place.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AAF4")

    label("loc_A77B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 1)), scpexpr(EXPR_END)), "loc_A7EC")

    ChrTalk(
        0x104,
        (
            "#00300FHaha. If PeTiote saw\x01",
            "that, she'd be jealous.\x02\x03",
            "Anyway, let's find her\x01",
            "next hidin' spot.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AAF4")

    label("loc_A7EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 2)), scpexpr(EXPR_END)), "loc_A850")

    ChrTalk(
        0x109,
        (
            "#10100FHaha, isn't that a good\x01",
            "thing?\x02\x03",
            "Anyway, let's find her\x01",
            "next hiding place.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AAF4")

    label("loc_A850")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 3)), scpexpr(EXPR_END)), "loc_A8BA")

    ChrTalk(
        0x105,
        (
            "#10300FHehe, being popular is\x01",
            "tough, eh?\x02\x03",
            "Anyway, shall we find\x01",
            "her next hiding place?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AAF4")

    label("loc_A8BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 4)), scpexpr(EXPR_END)), "loc_A919")

    ChrTalk(
        0x153,
        (
            "#01100FEhehe, that's great,\x01",
            "Lloyd.\x02\x03",
            "Then, let's find her\x01",
            "next hiding place!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AAF4")

    label("loc_A919")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 5)), scpexpr(EXPR_END)), "loc_A976")

    ChrTalk(
        0x156,
        (
            "#06400FHaha, isn't that great?\x02\x03",
            "Anyway, let's find her\x01",
            "next hiding place.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AAF4")

    label("loc_A976")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 6)), scpexpr(EXPR_END)), "loc_A9E2")

    ChrTalk(
        0x14C,
        (
            "#05900FHaha. Oh Lloyd, you're\x01",
            "really popular.\x02\x03",
            "Anyway, let's find her\x01",
            "next hiding place.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AAF4")

    label("loc_A9E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 7)), scpexpr(EXPR_END)), "loc_AA3F")

    ChrTalk(
        0x134,
        (
            "#01700FHaha. Isn't that great?\x02\x03",
            "Anyway, let's find her\x01",
            "next hiding place.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AAF4")

    label("loc_AA3F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 0)), scpexpr(EXPR_END)), "loc_AA9C")

    ChrTalk(
        0x135,
        (
            "#01802FHaha, isn't that great?\x02\x03",
            "Anyway, let's find her\x01",
            "next hiding place.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AAF4")

    label("loc_AA9C")


    ChrTalk(
        0x166,
        (
            "#14000FHmph, ain't that just\x01",
            "great.\x02\x03",
            "Anyway, let's look for\x01",
            "her next hiding place.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AAF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 7)), scpexpr(EXPR_END)), "loc_AB1D")

    ChrTalk(
        0x101,
        "#00000FYes, let's go.\x02",
    )

    CloseMessageWindow()
    Jump("loc_AB39")

    label("loc_AB1D")


    ChrTalk(
        0x101,
        "#00000FYeah, let's go.\x02",
    )

    CloseMessageWindow()

    label("loc_AB39")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x1C9, 5)
    OP_65(0x0, 0x1)
    OP_29(0x7F, 0x1, 0xD)
    SetChrPos(0x0, -200, 10, -18640, 180)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_51_A360 end

    def Function_52_AB69(): pass

    label("Function_52_AB69")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch10200.itc", 0x1E)
    LoadChrToIndex("chr/ch45400.itc", 0x1F)
    LoadChrToIndex("chr/ch24400.itc", 0x20)
    LoadChrToIndex("chr/ch24500.itc", 0x21)
    LoadChrToIndex("apl/ch50387.itc", 0x22)
    LoadEffect(0x0, "event\\eva02_00.eff")
    LoadEffect(0x1, "battle/ms00109.eff")
    SoundLoad(810)
    SoundLoad(862)
    SoundLoad(645)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x103, 0x1F)
    SetChrSubChip(0x103, 0x0)
    SetChrFlags(0x103, 0x1000)
    SetChrChipByIndex(0x1C, 0x20)
    SetChrFlags(0x1C, 0x8000)
    SetChrChipByIndex(0x1D, 0x21)
    SetChrFlags(0x1D, 0x8000)
    OP_68(-510, 3010, -21510, 0)
    MoveCamera(48, 32, 0, 0)
    OP_6E(1000, 0)
    SetCameraDistance(6590, 0)
    SetChrPos(0x101, 840, 1910, -27360, 0)
    SetChrPos(0x103, -60, 2190, -28450, 0)
    SetChrPos(0x102, 2750, 0, -18900, 180)
    SetChrPos(0x104, 2750, 90, -20300, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrFlags(0x109, 0x80)
    SetChrFlags(0x105, 0x80)
    OP_68(-1330, 3010, -21710, 3000)
    SetCameraDistance(8010, 3000)
    FadeToBright(1000, 0)
    OP_0D()

    def lambda_ACA6():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_ACA6)
    Sleep(50)

    def lambda_ACC3():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_ACC3)
    Sleep(500)
    OP_63(0x102, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    WaitChrThread(0x103, 1)
    OP_6F(0x79)
    OP_63(0x101, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_AD3A():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AD3A)
    Sleep(50)

    def lambda_AD4A():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_AD4A)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05200FAh, Elie and Randy.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(6870, 3000)

    def lambda_AD87():

        label("loc_AD87")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_AD87")

    QueueWorkItem2(0x102, 1, lambda_AD87)

    def lambda_AD99():

        label("loc_AD99")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_AD99")

    QueueWorkItem2(0x104, 1, lambda_AD99)

    def lambda_ADAB():
        OP_95(0xFE, 860, 0, -18960, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_ADAB)
    Sleep(50)

    def lambda_ADC8():
        OP_95(0xFE, -120, 50, -20150, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_ADC8)
    WaitChrThread(0x101, 1)

    def lambda_ADE6():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_ADE6)
    WaitChrThread(0x103, 1)

    def lambda_ADF7():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_ADF7)
    OP_6F(0x10)
    Sleep(300)

    ChrTalk(
        0x104,
        "#00309FYo, nice work.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FUhuhu. It looks like\x01",
            "both of you are working\x01",
            "hard.\x02\x03",
            "How is it going?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05212FWell, it's pretty\x01",
            "difficult... It's hot\x01",
            "inside this Mishy costume.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05526FLloyd... We're not out for an\x01",
            "afternoon stroll.\x02\x03",
            "#05521FYou have to exude friendliness,\x01",
            "conveying a "You found me!\x01",
            "Lucky☆" kind of feeling.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05206FY-Yeah... Got it.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109FTio... When you're\x01",
            "Mishy, you seem\x01",
            "different, somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00304FHaha, you're so spoiled,\x01",
            "Lloyd.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x1D, 0x80)
    SetChrPos(0x1D, 2880, 1730, -1360, 170)

    NpcTalk(
        0x1D,
        "Woman's Voice",
        "Ah, it's Mishy!\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_B08B():
        TurnDirection(0xFE, 0x1C, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B08B)
    Sleep(50)

    def lambda_B09B():
        OP_95(0xFE, -7940, 0, -14050, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_B09B)
    Sleep(50)

    def lambda_B0B8():
        TurnDirection(0xFE, 0x1C, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B0B8)
    Sleep(50)

    def lambda_B0C8():
        TurnDirection(0xFE, 0x1C, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_B0C8)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    SetChrPos(0x1C, 2710, 800, -7600, 180)
    SetChrPos(0x1D, 1300, 1050, -7030, 180)
    OP_68(-1280, 3010, -20050, 3000)

    def lambda_B112():
        OP_95(0xFE, 1930, 0, -16000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_B112)
    Sleep(50)

    def lambda_B12F():
        OP_95(0xFE, 830, 0, -15580, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_B12F)
    OP_6F(0x1)
    WaitChrThread(0x1C, 1)
    OP_93(0x1C, 0xE1, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x1C,
        (
            "Haha, it really is. We're\x01",
            "lucky to see him right after\x01",
            "we got off the ferris wheel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "Aww, how cute☆. Take my\x01",
            "picture, ok?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        "Yeah, right.\x02",
    )

    CloseMessageWindow()
    OP_95(0x1C, 2800, 0, -17840, 2000, 0x0)
    TurnDirection(0x1C, 0x102, 500)

    def lambda_B20A():
        TurnDirection(0xFE, 0x1C, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B20A)
    Sleep(50)

    def lambda_B21A():
        TurnDirection(0xFE, 0x1C, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_B21A)
    Sleep(300)

    ChrTalk(
        0x1C,
        (
            "Umm, excuse me. Will you\x01",
            "take our picture?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FYes, sure.\x02",
    )

    CloseMessageWindow()
    OP_93(0x104, 0x10E, 0x1F4)
    OP_68(-1870, 3010, -20590, 3000)
    OP_95(0x102, 0, 690, -22620, 2000, 0x0)
    OP_93(0x102, 0x0, 0x1F4)
    Sleep(300)
    OP_6F(0x1)
    Fade(250)
    SetChrChipByIndex(0x102, 0x22)
    SetChrSubChip(0x102, 0x0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05203F(A p-picture...? What\x01",
            "should I do in this\x01",
            "situation?)\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Stand near him\x01",          # 0
            "Stand near her\x01",          # 1
            "Stand between them\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-2290, 3010, -22170, 0)
    MoveCamera(35, 29, 0, 0)
    OP_6E(1000, 0)
    SetCameraDistance(5360, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_B3AE"),
        (1, "loc_B480"),
        (2, "loc_B55E"),
        (SWITCH_DEFAULT, "loc_B618"),
    )


    label("loc_B3AE")

    SetChrPos(0x101, 0, 0, -18900, 180)
    SetChrPos(0x1C, 1000, 0, -18900, 180)
    SetChrPos(0x1D, -1000, 0, -18900, 180)
    FadeToBright(1000, 0)
    OP_0D()
    BeginChrThread(0x101, 3, 0, 53)
    WaitChrThread(0x101, 3)
    Sleep(500)
    OP_63(0x1D, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x1D,
        "Eek, no faaair!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "Hahaha, it's ok, it's\x01",
            "ok.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109FAlright, here I go.\x02\x03",
            "#00102FSay cheese!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B618")

    label("loc_B480")

    SetChrPos(0x101, 0, 0, -18900, 180)
    SetChrPos(0x1C, 1000, 0, -18900, 180)
    SetChrPos(0x1D, -1000, 0, -18900, 180)
    FadeToBright(1000, 0)
    OP_0D()
    BeginChrThread(0x101, 3, 0, 54)
    WaitChrThread(0x101, 3)
    Sleep(500)

    ChrTalk(
        0x1D,
        (
            "Eek, yes! Mishy is all\x01",
            "miiine～♪\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        "H-Hahaha... (*sad*...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00111F(*sad*...)\x02\x03",
            "#00109F...Umm. Then, here I go.\x02\x03",
            "#00102FSay cheese!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B618")

    label("loc_B55E")

    OP_2C(0x86, 0x1)
    SetScenarioFlags(0x176, 7)
    SetChrPos(0x101, 0, 0, -18900, 180)
    SetChrPos(0x1C, 1000, 0, -18900, 180)
    SetChrPos(0x1D, -1000, 0, -18900, 180)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x1D,
        (
            "Uhuhu. Today is my Mishy\x01",
            "anniversary!☆\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        "Go ahead.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109FAlright, here I go.\x02\x03",
            "#00102FSay cheese!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B618")

    label("loc_B618")

    Sound(810, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0x102, 0x3, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)

    ChrTalk(
        0x1D,
        "Thank you very much.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        "Thanks.\x02",
    )

    CloseMessageWindow()

    def lambda_B684():
        OP_95(0xFE, 0, 440, -21620, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_B684)
    Sleep(50)

    def lambda_B6A1():
        OP_95(0xFE, -1000, 440, -20620, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_B6A1)
    WaitChrThread(0x1D, 1)

    def lambda_B6BF():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_B6BF)
    WaitChrThread(0x1C, 1)

    def lambda_B6D0():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_B6D0)
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    Sleep(500)

    ChrTalk(
        0x102,
        "#00100FHere you go.\x02",
    )

    CloseMessageWindow()
    OP_97(0x1C, 0xFFFFFC18, 0x0, 0x0, 0x7D0, 0x0)

    def lambda_B71D():
        OP_95(0xFE, -940, 2840, -31020, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_B71D)
    Sleep(50)

    def lambda_B73A():
        OP_95(0xFE, -940, 2840, -31020, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_B73A)
    Sleep(50)

    def lambda_B757():
        OP_95(0xFE, 0, 0, -18900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B757)

    def lambda_B771():
        OP_95(0xFE, -400, 0, -17600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_B771)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0xB4, 0x1F4)
    WaitChrThread(0x103, 1)
    TurnDirection(0x103, 0x101, 500)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x1D, 0x80)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B920")

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05204FPhew... Was that\x01",
            "alright?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Sound(2680, 255, 100, 0)

    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05524FThat was perfect.\x02\x03",
            "#05520FMishy is the symbol of the\x01",
            "theme park, so to speak... He's\x01",
            "like a walking attraction.\x02\x03",
            "#05524FIn situations like that, it's\x01",
            "best to stand in the center of\x01",
            "the picture.\x02\x03",
            "#05522FYou're getting used to being\x01",
            "Mishy, aren't you.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05209FHaha, thanks.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x86, 0x1, 0x5)
    Jump("loc_BBD0")

    label("loc_B920")


    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05204F*sigh*... Was it all\x01",
            "righ──\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x103, 0x101, 0xFA, 0x1388, 0x0)
    PlayEffect(0x1, 0x0, 0xFF, 0x0, 0, 300, -18900, 180, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sound(645, 0, 30, 0)
    Sound(862, 0, 50, 0)
    Sound(811, 0, 100, 0)
    OP_9B(0x1, 0x103, 0xB4, 0x3E8, 0x1388, 0x0)
    Sleep(500)
    Sound(3318, 255, 100, 0)

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05211FAck!?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xCF6)
    TurnDirection(0x101, 0x103, 500)
    Sound(2682, 255, 100, 0)

    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05526F...What a\x01",
            "disappointment, Mr.\x01",
            "Lloyd.\x02\x03",
            "#05531F...Why did you change\x01",
            "position on purpose?\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05205FW-Well... I wondered\x01",
            "about getting between a\x01",
            "couple...\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05526F*sight*... Please think\x01",
            "carefully.\x02\x03",
            "#05520FMishy is the symbol of the\x01",
            "theme park, so to speak... He's\x01",
            "like a walking attraction.\x02\x03",
            "#05531FIn situations like that, I\x01",
            "think it's better if you stand\x01",
            "properly between them.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05206FI-I see... (It would\x01",
            "have been better if I\x01",
            "didn't do that...)\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x86, 0x1, 0x6)

    label("loc_BBD0")


    ChrTalk(
        0x102,
        (
            "#00104FHaha. Since Tio's there,\x01",
            "I'm sure everything will\x01",
            "be all right.\x02\x03",
            "#00100FKeep up the good work,\x01",
            "you two. We'll be\x01",
            "watching.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309FGahaha, we'll be on our\x01",
            "date!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x104, 1000)
    Sleep(300)

    ChrTalk(
        0x102,
        "#00103FWe will not.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x102, 500)
    Sleep(300)

    ChrTalk(
        0x104,
        "#00306FUgh, rejected!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05200FHaha... We'll do the\x01",
            "best we can.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05520FThen, let's move on to\x01",
            "the next attraction,\x01",
            "shall we?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 2)
    NewScene("t1300", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_52_AB69 end

    def Function_53_BD60(): pass

    label("Function_53_BD60")

    OP_97(0x101, 0x0, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
    OP_97(0x101, 0x6A4, 0x0, 0x0, 0x7D0, 0x0)
    OP_97(0x101, 0x0, 0x0, 0x3E8, 0x7D0, 0x0)

    def lambda_BDA1():
        OP_97(0xFE, 0xFFFFFC18, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_BDA1)
    Sleep(50)

    def lambda_BDBE():
        OP_97(0xFE, 0xFFFFFE0C, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BDBE)
    WaitChrThread(0x1C, 1)

    def lambda_BDDC():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_BDDC)
    WaitChrThread(0x101, 1)

    def lambda_BDED():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BDED)
    Return()

    # Function_53_BD60 end

    def Function_54_BDF6(): pass

    label("Function_54_BDF6")

    OP_97(0x101, 0x0, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
    OP_97(0x101, 0xFFFFF95C, 0x0, 0x0, 0x7D0, 0x0)
    OP_97(0x101, 0x0, 0x0, 0x3E8, 0x7D0, 0x0)

    def lambda_BE37():
        OP_97(0xFE, 0x3E8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_BE37)
    Sleep(50)

    def lambda_BE54():
        OP_97(0xFE, 0x1F4, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BE54)
    WaitChrThread(0x1D, 1)

    def lambda_BE72():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_BE72)
    WaitChrThread(0x101, 1)

    def lambda_BE83():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BE83)
    Return()

    # Function_54_BDF6 end

    def Function_55_BE8C(): pass

    label("Function_55_BE8C")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's a sketch map of the\x01",
            "theme park.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Return()

    # Function_55_BE8C end

    def Function_56_BEC7(): pass

    label("Function_56_BEC7")

    EventBegin(0x1)
    TurnDirection(0x14, 0x0, 500)
    OP_4B(0x14, 0xFF)

    ChrTalk(
        0x14,
        (
            "Ladies and gentlemen, if you are\x01",
            "boarding the Ferris wheel, please\x01",
            "hand in your tickets here.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -330, 0, -15900, 350)
    OP_93(0x14, 0xA0, 0x0)
    OP_4C(0x14, 0xFF)
    EventEnd(0x4)
    Return()

    # Function_56_BEC7 end

    SaveToFile()

Try(main)
