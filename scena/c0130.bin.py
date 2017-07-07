from ScenarioHelper import *

def main():
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
        "Keya",                 # 1
        "Keya",                 # 2
        "Zeit",               # 3
        "SE control",                 # 4
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
        "Function_4_FBA",          # 04, 4
        "Function_5_108A",         # 05, 5
        "Function_6_14DC",         # 06, 6
        "Function_7_1C21",         # 07, 7
        "Function_8_1C74",         # 08, 8
        "Function_9_1CC9",         # 09, 9
        "Function_10_1D86",        # 0A, 10
        "Function_11_1E43",        # 0B, 11
        "Function_12_1E9A",        # 0C, 12
        "Function_13_2974",        # 0D, 13
        "Function_14_2C30",        # 0E, 14
        "Function_15_2F0C",        # 0F, 15
        "Function_16_311B",        # 10, 16
        "Function_17_333C",        # 11, 17
        "Function_18_354D",        # 12, 18
        "Function_19_375E",        # 13, 19
        "Function_20_3972",        # 14, 20
        "Function_21_3B86",        # 15, 21
        "Function_22_3F82",        # 16, 22
        "Function_23_40A8",        # 17, 23
        "Function_24_4105",        # 18, 24
        "Function_25_41AA",        # 19, 25
        "Function_26_424F",        # 1A, 26
        "Function_27_42F4",        # 1B, 27
        "Function_28_43A7",        # 1C, 28
        "Function_29_4484",        # 1D, 29
        "Function_30_448D",        # 1E, 30
        "Function_31_4544",        # 1F, 31
        "Function_32_45FB",        # 20, 32
        "Function_33_46B4",        # 21, 33
        "Function_34_476B",        # 22, 34
        "Function_35_4822",        # 23, 35
        "Function_36_48D9",        # 24, 36
        "Function_37_498E",        # 25, 37
        "Function_38_4A47",        # 26, 38
        "Function_39_4B02",        # 27, 39
        "Function_40_4B77",        # 28, 40
        "Function_41_4BA6",        # 29, 41
        "Function_42_4BD5",        # 2A, 42
        "Function_43_4C04",        # 2B, 43
        "Function_44_4C33",        # 2C, 44
        "Function_45_5845",        # 2D, 45
        "Function_46_584D",        # 2E, 46
        "Function_47_6A0B",        # 2F, 47
        "Function_48_6A65",        # 30, 48
        "Function_49_6A81",        # 31, 49
        "Function_50_75FE",        # 32, 50
        "Function_51_761A",        # 33, 51
        "Function_52_909F",        # 34, 52
        "Function_53_90EE",        # 35, 53
        "Function_54_9117",        # 36, 54
        "Function_55_91B6",        # 37, 55
        "Function_56_91CD",        # 38, 56
        "Function_57_91E4",        # 39, 57
        "Function_58_91FB",        # 3A, 58
        "Function_59_9212",        # 3B, 59
        "Function_60_922E",        # 3C, 60
        "Function_61_924A",        # 3D, 61
        "Function_62_9266",        # 3E, 62
        "Function_63_92A5",        # 3F, 63
        "Function_64_92EB",        # 40, 64
        "Function_65_9318",        # 41, 65
        "Function_66_9334",        # 42, 66
        "Function_67_9364",        # 43, 67
        "Function_68_9380",        # 44, 68
        "Function_69_9CBC",        # 45, 69
        "Function_70_9D11",        # 46, 70
        "Function_71_9D69",        # 47, 71
        "Function_72_9DC1",        # 48, 72
        "Function_73_9E19",        # 49, 73
        "Function_74_A88D",        # 4A, 74
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
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6D), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('八音盒', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6A5")
    Event(0, 16)

    label("loc_6A5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6D), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('优雅衣镜', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6CC")
    Event(0, 15)

    label("loc_6CC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('咪雪玩偶', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6F3")
    Event(0, 18)

    label("loc_6F3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('影丸储蓄罐', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_71A")
    Event(0, 17)

    label("loc_71A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x74), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('小径自行车', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_741")
    Event(0, 20)

    label("loc_741")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x74), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('竞赛旗', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_768")
    Event(0, 19)

    label("loc_768")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x74), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13B, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_783")
    Event(0, 5)

    label("loc_783")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_82B")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x71), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('ＺＷＥＩ２企鹅', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7BB")
    Event(0, 21)

    label("loc_7BB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x71), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('苦番茄人玩偶', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7D7")
    Event(0, 21)

    label("loc_7D7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x71), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('黑泰迪熊', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7F3")
    Event(0, 21)

    label("loc_7F3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x71), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('波波靠垫', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_80F")
    Event(0, 21)

    label("loc_80F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x71), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('古怪靠垫', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_82B")
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
    Jump("loc_FB6")

    label("loc_CED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_DAA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19D, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D08")
    Call(0, 74)
    Jump("loc_DA5")

    label("loc_D08")


    ChrTalk(
        0x8,
        (
            "#01108FIf Noel ceases to exist\x01",
            "Keyaもサビしいけど……\x01",
            "Cheer up, Noeloo.\x02\x03",
            "#01102FWith the Frank who got better\x01",
            "I'm waiting for two people to come and play.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DA5")

    Jump("loc_FB6")

    label("loc_DAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_DB8")
    Jump("loc_FB6")

    label("loc_DB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_DD7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x170, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DD2")
    TalkEnd(0xFE)
    Call(0, 6)
    Return()

    label("loc_DD2")

    Jump("loc_FB6")

    label("loc_DD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_FB6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13E, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F4E")

    ChrTalk(
        0x8,
        "#01105FOh, are Lloyd 's going out?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000Fああ、Keyaは日曜学校の宿題か？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01100FYeah, I can not play outside today.\x01",
            "I thought about doing it first.\x02\x03",
            "#01106FIf that is true that car\x01",
            "I wanted to ride.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FWow, that's a pity.\x02\x03",
            "#10109FEven on a sunny day this time\x01",
            "Let's drive together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#01109FYup! I am looking forward to it.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x13E, 1)
    Jump("loc_FB6")

    label("loc_F4E")


    ChrTalk(
        0x8,
        (
            "#01109FWell, this time\x01",
            "I'm looking forward to a sunny day.\x02\x03",
            "#01110FWell, today is a crop\x01",
            "Do your homework!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FB6")

    TalkEnd(0xFE)
    Return()

    # Function_3_CDC end

    def Function_4_FBA(): pass

    label("Function_4_FBA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1086")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1065")

    ChrTalk(
        0xA,
        "#01203FGurururu …… won.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FZeitがノエルさんに\x01",
            "It seems to be \"good person.\"\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10109FHaha ……\x01",
            "ありがとう、Zeit君。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1086")

    label("loc_1065")


    ChrTalk(
        0xA,
        "#01203FGurururu …… won.\x02",
    )

    CloseMessageWindow()

    label("loc_1086")

    TalkEnd(0xFE)
    Return()

    # Function_4_FBA end

    def Function_5_108A(): pass

    label("Function_5_108A")

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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0xA4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1124")
    SetChrPos(0x1A5, 256209, 0, 125400, 0)

    label("loc_1124")

    OP_0D()

    ChrTalk(
        0x109,
        (
            "#12P#10100FWell, here is my room.\x02\x03",
            "#10106FI do not have much fun.\x01",
            "It's a bit embarrassing though ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300FHuh, leave it alone\x01",
            "I guess it's fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00102FYeah, it seems to be Noel\x01",
            "I think it's good.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0xA4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_131E")
    OP_93(0x1A5, 0x87, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x1A5,
        (
            "#5P#01105FDo not you have that over there\x01",
            "What is a bear?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1261():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1261)

    def lambda_126E():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_126E)
    Sleep(50)

    def lambda_127E():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_127E)
    Sleep(50)

    def lambda_128E():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_128E)
    WaitChrThread(0x109, 1)

    ChrTalk(
        0x109,
        (
            "#12P#10109FHaha ……\x01",
            "I have an Orange with Fran\x01",
            "It is a stuffed doll.\x02\x03",
            "#10100FI was putting it in the place of the guard\x01",
            "I brought it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_140E")

    label("loc_131E")

    OP_93(0x101, 0x87, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#5P#00000FThat, it's over there\x01",
            "A stuffed animal ……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1363():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1363)
    Sleep(50)

    def lambda_1373():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1373)
    Sleep(50)

    def lambda_1383():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1383)
    WaitChrThread(0x109, 1)

    ChrTalk(
        0x109,
        (
            "#12P#10109FHaha ……\x01",
            "I have an Orange with Fran\x01",
            "It is a stuffed animal.\x02\x03",
            "#10100FI was putting it in the place of the guard\x01",
            "I brought it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_140E")


    ChrTalk(
        0x101,
        (
            "#5P#00000FHaha, I see.\x01",
            "It looks good to be an accent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10100FHehe, thank you.\x02\x03",
            "#10104FWell, then again again ……\x01",
            "Although I am a bad person, thank you.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 256010, 0, 121130, 0)
    SetScenarioFlags(0x13B, 6)
    EventEnd(0x5)
    Return()

    # Function_5_108A end

    def Function_6_14DC(): pass

    label("Function_6_14DC")

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

    def lambda_1590():

        label("loc_1590")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_1590")

    QueueWorkItem2(0x101, 2, lambda_1590)

    def lambda_15A2():

        label("loc_15A2")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_15A2")

    QueueWorkItem2(0x102, 2, lambda_15A2)

    def lambda_15B4():

        label("loc_15B4")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_15B4")

    QueueWorkItem2(0x103, 2, lambda_15B4)

    def lambda_15C6():

        label("loc_15C6")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_15C6")

    QueueWorkItem2(0x104, 2, lambda_15C6)

    def lambda_15D8():

        label("loc_15D8")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_15D8")

    QueueWorkItem2(0x109, 2, lambda_15D8)

    def lambda_15EA():

        label("loc_15EA")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_15EA")

    QueueWorkItem2(0x105, 2, lambda_15EA)
    OP_0D()

    ChrTalk(
        0x8,
        "#11P#01110FOh, everyone ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#00200FKeya……大丈夫ですか？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00108FSince yesterday\x01",
            "I do not feel well, but ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#01102FWell, yeah.\x01",
            "Keyaは大丈夫だけど……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x8)

    ChrTalk(
        0x8,
        (
            "#11P#01103FHey Lloyd … ….\x02\x03",
            "#01108FAfter all the eye of Suzuku,\x01",
            "It's hard to heal … ….?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x170, 3)), scpexpr(EXPR_END)), "loc_17CF")

    ChrTalk(
        0x101,
        (
            "#6P#00003F…… Oh, it's difficult\x01",
            "I think there is no mistake.\x02\x03",
            "#00000FBut, Shizuku-chan\x01",
            "Even now I was positive.\x02\x03",
            "Far away,\x01",
            "The treatment has advanced\x01",
            "I was pleased.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1849")

    label("loc_17CF")


    ChrTalk(
        0x101,
        (
            "#6P#00003F…… Oh, it's difficult\x01",
            "I think there is no mistake.\x02\x03",
            "#00008FI took this surgery,\x01",
            "It is a failure\x01",
            "I heard that … …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1849")


    ChrTalk(
        0x8,
        "#11P#01106FI see……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00303FHey, Keibo.\x01",
            "I understand that it is depressed … …\x01",
            "How about going out soon?\x02\x03",
            "#00300FEven Shizuku-chan,\x01",
            "Kiyoshi falls in that way\x01",
            "You do not want it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10103Fそ、そうだよ、Keyaちゃん。\x02\x03",
            "#10102FKeyaちゃんが\x01",
            "It would be better if you were smiling,\x01",
            "I think Shizuku is also happy!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#01108F… Well, that's right.\x02\x03",
            "#01102FKeyaはシズクの親友だから……\x01",
            "I have to cheer you up next time I see you.\x02",
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
            "#11P#01109FThank you, everyone.\x01",
            "Keyaもちょっと元気でてきた。\x02\x03",
            "#01100FWell, I'm blowing away\x01",
            "I'm going out for fun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00005FOh, ah … … be careful.\x02",
    )

    CloseMessageWindow()
    OP_95(0x8, 252320, 0, 65790, 2000, 0x1)

    def lambda_1B04():
        OP_95(0xFE, 251280, 0, 65770, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1B04)

    def lambda_1B1E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1B1E)
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
        "#11P#10308F……Are you OK?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FI do not know but …\x01",
            "Keyaならすぐに\x01",
            "It will become healthy.\x02\x03",
            "#00000FWell then, shall we go?\x02",
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

    # Function_6_14DC end

    def Function_7_1C21(): pass

    label("Function_7_1C21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13B, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C33")
    Call(0, 13)
    Jump("loc_1C73")

    label("loc_1C33")

    TalkBegin(0xFF)

    ChrTalk(
        0x101,
        (
            "#00000FThis is the room of Tio.\x01",
            "Let's stop entering.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)

    label("loc_1C73")

    Return()

    # Function_7_1C21 end

    def Function_8_1C74(): pass

    label("Function_8_1C74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13B, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C86")
    Call(0, 14)
    Jump("loc_1CC8")

    label("loc_1C86")

    TalkBegin(0xFF)

    ChrTalk(
        0x101,
        (
            "#00000FThis is the room of Randy.\x01",
            "Let's stop entering.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)

    label("loc_1CC8")

    Return()

    # Function_8_1C74 end

    def Function_9_1CC9(): pass

    label("Function_9_1CC9")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000F……そういえば、Keyaが\x01",
            "I told you to go to Sunday school.\x02\x03",
            "The manager also went out,\x01",
            "You may as well go out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FWell, let's call out.\x02",
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 800, 0, 1890, 0)
    EventEnd(0x4)
    Return()

    # Function_9_1CC9 end

    def Function_10_1D86(): pass

    label("Function_10_1D86")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000F……そういえば、Keyaが\x01",
            "I told you to go to Sunday school.\x02\x03",
            "The manager also went out,\x01",
            "You may as well go out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FWell, let's call out.\x02",
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -2190, 0, 68010, 90)
    EventEnd(0x4)
    Return()

    # Function_10_1D86 end

    def Function_11_1E43(): pass

    label("Function_11_1E43")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000FKeyaはこれから日曜学校だ。\x01",
            "The back door is a shortcut.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -1330, 0, 71380, 268)
    EventEnd(0x4)
    Return()

    # Function_11_1E43 end

    def Function_12_1E9A(): pass

    label("Function_12_1E9A")

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
        "#00005Fthis is……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)

    ChrTalk(
        0x104,
        (
            "#12P#00302FOh, white stone?\x01",
            "Is not it pretty beautiful?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#11P#00205FThis is certain ……\x02\x03",
            "#00200FMr. Lloyd in Mishram\x01",
            "Keyaにプレゼントした……？\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x101)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#00006FOh, on the Michelin beach\x01",
            "Keyaにあげた『ホワイトストーン』だ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00108FKeyaちゃんが\x01",
            "I wonder if I forgot to place it … ….?\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd took Whitestone.\x07\x00\x02",
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
        "#00011F#30W………… Eh ………………\x02",
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
        "#00005F#40W……………………………………\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2420")

    ChrTalk(
        0x106,
        (
            "#11P#10708F#30WWell, now ……\x01",
            "Keyaちゃん……？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24A6")

    label("loc_2420")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_246B")

    ChrTalk(
        0x109,
        (
            "#11P#10113F#30WWell, now ……\x01",
            "Keyaちゃん……？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24A6")

    label("loc_246B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_24A6")

    ChrTalk(
        0x105,
        "#11P#10408F#30W今のは……Keya……？\x02",
    )

    CloseMessageWindow()

    label("loc_24A6")


    ChrTalk(
        0x104,
        (
            "#12P#00301F#30WIt must be a mistake.\x01",
            "…… But where … …?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            "#11P#00206F#30WTo that which Lloyd got,\x01",
            "Things like residual thought\x01",
            "I feel that it is included.\x02\x03",
            "#00208F…… sorrow and delusion\x01",
            "It seems like you pushed it in force ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00106F#30WKeyaちゃん……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2611")

    ChrTalk(
        0x10A,
        (
            "#11P#00608F#30W…… Completely ……\x01",
            "A child who was innocent in that Noh weather … …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26C2")

    label("loc_2611")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2668")

    ChrTalk(
        0x105,
        (
            "#11P#10408F#30W… …. Good luck.\x01",
            "A child who was innocent until that … …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26C2")

    label("loc_2668")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_26C2")

    ChrTalk(
        0x109,
        (
            "#11P#10106F#30W…… the thought so far\x01",
            "Keyaちゃんにさせてたなんて……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26C2")

    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#00006F#30W…… With this … ….\x01",
            "A piece of delusion was completely gone.\x02\x03",
            "#00015FKeyaがあんな……\x01",
            "With the feeling that I killed my heart\x01",
            "It was a while … ….\x02\x03",
            "#00010FThat situation is absolutely wrong!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00101FWell … that kind of\x01",
            "It can not be right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00307F……When it comes to this,\x01",
            "What makes everything quill\x01",
            "I have to get to it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#11P#00201Fええ、Keyaの笑顔を\x01",
            "To regain … ….!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00007FOh … let's go, everyone.\x02\x03",
            "#00003F（Keya……待っててくれ。\x01",
            "I will absolutely pick you up …! )\x02",
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
            scpstr(SCPSTR_CODE_ITEM, '零之神珠'),
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber('零之神珠', 1)
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AD, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BC, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DE, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D9, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DE, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2971")
    OP_E0(0x34, 0x0)

    label("loc_2971")

    EventEnd(0x5)
    Return()

    # Function_12_1E9A end

    def Function_13_2974(): pass

    label("Function_13_2974")

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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0xA4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2A0E")
    SetChrPos(0x1A5, 169520, 0, 61730, 0)

    label("loc_2A0E")

    OP_0D()

    ChrTalk(
        0x102,
        "#6P#00100FThis is Tio's room.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300FSurely now, in Les Autonomous states\x01",
            "Are you on a business trip?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FOh, with Jonah\x01",
            "Epstein Foundation's\x01",
            "I am going to the laboratory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00100FWith the amendment of the Autonomous State Law, the power net also\x01",
            "Diffusion is proceeding,\x01",
            "I guess that helped the relationship.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#11P#10103FI do not know the difficult thing ….\x01",
            "It seems quite tough.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0xA4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2BE2")

    ChrTalk(
        0x1A5,
        "#12P#01100FTio, I hope to get back soon.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FOh, really.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2C18")

    label("loc_2BE2")


    ChrTalk(
        0x101,
        (
            "#00000FOh, as soon as I return\x01",
            "I do not mind.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C18")

    OP_5A()
    SetChrPos(0x0, 169990, 0, 63110, 180)
    SetScenarioFlags(0x13B, 3)
    EventEnd(0x5)
    Return()

    # Function_13_2974 end

    def Function_14_2C30(): pass

    label("Function_14_2C30")

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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0xA4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2CCA")
    SetChrPos(0x1A5, 13500, 0, 61420, 0)

    label("loc_2CCA")

    OP_0D()

    ChrTalk(
        0x101,
        "#12P#00000FThis is Randy 's room.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FRandy is now,\x01",
            "With the troops of the Belgard gate\x01",
            "It is in the midst of rehabilitation training.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10305FOh, surely in a cult incident\x01",
            "Did you have the case of the example?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10103FYup……\x01",
            "Something terrible as sequelae\x01",
            "I do not remember.\x02\x03",
            "#10108FTo regain physical strength and can\x01",
            "It looks like it will take some time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003FReally……\x01",
            "I want the guard to recover quickly.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0xA4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2EB6")

    ChrTalk(
        0x1A5,
        "#12P#01100FI wonder if Randy will come back soon.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FHehe, really.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2EF4")

    label("loc_2EB6")


    ChrTalk(
        0x102,
        (
            "#00100FWell, Randy also\x01",
            "I want to get back soon.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2EF4")

    OP_5A()
    SetChrPos(0x0, 14040, 0, 63300, 180)
    SetScenarioFlags(0x13B, 4)
    EventEnd(0x5)
    Return()

    # Function_14_2C30 end

    def Function_15_2F0C(): pass

    label("Function_15_2F0C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    ClearMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x8, 0x2)
    OP_68(157620, 1330, 125080, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F66")
    SetChrFlags(0x0, 0x8)

    label("loc_2F66")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F79")
    SetChrFlags(0x1, 0x8)

    label("loc_2F79")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F8C")
    SetChrFlags(0x2, 0x8)

    label("loc_2F8C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F9F")
    SetChrFlags(0x3, 0x8)

    label("loc_2F9F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2FB2")
    SetChrFlags(0x4, 0x8)

    label("loc_2FB2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2FC5")
    SetChrFlags(0x5, 0x8)

    label("loc_2FC5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2FDE")
    ClearChrFlags(0x102, 0x80)
    ClearChrBattleFlags(0x102, 0x8000)

    label("loc_2FDE")

    ClearChrFlags(0x102, 0x8)
    SetChrPos(0x102, 157620, 30, 125080, 90)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x102,
        "#0100FI wonder if I can do it here.\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Sound(814, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "In the room of Eli\x01",
            "New furniture was added.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber('优雅衣镜', 1)
    SetScenarioFlags(0x13C, 6)
    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_66(0x2, 0x1)
    Call(0, 23)
    Call(0, 39)
    Call(0, 44)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_308F")
    ClearChrFlags(0x0, 0x8)

    label("loc_308F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_30A2")
    ClearChrFlags(0x1, 0x8)

    label("loc_30A2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_30B5")
    ClearChrFlags(0x2, 0x8)

    label("loc_30B5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_30C8")
    ClearChrFlags(0x3, 0x8)

    label("loc_30C8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_30DB")
    ClearChrFlags(0x4, 0x8)

    label("loc_30DB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_30EE")
    ClearChrFlags(0x5, 0x8)

    label("loc_30EE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_3107")
    SetChrFlags(0x102, 0x80)
    SetChrBattleFlags(0x102, 0x8000)

    label("loc_3107")

    SetChrPos(0x0, 155990, 30, 120980, 0)
    EventEnd(0x5)
    Return()

    # Function_15_2F0C end

    def Function_16_311B(): pass

    label("Function_16_311B")

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
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3187")
    SetChrFlags(0x0, 0x8)

    label("loc_3187")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_319A")
    SetChrFlags(0x1, 0x8)

    label("loc_319A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_31AD")
    SetChrFlags(0x2, 0x8)

    label("loc_31AD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_31C0")
    SetChrFlags(0x3, 0x8)

    label("loc_31C0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_31D3")
    SetChrFlags(0x4, 0x8)

    label("loc_31D3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_31E6")
    SetChrFlags(0x5, 0x8)

    label("loc_31E6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_31FF")
    ClearChrFlags(0x102, 0x80)
    ClearChrBattleFlags(0x102, 0x8000)

    label("loc_31FF")

    ClearChrFlags(0x102, 0x8)
    SetChrPos(0x102, 154920, 30, 122580, 0)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x102,
        "#0100FI wonder if I can do it here.\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Sound(814, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "In the room of Eli\x01",
            "New furniture was added.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber('八音盒', 1)
    SetScenarioFlags(0x13C, 7)
    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_66(0x3, 0x1)
    Call(0, 23)
    Call(0, 39)
    Call(0, 44)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_32B0")
    ClearChrFlags(0x0, 0x8)

    label("loc_32B0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_32C3")
    ClearChrFlags(0x1, 0x8)

    label("loc_32C3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_32D6")
    ClearChrFlags(0x2, 0x8)

    label("loc_32D6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_32E9")
    ClearChrFlags(0x3, 0x8)

    label("loc_32E9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_32FC")
    ClearChrFlags(0x4, 0x8)

    label("loc_32FC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_330F")
    ClearChrFlags(0x5, 0x8)

    label("loc_330F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_3328")
    SetChrFlags(0x102, 0x80)
    SetChrBattleFlags(0x102, 0x8000)

    label("loc_3328")

    SetChrPos(0x0, 155990, 30, 120980, 0)
    EventEnd(0x5)
    Return()

    # Function_16_311B end

    def Function_17_333C(): pass

    label("Function_17_333C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    ClearMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xA, 0x2)
    OP_68(206000, 1300, 129509, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3396")
    SetChrFlags(0x0, 0x8)

    label("loc_3396")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_33A9")
    SetChrFlags(0x1, 0x8)

    label("loc_33A9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_33BC")
    SetChrFlags(0x2, 0x8)

    label("loc_33BC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_33CF")
    SetChrFlags(0x3, 0x8)

    label("loc_33CF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_33E2")
    SetChrFlags(0x4, 0x8)

    label("loc_33E2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_33F5")
    SetChrFlags(0x5, 0x8)

    label("loc_33F5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_340E")
    ClearChrFlags(0x103, 0x80)
    ClearChrBattleFlags(0x103, 0x8000)

    label("loc_340E")

    ClearChrFlags(0x103, 0x8)
    SetChrPos(0x103, 206000, 0, 129509, 0)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x103,
        "#0200FHere it is good.\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Sound(814, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "In Tio's room\x01",
            "New furniture was added.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber('影丸储蓄罐', 1)
    SetScenarioFlags(0x13D, 0)
    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_66(0x4, 0x1)
    Call(0, 23)
    Call(0, 39)
    Call(0, 46)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_34C1")
    ClearChrFlags(0x0, 0x8)

    label("loc_34C1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_34D4")
    ClearChrFlags(0x1, 0x8)

    label("loc_34D4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_34E7")
    ClearChrFlags(0x2, 0x8)

    label("loc_34E7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_34FA")
    ClearChrFlags(0x3, 0x8)

    label("loc_34FA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_350D")
    ClearChrFlags(0x4, 0x8)

    label("loc_350D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3520")
    ClearChrFlags(0x5, 0x8)

    label("loc_3520")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_3539")
    SetChrFlags(0x103, 0x80)
    SetChrBattleFlags(0x103, 0x8000)

    label("loc_3539")

    SetChrPos(0x0, 206030, 30, 121140, 0)
    EventEnd(0x5)
    Return()

    # Function_17_333C end

    def Function_18_354D(): pass

    label("Function_18_354D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    ClearMapObjFlags(0xB, 0x4)
    SetMapObjFlags(0xB, 0x2)
    OP_68(208220, 1300, 123970, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_35A7")
    SetChrFlags(0x0, 0x8)

    label("loc_35A7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_35BA")
    SetChrFlags(0x1, 0x8)

    label("loc_35BA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_35CD")
    SetChrFlags(0x2, 0x8)

    label("loc_35CD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_35E0")
    SetChrFlags(0x3, 0x8)

    label("loc_35E0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_35F3")
    SetChrFlags(0x4, 0x8)

    label("loc_35F3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3606")
    SetChrFlags(0x5, 0x8)

    label("loc_3606")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_361F")
    ClearChrFlags(0x103, 0x80)
    ClearChrBattleFlags(0x103, 0x8000)

    label("loc_361F")

    ClearChrFlags(0x103, 0x8)
    SetChrPos(0x103, 208220, 0, 123970, 90)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x103,
        "#0200FHere it is good.\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Sound(814, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "In Tio's room\x01",
            "New furniture was added.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber('咪雪玩偶', 1)
    SetScenarioFlags(0x13D, 1)
    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_66(0x5, 0x1)
    Call(0, 23)
    Call(0, 39)
    Call(0, 46)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_36D2")
    ClearChrFlags(0x0, 0x8)

    label("loc_36D2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_36E5")
    ClearChrFlags(0x1, 0x8)

    label("loc_36E5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_36F8")
    ClearChrFlags(0x2, 0x8)

    label("loc_36F8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_370B")
    ClearChrFlags(0x3, 0x8)

    label("loc_370B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_371E")
    ClearChrFlags(0x4, 0x8)

    label("loc_371E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3731")
    ClearChrFlags(0x5, 0x8)

    label("loc_3731")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_374A")
    SetChrFlags(0x103, 0x80)
    SetChrBattleFlags(0x103, 0x8000)

    label("loc_374A")

    SetChrPos(0x0, 206030, 30, 121140, 0)
    EventEnd(0x5)
    Return()

    # Function_18_354D end

    def Function_19_375E(): pass

    label("Function_19_375E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    ClearMapObjFlags(0xC, 0x4)
    SetMapObjFlags(0xC, 0x2)
    OP_68(258329, 1300, 122180, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_37B8")
    SetChrFlags(0x0, 0x8)

    label("loc_37B8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_37CB")
    SetChrFlags(0x1, 0x8)

    label("loc_37CB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_37DE")
    SetChrFlags(0x2, 0x8)

    label("loc_37DE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_37F1")
    SetChrFlags(0x3, 0x8)

    label("loc_37F1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3804")
    SetChrFlags(0x4, 0x8)

    label("loc_3804")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3817")
    SetChrFlags(0x5, 0x8)

    label("loc_3817")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_3830")
    ClearChrFlags(0x109, 0x80)
    ClearChrBattleFlags(0x109, 0x8000)

    label("loc_3830")

    ClearChrFlags(0x109, 0x8)
    SetChrPos(0x109, 258329, 0, 122180, 90)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x109,
        "#10100FIt looks good here.\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Sound(814, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Noel's room\x01",
            "New furniture was added.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber('竞赛旗', 1)
    SetScenarioFlags(0x13D, 2)
    OP_50(0x68, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_66(0x6, 0x1)
    Call(0, 23)
    Call(0, 39)
    Call(0, 49)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_38E6")
    ClearChrFlags(0x0, 0x8)

    label("loc_38E6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_38F9")
    ClearChrFlags(0x1, 0x8)

    label("loc_38F9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_390C")
    ClearChrFlags(0x2, 0x8)

    label("loc_390C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_391F")
    ClearChrFlags(0x3, 0x8)

    label("loc_391F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3932")
    ClearChrFlags(0x4, 0x8)

    label("loc_3932")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3945")
    ClearChrFlags(0x5, 0x8)

    label("loc_3945")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_395E")
    SetChrFlags(0x109, 0x80)
    SetChrBattleFlags(0x109, 0x8000)

    label("loc_395E")

    SetChrPos(0x0, 256010, 0, 121130, 0)
    EventEnd(0x5)
    Return()

    # Function_19_375E end

    def Function_20_3972(): pass

    label("Function_20_3972")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    ClearMapObjFlags(0xD, 0x4)
    SetMapObjFlags(0xD, 0x2)
    OP_68(258149, 1300, 125700, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_39CC")
    SetChrFlags(0x0, 0x8)

    label("loc_39CC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_39DF")
    SetChrFlags(0x1, 0x8)

    label("loc_39DF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_39F2")
    SetChrFlags(0x2, 0x8)

    label("loc_39F2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3A05")
    SetChrFlags(0x3, 0x8)

    label("loc_3A05")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3A18")
    SetChrFlags(0x4, 0x8)

    label("loc_3A18")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3A2B")
    SetChrFlags(0x5, 0x8)

    label("loc_3A2B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_3A44")
    ClearChrFlags(0x109, 0x80)
    ClearChrBattleFlags(0x109, 0x8000)

    label("loc_3A44")

    ClearChrFlags(0x109, 0x8)
    SetChrPos(0x109, 258149, 0, 125700, 90)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x109,
        "#10100FIt looks good here.\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Sound(814, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Noel's room\x01",
            "New furniture was added.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber('小径自行车', 1)
    SetScenarioFlags(0x13D, 3)
    OP_50(0x68, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_66(0x7, 0x1)
    Call(0, 23)
    Call(0, 39)
    Call(0, 49)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3AFA")
    ClearChrFlags(0x0, 0x8)

    label("loc_3AFA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3B0D")
    ClearChrFlags(0x1, 0x8)

    label("loc_3B0D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3B20")
    ClearChrFlags(0x2, 0x8)

    label("loc_3B20")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3B33")
    ClearChrFlags(0x3, 0x8)

    label("loc_3B33")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3B46")
    ClearChrFlags(0x4, 0x8)

    label("loc_3B46")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3B59")
    ClearChrFlags(0x5, 0x8)

    label("loc_3B59")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_3B72")
    SetChrFlags(0x109, 0x80)
    SetChrBattleFlags(0x109, 0x8000)

    label("loc_3B72")

    SetChrPos(0x0, 256010, 0, 121130, 0)
    EventEnd(0x5)
    Return()

    # Function_20_3972 end

    def Function_21_3B86(): pass

    label("Function_21_3B86")

    EventBegin(0x0)
    SoundLoad(3668)
    SoundLoad(3669)
    SoundLoad(3670)
    SoundLoad(3671)
    FadeToDark(0, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3BB2")
    SetChrFlags(0x0, 0x8)

    label("loc_3BB2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3BC5")
    SetChrFlags(0x1, 0x8)

    label("loc_3BC5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3BD8")
    SetChrFlags(0x2, 0x8)

    label("loc_3BD8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3BEB")
    SetChrFlags(0x3, 0x8)

    label("loc_3BEB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3BFE")
    SetChrFlags(0x4, 0x8)

    label("loc_3BFE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3C11")
    SetChrFlags(0x5, 0x8)

    label("loc_3C11")

    SetChrFlags(0x8, 0x80)
    SetChrFlags(0xA, 0x80)
    SetMessageWindowPos(16, 150, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00000F(by the way……\x01",
            "  Keyaが喜びそうなぬいぐるみを\x01",
            "You got it. )\x02\x03",
            "(Let 's give it as soon as possible.\x02",
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
            "ロイドはKeyaを捜して\x01",
            "I gave a stuffed animal present.\x07\x00\x02",
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
            "#01100F#3668Vわあ、Keyaにくれるのー！？\x02\x03",
            "#3669VErr …\x01",
            "Lloyd, thank you ♪\x02",
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
            "#00000FHaha, you are welcome.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x9, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "GetItemNumber('古怪靠垫', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3DF4")
    SubItemNumber('古怪靠垫', 1)
    SetScenarioFlags(0x13D, 5)
    OP_50(0x64, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    ClearMapObjFlags(0xF, 0x4)
    SetMapObjFlags(0xF, 0x2)
    OP_66(0x9, 0x1)
    SetChrPos(0x9, 255500, 0, 68590, 89)
    OP_68(256000, 1300, 68810, 0)
    Call(0, 22)

    label("loc_3DF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "GetItemNumber('波波靠垫', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3E4A")
    SubItemNumber('波波靠垫', 1)
    SetScenarioFlags(0x13D, 4)
    OP_50(0x64, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    ClearMapObjFlags(0xE, 0x4)
    SetMapObjFlags(0xE, 0x2)
    OP_66(0x8, 0x1)
    SetChrPos(0x9, 255940, 30, 66720, 180)
    OP_68(256220, 1330, 66750, 0)
    Call(0, 22)

    label("loc_3E4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "GetItemNumber('黑泰迪熊', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3EA0")
    SubItemNumber('黑泰迪熊', 1)
    SetScenarioFlags(0x13D, 6)
    OP_50(0x64, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    ClearMapObjFlags(0x10, 0x4)
    SetMapObjFlags(0x10, 0x2)
    OP_66(0xA, 0x1)
    SetChrPos(0x9, 258089, 0, 67110, 89)
    OP_68(258310, 1300, 67080, 0)
    Call(0, 22)

    label("loc_3EA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "GetItemNumber('苦番茄人玩偶', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3EF6")
    SubItemNumber('苦番茄人玩偶', 1)
    SetScenarioFlags(0x13D, 7)
    OP_50(0x64, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    ClearMapObjFlags(0x11, 0x4)
    SetMapObjFlags(0x11, 0x2)
    OP_66(0xB, 0x1)
    SetChrPos(0x9, 255560, 30, 72720, 0)
    OP_68(255320, 1330, 72710, 0)
    Call(0, 22)

    label("loc_3EF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "GetItemNumber('ＺＷＥＩ２企鹅', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3F4C")
    SubItemNumber('ＺＷＥＩ２企鹅', 1)
    SetScenarioFlags(0x13E, 0)
    OP_50(0x64, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    ClearMapObjFlags(0x12, 0x4)
    SetMapObjFlags(0x12, 0x2)
    OP_66(0xC, 0x1)
    SetChrPos(0x9, 256500, 30, 63940, 89)
    OP_68(256850, 1330, 63910, 0)
    Call(0, 22)

    label("loc_3F4C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13E, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12D, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3F6D")
    Call(0, 51)

    label("loc_3F6D")

    SetMessageWindowPos(14, 280, 60, 3)
    EventEnd(0x6)
    NewScene("c0130", 112, 0, 0)
    IdleLoop()
    Return()

    # Function_21_3B86 end

    def Function_22_3F82(): pass

    label("Function_22_3F82")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F99")
    Sleep(1000)
    Jump("loc_3F9C")

    label("loc_3F99")

    Sleep(500)

    label("loc_3F9C")

    FadeToBright(500, 0)
    OP_0D()
    Sleep(500)
    OP_63(0x9, 0x0, 1700, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1000)
    OP_C9(0x0, 0x80000000)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_400A")

    ChrTalk(
        0x9,
        "#01100F#3670VOh, this is probably good.\x02",
    )

    Jump("loc_4034")

    label("loc_400A")


    ChrTalk(
        0x9,
        "#01100F#3671VHuh, is this kid here?\x02",
    )


    label("loc_4034")

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
            "Keyaの部屋に\x01",
            "New furniture was added.\x07\x00\x02",
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

    # Function_22_3F82 end

    def Function_23_40A8(): pass

    label("Function_23_40A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13B, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4104")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "When I get furniture items\x01",
            "You can put it in the support room 's room.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetScenarioFlags(0x13B, 7)

    label("loc_4104")

    Return()

    # Function_23_40A8 end

    def Function_24_4105(): pass

    label("Function_24_4105")

    OP_F4(0x3)
    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "To take a break here\x01",      # 0
            "quit\x01",              # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_418C")
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

    label("loc_418C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_41A8")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_41A8")

    Return()

    # Function_24_4105 end

    def Function_25_41AA(): pass

    label("Function_25_41AA")

    OP_F4(0x3)
    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "To take a break here\x01",      # 0
            "quit\x01",              # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4231")
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

    label("loc_4231")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_424D")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_424D")

    Return()

    # Function_25_41AA end

    def Function_26_424F(): pass

    label("Function_26_424F")

    OP_F4(0x3)
    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "To take a break here\x01",      # 0
            "quit\x01",              # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_42D6")
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

    label("loc_42D6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_42F2")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_42F2")

    Return()

    # Function_26_424F end

    def Function_27_42F4(): pass

    label("Function_27_42F4")

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
            "There is an elegant appearance.\x02",
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

    # Function_27_42F4 end

    def Function_28_43A7(): pass

    label("Function_28_43A7")

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
            "There is a music box.\x02",
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

    # Function_28_43A7 end

    def Function_29_4484(): pass

    label("Function_29_4484")

    PlayBGM("ed7591", 0)
    Sleep(19000)
    OP_1F()
    Return()

    # Function_29_4484 end

    def Function_30_448D(): pass

    label("Function_30_448D")

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
            "There is a piggy banker.\x02",
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

    # Function_30_448D end

    def Function_31_4544(): pass

    label("Function_31_4544")

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
            "There is Meeeeee.\x02",
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

    # Function_31_4544 end

    def Function_32_45FB(): pass

    label("Function_32_45FB")

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
            "There is a flag for the race.\x02",
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

    # Function_32_45FB end

    def Function_33_46B4(): pass

    label("Function_33_46B4")

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
            "There is a mini bell bike.\x02",
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

    # Function_33_46B4 end

    def Function_34_476B(): pass

    label("Function_34_476B")

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
            "There is a pom cushion.\x02",
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

    # Function_34_476B end

    def Function_35_4822(): pass

    label("Function_35_4822")

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
            "There is a strange cushion.\x02",
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

    # Function_35_4822 end

    def Function_36_48D9(): pass

    label("Function_36_48D9")

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
            "There is a black teddy bear.\x02",
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

    # Function_36_48D9 end

    def Function_37_498E(): pass

    label("Function_37_498E")

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
            "There is an annoyance for a while.\x02",
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

    # Function_37_498E end

    def Function_38_4A47(): pass

    label("Function_38_4A47")

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
            "There is ZWEI 2 penguin.\x02",
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

    # Function_38_4A47 end

    def Function_39_4B02(): pass

    label("Function_39_4B02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13E, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4B76")
    OP_E0(0x16, 0x0)

    label("loc_4B76")

    Return()

    # Function_39_4B02 end

    def Function_40_4B77(): pass

    label("Function_40_4B77")

    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Return()

    # Function_40_4B77 end

    def Function_41_4BA6(): pass

    label("Function_41_4BA6")

    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Return()

    # Function_41_4BA6 end

    def Function_42_4BD5(): pass

    label("Function_42_4BD5")

    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    Return()

    # Function_42_4BD5 end

    def Function_43_4C04(): pass

    label("Function_43_4C04")

    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    Return()

    # Function_43_4C04 end

    def Function_44_4C33(): pass

    label("Function_44_4C33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12C, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5844")
    FadeToDark(1000, 0, -1)
    OP_0D()
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis362.itp")
    CreatePortrait(1, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis363.itp")
    LoadChrToIndex("chr/ch00102.itc", 0x1E)
    SetChrChipByIndex(0x102, 0x1E)
    SetChrSubChip(0x102, 0x0)
    SetChrFlags(0x102, 0x4)
    SetChrPos(0x102, 155910, 200, 123440, 290)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_4CE5")
    ClearChrFlags(0x101, 0x80)
    ClearChrBattleFlags(0x101, 0x8000)

    label("loc_4CE5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_4CFE")
    ClearChrFlags(0x102, 0x80)
    ClearChrBattleFlags(0x102, 0x8000)

    label("loc_4CFE")

    StopBGM(0xBB8)
    SetChrName("")
    SetMessageWindowPos(14, 280, 60, 3)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "On that day, Lloyd's\x01",
            "Returning to the support section between support activities ----\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Take a regular contact with the headquarters\x01",
            "I decided to take a break each time.\x02",
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
        "#00104F…………………………………….\x02",
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
        "Voice of Lloyd",
        "#1PEllie, is it okay?\x02",
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
            "Yeah, come in.\x02",
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

    def lambda_4F00():

        label("loc_4F00")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_4F00")

    QueueWorkItem2(0x102, 2, lambda_4F00)
    OP_0D()
    Sound(103, 0, 100, 0)
    Sleep(500)

    def lambda_4F1C():
        OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4F1C)

    def lambda_4F31():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4F31)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x101, 2)
    TurnDirection(0x101, 0x102, 500)
    EndChrThread(0x102, 0x2)
    OP_6F(0x79)
    Sleep(200)

    ChrTalk(
        0x102,
        "#00100FDo you plan to leave soon?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FOh, I also have business contact from the headquarters\x01",
            "I did not have anything today.\x02\x03",
            "#00000FNot everyone has gathered yet\x01",
            "You do not have to hurry so fast.\x02",
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
            "#00005FAh……\x01",
            "Does it increase somewhat?\x02",
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
            "#00102FHuhu, like this\x01",
            "Living is living, right?\x02\x03",
            "#00104FWhen I get back to my parents' occasion\x01",
            "Books and accessories that you do not need\x01",
            "I'm carrying it ….\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetMessageWindowPos(280, 150, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00009FNo, compared to my room\x01",
            "You are cleaning up cleanly, are not you?\x02\x03",
            "#00000FEven though it increased\x01",
            "All that matches the room ……\x02",
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

    def lambda_51CF():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_51CF)
    Sleep(200)

    def lambda_51DF():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_51DF)
    Sleep(500)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)

    ChrTalk(
        0x101,
        (
            "#00005Fthat's……\x01",
            "Maybe it is a music box?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FHehe, that's right.\x02",
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
            "#00104FI was in the shop of Imelda\x01",
            "The place called Leevelt\x01",
            "Antique · music box ……\x02\x03",
            "#00100FBecause it was a nostalgic song\x01",
            "I just bought it.\x02\x03",
            "#00109F… … Would you like to ask a moment?\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(280, 150, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00000FOh, I do not care.\x02",
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
            "#00009F#1POh no ……\x01",
            "It sounds like a sigh.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x1)
    Sleep(200)

    ChrTalk(
        0x102,
        (
            "#00109FHehe, is not it?\x02\x03",
            "#00104FSpeaking of Empire's Lee Wert Company\x01",
            "It is famous as an instrument maker\x01",
            "The music box is also popular.\x02\x03",
            "#00100FI used to play this same song a long time ago\x01",
            "With a smaller number of valves\x01",
            "I had it … ….\x02\x03",
            "#00106FWhen I took it to the destination I went to study abroad\x01",
            "You lost it.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(
        0x101,
        (
            "#00005F#1PI see……\x02\x03",
            "#00006F(Maybe with your parents\x01",
            "I wonder if it was a memorable item …? )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FBecause it was already out of print\x01",
            "I was giving up … ….\x02\x03",
            "#00100FI arrived at Mr. Imelda\x01",
            "It was really good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#1PThat's right.\x02\x03",
            "#00002FHaha, that shop also\x01",
            "Sometimes it is useful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00109FHehe, that's right.\x02",
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

    def lambda_5712():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5712)
    Sleep(200)

    def lambda_5722():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5722)
    OP_6F(0x79)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    Sleep(500)

    ChrTalk(
        0x102,
        (
            "#00100FWell.\x01",
            "Let's go, Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F……Ah!\x02",
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
            "We have all of Eli's furniture!\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_5805")
    SetChrFlags(0x101, 0x80)
    SetChrBattleFlags(0x101, 0x8000)

    label("loc_5805")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_581E")
    SetChrFlags(0x102, 0x80)
    SetChrBattleFlags(0x102, 0x8000)

    label("loc_581E")

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

    label("loc_5844")

    Return()

    # Function_44_4C33 end

    def Function_45_5845(): pass

    label("Function_45_5845")

    PlayBGM("ed7591", 1)
    Sleep(19000)
    Return()

    # Function_45_5845 end

    def Function_46_584D(): pass

    label("Function_46_584D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6A0A")
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_5925")
    ClearChrFlags(0x101, 0x80)
    ClearChrBattleFlags(0x101, 0x8000)

    label("loc_5925")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_593E")
    ClearChrFlags(0x103, 0x80)
    ClearChrBattleFlags(0x103, 0x8000)

    label("loc_593E")

    StopBGM(0xBB8)
    SetChrName("")
    SetMessageWindowPos(14, 280, 60, 3)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "On that day, Lloyd's\x01",
            "Returning to the support section between support activities ----\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Take a regular contact with the headquarters\x01",
            "I decided to take a break each time.\x02",
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
        "Voice of Lloyd",
        "#1PTio, is it okay?\x02",
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
            "Please, Lloyd.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(205300, 1330, 124060, 1500)
    OP_6F(0x79)
    Sound(103, 0, 100, 0)
    Sleep(500)
    OP_68(205440, 1330, 124910, 2000)

    def lambda_5B03():
        OP_9B(0x0, 0xFE, 0x0, 0x125C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5B03)

    def lambda_5B18():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5B18)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x101, 2)
    TurnDirection(0x101, 0x103, 500)
    OP_6F(0x79)
    Sleep(500)

    ChrTalk(
        0x103,
        "#00200FWould you like to leave soon?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FOh, I also have business contact from the headquarters\x01",
            "I did not have anything today.\x02\x03",
            "#00000FNot everyone has gathered yet\x01",
            "You do not have to hurry so fast.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00204FNo, I can leave right away.\x02",
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
            "#00005FAh……\x01",
            "Does it increase somewhat?\x02",
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
            "#00204F…… A pretty good thing\x01",
            "I got it.\x02\x03",
            "#00202FAlso about character goods\x01",
            "Crossbell compared to neighboring countries\x01",
            "There is considerable advantage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FIn any case\x01",
            "Because it is a mecca's knee.\x02\x03",
            "#00004FThanks to the Michelin theme park\x01",
            "It seems that it is also spreading in neighboring countries … …\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(209440, 1330, 124760, 2500)
    MoveCamera(60, 25, 0, 2500)
    OP_6E(350, 2500)
    SetCameraDistance(20500, 2500)

    def lambda_5EDD():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5EDD)
    Sleep(200)

    def lambda_5EED():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5EED)
    OP_6F(0x79)
    Sleep(500)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x103, 1)
    Call(0, 40)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x86, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_60E9")
    SetMessageWindowPos(280, 150, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00005Fby the way……\x02\x03",
            "#00000FOnly that one pink color\x01",
            "I told you \"Mieee\".\x02\x03",
            "#00004FI guess that's my little sister.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetMessageWindowPos(16, 150, -1, -1)

    AnonymousTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00202FYes, somewhat tohosho older brother\x01",
            "Burning care while saying it can not be helped,\x01",
            "It is a very high-spec sister character.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetMessageWindowPos(280, 150, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00012FIs that so … ….\x01",
            "(What are you sistering with high spec?)\x02\x03",
            "#00005FWell then, then,\x01",
            "What is that blackish cat?\x02\x03",
            "#00000FCushion is also treated\x01",
            "Misato has nothing to do with you?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_62E8")

    label("loc_60E9")

    SetMessageWindowPos(280, 150, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00005Fby the way……\x02\x03",
            "#00000FOnly that pink color\x01",
            "What version is it?\x02",
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
            "#00206F…… Lloyd is not studying too hard.\x02\x03",
            "#00200FThat is not a misunderstanding,\x01",
            "He is his sister Mie.\x02\x03",
            "#00211FAs long as you are a crossbell agent\x01",
            "I have to know that much.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetMessageWindowPos(280, 150, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00006FI have nothing to do ……\x01",
            "(I do not think the investigator is involved.\x02\x03",
            "#00005FWell then, then,\x01",
            "What is that blackish cat?\x02\x03",
            "#00000FCushion is also treated\x01",
            "Misato has nothing to do with you?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_62E8")

    Call(0, 41)

    def lambda_62F0():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_62F0)
    Sleep(200)

    def lambda_6300():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6300)
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
            "#00202FThat is \"Kagemal\".\x02\x03",
            "#00204FRecently, of popular serial novels that came out\x01",
            "A cat kept by the hero … …\x02\x03",
            "#00200FWith cute cuteness\x01",
            "With a distinctive cry called Bunew\x01",
            "It is a character that is breaking.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetMessageWindowPos(280, 150, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00005FWell, was that so.\x02\x03",
            "#00003FBy the way, as a prize of a casino\x01",
            "It seems to be in.\x02\x03",
            "#00009FBut, Mitsui Kitto is nice and nice\x01",
            "It seems impossible to say honestly cute\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetMessageWindowPos(16, 150, -1, -1)

    AnonymousTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00211FGiroz.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetMessageWindowPos(280, 150, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00006FNo, there is nothing.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetMessageWindowPos(16, 150, -1, -1)

    AnonymousTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00206F… Well, I understand what I mean.\x02\x03",
            "#00200FMiss you, I can not say anything\x01",
            "Unique instability is selling\x01",
            "It is a so-called \"loose character\" … ….\x02\x03",
            "#00203FKagemalu is not that unfriendly\x01",
            "On the contrary it is an exquisite hook\x01",
            "Because it is a classic mascot character.\x02\x03",
            "#00200FIt is hard to say that it is cute with a straight ball\x01",
            "Naturally it is natural.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetMessageWindowPos(280, 150, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00005FI see……\x01",
            "It seems to be convincing.\x02",
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
            "#00000FBy the way, as Tio\x01",
            "Mitsite, Kagemalu's\x01",
            "Which do you like better?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x103,
        (
            "#00203F……………………………………\x02\x03",
            "#00211F… … Have you heard?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00011FWhat……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203FI do not want to answer\x01",
            "The problem I was turning away … …\x02\x03",
            "#00201FHave you finally heard?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012FUh, that, Mr. Tio …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203FRegarding this matter, even after dinner\x01",
            "Let 's discuss thoroughly.\x02\x03",
            "#00204F…… Lloyd.\x01",
            "Tonight is going to get hot …\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00006F(… … I wanted to read a book, but\x01",
            "I do not think we should just give up today. )\x02",
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
            "I got all the furniture of Tiio!\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_69C5")
    SetChrFlags(0x101, 0x80)
    SetChrBattleFlags(0x101, 0x8000)

    label("loc_69C5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_69DE")
    SetChrFlags(0x103, 0x80)
    SetChrBattleFlags(0x103, 0x8000)

    label("loc_69DE")

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

    label("loc_6A0A")

    Return()

    # Function_46_584D end

    def Function_47_6A0B(): pass

    label("Function_47_6A0B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6A64")
    SetChrSubChip(0x103, 0x0)
    Sleep(100)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6A36")
    Jump("Function_47_6A0B")

    label("loc_6A36")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6A4A")
    Jump("loc_6A64")

    label("loc_6A4A")

    SetChrSubChip(0x103, 0x1)
    Sleep(100)
    SetChrSubChip(0x103, 0x2)
    Sleep(100)
    SetChrSubChip(0x103, 0x1)
    Sleep(100)
    Jump("Function_47_6A0B")

    label("loc_6A64")

    Return()

    # Function_47_6A0B end

    def Function_48_6A65(): pass

    label("Function_48_6A65")

    Sound(804, 0, 100, 0)
    Sleep(500)
    Sound(939, 2, 70, 0)
    Sleep(1000)
    Sound(73, 0, 100, 0)
    OP_24(0x3AB)
    Return()

    # Function_48_6A65 end

    def Function_49_6A81(): pass

    label("Function_49_6A81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12D, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_75FD")
    FadeToDark(1000, 0, -1)
    OP_0D()
    LoadChrToIndex("chr/ch02902.itc", 0x1E)
    SetChrChipByIndex(0x109, 0x1E)
    SetChrSubChip(0x109, 0x0)
    SetChrFlags(0x109, 0x4)
    SetChrPos(0x109, 254080, 150, 127100, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_6ADB")
    ClearChrFlags(0x101, 0x80)
    ClearChrBattleFlags(0x101, 0x8000)

    label("loc_6ADB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_6AF4")
    ClearChrFlags(0x109, 0x80)
    ClearChrBattleFlags(0x109, 0x8000)

    label("loc_6AF4")

    StopBGM(0xBB8)
    SetChrName("")
    SetMessageWindowPos(14, 280, 60, 3)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "On that day, Lloyd's\x01",
            "Returning to the support section between support activities ----\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Take a regular contact with the headquarters\x01",
            "I decided to take a break each time.\x02",
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
            "#10100FEr …\x01",
            "Yeah, is it such a place?\x02",
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
        "Voice of Lloyd",
        "#1PNoel, is it a bit better?\x02",
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
            "Yes, it is okay!\x02",
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

    def lambda_6D09():
        OP_9B(0x0, 0xFE, 0x0, 0x1068, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6D09)

    def lambda_6D1E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6D1E)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x109, 1)
    OP_6F(0x79)
    Sleep(200)

    ChrTalk(
        0x109,
        "#10100FWould you like to leave soon?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FOh, I also have business contact from the headquarters\x01",
            "I did not have anything today.\x02\x03",
            "#00000FNot everyone has gathered yet\x01",
            "You do not have to hurry so fast.\x02",
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
        "#00005FWell, were you writing a report?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10109FHaha ……\x01",
            "Once in a while, it is a form of dispatching.\x02\x03",
            "#10100FReport on Sonya Command\x01",
            "I have submitted it once a week.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00009FI see, thank you very much.\x02",
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
            "#00005F#4PWell …!\x01",
            "Are there more interesting things?\x02\x03",
            "#00000FTo a bicycle … ….\x01",
            "Is this a race flag?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x109, 0x101, 500)

    ChrTalk(
        0x109,
        "#10102FOh … Do you understand? Is it?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x109, 500)

    ChrTalk(
        0x101,
        (
            "#00000F#4POh, I also had about 2 years\x01",
            "I lived in the Republic.\x02\x03",
            "#00004FFrom here over there\x01",
            "I often saw my bicycle ……\x02\x03",
            "#00000FA race that uses a powertrain\x01",
            "Occasionally it was held?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10109FOh yeah, that's right!\x02\x03",
            "#10104F…… Actually my deceased father\x01",
            "I like that kind of person.\x02\x03",
            "#10100FWhen I was little I looked at the race\x01",
            "Take me to the Republic for a rail trip\x01",
            "There was something I gave you.\x02\x03",
            "#10102FBecause the work of the guard was busy\x01",
            "It was really only once … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#4PI see……\x02\x03",
            "#00000FWell then, Noel's guide likes cars\x01",
            "Is it from that time?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10109FHaha … … It is a matter of mind.\x02\x03",
            "#10100FIf you get a holiday\x01",
            "We would like to invite you to a\x01",
            "I'd like to go see it ….\x02\x03",
            "#10106FI do not have such a time to go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009F#4PHaha, each other.\x02\x03",
            "#00004F(Not only if you look at Noel\x01",
            "It seems I can participate in the race … …)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xFFFF)

    ChrTalk(
        0x101,
        (
            "#00003F#4PAnyway to the race ……\x02\x03",
            "#00002FOn the bicycle,\x01",
            "If there is a recommended model\x01",
            "Will not you tell me this time?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x109,
        "#10105FHuh……?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009F#4PNo, when I was over there,\x01",
            "A friend you got acquainted is on board\x01",
            "I was a bit curious.\x02\x03",
            "#00000FAlso like holiday cycling\x01",
            "I think I can go out and how about it?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x109,
        (
            "#10100FGood, I think it is good!\x02\x03",
            "#10104FIt's convenient and it will be exercise,\x01",
            "It's so much fun than anything!\x02\x03",
            "#10109FNext time, it is in my parents house\x01",
            "I will bring you a catalog!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00009F#4PHello, I beg you.\x02",
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
            "I got all the furniture of Noel!\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_75C6")
    SetChrFlags(0x101, 0x80)
    SetChrBattleFlags(0x101, 0x8000)

    label("loc_75C6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_75DF")
    SetChrFlags(0x109, 0x80)
    SetChrBattleFlags(0x109, 0x8000)

    label("loc_75DF")

    OP_49()
    OP_D7(0x1E)
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x12D, 1)
    OP_50(0x68, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    EventEnd(0x6)
    NewScene("c0130", 115, 0, 0)
    IdleLoop()

    label("loc_75FD")

    Return()

    # Function_49_6A81 end

    def Function_50_75FE(): pass

    label("Function_50_75FE")

    OP_95(0xFE, 255870, 0, 124760, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_50_75FE end

    def Function_51_761A(): pass

    label("Function_51_761A")

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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_76CE")
    ClearChrFlags(0x101, 0x80)
    ClearChrBattleFlags(0x101, 0x8000)

    label("loc_76CE")

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
        "Voice of Lloyd",
        "#2PKeya、ちょっといいか？\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x9, 0x1)
    Sleep(500)

    ChrTalk(
        0x9,
        (
            "#01100FOh, Lloyd!\x01",
            "OK.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(254320, 1330, 66480, 2000)
    MoveCamera(45, 23, 0, 2000)
    Sound(103, 0, 100, 0)
    Sleep(500)

    def lambda_77EC():
        OP_9B(0x0, 0xFE, 0x0, 0xA28, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_77EC)

    def lambda_7801():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7801)
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
            "#00005FOops ……\x01",
            "It seems she decorated it.\x02\x03",
            "#00009FWell, when you look like this\x01",
            "It's pretty spectacular.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#01109FErr …\x01",
            "Everyone is cute!\x02\x03",
            "#01111FAh, but …\x02",
        )
    )

    CloseMessageWindow()

    def lambda_78D7():

        label("loc_78D7")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_78D7")

    QueueWorkItem2(0x101, 1, lambda_78D7)
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
            "#01110F#5PThis child, Hontou\x01",
            "It's not a stuffed doll.\x02\x03",
            "#01100F\"Crispy\", put it inside\x01",
            "You wrote it in the case?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_79EC():

        label("loc_79EC")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_79EC")

    QueueWorkItem2(0x9, 1, lambda_79EC)
    BeginChrThread(0x101, 1, 0, 53)
    OP_68(257690, 1300, 64489, 2000)
    MoveCamera(60, 24, 0, 2000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x86, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_7A97")

    ChrTalk(
        0x101,
        (
            "#00005F#2PCostume ……\x01",
            "Is it the same as Missi?\x02\x03",
            "#00003Fなるほど、Keyaくらいの\x01",
            "It seems likely to be a child.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7B02")

    label("loc_7A97")


    ChrTalk(
        0x101,
        (
            "#00005F#2PCrocodile …\x01",
            "Oh, \"Costumes\"?\x02\x03",
            "#00003Fなるほど、Keyaくらいの\x01",
            "It seems likely to be a child.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7B02")

    WaitChrThread(0x101, 1)
    EndChrThread(0x9, 0x1)
    OP_6F(0x79)

    ChrTalk(
        0x9,
        (
            "#01105FOh, then then …\x02\x03",
            "#01109FKeya、中に入ってみるから\x01",
            "Can you help me?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x9, 500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x86, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_7BE8")

    ChrTalk(
        0x101,
        (
            "#00005F#2PIt's good, but……\x01",
            "I think you are pretty hot?\x02\x03",
            "#00012FWhen I used a substitute for Mitsushi before\x01",
            "I also became hello hello.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7C55")

    label("loc_7BE8")


    ChrTalk(
        0x101,
        (
            "#00005F#2PIt's good, but……\x01",
            "I think you are pretty hot?\x02\x03",
            "#00003FThis kind of fairly steaming\x01",
            "I have read something in some way.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7C55")


    ChrTalk(
        0x9,
        (
            "#01100FHmm, Maybe.\x02\x03",
            "#01109FAnd to Lloyd\x01",
            "I just want you to see it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#2POooh … I got it.\x02\x03",
            "#00004F(Well, that is scary,\x01",
            "It seems to be a serious thing in the future. )\x02",
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
            "#00004FAlright … this is fine with this.\x02\x03",
            "#00000FKeya、苦しくないか？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Well, hey kee.\x02\x03",
            "Suspend it\x01",
            "Is not it so hot?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FWow … … breathable\x01",
            "Are you thinking quite a bit?\x02",
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
        "Keyaペンギン",
        "Shazam!\x02",
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
            "#00011F#5SOhhhh! Is it?\x02\x03",
            "#00009F#3SWhat is it …?\x01",
            "Awesome cute …\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0xB, 255000, 0, 71000, 315)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8)

    NpcTalk(
        0xB,
        "Keyaペンギン",
        "#1PWell, oh?\x02",
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
        "Keyaペンギン",
        (
            "#1P#3672VHello.\x02\x03",
            "#3673VThank you for your consideration.\x02",
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
            "#00011FHuh …!\x01",
            "(This is a terrible destructive power …!\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_8178")
    ClearChrFlags(0x103, 0x80)
    ClearChrBattleFlags(0x103, 0x8000)

    label("loc_8178")

    SetChrPos(0x102, 250000, 0, 64000, 90)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x102, 0x8)
    SetChrFlags(0x102, 0x40)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_81B7")
    ClearChrFlags(0x102, 0x80)
    ClearChrBattleFlags(0x102, 0x8000)

    label("loc_81B7")


    NpcTalk(
        0x102,
        "Ely's voice",
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
        "Voice of Tio",
        (
            "#2PBecause I do not come back easily\x01",
            "I came to call you ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FOh, oh, I'm sorry to keep you waiting.\x02\x03",
            "#00004FThat … … after preparing your heart\x01",
            "Come inside.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x102,
        "Ely's voice",
        "#2PIs it? Is it? Is it?\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x103,
        "Voice of Tio",
        "#2PPreparation of the mind …?\x02",
    )

    CloseMessageWindow()
    Sound(103, 0, 100, 0)
    Sleep(500)
    SetChrPos(0x102, 251210, 0, 65690, 90)

    def lambda_831C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_831C)
    BeginChrThread(0x102, 1, 0, 55)
    Sleep(500)
    SetChrPos(0x103, 251210, 0, 65690, 90)

    def lambda_8347():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_8347)
    BeginChrThread(0x103, 1, 0, 56)

    ChrTalk(
        0x102,
        "#00100F#2PWhat on earth were you--\x02",
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
        "#00105F#2PWhat……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00205F#3P#N……………………… (pleasant)\x02",
    )

    CloseMessageWindow()
    OP_93(0x9, 0xE1, 0x1F4)

    NpcTalk(
        0x9,
        "Keyaペンギン",
        (
            "Ah, it is Eli and Tio.\x02\x03",
            "How are you?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8460():
        OP_A6(0xFE, 0x0, 0x14, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8460)
    Sleep(20)

    def lambda_847C():
        OP_A6(0xFE, 0x0, 0x14, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_847C)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#00105FWhat#500W,#40WWhat#500W,#40WI\x02",
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    ChrTalk(
        0x103,
        "#00201F#3P#N#5SThis is a case …!\x02",
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
        "#00011F#4P#10AA whip\x02",
    )

    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    Sleep(500)
    Sound(898, 0, 100, 0)

    def lambda_858C():
        OP_A6(0xFE, 0x0, 0x14, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_858C)
    Sleep(20)

    def lambda_85A8():
        OP_A6(0xFE, 0x0, 0x14, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_85A8)
    Sleep(20)

    def lambda_85C4():
        OP_A6(0xFE, 0x0, 0x14, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_85C4)
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
            "#00114FOr, it is cute!\x01",
            "カワイイわKeyaちゃん！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00204FOh, it can not be … …\x02\x03",
            "#00201FThis kind of thing in this dimension\x01",
            "It should be able to exist …!\x02",
        )
    )

    CloseMessageWindow()
    Sound(898, 0, 100, 0)

    def lambda_8689():
        OP_A6(0xFE, 0x0, 0x14, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8689)
    Sleep(20)

    def lambda_86A5():
        OP_A6(0xFE, 0x0, 0x14, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_86A5)
    Sleep(20)

    def lambda_86C1():
        OP_A6(0xFE, 0x0, 0x14, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_86C1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x9, 1)

    NpcTalk(
        0x9,
        "Keyaペンギン",
        (
            "It is painful, …\x02\x03",
            "Do not hold me so tight\x01",
            "I want it ……\x02",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8B13")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_87A3")
    ClearChrFlags(0x104, 0x80)
    ClearChrBattleFlags(0x104, 0x8000)

    label("loc_87A3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_87BC")
    ClearChrFlags(0x109, 0x80)
    ClearChrBattleFlags(0x109, 0x8000)

    label("loc_87BC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_87D5")
    ClearChrFlags(0x105, 0x80)
    ClearChrBattleFlags(0x105, 0x8000)

    label("loc_87D5")

    ClearChrFlags(0x109, 0x8)
    SetChrFlags(0x109, 0x40)
    SetChrPos(0x109, 251210, 0, 65690, 90)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_8800():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_8800)
    BeginChrThread(0x109, 1, 0, 57)
    Sleep(500)
    ClearChrFlags(0x104, 0x8)
    SetChrFlags(0x104, 0x40)
    SetChrPos(0x104, 251210, 0, 65690, 90)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_8840():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_8840)
    BeginChrThread(0x104, 1, 0, 58)
    Sleep(500)
    ClearChrFlags(0x105, 0x8)
    SetChrFlags(0x105, 0x40)
    SetChrPos(0x105, 251210, 0, 65690, 90)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_8880():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_8880)
    BeginChrThread(0x105, 1, 0, 56)

    ChrTalk(
        0x104,
        "#00305FWhat a noise! - what! Is it?\x02",
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
            "#10105F#12Pキ、Keyaちゃん！？\x02\x03",
            "#10109FWow Aaaaa!\x01",
            "Please let me hug you!\x02",
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
        "#00011F#4P#10AAdvertisement\x02",
    )

    WaitChrThread(0x109, 1)
    Sleep(500)
    Sound(898, 0, 100, 0)

    def lambda_89A0():
        OP_A6(0xFE, 0x0, 0x14, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_89A0)
    Sleep(20)

    def lambda_89BC():
        OP_A6(0xFE, 0x0, 0x14, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_89BC)
    Sleep(20)

    def lambda_89D8():
        OP_A6(0xFE, 0x0, 0x14, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_89D8)
    Sleep(20)

    def lambda_89F4():
        OP_A6(0xFE, 0x0, 0x14, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_89F4)
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
            "#10304F#6PFuh, it's a calamity.\x02\x03",
            "#10309FIt certainly is impossible\x01",
            "I think that it is a heinous cute.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309F#6PDisagreeable~!\x01",
            "If it appears seriously on the battlefield\x01",
            "Do not panic! Is it?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    TurnDirection(0x104, 0x9, 500)
    TurnDirection(0x105, 0x9, 500)
    Jump("loc_8CB2")

    label("loc_8B13")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_8B2C")
    ClearChrFlags(0x104, 0x80)
    ClearChrBattleFlags(0x104, 0x8000)

    label("loc_8B2C")

    ClearChrFlags(0x104, 0x8)
    SetChrFlags(0x104, 0x40)
    SetChrPos(0x104, 251210, 0, 65690, 90)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_8B57():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_8B57)
    BeginChrThread(0x104, 1, 0, 56)
    Sleep(500)

    ChrTalk(
        0x104,
        "#00305FWhat a noise! - what! Is it?\x02",
    )

    CloseMessageWindow()
    OP_6F(0x79)
    Sound(898, 0, 100, 0)

    def lambda_8BA8():
        OP_A6(0xFE, 0x0, 0x14, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8BA8)
    Sleep(20)

    def lambda_8BC4():
        OP_A6(0xFE, 0x0, 0x14, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8BC4)
    Sleep(20)

    def lambda_8BE0():
        OP_A6(0xFE, 0x0, 0x14, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_8BE0)
    OP_68(253160, 1330, 67480, 2000)
    OP_95(0x104, 253400, 0, 68000, 2000, 0x0)
    TurnDirection(0x104, 0x9, 500)
    Sleep(500)
    WaitChrThread(0x104, 1)
    OP_6F(0x79)

    ChrTalk(
        0x104,
        (
            "#00303F#6PHey hey, I can not do it\x01",
            "It's cowardly cute …! Is it?\x02\x03",
            "#00309FIf it appears seriously on the battlefield\x01",
            "Do not panic! Is it?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8CB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8CE0")
    Sleep(500)
    SetChrSubChip(0x101, 0x0)
    Sleep(750)
    Fade(500)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0x101, 0xFF)
    OP_0D()
    TurnDirection(0x101, 0x9, 500)
    Sleep(500)

    label("loc_8CE0")


    ChrTalk(
        0x101,
        (
            "#00012FHahaha ……\x01",
            "(It may not be a chalet … …)\x02",
        )
    )

    CloseMessageWindow()
    OP_68(254320, 1330, 68620, 2000)
    Sound(898, 0, 100, 0)

    def lambda_8D34():
        OP_A6(0xFE, 0x0, 0x14, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8D34)
    Sleep(20)

    def lambda_8D50():
        OP_A6(0xFE, 0x0, 0x14, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8D50)
    Sleep(20)

    def lambda_8D6C():
        OP_A6(0xFE, 0x0, 0x14, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_8D6C)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8DA6")
    Sleep(20)

    def lambda_8D92():
        OP_A6(0xFE, 0x0, 0x14, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_8D92)

    label("loc_8DA6")

    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x9, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8DC0")
    WaitChrThread(0x109, 1)

    label("loc_8DC0")

    OP_63(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_6F(0x79)
    Sleep(200)

    NpcTalk(
        0x9,
        "Keyaペンギン",
        (
            "Authority ……\x01",
            "This is ……\x02\x03",
            "そろそろゆるしてI want it ……\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(22000, 2500)
    FadeToDark(2000, 0, -1)
    Sound(898, 0, 100, 0)

    def lambda_8E50():
        OP_A6(0xFE, 0x0, 0x14, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8E50)
    Sleep(20)

    def lambda_8E6C():
        OP_A6(0xFE, 0x0, 0x14, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8E6C)
    Sleep(20)

    def lambda_8E88():
        OP_A6(0xFE, 0x0, 0x14, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_8E88)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8EC2")
    Sleep(20)

    def lambda_8EAE():
        OP_A6(0xFE, 0x0, 0x14, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_8EAE)

    label("loc_8EC2")

    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x9, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8EDC")
    WaitChrThread(0x109, 1)

    label("loc_8EDC")

    OP_0D()
    OP_64(0x9)
    SetChrName("")
    SetMessageWindowPos(14, 280, 60, 3)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "── After that, the female members\x01",
            "After a while it finally returned to me ……\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "あまりの危険さゆえに、Keyaペンギンは\x01",
            "It became the rule of strict prohibition afterwards.\x02",
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
            "Keyaに全てのぬいぐるみを贈った！\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_8FFB")
    SetChrFlags(0x101, 0x80)
    SetChrBattleFlags(0x101, 0x8000)

    label("loc_8FFB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_9014")
    SetChrFlags(0x102, 0x80)
    SetChrBattleFlags(0x102, 0x8000)

    label("loc_9014")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_902D")
    SetChrFlags(0x103, 0x80)
    SetChrBattleFlags(0x103, 0x8000)

    label("loc_902D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_9046")
    SetChrFlags(0x109, 0x80)
    SetChrBattleFlags(0x109, 0x8000)

    label("loc_9046")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_905F")
    SetChrFlags(0x104, 0x80)
    SetChrBattleFlags(0x104, 0x8000)

    label("loc_905F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_9078")
    SetChrFlags(0x105, 0x80)
    SetChrBattleFlags(0x105, 0x8000)

    label("loc_9078")

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

    # Function_51_761A end

    def Function_52_909F(): pass

    label("Function_52_909F")

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

    # Function_52_909F end

    def Function_53_90EE(): pass

    label("Function_53_90EE")

    OP_95(0xFE, 255000, 30, 64379, 2000, 0x1)
    OP_95(0xFE, 256640, 30, 64000, 2000, 0x0)
    Return()

    # Function_53_90EE end

    def Function_54_9117(): pass

    label("Function_54_9117")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_91B5")
    SetChrSubChip(0xFE, 0x1)
    Sleep(150)
    SetChrSubChip(0xFE, 0x2)
    Sleep(150)
    SetChrSubChip(0xFE, 0x1)
    Sleep(150)
    SetChrSubChip(0xFE, 0x0)
    Sleep(150)

    label("loc_913E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9155")
    Sleep(150)
    Jump("loc_913E")

    label("loc_9155")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9169")
    Jump("loc_91B5")

    label("loc_9169")

    SetChrSubChip(0xFE, 0x3)
    Sleep(150)
    SetChrSubChip(0xFE, 0x4)
    Sleep(150)
    SetChrSubChip(0xFE, 0x3)
    Sleep(150)
    SetChrSubChip(0xFE, 0x0)
    Sleep(150)

    label("loc_9185")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_919C")
    Sleep(150)
    Jump("loc_9185")

    label("loc_919C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_91B0")
    Jump("loc_91B5")

    label("loc_91B0")

    Jump("Function_54_9117")

    label("loc_91B5")

    Return()

    # Function_54_9117 end

    def Function_55_91B6(): pass

    label("Function_55_91B6")

    OP_9B(0x0, 0xFE, 0x0, 0xA28, 0x7D0, 0x0)
    TurnDirection(0xFE, 0x9, 0)
    Return()

    # Function_55_91B6 end

    def Function_56_91CD(): pass

    label("Function_56_91CD")

    OP_9B(0x0, 0xFE, 0x0, 0x640, 0x7D0, 0x0)
    TurnDirection(0xFE, 0x9, 0)
    Return()

    # Function_56_91CD end

    def Function_57_91E4(): pass

    label("Function_57_91E4")

    OP_9B(0x0, 0xFE, 0xFFF6, 0xBB8, 0x7D0, 0x0)
    TurnDirection(0xFE, 0x9, 0)
    Return()

    # Function_57_91E4 end

    def Function_58_91FB(): pass

    label("Function_58_91FB")

    OP_9B(0x0, 0xFE, 0xA, 0xBB8, 0x7D0, 0x0)
    TurnDirection(0xFE, 0x9, 0)
    Return()

    # Function_58_91FB end

    def Function_59_9212(): pass

    label("Function_59_9212")

    OP_95(0xFE, 255390, 30, 69100, 5000, 0x0)
    OP_93(0xFE, 0x0, 0x0)
    Return()

    # Function_59_9212 end

    def Function_60_922E(): pass

    label("Function_60_922E")

    OP_95(0xFE, 254730, 30, 69610, 5000, 0x0)
    OP_93(0xFE, 0x5A, 0x0)
    Return()

    # Function_60_922E end

    def Function_61_924A(): pass

    label("Function_61_924A")

    OP_95(0xFE, 254620, 30, 68940, 5000, 0x0)
    OP_93(0xFE, 0x2D, 0x0)
    Return()

    # Function_61_924A end

    def Function_62_9266(): pass

    label("Function_62_9266")

    SetChrChipByIndex(0xFE, 0xFF)

    def lambda_926F():
        OP_9D(0xFE, 0x3E800, 0x0, 0x1084C, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_926F)
    BeginChrThread(0xFE, 3, 0, 64)
    WaitChrThread(0xFE, 2)
    EndChrThread(0xFE, 0x3)
    OP_93(0xFE, 0x10E, 0x0)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_62_9266 end

    def Function_63_92A5(): pass

    label("Function_63_92A5")

    SetChrChipByIndex(0xFE, 0xFF)

    def lambda_92AE():
        OP_9D(0xFE, 0x3E8C8, 0x0, 0x109DC, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_92AE)
    BeginChrThread(0xFE, 3, 0, 64)
    WaitChrThread(0xFE, 2)
    EndChrThread(0xFE, 0x3)
    OP_93(0xFE, 0x10E, 0x0)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    Sleep(50)
    SetChrSubChip(0xFE, 0x3)
    Return()

    # Function_63_92A5 end

    def Function_64_92EB(): pass

    label("Function_64_92EB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9317")
    OP_93(0xFE, 0x10E, 0x3E8)
    OP_93(0xFE, 0x0, 0x3E8)
    OP_93(0xFE, 0x5A, 0x3E8)
    OP_93(0xFE, 0xB4, 0x3E8)
    Jump("Function_64_92EB")

    label("loc_9317")

    Return()

    # Function_64_92EB end

    def Function_65_9318(): pass

    label("Function_65_9318")

    OP_95(0xFE, 254750, 30, 67380, 2000, 0x0)
    TurnDirection(0xFE, 0x101, 500)
    Return()

    # Function_65_9318 end

    def Function_66_9334(): pass

    label("Function_66_9334")

    OP_95(0xFE, 254770, 30, 66380, 2000, 0x1)
    OP_95(0xFE, 255780, 30, 66850, 2000, 0x0)
    TurnDirection(0xFE, 0x101, 500)
    Return()

    # Function_66_9334 end

    def Function_67_9364(): pass

    label("Function_67_9364")

    OP_95(0xFE, 254550, 30, 67480, 2000, 0x0)
    TurnDirection(0xFE, 0x101, 500)
    Return()

    # Function_67_9364 end

    def Function_68_9380(): pass

    label("Function_68_9380")

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
            "#01111F#3657V#11P#40WUm, to this formula\x01",
            "Substituting this value …\x02",
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
        "#01109F#3039V#11P#30W#4S─ ─ Yeah! I can do it!\x02",
    )

    CloseMessageWindow()
    OP_24(0xBDF)
    OP_C9(0x1, 0x80000000)
    Sleep(300)
    Sound(808, 0, 100, 0)
    Sleep(1000)

    NpcTalk(
        0x101,
        "Voice of Lloyd",
        "Keya？\x02",
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
        "#01110F#3660V#5P#15A#30WOh, Lloyd.\x02",
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    OP_6F(0x79)
    WaitChrThread(0x101, 3)

    ChrTalk(
        0x101,
        (
            "#00005F#11PKeya、確か今日は\x01",
            "Should I have a Sunday school?\x02\x03",
            "#00000FIs it okay not to go out?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#01105F#5POh, yeah.\x01",
            "It may be time to meet again.\x02\x03",
            "#01100FDoes everyone also go to work?\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x102, 3)
    WaitChrThread(0x109, 3)
    WaitChrThread(0x105, 3)

    ChrTalk(
        0x102,
        (
            "#12P#00109FYes.\x01",
            "I thought about going out together.\x02\x03",
            "#00105FOh……\x01",
            "You were preparing for Sunday School?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#01109F#5PWell, sort of like that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10102F#12PKeyaちゃん、偉いなぁ。\x02\x03",
            "#10106FSunday School's preparation\x01",
            "I guess I did not do much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10304FHuh, I would rather say\x01",
            "I guess most of the time I did not attend class.\x02\x03",
            "#10302FFrom being taught by a bad priest\x01",
            "It is more efficient to study by yourself.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_984F():
        TurnDirection(0x101, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_984F)
    Sleep(150)

    def lambda_985F():
        TurnDirection(0x102, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_985F)
    Sleep(150)

    def lambda_986F():
        TurnDirection(0x109, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_986F)
    Sleep(150)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x109, 0)

    def lambda_988B():

        label("loc_988B")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_988B")

    QueueWorkItem2(0x101, 2, lambda_988B)

    def lambda_989D():

        label("loc_989D")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_989D")

    QueueWorkItem2(0x102, 2, lambda_989D)

    def lambda_98AF():

        label("loc_98AF")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_98AF")

    QueueWorkItem2(0x109, 2, lambda_98AF)

    ChrTalk(
        0x101,
        "#5P#00001FWasi, that … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00111F#11PKeyaちゃんに悪影響を\x01",
            "I do not want to give it ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#01100F#5PBarking?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10304FHuh, the fathers are angry.\x02\x03",
            "#10305F……that?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_997C():
        OP_95(0xFE, 253000, 30, 69300, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_997C)
    WaitChrThread(0x105, 1)
    Sleep(300)

    ChrTalk(
        0x105,
        "#6P#10301F………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#11PWadi\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#01105F#5PHmm, what's the matter?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10304FAs expected, Cross Bell\x01",
            "I thought that it is progressing a lot.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x105,
        "#6P#10300FCan not you go out more than that?\x02",
    )

    CloseMessageWindow()
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x109, 0x2)

    ChrTalk(
        0x101,
        "#00000F#11PThat's right.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x153, 500)

    def lambda_9AA5():

        label("loc_9AA5")

        TurnDirection(0xFE, 0x153, 500)
        Yield()
        Jump("loc_9AA5")

    QueueWorkItem2(0x101, 2, lambda_9AA5)
    Sleep(150)

    ChrTalk(
        0x101,
        "#00000F#11PKeya、一緒に出るか？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#01109F#5PWow!\x01",
            "Wait a moment!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    def lambda_9B0F():

        label("loc_9B0F")

        TurnDirection(0xFE, 0x153, 500)
        Yield()
        Jump("loc_9B0F")

    QueueWorkItem2(0x105, 2, lambda_9B0F)

    def lambda_9B21():

        label("loc_9B21")

        TurnDirection(0xFE, 0x153, 500)
        Yield()
        Jump("loc_9B21")

    QueueWorkItem2(0x102, 2, lambda_9B21)

    def lambda_9B33():

        label("loc_9B33")

        TurnDirection(0xFE, 0x153, 500)
        Yield()
        Jump("loc_9B33")

    QueueWorkItem2(0x109, 2, lambda_9B33)
    SetChrChipByIndex(0x153, 0xFF)
    SetChrSubChip(0x153, 0x0)
    Sound(802, 0, 100, 0)
    OP_68(255000, 1100, 69700, 3000)
    OP_9D(0x153, 0x3E0F8, 0x0, 0x11940, 0x12C, 0xBB8)
    ClearChrFlags(0x153, 0x4)
    OP_93(0x153, 0x2D, 0x1F4)

    def lambda_9B87():
        OP_95(0xFE, 255700, 0, 72800, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_9B87)
    WaitChrThread(0x153, 1)
    OP_93(0x153, 0x0, 0x1F4)
    Sleep(750)
    Fade(250)
    SetChrChipByIndex(0x153, 0x1E)
    SetChrSubChip(0x153, 0x0)
    OP_0D()
    OP_93(0x153, 0xB4, 0x1F4)
    SetChrFlags(0x153, 0x1000)

    def lambda_9BC9():
        OP_95(0xFE, 255700, 30, 70400, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_9BC9)
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
        "#5P#01110FYes, I will keep you waiting!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00002FOK, then shall we go?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00102FKeyaちゃんと一緒なら\x01",
            "Shall I get out of the back door?\x02",
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

    # Function_68_9380 end

    def Function_69_9CBC(): pass

    label("Function_69_9CBC")


    def lambda_9CC1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_9CC1)

    def lambda_9CD2():
        OP_95(0xFE, 253000, 0, 66000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9CD2)
    WaitChrThread(0xFE, 1)

    def lambda_9CF0():
        OP_95(0xFE, 254000, 0, 69300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9CF0)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_69_9CBC end

    def Function_70_9D11(): pass

    label("Function_70_9D11")

    Sleep(700)

    def lambda_9D19():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_9D19)

    def lambda_9D2A():
        OP_95(0xFE, 253000, 0, 66000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9D2A)
    WaitChrThread(0xFE, 1)

    def lambda_9D48():
        OP_95(0xFE, 254300, 0, 68300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9D48)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_70_9D11 end

    def Function_71_9D69(): pass

    label("Function_71_9D69")

    Sleep(1400)

    def lambda_9D71():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_9D71)

    def lambda_9D82():
        OP_95(0xFE, 253000, 0, 66000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9D82)
    WaitChrThread(0xFE, 1)

    def lambda_9DA0():
        OP_95(0xFE, 255100, 0, 67900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9DA0)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x13B, 0x1F4)
    Return()

    # Function_71_9D69 end

    def Function_72_9DC1(): pass

    label("Function_72_9DC1")

    Sleep(2100)

    def lambda_9DC9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_9DC9)

    def lambda_9DDA():
        OP_95(0xFE, 253000, 0, 66000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9DDA)
    WaitChrThread(0xFE, 1)

    def lambda_9DF8():
        OP_95(0xFE, 253100, 0, 67900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9DF8)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_72_9DC1 end

    def Function_73_9E19(): pass

    label("Function_73_9E19")

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

    def lambda_9EFC():
        OP_97(0x109, 0xFFFFEC78, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_9EFC)
    Sleep(200)

    def lambda_9F19():
        OP_97(0x102, 0xFFFFEC78, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_9F19)
    Sleep(200)

    def lambda_9F36():
        OP_97(0x105, 0xFFFFEC78, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_9F36)
    SetCameraDistance(22500, 2000)
    FadeToBright(1000, 0)
    VolumeBGM(0x50, 0x3E8)
    Sound(103, 0, 100, 0)
    Sleep(600)

    def lambda_9F71():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_9F71)
    Sleep(400)

    def lambda_9F85():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_9F85)
    Sleep(400)

    def lambda_9F99():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_9F99)

    def lambda_9FAA():
        OP_96(0xFE, 0xFFFFF448, 0xA, 0x108D8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_9FAA)
    Sleep(300)

    def lambda_9FC7():
        OP_96(0xFE, 0xFFFFFA24, 0xA, 0x108D8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9FC7)
    WaitChrThread(0x101, 1)
    TurnDirection(0x101, 0x104, 500)

    ChrTalk(
        0x101,
        "#00003F#11P── Hey, Randy.\x02",
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
        "Hmm? What a Lloyd.\x02",
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
            "#00008F#11PThat……\x01",
            "It's about your father.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x104,
        (
            "#6P#00306FOh, that is ……\x02\x03",
            "#00300FSomething you do not mind separately?\x01",
            "It is not uncommon in that world.\x02\x03",
            "Besides, when I left the group\x01",
            "My father and I have broken hearts.\x02\x03",
            "#00304FI do not feel anything ……\x01",
            "Well, I'm sorry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#11P……I see.\x02\x03",
            "#00001FBut, if you feel like it\x01",
            "Please let me know a variety of things?\x02\x03",
            "Once, as a leader\x01",
            "I may be able to ride consultation\x01",
            "I do not think so.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00305F………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00011F#11POh, sorry.\x01",
            "Was it a bit cheeky?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00304FHa ha, it is different.\x02\x03",
            "#00302FWhatever you say\x01",
            "I thought that you also grew.\x02\x03",
            "#00309FWell, my older brother is deeply impressed.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 5)), scpexpr(EXPR_END)), "loc_A527")

    ChrTalk(
        0x101,
        "#00006F#11PYou know.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00008F#11P…… That time, like this\x01",
            "I want you to manage it somehow.\x02\x03",
            "#00000FAlthough it may not be reliable\x01",
            "Is not it \"buddy\"?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00305FLloyd …\x02",
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x104)
    SetCameraDistance(22000, 1000)

    def lambda_A446():
        OP_96(0xFE, 0xFFFFF736, 0xA, 0x108D8, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A446)
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
            "#6P#00302F… …. OK, which story\x01",
            "Perhaps it will be heard.\x02\x03",
            "#00309FThat time I will ask - ___ 0.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002F#11PAh……!\x02",
    )

    CloseMessageWindow()
    Jump("loc_A5B9")

    label("loc_A527")


    ChrTalk(
        0x101,
        "#00006F#11PYou know.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00304F… Well, if you feel like it\x01",
            "I might consult him.\x02\x03",
            "#00300FAt that time I will ask for your kindness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#11PAh……!\x02",
    )

    CloseMessageWindow()

    label("loc_A5B9")

    SetChrPos(0x102, -7000, -2000, 68300, 270)
    SetChrPos(0x105, -7000, -2000, 67300, 270)

    NpcTalk(
        0x105,
        "Voice of Wadi",
        "#2P#2SWhat are you doing?\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x102,
        "Ely's voice",
        "#2P#2SBoth of them are lost articles?\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 5)), scpexpr(EXPR_END)), "loc_A6B0")
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

    def lambda_A697():
        OP_96(0xFE, 0xFFFFF542, 0xA, 0x108D8, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A697)
    WaitChrThread(0x104, 1)

    label("loc_A6B0")


    def lambda_A6B5():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_A6B5)

    ChrTalk(
        0x101,
        "#00011F#11PSorry, I will go!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#11P#00304FWell then,\x01",
            "When you start working, it is all.\x02",
        )
    )

    CloseMessageWindow()
    VolumeBGM(0x64, 0x3E8)

    def lambda_A729():
        OP_97(0x104, 0xFFFFEC78, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_A729)
    Sleep(100)

    def lambda_A746():
        OP_97(0x101, 0xFFFFEC78, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_A746)
    FadeToDark(1000, 0, -1)
    Sleep(400)

    def lambda_A76D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_A76D)
    Sleep(400)

    def lambda_A781():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A781)
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
            "With a driving car, across the crossbell\x01",
            "It is now possible to move.\x02\x03",
            "At the back door of the Special Affairs Support Division on Nishi Dori\x01",
            "Please stop using it because it is stopped.\x07\x00\x02",
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

    # Function_73_9E19 end

    def Function_74_A88D(): pass

    label("Function_74_A88D")

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
        "#11P#01100FTake care, everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10109Fふふ、行ってくるねKeyaちゃん。\x02\x03",
            "#10106F……こうしてKeyaちゃんに\x01",
            "Saying \"I do not mention you\"\x01",
            "It will be gone for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00002FOkay … after all I will miss you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106FKeyaちゃんと離れるなんて、\x01",
            "You can not bear with just imagining it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#01100FIf Noel ceases to exist\x01",
            "Keyaもサビしいけど……\x01",
            "Cheer up, Noeloo.\x02\x03",
            "#01109FWith the Frank who got better\x01",
            "I'm waiting for two people to come and play.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10102Fうん、ありがとうKeyaちゃん。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302FHa ha, Noel.\x01",
            "If this is the case, we will reorganize the guard\x01",
            "I guess it's getting tidied up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00202FAs soon as Mr. Fran\x01",
            "I have to get it recovered.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10109FHehe, that's right.\x02\x03",
            "#10100FKeyaちゃんの笑顔に\x01",
            "To see you again as soon as possible!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#12P#10302FWell, it's burning.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11P#01102FErr …\x02",
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

    # Function_74_A88D end

    SaveToFile()

Try(main)
