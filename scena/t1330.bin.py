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
        "M. W. L. Staff",         # 13
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
        "Function_4_791",          # 04, 4
        "Function_5_853",          # 05, 5
        "Function_6_A75",          # 06, 6
        "Function_7_B3A",          # 07, 7
        "Function_8_C84",          # 08, 8
        "Function_9_D4D",          # 09, 9
        "Function_10_EF8",         # 0A, 10
        "Function_11_FC2",         # 0B, 11
        "Function_12_10AF",        # 0C, 12
        "Function_13_1164",        # 0D, 13
        "Function_14_1219",        # 0E, 14
        "Function_15_12CC",        # 0F, 15
        "Function_16_1404",        # 10, 16
        "Function_17_145D",        # 11, 17
        "Function_18_14B4",        # 12, 18
        "Function_19_1580",        # 13, 19
        "Function_20_1637",        # 14, 20
        "Function_21_175A",        # 15, 21
        "Function_22_1802",        # 16, 22
        "Function_23_18D2",        # 17, 23
        "Function_24_19A8",        # 18, 24
        "Function_25_1BB1",        # 19, 25
        "Function_26_2652",        # 1A, 26
        "Function_27_268F",        # 1B, 27
        "Function_28_26CC",        # 1C, 28
        "Function_29_27D7",        # 1D, 29
        "Function_30_2839",        # 1E, 30
        "Function_31_28A8",        # 1F, 31
        "Function_32_291F",        # 20, 32
        "Function_33_298A",        # 21, 33
        "Function_34_29F5",        # 22, 34
        "Function_35_2A40",        # 23, 35
        "Function_36_2AB1",        # 24, 36
        "Function_37_2BF0",        # 25, 37
        "Function_38_2C2E",        # 26, 38
        "Function_39_2C76",        # 27, 39
        "Function_40_2CB6",        # 28, 40
        "Function_41_3748",        # 29, 41
        "Function_42_434A",        # 2A, 42
        "Function_43_4F91",        # 2B, 43
        "Function_44_59B4",        # 2C, 44
        "Function_45_6560",        # 2D, 45
        "Function_46_703D",        # 2E, 46
        "Function_47_7A6E",        # 2F, 47
        "Function_48_85A3",        # 30, 48
        "Function_49_92D1",        # 31, 49
        "Function_50_9D57",        # 32, 50
        "Function_51_A835",        # 33, 51
        "Function_52_B074",        # 34, 52
        "Function_53_C2EA",        # 35, 53
        "Function_54_C380",        # 36, 54
        "Function_55_C416",        # 37, 55
        "Function_56_C455",        # 38, 56
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
    Jump("loc_78D")

    label("loc_6CC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6E2")
    Jump("loc_78D")

    label("loc_6E2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_766")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_705")
    Call(0, 21)
    Jump("loc_761")

    label("loc_705")


    ChrTalk(
        0x8,
        (
            "#00102F*giggle*, I'll go buy the drinks, so please,\x01",
            "take your time and relax yourself.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_761")

    Jump("loc_78D")

    label("loc_766")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_77C")
    Jump("loc_78D")

    label("loc_77C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_78D")

    label("loc_78D")

    TalkEnd(0xFE)
    Return()

    # Function_3_6B3 end

    def Function_4_791(): pass

    label("Function_4_791")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7AA")
    Jump("loc_84F")

    label("loc_7AA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_812")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7CD")
    Call(0, 22)
    Jump("loc_80D")

    label("loc_7CD")


    ChrTalk(
        0x9,
        (
            "#00204FAs expected from Miss Fran...\x01",
            "She catches on quick.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_80D")

    Jump("loc_84F")

    label("loc_812")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_828")
    Jump("loc_84F")

    label("loc_828")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_83E")
    Jump("loc_84F")

    label("loc_83E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_84F")

    label("loc_84F")

    TalkEnd(0xFE)
    Return()

    # Function_4_791 end

    def Function_5_853(): pass

    label("Function_5_853")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_86C")
    Jump("loc_A71")

    label("loc_86C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_882")
    Jump("loc_A71")

    label("loc_882")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_898")
    Jump("loc_A71")

    label("loc_898")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A60")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9B6")

    ChrTalk(
        0xA,
        (
            "#00300FSome time ago, I thought to try\x01",
            "to chat up a lady who came out\x01",
            "the ferris wheel and was my type, but...\x02\x03",
            "#00306FIt looked like she\x01",
            "came as a couple.\x02\x03",
            "#00302FMan, as I suspected, maybe it's too\x01",
            "difficult to pick up girls at the theme park.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_A5B")

    label("loc_9B6")


    ChrTalk(
        0xA,
        (
            "#00306FThinkin' about it, there're many\x01",
            "customers who're couples or families...\x02\x03",
            "#00302FAs I suspected, maybe it's too hard\x01",
            "to pick up girls at the theme park.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A5B")

    Jump("loc_A71")

    label("loc_A60")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A71")

    label("loc_A71")

    TalkEnd(0xFE)
    Return()

    # Function_5_853 end

    def Function_6_A75(): pass

    label("Function_6_A75")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A8E")
    Jump("loc_B36")

    label("loc_A8E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AA4")
    Jump("loc_B36")

    label("loc_AA4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ABA")
    Jump("loc_B36")

    label("loc_ABA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AD0")
    Jump("loc_B36")

    label("loc_AD0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B36")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AF3")
    Call(0, 23)
    Jump("loc_B36")

    label("loc_AF3")


    ChrTalk(
        0xB,
        (
            "#10100FOh, Mr. Lloyd.\x01",
            "Have you decided what to ride for last?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B36")

    TalkEnd(0xFE)
    Return()

    # Function_6_A75 end

    def Function_7_B3A(): pass

    label("Function_7_B3A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C2D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BDD")

    ChrTalk(
        0xC,
        (
            "#10304FWatching people like\x01",
            "this is not bad too.\x02\x03",
            "#10302FHu hu, unexpectedly, the man\x01",
            "inside Michey could be somewhere.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_C28")

    label("loc_BDD")


    ChrTalk(
        0xC,
        (
            "#10302FHu hu, unexpectedly, the man\x01",
            "inside Michey could be somewhere.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C28")

    Jump("loc_C80")

    label("loc_C2D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C43")
    Jump("loc_C80")

    label("loc_C43")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C59")
    Jump("loc_C80")

    label("loc_C59")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C6F")
    Jump("loc_C80")

    label("loc_C6F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C80")

    label("loc_C80")

    TalkEnd(0xFE)
    Return()

    # Function_7_B3A end

    def Function_8_C84(): pass

    label("Function_8_C84")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C9D")
    Jump("loc_D49")

    label("loc_C9D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CB3")
    Jump("loc_D49")

    label("loc_CB3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D22")

    ChrTalk(
        0xD,
        (
            "#01102FI knew it, this\x01",
            "lake is pretty.\x02\x03",
            "#01109FI think it's clear until the bottom.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D49")

    label("loc_D22")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D38")
    Jump("loc_D49")

    label("loc_D38")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D49")

    label("loc_D49")

    TalkEnd(0xFE)
    Return()

    # Function_8_C84 end

    def Function_9_D4D(): pass

    label("Function_9_D4D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D66")
    Jump("loc_EF4")

    label("loc_D66")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DDF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D89")
    Call(0, 22)
    Jump("loc_DDA")

    label("loc_D89")


    ChrTalk(
        0xE,
        (
            "#06409FLike Tio says, \x01",
            "I'm sure that sun face\x01",
            "is the key to its popularity!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DDA")

    Jump("loc_EF4")

    label("loc_DDF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DF5")
    Jump("loc_EF4")

    label("loc_DF5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E0B")
    Jump("loc_EF4")

    label("loc_E0B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EF4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E2E")
    Call(0, 23)
    Jump("loc_EF4")

    label("loc_E2E")


    ChrTalk(
        0xE,
        (
            "#06402FIt seems that the view from \x01",
            "the ferris wheel at this \x01",
            "hour is outstandingly nice.\x02\x03",
            "#06409FIf you haven't decided what to ride,\x01",
            "why don't you ride that together\x01",
            "with someone, Mr. Lloyd?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EF4")

    TalkEnd(0xFE)
    Return()

    # Function_9_D4D end

    def Function_10_EF8(): pass

    label("Function_10_EF8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F11")
    Jump("loc_FBE")

    label("loc_F11")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F27")
    Jump("loc_FBE")

    label("loc_F27")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F97")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F4A")
    Call(0, 21)
    Jump("loc_F92")

    label("loc_F4A")


    ChrTalk(
        0xF,
        (
            "#05909FUh uh, in this case, I think\x01",
            "I will accept your suggestion.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F92")

    Jump("loc_FBE")

    label("loc_F97")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FAD")
    Jump("loc_FBE")

    label("loc_FAD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FBE")

    label("loc_FBE")

    TalkEnd(0xFE)
    Return()

    # Function_10_EF8 end

    def Function_11_FC2(): pass

    label("Function_11_FC2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FDB")
    Jump("loc_10AB")

    label("loc_FDB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FF1")
    Jump("loc_10AB")

    label("loc_FF1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1007")
    Jump("loc_10AB")

    label("loc_1007")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_109A")

    ChrTalk(
        0x10,
        (
            "#14006F*haah*, because I've played too much,\x01",
            "somehow now I'm tired.\x02\x03",
            "#14000FI guess I'll catch some\x01",
            "breeze for a while.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10AB")

    label("loc_109A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10AB")

    label("loc_10AB")

    TalkEnd(0xFE)
    Return()

    # Function_11_FC2 end

    def Function_12_10AF(): pass

    label("Function_12_10AF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10C8")
    Jump("loc_1160")

    label("loc_10C8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1123")

    ChrTalk(
        0x11,
        (
            "Ha ha, it looks like that Rimah \x01",
            "really liked the ferris wheel.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1160")

    label("loc_1123")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1139")
    Jump("loc_1160")

    label("loc_1139")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_114F")
    Jump("loc_1160")

    label("loc_114F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1160")

    label("loc_1160")

    TalkEnd(0xFE)
    Return()

    # Function_12_10AF end

    def Function_13_1164(): pass

    label("Function_13_1164")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_117D")
    Jump("loc_1215")

    label("loc_117D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11D8")

    ChrTalk(
        0x12,
        (
            "My my, Rimah...\x01",
            "There're still other\x01",
            "attractions too, you know?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1215")

    label("loc_11D8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11EE")
    Jump("loc_1215")

    label("loc_11EE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1204")
    Jump("loc_1215")

    label("loc_1204")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1215")

    label("loc_1215")

    TalkEnd(0xFE)
    Return()

    # Function_13_1164 end

    def Function_14_1219(): pass

    label("Function_14_1219")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1232")
    Jump("loc_12C8")

    label("loc_1232")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_128B")

    ChrTalk(
        0x13,
        (
            "Papa, let's do another round!\x01",
            "I wanna see Orchis Tower again!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12C8")

    label("loc_128B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12A1")
    Jump("loc_12C8")

    label("loc_12A1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12B7")
    Jump("loc_12C8")

    label("loc_12B7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12C8")

    label("loc_12C8")

    TalkEnd(0xFE)
    Return()

    # Function_14_1219 end

    def Function_15_12CC(): pass

    label("Function_15_12CC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1400")
    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "This attraction is the\x01",
            ""Sunshine Mole" ferris wheel!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "With one revolution of your\x01",
            "gondola, you leisurely enjoy\x01",
            "the best view in Michelam.\x02",
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
    TalkEnd(0xFE)
    Jump("loc_1403")

    label("loc_1400")

    Call(0, 25)

    label("loc_1403")

    Return()

    # Function_15_12CC end

    def Function_16_1404(): pass

    label("Function_16_1404")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1459")

    ChrTalk(
        0x15,
        (
            "Let's ride the ferris wheel!\x01",
            "The view will be amazing!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1459")

    label("loc_1459")

    TalkEnd(0xFE)
    Return()

    # Function_16_1404 end

    def Function_17_145D(): pass

    label("Function_17_145D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14B0")

    ChrTalk(
        0x16,
        (
            "I told you no, I'm not\x01",
            "really good with high places!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14B0")

    label("loc_14B0")

    TalkEnd(0xFE)
    Return()

    # Function_17_145D end

    def Function_18_14B4(): pass

    label("Function_18_14B4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1511")

    ChrTalk(
        0x17,
        (
            "*burp*...\x01",
            "I've got completely sick\x01",
            "of the gondola's swaying...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_157C")

    label("loc_1511")


    ChrTalk(
        0x17,
        (
            "H-Hey...\x01",
            "Can't we have something\x01",
            "else to ride for last?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        "I don't really want to get sick again...\x02",
    )

    CloseMessageWindow()

    label("loc_157C")

    TalkEnd(0xFE)
    Return()

    # Function_18_14B4 end

    def Function_19_1580(): pass

    label("Function_19_1580")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15D0")

    ChrTalk(
        0x18,
        (
            "Honestly, it's our long awaited date,\x01",
            "get a grip.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1633")

    label("loc_15D0")


    ChrTalk(
        0x18,
        (
            "It's fine, fine!\x01",
            "When I'll see the evening sun from the top,\x01",
            "getting sick won't be a problem!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1633")

    TalkEnd(0xFE)
    Return()

    # Function_19_1580 end

    def Function_20_1637(): pass

    label("Function_20_1637")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_16B9")

    ChrTalk(
        0x19,
        (
            "Riding the ferris wheel alone\x01",
            "needs quite the courage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "...I should've come\x01",
            "with a male friend.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1756")

    label("loc_16B9")


    ChrTalk(
        0x19,
        (
            "The view from the top was great.\x01",
            "It was really the right choice to\x01",
            "muster up my courage and ride it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "Well, riding alone was\x01",
            "somehow sad, though...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1756")

    TalkEnd(0xFE)
    Return()

    # Function_20_1637 end

    def Function_21_175A(): pass

    label("Function_21_175A")

    OP_4B(0x8, 0xFF)
    OP_4B(0xF, 0xFF)

    ChrTalk(
        0x8,
        (
            "#00100FThen, I will go buy\x01",
            "something to drink.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#05905FOh, but no.\x01",
            "I will go instead.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#00102F*giggle*, Miss Cecil,\x01",
            "please relax here.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    OP_4C(0x8, 0xFF)
    OP_4C(0xF, 0xFF)
    Return()

    # Function_21_175A end

    def Function_22_1802(): pass

    label("Function_22_1802")

    OP_4B(0x9, 0xFF)
    OP_4B(0xE, 0xFF)

    ChrTalk(
        0x9,
        (
            "#00204FAs expected, the ferris wheel\x01",
            "seems to be popular too.\x02\x03",
            "#00200FThe sun face at its center...\x01",
            "Could that be\x01",
            "its winning point?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#06409FAhaha, it must be for sure!\x02",
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)
    OP_4C(0xE, 0xFF)
    SetScenarioFlags(0x0, 1)
    ClearChrFlags(0x9, 0x10)
    ClearChrFlags(0xE, 0x10)
    Return()

    # Function_22_1802 end

    def Function_23_18D2(): pass

    label("Function_23_18D2")

    OP_4B(0xB, 0xFF)
    OP_4B(0xE, 0xFF)

    ChrTalk(
        0xE,
        (
            "#06400FAccording to the guide book,\x01",
            "the view from the ferris wheel at\x01",
            "this hour is outstandingly nice!\x02\x03",
            "#06409FBig sis, let's ride it later!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#10100FUh uh, should we do that?\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0xE, 0x10)
    SetScenarioFlags(0x0, 2)
    OP_4C(0xB, 0xFF)
    OP_4C(0xE, 0xFF)
    Return()

    # Function_23_18D2 end

    def Function_24_19A8(): pass

    label("Function_24_19A8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1A0D")
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

    label("loc_1A0D")

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
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A6B")
    ClearChrFlags(0xC, 0x80)
    SetChrChipByIndex(0xC, 0x12)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    Jump("loc_1BB0")

    label("loc_1A6B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1AC4")
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
    Jump("loc_1BB0")

    label("loc_1AC4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1AF3")
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x10)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x10)
    Jump("loc_1BB0")

    label("loc_1AF3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B6B")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x10, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1B4B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 1)), scpexpr(EXPR_END)), "loc_1B3D")
    SetChrFlags(0xA, 0x80)
    Jump("loc_1B4B")

    label("loc_1B3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 1)), scpexpr(EXPR_END)), "loc_1B4B")
    SetChrFlags(0x10, 0x80)

    label("loc_1B4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1B66")
    ClearChrFlags(0x1A, 0x80)

    label("loc_1B66")

    Jump("loc_1BB0")

    label("loc_1B6B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BB0")
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x10)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 6760, 10, -15090, 115)
    SetChrFlags(0xE, 0x10)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x10)

    label("loc_1BB0")

    Return()

    # Function_24_19A8 end

    def Function_25_1BB1(): pass

    label("Function_25_1BB1")

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
            "This attraction is the\x01",
            ""Sunshine Mole" ferris wheel!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "With one revolution of your\x01",
            "gondola, you leisurely enjoy\x01",
            "the best view in Michelam.\x02",
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
        "#00004F#12P(...Who should I invite?)\x02",
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
    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_1DA7")
    MenuCmd(3, 0, 0x0)

    label("loc_1DA7")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_1DB9")
    MenuCmd(3, 0, 0x1)

    label("loc_1DB9")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_1DCB")
    MenuCmd(3, 0, 0x2)

    label("loc_1DCB")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_1DDD")
    MenuCmd(3, 0, 0x3)

    label("loc_1DDD")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_1DEF")
    MenuCmd(3, 0, 0x4)

    label("loc_1DEF")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x20), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_1E01")
    MenuCmd(3, 0, 0x5)

    label("loc_1E01")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x40), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_1E13")
    MenuCmd(3, 0, 0x6)

    label("loc_1E13")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_1E25")
    MenuCmd(3, 0, 0x7)

    label("loc_1E25")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x100), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_1E37")
    MenuCmd(3, 0, 0x8)

    label("loc_1E37")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x200), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_1E49")
    MenuCmd(3, 0, 0x9)

    label("loc_1E49")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x400), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_1E5B")
    MenuCmd(3, 0, 0xA)

    label("loc_1E5B")

    MenuCmd(2, 0, -1, 55, 0)
    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_25F1")
    OP_D2(0x5, (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1EE1"),
        (1, "loc_1F24"),
        (2, "loc_1F66"),
        (3, "loc_1FAA"),
        (4, "loc_1FED"),
        (5, "loc_2030"),
        (6, "loc_2072"),
        (7, "loc_20B5"),
        (8, "loc_2100"),
        (9, "loc_2148"),
        (10, "loc_218C"),
        (SWITCH_DEFAULT, "loc_21D0"),
    )


    label("loc_1EE1")

    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        "#00000F#12P(Alright...I'll try to invite Elie.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_21D0")

    label("loc_1F24")

    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        "#00000F#12P(Alright...I'll try to invite Tio.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_21D0")

    label("loc_1F66")

    OP_50(0x67, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        "#00000F#12P(Alright...I'll try to invite Randy.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_21D0")

    label("loc_1FAA")

    OP_50(0x68, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        "#00000F#12P(Alright...I'll try to invite Noｱl.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_21D0")

    label("loc_1FED")

    OP_50(0x69, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        "#00000F#12P(Alright...I'll try to invite Wazy.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_21D0")

    label("loc_2030")

    OP_50(0x64, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        "#00000F#12P(Alright...I'll try to invite KeA.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_21D0")

    label("loc_2072")

    OP_50(0x6E, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        "#00000F#12P(Alright...I'll try to invite Fran.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_21D0")

    label("loc_20B5")

    OP_50(0x6D, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        "#00000F#12P(Alright...I'll try to invite sister Cecil.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_21D0")

    label("loc_2100")

    OP_50(0x6C, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        "#00000F#12P(Alright...I'll try to invite Miss Ilya.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_21D0")

    label("loc_2148")

    OP_50(0x6A, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        "#00000F#12P(Alright...I'll try to invite Rixia.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_21D0")

    label("loc_218C")

    OP_50(0x6F, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        "#00000F#12P(Alright...I'll try to invite Sully.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_21D0")

    label("loc_21D0")

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
        (0, "loc_224D"),
        (1, "loc_225C"),
        (2, "loc_226B"),
        (3, "loc_227A"),
        (4, "loc_2289"),
        (5, "loc_2292"),
        (6, "loc_22A1"),
        (7, "loc_22B0"),
        (8, "loc_22BF"),
        (9, "loc_22CE"),
        (10, "loc_22DD"),
        (SWITCH_DEFAULT, "loc_22EC"),
    )


    label("loc_224D")

    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    SetChrChipByIndex(0x1B, 0x0)
    Jump("loc_22EC")

    label("loc_225C")

    LoadChrToIndex("chr/ch00202.itc", 0x1F)
    SetChrChipByIndex(0x1B, 0x1)
    Jump("loc_22EC")

    label("loc_226B")

    LoadChrToIndex("chr/ch00302.itc", 0x1F)
    SetChrChipByIndex(0x1B, 0x2)
    Jump("loc_22EC")

    label("loc_227A")

    LoadChrToIndex("chr/ch02902.itc", 0x1F)
    SetChrChipByIndex(0x1B, 0x3)
    Jump("loc_22EC")

    label("loc_2289")

    SetChrChipByIndex(0x1B, 0x4)
    Jump("loc_22EC")

    label("loc_2292")

    LoadChrToIndex("chr/ch08202.itc", 0x1F)
    SetChrChipByIndex(0x1B, 0x5)
    Jump("loc_22EC")

    label("loc_22A1")

    LoadChrToIndex("chr/ch08502.itc", 0x1F)
    SetChrChipByIndex(0x1B, 0x6)
    Jump("loc_22EC")

    label("loc_22B0")

    LoadChrToIndex("chr/ch07502.itc", 0x1F)
    SetChrChipByIndex(0x1B, 0x7)
    Jump("loc_22EC")

    label("loc_22BF")

    LoadChrToIndex("chr/ch05102.itc", 0x1F)
    SetChrChipByIndex(0x1B, 0x20)
    Jump("loc_22EC")

    label("loc_22CE")

    LoadChrToIndex("chr/ch05202.itc", 0x1F)
    SetChrChipByIndex(0x1B, 0x21)
    Jump("loc_22EC")

    label("loc_22DD")

    LoadChrToIndex("chr/ch10002.itc", 0x1F)
    SetChrChipByIndex(0x1B, 0x8)
    Jump("loc_22EC")

    label("loc_22EC")

    SetChrSubChip(0x1B, 0x0)
    SetChrPos(0x101, -950, 0, -16000, 0)
    SetChrPos(0x1B, -250, 0, -16700, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x14,
        "Then, I'll take your ticket.\x02",
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
        0x14,
        "Two people, coming in!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrChipByIndex(0x101, 0x1E)
    Jc((scpexpr(EXPR_23, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_23E0")
    SetChrChipByIndex(0x1B, 0x12)
    Jump("loc_23E4")

    label("loc_23E0")

    SetChrChipByIndex(0x1B, 0x1F)

    label("loc_23E4")

    SetChrFlags(0x101, 0x4)
    SetChrPos(0x101, 999000, 200, 0, 90)
    SetChrPos(0x1B, 1001000, 200, 0, 270)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2457"),
        (1, "loc_245F"),
        (2, "loc_2467"),
        (3, "loc_246F"),
        (4, "loc_2477"),
        (5, "loc_247F"),
        (6, "loc_2487"),
        (7, "loc_248F"),
        (8, "loc_2497"),
        (9, "loc_249F"),
        (10, "loc_24A7"),
        (SWITCH_DEFAULT, "loc_24AF"),
    )


    label("loc_2457")

    Call(0, 40)
    Jump("loc_24AF")

    label("loc_245F")

    Call(0, 41)
    Jump("loc_24AF")

    label("loc_2467")

    Call(0, 42)
    Jump("loc_24AF")

    label("loc_246F")

    Call(0, 43)
    Jump("loc_24AF")

    label("loc_2477")

    Call(0, 44)
    Jump("loc_24AF")

    label("loc_247F")

    Call(0, 45)
    Jump("loc_24AF")

    label("loc_2487")

    Call(0, 46)
    Jump("loc_24AF")

    label("loc_248F")

    Call(0, 47)
    Jump("loc_24AF")

    label("loc_2497")

    Call(0, 48)
    Jump("loc_24AF")

    label("loc_249F")

    Call(0, 49)
    Jump("loc_24AF")

    label("loc_24A7")

    Call(0, 50)
    Jump("loc_24AF")

    label("loc_24AF")

    SetChrFlags(0x1B, 0x80)
    OP_49()
    OP_D7(0x1E)
    Jc((scpexpr(EXPR_23, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_24C7")
    OP_D7(0x1F)

    label("loc_24C7")

    OP_D7(0x20)
    OP_D7(0x21)
    OP_D7(0x22)
    OP_D7(0x23)
    Switch(
        (scpexpr(EXPR_23, 0x5), scpexpr(EXPR_END)),
        (0, "loc_251A"),
        (1, "loc_2528"),
        (2, "loc_2536"),
        (3, "loc_2544"),
        (4, "loc_2552"),
        (5, "loc_2560"),
        (6, "loc_256E"),
        (7, "loc_257C"),
        (8, "loc_258A"),
        (9, "loc_2598"),
        (10, "loc_25A6"),
        (SWITCH_DEFAULT, "loc_25B4"),
    )


    label("loc_251A")

    OP_D2(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_25B4")

    label("loc_2528")

    OP_D2(0x3, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_25B4")

    label("loc_2536")

    OP_D2(0x3, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_25B4")

    label("loc_2544")

    OP_D2(0x3, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_25B4")

    label("loc_2552")

    OP_D2(0x3, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_25B4")

    label("loc_2560")

    OP_D2(0x3, (scpexpr(EXPR_PUSH_LONG, 0x20), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_25B4")

    label("loc_256E")

    OP_D2(0x3, (scpexpr(EXPR_PUSH_LONG, 0x40), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_25B4")

    label("loc_257C")

    OP_D2(0x3, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_25B4")

    label("loc_258A")

    OP_D2(0x3, (scpexpr(EXPR_PUSH_LONG, 0x100), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_25B4")

    label("loc_2598")

    OP_D2(0x3, (scpexpr(EXPR_PUSH_LONG, 0x200), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_25B4")

    label("loc_25A6")

    OP_D2(0x3, (scpexpr(EXPR_PUSH_LONG, 0x400), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_25B4")

    label("loc_25B4")

    OP_D2(0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_25EC")
    StopSound(821, 1000, 40)
    StopSound(126, 1000, 70)
    StopBGM(0xFA0)
    WaitBGM()
    SetScenarioFlags(0x22, 1)
    NewScene("t1300", 0, 0, 0)
    IdleLoop()

    label("loc_25EC")

    Jump("loc_2637")

    label("loc_25F1")


    ChrTalk(
        0x14,
        "Oh, you aren't coming in?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        "We will await your next visit!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_2637")

    Call(0, 27)
    OP_4C(0x14, 0xFF)
    SetChrPos(0x0, 0, 0, -16500, 180)
    EventEnd(0x5)
    Return()

    # Function_25_1BB1 end

    def Function_26_2652(): pass

    label("Function_26_2652")

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

    # Function_26_2652 end

    def Function_27_268F(): pass

    label("Function_27_268F")

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

    # Function_27_268F end

    def Function_28_26CC(): pass

    label("Function_28_26CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_276D")
    SetMapObjFrame(0xFF, "sky01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky_y", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky01_y", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky_in", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky01_in", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky_y_in", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky01_y_in", 0x1, 0x1)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xD5, 0x8F, 0x7B, 0x26, 0x1F4, 0x0)
    Jump("loc_27D6")

    label("loc_276D")

    SetMapObjFrame(0xFF, "sky01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky_y", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky01_y", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky_in", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky01_in", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky_y_in", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky01_y_in", 0x0, 0x1)

    label("loc_27D6")

    Return()

    # Function_28_26CC end

    def Function_29_27D7(): pass

    label("Function_29_27D7")

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

    # Function_29_27D7 end

    def Function_30_2839(): pass

    label("Function_30_2839")

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

    # Function_30_2839 end

    def Function_31_28A8(): pass

    label("Function_31_28A8")

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

    # Function_31_28A8 end

    def Function_32_291F(): pass

    label("Function_32_291F")

    Sound(148, 2, 80, 0)
    Fade(1000)
    SetMapObjFrame(0xFF, "Null_in", 0x2, "loop00")
    OP_68(1000000, 1350, 0, 0)
    Jc((scpexpr(EXPR_23, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_296B")
    MoveCamera(30, 23, 0, 0)
    Jump("loc_2976")

    label("loc_296B")

    MoveCamera(45, 23, 0, 0)

    label("loc_2976")

    OP_6E(600, 0)
    SetCameraDistance(11000, 0)
    OP_0D()
    Return()

    # Function_32_291F end

    def Function_33_298A(): pass

    label("Function_33_298A")

    Sound(148, 2, 80, 0)
    Fade(1000)
    SetMapObjFrame(0xFF, "Null_in", 0x2, "loop01")
    OP_68(1000000, 1350, 0, 0)
    Jc((scpexpr(EXPR_23, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_29D6")
    MoveCamera(30, 23, 0, 0)
    Jump("loc_29E1")

    label("loc_29D6")

    MoveCamera(45, 23, 0, 0)

    label("loc_29E1")

    OP_6E(600, 0)
    SetCameraDistance(11000, 0)
    OP_0D()
    Return()

    # Function_33_298A end

    def Function_34_29F5(): pass

    label("Function_34_29F5")

    Sound(148, 2, 80, 0)
    Fade(1000)
    SetMapObjFrame(0xFF, "Null_in", 0x2, "goal")
    OP_68(1000000, 1350, 0, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(11000, 0)
    OP_0D()
    Return()

    # Function_34_29F5 end

    def Function_35_2A40(): pass

    label("Function_35_2A40")

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

    # Function_35_2A40 end

    def Function_36_2AB1(): pass

    label("Function_36_2AB1")

    Fade(250)
    Sound(812, 0, 100, 0)
    ClearChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2B15"),
        (1, "loc_2B1E"),
        (2, "loc_2B27"),
        (3, "loc_2B30"),
        (4, "loc_2B39"),
        (5, "loc_2B42"),
        (6, "loc_2B4B"),
        (7, "loc_2B54"),
        (8, "loc_2B5D"),
        (9, "loc_2B66"),
        (10, "loc_2B6F"),
        (SWITCH_DEFAULT, "loc_2B78"),
    )


    label("loc_2B15")

    SetChrChipByIndex(0x1B, 0x0)
    Jump("loc_2B78")

    label("loc_2B1E")

    SetChrChipByIndex(0x1B, 0x1)
    Jump("loc_2B78")

    label("loc_2B27")

    SetChrChipByIndex(0x1B, 0x2)
    Jump("loc_2B78")

    label("loc_2B30")

    SetChrChipByIndex(0x1B, 0x3)
    Jump("loc_2B78")

    label("loc_2B39")

    SetChrChipByIndex(0x1B, 0x4)
    Jump("loc_2B78")

    label("loc_2B42")

    SetChrChipByIndex(0x1B, 0x5)
    Jump("loc_2B78")

    label("loc_2B4B")

    SetChrChipByIndex(0x1B, 0x6)
    Jump("loc_2B78")

    label("loc_2B54")

    SetChrChipByIndex(0x1B, 0x7)
    Jump("loc_2B78")

    label("loc_2B5D")

    SetChrChipByIndex(0x1B, 0x20)
    Jump("loc_2B78")

    label("loc_2B66")

    SetChrChipByIndex(0x1B, 0x21)
    Jump("loc_2B78")

    label("loc_2B6F")

    SetChrChipByIndex(0x1B, 0x23)
    Jump("loc_2B78")

    label("loc_2B78")

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

    # Function_36_2AB1 end

    def Function_37_2BF0(): pass

    label("Function_37_2BF0")

    OP_93(0xFE, 0xB4, 0x1F4)

    def lambda_2BFC():
        OP_96(0xFE, 0xF4240, 0x0, 0xFFFFF9C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2BFC)
    Sleep(500)

    def lambda_2C19():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2C19)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_37_2BF0 end

    def Function_38_2C2E(): pass

    label("Function_38_2C2E")

    OP_93(0xFE, 0xE1, 0x1F4)
    Sleep(600)
    OP_93(0xFE, 0xB4, 0x1F4)

    def lambda_2C44():
        OP_96(0xFE, 0xF4240, 0x0, 0xFFFFF9C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2C44)
    Sleep(500)

    def lambda_2C61():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2C61)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_38_2C2E end

    def Function_39_2C76(): pass

    label("Function_39_2C76")


    def lambda_2C7B():
        OP_93(0xFE, 0xB4, 0xC8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2C7B)
    OP_93(0x1B, 0xB4, 0x1F4)

    def lambda_2C8F():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_2C8F)
    Sleep(500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    WaitChrThread(0x1B, 1)
    EndChrThread(0x101, 0x2)
    Return()

    # Function_39_2C76 end

    def Function_40_2CB6(): pass

    label("Function_40_2CB6")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu00101.itp")
    Call(0, 29)
    SetChrSubChip(0x1B, 0x2)
    SetChrSubChip(0x101, 0x1)
    Call(0, 32)

    NpcTalk(
        0x1B,
        "Elie",
        (
            "#00105FThe gondola keeps going high and high...\x02\x03",
            "#00102F*giggle*, somehow now I'm tense.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7FF), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E08")

    ChrTalk(
        0x101,
        (
            "#00002F#6PYeah, it's my first time too on a ferris\x01",
            "wheel and my heart is pounding.\x02\x03",
            "#00005F...Wait, Elie, didn't\x01",
            "you come to the theme\x01",
            "park before?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2EAA")

    label("loc_2E08")


    ChrTalk(
        0x101,
        (
            "#00000F#6PYeah, it's not my first time too on a ferris\x01",
            "wheel, but my heart is pounding too.\x02\x03",
            "#00005F...Wait, Elie, didn't\x01",
            "you come to the theme\x01",
            "park before?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2EAA")

    SetChrSubChip(0x1B, 0x0)

    NpcTalk(
        0x1B,
        "Elie",
        (
            "#00104FYes, you're right, but...\x02\x03",
            "#00100FWhen I came before,\x01",
            "I toured the other\x01",
            "attractions.\x02\x03",
            "#00106FAs you can imagine, you can't\x01",
            "really tour them all in one day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#6PIndeed.\x02\x03",
            "#00009FHa ha, then\x01",
            "let's enjoy this.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Elie",
        (
            "#00102FYes, I wonder how the scenery\x01",
            "from the top looks like...\x02",
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
        "#00102FOh...look, Lloyd.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#6PWow...\x01",
            "What an amazing view.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3278")

    NpcTalk(
        0x1B,
        "Elie",
        (
            "#00109FYes, really. The lake is completely\x01",
            "dyed in the red of the sunset...\x02\x03",
            "#00104F*haah*...it makes you sigh unconsciously.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#6PYeah...\x01",
            "It seems we rode at a nice hour.\x02\x03",
            "#00009FI was right in saving\x01",
            "the last ticket for this.\x02",
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
            "*giggle*, Lloyd.\x01",
            "Thank you for inviting me.\x02\x03",
            "It's very unlikely that I will\x01",
            "forget this lovely scenery \x01",
            "any time soon.\x02",
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
        "#00000F#6PHa ha, you're welcome.\x02",
    )

    CloseMessageWindow()
    Jump("loc_332E")

    label("loc_3278")


    NpcTalk(
        0x1B,
        "Elie",
        (
            "#00102FYes, really.  \x01",
            "The sunlight reflecting on the lake,\x01",
            "glittering and sparkling...\x02\x03",
            "#00104F*haah*...it makes you sigh unconsciously.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#6PHa ha, that's true.\x02",
    )

    CloseMessageWindow()

    label("loc_332E")

    SetChrSubChip(0x1B, 0x0)
    Sleep(300)
    OP_63(0x1B, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    NpcTalk(
        0x1B,
        "Elie",
        "#00105F...Ah......\x02",
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
            "#00113FThe couple who boarded\x01",
            "the gondola after ours...\x02\x03",
            "They're, uhm, kis...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#6PEh...?\x02",
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
            "#00012F#6PH-Ha ha...uhm...\x01",
            "They were lovey dovey, eh?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x1B, 0x0)

    NpcTalk(
        0x1B,
        "Elie",
        (
            "#00109FA-Ahaha...right.\x01",
            "I had heard this attraction\x01",
            "is popular among couples...\x02\x03",
            "#00106F#1SM-Maybe they're seeing us too as\x01",
            "having that kind of relationships...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#6PHuh...?\x02",
    )

    CloseMessageWindow()
    OP_63(0x1B, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    NpcTalk(
        0x1B,
        "Elie",
        (
            "#00109FN-No, it's nothing.\x01",
            "Oh ho ho ho...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#6PA-Ahahaha...\x01",
            "(Somehow the mood became awkward.)\x02",
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
        "#00000F#6P...It seems we've almost arrived.\x05\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Elie",
        "#00100FYes, let's exit.\x05\x02",
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
            "#00100F#11P*giggle*, thank you Lloyd.\x01",
            "I had fun riding it with you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#6PYeah. I'm glad I invited you.\x02\x03",
            "Then, see you later.\x02",
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

    # Function_40_2CB6 end

    def Function_41_3748(): pass

    label("Function_41_3748")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu00201.itp")
    Call(0, 29)
    SetChrSubChip(0x1B, 0x2)
    SetChrSubChip(0x101, 0x1)
    Call(0, 32)

    NpcTalk(
        0x1B,
        "Tio",
        (
            "#00203F...Hmm.\x01",
            "What a situation.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x101,
        "#00005F#6PHuh, what?\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x1B, 0x0)

    NpcTalk(
        0x1B,
        "Tio",
        (
            "#00203FMy first trip to a theme park, alone\x01",
            "with Mr. Lloyd on the ferris wheel...\x02\x03",
            "#00200FI was thinking it is\x01",
            "a special situation.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7FF), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3930")

    ChrTalk(
        0x101,
        (
            "#00012F#6PHa ha, sorry. It's my first\x01",
            "time on a ferris wheel too,\x01",
            "so I'm a little nervous.\x02\x03",
            "#00006FNow that you mention it,\x01",
            "it might have been better to\x01",
            "bring a few more people along.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39AD")

    label("loc_3930")


    ChrTalk(
        0x101,
        (
            "#00003F#6PHmm, is that so?\x02\x03",
            "#00012FNow that you mention it,\x01",
            "it might have been better to\x01",
            "bring a few more people along.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_39AD")


    NpcTalk(
        0x1B,
        "Tio",
        "#00211FThat is not what I meant, but...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    NpcTalk(
        0x1B,
        "Tio",
        (
            "#00202F...Whatever. We don't get\x01",
            "chances like this often, so\x01",
            "let's talk about many things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#6PHa ha, yeah.\x02",
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
            "#00203F...In short, Michey's cuteness is\x01",
            "summarized in those eight points──\x01",
            "And that is not an exaggeration.\x02\x03",
            "#00201FI am sure that in this day and age it is\x01",
            "only a matter of time before people\x01",
            "begin to specialize in this as a career...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00012F#6PU-Uhm, Miss Tio? \x01",
            "We're almost at the top...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1B, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    NpcTalk(
        0x1B,
        "Tio",
        (
            "#00205F...Oh, I was too focused.\x02\x03",
            "#00204FWell then, I will give you\x01",
            "the rest of the lecture later...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#6P(When did this become a lecture...!?)\x02",
    )

    CloseMessageWindow()
    OP_63(0x1B, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3EEE")
    SetChrSubChip(0x1B, 0x2)

    NpcTalk(
        0x1B,
        "Tio",
        (
            "#00205F...How pretty...\x01",
            "That vast Elm Lake is\x01",
            "completely dyed red.\x02\x03",
            "#00204FI feel it has a different air than the scenery\x01",
            "that can be seen from the Waterfront Area.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)

    ChrTalk(
        0x101,
        (
            "#00000F#6PYeah...\x01",
            "It seems we rode at a nice hour.\x02\x03",
            "#00009FI was right in saving\x01",
            "the last ticket for this.\x02",
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
            "...Thank you for inviting me,\x01",
            "Mr. Lloyd.\x02\x03",
            "I think this scenery will become\x01",
            "a very nice memory.\x02",
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
        "#00000F#6PHa ha, you're welcome.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4095")

    label("loc_3EEE")

    SetChrSubChip(0x1B, 0x1)

    NpcTalk(
        0x1B,
        "Tio",
        (
            "#00205FMr. Lloyd, please look \x01",
            "towards the central square.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    ChrTalk(
        0x101,
        (
            "#00005F#6POh, you can see Michey's\x01",
            "face in the flower bed.\x02\x03",
            "#00009FHa ha. Seeing that makes\x01",
            "me feel like we really came\x01",
            "to the theme park.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Tio",
        (
            "#00202FUh uh, that is true.\x02\x03",
            "#00204FI want to plant a garden just\x01",
            "like that one on the Support\x01",
            "Section building's roof.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#6PG-Give me a break.\x01",
            "I don't think we're\x01",
            "that unique a post.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4095")

    SetChrSubChip(0x1B, 0x0)

    NpcTalk(
        0x1B,
        "Tio",
        (
            "#00203F...*ahem*, then while I am in the mood, \x01",
            "let's return to the second half of the\x01",
            "lecture, shall we?\x02\x03",
            "#00201FIt was said not too long ago that\x01",
            "Michey's cuteness is in his eyebrows,\x01",
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
            "#00006F#6P(Looks like I'll have to go along\x01",
            "with this until we get off...)\x02\x03",
            "#00012F(Well it seems fun, so why not.)\x02",
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
        "#00000F#6P...It seems we've almost arrived.\x05\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Tio",
        "#00200FRight, let's get off.\x02",
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
            "#00200FThank you very much, Mr. Lloyd.\x01",
            "Because of you, I had fun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#6PYeah. I'm glad I invited you.\x02\x03",
            "Then, see you later.\x02",
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

    # Function_41_3748 end

    def Function_42_434A(): pass

    label("Function_42_434A")

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
            "#00306F*haah*, I'd never thought I'd be stuck\x01",
            "to ride a ferris wheel with another dude.\x02\x03",
            "#00301FLloyd, seriously...you aren't\x01",
            "aimin' at me, right?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7FF), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4557")

    ChrTalk(
        0x101,
        (
            "#00006F#6PHey now...\x01",
            "I don't swing that way.\x02\x03",
            "#00000FIt's just that since you already\x01",
            "came to the theme park, Randy,\x01",
            "you should know many things.\x02\x03",
            "#00002FI thought you'd have 100% enjoyed the\x01",
            "scenery from the ferris wheel for the first time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4660")

    label("loc_4557")


    ChrTalk(
        0x101,
        (
            "#00006F#6PHey now...\x01",
            "I don't swing that way.\x02\x03",
            "#00000FIt's just that since you already\x01",
            "came to the theme park, Randy,\x01",
            "you should know many things.\x02\x03",
            "#00002FI thought you'd have made some kind\x01",
            "of new discovery by looking at the\x01",
            "scenery from the ferris wheel too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4660")


    NpcTalk(
        0x1B,
        "Randy",
        (
            "#00305FWhat, am I a guidebook substitute?\x01\x02\x03",
            "#00308FIn the end, you only want me\x01",
            "when it's convenient for you...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00011F#6PAaargh, don't\x01",
            "say all that in\x01",
            "a dubious way!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Randy",
        "#00309FGwah ha ha, it's a joke.\x02",
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
        "#00002F#6P...We're almost at the top.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x1B, 0x2)

    NpcTalk(
        0x1B,
        "Randy",
        (
            "#00304FYeah, almost there.\x02\x03",
            "#00300FIt's not like Orchis Tower,\x01",
            "but it's still pretty high...\x01",
            "The view from here is superb.\x02\x03",
            "Furthermore, with the outstanding mood\x01",
            "inside this airtight gondola, the capture\x01",
            "succes rate increases manyfolds.\x02\x03",
            "#00309FFor a man and a woman to advance to the\x01",
            "next step, this is truly the most ideal place.\x02",
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
            "#00006F#6PCapture success rate...?\x01",
            "...What're you talking about...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrSubChip(0x1B, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4C17")
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
            "Ha ha, just some instruction\x01",
            "in the ways of love.\x02\x03",
            "Anyway, even so...\x01",
            "You invited ME at an exquisite \x01",
            "time when the sun sets...\x02\x03",
            "Although it's a top notch time\x01",
            "for makin' a girl fall...\x02\x03",
            "What's wrong with you?\x02",
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
            "#00000F...Well, due to the course of events,\x01",
            "this time there're too many girls.\x02\x03",
            "I thought that having such a time talking\x01",
            "to you once in a while couldn't be bad.\x02\x03",
            "#00009FStill, being able to look at such a sunset...\x01",
            "I was right in saving the last ticket for this.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4DD2")

    label("loc_4C17")


    NpcTalk(
        0x1B,
        "Randy",
        (
            "#00309FHa ha, just some instruction\x01",
            "in the ways of love.\x02\x03",
            "#00303FAnyway, even so...\x01",
            "To invite someone like\x01",
            "me to the ferris wheel...\x02\x03",
            "#00301FAlthough it's the perfect place to make \x01",
            "a girl fall... What's wrong with you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#6PW-Who do you take me for?\x02\x03",
            "#00000F...Well, due to the course of events,\x01",
            "this time there're too many girls.\x02\x03",
            "#00004FI thought that having such a time talking\x01",
            "to you once in a while couldn't be bad.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4DD2")

    OP_63(0x1B, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    NpcTalk(
        0x1B,
        "Randy",
        (
            "#00306FJeez, that's why you're\x01",
            "a natural gigolo...\x02\x03",
            "#00300FWell, I'll at least accept the\x01",
            "thought with gratitude.\x02",
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
        "#00000F#6P...It seems we've almost arrived.\x05\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Randy",
        "#00300FYeah, let's exit.\x05\x02",
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
            "#00300FThanks for havin' invited me.\x01",
            "It wasn't bad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#6PYeah. I'm glad I invited you.\x02\x03",
            "Then, see you later.\x02",
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

    # Function_42_434A end

    def Function_43_4F91(): pass

    label("Function_43_4F91")

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
            "#00006F#6P...Uhmm, Noｱl.\x01",
            "Why have you been silent since before?\x02",
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
            "#10105FAh, no! It's...\x01",
            "It's the first time I've ridden\x01",
            "a ferris wheel with a man.\x02\x03",
            "#10100FI rode it before\x01",
            "with Fran...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7FF), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_51A5")

    ChrTalk(
        0x101,
        (
            "#00009F#6PA-Aah...I see.\x02\x03",
            "#00000FWell, it's the first time riding one for me too.\x01",
            "It would help me if you taught me many things.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5229")

    label("loc_51A5")


    ChrTalk(
        0x101,
        (
            "#00009F#6PA-Aah...I see.\x02\x03",
            "#00000FWell, it's not that I rode\x01",
            "it so many times...\x01",
            "It would help me if you taught me many things.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5229")


    NpcTalk(
        0x1B,
        "Noｱl",
        "#10102FY-Yes! Please leave it to me!\x02",
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
            "#10100FI-It's become pretty high, eh?\x02\x03",
            "#10104FUhhm, as expected, the\x01",
            "view from here is amazing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00009F#6PYeah, it's a nice view indeed.\x02",
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
            "#10106FUhhm...Mr. Lloyd, are\x01",
            "you really happy to have\x01",
            "invited someone like me?\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_55BC")
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
            "Well, the sunset\x01",
            "is so pretty...\x02\x03",
            "Maybe you should've been seeing\x01",
            "this with a more lovely girl like\x01",
            "Miss Elie or Miss Cecil...\x02",
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
            "#00003F#6PUhhm, I think you don't have to\x01",
            "downvalue yourself like that.\x02\x03",
            "#00000FYou see, I think you have\x01",
            "your cute sides too, Noｱl.\x02",
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
            "I was right in saving\x01",
            "the last ticket for this.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_56E9")

    label("loc_55BC")


    NpcTalk(
        0x1B,
        "Noｱl",
        (
            "#10108FI mean, it's a rare chance to be on a ferris wheel.\x02\x03",
            "Maybe you should've been seeing this with a\x01",
            "more lovely girl like Miss Elie or Miss Cecil...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#6PUhhm, I think you don't have to\x01",
            "downvalue yourself like that.\x02\x03",
            "#00000FYou see, I think you have\x01",
            "your cute sides too, Noｱl.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_56E9")

    OP_63(0x1B, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x1B)

    ChrTalk(
        0x101,
        (
            "#00005F#6PO-Oh?\x01",
            "Did I say something weird, somehow?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Noｱl",
        (
            "#10109FN-No...\x01",
            "Uhmm, thank you very much.\x02\x03",
            "#10106F(It's like those words had no special meaning...)\x02\x03",
            "#10101F(Mr. Lloyd, now I see that he's more\x01",
            "a dangerous person than I thought.)\x02",
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
            "#00006F#6P(U-Uhmm...\x01",
            "She fell silent again.\x01",
            "I guess I did say something weird...)\x02",
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
        "#00000F#6P...It seems we've almost arrived.\x05\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Noｱl",
        (
            "#10100FOh, yes.\x01",
            "Let's exit.\x05\x02",
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
            "#10100FThank you very much\x01",
            "for having invited me.\x01",
            "I had fun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#6PYeah. I'm glad I invited you.\x02\x03",
            "Then, see you later.\x02",
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

    # Function_43_4F91 end

    def Function_44_59B4(): pass

    label("Function_44_59B4")

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
            "#00000F#6PBy the way, Wazy, have you\x01",
            "ever ridden the ferris wheel?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x1B, 0x0)

    NpcTalk(
        0x1B,
        "Wazy",
        (
            "#10309FHu hu, actually, no.\x02\x03",
            "#10300FWhen I come with a club's client to Michelam,\x01",
            "we meet many times at quite places like a bar.\x01\x02\x03",
            "#10304FIn that sense, the theme park\x01",
            "itself is quite new to me.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7FF), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5C03")

    ChrTalk(
        0x101,
        (
            "#00000F#6PEeh...somehow it's unexpected.\x02\x03",
            "#00003FIt's the first time for me\x01",
            "riding the ferris wheel,\x01",
            "so I'm quite nervous.\x02\x03",
            "#00002FHa ha, thinking about it, that's strange\x01",
            "since it's not even a screaming attraction.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5CE6")

    label("loc_5C03")


    ChrTalk(
        0x101,
        (
            "#00000F#6PEeh...somehow it's unexpected.\x02\x03",
            "#00003FI rode the ferris wheel before too,\x01",
            "but I'm not used to it yet and I'm nervous.\x02\x03",
            "#00002FHa ha, thinking about it, that's strange\x01",
            "since it's not even a screaming attraction.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5CE6")


    NpcTalk(
        0x1B,
        "Wazy",
        (
            "#10300FWell, I think that the ferris wheel \x01",
            "is classified as a scary ride.\x02\x03",
            "#10304FThere's people not good just with high places...\x02\x03",
            "#10302FAnd in the remote chance that a junction\x01",
            "broke down making the gondola hang, it\x01",
            "would turn into a very horrible incident.\x02",
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
            "#10309FHu hu, what's wrong with some thrills?\x02\x03",
            "#10304FWell, let's enjoy the ferris wheel now.\x02",
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
        "#00000F#6PWe should be almost at the top...\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Wazy",
        (
            "#10304FWe really came high up and\x01",
            "the gondola's movements\x01",
            "are unexpectedly slow.\x02\x03",
            "Maybe it's in order to make\x01",
            "people enjoy the view longer...\x02\x03",
            "#10302FHu hu,  maybe we can think about it\x01",
            "as a suspension bridge effect.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x101,
        (
            "#00005F#6PYeah, the illusion of romantic feelings from\x01",
            "the heartbeat going faster due to terror...\x01",
            "Somehow I've heard about it.\x02\x03",
            "#00009FThey say many couples ride this...\x01",
            "Maybe it's unexpectedly successful.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrSubChip(0x1B, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_629C")
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
            "Hu hu, as for me, showing me\x01",
            "even such a pretty sunset\x01",
            "is successful.\x02\x03",
            "It wouldn't be strange at all\x01",
            "if love sprouted between us.\x02",
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
            "I though that I was right in\x01",
            "saving the last ticket to be\x01",
            "able to see such a sunset, but...\x02\x03",
            "#00003FNo, no, what you say won't happen.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6387")

    label("loc_629C")


    NpcTalk(
        0x1B,
        "Wazy",
        (
            "#10304FHu hu, this situation with us\x01",
            "alone in a locked space...\x02\x03",
            "#10309FIt wouldn't be strange at all\x01",
            "if love sprouted between us.\x02",
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
            "#00003FNo, no, that won't happen.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6387")


    NpcTalk(
        0x1B,
        "Wazy",
        (
            "#10304FHu hu, how cold.\x01",
            "My feelings are serious, you know?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00011F#6PJ-Just stop\x01",
            "doing that!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Wazy",
        (
            "#10309FHu hu, as I thought,\x01",
            "teasing you is worth it.\x02",
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
        "#00000F#6P...It seems we've almost arrived.\x05\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Wazy",
        "#10300FYeah, let's exit.\x05\x02",
    )

    CloseMessageWindow()
    Call(0, 36)
    Call(0, 28)
    Call(0, 24)
    Call(0, 35)

    NpcTalk(
        0x1B,
        "Wazy",
        "#10300FHu hu, it was pretty fun.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#6PYeah. I'm glad I invited you.\x02\x03",
            "Then, see you later.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Wazy",
        "#10300FYeah, see you later.\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x1B, 3, 0, 39)
    WaitChrThread(0x1B, 3)
    Return()

    # Function_44_59B4 end

    def Function_45_6560(): pass

    label("Function_45_6560")

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
        "#01105F#11PWow, it keeps going up and up!\x02",
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
            "#00012F#6PK-KeA, it's dangerous making it sway,\x01",
            "so stay sit inside the gondola, ok?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x1B, 0xE1, 0x1F4)

    NpcTalk(
        0x1B,
        "KeA",
        (
            "#01105F#11PAh, you're right too.\x02\x03",
            "#01109FEheheh, KeA got carried away.\x02",
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
            "#01109FI guess the scenery is\x01",
            "amazing at the top, huh?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7FF), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_682D")

    ChrTalk(
        0x101,
        (
            "#00004F#6PAh, it's my first time too\x01",
            "so I don't know yet, but...\x02\x03",
            "#00000FI'm sure we can look forward to it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_68AA")

    label("loc_682D")


    ChrTalk(
        0x101,
        (
            "#00004F#6PYeah, I rode in this before too\x01",
            "and the scenery was pretty nice.\x02\x03",
            "#00000FI'm sure you can look forward to it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_68AA")

    OP_63(0x1B, 0x12C, 1300, 0x36, 0x39, 0xFA, 0x0)
    Sleep(1000)

    NpcTalk(
        0x1B,
        "KeA",
        (
            "#01109F*thump thump*...\x01",
            "I can't really wait!\x02",
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
        "#00011F#6PI-I know, so calm down.\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6B9F")
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
            "Woooow, so high!!\x02\x03",
            "It's super pretty with\x01",
            "the totally red sky!!\x02",
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
            "#00004F#6PYeah...\x01",
            "It seems we rode at a nice hour.\x02\x03",
            "#00009FI was right in saving\x01",
            "the last ticket for this.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "KeA",
        (
            "#01102F#11PEh eh he, thanks for having invited me.\x02\x03",
            "#01110FAh, look, look Lloyd!\x01",
            "A fish leapt just now!!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6BFB")

    label("loc_6B9F")


    NpcTalk(
        0x1B,
        "KeA",
        (
            "#01110F#11PWoooow, so high!!\x02\x03",
            "#01109FAh, look, look Lloyd!\x01",
            "A fish leapt just now!!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6BFB")


    ChrTalk(
        0x101,
        (
            "#00002F#6POh, I wonder what fish is it?\x01",
            "I didn't really see it well, though...\x02",
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
            "#01100FSay, which one has the best view,\x01",
            "the scenery here or the one from\x01",
            "Orchis Tower...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F#6PHm? Let's see...\x01",
            "Definitely Orchis Tower,\x01",
            "if we speak of height, but...\x02\x03",
            "#00003FThe scenery is completely different\x01",
            "from this place, so I can't say without\x01",
            "reservation which is the better one.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "KeA",
        (
            "#01103F#11PMmmh, I see...\x02\x03",
            "#01109F...That's profound, Lloyd!\x02",
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
            "#00012F#6PYou're pretty excited, eh...?\x02\x03",
            "#00004F(...Well, what's important is that she's\x01",
            "cheered up. I guess I can relax for now.)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1B, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    NpcTalk(
        0x1B,
        "KeA",
        "#01110F#11PAh, a fish has leapt again!\x02",
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
            "#00000F#6PIt seems we have arrived.\x01",
            "KeA, let's exit.\x05\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "KeA",
        "#01100FYes, okay!\x05\x02",
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
            "#01109FEheheh, the view was nice,\x01",
            "I really enjoyed!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#6PYeah. I'm glad I invited you.\x02\x03",
            "Then, see you later.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "KeA",
        "#01100FYes! Later, Lloyd!\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x1B, 3, 0, 39)
    WaitChrThread(0x1B, 3)
    Return()

    # Function_45_6560 end

    def Function_46_703D(): pass

    label("Function_46_703D")

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
            "#06404FThis sensation of the ground\x01",
            "getting far and far away...\x02\x03",
            "#06409FWhen I ride the ferris wheel,\x01",
            "my heart always pounds.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7FF), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_71B1")

    ChrTalk(
        0x101,
        (
            "#00004F#6PYeah. For me it's the first time,\x01",
            "and I'm really nervous.\x02\x03",
            "#00000FIf I had to say, it seems\x01",
            "you're excited, Fran.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7232")

    label("loc_71B1")


    ChrTalk(
        0x101,
        (
            "#00004F#6PHa ha, I know what you mean.\x01",
            "It really makes you nervous.\x02\x03",
            "#00000FIf I had to say, it seems\x01",
            "you're excited, Fran.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7232")

    SetChrSubChip(0x1B, 0x0)

    NpcTalk(
        0x1B,
        "Fran",
        (
            "#06402FOh, you can tell?\x02\x03",
            "#06404FAfter all, riding in a ferris wheel\x01",
            "with a man is a rare experience.\x02\x03",
            "#06409FFurhermore, with Mr. Lloyd!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009F#6PHa ha, maybe I'm not fit\x01",
            "for that "furthermore"...\x02\x03",
            "#00000FThinking about it, it's quite a rare\x01",
            "opportunity for the two of us to be alone.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Fran",
        (
            "#06409FUh uh, then, since it's a rare chance,\x01",
            "let's talk about many things!\x02",
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
        "#06400FAh, please look, Mr. Lloyd!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#6PYeah, we're almost at the top.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_75FD")
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
            "*haaah*, how wonderful.\x02\x03",
            "With the fully red sunset\x01",
            "it's really romantic!\x02",
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
            "#00004F#6PYeah...\x01",
            "It seems we rode at a nice hour.\x02\x03",
            "#00009FI was right in saving\x01",
            "the last ticket for this.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Fran",
        (
            "#06402FUh uh, thank you for\x01",
            "having invited me!\x02\x03",
            "I had riden it with big sis before,\x01",
            "but the view is really amazing!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7672")

    label("loc_75FD")


    NpcTalk(
        0x1B,
        "Fran",
        (
            "#06402F*haaah*, how wonderful.\x02\x03",
            "#06409FI had riden it with big sis before,\x01",
            "but the view is really amazing!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7672")

    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x101,
        (
            "#00005F#6PBy the way Fran,\x01",
            "you've never gone\x01",
            "out with a man?\x02",
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
            "#06405FNo, I haven't...\x01",
            "Why do you ask?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#6PW-Well...\x01",
            "There's no particular meaning.\x02\x03",
            "#00000FI was thinking that you're\x01",
            "pretty popular, Fran.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Fran",
        (
            "#06402FAhaha, me? Not at all.\x02\x03",
            "#06404FAlso, there aren't quite\x01",
            "any men cooler and more\x01",
            "reliable than my big sis.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00012F#6PIs her your standard, Fran...?\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Fran",
        (
            "#06409FEheheh, but of course.\x02\x03",
            "Since I was a child, my favorite\x01",
            "has always been big sis!\x02\x03",
            "#06400FAh, but Mr. Lloyd could\x01",
            "barely get a passing mark.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009F#6PHa ha...well, thanks.\x01",
            "(They really are close sisters...)\x02",
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
            "#00000F#6PIt seems we have arrived.\x01",
            "Fran, let's exit.\x05\x02",
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
            "#06400FEheheh, the view was nice\x01",
            "and I had a lot of fun!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#6PYeah. I'm glad I invited you.\x02\x03",
            "Then, see you later.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Fran",
        "#06400FYes! Later, then.\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x1B, 3, 0, 39)
    WaitChrThread(0x1B, 3)
    Return()

    # Function_46_703D end

    def Function_47_7A6E(): pass

    label("Function_47_7A6E")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu05900.itp")
    Call(0, 29)
    Call(0, 32)

    NpcTalk(
        0x1B,
        "Cecil",
        (
            "#05900FEeh...so itis like this\x01",
            "inside the gondola.\x02\x03",
            "#05904FIt is just like a big cradle.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7FF), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7BB2")

    ChrTalk(
        0x101,
        (
            "#00004F#6PYeah, it's the first time for me too,\x01",
            "but it feels indeed like that.\x02\x03",
            "#00000FI think it can really shake,\x01",
            "so be careful, sister Cecil.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7C1E")

    label("loc_7BB2")


    ChrTalk(
        0x101,
        (
            "#00004F#6PYeah, it indeed feels like that.\x02\x03",
            "#00000FPlease be careful sister Cecil,\x01",
            "it can shake a lot.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7C1E")


    NpcTalk(
        0x1B,
        "Cecil",
        (
            "#05900FUh uh, thank you Lloyd.\x02\x03",
            "#05904FWe haven't been alone since when we went\x01",
            "together to see the Arc-en-ciel public \x01",
            "performance at the Anniversary Festival.\x02\x03",
            "#05909FLet's talk about many things\x01",
            "since it is a rare opportunity.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F#6PY-Yeah...you're right.\x02\x03",
            "#00003F(Now that I think about it,\x01",
            "I somehow got nervous...)\x02",
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
            "#05904FUh uh, even so, the theme\x01",
            "park is really a fun place.\x02\x03",
            "#05902FYou are received by the cute Michey,\x01",
            "there are a lot of funny attraction...\x01",
            "It is just like having strayed into a dreamworld.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002F#6PHa ha...for real.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00008F#6PDidn't you come with...\x01",
            "My brother, when he was alive?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Cecil",
        (
            "#05904FUh uh...sadly, no.\x01",
            "At that time, there wasn't such\x01",
            "a place in Crossbell yet.\x02\x03",
            "#05900FBut I went on many\x01",
            "dates with Guy that\x01",
            "were no less fun.\x02\x03",
            "#05909FWhen we went to eat,\x01",
            "he introduced me a lot\x01",
            "of recommended stands.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00012F#6PS-Stands at a date...\x02\x03",
            "#00006FThey were dates, my brother\x01",
            "could've at least looked for\x01",
            "fancy stores or something.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Cecil",
        (
            "#05905FOh, but they vere so good\x01",
            "and I really liked them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#6P(Uhhm...Sister Cecil and my big brother...\x01",
            "They really suited one another...)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1B, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x1B, 0x2)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_831C")

    NpcTalk(
        0x1B,
        "Cecil",
        (
            "#05905FOh...we are almost at the top.\x02\x03",
            "#05909FThe red sunset is very pretty...\x01",
            "It is a different scenery from the\x01",
            "one you can see from the hospital.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)

    ChrTalk(
        0x101,
        (
            "#00004F#6PYeah...\x01",
            "It seems we rode at a nice hour.\x02\x03",
            "#00009FI was right in saving\x01",
            "the last ticket for this.\x02",
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
            "Thank you for having invited me.\x02\x03",
            "This red sunset too has become \x01",
            "a very lovely memory.\x02",
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
    Jump("loc_841E")

    label("loc_831C")


    NpcTalk(
        0x1B,
        "Cecil",
        (
            "#05905FOh...we are almost at the top.\x02\x03",
            "#05909FThe lake is really pretty...\x01",
            "It is a different scenery from the\x01",
            "one you can see from the hospital.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)

    ChrTalk(
        0x101,
        "#00002F#6PYeah...it's true.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x1B, 0x0)

    NpcTalk(
        0x1B,
        "Cecil",
        (
            "#05902FUh uh, it has become\x01",
            "a very lovely memory.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_841E")

    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x101,
        "#00009F#6PHa ha, I'm glad too if you've enjoyed it.\x02",
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
            "#00000F#6PIt seems we have arrived.\x01",
            "Shall we exit, sister Cecil?\x05\x02",
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
            "#05900FUh uh, I had a lot of fun.\x01",
            "Thank you, Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#6PYeah, I too am glad to have invited you.\x02\x03",
            "Then, see you later.\x02",
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

    # Function_47_7A6E end

    def Function_48_85A3(): pass

    label("Function_48_85A3")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu01700.itp")
    Call(0, 29)
    SetChrSubChip(0x1B, 0x2)
    SetChrSubChip(0x101, 0x1)
    Call(0, 32)

    NpcTalk(
        0x1B,
        "Ilya",
        (
            "#01704FHm hm...\x01",
            "For someone like me it's a place\x01",
            "that lacks a little something, but...\x02\x03",
            "#01700FEven such a relaxing ride\x01",
            "is not bad once in a while.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7FF), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8773")

    ChrTalk(
        0x101,
        (
            "#00002F#6PHa ha, hearing you saying \x01",
            "this makes me at ease too.\x02\x03",
            "#00004FThey say that when you arrive at the top,\x01",
            "the scenery is quite nice...\x02\x03",
            "#00000FI think you'll be able to enjoy\x01",
            "it quite a lot too, Miss Ilya.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_884C")

    label("loc_8773")


    ChrTalk(
        0x101,
        (
            "#00002F#6PHa ha, hearing you saying\x01",
            "this makes me at ease too.\x02\x03",
            "#00004FMost of all, when you arrive at the top,\x01",
            "the scenery is quite nice...\x02\x03",
            "#00000FI think you'll be able to enjoy\x01",
            "it quite a lot too, Miss Ilya.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_884C")

    SetChrSubChip(0x1B, 0x0)

    NpcTalk(
        0x1B,
        "Ilya",
        (
            "#01709FIs the view that nice?\x01",
            "Uh uh, I guess I'll look forward to it.\x02\x03",
            "#01703FHmm, still, at such a speed it'll take\x01",
            "some time before reaching the top.\x02\x03",
            "#01702FUh uh, it's a rare chance so,\x01",
            "why don't we speak frankly?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#6PY-Yes, alright.\x01",
            "(I have a slightly bad presentiment...)\x02",
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
            "#01709FSo... Younger brother,\x01",
            "who're you aiming for in the end?\x02\x03",
            "#01705FCecil, as I thought?\x01",
            "Or one of your colleagues?\x01",
            "Could it be Rixia or me?\x02\x03",
            "#01704FAh, just so you know, Sully is still off limits, ok?\x01",
            "Until she grows up splendidly...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00006F#6PP-Please wait a moment!\x02\x03",
            "#00011FYou're asking me in rapid succession\x01",
            "who am I aiming to or not...\x01",
            "I mean, you're troubling me!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Ilya",
        (
            "#01706FEeh, what's wrong with that? Abandon yourself\x01",
            "to the course of events and tell me in secret.\x02\x03",
            "#01700FI'm Cecil's best friend so to you,\x01",
            "younger brother, I'm like another\x01",
            "big sister, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#6PT-That reasoning is weird...\x01",
            "And sister Cecil is not my real sister.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Ilya",
        (
            "#01709FHmph, you're no fun!\x01",
            "In this case, I'll make you spit\x01",
            "it out by tickling you, you know!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00011F#6P(T-This is bad, I have to\x01",
            "change the subject somehow...)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x101, 0x1)

    ChrTalk(
        0x101,
        (
            "#00005F#6PA-Aah, Miss Ilya!\x01",
            "In the meantime we have\x01",
            "almost reached the top.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1B, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x1B, 0x2)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8FC0")
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
            "Eeh...!\x01",
            "Indeed, it's quite a nice view.\x02\x03",
            "Also, thanks to the lake dyed in\x01",
            "vermillion due to the sunset, it\x01",
            "feels very... Nostalgic, I'd say...\x02",
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
            "#00004F#6PYes... \x01",
            "It seems we rode at a nice hour.\x02\x03",
            "#00009FI was right in saving\x01",
            "the last ticket for this.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Ilya",
        (
            "#01709FUh uh, frankly, it's more than what I imagined.\x01",
            "Thanks for having invited me.\x02\x03",
            "#01703FUhhm, I wonder if I could recreate\x01",
            "this image on the stage somehow...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_90D0")

    label("loc_8FC0")


    NpcTalk(
        0x1B,
        "Ilya",
        (
            "#01705FEeh...!\x01",
            "Indeed, it's quite a nice view.\x02\x03",
            "#01709FTo be able to see such nature\x01",
            "in Crossbell, a metropolis...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#6PHa ha...\x01",
            "Thinking aobut it, it's unexpected.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Ilya",
        (
            "#01703FUhhm, I wonder if I could recreate\x01",
            "this image on the stage somehow...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_90D0")

    OP_63(0x1B, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x1B)

    ChrTalk(
        0x101,
        (
            "#00006F#6P(*phew"...\x01",
            "Somehow I managed to relax the mood.)\x02\x03",
            "#00002F(Even so, she really thinks\x01",
            "about plays all the time.\x01",
            "I guess it's to be expected from Miss Ilya...)\x02",
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
            "#00000F#6PIt seems we have arrived.\x01",
            "Let's exit, Miss Ilya.\x05\x02",
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
            "#01700FUh uh, it was quite fun.\x01",
            "Thanks, younger brother.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#6PI too am glad to have invited you.\x02\x03",
            "Then, see you later.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Ilya",
        "#01700FYes, see you later.\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x1B, 3, 0, 39)
    WaitChrThread(0x1B, 3)
    Return()

    # Function_48_85A3 end

    def Function_49_92D1(): pass

    label("Function_49_92D1")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu01800.itp")
    Call(0, 29)
    SetChrSubChip(0x1B, 0x2)
    SetChrSubChip(0x101, 0x1)
    Call(0, 32)

    NpcTalk(
        0x1B,
        "Rixia",
        (
            "#01802F*haah*...\x01",
            "A "ferris wheel" is something nice.\x02\x03",
            "#01804FIt's quite and calm so\x01",
            "it's very relaxing.\x02\x03",
            "#01802FI think I somehow understand\x01",
            "why it's popular among\x01",
            "families and couples.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7FF), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9461")

    ChrTalk(
        0x101,
        (
            "#00004F#6PHa ha, for sure.\x02\x03",
            "#00000FAlso, according to what I've heard, the\x01",
            "scenery from the top is exceptional too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_94D7")

    label("loc_9461")


    ChrTalk(
        0x101,
        (
            "#00004F#6PHa ha, for sure.\x02\x03",
            "#00002FAlso, I rode it just before and the\x01",
            "scenery from the top was exceptional too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_94D7")

    SetChrSubChip(0x1B, 0x0)

    NpcTalk(
        0x1B,
        "Rixia",
        (
            "#01809FUh uh, I'll look forward to that.\x02\x03",
            "#01802FThen, why don't we talk about\x01",
            "many things until we reach the top?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x101,
        (
            "#00002F#6PYeah, it'll take some\x01",
            "time in a way, so\x01",
            "that could be nice.\x02",
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
        "#01804F...*dozing*...*dozing*...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#6P(Uhmm, somehow she looks to be sleeping.)\x02\x03",
            "#00006F(Training every day is probably tough,\x01",
            "and maybe she's also tired from the beach.)\x02\x03",
            "#00002F(It seems we'll soon reach the top...\x01",
            "Should I let her sleep like this...?)\x02",
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
        "#00005F#6POh, did you wake up?\x02",
    )

    CloseMessageWindow()
    OP_63(0x1B, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    NpcTalk(
        0x1B,
        "Rixia",
        (
            "#01805FI-I'm sorry!\x01",
            "I unconsciously dozed off...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009F#6PHa ha, no need to apologize.\x01",
            "More importantly...\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    Sleep(250)
    SetChrSubChip(0x1B, 0x2)
    Sleep(250)
    OP_63(0x1B, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_99AE")
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
            "Oh...we're already at the top.\x02\x03",
            "The sunset light dyes crimson\x01",
            "the water surface... It's a very\x01",
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
            "#00004F#6PYeah...\x01",
            "It seems we rode at a nice hour.\x02\x03",
            "#00009FI was right in saving\x01",
            "the last ticket for this.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Rixia",
        (
            "#01809FUh uh, thank you very much\x01",
            "for having invited me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9A58")

    label("loc_99AE")


    NpcTalk(
        0x1B,
        "Rixia",
        (
            "#01805FOh...we're already at the top.\x02\x03",
            "#01802FThe evirons surrounded with the vast lake...\x01",
            "It's a very pretty view.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002F#6PYeah...it's a nice scenery.\x02",
    )

    CloseMessageWindow()

    label("loc_9A58")

    OP_63(0x1B, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x1B)

    NpcTalk(
        0x1B,
        "Rixia",
        (
            "#01808F(...Still, to fall asleep when we're\x01",
            "alone in such a close space...)\x02\x03",
            "#01803F(No matter how much I felt at ease,\x01",
            "if the other party were "Yin"'s target...)\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x101,
        (
            "#00005F#6P...Uhhm, Rixia?\x02\x03",
            "#00002FIf you're still sleepy, you can\x01",
            "sleep without me minding...?\x02\x03",
            "When we arrive down, I'll wake you up.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x1B, 0x0)

    NpcTalk(
        0x1B,
        "Rixia",
        (
            "#01804F...No... I was only spacing out\x01",
            "since the view is really pretty.\x02\x03",
            "#01802FUh uh, please don't worry.\x02",
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
            "#00000F#6PIt seems we have arrived.\x01",
            "Rixia, should we exit?\x05\x02",
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
            "#01802FEhhm, it was very fun.\x01",
            "Thank you very much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#6PYeah. I'm glad I invited you.\x02\x03",
            "Then, see you later.\x02",
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

    # Function_49_92D1 end

    def Function_50_9D57(): pass

    label("Function_50_9D57")

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
            "#04211FW-Whoa, it's going up rapidly...\x02\x03",
            "#04206FH-Hey, is it going to be fine?\x01",
            "This box, it won't simply\x01",
            "fall with a tiny shock...?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x101,
        (
            "#00004F#6PHa ha, don't worry,\x01",
            "it won't fall.\x02\x03",
            "#00002FYou jump in high places\x01",
            "at Arc-en-ciel practice...\x01",
            "You shouldn't be that scared...\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x1B, 0x0)

    NpcTalk(
        0x1B,
        "Sully",
        (
            "#04206FI-I'm not scared, but...\x01",
            "The height is different, you know!?\x02\x03",
            "#04201FJeez...\x01",
            "If you consider this nothing\x01",
            "serious, I'm gonna punch you.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7FF), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A05F")

    ChrTalk(
        0x101,
        (
            "#00006F#6PI think that a girl shouldn't\x01",
            "say something like that, but...\x02\x03",
            "#00002FWell, I've heard that the view\x01",
            "from the top is quite amazing.\x02\x03",
            "I guess it's worth really\x01",
            "counterbalances the fear.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A134")

    label("loc_A05F")


    ChrTalk(
        0x101,
        (
            "#00006F#6PI think that a girl shouldn't\x01",
            "say something like that, but...\x02\x03",
            "#00002FWell, I've riden it before too and the\x01",
            "view from the top is quite amazing.\x02\x03",
            "I guess it's worth really\x01",
            "counterbalances the fear.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A134")

    OP_63(0x1B, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    NpcTalk(
        0x1B,
        "Sully",
        "#04206FL-Like I told you, I'm not afraid, jeez!\x02",
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
            "#00002F#6POh...\x01",
            "We're almost at the top.\x02",
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
            "#04211FW-Whoa...\x01",
            "R-Really, it's too high...!\x02\x03",
            "#04207FM-Make it go down! Make it go down now!!\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x101,
        (
            "#00012F#6PThere there, calm down.\x02\x03",
            "#00002FIf you only look down you'll get scared.\x01",
            "...Say, try looking over there.\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A57C")
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
            "I didn't figure it out on the water bus,\x01",
            "but this place is surrounded\x01",
            "by so much water, huh...?\x02\x03",
            "Also, the entire lake, dyed in red\x01",
            "by the sunset, is really pretty...\x02",
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
            "#00004F#6PYeah...\x01",
            "It seems we rode at a nice hour.\x02\x03",
            "#00009FI was right in saving\x01",
            "the last ticket for this.\x02",
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
            "#04203FH-Hmph...\x01",
            "I won't say thanks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#6PHa ha...how honest you're.\x02\x03",
            "#00000FHowever, hasn't your fear of\x01",
            "being in a high place blown away?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A661")

    label("loc_A57C")


    NpcTalk(
        0x1B,
        "Sully",
        (
            "#04205FAh...\x02\x03",
            "I didn't figure it out on the water\x01",
            "bus, but this place is surrounded\x01",
            "by so much water, huh...?\x02\x03",
            "#04202F...What a pretty view.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#6PHa ha...hasn't your fear of being\x01",
            "in a high place blown away?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A661")

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
            "#04211FW-Whoa! High, it's high!!\x02\x03",
            "#04206FJ-Jeez!!\x01",
            "Don't make me remember, man!\x02",
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
            "#00000F#6PIt seems we have arrived.\x01",
            "Sully, should we exit?\x05\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Sully",
        "#04200F...Y-Yes.\x05\x02",
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
            "#14012FW-Well...\x01",
            "It was moderately fun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#6PYeah. I'm glad I invited you.\x02\x03",
            "Then, see you later.\x02",
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

    # Function_50_9D57 end

    def Function_51_A835(): pass

    label("Function_51_A835")

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
        "#00005FThere...!\x02",
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
            "Eek! You found me again☆\x07\x00\x02",
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
            "Mishishi, you're really \x01",
            "good at this, mister☆\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "It's unheard of for me to be\x01",
            "found when I'm serious.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FI-I think that's\x01",
            "an exaggeration...\x02",
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

    def lambda_AA87():

        label("loc_AA87")

        TurnDirection(0xFE, 0x1A, 500)
        Yield()
        Jump("loc_AA87")

    QueueWorkItem2(0x101, 1, lambda_AA87)

    def lambda_AA99():

        label("loc_AA99")

        TurnDirection(0xFE, 0x1A, 500)
        Yield()
        Jump("loc_AA99")

    QueueWorkItem2(0xEF, 1, lambda_AA99)
    SetChrFlags(0x1A, 0x1000)
    OP_95(0x1A, 10920, 0, -15100, 5000, 0x0)
    OP_95(0x1A, 6460, 0, -18160, 5000, 0x0)

    def lambda_AAD8():
        OP_95(0xFE, 710, 0, -17500, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_AAD8)
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
            "#00012FHmm, I feel like she really\x01",
            "likes me or something...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 7)), scpexpr(EXPR_END)), "loc_AC03")

    ChrTalk(
        0x102,
        (
            "#00100F*giggle*, aren't you glad?\x02\x03",
            "Anyway, let's find her\x01",
            "next hiding place.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AFFA")

    label("loc_AC03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 0)), scpexpr(EXPR_END)), "loc_AC62")

    ChrTalk(
        0x103,
        (
            "#00200FPersonally, I am jealous.\x02\x03",
            "Anyway, let's find her\x01",
            "next hiding place.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AFFA")

    label("loc_AC62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 1)), scpexpr(EXPR_END)), "loc_ACDD")

    ChrTalk(
        0x104,
        (
            "#00300FHa ha, if peTiote saw that\x01",
            "she'd be jealous, huh?\x02\x03",
            "In any case, let's find her\x01",
            "next hidin' spot.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AFFA")

    label("loc_ACDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 2)), scpexpr(EXPR_END)), "loc_AD4A")

    ChrTalk(
        0x109,
        (
            "#10100FUh uh, and what's wrong with that?\x02\x03",
            "At any rate, let's find her\x01",
            "next hiding place.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AFFA")

    label("loc_AD4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 3)), scpexpr(EXPR_END)), "loc_ADB5")

    ChrTalk(
        0x105,
        (
            "#10300FHu hu, being popular is tough, eh?\x02\x03",
            "Anyway, shall we find her\x01",
            "next hiding place?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AFFA")

    label("loc_ADB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 4)), scpexpr(EXPR_END)), "loc_AE19")

    ChrTalk(
        0x153,
        (
            "#01100FEheheh, good for you, eh, Lloyd?\x02\x03",
            "Then, let's find her\x01",
            "next hiding place!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AFFA")

    label("loc_AE19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 5)), scpexpr(EXPR_END)), "loc_AE76")

    ChrTalk(
        0x156,
        (
            "#06400FUh uh, aren't you glad?\x02\x03",
            "Anyway, let's find her\x01",
            "next hiding place.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AFFA")

    label("loc_AE76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 6)), scpexpr(EXPR_END)), "loc_AEE9")

    ChrTalk(
        0x14C,
        (
            "#05900FUh uh, oh Lloyd,\x01",
            "you really are popular.\x02\x03",
            "In any case, let's find her\x01",
            "next hiding place.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AFFA")

    label("loc_AEE9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 7)), scpexpr(EXPR_END)), "loc_AF4A")

    ChrTalk(
        0x134,
        (
            "#01700FUh uh, ain't you glad?\x02\x03",
            "At any rate, let's find her\x01",
            "next hiding place.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AFFA")

    label("loc_AF4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 0)), scpexpr(EXPR_END)), "loc_AFA7")

    ChrTalk(
        0x135,
        (
            "#01802FUh uh, aren't you glad?\x02\x03",
            "Anyway, let's find her\x01",
            "next hiding place.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AFFA")

    label("loc_AFA7")


    ChrTalk(
        0x166,
        (
            "#14000FHmph, ain't that good.\x02\x03",
            "Anyway, let's find her\x01",
            "next hiding place, huh?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AFFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 7)), scpexpr(EXPR_END)), "loc_B028")

    ChrTalk(
        0x101,
        "#00000FYes, let's do that.\x02",
    )

    CloseMessageWindow()
    Jump("loc_B044")

    label("loc_B028")


    ChrTalk(
        0x101,
        "#00000FYeah, let's go.\x02",
    )

    CloseMessageWindow()

    label("loc_B044")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x1C9, 5)
    OP_65(0x0, 0x1)
    OP_29(0x7F, 0x1, 0xD)
    SetChrPos(0x0, -200, 10, -18640, 180)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_51_A835 end

    def Function_52_B074(): pass

    label("Function_52_B074")

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

    def lambda_B1B1():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B1B1)
    Sleep(50)

    def lambda_B1CE():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_B1CE)
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

    def lambda_B245():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B245)
    Sleep(50)

    def lambda_B255():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_B255)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05200FOh, Elie and Randy.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(6870, 3000)

    def lambda_B292():

        label("loc_B292")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_B292")

    QueueWorkItem2(0x102, 1, lambda_B292)

    def lambda_B2A4():

        label("loc_B2A4")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_B2A4")

    QueueWorkItem2(0x104, 1, lambda_B2A4)

    def lambda_B2B6():
        OP_95(0xFE, 860, 0, -18960, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B2B6)
    Sleep(50)

    def lambda_B2D3():
        OP_95(0xFE, -120, 50, -20150, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_B2D3)
    WaitChrThread(0x101, 1)

    def lambda_B2F1():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B2F1)
    WaitChrThread(0x103, 1)

    def lambda_B302():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_B302)
    OP_6F(0x10)
    Sleep(300)

    ChrTalk(
        0x104,
        "#00309FHeiya, thanks for your hard work.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F*giggle*, it seems you two\x01",
            "are doing your best too.\x02\x03",
            "How is it going?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05212FWell, it's quite tough...\x01",
            "Inside the costume is hot, you know.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05526FMr. Lloyd...\x01",
            "Going around is not a stroll.\x02\x03",
            "#05521FWhile behaving amiably,\x01",
            "you have to emanate a\x01",
            ""You found me! Lucky☆" feeling.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05206FR-Right...understood.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109FTio...\x01",
            "When it comes to Michey,\x01",
            "your vigor changes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00304FHa ha, Lloyd too loses his face.\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x1D, 0x80)
    SetChrPos(0x1D, 2880, 1730, -1360, 170)

    NpcTalk(
        0x1D,
        "Woman's Voice",
        "Ah, it's Michey!\x02",
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

    def lambda_B5A0():
        TurnDirection(0xFE, 0x1C, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B5A0)
    Sleep(50)

    def lambda_B5B0():
        OP_95(0xFE, -7940, 0, -14050, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_B5B0)
    Sleep(50)

    def lambda_B5CD():
        TurnDirection(0xFE, 0x1C, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B5CD)
    Sleep(50)

    def lambda_B5DD():
        TurnDirection(0xFE, 0x1C, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_B5DD)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    SetChrPos(0x1C, 2710, 800, -7600, 180)
    SetChrPos(0x1D, 1300, 1050, -7030, 180)
    OP_68(-1280, 3010, -20050, 3000)

    def lambda_B627():
        OP_95(0xFE, 1930, 0, -16000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_B627)
    Sleep(50)

    def lambda_B644():
        OP_95(0xFE, 830, 0, -15580, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_B644)
    OP_6F(0x1)
    WaitChrThread(0x1C, 1)
    OP_93(0x1C, 0xE1, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x1C,
        (
            "Ha ha, it's true.\x01",
            "We were lucky finding him after\x01",
            "coming back from the ferris wheel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "Aww, he's cute☆\x01",
            "Say, let's take a picture.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        "Yeah, you're right.\x02",
    )

    CloseMessageWindow()
    OP_95(0x1C, 2800, 0, -17840, 2000, 0x0)
    TurnDirection(0x1C, 0x102, 500)

    def lambda_B72D():
        TurnDirection(0xFE, 0x1C, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B72D)
    Sleep(50)

    def lambda_B73D():
        TurnDirection(0xFE, 0x1C, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_B73D)
    Sleep(300)

    ChrTalk(
        0x1C,
        (
            "Uhhm, excuse me.\x01",
            "Could you take us a\x01",
            "picture with this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FYes, all right.\x02",
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
            "#05203F(A p-picture...?\x01",
            "What should I do\x01",
            "on this occasion?)\x07\x00\x02",
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
            "Stand Near Him\x01",          # 0
            "Stand Near Her\x01",          # 1
            "Stand Between Them\x01",      # 2
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
        (0, "loc_B8E2"),
        (1, "loc_B9BA"),
        (2, "loc_BAA4"),
        (SWITCH_DEFAULT, "loc_BB67"),
    )


    label("loc_B8E2")

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
            "Ha ha ha, \x01",
            "it's ok, it's ok.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109FThen, I'm taking it.\x02\x03",
            "#00102FHere, cheese!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BB67")

    label("loc_B9BA")

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
            "Eek, yes!\x01",
            "Michey is all miiine♪\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "H-Ha ha ha...\x01",
            "(*sad*...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00111F(*gloomy*...)\x02\x03",
            "#00109F...E-Ehm.\x01",
            "Then, I'm taking it.\x02\x03",
            "#00102FHere, cheese!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BB67")

    label("loc_BAA4")

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
            "Uhuhu, today will be a \x01",
            "Michey's memorial day☆\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        "Thanks!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109FThen, I'm taking it.\x02\x03",
            "#00102FHere, cheese!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BB67")

    label("loc_BB67")

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

    def lambda_BBD3():
        OP_95(0xFE, 0, 440, -21620, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_BBD3)
    Sleep(50)

    def lambda_BBF0():
        OP_95(0xFE, -1000, 440, -20620, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_BBF0)
    WaitChrThread(0x1D, 1)

    def lambda_BC0E():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_BC0E)
    WaitChrThread(0x1C, 1)

    def lambda_BC1F():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_BC1F)
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    Sleep(500)

    ChrTalk(
        0x102,
        "#00100FHere, you're welcome.\x02",
    )

    CloseMessageWindow()
    OP_97(0x1C, 0xFFFFFC18, 0x0, 0x0, 0x7D0, 0x0)

    def lambda_BC75():
        OP_95(0xFE, -940, 2840, -31020, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_BC75)
    Sleep(50)

    def lambda_BC92():
        OP_95(0xFE, -940, 2840, -31020, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_BC92)
    Sleep(50)

    def lambda_BCAF():
        OP_95(0xFE, 0, 0, -18900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BCAF)

    def lambda_BCC9():
        OP_95(0xFE, -400, 0, -17600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_BCC9)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0xB4, 0x1F4)
    WaitChrThread(0x103, 1)
    TurnDirection(0x103, 0x101, 500)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x1D, 0x80)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BE8A")

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05204F*sigh*...\x01",
            "Was it all right?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Sound(2680, 255, 100, 0)

    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05524FPerfect, Mr. Lloyd.\x02\x03",
            "#05520FMichey is, so to speak,\x01",
            "the theme park's symbol...\x01",
            "He is like a walking attraction.\x02\x03",
            "#05524FI think it is more suitable\x01",
            "if in cases like that you stand\x01",
            "properly in between them.\x02\x03",
            "#05522FYou have become quite\x01",
            "accustomed to Michey too.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05209FHa ha, thank you.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x86, 0x1, 0x5)
    Jump("loc_C142")

    label("loc_BE8A")


    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05204F*sigh*...\x01",
            "Was it all righ──\x07\x00\x02",
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
            "#05526F...What a disappointment, Mr. Lloyd.\x02\x03",
            "#05531F...Why did you change\x01",
            "position on porpuse?\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05205FW-Well...\x01",
            "I didn't know if to get\x01",
            "between a couple or not...\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05526F*haah*...\x01",
            "Please think carefully.\x02\x03",
            "#05520FMichey is, so to speak,\x01",
            "the theme park's symbol...\x01",
            "He is like a walking attraction.\x02\x03",
            "#05531FI think it's more suitable\x01",
            "if in cases like that you stand\x01",
            "properly in between them.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05206FI-Is that so...?\x01",
            "(It was right doing\x01",
            "something unnecessary...)\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x86, 0x1, 0x6)

    label("loc_C142")


    ChrTalk(
        0x102,
        (
            "#00104F*giggle*, at this rate,\x01",
            "if you have Tio with\x01",
            "you, you'll do fine.\x02\x03",
            "#00100FGood luck you two.\x01",
            "We'll watch over you too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309FGwah ha ha, and have a\x01",
            "date at the same time!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x104, 1000)
    Sleep(300)

    ChrTalk(
        0x102,
        "#00103FThat's not it.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x102, 500)
    Sleep(300)

    ChrTalk(
        0x104,
        "#00306FArgh, an immediate reply...!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05200FHa ha...let's try to do\x01",
            "this as best as possible.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05520FThen, let's go to the next place.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 2)
    NewScene("t1300", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_52_B074 end

    def Function_53_C2EA(): pass

    label("Function_53_C2EA")

    OP_97(0x101, 0x0, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
    OP_97(0x101, 0x6A4, 0x0, 0x0, 0x7D0, 0x0)
    OP_97(0x101, 0x0, 0x0, 0x3E8, 0x7D0, 0x0)

    def lambda_C32B():
        OP_97(0xFE, 0xFFFFFC18, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_C32B)
    Sleep(50)

    def lambda_C348():
        OP_97(0xFE, 0xFFFFFE0C, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C348)
    WaitChrThread(0x1C, 1)

    def lambda_C366():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_C366)
    WaitChrThread(0x101, 1)

    def lambda_C377():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C377)
    Return()

    # Function_53_C2EA end

    def Function_54_C380(): pass

    label("Function_54_C380")

    OP_97(0x101, 0x0, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
    OP_97(0x101, 0xFFFFF95C, 0x0, 0x0, 0x7D0, 0x0)
    OP_97(0x101, 0x0, 0x0, 0x3E8, 0x7D0, 0x0)

    def lambda_C3C1():
        OP_97(0xFE, 0x3E8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_C3C1)
    Sleep(50)

    def lambda_C3DE():
        OP_97(0xFE, 0x1F4, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C3DE)
    WaitChrThread(0x1D, 1)

    def lambda_C3FC():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_C3FC)
    WaitChrThread(0x101, 1)

    def lambda_C40D():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C40D)
    Return()

    # Function_54_C380 end

    def Function_55_C416(): pass

    label("Function_55_C416")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a sketch map\x01",
            "of the theme park.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Return()

    # Function_55_C416 end

    def Function_56_C455(): pass

    label("Function_56_C455")

    EventBegin(0x1)
    TurnDirection(0x14, 0x0, 500)
    OP_4B(0x14, 0xFF)

    ChrTalk(
        0x14,
        (
            "Mister customers, if you\x01",
            "are boarding the ferris wheel,\x01",
            "please hand over your ticket here.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -330, 0, -15900, 350)
    OP_93(0x14, 0xA0, 0x0)
    OP_4C(0x14, 0xFF)
    EventEnd(0x4)
    Return()

    # Function_56_C455 end

    SaveToFile()

Try(main)
