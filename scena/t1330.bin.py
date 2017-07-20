from ScenarioHelper import *

def main():
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
        "Erie",                 # 1
        "Tio",                 # 2
        "Randy",               # 3
        "Noel",                 # 4
        "Waji",                   # 5
        "Keya",                 # 6
        "Franc",                 # 7
        "Cecil",                 # 8
        "Shuri",                 # 9
        "Marsun",               # 10
        "corona",                 # 11
        "Lima",                   # 12
        "MWL staff",         # 13
        "tourist",                 # 14
        "tourist",                 # 15
        "tourist",                 # 16
        "tourist",                 # 17
        "tourist",                 # 18
        "Misee",               # 19
        "dummy",                 # 20
        "Man",                     # 21
        "woman",                     # 22
        "Directions to Wonderland entrance square",# 23
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

    PlaceName(-0.38999998569488525, 0.0, -83.0999984741211, 0x0000, 0x0000, "Directions to Wonderland entrance square")

    ChipFrameInfo(1300, 0)                                       # 0

    ScpFunction((
        "Function_0_514",          # 00, 0
        "Function_1_5CC",          # 01, 1
        "Function_2_658",          # 02, 2
        "Function_3_6B3",          # 03, 3
        "Function_4_77D",          # 04, 4
        "Function_5_833",          # 05, 5
        "Function_6_A22",          # 06, 6
        "Function_7_AE0",          # 07, 7
        "Function_8_C10",          # 08, 8
        "Function_9_CDD",          # 09, 9
        "Function_10_E68",         # 0A, 10
        "Function_11_F22",         # 0B, 11
        "Function_12_FF8",         # 0C, 12
        "Function_13_109F",        # 0D, 13
        "Function_14_1157",        # 0E, 14
        "Function_15_1200",        # 0F, 15
        "Function_16_132F",        # 10, 16
        "Function_17_1387",        # 11, 17
        "Function_18_13DF",        # 12, 18
        "Function_19_149C",        # 13, 19
        "Function_20_153A",        # 14, 20
        "Function_21_1640",        # 15, 21
        "Function_22_1700",        # 16, 22
        "Function_23_17BE",        # 17, 23
        "Function_24_1881",        # 18, 24
        "Function_25_1A8A",        # 19, 25
        "Function_26_253D",        # 1A, 26
        "Function_27_257A",        # 1B, 27
        "Function_28_25B7",        # 1C, 28
        "Function_29_26C2",        # 1D, 29
        "Function_30_2724",        # 1E, 30
        "Function_31_2793",        # 1F, 31
        "Function_32_280A",        # 20, 32
        "Function_33_2875",        # 21, 33
        "Function_34_28E0",        # 22, 34
        "Function_35_292B",        # 23, 35
        "Function_36_299C",        # 24, 36
        "Function_37_2ADB",        # 25, 37
        "Function_38_2B19",        # 26, 38
        "Function_39_2B61",        # 27, 39
        "Function_40_2BA1",        # 28, 40
        "Function_41_35D7",        # 29, 41
        "Function_42_4147",        # 2A, 42
        "Function_43_4C9C",        # 2B, 43
        "Function_44_56AC",        # 2C, 44
        "Function_45_6153",        # 2D, 45
        "Function_46_6BEA",        # 2E, 46
        "Function_47_7665",        # 2F, 47
        "Function_48_80A3",        # 30, 48
        "Function_49_8CC3",        # 31, 49
        "Function_50_96C2",        # 32, 50
        "Function_51_A136",        # 33, 51
        "Function_52_A9B9",        # 34, 52
        "Function_53_BBA3",        # 35, 53
        "Function_54_BC39",        # 36, 54
        "Function_55_BCCF",        # 37, 55
        "Function_56_BD0D",        # 38, 56
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6CC")
    Jump("loc_779")

    label("loc_6CC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6E2")
    Jump("loc_779")

    label("loc_6E2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_752")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_705")
    Call(0, 21)
    Jump("loc_74D")

    label("loc_705")


    ChrTalk(
        0x8,
        (
            "#00102FHehe, I will buy you a drink\x01",
            "Please rest at ease.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_74D")

    Jump("loc_779")

    label("loc_752")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_768")
    Jump("loc_779")

    label("loc_768")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_779")

    label("loc_779")

    TalkEnd(0xFE)
    Return()

    # Function_3_6B3 end

    def Function_4_77D(): pass

    label("Function_4_77D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_796")
    Jump("loc_82F")

    label("loc_796")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7F2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7B9")
    Call(0, 22)
    Jump("loc_7ED")

    label("loc_7B9")


    ChrTalk(
        0x9,
        (
            "#00204FMr. Fran Franc …\x01",
            "You understand the story.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7ED")

    Jump("loc_82F")

    label("loc_7F2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_808")
    Jump("loc_82F")

    label("loc_808")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_81E")
    Jump("loc_82F")

    label("loc_81E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_82F")

    label("loc_82F")

    TalkEnd(0xFE)
    Return()

    # Function_4_77D end

    def Function_5_833(): pass

    label("Function_5_833")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_84C")
    Jump("loc_A1E")

    label("loc_84C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_862")
    Jump("loc_A1E")

    label("loc_862")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_878")
    Jump("loc_A1E")

    label("loc_878")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A0D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_97E")

    ChrTalk(
        0xA,
        (
            "#00300FA while ago, it came out from the Ferris wheel\x01",
            "A little favorite sister\x01",
            "I thought I was going to give up … …\x02\x03",
            "#00306FApparently\x01",
            "She seems to have come at a couple.\x02\x03",
            "#00302FWell, indeed within the theme park\x01",
            "I guess it was impossible for Nanpa - san.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_A08")

    label("loc_97E")


    ChrTalk(
        0xA,
        (
            "#00306FThink about it, you like a couple customers\x01",
            "There are many family guests.\x02\x03",
            "#00302FIndeed within the theme park\x01",
            "I guess it was impossible for Nanpa - san.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A08")

    Jump("loc_A1E")

    label("loc_A0D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A1E")

    label("loc_A1E")

    TalkEnd(0xFE)
    Return()

    # Function_5_833 end

    def Function_6_A22(): pass

    label("Function_6_A22")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A3B")
    Jump("loc_ADC")

    label("loc_A3B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A51")
    Jump("loc_ADC")

    label("loc_A51")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A67")
    Jump("loc_ADC")

    label("loc_A67")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A7D")
    Jump("loc_ADC")

    label("loc_A7D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ADC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AA0")
    Call(0, 23)
    Jump("loc_ADC")

    label("loc_AA0")


    ChrTalk(
        0xB,
        (
            "#10100FOh, Mr. Lloyd.\x01",
            "Did you decide what to ride at the end?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ADC")

    TalkEnd(0xFE)
    Return()

    # Function_6_A22 end

    def Function_7_AE0(): pass

    label("Function_7_AE0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BB9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B76")

    ChrTalk(
        0xC,
        (
            "#10304FIn this way human observation\x01",
            "It is not bad to do.\x02\x03",
            "#10302FHuh, it's unexpected somewhere\x01",
            "There were people in Miichi.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_BB4")

    label("loc_B76")


    ChrTalk(
        0xC,
        (
            "#10302FHuh, it's unexpected somewhere\x01",
            "There were people in Miichi.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BB4")

    Jump("loc_C0C")

    label("loc_BB9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BCF")
    Jump("loc_C0C")

    label("loc_BCF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BE5")
    Jump("loc_C0C")

    label("loc_BE5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BFB")
    Jump("loc_C0C")

    label("loc_BFB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C0C")

    label("loc_C0C")

    TalkEnd(0xFE)
    Return()

    # Function_7_AE0 end

    def Function_8_C10(): pass

    label("Function_8_C10")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C29")
    Jump("loc_CD9")

    label("loc_C29")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C3F")
    Jump("loc_CD9")

    label("loc_C3F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CB2")

    ChrTalk(
        0xD,
        (
            "#01102FAfter all,\x01",
            "The lake here is pretty.\x02\x03",
            "#01109FI feel that it is transparent to the bottom.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CD9")

    label("loc_CB2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CC8")
    Jump("loc_CD9")

    label("loc_CC8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CD9")

    label("loc_CD9")

    TalkEnd(0xFE)
    Return()

    # Function_8_C10 end

    def Function_9_CDD(): pass

    label("Function_9_CDD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CF6")
    Jump("loc_E64")

    label("loc_CF6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D71")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D19")
    Call(0, 22)
    Jump("loc_D6C")

    label("loc_D19")


    ChrTalk(
        0xE,
        (
            "#06409FAs Tio said,\x01",
            "Surely that sun's face\x01",
            "It's a secret of popularity ~!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D6C")

    Jump("loc_E64")

    label("loc_D71")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D87")
    Jump("loc_E64")

    label("loc_D87")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D9D")
    Jump("loc_E64")

    label("loc_D9D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E64")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DC0")
    Call(0, 23)
    Jump("loc_E64")

    label("loc_DC0")


    ChrTalk(
        0xE,
        (
            "#06402FIn this time zone,\x01",
            "The view from the Ferris wheel\x01",
            "It looks pretty good.\x02\x03",
            "#06409FIf it is not decided what to ride,\x01",
            "Lloyd's with someone\x01",
            "Why do not you ride?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E64")

    TalkEnd(0xFE)
    Return()

    # Function_9_CDD end

    def Function_10_E68(): pass

    label("Function_10_E68")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E81")
    Jump("loc_F1E")

    label("loc_E81")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E97")
    Jump("loc_F1E")

    label("loc_E97")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EF7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EBA")
    Call(0, 21)
    Jump("loc_EF2")

    label("loc_EBA")


    ChrTalk(
        0xF,
        (
            "#05909FHuhu, then\x01",
            "I wonder if I will give it up to your words.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EF2")

    Jump("loc_F1E")

    label("loc_EF7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F0D")
    Jump("loc_F1E")

    label("loc_F0D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F1E")

    label("loc_F1E")

    TalkEnd(0xFE)
    Return()

    # Function_10_E68 end

    def Function_11_F22(): pass

    label("Function_11_F22")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F3B")
    Jump("loc_FF4")

    label("loc_F3B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F51")
    Jump("loc_FF4")

    label("loc_F51")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F67")
    Jump("loc_FF4")

    label("loc_F67")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FE3")

    ChrTalk(
        0x10,
        (
            "#14006FHaha, I played quite well.\x01",
            "I feel tired somewhat.\x02\x03",
            "#14000FEven in the wind for a while\x01",
            "It seems to me like that.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FF4")

    label("loc_FE3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FF4")

    label("loc_FF4")

    TalkEnd(0xFE)
    Return()

    # Function_11_F22 end

    def Function_12_FF8(): pass

    label("Function_12_FF8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1011")
    Jump("loc_109B")

    label("loc_1011")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_105E")

    ChrTalk(
        0x11,
        (
            "Haha, Lima really\x01",
            "You seem to like the Ferris wheel.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_109B")

    label("loc_105E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1074")
    Jump("loc_109B")

    label("loc_1074")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_108A")
    Jump("loc_109B")

    label("loc_108A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_109B")

    label("loc_109B")

    TalkEnd(0xFE)
    Return()

    # Function_12_FF8 end

    def Function_13_109F(): pass

    label("Function_13_109F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10B8")
    Jump("loc_1153")

    label("loc_10B8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1116")

    ChrTalk(
        0x12,
        (
            "Oh no, if you remember … …\x01",
            "There are still more attractions\x01",
            "There are other things too?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1153")

    label("loc_1116")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_112C")
    Jump("loc_1153")

    label("loc_112C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1142")
    Jump("loc_1153")

    label("loc_1142")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1153")

    label("loc_1153")

    TalkEnd(0xFE)
    Return()

    # Function_13_109F end

    def Function_14_1157(): pass

    label("Function_14_1157")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1170")
    Jump("loc_11FC")

    label("loc_1170")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11BF")

    ChrTalk(
        0x13,
        (
            "Daddy, let's go one more time!\x01",
            "I also saw the Orkis Tower!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11FC")

    label("loc_11BF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11D5")
    Jump("loc_11FC")

    label("loc_11D5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11EB")
    Jump("loc_11FC")

    label("loc_11EB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11FC")

    label("loc_11FC")

    TalkEnd(0xFE)
    Return()

    # Function_14_1157 end

    def Function_15_1200(): pass

    label("Function_15_1200")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_132B")
    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "This attraction,\x01",
            "Ferris wheel \"Sunshine Mall\" is!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "From the gondola slowly going around,\x01",
            "Mishram best view\x01",
            "You can enjoy it slowly.\x02",
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
    TalkEnd(0xFE)
    Jump("loc_132E")

    label("loc_132B")

    Call(0, 25)

    label("loc_132E")

    Return()

    # Function_15_1200 end

    def Function_16_132F(): pass

    label("Function_16_132F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1383")

    ChrTalk(
        0x15,
        (
            "Let's ride a Ferris wheel!\x01",
            "It's so scary ~!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1383")

    label("loc_1383")

    TalkEnd(0xFE)
    Return()

    # Function_16_132F end

    def Function_17_1387(): pass

    label("Function_17_1387")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13DB")

    ChrTalk(
        0x16,
        (
            "Even I'm bad, I have a high place\x01",
            "I'm not good at it!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13DB")

    label("loc_13DB")

    TalkEnd(0xFE)
    Return()

    # Function_17_1387 end

    def Function_18_13DF(): pass

    label("Function_18_13DF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_143C")

    ChrTalk(
        0x17,
        (
            "Sea urchin\x01",
            "To the fluctuating gondola\x01",
            "I got totally drunk ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1498")

    label("loc_143C")


    ChrTalk(
        0x17,
        (
            "What?\x01",
            "After all it is\x01",
            "Will not it be different?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        "I'm sorry if I get drunk again … …\x02",
    )

    CloseMessageWindow()

    label("loc_1498")

    TalkEnd(0xFE)
    Return()

    # Function_18_13DF end

    def Function_19_149C(): pass

    label("Function_19_149C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14EE")

    ChrTalk(
        0x18,
        (
            "I already have a date\x01",
            "Firmly.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1536")

    label("loc_14EE")


    ChrTalk(
        0x18,
        (
            "It's okay it's okay!\x01",
            "When seeing the sunset from the summit,\x01",
            "Because I do not mind getting intoxicated!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1536")

    TalkEnd(0xFE)
    Return()

    # Function_19_149C end

    def Function_20_153A(): pass

    label("Function_20_153A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15BB")

    ChrTalk(
        0x19,
        (
            "One person riding a Ferris wheel\x01",
            "I need a lot of courage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "…… Even with a male friend\x01",
            "I was supposed to come with you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_163C")

    label("loc_15BB")


    ChrTalk(
        0x19,
        (
            "The view from the top was the best.\x01",
            "After all it was courageous\x01",
            "It was a correct answer on a ride.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "Well, to ride alone\x01",
            "I was sad lonely … but …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_163C")

    TalkEnd(0xFE)
    Return()

    # Function_20_153A end

    def Function_21_1640(): pass

    label("Function_21_1640")

    OP_4B(0x8, 0xFF)
    OP_4B(0xF, 0xFF)

    ChrTalk(
        0x8,
        (
            "#00100FWell then, me,\x01",
            "I'm buying something to drink.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#05905FOh, no.\x01",
            "Then I will buy it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#00102FHehe, Cecil\x01",
            "Please rest at ease.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    OP_4C(0x8, 0xFF)
    OP_4C(0xF, 0xFF)
    Return()

    # Function_21_1640 end

    def Function_22_1700(): pass

    label("Function_22_1700")

    OP_4B(0x9, 0xFF)
    OP_4B(0xE, 0xFF)

    ChrTalk(
        0x9,
        (
            "#00204FAgain, Ferris wheel\x01",
            "It seems to be very popular.\x02\x03",
            "#00200FThe face of the sun in the middle ……\x01",
            "It is exactly what it is\x01",
            "I wonder if it is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#06409FHaha, surely that's right ~!\x02",
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)
    OP_4C(0xE, 0xFF)
    SetScenarioFlags(0x0, 1)
    ClearChrFlags(0x9, 0x10)
    ClearChrFlags(0xE, 0x10)
    Return()

    # Function_22_1700 end

    def Function_23_17BE(): pass

    label("Function_23_17BE")

    OP_4B(0xB, 0xFF)
    OP_4B(0xE, 0xFF)

    ChrTalk(
        0xE,
        (
            "#06400FAccording to the guidebook,\x01",
            "In this time zone the view from the Ferris wheel\x01",
            "You know it's pretty good ~!\x02\x03",
            "#06409FOnee, let's ride with you later ~!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#10100FHuhu, I do not care.\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0xE, 0x10)
    SetScenarioFlags(0x0, 2)
    OP_4C(0xB, 0xFF)
    OP_4C(0xE, 0xFF)
    Return()

    # Function_23_17BE end

    def Function_24_1881(): pass

    label("Function_24_1881")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_18E6")
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

    label("loc_18E6")

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
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1944")
    ClearChrFlags(0xC, 0x80)
    SetChrChipByIndex(0xC, 0x12)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    Jump("loc_1A89")

    label("loc_1944")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_199D")
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
    Jump("loc_1A89")

    label("loc_199D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19CC")
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x10)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x10)
    Jump("loc_1A89")

    label("loc_19CC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A44")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x10, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1A24")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 1)), scpexpr(EXPR_END)), "loc_1A16")
    SetChrFlags(0xA, 0x80)
    Jump("loc_1A24")

    label("loc_1A16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 1)), scpexpr(EXPR_END)), "loc_1A24")
    SetChrFlags(0x10, 0x80)

    label("loc_1A24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1A3F")
    ClearChrFlags(0x1A, 0x80)

    label("loc_1A3F")

    Jump("loc_1A89")

    label("loc_1A44")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A89")
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x10)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 6760, 10, -15090, 115)
    SetChrFlags(0xE, 0x10)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x10)

    label("loc_1A89")

    Return()

    # Function_24_1881 end

    def Function_25_1A8A(): pass

    label("Function_25_1A8A")

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
            "This attraction,\x01",
            "Ferris wheel \"Sunshine Mall\" is!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "From the gondola slowly going around,\x01",
            "Mishram best view\x01",
            "You can enjoy it slowly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "If you do not mind,\x01",
            "How about with someone?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00004F#12P(… … Who should I invite?)\x02",
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
    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_1C9E")
    MenuCmd(3, 0, 0x0)

    label("loc_1C9E")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_1CB0")
    MenuCmd(3, 0, 0x1)

    label("loc_1CB0")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_1CC2")
    MenuCmd(3, 0, 0x2)

    label("loc_1CC2")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_1CD4")
    MenuCmd(3, 0, 0x3)

    label("loc_1CD4")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_1CE6")
    MenuCmd(3, 0, 0x4)

    label("loc_1CE6")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x20), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_1CF8")
    MenuCmd(3, 0, 0x5)

    label("loc_1CF8")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x40), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_1D0A")
    MenuCmd(3, 0, 0x6)

    label("loc_1D0A")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_1D1C")
    MenuCmd(3, 0, 0x7)

    label("loc_1D1C")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x100), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_1D2E")
    MenuCmd(3, 0, 0x8)

    label("loc_1D2E")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x200), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_1D40")
    MenuCmd(3, 0, 0x9)

    label("loc_1D40")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x400), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_1D52")
    MenuCmd(3, 0, 0xA)

    label("loc_1D52")

    MenuCmd(2, 0, -1, 55, 0)
    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_24DB")
    OP_D2(0x5, (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1DD8"),
        (1, "loc_1E19"),
        (2, "loc_1E5A"),
        (3, "loc_1E9D"),
        (4, "loc_1EDE"),
        (5, "loc_1F1D"),
        (6, "loc_1F5E"),
        (7, "loc_1F9F"),
        (8, "loc_1FE2"),
        (9, "loc_2027"),
        (10, "loc_206A"),
        (SWITCH_DEFAULT, "loc_20AB"),
    )


    label("loc_1DD8")

    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        "#00000F#12P(Okay … let's invite Ellie.\x02",
    )

    CloseMessageWindow()
    Jump("loc_20AB")

    label("loc_1E19")

    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        "#00000F#12P(Alright … let's invite Tio.\x02",
    )

    CloseMessageWindow()
    Jump("loc_20AB")

    label("loc_1E5A")

    OP_50(0x67, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        "#00000F#12P(Alright … let's invite Randy.\x02",
    )

    CloseMessageWindow()
    Jump("loc_20AB")

    label("loc_1E9D")

    OP_50(0x68, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        "#00000F#12P(Okay … let's invite Noel.\x02",
    )

    CloseMessageWindow()
    Jump("loc_20AB")

    label("loc_1EDE")

    OP_50(0x69, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        "#00000F#12P(Okay … let's invite Wazi.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_20AB")

    label("loc_1F1D")

    OP_50(0x64, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        "#00000F#12P(Alright … let's invite Ka'a.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_20AB")

    label("loc_1F5E")

    OP_50(0x6E, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        "#00000F#12P(Alright … let's invite the franc.\x02",
    )

    CloseMessageWindow()
    Jump("loc_20AB")

    label("loc_1F9F")

    OP_50(0x6D, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        "#00000F#12P(Alright … let's invite Cecil 's older sister.\x02",
    )

    CloseMessageWindow()
    Jump("loc_20AB")

    label("loc_1FE2")

    OP_50(0x6C, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        "#00000F#12P(Alright … let's invite Iria.\x02",
    )

    CloseMessageWindow()
    Jump("loc_20AB")

    label("loc_2027")

    OP_50(0x6A, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        "#00000F#12P(Alright … let's invite Leisha.\x02",
    )

    CloseMessageWindow()
    Jump("loc_20AB")

    label("loc_206A")

    OP_50(0x6F, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        "#00000F#12P(Alright … let's invite Sri.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_20AB")

    label("loc_20AB")

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
        (0, "loc_2128"),
        (1, "loc_2137"),
        (2, "loc_2146"),
        (3, "loc_2155"),
        (4, "loc_2164"),
        (5, "loc_216D"),
        (6, "loc_217C"),
        (7, "loc_218B"),
        (8, "loc_219A"),
        (9, "loc_21A9"),
        (10, "loc_21B8"),
        (SWITCH_DEFAULT, "loc_21C7"),
    )


    label("loc_2128")

    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    SetChrChipByIndex(0x1B, 0x0)
    Jump("loc_21C7")

    label("loc_2137")

    LoadChrToIndex("chr/ch00202.itc", 0x1F)
    SetChrChipByIndex(0x1B, 0x1)
    Jump("loc_21C7")

    label("loc_2146")

    LoadChrToIndex("chr/ch00302.itc", 0x1F)
    SetChrChipByIndex(0x1B, 0x2)
    Jump("loc_21C7")

    label("loc_2155")

    LoadChrToIndex("chr/ch02902.itc", 0x1F)
    SetChrChipByIndex(0x1B, 0x3)
    Jump("loc_21C7")

    label("loc_2164")

    SetChrChipByIndex(0x1B, 0x4)
    Jump("loc_21C7")

    label("loc_216D")

    LoadChrToIndex("chr/ch08202.itc", 0x1F)
    SetChrChipByIndex(0x1B, 0x5)
    Jump("loc_21C7")

    label("loc_217C")

    LoadChrToIndex("chr/ch08502.itc", 0x1F)
    SetChrChipByIndex(0x1B, 0x6)
    Jump("loc_21C7")

    label("loc_218B")

    LoadChrToIndex("chr/ch07502.itc", 0x1F)
    SetChrChipByIndex(0x1B, 0x7)
    Jump("loc_21C7")

    label("loc_219A")

    LoadChrToIndex("chr/ch05102.itc", 0x1F)
    SetChrChipByIndex(0x1B, 0x20)
    Jump("loc_21C7")

    label("loc_21A9")

    LoadChrToIndex("chr/ch05202.itc", 0x1F)
    SetChrChipByIndex(0x1B, 0x21)
    Jump("loc_21C7")

    label("loc_21B8")

    LoadChrToIndex("chr/ch10002.itc", 0x1F)
    SetChrChipByIndex(0x1B, 0x8)
    Jump("loc_21C7")

    label("loc_21C7")

    SetChrSubChip(0x1B, 0x0)
    SetChrPos(0x101, -950, 0, -16000, 0)
    SetChrPos(0x1B, -250, 0, -16700, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x14,
        "Then, we will keep your tickets.\x02",
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
        0x14,
        "We will inform you of 2 people!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrChipByIndex(0x101, 0x1E)
    Jc((scpexpr(EXPR_23, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_22CA")
    SetChrChipByIndex(0x1B, 0x12)
    Jump("loc_22CE")

    label("loc_22CA")

    SetChrChipByIndex(0x1B, 0x1F)

    label("loc_22CE")

    SetChrFlags(0x101, 0x4)
    SetChrPos(0x101, 999000, 200, 0, 90)
    SetChrPos(0x1B, 1001000, 200, 0, 270)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2341"),
        (1, "loc_2349"),
        (2, "loc_2351"),
        (3, "loc_2359"),
        (4, "loc_2361"),
        (5, "loc_2369"),
        (6, "loc_2371"),
        (7, "loc_2379"),
        (8, "loc_2381"),
        (9, "loc_2389"),
        (10, "loc_2391"),
        (SWITCH_DEFAULT, "loc_2399"),
    )


    label("loc_2341")

    Call(0, 40)
    Jump("loc_2399")

    label("loc_2349")

    Call(0, 41)
    Jump("loc_2399")

    label("loc_2351")

    Call(0, 42)
    Jump("loc_2399")

    label("loc_2359")

    Call(0, 43)
    Jump("loc_2399")

    label("loc_2361")

    Call(0, 44)
    Jump("loc_2399")

    label("loc_2369")

    Call(0, 45)
    Jump("loc_2399")

    label("loc_2371")

    Call(0, 46)
    Jump("loc_2399")

    label("loc_2379")

    Call(0, 47)
    Jump("loc_2399")

    label("loc_2381")

    Call(0, 48)
    Jump("loc_2399")

    label("loc_2389")

    Call(0, 49)
    Jump("loc_2399")

    label("loc_2391")

    Call(0, 50)
    Jump("loc_2399")

    label("loc_2399")

    SetChrFlags(0x1B, 0x80)
    OP_49()
    OP_D7(0x1E)
    Jc((scpexpr(EXPR_23, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_23B1")
    OP_D7(0x1F)

    label("loc_23B1")

    OP_D7(0x20)
    OP_D7(0x21)
    OP_D7(0x22)
    OP_D7(0x23)
    Switch(
        (scpexpr(EXPR_23, 0x5), scpexpr(EXPR_END)),
        (0, "loc_2404"),
        (1, "loc_2412"),
        (2, "loc_2420"),
        (3, "loc_242E"),
        (4, "loc_243C"),
        (5, "loc_244A"),
        (6, "loc_2458"),
        (7, "loc_2466"),
        (8, "loc_2474"),
        (9, "loc_2482"),
        (10, "loc_2490"),
        (SWITCH_DEFAULT, "loc_249E"),
    )


    label("loc_2404")

    OP_D2(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_249E")

    label("loc_2412")

    OP_D2(0x3, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_249E")

    label("loc_2420")

    OP_D2(0x3, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_249E")

    label("loc_242E")

    OP_D2(0x3, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_249E")

    label("loc_243C")

    OP_D2(0x3, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_249E")

    label("loc_244A")

    OP_D2(0x3, (scpexpr(EXPR_PUSH_LONG, 0x20), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_249E")

    label("loc_2458")

    OP_D2(0x3, (scpexpr(EXPR_PUSH_LONG, 0x40), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_249E")

    label("loc_2466")

    OP_D2(0x3, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_249E")

    label("loc_2474")

    OP_D2(0x3, (scpexpr(EXPR_PUSH_LONG, 0x100), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_249E")

    label("loc_2482")

    OP_D2(0x3, (scpexpr(EXPR_PUSH_LONG, 0x200), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_249E")

    label("loc_2490")

    OP_D2(0x3, (scpexpr(EXPR_PUSH_LONG, 0x400), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_249E")

    label("loc_249E")

    OP_D2(0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24D6")
    StopSound(821, 1000, 40)
    StopSound(126, 1000, 70)
    StopBGM(0xFA0)
    WaitBGM()
    SetScenarioFlags(0x22, 1)
    NewScene("t1300", 0, 0, 0)
    IdleLoop()

    label("loc_24D6")

    Jump("loc_2522")

    label("loc_24DB")


    ChrTalk(
        0x14,
        "Oh, will you stop it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        "I am waiting for another visit!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_2522")

    Call(0, 27)
    OP_4C(0x14, 0xFF)
    SetChrPos(0x0, 0, 0, -16500, 180)
    EventEnd(0x5)
    Return()

    # Function_25_1A8A end

    def Function_26_253D(): pass

    label("Function_26_253D")

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

    # Function_26_253D end

    def Function_27_257A(): pass

    label("Function_27_257A")

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

    # Function_27_257A end

    def Function_28_25B7(): pass

    label("Function_28_25B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2658")
    SetMapObjFrame(0xFF, "sky01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky_y", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky01_y", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky_in", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky01_in", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky_y_in", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky01_y_in", 0x1, 0x1)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xD5, 0x8F, 0x7B, 0x26, 0x1F4, 0x0)
    Jump("loc_26C1")

    label("loc_2658")

    SetMapObjFrame(0xFF, "sky01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky_y", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky01_y", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky_in", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky01_in", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky_y_in", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky01_y_in", 0x0, 0x1)

    label("loc_26C1")

    Return()

    # Function_28_25B7 end

    def Function_29_26C2(): pass

    label("Function_29_26C2")

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

    # Function_29_26C2 end

    def Function_30_2724(): pass

    label("Function_30_2724")

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

    # Function_30_2724 end

    def Function_31_2793(): pass

    label("Function_31_2793")

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

    # Function_31_2793 end

    def Function_32_280A(): pass

    label("Function_32_280A")

    Sound(148, 2, 80, 0)
    Fade(1000)
    SetMapObjFrame(0xFF, "Null_in", 0x2, "loop00")
    OP_68(1000000, 1350, 0, 0)
    Jc((scpexpr(EXPR_23, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2856")
    MoveCamera(30, 23, 0, 0)
    Jump("loc_2861")

    label("loc_2856")

    MoveCamera(45, 23, 0, 0)

    label("loc_2861")

    OP_6E(600, 0)
    SetCameraDistance(11000, 0)
    OP_0D()
    Return()

    # Function_32_280A end

    def Function_33_2875(): pass

    label("Function_33_2875")

    Sound(148, 2, 80, 0)
    Fade(1000)
    SetMapObjFrame(0xFF, "Null_in", 0x2, "loop01")
    OP_68(1000000, 1350, 0, 0)
    Jc((scpexpr(EXPR_23, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_28C1")
    MoveCamera(30, 23, 0, 0)
    Jump("loc_28CC")

    label("loc_28C1")

    MoveCamera(45, 23, 0, 0)

    label("loc_28CC")

    OP_6E(600, 0)
    SetCameraDistance(11000, 0)
    OP_0D()
    Return()

    # Function_33_2875 end

    def Function_34_28E0(): pass

    label("Function_34_28E0")

    Sound(148, 2, 80, 0)
    Fade(1000)
    SetMapObjFrame(0xFF, "Null_in", 0x2, "goal")
    OP_68(1000000, 1350, 0, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(11000, 0)
    OP_0D()
    Return()

    # Function_34_28E0 end

    def Function_35_292B(): pass

    label("Function_35_292B")

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

    # Function_35_292B end

    def Function_36_299C(): pass

    label("Function_36_299C")

    Fade(250)
    Sound(812, 0, 100, 0)
    ClearChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2A00"),
        (1, "loc_2A09"),
        (2, "loc_2A12"),
        (3, "loc_2A1B"),
        (4, "loc_2A24"),
        (5, "loc_2A2D"),
        (6, "loc_2A36"),
        (7, "loc_2A3F"),
        (8, "loc_2A48"),
        (9, "loc_2A51"),
        (10, "loc_2A5A"),
        (SWITCH_DEFAULT, "loc_2A63"),
    )


    label("loc_2A00")

    SetChrChipByIndex(0x1B, 0x0)
    Jump("loc_2A63")

    label("loc_2A09")

    SetChrChipByIndex(0x1B, 0x1)
    Jump("loc_2A63")

    label("loc_2A12")

    SetChrChipByIndex(0x1B, 0x2)
    Jump("loc_2A63")

    label("loc_2A1B")

    SetChrChipByIndex(0x1B, 0x3)
    Jump("loc_2A63")

    label("loc_2A24")

    SetChrChipByIndex(0x1B, 0x4)
    Jump("loc_2A63")

    label("loc_2A2D")

    SetChrChipByIndex(0x1B, 0x5)
    Jump("loc_2A63")

    label("loc_2A36")

    SetChrChipByIndex(0x1B, 0x6)
    Jump("loc_2A63")

    label("loc_2A3F")

    SetChrChipByIndex(0x1B, 0x7)
    Jump("loc_2A63")

    label("loc_2A48")

    SetChrChipByIndex(0x1B, 0x20)
    Jump("loc_2A63")

    label("loc_2A51")

    SetChrChipByIndex(0x1B, 0x21)
    Jump("loc_2A63")

    label("loc_2A5A")

    SetChrChipByIndex(0x1B, 0x23)
    Jump("loc_2A63")

    label("loc_2A63")

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

    # Function_36_299C end

    def Function_37_2ADB(): pass

    label("Function_37_2ADB")

    OP_93(0xFE, 0xB4, 0x1F4)

    def lambda_2AE7():
        OP_96(0xFE, 0xF4240, 0x0, 0xFFFFF9C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2AE7)
    Sleep(500)

    def lambda_2B04():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2B04)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_37_2ADB end

    def Function_38_2B19(): pass

    label("Function_38_2B19")

    OP_93(0xFE, 0xE1, 0x1F4)
    Sleep(600)
    OP_93(0xFE, 0xB4, 0x1F4)

    def lambda_2B2F():
        OP_96(0xFE, 0xF4240, 0x0, 0xFFFFF9C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2B2F)
    Sleep(500)

    def lambda_2B4C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2B4C)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_38_2B19 end

    def Function_39_2B61(): pass

    label("Function_39_2B61")


    def lambda_2B66():
        OP_93(0xFE, 0xB4, 0xC8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2B66)
    OP_93(0x1B, 0xB4, 0x1F4)

    def lambda_2B7A():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_2B7A)
    Sleep(500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    WaitChrThread(0x1B, 1)
    EndChrThread(0x101, 0x2)
    Return()

    # Function_39_2B61 end

    def Function_40_2BA1(): pass

    label("Function_40_2BA1")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu00101.itp")
    Call(0, 29)
    SetChrSubChip(0x1B, 0x2)
    SetChrSubChip(0x101, 0x1)
    Call(0, 32)

    NpcTalk(
        0x1B,
        "Erie",
        (
            "#00105FGondola rises steadily and high … …\x02\x03",
            "#00102FHehuu, I got nervous somehow.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7FF), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2CEA")

    ChrTalk(
        0x101,
        (
            "#00002F#6POh, I am the first Ferris wheel\x01",
            "I was excited.\x02\x03",
            "#00005F…… Erie is before\x01",
            "Coming to a theme park\x01",
            "Was not there any?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D80")

    label("loc_2CEA")


    ChrTalk(
        0x101,
        (
            "#00000F#6POh, the Ferris wheel is not the first time\x01",
            "I was excited.\x02\x03",
            "#00005F…… Erie is before\x01",
            "Coming to a theme park\x01",
            "Was not there any?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D80")

    SetChrSubChip(0x1B, 0x0)

    NpcTalk(
        0x1B,
        "Erie",
        (
            "#00104FYeah, that's right ……\x02\x03",
            "#00100FWhen I came in front\x01",
            "Other attractions\x01",
            "It was going around.\x02\x03",
            "#00106FAfter all, in a day\x01",
            "I could not turn around very much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#6PIndeed, that's what it is.\x02\x03",
            "#00009FHaha, then\x01",
            "I'm looking forward to it.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Erie",
        (
            "#00102FYeah, the view on the top is\x01",
            "I wonder what kind of thing ……\x02",
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
        "Erie",
        "#00102FOh …… Look, Lloyd.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#6PAh……\x01",
            "It's a nice view.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3114")

    NpcTalk(
        0x1B,
        "Erie",
        (
            "#00109FYeah, really.\x01",
            "The lake is dyed red in sunset … …\x02\x03",
            "#00104FHaa … … I will unexpectedly sigh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#6PAh……\x01",
            "It seems that I could get on a good time.\x02\x03",
            "#00009FThe last ticket\x01",
            "It was the right answer.\x02",
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
    SetChrName("Erie")

    AnonymousTalk(
        0xFF,
        (
            "Hehe, Lloyd.\x01",
            "Thank you for inviting me.\x02\x03",
            "This nice sight is\x01",
            "I will not forget for a while.\x02",
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
        "#00000F#6PHaha, you are welcome.\x02",
    )

    CloseMessageWindow()
    Jump("loc_31B1")

    label("loc_3114")


    NpcTalk(
        0x1B,
        "Erie",
        (
            "#00102FYeah, really.\x01",
            "The sun's light is reflected on the lake,\x01",
            "Shining sparkling ……\x02\x03",
            "#00104FHaa … … I will unexpectedly sigh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#6PHey, really.\x02",
    )

    CloseMessageWindow()

    label("loc_31B1")

    SetChrSubChip(0x1B, 0x0)
    Sleep(300)
    OP_63(0x1B, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    NpcTalk(
        0x1B,
        "Erie",
        "#00105F……Ah…………\x02",
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
        "#00005F#6PEli, what 's wrong?\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Erie",
        (
            "#00112FNo, no, that …\x02\x03",
            "#00113FTo the succeeding gondola\x01",
            "A couple is on board ……\x02\x03",
            "They, that kiss, kiss … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#6PHuh……?\x02",
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
            "#00012F#6PHahaha … that.\x01",
            "It was Atsuatsu.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x1B, 0x0)

    NpcTalk(
        0x1B,
        "Erie",
        (
            "#00109FOh, haha … well.\x01",
            "It's also popular with couples\x01",
            "I was listening … ….\x02\x03",
            "#00106F#1SEven we\x01",
            "It seems like that kind of relationship ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#6Peh……?\x02",
    )

    CloseMessageWindow()
    OP_63(0x1B, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    NpcTalk(
        0x1B,
        "Erie",
        (
            "#00109FNo, nothing.\x01",
            "Hahahahoh ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#6POh, hahaha ……\x01",
            "I feel somewhat awkward.\x02",
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
        "#00000F#6P… … It looks like arriving soon.\x05\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Erie",
        "#00100FLet 's suppose to get off.\x05\x02",
    )

    CloseMessageWindow()
    Call(0, 36)
    Call(0, 28)
    Call(0, 24)
    Call(0, 35)

    NpcTalk(
        0x1B,
        "Erie",
        (
            "#00100F#11PHehe, Thank you Lloyd.\x01",
            "It was fun riding together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#6POh, I'm glad you invited me too.\x02\x03",
            "Well then, see you later.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Erie",
        "#00100F#11PWell, see you.\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x1B, 3, 0, 39)
    WaitChrThread(0x1B, 3)
    Return()

    # Function_40_2BA1 end

    def Function_41_35D7(): pass

    label("Function_41_35D7")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu00201.itp")
    Call(0, 29)
    SetChrSubChip(0x1B, 0x2)
    SetChrSubChip(0x101, 0x1)
    Call(0, 32)

    NpcTalk(
        0x1B,
        "Tio",
        (
            "#00203F…… Hmm, this is\x01",
            "What kind of situation is it?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x101,
        "#00005F#6PHeck, what is it?\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x1B, 0x0)

    NpcTalk(
        0x1B,
        "Tio",
        (
            "#00203FThe first theme park,\x01",
            "Ferris wheel and Mr. Lloyd only two people ……\x02\x03",
            "#00200FConsidering, considerably\x01",
            "I thought it was a special situation.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7FF), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_37AC")

    ChrTalk(
        0x101,
        (
            "#00012F#6PHaha …… Sorry,\x01",
            "I am the first Ferris wheel\x01",
            "I am feeling somehow nervous.\x02\x03",
            "#00006FAs I was told,\x01",
            "Who would call some more people\x01",
            "It might have been fun.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3827")

    label("loc_37AC")


    ChrTalk(
        0x101,
        (
            "#00003F#6PWell, apparently so.\x02\x03",
            "#00012FWell, if you are told,\x01",
            "Who would call some more people\x01",
            "It might have been fun.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3827")


    NpcTalk(
        0x1B,
        "Tio",
        "#00211FI do not mean that … …\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    NpcTalk(
        0x1B,
        "Tio",
        (
            "#00202F… Well good.\x01",
            "I am impressed and various\x01",
            "Shall I talk about it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#6PHaha, that's right.\x02",
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
            "#00203F…… In other words, Mitsushi's loveliness is\x01",
            "That eight-character eyebrow is consolidated ─\x01",
            "It is no exaggeration to say so.\x02\x03",
            "#00201FIf that angle was missing even a little,\x01",
            "The current continent is also called the dark era Kaguya\x01",
            "When it was a turbulent era, experts ……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00012F#6POh, hey, Tio?\x01",
            "It is almost time for me ……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1B, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    NpcTalk(
        0x1B,
        "Tio",
        (
            "#00205F…… I just caught on.\x02\x03",
            "#00204FSo, the continuation of the lecture is\x01",
            "In the meantime ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#6P(When did you lecture …?!?)\x02",
    )

    CloseMessageWindow()
    OP_63(0x1B, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D2C")
    SetChrSubChip(0x1B, 0x2)

    NpcTalk(
        0x1B,
        "Tio",
        (
            "#00205F… … How beautiful …\x01",
            "That extensive Elm lake\x01",
            "It is dyed red.\x02\x03",
            "#00204FWhat is the scenery seen from the city's port area?\x01",
            "I feel a different feeling again.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)

    ChrTalk(
        0x101,
        (
            "#00000F#6PAh……\x01",
            "It seems that I could get on a good time.\x02\x03",
            "#00009FThe last ticket\x01",
            "It was the right answer.\x02",
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
            "…… Lloyd, please invite me\x01",
            "Thank you very much.\x02\x03",
            "This scene, very good\x01",
            "It is likely to be memories.\x02",
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
        "#00000F#6PHaha, you are welcome.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3EBA")

    label("loc_3D2C")

    SetChrSubChip(0x1B, 0x1)

    NpcTalk(
        0x1B,
        "Tio",
        (
            "#00205FMr. Lloyd, towards the central square\x01",
            "Please take a look.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    ChrTalk(
        0x101,
        (
            "#00005F#6POh … it was on the flower bed.\x01",
            "I can see the face of Misashi.\x02\x03",
            "#00009FHahaha, when you look at that\x01",
            "Really a theme park\x01",
            "I feel like I came.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Tio",
        (
            "#00202FHehe, it is.\x02\x03",
            "#00204FAlso on the roof of the support department\x01",
            "The same gardening as that\x01",
            "I would like to do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#6PWell, forgive me.\x01",
            "To a department that is too unique\x01",
            "It seems to be wrong.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3EBA")

    SetChrSubChip(0x1B, 0x0)

    NpcTalk(
        0x1B,
        "Tio",
        (
            "#00203F…… Kohon, where I felt\x01",
            "Let's move to the second half of the lecture.\x02\x03",
            "#00201FMitsushi's loveliness lies in the eyebrows,\x01",
            "Although I did a story earlier,\x01",
            "According to recent research …\x02",
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
            "#00006F#6P(Apparently until we got off\x01",
            "It looks like I will be dating … …)\x02\x03",
            "#00012F(Well, maybe because it looks like fun.\x02",
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
        "#00000F#6P… … It looks like arriving soon.\x05\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Tio",
        "#00200FWell, let's suppose it is getting down.\x05\x02",
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
            "#00200FThank you, Mr. Lloyd.\x01",
            "Thanks and I enjoyed it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#6POh, I'm glad you invited me too.\x02\x03",
            "Well then, see you later.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Tio",
        "#00200FWell, see you.\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x1B, 3, 0, 39)
    WaitChrThread(0x1B, 3)
    Return()

    # Function_41_35D7 end

    def Function_42_4147(): pass

    label("Function_42_4147")

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
            "#00306FHa, it is not bad and it's two people\x01",
            "I guess it will become a fun riding a Ferris wheel.\x02\x03",
            "#00301FLloyd, you … … seriously with me\x01",
            "I guess it is not aiming?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7FF), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4318")

    ChrTalk(
        0x101,
        (
            "#00006F#6PYou know.\x01",
            "I do not have such a hobby.\x02\x03",
            "#00000FHowever, I have been to before.\x01",
            "If it is Randy, also in the theme park\x01",
            "Because it seems to be detailed in various ways.\x02\x03",
            "#00002FThe scenery from the Ferris wheel for the first time\x01",
            "I thought that it seemed to be 100 enjoyable.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43F7")

    label("loc_4318")


    ChrTalk(
        0x101,
        (
            "#00006F#6PYou know.\x01",
            "I do not have such a hobby.\x02\x03",
            "#00000FHowever, I have been to before.\x01",
            "If it is Randy, also in the theme park\x01",
            "Because it seems to be detailed in various ways.\x02\x03",
            "#00002FAlso in the landscape seen from the Ferris wheel,\x01",
            "Also something new discovered\x01",
            "I thought it was there.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_43F7")


    NpcTalk(
        0x1B,
        "Randy",
        (
            "#00305FWhat is it\x01",
            "Would you like a guide book?\x02\x03",
            "#00308FAfter all I, something to you\x01",
            "Is it a convenient man ……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00011F#6PDaichi, every one\x01",
            "A fancy way of saying\x01",
            "Do it!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Randy",
        "#00309FWell, it is a joke.\x02",
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
        "#00002F#6P… … It is nearly at the summit.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x1B, 0x2)

    NpcTalk(
        0x1B,
        "Randy",
        (
            "#00304FOh, it is about time.\x02\x03",
            "#00300FIt is not as good as the Orkis Tower\x01",
            "There is considerable altitude,\x01",
            "The view from here is a magnificent view.\x02\x03",
            "Besides, this sealed\x01",
            "The inside of the gondola has excellent mood,\x01",
            "The probability of success of a strategy also jumps double.\x02\x03",
            "#00309FFor men and women to proceed to the next step,\x01",
            "It is exactly the right place.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00006F#6P…… What are you talking about?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrSubChip(0x1B, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4936")
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
            "Hahaha\x01",
            "It's a love affair.\x02\x03",
            "But even so ……\x01",
            "In this exquisite time of sunset\x01",
            "I'm inviting something.\x02\x03",
            "How to drop a girl\x01",
            "Even though it is the best timing,\x01",
            "What did you do with you too?\x02",
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
            "#00012F#6POh, do you think you are me?\x02\x03",
            "#00000F…… Well, this time the female team is on track\x01",
            "It's been quite a lot.\x02\x03",
            "Once in a while like Randy\x01",
            "Whether it is not bad to make a talking time.\x02\x03",
            "#00009FBut, I do not see such a sunset ……\x01",
            "I got the last ticket and was right.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4AD4")

    label("loc_4936")


    NpcTalk(
        0x1B,
        "Randy",
        (
            "#00309FHahaha\x01",
            "It's a love affair.\x02\x03",
            "#00303FBut even so ……\x01",
            "To the precious Ferris Wheel\x01",
            "I'm inviting something.\x02\x03",
            "#00301FEven though it's a great place to drop a girl,\x01",
            "What did you do with you too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#6POh, do you think you are me?\x02\x03",
            "#00000F…… Well, this time the female team is on track\x01",
            "It's been quite a lot.\x02\x03",
            "#00004FOnce in a while like Randy\x01",
            "Whether it is not bad to make a talking time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4AD4")

    OP_63(0x1B, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    NpcTalk(
        0x1B,
        "Randy",
        (
            "#00306FIt's like this\x01",
            "He is a natural gigolo … …\x02\x03",
            "#00300FWell, just feelings\x01",
            "Please accept it gently.\x02",
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
        "#00000F#6P… … It looks like arriving soon.\x05\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Randy",
        "#00300FOh, it will get off.\x05\x02",
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
            "#00300FThank you for inviting me.\x01",
            "I enjoyed it so much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#6POh, I'm glad you invited me too.\x02\x03",
            "Well then, see you later.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Randy",
        "#00300FOh, sure.\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x1B, 3, 0, 39)
    WaitChrThread(0x1B, 3)
    Return()

    # Function_42_4147 end

    def Function_43_4C9C(): pass

    label("Function_43_4C9C")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu10101.itp")
    Call(0, 29)
    SetChrSubChip(0x1B, 0x2)
    SetChrSubChip(0x101, 0x1)
    Call(0, 32)

    NpcTalk(
        0x1B,
        "Noel",
        "#10101F………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#6P………………………………\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Noel",
        "#10106F………………………………\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x101,
        (
            "#00006F#6P…, that, Noel.\x01",
            "Why are you silent from a while ago?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1B, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x1B, 0x0)

    NpcTalk(
        0x1B,
        "Noel",
        (
            "#10105FOh, no! That……\x01",
            "Watching a man and a Ferris wheel\x01",
            "Because it is my first time.\x02\x03",
            "#10100FWhen I got on the front,\x01",
            "It was with Fran.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7FF), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4ECA")

    ChrTalk(
        0x101,
        (
            "#00009F#6POh, ah … … that kind of thing.\x02\x03",
            "#00000FWell, it's my first time to ride.\x01",
            "I wonder if it will be helpful if you teach me various things.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4F4F")

    label("loc_4ECA")


    ChrTalk(
        0x101,
        (
            "#00009F#6POh, ah … … that kind of thing.\x02\x03",
            "#00000FWell, I'm still too much\x01",
            "I am not going to ride ……\x01",
            "I wonder if it will be helpful if you teach me various things.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F4F")


    NpcTalk(
        0x1B,
        "Noel",
        "#10102FWait! Let me take care of that!\x02",
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
        "Noel",
        (
            "#10100FIt has become quite high.\x02\x03",
            "#10104FWell, after all from here\x01",
            "The view is wonderful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00009F#6POh, it is certainly a nice sight.\x02",
    )

    CloseMessageWindow()
    OP_63(0x1B, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x1B)
    SetChrSubChip(0x1B, 0x0)

    NpcTalk(
        0x1B,
        "Noel",
        (
            "#10106FThat … … Lloyd,\x01",
            "I really do not know what to do\x01",
            "Was it good to invite?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x101,
        "#00005F#6PWell, why?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_52CE")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("Noel")

    AnonymousTalk(
        0xFF,
        (
            "That's it\x01",
            "The sunset is beautiful.\x02\x03",
            "Ely and Cecil,\x01",
            "A person with a more wonderful woman … …\x02",
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
            "#00003F#6PWell, I wanted myself so much\x01",
            "I do not have to lower it.\x02\x03",
            "#00000FHey, Noel\x01",
            "I think there is a cute place.\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    NpcTalk(
        0x1B,
        "Noel",
        "#10114F#4SOh.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009F#6PAnyway, this sunset ……\x01",
            "The last ticket\x01",
            "Was it the right answer?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_53C0")

    label("loc_52CE")


    NpcTalk(
        0x1B,
        "Noel",
        (
            "#10108FThat's the Ferris Wheel.\x02\x03",
            "Ely and Cecil,\x01",
            "A person with a more wonderful woman … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#6PWell, I wanted myself so much\x01",
            "I do not have to lower it.\x02\x03",
            "#00000FHey, Noel\x01",
            "I think there is a cute place.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_53C0")

    OP_63(0x1B, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x1B)

    ChrTalk(
        0x101,
        (
            "#00005F#6POh, that?\x01",
            "Something, did I say weird things?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Noel",
        (
            "#10109FNo……\x01",
            "Thank you very much.\x02\x03",
            "#10106F(I do not feel this as a special word …).\x02\x03",
            "#10101F(Lloyd's more than I thought\x01",
            "I feel like a dangerous person. )\x02",
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
            "#00006F#6P(Well, hmm … ….\x01",
            "I was silent again.\x01",
            "I guess they said weirdly strange things … …)\x02",
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
        "#00000F#6P… … It looks like arriving soon.\x05\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Noel",
        (
            "#10100FOh, yes.\x01",
            "Shall I get off?\x05\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 36)
    Call(0, 28)
    Call(0, 24)
    Call(0, 35)

    NpcTalk(
        0x1B,
        "Noel",
        (
            "#10100FPlease invite me\x01",
            "Thank you very much.\x01",
            "Thanks to you I enjoyed it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#6POh, I'm glad you invited me too.\x02\x03",
            "Well then, see you later.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Noel",
        "#10100FYes, also!\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x1B, 3, 0, 39)
    WaitChrThread(0x1B, 3)
    Return()

    # Function_43_4C9C end

    def Function_44_56AC(): pass

    label("Function_44_56AC")

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
            "#00000F#6P… … Wishes,\x01",
            "Have you ever taken a Ferris wheel?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x1B, 0x0)

    NpcTalk(
        0x1B,
        "Waji",
        (
            "#10309FHuh, in fact it is not true.\x02\x03",
            "#10300FWhen club guests and Michelin come,\x01",
            "In a quiet place like a bar\x01",
            "I often see you.\x02\x03",
            "#10304FIn that sense,\x01",
            "The theme park itself is fresh and fresh.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7FF), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_58BE")

    ChrTalk(
        0x101,
        (
            "#00000F#6POh … it is kind of unexpected.\x02\x03",
            "#00003FFor me,\x01",
            "Because I ride a Ferris wheel for the first time\x01",
            "I am pretty nervous.\x02\x03",
            "#00002FHahaha, if you think about it\x01",
            "It is a strange story though it is not a screaming system.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_596A")

    label("loc_58BE")


    ChrTalk(
        0x101,
        (
            "#00000F#6POh … it is kind of unexpected.\x02\x03",
            "#00003FI got on the Ferris wheel for the moment,\x01",
            "I am nervous because I have not gotten used to it yet.\x02\x03",
            "#00002FHahaha, if you think about it\x01",
            "It is a strange story though it is not a screaming system.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_596A")


    NpcTalk(
        0x1B,
        "Waji",
        (
            "#10300FNo, Ferris wheel is unexpected\x01",
            "I think it will be classified as a scary vehicle.\x02\x03",
            "#10304FSome people are not good at being high only … ….\x02\x03",
            "#10302FIn the unlikely event, I hang a gondola\x01",
            "If the connection part is broken\x01",
            "It will be a catastrophe.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00006F#6PSomething to be suddenly uneasy\x01",
            "Do not say … …\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Waji",
        (
            "#10309FWhoops, thrills can be born?\x02\x03",
            "#10304FWell, now let's enjoy the Ferris wheel.\x02",
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
        "#00000F#6PIt is about time to get to the top ……\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Waji",
        (
            "#10304FAlthough it became high indeed,\x01",
            "The movement itself of the gondola\x01",
            "It's surprisingly slow.\x02\x03",
            "Long enough to enjoy the scenery\x01",
            "I wonder if it is a wake-up … ….\x02\x03",
            "#10302FAlso consider the so-called suspension bridge effect\x01",
            "It may be that way.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x101,
        (
            "#00005F#6POh, beating to get faster with fear,\x01",
            "It's like illusion with love affection … …\x01",
            "I have heard somehow.\x02\x03",
            "#00009FIt's a story that there are many couples\x01",
            "It may be surprising to me.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrSubChip(0x1B, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5E90")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("Waji")

    AnonymousTalk(
        0xFF,
        (
            "Huh, for me\x01",
            "Until such a beautiful sunset\x01",
            "That's why I'm showing it.\x02\x03",
            "Even though my love has grown up\x01",
            "It's a strange situation.\x02",
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
            "#00012F#6PA, ear raise … …\x02\x03",
            "When such a sunset was seen,\x01",
            "Take the last ticket\x01",
            "I thought it was a correct answer … ….\x02\x03",
            "#00003FThere is no, it is not.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5F6C")

    label("loc_5E90")


    NpcTalk(
        0x1B,
        "Waji",
        (
            "#10304FHuh, this situation of two people alone in a closed room ……\x02\x03",
            "#10309FEven though my love has grown up\x01",
            "It's a strange situation.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00012F#6PA, ear raise … …\x02\x03",
            "#00003FThere is no, it is not.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5F6C")


    NpcTalk(
        0x1B,
        "Waji",
        (
            "#10304FHuh, I will not bend.\x01",
            "Are you serious about me?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00011F#6PSo that's why\x01",
            "Stop it!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Waji",
        (
            "#10309FHuh, after all you king\x01",
            "There are places to apply.\x02",
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
        "#00000F#6P… … It looks like arriving soon.\x05\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Waji",
        "#10300FOh, shall we?\x05\x02",
    )

    CloseMessageWindow()
    Call(0, 36)
    Call(0, 28)
    Call(0, 24)
    Call(0, 35)

    NpcTalk(
        0x1B,
        "Waji",
        "#10300FHugh, it was fun.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#6POh, I'm glad you invited me too.\x02\x03",
            "Well then, see you later.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Waji",
        "#10300FOh, later again.\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x1B, 3, 0, 39)
    WaitChrThread(0x1B, 3)
    Return()

    # Function_44_56AC end

    def Function_45_6153(): pass

    label("Function_45_6153")

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
        "Keya",
        "#01105F#11PWow, go up steadily!\x02",
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
            "#00012F#6PKi, Kia, because it's dangerous to shake\x01",
            "Like sitting in the gondola.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x1B, 0xE1, 0x1F4)

    NpcTalk(
        0x1B,
        "Keya",
        (
            "#01105F#11POh, that's right.\x02\x03",
            "#01109FWell, Ka'aa was crazy.\x02",
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
        "Keya",
        (
            "#01100FHey, Lloyd.\x02\x03",
            "#01109FAfter all the top\x01",
            "I wonder if the scenery is amazing?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7FF), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_641B")

    ChrTalk(
        0x101,
        (
            "#00004F#6POh, I am the first time.\x01",
            "I do not know yet ….\x02\x03",
            "#00000FI'm sure you can expect it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6481")

    label("loc_641B")


    ChrTalk(
        0x101,
        (
            "#00004F#6POh, I got on it earlier,\x01",
            "It was pretty nice scenery.\x02\x03",
            "#00000FI'm sure you can expect it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6481")

    OP_63(0x1B, 0x12C, 1300, 0x36, 0x39, 0xFA, 0x0)
    Sleep(1000)

    NpcTalk(
        0x1B,
        "Keya",
        (
            "#01109FIt's exciting!\x01",
            "I'm really looking forward to it!\x02",
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
        "#00011F#6PWell, because I understood, calm down.\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_677A")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("Keya")

    AnonymousTalk(
        0xFF,
        (
            "Oh my, it's high! It is!\x02\x03",
            "Besides, the sky is bright red\x01",
            "Sooooo Kire! It is!\x02",
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
            "#00004F#6PAh……\x01",
            "It seems that I could get on a good time.\x02\x03",
            "#00009FThe last ticket\x01",
            "It was the right answer.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Keya",
        (
            "#01102F#11PThank you for inviting me.\x02\x03",
            "#01110FOh, look at and see Lloyd!\x01",
            "Now the fish bounced! It is!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_67DE")

    label("loc_677A")


    NpcTalk(
        0x1B,
        "Keya",
        (
            "#01110F#11POh my, it's high! It is!\x02\x03",
            "#01109FOh, look at and see Lloyd!\x01",
            "Now the fish bounced! It is!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_67DE")


    ChrTalk(
        0x101,
        (
            "#00002F#6POh, what fish would that be?\x01",
            "Although it did not look good indeed ……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1B, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x1B)
    OP_93(0x1B, 0xE1, 0x1F4)

    NpcTalk(
        0x1B,
        "Keya",
        (
            "#01105F#11Pby the way……\x02\x03",
            "#01100FHey, the scenery here,\x01",
            "Scenery from Orchis Tower,\x01",
            "Which one do you prefer?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F#6PHmm? I see.\x01",
            "Speaking of height, definitely\x01",
            "It's an Orkis Tower ….\x02\x03",
            "#00003FBecause the scenery is completely different from here,\x01",
            "Which is better?\x01",
            "I wonder if I can say it.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Keya",
        (
            "#01103F#11PMuu, I see …\x02\x03",
            "#01109F… It's deep, Lloyd!\x02",
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
            "#00012F#6PThe equivalent tension is rising …\x02\x03",
            "#00004F(… well, how are you doing?\x01",
            "It is safe for the moment. )\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1B, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    NpcTalk(
        0x1B,
        "Keya",
        "#01110F#11POh, the fish jumped again!\x02",
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
            "#00000F#6PIt seems that it will arrive soon.\x01",
            "Ka'a, let's get off.\x05\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Keya",
        "#01100FYes, okay!\x05\x02",
    )

    CloseMessageWindow()
    Call(0, 36)
    Call(0, 28)
    Call(0, 24)
    Call(0, 35)

    NpcTalk(
        0x1B,
        "Keya",
        (
            "#01109FEh, I got a good view\x01",
            "It was a lot of fun!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#6POh, I'm glad you invited me too.\x02\x03",
            "Well then, see you later.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Keya",
        "#01100FYup! See you again, Lloyd!\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x1B, 3, 0, 39)
    WaitChrThread(0x1B, 3)
    Return()

    # Function_45_6153 end

    def Function_46_6BEA(): pass

    label("Function_46_6BEA")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu06400.itp")
    Call(0, 29)
    SetChrSubChip(0x1B, 0x2)
    SetChrSubChip(0x101, 0x1)
    Call(0, 32)
    OP_63(0x1B, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    NpcTalk(
        0x1B,
        "Franc",
        (
            "#06404FAs this ground gradually increases\x01",
            "Sensation to go away …\x02\x03",
            "#06409FTaking a Ferris wheel, every time\x01",
            "I'm throbbing, do not you think?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7FF), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6D57")

    ChrTalk(
        0x101,
        (
            "#00004F#6POh, I also get on for the first time\x01",
            "Do not get really nervous.\x02\x03",
            "#00000FWhich way is Fran\x01",
            "I feel excited.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6DD6")

    label("loc_6D57")


    ChrTalk(
        0x101,
        (
            "#00004F#6PHaha, I understand your feelings.\x01",
            "I'm really getting nervous.\x02\x03",
            "#00000FWhich way is Fran\x01",
            "I feel excited.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6DD6")

    SetChrSubChip(0x1B, 0x0)

    NpcTalk(
        0x1B,
        "Franc",
        (
            "#06402FOh, I understand ~?\x02\x03",
            "#06404FAnyway, I do not want to ride a Ferris wheel with a guy\x01",
            "It's rare experience.\x02\x03",
            "#06409FMoreover, the other party is Mr. Lloyd!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009F#6PHaha, \"What's more\"\x01",
            "Although the other party may not be served … …\x02\x03",
            "#00000FIf you think about it, you and two will also be with you\x01",
            "It's a pretty rare opportunity.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Franc",
        (
            "#06409FHuhu, that's all I need\x01",
            "Let's talk about various things ~!\x02",
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
        "Franc",
        "#06400FOh, please look at Mr. Lloyd!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#6POh, it is almost over there.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7199")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("Franc")

    AnonymousTalk(
        0xFF,
        (
            "Haa ~, I do not collect.\x02\x03",
            "With a bright red sunset,\x01",
            "It's so romantic!\x02",
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
            "#00004F#6PAh……\x01",
            "It seems that I could get on a good time.\x02\x03",
            "#00009FThe last ticket\x01",
            "It was the right answer.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Franc",
        (
            "#06402FHuhu, please invite me.\x01",
            "I'm really thankful to you!\x02\x03",
            "I also rode with my sister before,\x01",
            "After all it is a really nice view ~!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7213")

    label("loc_7199")


    NpcTalk(
        0x1B,
        "Franc",
        (
            "#06402FHaa ~, I do not collect.\x02\x03",
            "#06409FI also rode with my sister before,\x01",
            "After all it is a really nice view ~!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7213")

    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x101,
        (
            "#00005F#6PBy the way,\x01",
            "Until now I have been going out with a guy\x01",
            "Have not you done it?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1B, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x1B, 0x0)

    NpcTalk(
        0x1B,
        "Franc",
        (
            "#06405FWell, yes, but … …\x01",
            "why~?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#6PNo……\x01",
            "I do not have any special meaning.\x02\x03",
            "#00000FAfter all it was a frank,\x01",
            "I thought that it might be quite popular.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Franc",
        (
            "#06402FHaha, I am nothing at all ~ is it?\x02\x03",
            "#06404FPlus, older sister\x01",
            "I am cool and dependable\x01",
            "There are not many men.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00012F#6PIs the standard of frank there …?\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Franc",
        (
            "#06409FEh, of course.\x02\x03",
            "From my childhood, my number one\x01",
            "Always because you are older sister!\x02\x03",
            "#06400FOh, but if it was Mr. Lloyd\x01",
            "It may be a bit far from the point of being ~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009F#6PHahaha … That's right.\x01",
            "(Really sister's relationship is good … …)\x02",
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
            "#00000F#6PIt seems that it will arrive soon.\x01",
            "Franc, let's get off.\x05\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Franc",
        "#06400FYes, let's do so.\x05\x02",
    )

    CloseMessageWindow()
    Call(0, 36)
    Call(0, 28)
    Call(0, 24)
    Call(0, 35)

    NpcTalk(
        0x1B,
        "Franc",
        (
            "#06400FEh, I got a good view\x01",
            "It was a lot of fun ~!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#6POh, I'm glad you invited me too.\x02\x03",
            "Well then, see you later.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Franc",
        "#06400FYes! see you~.\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x1B, 3, 0, 39)
    WaitChrThread(0x1B, 3)
    Return()

    # Function_46_6BEA end

    def Function_47_7665(): pass

    label("Function_47_7665")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu05900.itp")
    Call(0, 29)
    Call(0, 32)

    NpcTalk(
        0x1B,
        "Cecil",
        (
            "#05900FOh … inside the gondola\x01",
            "It is becoming like this.\x02\x03",
            "#05904FIt sounds like a big cradle.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7FF), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7792")

    ChrTalk(
        0x101,
        (
            "#00004F#6POh, I also get on for the first time\x01",
            "Sure it is such a feeling.\x02\x03",
            "#00000FI think it is quite shaking,\x01",
            "Cecil elder sister, be careful.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_77F4")

    label("loc_7792")


    ChrTalk(
        0x101,
        (
            "#00004F#6POh, it certainly is such a feeling.\x02\x03",
            "#00000FBecause it shakes quite well,\x01",
            "Cecil elder sister, be careful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_77F4")


    NpcTalk(
        0x1B,
        "Cecil",
        (
            "#05900FHehe, Thank you Lloyd.\x02\x03",
            "#05904FLloyd and two of us are also\x01",
            "A memorial festival of Alcan Shell\x01",
            "Ever since I went to see it together.\x02\x03",
            "#05909FBecause it's painful,\x01",
            "Let's talk a lot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F#6POh, oh … That's right.\x02\x03",
            "#00003F(What do you think if you think so?\x01",
            "I was nervous … …)\x02",
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
            "#05904FHuhu, even so\x01",
            "Theme park is a really fun place.\x02\x03",
            "#05902FCute Michi welcomes me,\x01",
            "A lot of fun attractions ……\x01",
            "It seems as if he got lost in a dream world.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002F#6PHaha …. It certainly is.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00008F#6PIf my older brother was alive ……\x01",
            "Did you want to come with us?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Cecil",
        (
            "#05904FHehe … … just for a moment.\x01",
            "In those days, still in the crossbell\x01",
            "Because there was no such place.\x02\x03",
            "#05900FBut, with Mr. Guy\x01",
            "The date I went a few times also\x01",
            "It was so much fun to lose.\x02\x03",
            "#05909FWhen I went for a meal something,\x01",
            "I recommend a recommended stall\x01",
            "I got a lot of introductions.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00012F#6PDead, stalls on a date … ….\x02\x03",
            "#00006FBecause it is troublesome,\x01",
            "Big brother and stylish shop\x01",
            "You should have looked for it.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Cecil",
        (
            "#05905FOh, it is very tasty\x01",
            "I liked it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#6P(Well … … Cecil's older brother and older brother,\x01",
            "After all it was a perfect match … …)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1B, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x1B, 0x2)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7E56")

    NpcTalk(
        0x1B,
        "Cecil",
        (
            "#05905FAh … … It's almost time.\x02\x03",
            "#05909FThe red sunset is very beautiful ……\x01",
            "What is the scenery seen from the hospital\x01",
            "It looks different again.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)

    ChrTalk(
        0x101,
        (
            "#00004F#6PAh……\x01",
            "It seems that I could get on a good time.\x02\x03",
            "#00009FThe last ticket\x01",
            "It was the right answer.\x02",
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
            "Hehe, Thank you for inviting me.\x02\x03",
            "This sunset is also very nice\x01",
            "I became a memory.\x02",
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
    Jump("loc_7F2E")

    label("loc_7E56")


    NpcTalk(
        0x1B,
        "Cecil",
        (
            "#05905FAh … … It's almost time.\x02\x03",
            "#05909FThe lake is very beautiful ……\x01",
            "What is the scenery seen from the hospital\x01",
            "It looks different again.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)

    ChrTalk(
        0x101,
        "#00002F#6POh … it is true.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x1B, 0x0)

    NpcTalk(
        0x1B,
        "Cecil",
        (
            "#05902FHehe, very nice\x01",
            "I became a memory.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7F2E")

    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x101,
        "#00009F#6PHello, I'm happy that I am glad.\x02",
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
            "#00000F#6PIt seems that it will arrive soon.\x01",
            "Cecil elder sister, shall we get off?\x05\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Cecil",
        "#05900FYes, let's do.\x05\x02",
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
            "#05900FHehe, I had a lot of fun.\x01",
            "Thank you Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#6POh, I'm glad you invited me too.\x02\x03",
            "Well then, see you later.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Cecil",
        "#05900FWell, see you later.\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x1B, 3, 0, 39)
    WaitChrThread(0x1B, 3)
    Return()

    # Function_47_7665 end

    def Function_48_80A3(): pass

    label("Function_48_80A3")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu01700.itp")
    Call(0, 29)
    SetChrSubChip(0x1B, 0x2)
    SetChrSubChip(0x101, 0x1)
    Call(0, 32)

    NpcTalk(
        0x1B,
        "Ilia",
        (
            "#01704FHmmm …\x01",
            "For me it's just a bit\x01",
            "It's an unsatisfactory place ….\x02\x03",
            "#01700FSuch a relaxed ride also\x01",
            "Sometimes it's not bad.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7FF), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_824A")

    ChrTalk(
        0x101,
        (
            "#00002F#6PHaha, if you say so\x01",
            "Even I am comfortable.\x02\x03",
            "#00004FAnything, if you go to the top\x01",
            "It seems that the scenery is quite good … ….\x02\x03",
            "#00000FIria-san enough\x01",
            "I think you can have fun.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8307")

    label("loc_824A")


    ChrTalk(
        0x101,
        (
            "#00002F#6PHaha, if you say so\x01",
            "Even I am comfortable.\x02\x03",
            "#00004FHowever, if you go to the top\x01",
            "The scenery is quite good … ….\x02\x03",
            "#00000FIria-san enough\x01",
            "I think you can have fun.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8307")

    SetChrSubChip(0x1B, 0x0)

    NpcTalk(
        0x1B,
        "Ilia",
        (
            "#01709FYou have so much view?\x01",
            "I wonder if I will expect it.\x02\x03",
            "#01703FOh, but at this speed\x01",
            "It seems to take a little to the top.\x02\x03",
            "#01702FHuhu, that's the opportunity\x01",
            "Let's break your belly and talk about it, too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#6PWell, yeah, that's fine.\x01",
            "(I have a bad feeling a bit … …)\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 30)
    Call(0, 33)

    NpcTalk(
        0x1B,
        "Ilia",
        (
            "#01709FThat's why,\x01",
            "Who is my aim at the end after all?\x02\x03",
            "#01705FAfter all Cecil?\x01",
            "Or someone from my colleagues?\x01",
            "Did you mean me or Lisa?\x02\x03",
            "#01704FOh, but for the sake of say, Shuri is not good yet?\x01",
            "As a guardian, until it grows up … …\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00006F#6PWait a moment, please!\x02\x03",
            "#00011FWho is the aim and how,\x01",
            "Even if I have been questioned quickly ……\x01",
            "Because that is troubling!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Ilia",
        (
            "#01706FWell, that's not okay.\x01",
            "Leave it to the momentum and tell me Kossori.\x02\x03",
            "#01700FI am Cecil's close friend,\x01",
            "Another brother for you\x01",
            "Is not it like your older sister?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#6PWell, that's also strange … …\x01",
            "Cecil 's older sister is not even an older sister.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Ilia",
        (
            "#01709FEh, it's bad!\x01",
            "Even if I tickle it\x01",
            "I'll vomit! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00011F#6P(Well, bad,\x01",
            "I have to change the topic somehow ……)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x101, 0x1)

    ChrTalk(
        0x101,
        (
            "#00005F#6POh, ah!\x01",
            "While I am at it, soon\x01",
            "It seems to be at the top.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1B, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x1B, 0x2)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_89C7")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("Ilia")

    AnonymousTalk(
        0xFF,
        (
            "Well …!\x01",
            "Certainly the scenery is good.\x02\x03",
            "Besides, at sunset\x01",
            "Thanks to the lake being dyed red,\x01",
            "Is it so nostalgic ……\x02",
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
            "#00004F#6PYeah ….\x01",
            "I seem to have got on a good time.\x02\x03",
            "#00009FThe last ticket\x01",
            "Take this as a correct answer.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Ilia",
        (
            "#01709FHuh, to be honest with more than imagination.\x01",
            "Thank you for inviting me.\x02\x03",
            "#01703FWell, this image\x01",
            "I wonder if I can manage it on the stage ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8AC2")

    label("loc_89C7")


    NpcTalk(
        0x1B,
        "Ilia",
        (
            "#01705FWell …!\x01",
            "Certainly the scenery is good.\x02\x03",
            "#01709FIn the big city, Crossbell\x01",
            "I can see such nature ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#6Pmy mother……\x01",
            "It is surprising if you think about it.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Ilia",
        (
            "#01703FWell, this image\x01",
            "I wonder if I can manage it on the stage ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8AC2")

    OP_63(0x1B, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x1B)

    ChrTalk(
        0x101,
        (
            "#00006F#6P(Fuu … ….\x01",
            "Did you manage to distract yourself? )\x02\x03",
            "#00002F(Even so, at any time really\x01",
            "You are thinking about the stage.\x01",
            "As expected Iriria … …)\x02",
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
            "#00000F#6PIt seems that it will arrive soon.\x01",
            "Mr. Ilya, let's get off.\x05\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Ilia",
        "#01700FYes it is.\x05\x02",
    )

    CloseMessageWindow()
    Call(0, 36)
    Call(0, 28)
    Call(0, 24)
    Call(0, 35)

    NpcTalk(
        0x1B,
        "Ilia",
        (
            "#01700FHugh, it was fun.\x01",
            "Thank you, my younger brother.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#6PIt was nice to invite me.\x02\x03",
            "Well then, see you later.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Ilia",
        "#01700FWell, see you later.\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x1B, 3, 0, 39)
    WaitChrThread(0x1B, 3)
    Return()

    # Function_48_80A3 end

    def Function_49_8CC3(): pass

    label("Function_49_8CC3")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu01800.itp")
    Call(0, 29)
    SetChrSubChip(0x1B, 0x2)
    SetChrSubChip(0x101, 0x1)
    Call(0, 32)

    NpcTalk(
        0x1B,
        "Lisha",
        (
            "#01802FHa\x01",
            "Ferris wheel is a nice thing.\x02\x03",
            "#01804FIt is relaxing, quiet,\x01",
            "You say that it will be very calm.\x02\x03",
            "#01802FFor families and couples\x01",
            "To be popular,\x01",
            "I feel like understanding.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7FF), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8E37")

    ChrTalk(
        0x101,
        (
            "#00004F#6PHaha, for sure.\x02\x03",
            "#00000FAs I heard about it,\x01",
            "It seems that the scenery from the top is also exceptional.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8E99")

    label("loc_8E37")


    ChrTalk(
        0x101,
        (
            "#00004F#6PHaha, for sure.\x02\x03",
            "#00002FI also got on it a while ago,\x01",
            "The scenery from the top was also exceptional.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8E99")

    SetChrSubChip(0x1B, 0x0)

    NpcTalk(
        0x1B,
        "Lisha",
        (
            "#01809FHehe, it is pleasure.\x02\x03",
            "#01802FWell then, until you get to the top\x01",
            "Why do not you talk about various things?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x101,
        (
            "#00002F#6POh, as it is\x01",
            "It will take time\x01",
            "It might be nice.\x02",
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
        "Lisha",
        "#01804F…… Utsura …… Utsura ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#6P(Well, I do not feel sleepy.\x02\x03",
            "#00006F(It will be tough in practice everyday,\x01",
            "It may be fatigue on the beach. )\x02\x03",
            "#00002F(It seems to be on the summit soon,\x01",
            "I wonder if I let you sleep like this …? )\x02",
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
        "Lisha",
        "#01805FHa ha\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#6PUh, did you get up?\x02",
    )

    CloseMessageWindow()
    OP_63(0x1B, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    NpcTalk(
        0x1B,
        "Lisha",
        (
            "#01805FWell, sorry!\x01",
            "Just a moment … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009F#6PHaha, I do not apologize.\x01",
            "More than that …\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    Sleep(250)
    SetChrSubChip(0x1B, 0x2)
    Sleep(250)
    OP_63(0x1B, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_932E")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("Lisha")

    AnonymousTalk(
        0xFF,
        (
            "Ah … it is already over there.\x02\x03",
            "The sunset light dyed the surface of the water to vermilion … …\x01",
            "It is a very beautiful view.\x02",
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
            "#00004F#6PAh……\x01",
            "It seems that I could get on a good time.\x02\x03",
            "#00009FThe last ticket\x01",
            "It was the right answer.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Lisha",
        (
            "#01809FHuhu, invite me\x01",
            "Thank you very much.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_93C4")

    label("loc_932E")


    NpcTalk(
        0x1B,
        "Lisha",
        (
            "#01805FAh … it is already over there.\x02\x03",
            "#01802FSurrounded by a vast lake ……\x01",
            "It is a very beautiful view.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002F#6POh … it's a nice scenery.\x02",
    )

    CloseMessageWindow()

    label("loc_93C4")

    OP_63(0x1B, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x1B)

    NpcTalk(
        0x1B,
        "Lisha",
        (
            "#01808F(… but, at the time of only two people in such a closed room\x01",
            "I do not feel like sleeping … …)\x02\x03",
            "#01803F(Even though it was cheap,\x01",
            "If the other party is a target of \"silver\" … …)\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x101,
        (
            "#00005F#6PWell, Lisha?\x02\x03",
            "#00002FIf I am still sleepy,\x01",
            "You can sleep without worrying about it, right?\x02\x03",
            "I will wake you when I arrive below.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x1B, 0x0)

    NpcTalk(
        0x1B,
        "Lisha",
        (
            "#01804F……House……\x01",
            "I was shocked because it was so beautiful.\x02\x03",
            "#01802FHehe, do not mind.\x02",
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
            "#00000F#6PIt seems that it will arrive soon.\x01",
            "Lisha, let's get off.\x05\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Lisha",
        "#01802FYes.\x05\x02",
    )

    CloseMessageWindow()
    Call(0, 36)
    Call(0, 28)
    Call(0, 24)
    Call(0, 35)

    NpcTalk(
        0x1B,
        "Lisha",
        (
            "#01802FWell, it was a lot of fun.\x01",
            "Thank you very much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#6POh, I'm glad you invited me too.\x02\x03",
            "Well then, see you later.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Lisha",
        "#01802FYes, I will do it later.\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x1B, 3, 0, 39)
    WaitChrThread(0x1B, 3)
    Return()

    # Function_49_8CC3 end

    def Function_50_96C2(): pass

    label("Function_50_96C2")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu04201.itp")
    Call(0, 29)
    SetChrSubChip(0x1B, 0x2)
    SetChrSubChip(0x101, 0x1)
    Call(0, 32)
    OP_63(0x1B, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    NpcTalk(
        0x1B,
        "Shuri",
        (
            "#04211FWow, it's going up steadily … …\x02\x03",
            "#04206FHey, hey are you okay! Is it?\x01",
            "Such a box, with a little shock\x01",
            "Easy to fall … …\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x101,
        (
            "#00004F#6PDo not worry\x01",
            "You never fall.\x02\x03",
            "#00002FEven in the practice of alkane shell\x01",
            "You fly at high places,\x01",
            "Even such afraid things ……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x1B, 0x0)

    NpcTalk(
        0x1B,
        "Shuri",
        (
            "#04206FThis is not scary, but …\x01",
            "The height is incorrect! Is it?\x02\x03",
            "#04201FGeez……\x01",
            "If it does not matter much in this\x01",
            "I'm going to hit you.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7FF), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_99A5")

    ChrTalk(
        0x101,
        (
            "#00006F#6PGirls like that\x01",
            "I do not think he is saying that ….\x02\x03",
            "#00002FWell, as I heard it\x01",
            "The view from the top seems to be quite amazing.\x02\x03",
            "The value worth the fear is\x01",
            "Is not there enough?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9A59")

    label("loc_99A5")


    ChrTalk(
        0x101,
        (
            "#00006F#6PGirls like that\x01",
            "I do not think he is saying that ….\x02\x03",
            "#00002FWell, I got on it earlier\x01",
            "The view from the top is quite amazing.\x02\x03",
            "The value worth the fear is\x01",
            "Is not there enough?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9A59")

    OP_63(0x1B, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    NpcTalk(
        0x1B,
        "Shuri",
        "#04206FBut, so scared something of Nettsu!\x02",
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
            "#00002F#6POops ……\x01",
            "This area is it's near the top.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1B, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    NpcTalk(
        0x1B,
        "Shuri",
        (
            "#04211FAwaiting ……\x01",
            "And, after all, it is too expensive …!\x02\x03",
            "#04207FGet it down! Get it down now! It is!\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x101,
        (
            "#00012F#6PHow about you calm down.\x02\x03",
            "#00002FI am scared because I am watching the whole thing down.\x01",
            "Look, see the other side.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Shuri",
        "#04205FMum, beyond … …\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    OP_63(0x1B, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9E7A")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("Shuri")

    AnonymousTalk(
        0xFF,
        (
            "Ah……\x02\x03",
            "I did not know by the water bus,\x01",
            "Here in this lot of water\x01",
            "Is it surrounded …?\x02\x03",
            "Besides, the whole lake at sunset\x01",
            "It stains dark red and it is very beautiful …\x02",
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
            "#00004F#6PAh……\x01",
            "It seems that I could get on a good time.\x02\x03",
            "#00009FThe last ticket\x01",
            "It was the right answer.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1B, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    NpcTalk(
        0x1B,
        "Shuri",
        (
            "#04203FFun\x01",
            "I will not say a boyfriend.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#6PHaha … … It is not frank.\x02\x03",
            "#00000FBut, I'm afraid of being high\x01",
            "Was not he blown away?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9F4A")

    label("loc_9E7A")


    NpcTalk(
        0x1B,
        "Shuri",
        (
            "#04205FAh……\x02\x03",
            "I did not know by the water bus,\x01",
            "Here in this lot of water\x01",
            "Is it surrounded …?\x02\x03",
            "#04202F…… It's a beautiful view.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#6PHahaha … fear of being in a high place\x01",
            "Was not he blown away?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9F4A")

    OP_63(0x1B, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x1B)
    OP_63(0x1B, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    NpcTalk(
        0x1B,
        "Shuri",
        (
            "#04211FWow, that's it! High high! It is!\x02\x03",
            "#04206FWell, well! It is!\x01",
            "Do not remind me!\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x101,
        "#00006F#6PGo, sorry.\x02",
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
            "#00000F#6PIt seems that it will arrive soon.\x01",
            "Shuri, let's get off.\x05\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Shuri",
        "#04200F……No.\x05\x02",
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
        "Shuri",
        (
            "#14012FWell, well ….\x01",
            "It was fun so much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#6POh, I'm glad you invited me too.\x02\x03",
            "Well then, see you later.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Shuri",
        "#14000FHun, then.\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x1B, 3, 0, 39)
    WaitChrThread(0x1B, 3)
    Return()

    # Function_50_96C2 end

    def Function_51_A136(): pass

    label("Function_51_A136")

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
        "#00005FThere was …!\x02",
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
            "Kyat, I found it ☆\x07\x00\x02",
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
            "Misashi, an older brother\x01",
            "I'm really good at finding ☆\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "To find out serious me,\x01",
            "Because it is not a common thing.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FWell, that's a big deal.\x01",
            "I do not feel like it is ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "Anyway, if you find it two more times\x01",
            "The boyfriend won ~!\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "Misashi, do your best!\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A3BE():

        label("loc_A3BE")

        TurnDirection(0xFE, 0x1A, 500)
        Yield()
        Jump("loc_A3BE")

    QueueWorkItem2(0x101, 1, lambda_A3BE)

    def lambda_A3D0():

        label("loc_A3D0")

        TurnDirection(0xFE, 0x1A, 500)
        Yield()
        Jump("loc_A3D0")

    QueueWorkItem2(0xEF, 1, lambda_A3D0)
    SetChrFlags(0x1A, 0x1000)
    OP_95(0x1A, 10920, 0, -15100, 5000, 0x0)
    OP_95(0x1A, 6460, 0, -18160, 5000, 0x0)

    def lambda_A40F():
        OP_95(0xFE, 710, 0, -17500, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_A40F)
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
            "#00012FWell, sort of wonderful\x01",
            "I feel like I love you ….\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 7)), scpexpr(EXPR_END)), "loc_A537")

    ChrTalk(
        0x102,
        (
            "#00100FHehe, it was good.\x02\x03",
            "Anyway, next hiding place\x01",
            "Let's find it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A939")

    label("loc_A537")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 0)), scpexpr(EXPR_END)), "loc_A597")

    ChrTalk(
        0x103,
        (
            "#00200FPersonally I am jealous.\x02\x03",
            "Anyway, next hiding place\x01",
            "Let's find it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A939")

    label("loc_A597")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 1)), scpexpr(EXPR_END)), "loc_A60E")

    ChrTalk(
        0x104,
        (
            "#00300FHaha, if you saw Tio\x01",
            "It looks like envy.\x02\x03",
            "Anyway, next hiding place\x01",
            "When you look for it, it is.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A939")

    label("loc_A60E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 2)), scpexpr(EXPR_END)), "loc_A670")

    ChrTalk(
        0x109,
        (
            "#10100FHehe, is not it nice?\x02\x03",
            "Anyway, next hiding place\x01",
            "Let's find it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A939")

    label("loc_A670")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 3)), scpexpr(EXPR_END)), "loc_A6D4")

    ChrTalk(
        0x105,
        (
            "#10300FHuff, the man who is motto is painful.\x02\x03",
            "Anyway, next hiding place\x01",
            "Let's look for it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A939")

    label("loc_A6D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 4)), scpexpr(EXPR_END)), "loc_A734")

    ChrTalk(
        0x153,
        (
            "#01100FWell, that was good, is not it?\x02\x03",
            "Then, the next hiding place\x01",
            "Look for it!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A939")

    label("loc_A734")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 5)), scpexpr(EXPR_END)), "loc_A7A2")

    ChrTalk(
        0x156,
        (
            "#06400FHehe, was not it good?\x02\x03",
            "Anyway, next hiding place\x01",
            "Let's try to find it ~.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A939")

    label("loc_A7A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 6)), scpexpr(EXPR_END)), "loc_A815")

    ChrTalk(
        0x14C,
        (
            "#05900FHuhu, if Lloyd's\x01",
            "It's really motome.\x02\x03",
            "Anyway, next hiding place\x01",
            "Let's try looking.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A939")

    label("loc_A815")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 7)), scpexpr(EXPR_END)), "loc_A879")

    ChrTalk(
        0x134,
        (
            "#01700FHehe, it was good.\x02\x03",
            "Anyway, next hiding place\x01",
            "Let's try looking for it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A939")

    label("loc_A879")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 0)), scpexpr(EXPR_END)), "loc_A8E5")

    ChrTalk(
        0x135,
        (
            "#01802FHehe, was not it good?\x02\x03",
            "Anyway, next hiding place\x01",
            "Let's try looking.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A939")

    label("loc_A8E5")


    ChrTalk(
        0x166,
        (
            "#14000FHuh, is not it nice?\x02\x03",
            "Anyway, next hiding place\x01",
            "Let's try it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A939")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 7)), scpexpr(EXPR_END)), "loc_A96A")

    ChrTalk(
        0x101,
        "#00000FWell, let's do that.\x02",
    )

    CloseMessageWindow()
    Jump("loc_A989")

    label("loc_A96A")


    ChrTalk(
        0x101,
        "#00000FOh, let's do that.\x02",
    )

    CloseMessageWindow()

    label("loc_A989")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x1C9, 5)
    OP_65(0x0, 0x1)
    OP_29(0x7F, 0x1, 0xD)
    SetChrPos(0x0, -200, 10, -18640, 180)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_51_A136 end

    def Function_52_A9B9(): pass

    label("Function_52_A9B9")

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

    def lambda_AAF6():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AAF6)
    Sleep(50)

    def lambda_AB13():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_AB13)
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

    def lambda_AB8A():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AB8A)
    Sleep(50)

    def lambda_AB9A():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_AB9A)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05200FOh it's Elie and Randy\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(6870, 3000)

    def lambda_ABDA():

        label("loc_ABDA")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_ABDA")

    QueueWorkItem2(0x102, 1, lambda_ABDA)

    def lambda_ABEC():

        label("loc_ABEC")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_ABEC")

    QueueWorkItem2(0x104, 1, lambda_ABEC)

    def lambda_ABFE():
        OP_95(0xFE, 860, 0, -18960, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_ABFE)
    Sleep(50)

    def lambda_AC1B():
        OP_95(0xFE, -120, 50, -20150, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_AC1B)
    WaitChrThread(0x101, 1)

    def lambda_AC39():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AC39)
    WaitChrThread(0x103, 1)

    def lambda_AC4A():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_AC4A)
    OP_6F(0x10)
    Sleep(300)

    ChrTalk(
        0x104,
        "#00309FOh nice work\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FUhufu, both of us\x01",
            "Looks like I'm doing my best.\x02\x03",
            "How are you feeling?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05212FNo, it's pretty tough ……\x01",
            "It is hot inside costume too.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05526FMr. Lloyd ……\x01",
            "Traveling is not a stroll.\x02\x03",
            "#05521FWhile sowing love,\x01",
            "\"Found lucky ☆\"\x01",
            "I have to make a feeling.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05206FOh…. Right\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109FTio-chan ……\x01",
            "When it comes to MICHI\x01",
            "The power is different.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00304FHaha, you kind of spoiled it Mishy\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x1D, 0x80)
    SetChrPos(0x1D, 2880, 1730, -1360, 170)

    NpcTalk(
        0x1D,
        "Female voice",
        "Oh, Misashida ~!\x02",
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

    def lambda_AEBC():
        TurnDirection(0xFE, 0x1C, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AEBC)
    Sleep(50)

    def lambda_AECC():
        OP_95(0xFE, -7940, 0, -14050, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_AECC)
    Sleep(50)

    def lambda_AEE9():
        TurnDirection(0xFE, 0x1C, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_AEE9)
    Sleep(50)

    def lambda_AEF9():
        TurnDirection(0xFE, 0x1C, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_AEF9)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    SetChrPos(0x1C, 2710, 800, -7600, 180)
    SetChrPos(0x1D, 1300, 1050, -7030, 180)
    OP_68(-1280, 3010, -20050, 3000)

    def lambda_AF43():
        OP_95(0xFE, 1930, 0, -16000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_AF43)
    Sleep(50)

    def lambda_AF60():
        OP_95(0xFE, 830, 0, -15580, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_AF60)
    OP_6F(0x1)
    WaitChrThread(0x1C, 1)
    OP_93(0x1C, 0xE1, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x1C,
        (
            "Haha, that's true.\x01",
            "I do not want to see the Ferris wheel on my way home.\x01",
            "I was lucky.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "Yeah, cute ☆\x01",
            "Let's have a picture taken ~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        "OH right\x02",
    )

    CloseMessageWindow()
    OP_95(0x1C, 2800, 0, -17840, 2000, 0x0)
    TurnDirection(0x1C, 0x102, 500)

    def lambda_B030():
        TurnDirection(0xFE, 0x1C, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B030)
    Sleep(50)

    def lambda_B040():
        TurnDirection(0xFE, 0x1C, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_B040)
    Sleep(300)

    ChrTalk(
        0x1C,
        (
            "Excuse me.\x01",
            "Taking a picture with this guy\x01",
            "Can I get it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FYes, of course\x02",
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
            "#05203F(Shu, it is a photo … ….\x01",
            "In such a case\x01",
            "What should I do? )\x07\x00\x02",
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
            "Stand beside my boyfriend\x01",      # 0
            "Stand next to her\x01",      # 1
            "Stand between the two\x01",      # 2
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
        (0, "loc_B1EF"),
        (1, "loc_B2D0"),
        (2, "loc_B3D5"),
        (SWITCH_DEFAULT, "loc_B498"),
    )


    label("loc_B1EF")

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
        "Cars, it is cheerful!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "Hahaha\x01",
            "Is not it okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109FOk here we go\x02\x03",
            "#00102FAnd, Cheese!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B498")

    label("loc_B2D0")

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
            "Kyat, you guys!\x01",
            "Mitsushi Hitotsu ♪\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "Hahaha ……\x01",
            "(Doing well ……)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00111F(Doing well ……)\x02\x03",
            "#00109F……Let me see.\x01",
            "Ok here we go\x02\x03",
            "#00102FAnd, Cheese!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B498")

    label("loc_B3D5")

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
            "Planning is\x01",
            "I Misshii anniversary today ☆\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        "Regards Ssu ~.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109FOk here we go\x02\x03",
            "#00102FAnd, Cheese!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B498")

    label("loc_B498")

    Sound(810, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0x102, 0x3, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)

    ChrTalk(
        0x1D,
        "Thank you very much~.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        "Thanks\x02",
    )

    CloseMessageWindow()

    def lambda_B50D():
        OP_95(0xFE, 0, 440, -21620, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_B50D)
    Sleep(50)

    def lambda_B52A():
        OP_95(0xFE, -1000, 440, -20620, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_B52A)
    WaitChrThread(0x1D, 1)

    def lambda_B548():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_B548)
    WaitChrThread(0x1C, 1)

    def lambda_B559():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_B559)
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    Sleep(500)

    ChrTalk(
        0x102,
        "#00100FHaha, no problem\x02",
    )

    CloseMessageWindow()
    OP_97(0x1C, 0xFFFFFC18, 0x0, 0x0, 0x7D0, 0x0)

    def lambda_B5A8():
        OP_95(0xFE, -940, 2840, -31020, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_B5A8)
    Sleep(50)

    def lambda_B5C5():
        OP_95(0xFE, -940, 2840, -31020, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_B5C5)
    Sleep(50)

    def lambda_B5E2():
        OP_95(0xFE, 0, 0, -18900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B5E2)

    def lambda_B5FC():
        OP_95(0xFE, -400, 0, -17600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_B5FC)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0xB4, 0x1F4)
    WaitChrThread(0x103, 1)
    TurnDirection(0x103, 0x101, 500)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x1D, 0x80)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B7A7")

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05204FFuu …\x01",
            "I wish it was good now.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Sound(2680, 255, 100, 0)

    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05524FPerfect, Lloyd\x02\x03",
            "#05520FMikoshi is, so to speak,\x01",
            "Symbol of theme park ……\x01",
            "It is like a walking tourist attraction.\x02\x03",
            "#05524FOh yeah,\x01",
            "It is right to stand in the middle\x01",
            "I think that it is More · Better.\x02\x03",
            "#05522FIt's pretty cool\x01",
            "You followed the board.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05209FHaha, thanks\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x86, 0x1, 0x5)
    Jump("loc_BA32")

    label("loc_B7A7")


    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05204FFuu …\x01",
            "It is good so now ──\x07\x00\x02",
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
            "#05211FA whip Is it?\x07\x00\x02",
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
            "#05526F…… I am disappointed with Mr. Lloyd.\x02\x03",
            "#05531F… … why bother\x01",
            "Did you change the standing position?\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05205FNo……\x01",
            "It is also possible to enter between couples\x01",
            "Thinking … …\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05526FHa\x01",
            "Please think carefully.\x02\x03",
            "#05520FMikoshi is, so to speak,\x01",
            "Symbol of theme park ……\x01",
            "It is like a walking tourist attraction.\x02\x03",
            "#05531FOh yeah,\x01",
            "It is right to stand in the middle\x01",
            "I think that it is More · Better.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05206FThat's right.\x01",
            "(Do not be afraid\x01",
            "I should have done it …).\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x86, 0x1, 0x6)

    label("loc_BA32")


    ChrTalk(
        0x102,
        (
            "#00104FHuhu, that's what it is\x01",
            "If there is Tio\x01",
            "Surely okay.\x02\x03",
            "#00100FGood luck with both of you.\x01",
            "Because we are also watching.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309FHaha\x01",
            "I'm going out for a date!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x104, 1000)
    Sleep(300)

    ChrTalk(
        0x102,
        "#00103FNope.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x102, 500)
    Sleep(300)

    ChrTalk(
        0x104,
        "#00306FUgh, rejected\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05200FHahaha … as much as you can\x01",
            "I'll try it right.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05520FWell let's go on to the next one\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 2)
    NewScene("t1300", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_52_A9B9 end

    def Function_53_BBA3(): pass

    label("Function_53_BBA3")

    OP_97(0x101, 0x0, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
    OP_97(0x101, 0x6A4, 0x0, 0x0, 0x7D0, 0x0)
    OP_97(0x101, 0x0, 0x0, 0x3E8, 0x7D0, 0x0)

    def lambda_BBE4():
        OP_97(0xFE, 0xFFFFFC18, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_BBE4)
    Sleep(50)

    def lambda_BC01():
        OP_97(0xFE, 0xFFFFFE0C, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BC01)
    WaitChrThread(0x1C, 1)

    def lambda_BC1F():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_BC1F)
    WaitChrThread(0x101, 1)

    def lambda_BC30():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BC30)
    Return()

    # Function_53_BBA3 end

    def Function_54_BC39(): pass

    label("Function_54_BC39")

    OP_97(0x101, 0x0, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
    OP_97(0x101, 0xFFFFF95C, 0x0, 0x0, 0x7D0, 0x0)
    OP_97(0x101, 0x0, 0x0, 0x3E8, 0x7D0, 0x0)

    def lambda_BC7A():
        OP_97(0xFE, 0x3E8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_BC7A)
    Sleep(50)

    def lambda_BC97():
        OP_97(0xFE, 0x1F4, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BC97)
    WaitChrThread(0x1D, 1)

    def lambda_BCB5():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_BCB5)
    WaitChrThread(0x101, 1)

    def lambda_BCC6():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BCC6)
    Return()

    # Function_54_BC39 end

    def Function_55_BCCF(): pass

    label("Function_55_BCCF")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Of the theme park\x01",
            "A sketch is drawn.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Return()

    # Function_55_BCCF end

    def Function_56_BD0D(): pass

    label("Function_56_BD0D")

    EventBegin(0x1)
    TurnDirection(0x14, 0x0, 500)
    OP_4B(0x14, 0xFF)

    ChrTalk(
        0x14,
        (
            "When you ride a Ferris wheel\x01",
            "Tickets to this person\x01",
            "Please hand it in.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -330, 0, -15900, 350)
    OP_93(0x14, 0xA0, 0x0)
    OP_4C(0x14, 0xFF)
    EventEnd(0x4)
    Return()

    # Function_56_BD0D end

    SaveToFile()

Try(main)
