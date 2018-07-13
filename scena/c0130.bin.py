from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c0130.bin",                # FileName
        "c0130",                    # MapName
        "c0130",                    # Location
        0x0009,                     # MapIndex
        "ed7150",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 9, 0, 1, 0, 2],
    )

    BuildStringList((
        "c0130",                  # 0
        "KeA",                    # 1
        "KeA",                    # 2
        "Zeit",                   # 3
        "SE制御",                 # 4
    ))

    AddCharChip((
        "chr/ch08200.itc",                   # 00
        "chr/ch08202.itc",                   # 01
        "chr/ch02707.itc",                   # 02
    ))

    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   0,   0,   0,   3,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    405,  0x0, 0,   2,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 9,   1.0,                   -0.5,                  -1.0,                  4.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.5,                  0.25,                  0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 10,  -3.299999952316284,    68.0,                  -1.0,                  4.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   1.649999976158142,     -34.0,                 0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 11,  1.0,                   71.5,                  0.0,                   9.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000001788139343,   0.0,                   -0.5,                  -23.83333396911621,    -0.0,                  1.0])

    DeclActor(13960,   0,       63640,   1500,    13960,   1500,    63640,   0x007C, 0,  8,  0x0000)
    DeclActor(170000,  0,       63560,   1500,    170000,  1500,    63560,   0x007C, 0,  7,  0x0000)
    DeclActor(158830,  0,       125480,  1200,    158830,  2000,    125480,  0x007C, 0,  27, 0x0000)
    DeclActor(155320,  30,      123780,  1200,    155320,  1500,    123780,  0x007C, 0,  28, 0x0000)
    DeclActor(205730,  0,       130250,  1200,    205730,  1500,    130250,  0x007C, 0,  30, 0x0000)
    DeclActor(208820,  0,       123770,  1200,    208820,  2500,    123770,  0x007C, 0,  31, 0x0000)
    DeclActor(259740,  0,       121980,  1200,    259740,  3000,    121980,  0x007C, 0,  32, 0x0000)
    DeclActor(259339,  0,       126100,  1200,    259339,  1500,    126100,  0x007C, 0,  33, 0x0000)
    DeclActor(255780,  30,      65319,   1200,    255780,  1500,    65319,   0x007C, 0,  34, 0x0000)
    DeclActor(257120,  30,      68930,   1200,    257120,  1030,    68930,   0x007C, 0,  35, 0x0000)
    DeclActor(259010,  0,       66930,   1200,    259010,  1000,    66930,   0x007C, 0,  36, 0x0000)
    DeclActor(255680,  30,      73720,   1200,    255680,  1500,    73720,   0x007C, 0,  37, 0x0000)
    DeclActor(258000,  0,       63980,   1200,    258000,  2000,    63980,   0x007C, 0,  38, 0x0000)
    DeclActor(153580,  30,      127880,  1200,    153370,  1530,    128389,  0x007C, 0,  24, 0x0000)
    DeclActor(207040,  30,      128539,  1200,    207640,  1500,    129090,  0x007C, 0,  25, 0x0000)
    DeclActor(258360,  0,       128430,  1200,    258360,  1500,    128430,  0x007C, 0,  26, 0x0000)
    DeclActor(253320,  30,      71340,   1200,    253320,  1500,    71340,   0x007C, 0,  12, 0x0000)

    ChipFrameInfo(1472, 0)                                       # 0

    ScpFunction((
        "Function_0_5C0",          # 00, 0
        "Function_1_670",          # 01, 1
        "Function_2_950",          # 02, 2
        "Function_3_CDC",          # 03, 3
        "Function_4_100D",         # 04, 4
        "Function_5_10D2",         # 05, 5
        "Function_6_1500",         # 06, 6
        "Function_7_1C1B",         # 07, 7
        "Function_8_1C65",         # 08, 8
        "Function_9_1CB1",         # 09, 9
        "Function_10_1D83",        # 0A, 10
        "Function_11_1E55",        # 0B, 11
        "Function_12_1EC4",        # 0C, 12
        "Function_13_2963",        # 0D, 13
        "Function_14_2C50",        # 0E, 14
        "Function_15_2F62",        # 0F, 15
        "Function_16_3178",        # 10, 16
        "Function_17_33A0",        # 11, 17
        "Function_18_35B1",        # 12, 18
        "Function_19_37C2",        # 13, 19
        "Function_20_39DB",        # 14, 20
        "Function_21_3BF4",        # 15, 21
        "Function_22_400E",        # 16, 22
        "Function_23_4135",        # 17, 23
        "Function_24_41A1",        # 18, 24
        "Function_25_423F",        # 19, 25
        "Function_26_42DD",        # 1A, 26
        "Function_27_437B",        # 1B, 27
        "Function_28_4433",        # 1C, 28
        "Function_29_4510",        # 1D, 29
        "Function_30_4519",        # 1E, 30
        "Function_31_45D0",        # 1F, 31
        "Function_32_4688",        # 20, 32
        "Function_33_473D",        # 21, 33
        "Function_34_47EF",        # 22, 34
        "Function_35_48A4",        # 23, 35
        "Function_36_495D",        # 24, 36
        "Function_37_4A12",        # 25, 37
        "Function_38_4ACE",        # 26, 38
        "Function_39_4B86",        # 27, 39
        "Function_40_4BFB",        # 28, 40
        "Function_41_4C2A",        # 29, 41
        "Function_42_4C59",        # 2A, 42
        "Function_43_4C88",        # 2B, 43
        "Function_44_4CB7",        # 2C, 44
        "Function_45_59ED",        # 2D, 45
        "Function_46_59F5",        # 2E, 46
        "Function_47_6D1E",        # 2F, 47
        "Function_48_6D78",        # 30, 48
        "Function_49_6D94",        # 31, 49
        "Function_50_79D1",        # 32, 50
        "Function_51_79ED",        # 33, 51
        "Function_52_9539",        # 34, 52
        "Function_53_9588",        # 35, 53
        "Function_54_95B1",        # 36, 54
        "Function_55_9650",        # 37, 55
        "Function_56_9667",        # 38, 56
        "Function_57_967E",        # 39, 57
        "Function_58_9695",        # 3A, 58
        "Function_59_96AC",        # 3B, 59
        "Function_60_96C8",        # 3C, 60
        "Function_61_96E4",        # 3D, 61
        "Function_62_9700",        # 3E, 62
        "Function_63_973F",        # 3F, 63
        "Function_64_9785",        # 40, 64
        "Function_65_97B2",        # 41, 65
        "Function_66_97CE",        # 42, 66
        "Function_67_97FE",        # 43, 67
        "Function_68_981A",        # 44, 68
        "Function_69_A1C3",        # 45, 69
        "Function_70_A218",        # 46, 70
        "Function_71_A270",        # 47, 71
        "Function_72_A2C8",        # 48, 72
        "Function_73_A320",        # 49, 73
        "Function_74_AE77",        # 4A, 74
    ))


    def Function_0_5C0(): pass

    label("Function_0_5C0")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_5F8"),
        (1, "loc_604"),
        (2, "loc_610"),
        (3, "loc_61C"),
        (4, "loc_628"),
        (5, "loc_634"),
        (6, "loc_640"),
        (SWITCH_DEFAULT, "loc_64C"),
    )


    label("loc_5F8")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_658")

    label("loc_604")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_658")

    label("loc_610")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_658")

    label("loc_61C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_658")

    label("loc_628")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_658")

    label("loc_634")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_658")

    label("loc_640")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_658")

    label("loc_64C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_658")

    label("loc_658")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_66F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_658")

    label("loc_66F")

    Return()

    # Function_0_5C0 end

    def Function_1_670(): pass

    label("Function_1_670")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_82B")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6D), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x34B, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6A5")
    Event(0, 16)

    label("loc_6A5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6D), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x34A, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6CC")
    Event(0, 15)

    label("loc_6CC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x34D, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6F3")
    Event(0, 18)

    label("loc_6F3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x34C, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_71A")
    Event(0, 17)

    label("loc_71A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x74), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x351, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_741")
    Event(0, 20)

    label("loc_741")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x74), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x350, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_768")
    Event(0, 19)

    label("loc_768")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x74), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13B, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_783")
    Event(0, 5)

    label("loc_783")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_82B")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x71), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x358, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7BB")
    Event(0, 21)

    label("loc_7BB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x71), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x357, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7D7")
    Event(0, 21)

    label("loc_7D7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x71), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x356, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7F3")
    Event(0, 21)

    label("loc_7F3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x71), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x355, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_80F")
    Event(0, 21)

    label("loc_80F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x71), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x354, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_82B")
    Event(0, 21)

    label("loc_82B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_839")
    Jump("loc_935")

    label("loc_839")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_889")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    ClearChrFlags(0x8, 0x1)
    SetChrPos(0x8, 257500, 500, 68000, 270)
    SetChrPos(0xA, 258550, 0, 66740, 180)
    Jump("loc_935")

    label("loc_889")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_897")
    Jump("loc_935")

    label("loc_897")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_8DB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x170, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8D6")
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    SetChrPos(0x8, 257500, 500, 68000, 270)
    ClearChrFlags(0x8, 0x1)

    label("loc_8D6")

    Jump("loc_935")

    label("loc_8DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_8E9")
    Jump("loc_935")

    label("loc_8E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_8F7")
    Jump("loc_935")

    label("loc_8F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_92C")
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    SetChrPos(0x8, 254100, 200, 71300, 270)
    Jump("loc_935")

    label("loc_92C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_935")

    label("loc_935")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x71), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_94F")
    Event(0, 68)

    label("loc_94F")

    Return()

    # Function_1_670 end

    def Function_2_950(): pass

    label("Function_2_950")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_963")
    OP_1B(0x2, 0x0, 0x49)

    label("loc_963")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9AD")
    OP_7D(0xD2, 0xD2, 0xE6, 0x0, 0x0)
    SetMapObjFrame(0xFF, "wlight_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ylight_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "out_add", 0x0, 0x1)

    label("loc_9AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A01")
    SetMapObjFrame(0xFF, "wlight_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ylight_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "out_add", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_A01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_A86")
    SetMapObjFrame(0xFF, "danbo", 0x1, 0x1)
    SetMapObjFrame(0xFF, "n01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "n02", 0x0, 0x1)
    SetMapObjFrame(0xFF, "n03", 0x0, 0x1)
    SetMapObjFrame(0xFF, "asihuki", 0x0, 0x1)
    SetBarrier(0x0, 0x0, 0x1, 0x0, 255600, -1000, 128900, 8000, 5000, 0)
    SetBarrier(0x0, 0x1, 0x1, 0x0, 258899, -1000, 126000, 5000, 5000, 90000)
    Jump("loc_AC3")

    label("loc_A86")

    SetMapObjFrame(0xFF, "danbo", 0x0, 0x1)
    SetMapObjFrame(0xFF, "n01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "n02", 0x1, 0x1)
    SetMapObjFrame(0xFF, "n03", 0x1, 0x1)
    SetMapObjFrame(0xFF, "asihuki", 0x1, 0x1)

    label("loc_AC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_ADD")
    SetMapObjFlags(0x8, 0x4)
    ClearMapObjFlags(0x8, 0x2)
    OP_65(0x2, 0x1)

    label("loc_ADD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B08")
    SetMapObjFlags(0x9, 0x4)
    ClearMapObjFlags(0x9, 0x2)
    OP_65(0x3, 0x1)
    SetMapObjFlags(0x14, 0x4)
    ClearMapObjFlags(0x14, 0x2)
    Jump("loc_B0E")

    label("loc_B08")

    SetMapObjFlags(0x13, 0x4)

    label("loc_B0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B28")
    SetMapObjFlags(0xA, 0x4)
    ClearMapObjFlags(0xA, 0x2)
    OP_65(0x4, 0x1)

    label("loc_B28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B42")
    SetMapObjFlags(0xB, 0x4)
    ClearMapObjFlags(0xB, 0x2)
    OP_65(0x5, 0x1)

    label("loc_B42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B60")
    SetMapObjFlags(0xC, 0x4)
    ClearMapObjFlags(0xC, 0x2)
    OP_65(0x6, 0x1)

    label("loc_B60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B7E")
    SetMapObjFlags(0xD, 0x4)
    ClearMapObjFlags(0xD, 0x2)
    OP_65(0x7, 0x1)

    label("loc_B7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B98")
    SetMapObjFlags(0xE, 0x4)
    ClearMapObjFlags(0xE, 0x2)
    OP_65(0x8, 0x1)

    label("loc_B98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BB2")
    SetMapObjFlags(0xF, 0x4)
    ClearMapObjFlags(0xF, 0x2)
    OP_65(0x9, 0x1)

    label("loc_BB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BCC")
    SetMapObjFlags(0x10, 0x4)
    ClearMapObjFlags(0x10, 0x2)
    OP_65(0xA, 0x1)

    label("loc_BCC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BE6")
    SetMapObjFlags(0x11, 0x4)
    ClearMapObjFlags(0x11, 0x2)
    OP_65(0xB, 0x1)

    label("loc_BE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C00")
    SetMapObjFlags(0x12, 0x4)
    ClearMapObjFlags(0x12, 0x2)
    OP_65(0xC, 0x1)

    label("loc_C00")

    OP_65(0x10, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C1, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BC, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C6F")
    LoadEffect(0x10, "event\\eva00_00.eff")
    PlayEffect(0x10, 0x9, 0xFF, 0x0, 253320, 1200, 71340, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x10, 0x1)

    label("loc_C6F")

    ClearMapObjFlags(0x1, 0x10)
    ClearMapObjFlags(0x4, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_C8E")
    SetMapObjFlags(0x1, 0x10)
    OP_65(0x0, 0x1)

    label("loc_C8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_CA1")
    SetMapObjFlags(0x4, 0x10)
    OP_65(0x1, 0x1)

    label("loc_CA1")

    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CC3")
    ModifyEventFlags(1, 0, 0x80)
    ModifyEventFlags(1, 1, 0x80)

    label("loc_CC3")

    ModifyEventFlags(0, 2, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CDB")
    ModifyEventFlags(1, 2, 0x80)

    label("loc_CDB")

    Return()

    # Function_2_950 end

    def Function_3_CDC(): pass

    label("Function_3_CDC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_CED")
    Jump("loc_1009")

    label("loc_CED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_D9A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19D, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D08")
    Call(0, 74)
    Jump("loc_D95")

    label("loc_D08")


    ChrTalk(
        0x8,
        (
            "#01108FIf Noｱl goes away,\x01",
            "KeA too will be sad...\x01",
            "Cheer up, Noｱl.\x02\x03",
            "#01102FI'll wait for you and a healthy\x01",
            "Fran to come to have fun here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D95")

    Jump("loc_1009")

    label("loc_D9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_DA8")
    Jump("loc_1009")

    label("loc_DA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_DC7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x170, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DC2")
    TalkEnd(0xFE)
    Call(0, 6)
    Return()

    label("loc_DC2")

    Jump("loc_1009")

    label("loc_DC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1009")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13E, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F8A")

    ChrTalk(
        0x8,
        "#01105FAh, Lloyd, guys, are you going out?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYeah. KeA, are you doing Sunday School homework?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01100FYes, since I can't go play outside today,\x01",
            "I thought to do them earlier.\x02\x03",
            "#01106FThe truth is that I really\x01",
            "wanted to ride in that car.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FUuh, what a pity.\x02\x03",
            "#10109FNext time, let's go for a drive with everyone\x01",
            "when we're on a break and it's sunny, ok?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#01109FYes! I'll look forward to it!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x13E, 1)
    Jump("loc_1009")

    label("loc_F8A")


    ChrTalk(
        0x8,
        (
            "#01109FEhehe, I can't wait for the\x01",
            "next day of clear weather.\x02\x03",
            "#01110FAlright, today I'm going to\x01",
            "do my homework quickly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1009")

    TalkEnd(0xFE)
    Return()

    # Function_3_CDC end

    def Function_4_100D(): pass

    label("Function_4_100D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_10CE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10B2")

    ChrTalk(
        0xA,
        "#01203FGrrrowl...woof.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FIt appears that Zeit is saying\x01",
            ""Stay well" to Miss Noｱl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10109FAhaha...\x01",
            "Thank you, Zeit.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_10CE")

    label("loc_10B2")


    ChrTalk(
        0xA,
        "#01203FGrrrowl...woof.\x02",
    )

    CloseMessageWindow()

    label("loc_10CE")

    TalkEnd(0xFE)
    Return()

    # Function_4_100D end

    def Function_5_10D2(): pass

    label("Function_5_10D2")

    EventBegin(0x0)
    Fade(500)
    OP_68(256649, 800, 124480, 0)
    MoveCamera(26, 22, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(24500, 0)
    SetChrPos(0x102, 257410, 0, 124690, 45)
    SetChrPos(0x101, 255000, 0, 124690, 315)
    SetChrPos(0x109, 256829, 0, 121730, 0)
    SetChrPos(0x105, 255220, 0, 122530, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0xA4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_116C")
    SetChrPos(0x1A5, 256209, 0, 125400, 0)

    label("loc_116C")

    OP_0D()

    ChrTalk(
        0x109,
        (
            "#12P#10100FUhhm, this is my room.\x02\x03",
            "#10106FI don't have many interests\x01",
            "so I'm a bit embarrassed...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300FHu hu, it's nice\x01",
            "and clean, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00102FYes, I think it's nice, it's\x01",
            "typical of Miss Noｱl.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0xA4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1357")
    OP_93(0x1A5, 0x87, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x1A5,
        (
            "#5P#01105FHey hey, what's with the\x01",
            "bear over there?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_12A1():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_12A1)

    def lambda_12AE():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_12AE)
    Sleep(50)

    def lambda_12BE():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_12BE)
    Sleep(50)

    def lambda_12CE():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_12CE)
    WaitChrThread(0x109, 1)

    ChrTalk(
        0x109,
        (
            "#12P#10109FAhaha...\x01",
            "It's a plushy I have as\x01",
            "a match to Fran's.\x02\x03",
            "#10100FI brought it from my guard\x01",
            "room at the CGF.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1433")

    label("loc_1357")

    OP_93(0x101, 0x87, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#5P#00000FOh, that plushy\x01",
            "over there...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1390():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1390)
    Sleep(50)

    def lambda_13A0():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_13A0)
    Sleep(50)

    def lambda_13B0():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_13B0)
    WaitChrThread(0x109, 1)

    ChrTalk(
        0x109,
        (
            "#12P#10109FAhaha...\x01",
            "It's a plushy I have as\x01",
            "a match to Fran's.\x02\x03",
            "#10100FI bought it from my guard\x01",
            "room at the CGF.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1433")


    ChrTalk(
        0x101,
        (
            "#5P#00000FHa ha, I see.\x01",
            "It's nice to give emphasis.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10100FUh uh, thank you very much.\x02\x03",
            "#10104FUhm, then, once again...\x01",
            "I am inexperienced, but please, treat me well.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 256010, 0, 121130, 0)
    SetScenarioFlags(0x13B, 6)
    EventEnd(0x5)
    Return()

    # Function_5_10D2 end

    def Function_6_1500(): pass

    label("Function_6_1500")

    EventBegin(0x0)
    Fade(500)
    OP_68(256920, 1000, 67670, 0)
    MoveCamera(50, 21, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x101, 255850, 0, 68670, 135)
    SetChrPos(0x102, 256720, 30, 66620, 45)
    SetChrPos(0x103, 254820, 30, 69190, 135)
    SetChrPos(0x104, 254420, 0, 67580, 90)
    SetChrPos(0x109, 255300, 30, 66540, 56)
    SetChrPos(0x105, 258360, 0, 66040, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)

    def lambda_15B4():

        label("loc_15B4")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_15B4")

    QueueWorkItem2(0x101, 2, lambda_15B4)

    def lambda_15C6():

        label("loc_15C6")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_15C6")

    QueueWorkItem2(0x102, 2, lambda_15C6)

    def lambda_15D8():

        label("loc_15D8")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_15D8")

    QueueWorkItem2(0x103, 2, lambda_15D8)

    def lambda_15EA():

        label("loc_15EA")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_15EA")

    QueueWorkItem2(0x104, 2, lambda_15EA)

    def lambda_15FC():

        label("loc_15FC")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_15FC")

    QueueWorkItem2(0x109, 2, lambda_15FC)

    def lambda_160E():

        label("loc_160E")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_160E")

    QueueWorkItem2(0x105, 2, lambda_160E)
    OP_0D()

    ChrTalk(
        0x8,
        "#11P#01110FAh, everyone...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#00200FKeA...are you alright?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00108FYou've been spent\x01",
            "since yesterday...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#01102FEhehe, yes.\x01",
            "KeA is alright...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x8)

    ChrTalk(
        0x8,
        (
            "#11P#01103FHey, Lloyd...\x02\x03",
            "#01108FIs healing Shizuku's eyes\x01",
            "difficult like I think...?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x170, 3)), scpexpr(EXPR_END)), "loc_17E9")

    ChrTalk(
        0x101,
        (
            "#6P#00003F...Yeah, I think it is.\x01\x02\x03",
            "#00000FHowever, Shizuku was\x01",
            "positive, even now.\x02\x03",
            "Far from being sad, she\x01",
            "was happy that medical\x01",
            "treatments made progress.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1858")

    label("loc_17E9")


    ChrTalk(
        0x101,
        (
            "#6P#00003F...Yeah, I think it is.\x01\x02\x03",
            "#00008FThe surgery she went\x01",
            "through seems it wasn't\x01",
            "a failure, but...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1858")


    ChrTalk(
        0x8,
        "#11P#01106FI see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00303FHey, Keddo.\x01",
            "I know you're said, but...\x01",
            "Isn't it time you cheer up?\x02\x03",
            "#00300FDidn't Shizuku herself said\x01",
            "that she doesn't want for you\x01",
            "to be so said, hm, Keddo?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10103FR-Right, KeA.\x02\x03",
            "#10102FI think that if you smiled\x01",
            "for her it would be better,\x01",
            "even Shizuku would be happy!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#01108F...Yes, you're right.\x02\x03",
            "#01102FKeA is Shizuku's friend...\x01",
            "Next time I see her, I must encourage her.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(500)
    ClearChrFlags(0x8, 0x4)
    ClearChrFlags(0x8, 0x20)
    ClearChrFlags(0x8, 0x2)
    SetChrFlags(0x8, 0x1)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, 256600, 0, 67990, 270)
    SetChrFlags(0x8, 0x40)
    Sound(802, 0, 100, 0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#11P#01109FEhehe, thanks guys.\x01",
            "KeA too has cheered up a little.\x02\x03",
            "#01100FUhm, I've made a promise,\x01",
            "so I'm going to play.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00005FY-Yeah...be careful.\x02",
    )

    CloseMessageWindow()
    OP_95(0x8, 252320, 0, 65790, 2000, 0x1)

    def lambda_1B08():
        OP_95(0xFE, 251280, 0, 65770, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1B08)

    def lambda_1B22():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1B22)
    WaitChrThread(0x8, 1)
    WaitChrThread(0x8, 2)
    SetChrFlags(0x8, 0x80)
    EndChrThread(0x0, 0x2)
    EndChrThread(0x1, 0x2)
    EndChrThread(0x2, 0x2)
    EndChrThread(0x3, 0x2)
    EndChrThread(0x4, 0x2)
    EndChrThread(0x5, 0x2)
    Sleep(200)
    Sound(104, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x105,
        "#11P#10308F...Is she okay?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FI don't know, but...\x01",
            "I'd like she cheered\x01",
            "up immediately.\x02\x03",
            "#00000FWell then, should we go?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x0, 255390, 0, 67800, 225)
    SetScenarioFlags(0x170, 5)
    OP_50(0x64, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    EventEnd(0x5)
    Return()

    # Function_6_1500 end

    def Function_7_1C1B(): pass

    label("Function_7_1C1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13B, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C2D")
    Call(0, 13)
    Jump("loc_1C64")

    label("loc_1C2D")

    TalkBegin(0xFF)

    ChrTalk(
        0x101,
        (
            "#00000FThis is Tio's room.\x01",
            "Let's not enter.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)

    label("loc_1C64")

    Return()

    # Function_7_1C1B end

    def Function_8_1C65(): pass

    label("Function_8_1C65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13B, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C77")
    Call(0, 14)
    Jump("loc_1CB0")

    label("loc_1C77")

    TalkBegin(0xFF)

    ChrTalk(
        0x101,
        (
            "#00000FThis is Randy's room.\x01",
            "Let's not enter.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)

    label("loc_1CB0")

    Return()

    # Function_8_1C65 end

    def Function_9_1CB1(): pass

    label("Function_9_1CB1")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000F...Now that I think about it, KeA said\x01",
            "she was going to Sunday School.\x02\x03",
            "Chief has gone out too, maybe it\x01",
            "would be better going out together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FYes, let's ask her.\x02",
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 800, 0, 1890, 0)
    EventEnd(0x4)
    Return()

    # Function_9_1CB1 end

    def Function_10_1D83(): pass

    label("Function_10_1D83")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000F...Now that I think about it, KeA said\x01",
            "she was going to Sunday School.\x02\x03",
            "Chief has gone out too, maybe it\x01",
            "would be better going out together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FYes, let's ask her.\x02",
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -2190, 0, 68010, 90)
    EventEnd(0x4)
    Return()

    # Function_10_1D83 end

    def Function_11_1E55(): pass

    label("Function_11_1E55")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000FKeA is going to Sunday School.\x01",
            "Let's use the back entrance as a shortcut.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -1330, 0, 71380, 268)
    EventEnd(0x4)
    Return()

    # Function_11_1E55 end

    def Function_12_1EC4(): pass

    label("Function_12_1EC4")

    EventBegin(0x0)
    FadeToDark(500, 0, -1)
    OP_0D()
    StopEffect(0x9, 0x0)
    OP_65(0x10, 0x1)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis382.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis383.itp")
    CreatePortrait(2, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis384.itp")
    CreatePortrait(3, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis385.itp")
    OP_68(253680, 1430, 71690, 0)
    MoveCamera(44, 21, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(21000, 0)
    SetChrPos(0x101, 254540, 30, 72300, 225)
    SetChrPos(0x102, 253960, 30, 69890, 315)
    SetChrPos(0x103, 255030, 30, 71510, 270)
    SetChrPos(0x104, 255370, 30, 70080, 315)
    SetChrPos(0xF4, 256240, 30, 72240, 270)
    SetChrPos(0xF5, 256019, 30, 71220, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    FadeToBright(1000, 0)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005FThis is...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)

    ChrTalk(
        0x104,
        (
            "#12P#00302FEeh, a white stone?\x01",
            "Isn't it quite pretty?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#11P#00205FI'm sure this is...\x02\x03",
            "#00200FThe one Mr. Lloyd gave to KeA\x01",
            "as a present at Michelam...?\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x101)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#00006FYeah, it's the "White Stone" I gave\x01",
            "to KeA at the beach at Michelam.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00108FCould KeA have forgotten it...?\x01\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd took the White Stone in his hand.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopBGM(0xBB8)
    FadeToDark(500, 0, -1)
    OP_0D()
    Sound(824, 0, 100, 0)
    Sleep(1000)
    Sound(2955, 255, 50, 0)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(2200)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#00011F#30W.........eh.........\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7534", 0)
    Sound(824, 0, 100, 0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    Sound(2956, 255, 50, 0)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(2600)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(300)
    Sound(2957, 255, 60, 0)
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    Sleep(500)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    Sleep(300)
    Sound(2958, 255, 75, 0)
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    Sleep(1000)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    Sleep(300)
    Sound(2959, 255, 90, 0)
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    Sleep(1000)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    Sleep(300)
    Sleep(2000)
    Sound(2960, 255, 100, 0)
    OP_CB(0x3, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x3, 0x3)
    Sleep(2500)
    FadeToDark(2000, 16777215, -1)
    Sound(829, 0, 100, 0)
    OP_CB(0x3, 0x3, 0xFFFFFF, 0x7D0, 0x0, 0x0)
    OP_0D()
    SetCameraDistance(19000, 0)
    SetCameraDistance(21000, 2000)
    FadeToBright(2000, 16777215)
    OP_0D()
    OP_CC(0x0, 0x3, 0x3)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005F#40W............\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2429")

    ChrTalk(
        0x106,
        (
            "#11P#10708F#30WW-Was that...\x01",
            "KeA?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_249C")

    label("loc_2429")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2465")

    ChrTalk(
        0x109,
        (
            "#11P#10113F#30WW-Was that...\x01",
            "KeA?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_249C")

    label("loc_2465")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_249C")

    ChrTalk(
        0x105,
        "#11P#10408F#30WWas that...KeA...?\x02",
    )

    CloseMessageWindow()

    label("loc_249C")


    ChrTalk(
        0x104,
        (
            "#12P#00301F#30WNo doubt she was.\x01",
            "...But where was she...?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            "#11P#00206F#30WIn what Mr. Lloyd had in his hand\x01",
            "I also sense something like\x01",
            "residual thoughts were put in.\x02\x03",
            "#00208F...Like sadness and indecision\x01",
            "were forcibly crowded inside...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00106F#30WKeA...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2614")

    ChrTalk(
        0x10A,
        (
            "#11P#00608F#30W...Honestly...\x01",
            "That insolent and innocent child...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26A8")

    label("loc_2614")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_265F")

    ChrTalk(
        0x105,
        (
            "#11P#10408F#30W...Oh boy.\x01",
            "A child so innocent...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26A8")

    label("loc_265F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_26A8")

    ChrTalk(
        0x109,
        (
            "#11P#10106F#30W...KeA gave it that\x01",
            "much thoughts...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26A8")

    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#00006F#30W...With this, now...\x01",
            "A piece of indecision completely vanished.\x02\x03",
            "#00015FKeA...\x01",
            "She has always been concealing\x01",
            "her emotions and feelings...\x02\x03",
            "#00010FSuch a situation is completely wrong!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00101FRight... There's no way that\x01",
            "that it's something right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00307F...This being the case,\x01",
            "we have to reach Keddo\x01",
            "by all costs!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#11P#00201FYes, also in order to\x01",
            "retrieve KeA's smile...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00007FYeah...let's go, everyone.\x02\x03",
            "#00003F(KeA...wait for us.\x01",
            "We're coming to get you...!)\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xBB8)
    SetCameraDistance(21375, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    WaitBGM()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x3A1),
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x3A1, 1)
    OP_49()
    OP_CC(0x1, 0xFF, 0x0)
    Sleep(10)
    OP_1F()
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x0, 254410, 30, 69820, 225)
    SetScenarioFlags(0x1BC, 5)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AD, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BC, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DE, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D9, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DE, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2960")
    OP_E0(0x34, 0x0)

    label("loc_2960")

    EventEnd(0x5)
    Return()

    # Function_12_1EC4 end

    def Function_13_2963(): pass

    label("Function_13_2963")

    EventBegin(0x0)
    Fade(500)
    OP_68(169990, 1000, 63110, 0)
    MoveCamera(43, 25, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(23860, 0)
    SetChrPos(0x101, 170800, 0, 62310, 315)
    SetChrPos(0x102, 168790, 0, 62190, 45)
    SetChrPos(0x109, 171240, 0, 63400, 270)
    SetChrPos(0x105, 168190, 0, 63200, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0xA4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_29FD")
    SetChrPos(0x1A5, 169520, 0, 61730, 0)

    label("loc_29FD")

    OP_0D()

    ChrTalk(
        0x102,
        "#6P#00100FThis is Tio's room.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300FShe's currently on a business trip in\x01",
            "the autonomous state of Leman, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah, she went with Jona\x01",
            "to the Epstein Foundation\x01",
            "research lab.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00100FWith the state laws revised, even\x01",
            "the orbal net spreading has been\x01",
            "proceeding. They are helping with that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#11P#10103FI don't understand complicated things, but...\x01",
            "They seem to have it hard too.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0xA4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2BFB")

    ChrTalk(
        0x1A5,
        "#12P#01100FI hope Tio comes home fast.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYeah, really.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2C38")

    label("loc_2BFB")


    ChrTalk(
        0x101,
        (
            "#00000FYeah, it would be nice if\x01",
            "she came back quickly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C38")

    OP_5A()
    SetChrPos(0x0, 169990, 0, 63110, 180)
    SetScenarioFlags(0x13B, 3)
    EventEnd(0x5)
    Return()

    # Function_13_2963 end

    def Function_14_2C50(): pass

    label("Function_14_2C50")

    EventBegin(0x0)
    Fade(500)
    OP_68(14040, 800, 63300, 0)
    MoveCamera(41, 26, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(23800, 0)
    SetChrPos(0x101, 12730, 0, 61720, 45)
    SetChrPos(0x102, 14330, 0, 61720, 315)
    SetChrPos(0x109, 11530, 0, 62750, 90)
    SetChrPos(0x105, 15130, 0, 62750, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0xA4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2CEA")
    SetChrPos(0x1A5, 13500, 0, 61420, 0)

    label("loc_2CEA")

    OP_0D()

    ChrTalk(
        0x101,
        "#12P#00000FThis is Randy's room.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FRandy is currently in the midst\x01",
            "of rehabilitation training at\x01",
            "Tangram Gate with the CGF.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10305FAh, if I remember correctly, during the Cult\x01",
            "incident they were served that drug, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10103FYes...\x01",
            "Severe after-effects\x01",
            "didn't remain though.\x02\x03",
            "#10108FTo regain stamina and their senses\x01",
            "it seems it will take some time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003FI see...\x01",
            "I hope the CGF recover quickly.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0xA4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2F0A")

    ChrTalk(
        0x1A5,
        "#12P#01100FI wish Randy too came back home fast.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100F*giggle*, really.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2F4A")

    label("loc_2F0A")


    ChrTalk(
        0x102,
        (
            "#00100FRight, I'd like for Randy too\x01",
            "to come home quickly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F4A")

    OP_5A()
    SetChrPos(0x0, 14040, 0, 63300, 180)
    SetScenarioFlags(0x13B, 4)
    EventEnd(0x5)
    Return()

    # Function_14_2C50 end

    def Function_15_2F62(): pass

    label("Function_15_2F62")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    ClearMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x8, 0x2)
    OP_68(157620, 1330, 125080, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2FBC")
    SetChrFlags(0x0, 0x8)

    label("loc_2FBC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2FCF")
    SetChrFlags(0x1, 0x8)

    label("loc_2FCF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2FE2")
    SetChrFlags(0x2, 0x8)

    label("loc_2FE2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2FF5")
    SetChrFlags(0x3, 0x8)

    label("loc_2FF5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3008")
    SetChrFlags(0x4, 0x8)

    label("loc_3008")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_301B")
    SetChrFlags(0x5, 0x8)

    label("loc_301B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_3034")
    ClearChrFlags(0x102, 0x80)
    ClearChrBattleFlags(0x102, 0x8000)

    label("loc_3034")

    ClearChrFlags(0x102, 0x8)
    SetChrPos(0x102, 157620, 30, 125080, 90)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x102,
        "#0100FI wonder if here it's fine.\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Sound(814, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A new furniture was\x01",
            "added to Elie's room.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber(0x34A, 1)
    SetScenarioFlags(0x13C, 6)
    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_66(0x2, 0x1)
    Call(0, 23)
    Call(0, 39)
    Call(0, 44)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_30EC")
    ClearChrFlags(0x0, 0x8)

    label("loc_30EC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_30FF")
    ClearChrFlags(0x1, 0x8)

    label("loc_30FF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3112")
    ClearChrFlags(0x2, 0x8)

    label("loc_3112")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3125")
    ClearChrFlags(0x3, 0x8)

    label("loc_3125")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3138")
    ClearChrFlags(0x4, 0x8)

    label("loc_3138")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_314B")
    ClearChrFlags(0x5, 0x8)

    label("loc_314B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_3164")
    SetChrFlags(0x102, 0x80)
    SetChrBattleFlags(0x102, 0x8000)

    label("loc_3164")

    SetChrPos(0x0, 155990, 30, 120980, 0)
    EventEnd(0x5)
    Return()

    # Function_15_2F62 end

    def Function_16_3178(): pass

    label("Function_16_3178")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    ClearMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0x9, 0x2)
    SetMapObjFlags(0x13, 0x4)
    ClearMapObjFlags(0x14, 0x4)
    SetMapObjFlags(0x14, 0x2)
    OP_68(154920, 1330, 122580, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_31E4")
    SetChrFlags(0x0, 0x8)

    label("loc_31E4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_31F7")
    SetChrFlags(0x1, 0x8)

    label("loc_31F7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_320A")
    SetChrFlags(0x2, 0x8)

    label("loc_320A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_321D")
    SetChrFlags(0x3, 0x8)

    label("loc_321D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3230")
    SetChrFlags(0x4, 0x8)

    label("loc_3230")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3243")
    SetChrFlags(0x5, 0x8)

    label("loc_3243")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_325C")
    ClearChrFlags(0x102, 0x80)
    ClearChrBattleFlags(0x102, 0x8000)

    label("loc_325C")

    ClearChrFlags(0x102, 0x8)
    SetChrPos(0x102, 154920, 30, 122580, 0)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x102,
        "#0100FI wonder if here it's fine.\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Sound(814, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A new furniture was\x01",
            "added to Elie's room.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber(0x34B, 1)
    SetScenarioFlags(0x13C, 7)
    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_66(0x3, 0x1)
    Call(0, 23)
    Call(0, 39)
    Call(0, 44)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3314")
    ClearChrFlags(0x0, 0x8)

    label("loc_3314")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3327")
    ClearChrFlags(0x1, 0x8)

    label("loc_3327")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_333A")
    ClearChrFlags(0x2, 0x8)

    label("loc_333A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_334D")
    ClearChrFlags(0x3, 0x8)

    label("loc_334D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3360")
    ClearChrFlags(0x4, 0x8)

    label("loc_3360")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3373")
    ClearChrFlags(0x5, 0x8)

    label("loc_3373")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_338C")
    SetChrFlags(0x102, 0x80)
    SetChrBattleFlags(0x102, 0x8000)

    label("loc_338C")

    SetChrPos(0x0, 155990, 30, 120980, 0)
    EventEnd(0x5)
    Return()

    # Function_16_3178 end

    def Function_17_33A0(): pass

    label("Function_17_33A0")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    ClearMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xA, 0x2)
    OP_68(206000, 1300, 129509, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_33FA")
    SetChrFlags(0x0, 0x8)

    label("loc_33FA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_340D")
    SetChrFlags(0x1, 0x8)

    label("loc_340D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3420")
    SetChrFlags(0x2, 0x8)

    label("loc_3420")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3433")
    SetChrFlags(0x3, 0x8)

    label("loc_3433")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3446")
    SetChrFlags(0x4, 0x8)

    label("loc_3446")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3459")
    SetChrFlags(0x5, 0x8)

    label("loc_3459")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_3472")
    ClearChrFlags(0x103, 0x80)
    ClearChrBattleFlags(0x103, 0x8000)

    label("loc_3472")

    ClearChrFlags(0x103, 0x8)
    SetChrPos(0x103, 206000, 0, 129509, 0)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x103,
        "#0200FIt should be fine here.\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Sound(814, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A new furniture was\x01",
            "added to Tio's room.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber(0x34C, 1)
    SetScenarioFlags(0x13D, 0)
    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_66(0x4, 0x1)
    Call(0, 23)
    Call(0, 39)
    Call(0, 46)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3525")
    ClearChrFlags(0x0, 0x8)

    label("loc_3525")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3538")
    ClearChrFlags(0x1, 0x8)

    label("loc_3538")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_354B")
    ClearChrFlags(0x2, 0x8)

    label("loc_354B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_355E")
    ClearChrFlags(0x3, 0x8)

    label("loc_355E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3571")
    ClearChrFlags(0x4, 0x8)

    label("loc_3571")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3584")
    ClearChrFlags(0x5, 0x8)

    label("loc_3584")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_359D")
    SetChrFlags(0x103, 0x80)
    SetChrBattleFlags(0x103, 0x8000)

    label("loc_359D")

    SetChrPos(0x0, 206030, 30, 121140, 0)
    EventEnd(0x5)
    Return()

    # Function_17_33A0 end

    def Function_18_35B1(): pass

    label("Function_18_35B1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    ClearMapObjFlags(0xB, 0x4)
    SetMapObjFlags(0xB, 0x2)
    OP_68(208220, 1300, 123970, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_360B")
    SetChrFlags(0x0, 0x8)

    label("loc_360B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_361E")
    SetChrFlags(0x1, 0x8)

    label("loc_361E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3631")
    SetChrFlags(0x2, 0x8)

    label("loc_3631")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3644")
    SetChrFlags(0x3, 0x8)

    label("loc_3644")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3657")
    SetChrFlags(0x4, 0x8)

    label("loc_3657")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_366A")
    SetChrFlags(0x5, 0x8)

    label("loc_366A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_3683")
    ClearChrFlags(0x103, 0x80)
    ClearChrBattleFlags(0x103, 0x8000)

    label("loc_3683")

    ClearChrFlags(0x103, 0x8)
    SetChrPos(0x103, 208220, 0, 123970, 90)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x103,
        "#0200FIt should be fine here.\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Sound(814, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A new furniture was\x01",
            "added to Tio's room.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber(0x34D, 1)
    SetScenarioFlags(0x13D, 1)
    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_66(0x5, 0x1)
    Call(0, 23)
    Call(0, 39)
    Call(0, 46)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3736")
    ClearChrFlags(0x0, 0x8)

    label("loc_3736")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3749")
    ClearChrFlags(0x1, 0x8)

    label("loc_3749")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_375C")
    ClearChrFlags(0x2, 0x8)

    label("loc_375C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_376F")
    ClearChrFlags(0x3, 0x8)

    label("loc_376F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3782")
    ClearChrFlags(0x4, 0x8)

    label("loc_3782")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3795")
    ClearChrFlags(0x5, 0x8)

    label("loc_3795")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_37AE")
    SetChrFlags(0x103, 0x80)
    SetChrBattleFlags(0x103, 0x8000)

    label("loc_37AE")

    SetChrPos(0x0, 206030, 30, 121140, 0)
    EventEnd(0x5)
    Return()

    # Function_18_35B1 end

    def Function_19_37C2(): pass

    label("Function_19_37C2")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    ClearMapObjFlags(0xC, 0x4)
    SetMapObjFlags(0xC, 0x2)
    OP_68(258329, 1300, 122180, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_381C")
    SetChrFlags(0x0, 0x8)

    label("loc_381C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_382F")
    SetChrFlags(0x1, 0x8)

    label("loc_382F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3842")
    SetChrFlags(0x2, 0x8)

    label("loc_3842")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3855")
    SetChrFlags(0x3, 0x8)

    label("loc_3855")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3868")
    SetChrFlags(0x4, 0x8)

    label("loc_3868")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_387B")
    SetChrFlags(0x5, 0x8)

    label("loc_387B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_3894")
    ClearChrFlags(0x109, 0x80)
    ClearChrBattleFlags(0x109, 0x8000)

    label("loc_3894")

    ClearChrFlags(0x109, 0x8)
    SetChrPos(0x109, 258329, 0, 122180, 90)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x109,
        "#10100FIt looks like here it's fine.\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Sound(814, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A new furniture was\x01",
            "added to Noｱl's room.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber(0x350, 1)
    SetScenarioFlags(0x13D, 2)
    OP_50(0x68, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_66(0x6, 0x1)
    Call(0, 23)
    Call(0, 39)
    Call(0, 49)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_394F")
    ClearChrFlags(0x0, 0x8)

    label("loc_394F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3962")
    ClearChrFlags(0x1, 0x8)

    label("loc_3962")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3975")
    ClearChrFlags(0x2, 0x8)

    label("loc_3975")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3988")
    ClearChrFlags(0x3, 0x8)

    label("loc_3988")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_399B")
    ClearChrFlags(0x4, 0x8)

    label("loc_399B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_39AE")
    ClearChrFlags(0x5, 0x8)

    label("loc_39AE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_39C7")
    SetChrFlags(0x109, 0x80)
    SetChrBattleFlags(0x109, 0x8000)

    label("loc_39C7")

    SetChrPos(0x0, 256010, 0, 121130, 0)
    EventEnd(0x5)
    Return()

    # Function_19_37C2 end

    def Function_20_39DB(): pass

    label("Function_20_39DB")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    ClearMapObjFlags(0xD, 0x4)
    SetMapObjFlags(0xD, 0x2)
    OP_68(258149, 1300, 125700, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3A35")
    SetChrFlags(0x0, 0x8)

    label("loc_3A35")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3A48")
    SetChrFlags(0x1, 0x8)

    label("loc_3A48")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3A5B")
    SetChrFlags(0x2, 0x8)

    label("loc_3A5B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3A6E")
    SetChrFlags(0x3, 0x8)

    label("loc_3A6E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3A81")
    SetChrFlags(0x4, 0x8)

    label("loc_3A81")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3A94")
    SetChrFlags(0x5, 0x8)

    label("loc_3A94")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_3AAD")
    ClearChrFlags(0x109, 0x80)
    ClearChrBattleFlags(0x109, 0x8000)

    label("loc_3AAD")

    ClearChrFlags(0x109, 0x8)
    SetChrPos(0x109, 258149, 0, 125700, 90)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x109,
        "#10100FIt looks like here it's fine.\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Sound(814, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A new furniture was\x01",
            "added to Noｱl's room.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber(0x351, 1)
    SetScenarioFlags(0x13D, 3)
    OP_50(0x68, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_66(0x7, 0x1)
    Call(0, 23)
    Call(0, 39)
    Call(0, 49)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3B68")
    ClearChrFlags(0x0, 0x8)

    label("loc_3B68")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3B7B")
    ClearChrFlags(0x1, 0x8)

    label("loc_3B7B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3B8E")
    ClearChrFlags(0x2, 0x8)

    label("loc_3B8E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3BA1")
    ClearChrFlags(0x3, 0x8)

    label("loc_3BA1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3BB4")
    ClearChrFlags(0x4, 0x8)

    label("loc_3BB4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3BC7")
    ClearChrFlags(0x5, 0x8)

    label("loc_3BC7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_3BE0")
    SetChrFlags(0x109, 0x80)
    SetChrBattleFlags(0x109, 0x8000)

    label("loc_3BE0")

    SetChrPos(0x0, 256010, 0, 121130, 0)
    EventEnd(0x5)
    Return()

    # Function_20_39DB end

    def Function_21_3BF4(): pass

    label("Function_21_3BF4")

    EventBegin(0x0)
    SoundLoad(3668)
    SoundLoad(3669)
    SoundLoad(3670)
    SoundLoad(3671)
    FadeToDark(0, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3C20")
    SetChrFlags(0x0, 0x8)

    label("loc_3C20")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3C33")
    SetChrFlags(0x1, 0x8)

    label("loc_3C33")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3C46")
    SetChrFlags(0x2, 0x8)

    label("loc_3C46")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3C59")
    SetChrFlags(0x3, 0x8)

    label("loc_3C59")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3C6C")
    SetChrFlags(0x4, 0x8)

    label("loc_3C6C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3C7F")
    SetChrFlags(0x5, 0x8)

    label("loc_3C7F")

    SetChrFlags(0x8, 0x80)
    SetChrFlags(0xA, 0x80)
    SetMessageWindowPos(16, 150, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00000F(Now that I think about it...\x01",
            "I have a plushy that seems\x01",
            "it could make KeA happy.)\x02\x03",
            "(Since I'm here, I'll give it \x01",
            "to her as a present.)\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd looked for KeA and gave\x01",
            "her the plushy as a present.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(280, 150, -1, -1)

    AnonymousTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#01100F#3668VWow, are you giving this to KeA!?\x02\x03",
            "#3669VEhehe...\x01",
            "Thank you, Lloyd♪\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_24(0xE55)
    OP_C9(0x1, 0x80000000)
    SetMessageWindowPos(16, 150, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00000FHa ha, you're welcome.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x9, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x354, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3E80")
    SubItemNumber(0x354, 1)
    SetScenarioFlags(0x13D, 5)
    OP_50(0x64, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    ClearMapObjFlags(0xF, 0x4)
    SetMapObjFlags(0xF, 0x2)
    OP_66(0x9, 0x1)
    SetChrPos(0x9, 255500, 0, 68590, 89)
    OP_68(256000, 1300, 68810, 0)
    Call(0, 22)

    label("loc_3E80")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x355, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3ED6")
    SubItemNumber(0x355, 1)
    SetScenarioFlags(0x13D, 4)
    OP_50(0x64, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    ClearMapObjFlags(0xE, 0x4)
    SetMapObjFlags(0xE, 0x2)
    OP_66(0x8, 0x1)
    SetChrPos(0x9, 255940, 30, 66720, 180)
    OP_68(256220, 1330, 66750, 0)
    Call(0, 22)

    label("loc_3ED6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x356, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3F2C")
    SubItemNumber(0x356, 1)
    SetScenarioFlags(0x13D, 6)
    OP_50(0x64, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    ClearMapObjFlags(0x10, 0x4)
    SetMapObjFlags(0x10, 0x2)
    OP_66(0xA, 0x1)
    SetChrPos(0x9, 258089, 0, 67110, 89)
    OP_68(258310, 1300, 67080, 0)
    Call(0, 22)

    label("loc_3F2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x357, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3F82")
    SubItemNumber(0x357, 1)
    SetScenarioFlags(0x13D, 7)
    OP_50(0x64, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    ClearMapObjFlags(0x11, 0x4)
    SetMapObjFlags(0x11, 0x2)
    OP_66(0xB, 0x1)
    SetChrPos(0x9, 255560, 30, 72720, 0)
    OP_68(255320, 1330, 72710, 0)
    Call(0, 22)

    label("loc_3F82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x358, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3FD8")
    SubItemNumber(0x358, 1)
    SetScenarioFlags(0x13E, 0)
    OP_50(0x64, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    ClearMapObjFlags(0x12, 0x4)
    SetMapObjFlags(0x12, 0x2)
    OP_66(0xC, 0x1)
    SetChrPos(0x9, 256500, 30, 63940, 89)
    OP_68(256850, 1330, 63910, 0)
    Call(0, 22)

    label("loc_3FD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13E, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12D, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3FF9")
    Call(0, 51)

    label("loc_3FF9")

    SetMessageWindowPos(14, 280, 60, 3)
    EventEnd(0x6)
    NewScene("c0130", 112, 0, 0)
    IdleLoop()
    Return()

    # Function_21_3BF4 end

    def Function_22_400E(): pass

    label("Function_22_400E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4025")
    Sleep(1000)
    Jump("loc_4028")

    label("loc_4025")

    Sleep(500)

    label("loc_4028")

    FadeToBright(500, 0)
    OP_0D()
    Sleep(500)
    OP_63(0x9, 0x0, 1700, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1000)
    OP_C9(0x0, 0x80000000)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4098")

    ChrTalk(
        0x9,
        "#01100F#3670VYep, I guess here it's fine.\x02",
    )

    Jump("loc_40C4")

    label("loc_4098")


    ChrTalk(
        0x9,
        "#01100F#3671VHmm, should I put it here?\x02",
    )


    label("loc_40C4")

    CloseMessageWindow()
    OP_24(0xE56)
    OP_24(0xE57)
    OP_C9(0x1, 0x80000000)
    Sleep(500)
    Sound(814, 0, 100, 0)
    SetChrName("")
    SetMessageWindowPos(14, 280, 60, 3)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A new furniture was\x01",
            "added to KeA's room.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Call(0, 23)
    Call(0, 39)
    FadeToDark(500, 0, -1)
    OP_0D()
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Return()

    # Function_22_400E end

    def Function_23_4135(): pass

    label("Function_23_4135")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13B, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_41A0")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "When you acquire furniture items,\x01",
            "you can place them in the protagonists' rooms.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetScenarioFlags(0x13B, 7)

    label("loc_41A0")

    Return()

    # Function_23_4135 end

    def Function_24_41A1(): pass

    label("Function_24_41A1")

    OP_F4(0x3)
    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Rest Here\x01",      # 0
            "Quit\x01",           # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4221")
    SoundLoad(13)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    Sound(13, 0, 100, 0)
    OP_0D()
    OP_32(0xFF, 0xFE, 0x0)
    OP_6A(0x0, 0x0)
    OP_31(0x1)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_4221")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_423D")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_423D")

    Return()

    # Function_24_41A1 end

    def Function_25_423F(): pass

    label("Function_25_423F")

    OP_F4(0x3)
    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Rest Here\x01",      # 0
            "Quit\x01",           # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_42BF")
    SoundLoad(13)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    Sound(13, 0, 100, 0)
    OP_0D()
    OP_32(0xFF, 0xFE, 0x0)
    OP_6A(0x0, 0x0)
    OP_31(0x1)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_42BF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_42DB")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_42DB")

    Return()

    # Function_25_423F end

    def Function_26_42DD(): pass

    label("Function_26_42DD")

    OP_F4(0x3)
    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Rest Here\x01",      # 0
            "Quit\x01",           # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_435D")
    SoundLoad(13)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    Sound(13, 0, 100, 0)
    OP_0D()
    OP_32(0xFF, 0xFE, 0x0)
    OP_6A(0x0, 0x0)
    OP_31(0x1)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_435D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4379")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_4379")

    Return()

    # Function_26_42DD end

    def Function_27_437B(): pass

    label("Function_27_437B")

    TalkBegin(0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis362.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It is a stylish mirror.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_49()
    OP_CC(0x1, 0xFF, 0x0)
    TalkEnd(0xFF)
    Return()

    # Function_27_437B end

    def Function_28_4433(): pass

    label("Function_28_4433")

    TalkBegin(0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis363.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It is a music box.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopBGM(0x1F4)
    WaitBGM()
    Sleep(10)
    Sound(949, 0, 100, 0)
    Sleep(900)
    Sound(949, 0, 100, 0)
    Sleep(900)
    Sound(949, 0, 100, 0)
    Sleep(900)
    BeginChrThread(0xB, 1, 0, 29)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_49()
    OP_CC(0x1, 0xFF, 0x0)
    TalkEnd(0xFF)
    Return()

    # Function_28_4433 end

    def Function_29_4510(): pass

    label("Function_29_4510")

    PlayBGM("ed7591", 0)
    Sleep(19000)
    OP_1F()
    Return()

    # Function_29_4510 end

    def Function_30_4519(): pass

    label("Function_30_4519")

    TalkBegin(0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis364.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It is a Kagemaru bank.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_49()
    OP_CC(0x1, 0xFF, 0x0)
    TalkEnd(0xFF)
    Return()

    # Function_30_4519 end

    def Function_31_45D0(): pass

    label("Function_31_45D0")

    TalkBegin(0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis365.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It is a Miichie plushy.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_49()
    OP_CC(0x1, 0xFF, 0x0)
    TalkEnd(0xFF)
    Return()

    # Function_31_45D0 end

    def Function_32_4688(): pass

    label("Function_32_4688")

    TalkBegin(0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis370.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It is a racing flag.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_49()
    OP_CC(0x1, 0xFF, 0x0)
    TalkEnd(0xFF)
    Return()

    # Function_32_4688 end

    def Function_33_473D(): pass

    label("Function_33_473D")

    TalkBegin(0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis371.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It is a minivelo.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_49()
    OP_CC(0x1, 0xFF, 0x0)
    TalkEnd(0xFF)
    Return()

    # Function_33_473D end

    def Function_34_47EF(): pass

    label("Function_34_47EF")

    TalkBegin(0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis373.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It is a Pom cushion.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_49()
    OP_CC(0x1, 0xFF, 0x0)
    TalkEnd(0xFF)
    Return()

    # Function_34_47EF end

    def Function_35_48A4(): pass

    label("Function_35_48A4")

    TalkBegin(0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis372.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It is a strange cushion.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_49()
    OP_CC(0x1, 0xFF, 0x0)
    TalkEnd(0xFF)
    Return()

    # Function_35_48A4 end

    def Function_36_495D(): pass

    label("Function_36_495D")

    TalkBegin(0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis374.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It is a black teddy.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_49()
    OP_CC(0x1, 0xFF, 0x0)
    TalkEnd(0xFF)
    Return()

    # Function_36_495D end

    def Function_37_4A12(): pass

    label("Function_37_4A12")

    TalkBegin(0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis375.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It is an Acerbic Tomartian.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_49()
    OP_CC(0x1, 0xFF, 0x0)
    TalkEnd(0xFF)
    Return()

    # Function_37_4A12 end

    def Function_38_4ACE(): pass

    label("Function_38_4ACE")

    TalkBegin(0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis376.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It is a ZWEI 2 penguin.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_49()
    OP_CC(0x1, 0xFF, 0x0)
    TalkEnd(0xFF)
    Return()

    # Function_38_4ACE end

    def Function_39_4B86(): pass

    label("Function_39_4B86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13E, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4BFA")
    OP_E0(0x16, 0x0)

    label("loc_4BFA")

    Return()

    # Function_39_4B86 end

    def Function_40_4BFB(): pass

    label("Function_40_4BFB")

    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Return()

    # Function_40_4BFB end

    def Function_41_4C2A(): pass

    label("Function_41_4C2A")

    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Return()

    # Function_41_4C2A end

    def Function_42_4C59(): pass

    label("Function_42_4C59")

    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    Return()

    # Function_42_4C59 end

    def Function_43_4C88(): pass

    label("Function_43_4C88")

    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    Return()

    # Function_43_4C88 end

    def Function_44_4CB7(): pass

    label("Function_44_4CB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12C, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_59EC")
    FadeToDark(1000, 0, -1)
    OP_0D()
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis362.itp")
    CreatePortrait(1, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis363.itp")
    LoadChrToIndex("chr/ch00102.itc", 0x1E)
    SetChrChipByIndex(0x102, 0x1E)
    SetChrSubChip(0x102, 0x0)
    SetChrFlags(0x102, 0x4)
    SetChrPos(0x102, 155910, 200, 123440, 290)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_4D69")
    ClearChrFlags(0x101, 0x80)
    ClearChrBattleFlags(0x101, 0x8000)

    label("loc_4D69")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_4D82")
    ClearChrFlags(0x102, 0x80)
    ClearChrBattleFlags(0x102, 0x8000)

    label("loc_4D82")

    StopBGM(0xBB8)
    SetChrName("")
    SetMessageWindowPos(14, 280, 60, 3)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "That day, Lloyd and the others returned to the\x01",
            "Support Section on a break from their duties──\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "They made their scheduled report to HQ\x01",
            "and decided to each take their rest.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(154920, 1880, 123500, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(22500, 0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7102", 0)
    FadeToBright(1000, 0)
    OP_68(154920, 1330, 123500, 2000)
    OP_6F(0x79)
    OP_0D()
    Sleep(1000)

    ChrTalk(
        0x102,
        "#00104F............\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Sound(808, 0, 100, 0)
    Sleep(500)
    SetChrPos(0x101, 155790, 0, 118500, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x101, 0x8)

    NpcTalk(
        0x101,
        "Lloyd's Voice",
        "#1PElie, can I?\x02",
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x102, 0x1)
    Sleep(500)

    ChrTalk(
        0x102,
        (
            "#00100FLloyd?\x01",
            "Yes, come in.\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    Sound(812, 0, 100, 0)
    SetChrFlags(0x102, 0x40)
    SetChrPos(0x102, 155440, 30, 122630, 180)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    ClearChrFlags(0x102, 0x4)
    OP_68(155280, 1330, 121810, 2000)
    SetCameraDistance(21220, 2000)
    Sleep(500)
    OP_9B(0x0, 0x102, 0x0, 0x1F4, 0x3E8, 0x0)

    def lambda_4FA8():

        label("loc_4FA8")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_4FA8")

    QueueWorkItem2(0x102, 2, lambda_4FA8)
    OP_0D()
    Sound(103, 0, 100, 0)
    Sleep(500)

    def lambda_4FC4():
        OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4FC4)

    def lambda_4FD9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4FD9)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x101, 2)
    TurnDirection(0x101, 0x102, 500)
    EndChrThread(0x102, 0x2)
    OP_6F(0x79)
    Sleep(200)

    ChrTalk(
        0x102,
        "#00100FIs it time to go?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FWell, there haven't been any special\x01",
            "requests from HQ today...\x02\x03",
            "#00000FEveryone hasn't gathered yet,\x01",
            "so there's no such a hurry.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x101, 0x14A, 0x1F4)
    Sleep(750)
    OP_93(0x101, 0x1E, 0x1F4)
    Sleep(750)

    ChrTalk(
        0x101,
        (
            "#00005FAh...\x01",
            "You have added some things, hm?\x02",
        )
    )

    CloseMessageWindow()
    OP_68(157760, 1330, 124430, 3000)
    SetCameraDistance(22230, 3000)
    OP_93(0x101, 0x2D, 0x1F4)
    OP_93(0x102, 0x2D, 0x1F4)
    OP_6F(0x79)
    Sleep(500)
    Call(0, 40)
    Sleep(1000)
    SetMessageWindowPos(16, 150, -1, -1)

    AnonymousTalk(
        0x102,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00102F*giggle*, living like this, I did\x01",
            "it unintentionally, you know.\x02\x03",
            "#00104FWhen I occasionally went back\x01",
            "to my home I took there the books\x01",
            "and small things I don't need, but...\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetMessageWindowPos(280, 150, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00009FWell, compared to my room\x01",
            "it's cleanly tidied up.\x02\x03",
            "#00000FAlthough the things have increased,\x01",
            "they're just items that suit the room...\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Call(0, 41)
    OP_68(155770, 1330, 122300, 2000)
    SetCameraDistance(23220, 2000)
    OP_6F(0x79)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_52D5():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_52D5)
    Sleep(200)

    def lambda_52E5():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_52E5)
    Sleep(500)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)

    ChrTalk(
        0x101,
        (
            "#00005FBy the way...\x01",
            "Could that be a music box?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100F*giggle*, it is.\x02",
    )

    CloseMessageWindow()
    OP_68(155140, 1330, 123720, 2000)
    SetCameraDistance(22230, 2000)
    OP_6F(0x79)
    Sleep(500)
    Call(0, 42)
    Sleep(1000)
    SetMessageWindowPos(16, 150, -1, -1)

    AnonymousTalk(
        0x102,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00104FIt's an antique music box from\x01",
            "the Rieveldt Corp. that was\x01",
            "at Mrs. Imelda's shop...\x02\x03",
            "#00100FSince it was a nostalgic music, I\x01",
            "ended up buying it without thinking.\x02\x03",
            "#00109F...Do you want to listen to it for a bit?\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(280, 150, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00000FYeah, I'm curious.\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 43)
    Sleep(750)
    StopBGM(0x1388)
    MoveCamera(45, 22, 0, 4000)
    SetCameraDistance(20000, 4000)
    OP_95(0x102, 155440, 30, 122630, 1000, 0x0)
    Sleep(1000)
    Fade(500)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0x102, 0x1E)
    SetChrSubChip(0x102, 0x0)
    SetChrFlags(0x102, 0x4)
    SetChrPos(0x102, 155910, 200, 123440, 290)
    OP_0D()
    Sleep(250)
    OP_95(0x101, 154430, 30, 122450, 2000, 0x0)
    OP_93(0x101, 0x2D, 0x1F4)
    OP_6F(0x79)
    Sound(949, 0, 100, 0)
    Sleep(900)
    Sound(949, 0, 100, 0)
    Sleep(900)
    Sound(949, 0, 100, 0)
    Sleep(900)
    Sound(853, 0, 50, 0)
    OP_74(0x9, 0x1E)
    OP_71(0x9, 0x0, 0xF, 0x0, 0x8)
    Sleep(1500)
    SetCameraDistance(18000, 19000)
    OP_71(0x9, 0xF, 0x5F, 0x0, 0x20)
    BeginChrThread(0xB, 1, 0, 45)
    WaitChrThread(0xB, 1)
    OP_74(0x9, 0x0)
    Sleep(1000)
    PlayBGM("ed7102", 0)

    ChrTalk(
        0x101,
        (
            "#00009F#1P*haah*...\x01",
            "A timbre like it's sighing.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x1)
    Sleep(200)

    ChrTalk(
        0x102,
        (
            "#00109F*giggle*, right?\x02\x03",
            "#00104FSpeaking of the Empire Rieveldt Corp., it's\x01",
            "a famous music instrument manufacturer\x01",
            "and the music boxes are very popular too.\x02\x03",
            "#00100FBack in the day I even had one\x01",
            "with a much smaller number of\x01",
            "valves with the same tune as this...\x02\x03",
            "#00106FWhen I went to study abroad I took\x01",
            "it with me and I ended up losing it.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(
        0x101,
        (
            "#00005F#1PReally...?\x02\x03",
            "#00006F(Could it be a memento\x01",
            "of her parents, I wonder...?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FBecause it went already out of\x01",
            "production I had resigned myself...\x02\x03",
            "#00100FI was really glad one was stocked\x01",
            "up at Mrs. Imelda's shop.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#1PI see...\x02\x03",
            "#00002FHa ha, now and then\x01",
            "even her shop is useful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00109F*giggle*, right.\x02",
    )

    CloseMessageWindow()
    Fade(500)
    Sound(812, 0, 100, 0)
    SetChrFlags(0x102, 0x40)
    SetChrPos(0x102, 155640, 30, 122530, 180)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    ClearChrFlags(0x102, 0x4)
    OP_68(154430, 1330, 122240, 1500)
    MoveCamera(45, 25, 0, 1500)
    OP_6E(350, 1500)
    SetCameraDistance(19750, 1500)
    OP_0D()

    def lambda_58B8():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_58B8)
    Sleep(200)

    def lambda_58C8():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_58C8)
    OP_6F(0x79)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    Sleep(500)

    ChrTalk(
        0x102,
        (
            "#00100FWell then.\x01",
            "Should we go, Lloyd?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F...Yeah!\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(20750, 1500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(9, 0, 100, 0)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "You got all of Elie's furniture!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    StopBGM(0xBB8)
    WaitBGM()
    Sleep(10)
    OP_1F()
    SetChrChipByIndex(0x102, 0xFF)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x0, 0x40)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_59AD")
    SetChrFlags(0x101, 0x80)
    SetChrBattleFlags(0x101, 0x8000)

    label("loc_59AD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_59C6")
    SetChrFlags(0x102, 0x80)
    SetChrBattleFlags(0x102, 0x8000)

    label("loc_59C6")

    OP_49()
    OP_D7(0x1E)
    OP_CC(0x1, 0xFF, 0x0)
    OP_74(0x9, 0x1E)
    OP_70(0x9, 0x0)
    SetScenarioFlags(0x12C, 6)
    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    EventEnd(0x6)
    NewScene("c0130", 108, 0, 0)
    IdleLoop()

    label("loc_59EC")

    Return()

    # Function_44_4CB7 end

    def Function_45_59ED(): pass

    label("Function_45_59ED")

    PlayBGM("ed7591", 1)
    Sleep(19000)
    Return()

    # Function_45_59ED end

    def Function_46_59F5(): pass

    label("Function_46_59F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6D1D")
    FadeToDark(1000, 0, -1)
    OP_0D()
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis365.itp")
    CreatePortrait(1, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis364.itp")
    LoadChrToIndex("apl/ch50218.itc", 0x1E)
    LoadChrToIndex("chr/ch00202.itc", 0x1F)
    SoundLoad(938)
    SoundLoad(939)
    SetChrChipByIndex(0x103, 0x1E)
    SetChrSubChip(0x103, 0x0)
    SetChrFlags(0x103, 0x4)
    SetChrPos(0x103, 205890, 80, 126750, 180)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x103, 3, 0, 47)
    ClearMapObjFlags(0x15, 0x4)
    OP_70(0x15, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_5ACD")
    ClearChrFlags(0x101, 0x80)
    ClearChrBattleFlags(0x101, 0x8000)

    label("loc_5ACD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_5AE6")
    ClearChrFlags(0x103, 0x80)
    ClearChrBattleFlags(0x103, 0x8000)

    label("loc_5AE6")

    StopBGM(0xBB8)
    SetChrName("")
    SetMessageWindowPos(14, 280, 60, 3)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "That day, Lloyd and the others returned to the\x01",
            "Support Section on a break from their duties──\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "They made their scheduled report to HQ\x01",
            "and decided to each take their rest.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(205970, 1830, 125860, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(22510, 0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7102", 0)
    Sound(938, 2, 50, 0)
    FadeToBright(1000, 0)
    OP_68(205970, 1330, 125860, 2000)
    OP_6F(0x79)
    OP_0D()
    Sleep(1000)
    Sound(808, 0, 100, 0)
    Sleep(500)
    SetChrPos(0x101, 205780, 0, 119210, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x101, 0x8)

    NpcTalk(
        0x101,
        "Lloyd's Voice",
        "#1PTio, do you have a moment?\x02",
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(700)
    StopSound(938, 300, 40)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)

    ChrTalk(
        0x103,
        (
            "#00200FYes.\x01",
            "Please come in, Mr. Lloyd.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(205300, 1330, 124060, 1500)
    OP_6F(0x79)
    Sound(103, 0, 100, 0)
    Sleep(500)
    OP_68(205440, 1330, 124910, 2000)

    def lambda_5CF0():
        OP_9B(0x0, 0xFE, 0x0, 0x125C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5CF0)

    def lambda_5D05():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5D05)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x101, 2)
    TurnDirection(0x101, 0x103, 500)
    OP_6F(0x79)
    Sleep(500)

    ChrTalk(
        0x103,
        "#00200FIs it time to go out?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FWell, there haven't been any special\x01",
            "requests from HQ today...\x02\x03",
            "#00000FEveryone hasn't gathered yet,\x01",
            "so there's no such a hurry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00204FNo, I can go immediately.\x02",
    )

    CloseMessageWindow()
    Sound(938, 2, 50, 0)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    Sleep(1000)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x101, 0x50, 0x1F4)
    Sleep(750)
    OP_93(0x101, 0x0, 0x1F4)
    Sleep(750)

    ChrTalk(
        0x101,
        (
            "#00005FAh...\x01",
            "You have added some things, hm?\x02",
        )
    )

    CloseMessageWindow()
    OP_68(209790, 1330, 124450, 2500)
    MoveCamera(60, 25, 0, 2500)
    OP_6E(350, 2500)
    SetCameraDistance(20000, 2500)
    OP_6F(0x79)
    Sleep(1000)
    OP_68(205740, 1330, 129949, 5000)
    MoveCamera(30, 25, 0, 5000)
    OP_6F(0x79)
    Sleep(2000)
    BeginChrThread(0xB, 1, 0, 48)
    Fade(500)
    OP_68(205720, 1330, 125260, 0)
    OP_6E(350, 0)
    SetCameraDistance(22510, 0)
    MoveCamera(45, 22, 0, 0)
    OP_0D()
    Sleep(1000)
    StopSound(938, 300, 40)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitChrThread(0x103, 3)
    Sleep(800)
    SetChrChipByIndex(0x103, 0x1F)
    SetChrSubChip(0x103, 0x0)
    Sleep(200)
    Sound(71, 0, 60, 0)
    OP_74(0x15, 0x1E)
    OP_71(0x15, 0x1, 0xA, 0x0, 0x8)
    OP_79(0x15)
    Sleep(500)
    Fade(500)
    SetChrFlags(0x103, 0x40)
    SetChrPos(0x103, 205890, 0, 126850, 180)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    ClearChrFlags(0x103, 0x4)
    OP_0D()
    Sleep(1000)

    ChrTalk(
        0x103,
        (
            "#00204F...I was able to get some\x01",
            "pretty nice things.\x02\x03",
            "#00202FRegarding character goods too,\x01",
            "Crossbell, compared to the nearby\x01",
            "countries, has quite the advantage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHa ha, after all it's Michey's\x01",
            "home territory, hm?\x02\x03",
            "#00004FThanks to Michelam Theme Park it seems\x01",
            "he's also expanding to the nearby countries...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(209440, 1330, 124760, 2500)
    MoveCamera(60, 25, 0, 2500)
    OP_6E(350, 2500)
    SetCameraDistance(20500, 2500)

    def lambda_60F2():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_60F2)
    Sleep(200)

    def lambda_6102():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6102)
    OP_6F(0x79)
    Sleep(500)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x103, 1)
    Call(0, 40)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x86, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6348")
    SetMessageWindowPos(280, 150, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00005FBy the way...\x02\x03",
            "#00000FThat pink-colored Michey over there...\x01",
            "Her name was "Miichie" I guess.\x02\x03",
            "#00004FI think it's Michey's little sister, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetMessageWindowPos(16, 150, -1, -1)

    AnonymousTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00202FYes, although she says her big brother is a bit\x01",
            "pathetic, she meddles in his business. It is an\x01",
            "extremely high spec little sister character.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetMessageWindowPos(280, 150, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00012FI-Is that so...\x01",
            "(What's a "high spec little sister"?)\x02\x03",
            "#00005FHmm, then, what about\x01",
            "that blackish cat there?\x02\x03",
            "#00000FIt also decorates a cushion...\x01",
            "Is it related to Michey?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_656A")

    label("loc_6348")

    SetMessageWindowPos(280, 150, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00005FBy the way...\x02\x03",
            "#00000FThat pink-colored Michey,\x01",
            "what kind of version is it?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_63(0x103, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    SetMessageWindowPos(16, 150, -1, -1)

    AnonymousTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00206F...Mr. Lloyd, you lack study too much.\x02\x03",
            "#00200FThat isn't Michey, it is\x01",
            "his little sister, "Miichie".\x02\x03",
            "#00211FBeing a Crossbell detective,\x01",
            "you must know at least that.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetMessageWindowPos(280, 150, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00006FI-I'm ashamed... (Although I think it's got \x01",
            "nothing to do with being a detective.)\x02\x03",
            "#00005FHmm, then, what about\x01",
            "that blackish cat there?\x02\x03",
            "#00000FIt also decorates a cushion...\x01",
            "Is it related to Michey?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_656A")

    Call(0, 41)

    def lambda_6572():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6572)
    Sleep(200)

    def lambda_6582():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6582)
    OP_68(205550, 1330, 128690, 3000)
    MoveCamera(34, 25, 0, 3000)
    OP_6F(0x79)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x103, 1)
    Sleep(500)
    Call(0, 42)
    Sleep(1000)
    SetMessageWindowPos(16, 150, -1, -1)

    AnonymousTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00202FThat is "Kagemaru".\x02\x03",
            "#00204FIt is the cat the protagonist of a recent\x01",
            "popular series of novels keeps...\x02\x03",
            "#00200FIt is a character who keeps making a\x01",
            "break through with his brazen cuteness\x01",
            "and his characteristic "bunyuu" cry.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetMessageWindowPos(280, 150, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00005FEeh, I see.\x02\x03",
            "#00003FNow that I think about it, it seems\x01",
            "he's also among the casino prizes.\x02\x03",
            "#00009FStill, Michey and this guy too...\x01",
            "I wouldn't honestly say they're cute──\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetMessageWindowPos(16, 150, -1, -1)

    AnonymousTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00211F*glare*.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetMessageWindowPos(280, 150, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00006FNo, it's nothing.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetMessageWindowPos(16, 150, -1, -1)

    AnonymousTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00206F...Well, I know what you want to say.\x02\x03",
            "#00200FMichey is a "humorous character"\x01",
            "whose selling point is a unique\x01",
            "crankiness beyond description...\x02\x03",
            "#00203FWhile Kagemaru is a standard\x01",
            "mascot with a lack of grace, that,\x01",
            "conversely, turns into a superb hook.\x02\x03",
            "#00200FAlthough it is hard to frankly say they are\x01",
            "cute, it is obvious that is a fact.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetMessageWindowPos(280, 150, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00005FI see... Somehow it's like they \x01",
            "have a persuasive power.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Call(0, 43)
    Sleep(250)
    OP_68(205720, 1330, 125260, 2500)
    OP_6E(350, 2500)
    SetCameraDistance(22510, 2500)
    MoveCamera(45, 22, 0, 2500)
    TurnDirection(0x103, 0x101, 500)
    OP_6F(0x79)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00000FBy the way, Tio, between\x01",
            "Michey and Kagemaru, which\x01",
            "one do you like the most?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x103,
        (
            "#00203F............\x02\x03",
            "#00211F...You asked about it, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00011FHuh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203FAbout the problem I was averting my eyes from,\x01",
            "not wanting to give an answer to it...\x02\x03",
            "#00201FYou really asked about it, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012FHuh, uhm, Miss Tio...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203FLet's talk at leisure about\x01",
            "this matter after dinner.\x02\x03",
            "#00204F...Mr. Lloyd. It seems it is\x01",
            "going to be heated tonight...!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00006F(...I have a book I wanted to read, but it\x01",
            "seems I have to resign myself for today.)\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(23510, 1500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(9, 0, 100, 0)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "You got all of Tio's furniture!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    StopBGM(0xBB8)
    WaitBGM()
    Sleep(10)
    OP_1F()
    SetChrChipByIndex(0x103, 0xFF)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x103, 0x4)
    ClearChrFlags(0x0, 0x40)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_6CD8")
    SetChrFlags(0x101, 0x80)
    SetChrBattleFlags(0x101, 0x8000)

    label("loc_6CD8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_6CF1")
    SetChrFlags(0x103, 0x80)
    SetChrBattleFlags(0x103, 0x8000)

    label("loc_6CF1")

    OP_49()
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_CC(0x1, 0xFF, 0x0)
    SetMapObjFlags(0x15, 0x4)
    SetScenarioFlags(0x12C, 7)
    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_24(0x3AA)
    OP_24(0x3AB)
    EventEnd(0x6)
    NewScene("c0130", 110, 0, 0)
    IdleLoop()

    label("loc_6D1D")

    Return()

    # Function_46_59F5 end

    def Function_47_6D1E(): pass

    label("Function_47_6D1E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6D77")
    SetChrSubChip(0x103, 0x0)
    Sleep(100)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6D49")
    Jump("Function_47_6D1E")

    label("loc_6D49")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6D5D")
    Jump("loc_6D77")

    label("loc_6D5D")

    SetChrSubChip(0x103, 0x1)
    Sleep(100)
    SetChrSubChip(0x103, 0x2)
    Sleep(100)
    SetChrSubChip(0x103, 0x1)
    Sleep(100)
    Jump("Function_47_6D1E")

    label("loc_6D77")

    Return()

    # Function_47_6D1E end

    def Function_48_6D78(): pass

    label("Function_48_6D78")

    Sound(804, 0, 100, 0)
    Sleep(500)
    Sound(939, 2, 70, 0)
    Sleep(1000)
    Sound(73, 0, 100, 0)
    OP_24(0x3AB)
    Return()

    # Function_48_6D78 end

    def Function_49_6D94(): pass

    label("Function_49_6D94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12D, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_79D0")
    FadeToDark(1000, 0, -1)
    OP_0D()
    LoadChrToIndex("chr/ch02902.itc", 0x1E)
    SetChrChipByIndex(0x109, 0x1E)
    SetChrSubChip(0x109, 0x0)
    SetChrFlags(0x109, 0x4)
    SetChrPos(0x109, 254080, 150, 127100, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_6DEE")
    ClearChrFlags(0x101, 0x80)
    ClearChrBattleFlags(0x101, 0x8000)

    label("loc_6DEE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_6E07")
    ClearChrFlags(0x109, 0x80)
    ClearChrBattleFlags(0x109, 0x8000)

    label("loc_6E07")

    StopBGM(0xBB8)
    SetChrName("")
    SetMessageWindowPos(14, 280, 60, 3)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "That day, Lloyd and the others returned to the\x01",
            "Support Section on a break from their duties──\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "They made their scheduled report to HQ\x01",
            "and decided to each take their rest.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(254580, 1800, 125790, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(22500, 0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7102", 0)
    FadeToBright(1000, 0)
    OP_68(254580, 1300, 125790, 2000)
    OP_6F(0x79)
    OP_0D()
    Sleep(1000)

    ChrTalk(
        0x109,
        (
            "#10100FUhhm...\x01",
            "Yes, I guess this does it?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Sound(808, 0, 100, 0)
    Sleep(500)
    SetChrPos(0x101, 255880, 0, 119170, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x101, 0x8)

    NpcTalk(
        0x101,
        "Lloyd's Voice",
        "#1PNoｱl, do you have a minute?\x02",
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x109, 0x1)
    Sleep(500)

    ChrTalk(
        0x109,
        (
            "#10100FMr. Lloyd?\x01",
            "Yes, it's alright!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    Sound(812, 0, 100, 0)
    SetChrFlags(0x109, 0x40)
    SetChrPos(0x109, 254580, 0, 126410, 180)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    ClearChrFlags(0x109, 0x4)
    OP_0D()
    OP_68(255330, 1300, 123600, 2500)
    SetCameraDistance(21000, 2500)
    BeginChrThread(0x109, 1, 0, 50)
    Sleep(500)
    Sound(103, 0, 100, 0)
    Sleep(500)

    def lambda_705D():
        OP_9B(0x0, 0xFE, 0x0, 0x1068, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_705D)

    def lambda_7072():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7072)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x109, 1)
    OP_6F(0x79)
    Sleep(200)

    ChrTalk(
        0x109,
        "#10100FIs it time to go out?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FWell, there haven't been any special\x01",
            "requests from HQ today...\x02\x03",
            "#00000FEveryone hasn't gathered yet,\x01",
            "so there's no such a hurry.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x101, 0x14A, 0x1F4)
    Sleep(200)
    OP_68(254560, 1300, 125250, 1500)
    SetCameraDistance(20000, 1500)
    OP_93(0x109, 0x14A, 0x1F4)
    OP_6F(0x79)
    Sleep(500)

    ChrTalk(
        0x101,
        "#00005FOh, were you writing a report?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10109FAhaha...\x01",
            "Well, it's because I'm on loan here.\x02\x03",
            "#10100FI'm filing one report a week\x01",
            "to Commander Sonya.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00009FI see, thank you for your hard work.\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Sleep(200)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(255830, 1300, 124180, 3000)
    MoveCamera(59, 14, 0, 3000)
    OP_6E(450, 3000)
    SetCameraDistance(16500, 3000)
    OP_93(0x101, 0x2D, 0x1F4)
    Sleep(200)
    OP_93(0x109, 0x5A, 0x1F4)
    Sleep(500)
    OP_93(0x101, 0x5A, 0x1F4)
    Sleep(750)
    OP_6F(0x79)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#00005F#4PEeh...!\x01",
            "The interesting things have increased in here, eh?\x02\x03",
            "#00000FA bicycle and...\x01",
            "Is that a race flag?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x109, 0x101, 500)

    ChrTalk(
        0x109,
        "#10102FOh...you can tell!?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x109, 500)

    ChrTalk(
        0x101,
        (
            "#00000F#4PYeah, after all I lived for two\x01",
            "years in the Republic too.\x02\x03",
            "#00004FThere I often saw more\x01",
            "bicycles than here.\x02\x03",
            "#00000FSometimes they even held exhibitions\x01",
            "of races where orbal cars are used, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10109FYes, yes, that's right!\x02\x03",
            "#10104F...Actually, my late\x01",
            "dad liked those.\x02\x03",
            "#10100FWhen I was little he took\x01",
            "me on a railroad trip to\x01",
            "see a race.\x02\x03",
            "#10102FSince he was busy with CGF\x01",
            "work it only happened once...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#4PI see...\x02\x03",
            "#00000FThen, your fondness for orbal\x01",
            "vehicles comes from there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10109FAhaha...what acumen.\x02\x03",
            "#10100FWhen I receive days off,\x01",
            "I'd absolutely like to go\x01",
            "see an orbal race again...\x02\x03",
            "#10106FI haven't so much free time, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009F#4PHa ha, same here.\x02\x03",
            "#00004F(Although in case of Noｱl seems she wouldn't\x01",
            "just see it but taking part to the race...)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xFFFF)

    ChrTalk(
        0x101,
        (
            "#00003F#4PSetting aside the races...\x02\x03",
            "#00002FAbout bicycles, if you\x01",
            "have a model you suggest,\x01",
            "could you tell me next time?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x109,
        "#10105FHuh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009F#4PWell, when I was there I\x01",
            "had a friend who rode it\x01",
            "and I was a bit interested.\x02\x03",
            "#00000FI think we could go around cycling\x01",
            "on our days off, what do you say?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x109,
        (
            "#10100FI-I think it would be nice!\x02\x03",
            "#10104FIt's useful, you exercise with it,\x01",
            "and best of all it's super fun!\x02\x03",
            "#10109FNext time I'll bring you a\x01",
            "catalog I have at home!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00009F#4PHa ha, thank you very much.\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(17100, 1500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(9, 0, 100, 0)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "You got all of Noｱl's furniture!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    StopBGM(0xBB8)
    WaitBGM()
    Sleep(10)
    OP_1F()
    SetChrChipByIndex(0x109, 0xFF)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x109, 0x4)
    ClearChrFlags(0x0, 0x40)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_7999")
    SetChrFlags(0x101, 0x80)
    SetChrBattleFlags(0x101, 0x8000)

    label("loc_7999")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_79B2")
    SetChrFlags(0x109, 0x80)
    SetChrBattleFlags(0x109, 0x8000)

    label("loc_79B2")

    OP_49()
    OP_D7(0x1E)
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x12D, 1)
    OP_50(0x68, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    EventEnd(0x6)
    NewScene("c0130", 115, 0, 0)
    IdleLoop()

    label("loc_79D0")

    Return()

    # Function_49_6D94 end

    def Function_50_79D1(): pass

    label("Function_50_79D1")

    OP_95(0xFE, 255870, 0, 124760, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_50_79D1 end

    def Function_51_79ED(): pass

    label("Function_51_79ED")

    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis342.itp")
    CreatePortrait(1, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis343.itp")
    LoadChrToIndex("apl/ch51542.itc", 0x1E)
    LoadChrToIndex("apl/ch51216.itc", 0x1F)
    SoundLoad(3672)
    SoundLoad(3673)
    SoundLoad(3031)
    SoundLoad(3318)
    SoundLoad(3319)
    SetChrChipByIndex(0x9, 0x1)
    SetChrSubChip(0x9, 0x0)
    SetChrFlags(0x9, 0x4)
    SetChrFlags(0x9, 0x40)
    ClearChrFlags(0x9, 0x1)
    SetChrPos(0x9, 254100, 150, 71270, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_7AA1")
    ClearChrFlags(0x101, 0x80)
    ClearChrBattleFlags(0x101, 0x8000)

    label("loc_7AA1")

    Sleep(1000)
    OP_68(254920, 1830, 70340, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(22500, 0)
    StopBGM(0xBB8)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7102", 0)
    FadeToBright(1000, 0)
    OP_68(254920, 1330, 70340, 2000)
    OP_6F(0x79)
    OP_0D()
    Sleep(1000)
    Sound(808, 0, 100, 0)
    Sleep(500)
    SetChrPos(0x101, 251210, 0, 65690, 90)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x101, 0x8)

    NpcTalk(
        0x101,
        "Lloyd's Voice",
        "#2PKeA, do you have a moment?\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x9, 0x1)
    Sleep(500)

    ChrTalk(
        0x9,
        (
            "#01100FAh, Lloyd!\x01",
            "It's ok.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(254320, 1330, 66480, 2000)
    MoveCamera(45, 23, 0, 2000)
    Sound(103, 0, 100, 0)
    Sleep(500)

    def lambda_7BC0():
        OP_9B(0x0, 0xFE, 0x0, 0xA28, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7BC0)

    def lambda_7BD5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7BD5)
    BeginChrThread(0x9, 1, 0, 52)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x101, 2)
    TurnDirection(0x101, 0x9, 500)
    WaitChrThread(0x9, 1)
    OP_6F(0x79)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#00005FWhoa...\x01",
            "Looks like you've fully decorated it.\x02\x03",
            "#00009FHmm, seeing it like this\x01",
            "it's quite the spectacle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#01109FEhehe...\x01",
            "They're all cute, right?\x02\x03",
            "#01111FAh, but...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7CBA():

        label("loc_7CBA")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_7CBA")

    QueueWorkItem2(0x101, 1, lambda_7CBA)
    OP_68(256450, 1300, 64640, 3000)
    MoveCamera(60, 22, 0, 3000)
    SetCameraDistance(20000, 3000)
    OP_93(0x9, 0x5A, 0x1F4)
    OP_95(0x9, 256810, 30, 66480, 2000, 0x1)
    OP_95(0x9, 258100, 0, 65290, 2000, 0x0)
    OP_93(0x9, 0xB4, 0x1F4)
    TurnDirection(0x9, 0x101, 500)
    Sleep(500)
    OP_6F(0x79)
    EndChrThread(0x101, 0x1)

    ChrTalk(
        0x9,
        (
            "#01110F#5PThis one, actually it\x01",
            "says it's not a plushy.\x02\x03",
            "#01100FIt's written in the manual that it's a\x01",
            ""character costume", you enter inside it.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_7DE2():

        label("loc_7DE2")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_7DE2")

    QueueWorkItem2(0x9, 1, lambda_7DE2)
    BeginChrThread(0x101, 1, 0, 53)
    OP_68(257690, 1300, 64489, 2000)
    MoveCamera(60, 24, 0, 2000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x86, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_7EA0")

    ChrTalk(
        0x101,
        (
            "#00005F#2PA character costume...\x01",
            "Like Michey's?\x02\x03",
            "#00003FIndeed, if it's a child like you\x01",
            "KeA, it seems you could fit in.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7F20")

    label("loc_7EA0")


    ChrTalk(
        0x101,
        (
            "#00005F#2PA character costume...\x01",
            "Ah, yeah, I see.\x02\x03",
            "#00003FIndeed, if it's a child like you\x01",
            "KeA, it seems you could fit in.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7F20")

    WaitChrThread(0x101, 1)
    EndChrThread(0x9, 0x1)
    OP_6F(0x79)

    ChrTalk(
        0x9,
        (
            "#01105FAh, then...\x02\x03",
            "#01109FKeA will try to get inside,\x01",
            "can you help?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x9, 500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x86, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_800D")

    ChrTalk(
        0x101,
        (
            "#00005F#2PAlright, but...\x01",
            "I think it'll be quite hot.\x02\x03",
            "#00012FWhen I stood-in as Michey before,\x01",
            "I became totally exhausted.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_808A")

    label("loc_800D")


    ChrTalk(
        0x101,
        (
            "#00005F#2PAlright, but...\x01",
            "I think it'll be quite hot.\x02\x03",
            "#00003FOnce I read somewhere that\x01",
            "these things are quite sultry.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_808A")


    ChrTalk(
        0x9,
        (
            "#01100FHmm, I guess I'll be fine.\x02\x03",
            "#01109FAlso, I want Lloyd\x01",
            "to look at me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#2PUh...alright.\x02\x03",
            "#00004F(Uhhm, seems things could be hard in the future,\x01",
            "I wonder how she will turn out to be.)\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xBB8)
    SetMapObjFlags(0x12, 0x4)
    Sleep(2000)
    OP_68(254670, 1330, 68760, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(22500, 0)
    SetChrChipByIndex(0x9, 0x1E)
    SetChrSubChip(0x9, 0x0)
    SetChrPos(0x9, 255210, 30, 69560, 0)
    SetChrPos(0x101, 255340, 0, 68850, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(1000, 0, 100, 0)
    Sleep(1000)
    OP_9B(0x1, 0x101, 0xB4, 0x1F4, 0x3E8, 0x0)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#00004FOk...all set.\x02\x03",
            "#00000FKeA, does it hurt?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Nope, I'm fine.\x02\x03",
            "It feels cool and it's\x01",
            "not that hot, you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FEeeh... Could they have thought\x01",
            "quite well about air permeability?\x02",
        )
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7105", 0)
    Sleep(500)
    SetCameraDistance(20000, 500)
    TurnDirection(0x9, 0x101, 500)
    OP_82(0x0, 0x64, 0xBB8, 0xC8)
    Sound(3031, 255, 100, 0)

    NpcTalk(
        0x9,
        "KeA Penguin",
        "Tadaan!\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1500)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(1000)
    OP_82(0x0, 0x64, 0xBB8, 0xC8)
    SetMessageWindowPos(16, 150, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00011F#5SOoooh!?\x02\x03",
            "#00009F#3SW-What can I say...\x01",
            "You're terrifically cute...\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0xB, 255000, 0, 71000, 315)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8)

    NpcTalk(
        0xB,
        "KeA Penguin",
        "#1PEhehe, is that so?\x02",
    )

    CloseMessageWindow()
    OP_5A()
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x9, 1, 0, 54)
    Fade(150)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x0, 0x0, 0x0)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    Sleep(500)
    OP_0D()
    Fade(150)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x0, 0x0, 0x0)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    Sleep(500)
    OP_0D()
    Fade(150)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x0, 0x0, 0x0)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    Sleep(500)
    OP_0D()
    Fade(150)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x0, 0x0, 0x0)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    Sleep(500)
    OP_0D()
    Sleep(500)
    OP_C9(0x0, 0x80000000)

    NpcTalk(
        0xB,
        "KeA Penguin",
        (
            "#1P#3672VGood morning.\x02\x03",
            "#3673VNice to meet you.\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xE59)
    OP_C9(0x1, 0x80000000)
    SetMessageWindowPos(16, 150, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00011FOoh...!\x01",
            "(This has such a destructive force...!)\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(500)
    Sound(808, 0, 100, 0)
    Sleep(500)
    SetChrPos(0x103, 250000, 0, 64000, 90)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x103, 0x8)
    SetChrFlags(0x103, 0x40)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_85B1")
    ClearChrFlags(0x103, 0x80)
    ClearChrBattleFlags(0x103, 0x8000)

    label("loc_85B1")

    SetChrPos(0x102, 250000, 0, 64000, 90)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x102, 0x8)
    SetChrFlags(0x102, 0x40)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_85F0")
    ClearChrFlags(0x102, 0x80)
    ClearChrBattleFlags(0x102, 0x8000)

    label("loc_85F0")


    NpcTalk(
        0x102,
        "Elie's Voice",
        "#2PLloyd, are you there?\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(253400, 1330, 66290, 1500)
    SetCameraDistance(22500, 1500)
    OP_93(0x101, 0xE1, 0x1F4)
    OP_6F(0x79)

    NpcTalk(
        0x103,
        "Tio's Voice",
        (
            "#2PSince you weren't coming back,\x01",
            "we came to call you...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FAh, yeah, sorry to have made you wait.\x02\x03",
            "#00004FUhm... Come inside, after you\x01",
            "have mentally prepared.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x102,
        "Elie's Voice",
        "#2P???\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x103,
        "Tio's Voice",
        "#2PMentally prepared...is it?\x02",
    )

    CloseMessageWindow()
    Sound(103, 0, 100, 0)
    Sleep(500)
    SetChrPos(0x102, 251210, 0, 65690, 90)

    def lambda_8775():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_8775)
    BeginChrThread(0x102, 1, 0, 55)
    Sleep(500)
    SetChrPos(0x103, 251210, 0, 65690, 90)

    def lambda_87A0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_87A0)
    BeginChrThread(0x103, 1, 0, 56)

    ChrTalk(
        0x102,
        "#00100F#2PWhat in the world are you──\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x102, 1)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x103, 2)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#00105F#2PWhat...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00205F#3P#N............(*agape*)\x02",
    )

    CloseMessageWindow()
    OP_93(0x9, 0xE1, 0x1F4)

    NpcTalk(
        0x9,
        "KeA Penguin",
        (
            "Ah, it is Elie and Tio.\x02\x03",
            "Good day to you all.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_88AE():
        OP_A6(0xFE, 0x0, 0x14, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_88AE)
    Sleep(20)

    def lambda_88CA():
        OP_A6(0xFE, 0x0, 0x14, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_88CA)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#00105FWh#500W, #40Wwh#500W, #40Wwha...\x02",
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    ChrTalk(
        0x103,
        "#00201F#3P#N#5SThis is an incident...!\x02",
    )

    CloseMessageWindow()
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(254700, 1300, 68970, 1000)
    SetCameraDistance(20000, 1000)
    BeginChrThread(0x102, 1, 0, 59)
    Sleep(50)
    BeginChrThread(0x103, 1, 0, 60)
    Sleep(260)
    BeginChrThread(0x101, 1, 0, 62)
    OP_82(0x0, 0x64, 0xBB8, 0x64)
    Sound(811, 0, 100, 0)
    Sound(3318, 255, 100, 0)

    ChrTalk(
        0x101,
        "#00011F#4P#10AWhoa!\x02",
    )

    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    Sleep(500)
    Sound(898, 0, 100, 0)

    def lambda_89DA():
        OP_A6(0xFE, 0x0, 0x14, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_89DA)
    Sleep(20)

    def lambda_89F6():
        OP_A6(0xFE, 0x0, 0x14, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_89F6)
    Sleep(20)

    def lambda_8A12():
        OP_A6(0xFE, 0x0, 0x14, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_8A12)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x9, 1)
    WaitChrThread(0x101, 1)
    SetChrSubChip(0x101, 0x2)
    Sleep(500)
    OP_6F(0x79)

    ChrTalk(
        0x102,
        (
            "#00114FC-Cute!\x01",
            "You're cute, KeA!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00204FI-Impossible...\x02\x03",
            "#00201FThat such a thing could exist\x01",
            "in the bidimensional plane is...!\x02",
        )
    )

    CloseMessageWindow()
    Sound(898, 0, 100, 0)

    def lambda_8AD4():
        OP_A6(0xFE, 0x0, 0x14, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8AD4)
    Sleep(20)

    def lambda_8AF0():
        OP_A6(0xFE, 0x0, 0x14, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8AF0)
    Sleep(20)

    def lambda_8B0C():
        OP_A6(0xFE, 0x0, 0x14, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_8B0C)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x9, 1)

    NpcTalk(
        0x9,
        "KeA Penguin",
        (
            "I-It's hard to breath...\x02\x03",
            "Please, do not hug\x01",
            "KeA so much...\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    OP_93(0x101, 0x13B, 0x0)
    OP_0D()
    Sleep(250)
    OP_95(0x101, 254940, 0, 68140, 2000, 0x0)
    TurnDirection(0x101, 0x9, 0)
    OP_68(253400, 1330, 66290, 2500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8F70")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_8BE7")
    ClearChrFlags(0x104, 0x80)
    ClearChrBattleFlags(0x104, 0x8000)

    label("loc_8BE7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_8C00")
    ClearChrFlags(0x109, 0x80)
    ClearChrBattleFlags(0x109, 0x8000)

    label("loc_8C00")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_8C19")
    ClearChrFlags(0x105, 0x80)
    ClearChrBattleFlags(0x105, 0x8000)

    label("loc_8C19")

    ClearChrFlags(0x109, 0x8)
    SetChrFlags(0x109, 0x40)
    SetChrPos(0x109, 251210, 0, 65690, 90)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_8C44():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_8C44)
    BeginChrThread(0x109, 1, 0, 57)
    Sleep(500)
    ClearChrFlags(0x104, 0x8)
    SetChrFlags(0x104, 0x40)
    SetChrPos(0x104, 251210, 0, 65690, 90)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_8C84():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_8C84)
    BeginChrThread(0x104, 1, 0, 58)
    Sleep(500)
    ClearChrFlags(0x105, 0x8)
    SetChrFlags(0x105, 0x40)
    SetChrPos(0x105, 251210, 0, 65690, 90)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_8CC4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_8CC4)
    BeginChrThread(0x105, 1, 0, 56)

    ChrTalk(
        0x104,
        "#00305FWhat's all this noi──what the heck!?\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0xE1, 0x1F4)
    WaitChrThread(0x109, 1)
    WaitChrThread(0x109, 2)
    WaitChrThread(0x105, 1)
    WaitChrThread(0x105, 2)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x104, 2)
    OP_6F(0x79)

    ChrTalk(
        0x109,
        (
            "#10105F#12PK-KeA!?\x02\x03",
            "#10109FWhaaaaaaaaaaaaaaaa!!\x01",
            "Please, let me hug her too!!\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x109, 1, 0, 61)
    Sleep(200)
    BeginChrThread(0x101, 1, 0, 63)
    OP_82(0x0, 0x64, 0xBB8, 0x64)
    Sound(811, 0, 100, 0)
    Sound(3319, 255, 100, 0)

    ChrTalk(
        0x101,
        "#00011F#4P#10AAck!\x02",
    )

    WaitChrThread(0x109, 1)
    Sleep(500)
    Sound(898, 0, 100, 0)

    def lambda_8DD1():
        OP_A6(0xFE, 0x0, 0x14, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8DD1)
    Sleep(20)

    def lambda_8DED():
        OP_A6(0xFE, 0x0, 0x14, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8DED)
    Sleep(20)

    def lambda_8E09():
        OP_A6(0xFE, 0x0, 0x14, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_8E09)
    Sleep(20)

    def lambda_8E25():
        OP_A6(0xFE, 0x0, 0x14, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_8E25)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x9, 1)
    WaitChrThread(0x109, 1)
    WaitChrThread(0x101, 1)
    Sleep(500)
    OP_68(255000, 1330, 66890, 2000)
    BeginChrThread(0x104, 1, 0, 66)
    Sleep(200)
    BeginChrThread(0x105, 1, 0, 65)
    WaitChrThread(0x105, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x79)

    ChrTalk(
        0x105,
        (
            "#10304F#6PHu hu, how unfortunate.\x02\x03",
            "#10309FI really think it's an impossibly\x01",
            "atrocious cuteness, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309F#6PMaaan!\x01",
            "If she showed up on the battlefield for real,\x01",
            "panic will ensue in a different meanin', right!?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    TurnDirection(0x104, 0x9, 500)
    TurnDirection(0x105, 0x9, 500)
    Jump("loc_913D")

    label("loc_8F70")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_8F89")
    ClearChrFlags(0x104, 0x80)
    ClearChrBattleFlags(0x104, 0x8000)

    label("loc_8F89")

    ClearChrFlags(0x104, 0x8)
    SetChrFlags(0x104, 0x40)
    SetChrPos(0x104, 251210, 0, 65690, 90)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_8FB4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_8FB4)
    BeginChrThread(0x104, 1, 0, 56)
    Sleep(500)

    ChrTalk(
        0x104,
        "#00305FWhat's all this noi──what the heck!?\x02",
    )

    CloseMessageWindow()
    OP_6F(0x79)
    Sound(898, 0, 100, 0)

    def lambda_9009():
        OP_A6(0xFE, 0x0, 0x14, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9009)
    Sleep(20)

    def lambda_9025():
        OP_A6(0xFE, 0x0, 0x14, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_9025)
    Sleep(20)

    def lambda_9041():
        OP_A6(0xFE, 0x0, 0x14, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_9041)
    OP_68(253160, 1330, 67480, 2000)
    OP_95(0x104, 253400, 0, 68000, 2000, 0x0)
    TurnDirection(0x104, 0x9, 500)
    Sleep(500)
    WaitChrThread(0x104, 1)
    OP_6F(0x79)

    ChrTalk(
        0x104,
        (
            "#00303F#6PHey now, what's with this\x01",
            "impossible atrocious cuteness...!?\x02\x03",
            "#00309FIf she showed up on the battlefield for real,\x01",
            "panic will ensue in a different meaning, right!?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_913D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_916B")
    Sleep(500)
    SetChrSubChip(0x101, 0x0)
    Sleep(750)
    Fade(500)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0x101, 0xFF)
    OP_0D()
    TurnDirection(0x101, 0x9, 500)
    Sleep(500)

    label("loc_916B")


    ChrTalk(
        0x101,
        (
            "#00012FHa, ha ha...\x01",
            "(Maybe it's no laughing matter...)\x02",
        )
    )

    CloseMessageWindow()
    OP_68(254320, 1330, 68620, 2000)
    Sound(898, 0, 100, 0)

    def lambda_91C3():
        OP_A6(0xFE, 0x0, 0x14, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_91C3)
    Sleep(20)

    def lambda_91DF():
        OP_A6(0xFE, 0x0, 0x14, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_91DF)
    Sleep(20)

    def lambda_91FB():
        OP_A6(0xFE, 0x0, 0x14, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_91FB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9235")
    Sleep(20)

    def lambda_9221():
        OP_A6(0xFE, 0x0, 0x14, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_9221)

    label("loc_9235")

    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x9, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_924F")
    WaitChrThread(0x109, 1)

    label("loc_924F")

    OP_63(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_6F(0x79)
    Sleep(200)

    NpcTalk(
        0x9,
        "KeA Penguin",
        (
            "Auuugh...\x01",
            "I surrender...\x02\x03",
            "Please let KeA go already...\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(22000, 2500)
    FadeToDark(2000, 0, -1)
    Sound(898, 0, 100, 0)

    def lambda_92CF():
        OP_A6(0xFE, 0x0, 0x14, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_92CF)
    Sleep(20)

    def lambda_92EB():
        OP_A6(0xFE, 0x0, 0x14, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_92EB)
    Sleep(20)

    def lambda_9307():
        OP_A6(0xFE, 0x0, 0x14, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_9307)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9341")
    Sleep(20)

    def lambda_932D():
        OP_A6(0xFE, 0x0, 0x14, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_932D)

    label("loc_9341")

    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x9, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_935B")
    WaitChrThread(0x109, 1)

    label("loc_935B")

    OP_0D()
    OP_64(0x9)
    SetChrName("")
    SetMessageWindowPos(14, 280, 60, 3)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "──Then, after some time, the womenfolk\x01",
            "finally came to their senses...\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Due to its excessive dangerousness, a rule that\x01",
            "banned KeA Penguin from now on was made.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    Sound(9, 0, 100, 0)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "You gave all the plushies to KeA!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    StopBGM(0xBB8)
    WaitBGM()
    Sleep(10)
    OP_1F()
    SetChrFlags(0x9, 0x80)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x0, 0x40)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_9495")
    SetChrFlags(0x101, 0x80)
    SetChrBattleFlags(0x101, 0x8000)

    label("loc_9495")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_94AE")
    SetChrFlags(0x102, 0x80)
    SetChrBattleFlags(0x102, 0x8000)

    label("loc_94AE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_94C7")
    SetChrFlags(0x103, 0x80)
    SetChrBattleFlags(0x103, 0x8000)

    label("loc_94C7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_94E0")
    SetChrFlags(0x109, 0x80)
    SetChrBattleFlags(0x109, 0x8000)

    label("loc_94E0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_94F9")
    SetChrFlags(0x104, 0x80)
    SetChrBattleFlags(0x104, 0x8000)

    label("loc_94F9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_9512")
    SetChrFlags(0x105, 0x80)
    SetChrBattleFlags(0x105, 0x8000)

    label("loc_9512")

    OP_49()
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_CC(0x1, 0xFF, 0x0)
    ClearMapObjFlags(0x12, 0x4)
    SetScenarioFlags(0x12D, 4)
    OP_50(0x64, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    EventEnd(0x6)
    NewScene("c0130", 112, 0, 0)
    IdleLoop()
    Return()

    # Function_51_79ED end

    def Function_52_9539(): pass

    label("Function_52_9539")

    SetChrChipByIndex(0xFE, 0x0)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0xB4, 0x0)
    Sound(812, 0, 100, 0)
    OP_9C(0xFE, 0x0, 0x0, 0xFFFFFC18, 0x1F4, 0xBB8)
    ClearChrFlags(0xFE, 0x4)
    SetChrFlags(0x9, 0x1)
    OP_95(0xFE, 253820, 30, 66880, 2000, 0x0)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_52_9539 end

    def Function_53_9588(): pass

    label("Function_53_9588")

    OP_95(0xFE, 255000, 30, 64379, 2000, 0x1)
    OP_95(0xFE, 256640, 30, 64000, 2000, 0x0)
    Return()

    # Function_53_9588 end

    def Function_54_95B1(): pass

    label("Function_54_95B1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_964F")
    SetChrSubChip(0xFE, 0x1)
    Sleep(150)
    SetChrSubChip(0xFE, 0x2)
    Sleep(150)
    SetChrSubChip(0xFE, 0x1)
    Sleep(150)
    SetChrSubChip(0xFE, 0x0)
    Sleep(150)

    label("loc_95D8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_95EF")
    Sleep(150)
    Jump("loc_95D8")

    label("loc_95EF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9603")
    Jump("loc_964F")

    label("loc_9603")

    SetChrSubChip(0xFE, 0x3)
    Sleep(150)
    SetChrSubChip(0xFE, 0x4)
    Sleep(150)
    SetChrSubChip(0xFE, 0x3)
    Sleep(150)
    SetChrSubChip(0xFE, 0x0)
    Sleep(150)

    label("loc_961F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9636")
    Sleep(150)
    Jump("loc_961F")

    label("loc_9636")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_964A")
    Jump("loc_964F")

    label("loc_964A")

    Jump("Function_54_95B1")

    label("loc_964F")

    Return()

    # Function_54_95B1 end

    def Function_55_9650(): pass

    label("Function_55_9650")

    OP_9B(0x0, 0xFE, 0x0, 0xA28, 0x7D0, 0x0)
    TurnDirection(0xFE, 0x9, 0)
    Return()

    # Function_55_9650 end

    def Function_56_9667(): pass

    label("Function_56_9667")

    OP_9B(0x0, 0xFE, 0x0, 0x640, 0x7D0, 0x0)
    TurnDirection(0xFE, 0x9, 0)
    Return()

    # Function_56_9667 end

    def Function_57_967E(): pass

    label("Function_57_967E")

    OP_9B(0x0, 0xFE, 0xFFF6, 0xBB8, 0x7D0, 0x0)
    TurnDirection(0xFE, 0x9, 0)
    Return()

    # Function_57_967E end

    def Function_58_9695(): pass

    label("Function_58_9695")

    OP_9B(0x0, 0xFE, 0xA, 0xBB8, 0x7D0, 0x0)
    TurnDirection(0xFE, 0x9, 0)
    Return()

    # Function_58_9695 end

    def Function_59_96AC(): pass

    label("Function_59_96AC")

    OP_95(0xFE, 255390, 30, 69100, 5000, 0x0)
    OP_93(0xFE, 0x0, 0x0)
    Return()

    # Function_59_96AC end

    def Function_60_96C8(): pass

    label("Function_60_96C8")

    OP_95(0xFE, 254730, 30, 69610, 5000, 0x0)
    OP_93(0xFE, 0x5A, 0x0)
    Return()

    # Function_60_96C8 end

    def Function_61_96E4(): pass

    label("Function_61_96E4")

    OP_95(0xFE, 254620, 30, 68940, 5000, 0x0)
    OP_93(0xFE, 0x2D, 0x0)
    Return()

    # Function_61_96E4 end

    def Function_62_9700(): pass

    label("Function_62_9700")

    SetChrChipByIndex(0xFE, 0xFF)

    def lambda_9709():
        OP_9D(0xFE, 0x3E800, 0x0, 0x1084C, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_9709)
    BeginChrThread(0xFE, 3, 0, 64)
    WaitChrThread(0xFE, 2)
    EndChrThread(0xFE, 0x3)
    OP_93(0xFE, 0x10E, 0x0)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_62_9700 end

    def Function_63_973F(): pass

    label("Function_63_973F")

    SetChrChipByIndex(0xFE, 0xFF)

    def lambda_9748():
        OP_9D(0xFE, 0x3E8C8, 0x0, 0x109DC, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_9748)
    BeginChrThread(0xFE, 3, 0, 64)
    WaitChrThread(0xFE, 2)
    EndChrThread(0xFE, 0x3)
    OP_93(0xFE, 0x10E, 0x0)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    Sleep(50)
    SetChrSubChip(0xFE, 0x3)
    Return()

    # Function_63_973F end

    def Function_64_9785(): pass

    label("Function_64_9785")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_97B1")
    OP_93(0xFE, 0x10E, 0x3E8)
    OP_93(0xFE, 0x0, 0x3E8)
    OP_93(0xFE, 0x5A, 0x3E8)
    OP_93(0xFE, 0xB4, 0x3E8)
    Jump("Function_64_9785")

    label("loc_97B1")

    Return()

    # Function_64_9785 end

    def Function_65_97B2(): pass

    label("Function_65_97B2")

    OP_95(0xFE, 254750, 30, 67380, 2000, 0x0)
    TurnDirection(0xFE, 0x101, 500)
    Return()

    # Function_65_97B2 end

    def Function_66_97CE(): pass

    label("Function_66_97CE")

    OP_95(0xFE, 254770, 30, 66380, 2000, 0x1)
    OP_95(0xFE, 255780, 30, 66850, 2000, 0x0)
    TurnDirection(0xFE, 0x101, 500)
    Return()

    # Function_66_97CE end

    def Function_67_97FE(): pass

    label("Function_67_97FE")

    OP_95(0xFE, 254550, 30, 67480, 2000, 0x0)
    TurnDirection(0xFE, 0x101, 500)
    Return()

    # Function_67_97FE end

    def Function_68_981A(): pass

    label("Function_68_981A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(3657)
    SoundLoad(3039)
    SoundLoad(3660)
    AddParty(0x52, 0xFF, 0xFF)
    LoadChrToIndex("apl/ch51100.itc", 0x1E)
    OP_68(253500, 1100, 71300, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21000, 0)
    SetChrPos(0x101, 251000, 0, 66000, 90)
    SetChrPos(0x102, 251000, 0, 66000, 90)
    SetChrPos(0x109, 251000, 0, 66000, 90)
    SetChrPos(0x105, 251000, 0, 66000, 90)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0x153, 0x4)
    SetChrPos(0x153, 254100, 200, 71300, 270)
    SetChrChipByIndex(0x153, 0x1)
    SetChrSubChip(0x153, 0x0)
    SetCameraDistance(22000, 1500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Sleep(300)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x153,
        (
            "#01111F#3657V#11P#40WLet's see, if I substitute this value\x01",
            "in this numerical formula, then...\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xE49)
    OP_63(0x153, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x153)
    OP_63(0x153, 0x0, 1700, 0x22, 0x24, 0xFA, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x153,
        "#01109F#3039V#11P#30W#4S──Yes! I did it!\x02",
    )

    CloseMessageWindow()
    OP_24(0xBDF)
    OP_C9(0x1, 0x80000000)
    Sleep(300)
    Sound(808, 0, 100, 0)
    Sleep(1000)

    NpcTalk(
        0x101,
        "Lloyd's Voice",
        "KeA?\x02",
    )

    CloseMessageWindow()
    OP_63(0x153, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x153, 0x1)
    Sound(103, 0, 100, 0)
    OP_68(254000, 1100, 69900, 3000)
    MoveCamera(45, 23, 0, 3000)
    SetCameraDistance(23000, 3000)
    BeginChrThread(0x101, 3, 0, 69)
    BeginChrThread(0x102, 3, 0, 70)
    BeginChrThread(0x109, 3, 0, 71)
    BeginChrThread(0x105, 3, 0, 72)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x153,
        "#01110F#3660V#5P#15A#30WAh, Lloyd.\x02",
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    OP_6F(0x79)
    WaitChrThread(0x101, 3)

    ChrTalk(
        0x101,
        (
            "#00005F#11PKeA, you have Sunday\x01",
            "School today, right?\x02\x03",
            "#00000FAre you fine not leaving?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#01105F#5PAh, yes.\x01",
            "Maybe it's already time to meet.\x02\x03",
            "#01100FGuys, are you going out for a job?\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x102, 3)
    WaitChrThread(0x109, 3)
    WaitChrThread(0x105, 3)

    ChrTalk(
        0x102,
        (
            "#12P#00109FYes, if you want, we thought\x01",
            "we could go out together.\x02\x03",
            "#00105FMy.. Were you doing\x01",
            "Sunday School homework?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#01109F#5PEhehe, that's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10102F#12PYou're so good, KeA.\x02\x03",
            "#10106FI guess I almost never did\x01",
            "Sunday School homework.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10304FHu hu, if pushed I'd say that I\x01",
            "almost never showed up at lessons.\x02\x03",
            "#10302FMore than being taught by an inept Father,\x01",
            "it was efficient studying by myself.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_9D33():
        TurnDirection(0x101, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_9D33)
    Sleep(150)

    def lambda_9D43():
        TurnDirection(0x102, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_9D43)
    Sleep(150)

    def lambda_9D53():
        TurnDirection(0x109, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_9D53)
    Sleep(150)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x109, 0)

    def lambda_9D6F():

        label("loc_9D6F")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_9D6F")

    QueueWorkItem2(0x101, 2, lambda_9D6F)

    def lambda_9D81():

        label("loc_9D81")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_9D81")

    QueueWorkItem2(0x102, 2, lambda_9D81)

    def lambda_9D93():

        label("loc_9D93")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_9D93")

    QueueWorkItem2(0x109, 2, lambda_9D93)

    ChrTalk(
        0x101,
        "#5P#00001FWazy, you know...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00111F#11PI'd wish for you to not set\x01",
            "a bad example for KeA...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#01100F#5PHoeee...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10304FHu hu, the parents got angry.\x02\x03",
            "#10305F...Oh?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_9E60():
        OP_95(0xFE, 253000, 30, 69300, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_9E60)
    WaitChrThread(0x105, 1)
    Sleep(300)

    ChrTalk(
        0x105,
        "#6P#10301F............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#11PWazy?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#01105F#5PHmm, something's wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10304FHu hu, I thought that Crossbell\x01",
            "is really progressing in many ways.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x105,
        "#6P#10300FMore importantly, should we go?\x02",
    )

    CloseMessageWindow()
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x109, 0x2)

    ChrTalk(
        0x101,
        "#00000F#11PRight.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x153, 500)

    def lambda_9F90():

        label("loc_9F90")

        TurnDirection(0xFE, 0x153, 500)
        Yield()
        Jump("loc_9F90")

    QueueWorkItem2(0x101, 2, lambda_9F90)
    Sleep(150)

    ChrTalk(
        0x101,
        "#00000F#11PKeA, are you coming with us?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#01109F#5PYes!\x01",
            "Just wait a moment!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    def lambda_9FFD():

        label("loc_9FFD")

        TurnDirection(0xFE, 0x153, 500)
        Yield()
        Jump("loc_9FFD")

    QueueWorkItem2(0x105, 2, lambda_9FFD)

    def lambda_A00F():

        label("loc_A00F")

        TurnDirection(0xFE, 0x153, 500)
        Yield()
        Jump("loc_A00F")

    QueueWorkItem2(0x102, 2, lambda_A00F)

    def lambda_A021():

        label("loc_A021")

        TurnDirection(0xFE, 0x153, 500)
        Yield()
        Jump("loc_A021")

    QueueWorkItem2(0x109, 2, lambda_A021)
    SetChrChipByIndex(0x153, 0xFF)
    SetChrSubChip(0x153, 0x0)
    Sound(802, 0, 100, 0)
    OP_68(255000, 1100, 69700, 3000)
    OP_9D(0x153, 0x3E0F8, 0x0, 0x11940, 0x12C, 0xBB8)
    ClearChrFlags(0x153, 0x4)
    OP_93(0x153, 0x2D, 0x1F4)

    def lambda_A075():
        OP_95(0xFE, 255700, 0, 72800, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_A075)
    WaitChrThread(0x153, 1)
    OP_93(0x153, 0x0, 0x1F4)
    Sleep(750)
    Fade(250)
    SetChrChipByIndex(0x153, 0x1E)
    SetChrSubChip(0x153, 0x0)
    OP_0D()
    OP_93(0x153, 0xB4, 0x1F4)
    SetChrFlags(0x153, 0x1000)

    def lambda_A0B7():
        OP_95(0xFE, 255700, 30, 70400, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_A0B7)
    WaitChrThread(0x153, 1)
    ClearChrFlags(0x153, 0x1000)
    OP_93(0x153, 0xE1, 0x1F4)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x105, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x109, 0x2)
    OP_6F(0x79)

    ChrTalk(
        0x153,
        "#5P#01110FYes, sorry to make you waiting!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00002FAlright, let's go then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00102FSince we're with KeA, should\x01",
            "we go out from the back exit?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_49()
    SetChrChipByIndex(0x153, 0xFF)
    SetChrSubChip(0x153, 0x0)
    OP_D7(0x1E)
    RemoveParty(0x52, 0xFF)
    AddParty(0xA4, 0xFF, 0xFF)
    SetChrPos(0x0, 254700, 30, 69400, 225)
    SetScenarioFlags(0x126, 2)
    EventEnd(0x5)
    Return()

    # Function_68_981A end

    def Function_69_A1C3(): pass

    label("Function_69_A1C3")


    def lambda_A1C8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_A1C8)

    def lambda_A1D9():
        OP_95(0xFE, 253000, 0, 66000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A1D9)
    WaitChrThread(0xFE, 1)

    def lambda_A1F7():
        OP_95(0xFE, 254000, 0, 69300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A1F7)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_69_A1C3 end

    def Function_70_A218(): pass

    label("Function_70_A218")

    Sleep(700)

    def lambda_A220():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_A220)

    def lambda_A231():
        OP_95(0xFE, 253000, 0, 66000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A231)
    WaitChrThread(0xFE, 1)

    def lambda_A24F():
        OP_95(0xFE, 254300, 0, 68300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A24F)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_70_A218 end

    def Function_71_A270(): pass

    label("Function_71_A270")

    Sleep(1400)

    def lambda_A278():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_A278)

    def lambda_A289():
        OP_95(0xFE, 253000, 0, 66000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A289)
    WaitChrThread(0xFE, 1)

    def lambda_A2A7():
        OP_95(0xFE, 255100, 0, 67900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A2A7)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x13B, 0x1F4)
    Return()

    # Function_71_A270 end

    def Function_72_A2C8(): pass

    label("Function_72_A2C8")

    Sleep(2100)

    def lambda_A2D0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_A2D0)

    def lambda_A2E1():
        OP_95(0xFE, 253000, 0, 66000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A2E1)
    WaitChrThread(0xFE, 1)

    def lambda_A2FF():
        OP_95(0xFE, 253100, 0, 67900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A2FF)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_72_A2C8 end

    def Function_73_A320(): pass

    label("Function_73_A320")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    LoadChrToIndex("apl/ch51275.itc", 0x1E)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu00300.itp")
    OP_68(-2250, 1100, 67800, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23500, 0)
    SetChrPos(0x101, -2000, 10, 69500, 180)
    SetChrPos(0x102, -2000, 10, 68300, 270)
    SetChrPos(0x104, -1000, 0, 68300, 270)
    SetChrPos(0x109, -2500, 10, 67300, 270)
    SetChrPos(0x105, -1500, 10, 67300, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    def lambda_A403():
        OP_97(0x109, 0xFFFFEC78, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_A403)
    Sleep(200)

    def lambda_A420():
        OP_97(0x102, 0xFFFFEC78, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_A420)
    Sleep(200)

    def lambda_A43D():
        OP_97(0x105, 0xFFFFEC78, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_A43D)
    SetCameraDistance(22500, 2000)
    FadeToBright(1000, 0)
    VolumeBGM(0x50, 0x3E8)
    Sound(103, 0, 100, 0)
    Sleep(600)

    def lambda_A478():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_A478)
    Sleep(400)

    def lambda_A48C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_A48C)
    Sleep(400)

    def lambda_A4A0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_A4A0)

    def lambda_A4B1():
        OP_96(0xFE, 0xFFFFF448, 0xA, 0x108D8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A4B1)
    Sleep(300)

    def lambda_A4CE():
        OP_96(0xFE, 0xFFFFFA24, 0xA, 0x108D8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A4CE)
    WaitChrThread(0x101, 1)
    TurnDirection(0x101, 0x104, 500)

    ChrTalk(
        0x101,
        "#00003F#11P──Say, Randy.\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x104, 1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x104, 0x101, 500)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)

    AnonymousTalk(
        0x104,
        "Uhm? What, Lloyd.\x02",
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
            "#00008F#11PYou know...\x01",
            "About your father...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x104,
        (
            "#6P#00306FAh, that...\x01\x02\x03",
            "#00300FI don't particularly mind it, you know?\x01",
            "It's no rare story in that kind of world.\x02\x03",
            "Also, when I broke away from the group,\x01",
            "I severed ties with my ol' man.\x02\x03",
            "#00304FIt doesn't mean I didn't feel anything, but...\x01",
            "Well, I felt relieved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#11P...I see.\x02\x03",
            "#00001FHowever, when you feel like it,\x01",
            "you can tell me everything, okay?\x02\x03",
            "After all, as the leader\x01",
            "there could be things I\x01",
            "can you advice on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00305F............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00011F#11PAh, sorry.\x01",
            "Was I a bit impertinent?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00304FHa ha, no, no.\x02\x03",
            "#00302FAll things considered, I\x01",
            "thought you've grown up too.\x02\x03",
            "#00309FHmm, your big bro here is deeply moved.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 5)), scpexpr(EXPR_END)), "loc_AAB4")

    ChrTalk(
        0x101,
        "#00006F#11PHey now...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00008F#11P...It's just...that I'd want to be\x01",
            "of help to you in such moments.\x02\x03",
            "#00000FMaybe I'm not so reliable, but that's\x01",
            "what means to be "buddies", right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00305FLloyd...\x02",
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x104)
    SetCameraDistance(22000, 1000)

    def lambda_A9B5():
        OP_96(0xFE, 0xFFFFF736, 0xA, 0x108D8, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A9B5)
    WaitChrThread(0x104, 1)
    OP_6F(0x79)
    SetChrChipByIndex(0x104, 0x1E)
    SetChrSubChip(0x104, 0x2)
    SetChrFlags(0x104, 0x10)
    SetChrFlags(0x104, 0x2)
    SetChrFlags(0x104, 0x20)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x6)
    SetChrFlags(0x101, 0x10)
    SetChrFlags(0x101, 0x2)
    SetChrFlags(0x101, 0x20)
    Sleep(100)
    SetChrSubChip(0x104, 0x3)
    SetChrSubChip(0x101, 0x7)
    Sound(811, 0, 30, 0)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#6P#00302F...Alright, got it. Maybe one\x01",
            "day I'll tell you everything.\x02\x03",
            "#00309FI'll count on you when that time comes──buddy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002F#11PYeah...!\x02",
    )

    CloseMessageWindow()
    Jump("loc_AB4F")

    label("loc_AAB4")


    ChrTalk(
        0x101,
        "#00006F#11PHey now...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00304F...Well, if I feel like it I\x01",
            "could ask you for advice.\x02\x03",
            "#00300FI'll count on you, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#11PYeah...!\x02",
    )

    CloseMessageWindow()

    label("loc_AB4F")

    SetChrPos(0x102, -7000, -2000, 68300, 270)
    SetChrPos(0x105, -7000, -2000, 67300, 270)

    NpcTalk(
        0x105,
        "Wazy's Voice",
        "#2P#2SOh, what're you doing?\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x102,
        "Elie's Voice",
        "#2P#2SDid you forget something?\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 5)), scpexpr(EXPR_END)), "loc_AC57")
    SetCameraDistance(22500, 700)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    ClearChrFlags(0x104, 0x10)
    ClearChrFlags(0x104, 0x2)
    ClearChrFlags(0x104, 0x20)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x101, 0x10)
    ClearChrFlags(0x101, 0x2)
    ClearChrFlags(0x101, 0x20)

    def lambda_AC3E():
        OP_96(0xFE, 0xFFFFF542, 0xA, 0x108D8, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_AC3E)
    WaitChrThread(0x104, 1)

    label("loc_AC57")


    def lambda_AC5C():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_AC5C)

    ChrTalk(
        0x101,
        "#00011F#11PSorry, we'll be there immediately!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#11P#00304FAlright then, let's begin our\x01",
            "work in a nice and relaxed way.\x02",
        )
    )

    CloseMessageWindow()
    VolumeBGM(0x64, 0x3E8)

    def lambda_ACF0():
        OP_97(0x104, 0xFFFFEC78, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_ACF0)
    Sleep(100)

    def lambda_AD0D():
        OP_97(0x101, 0xFFFFEC78, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_AD0D)
    FadeToDark(1000, 0, -1)
    Sleep(400)

    def lambda_AD34():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_AD34)
    Sleep(400)

    def lambda_AD48():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_AD48)
    OP_0D()
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x104, 0xFF)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_CC(0x1, 0xFF, 0x0)
    Sound(814, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "You are now able to move everywhere\x01",
            "in Crossbell via orbal car.\x02\x03",
            "It is parked at the Special Support Section back\x01",
            "entrance facing West Street. Please try using it.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x140, 1)
    OP_C9(0x1, 0x1000)
    EventEnd(0x5)
    NewScene("c0200", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_73_A320 end

    def Function_74_AE77(): pass

    label("Function_74_AE77")

    EventBegin(0x0)
    Fade(500)
    OP_68(256290, 1300, 67750, 0)
    MoveCamera(50, 18, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(22450, 0)
    SetChrPos(0x101, 255980, 0, 68000, 90)
    SetChrPos(0x102, 255700, 30, 68900, 90)
    SetChrPos(0x103, 255360, 0, 67250, 90)
    SetChrPos(0x104, 254500, 0, 68200, 90)
    SetChrPos(0x109, 253700, 30, 68850, 90)
    SetChrPos(0x105, 253800, 0, 67250, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrSubChip(0x8, 0x0)
    OP_0D()

    ChrTalk(
        0x8,
        "#11P#01100FSafe travels, everyone!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10109FUh uh, we're going, KeA.\x02\x03",
            "#10106F...And so, even being told\x01",
            ""safe travels" by KeA is going\x01",
            "to disappear for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00002FHa ha...you'll really miss her, eh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106FParting from KeA is something you \x01",
            "can't bear, even if you just imagine it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#01100FIf Noｱl goes away,\x01",
            "KeA too will be sad...\x01",
            "Cheer up, Noｱl.\x02\x03",
            "#01109FI'll wait for you and a healthy\x01",
            "Fran to come to have fun here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10102FYes, thank you, KeA.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302FHa ha, Noｱl.\x01",
            "If things are like this, you must go\x01",
            "reorganize the CGF on the double.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00202FEven Miss Fran must\x01",
            "recover immediately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10109FUh uh, you're right.\x02\x03",
            "#10100FIt's also in order to reunite with KeA's\x01",
            "smile even only one day faster!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#12P#10302FOh boy, you're fired up, eh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11P#01102FEhehe...\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x19D, 5)
    OP_50(0x64, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_69(0xFF, 0x0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x0, 255700, 0, 68570, 90)
    EventEnd(0x5)
    Return()

    # Function_74_AE77 end

    SaveToFile()

Try(main)
