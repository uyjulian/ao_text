from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c1420.bin",                # FileName
        "c1420",                    # MapName
        "c1420",                    # Location
        0x002F,                     # MapIndex
        "ed7116",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 47, 0, 2, 0, 3],
    )

    BuildStringList((
        "c1420",                  # 0
        "Luganov",                # 1
        "Jed",                    # 2
        "Huey",                   # 3
        "Slash",                  # 4
        "Kｷki",                  # 5
        "Dino",                   # 6
    ))

    AddCharChip((
        "chr/ch06800.itc",                   # 00
        "chr/ch30800.itc",                   # 01
        "chr/ch31700.itc",                   # 02
        "chr/ch30802.itc",                   # 03
        "chr/ch31702.itc",                   # 04
    ))

    DeclNpc(17079,   1000,    4294964717, 225,  261,  0x0, 0,   1,   0,   0,   1,   0,   4,   255,  0)
    DeclNpc(12189,   0,       4294962027, 270,  261,  0x0, 0,   2,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(18700,   4000,    4294959086, 315,  261,  0x0, 0,   2,   0,   0,   0,   0,   18,  255,  0)
    DeclNpc(1779,    0,       4294962036, 90,   261,  0x0, 0,   1,   0,   0,   0,   0,   21,  255,  0)
    DeclNpc(11420,   0,       7809,    0,    261,  0x0, 0,   1,   0,   0,   0,   0,   22,  255,  0)
    DeclNpc(2920,    0,       6769,    89,   389,  0x0, 0,   0,   0,   0,   0,   0,   24,  255,  0)

    DeclEvent(0x0040, 0, 15,  6.260000228881836,     -1.0800000429153442,   -1.0,                  9.0,                   [0.1666666716337204,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.1666666716337204,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -1.0433334112167358,   0.18000000715255737,   0.20000000298023224,   1.0])

    ChipFrameInfo(540, 0)                                        # 0

    ScpFunction((
        "Function_0_21C",          # 00, 0
        "Function_1_2CC",          # 01, 1
        "Function_2_2F7",          # 02, 2
        "Function_3_992",          # 03, 3
        "Function_4_A07",          # 04, 4
        "Function_5_1031",         # 05, 5
        "Function_6_15AB",         # 06, 6
        "Function_7_1754",         # 07, 7
        "Function_8_18A8",         # 08, 8
        "Function_9_1B2A",         # 09, 9
        "Function_10_2046",        # 0A, 10
        "Function_11_2615",        # 0B, 11
        "Function_12_279C",        # 0C, 12
        "Function_13_291F",        # 0D, 13
        "Function_14_2C07",        # 0E, 14
        "Function_15_2D3C",        # 0F, 15
        "Function_16_30CB",        # 10, 16
        "Function_17_314A",        # 11, 17
        "Function_18_32F4",        # 12, 18
        "Function_19_36B1",        # 13, 19
        "Function_20_384A",        # 14, 20
        "Function_21_3A95",        # 15, 21
        "Function_22_3E12",        # 16, 22
        "Function_23_40E7",        # 17, 23
        "Function_24_419A",        # 18, 24
        "Function_25_46C3",        # 19, 25
        "Function_26_57C6",        # 1A, 26
    ))


    def Function_0_21C(): pass

    label("Function_0_21C")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_254"),
        (1, "loc_260"),
        (2, "loc_26C"),
        (3, "loc_278"),
        (4, "loc_284"),
        (5, "loc_290"),
        (6, "loc_29C"),
        (SWITCH_DEFAULT, "loc_2A8"),
    )


    label("loc_254")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_2B4")

    label("loc_260")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_2B4")

    label("loc_26C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_2B4")

    label("loc_278")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_2B4")

    label("loc_284")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_2B4")

    label("loc_290")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_2B4")

    label("loc_29C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2B4")

    label("loc_2A8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2B4")

    label("loc_2B4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2CB")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2B4")

    label("loc_2CB")

    Return()

    # Function_0_21C end

    def Function_1_2CC(): pass

    label("Function_1_2CC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2F6")
    OP_94(0xFE, 0x38C2, 0xFFFFF1B4, 0x4902, 0xFFFFF984, 0x3E8)
    Sleep(300)
    Jump("Function_1_2CC")

    label("loc_2F6")

    Return()

    # Function_1_2CC end

    def Function_2_2F7(): pass

    label("Function_2_2F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_30F")
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    Jump("loc_991")

    label("loc_30F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_384")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrPos(0x9, 8410, 150, 2820, 180)
    SetChrChipByIndex(0x9, 0x4)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    SetChrPos(0xA, 8610, 0, 620, 0)
    SetChrPos(0xB, 9810, 0, 1720, 315)
    SetChrFlags(0x9, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37F")
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xB, 0x10)

    label("loc_37F")

    Jump("loc_991")

    label("loc_384")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3AB")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    Jump("loc_991")

    label("loc_3AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3ED")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 5200, 0, -850, 135)
    SetChrFlags(0xD, 0x10)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    Jump("loc_991")

    label("loc_3ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_48C")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xC, 11110, 0, -5220, 315)
    SetChrPos(0xD, 9940, 0, -4200, 135)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_42C")
    SetChrFlags(0xD, 0x10)

    label("loc_42C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_43B")
    SetChrFlags(0xC, 0x10)

    label("loc_43B")

    SetChrPos(0x9, 7030, 0, -50, 225)
    SetChrPos(0xB, 5200, 0, -850, 90)
    SetChrPos(0xA, 7320, 0, -1690, 315)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_487")
    SetChrFlags(0x9, 0x10)
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0xA, 0x10)

    label("loc_487")

    Jump("loc_991")

    label("loc_48C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_583")
    ClearChrFlags(0xD, 0x80)
    BeginChrThread(0x8, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16F, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_518")
    SetChrPos(0x8, 11740, 0, 3420, 270)
    SetChrPos(0xB, 10710, 0, 3950, 180)
    SetChrPos(0xA, 11310, 0, 2070, 0)
    SetChrPos(0x9, 11990, 0, -2650, 270)
    SetChrPos(0xC, 10020, 0, -3240, 0)
    SetChrPos(0xD, 10920, 0, -1430, 180)
    Event(0, 25)
    Jump("loc_57E")

    label("loc_518")

    SetChrPos(0x8, 16290, 1000, -1650, 315)
    SetChrPos(0x9, 15290, 1000, -650, 135)
    SetChrPos(0xA, 11110, 0, -5220, 315)
    SetChrPos(0xB, 9940, 0, -4200, 135)
    SetChrPos(0xC, 7030, 0, -50, 180)
    SetChrPos(0xD, 7320, 0, -1690, 0)

    label("loc_57E")

    Jump("loc_991")

    label("loc_583")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_620")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0x8, 8420, 0, -590, 90)
    BeginChrThread(0x8, 0, 0, 0)
    SetChrPos(0xB, 9260, 0, -2100, 90)
    SetChrPos(0xA, 9360, 0, 930, 90)
    SetChrPos(0xD, 11270, 0, -2110, 270)
    SetChrPos(0x9, 11840, 0, -590, 270)
    SetChrPos(0xC, 11330, 0, 1080, 270)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0xD, 0x10)
    SetChrFlags(0x9, 0x10)
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xC, 0x10)
    Jump("loc_991")

    label("loc_620")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_69B")
    SetChrFlags(0xC, 0x80)
    SetChrPos(0x8, 8420, 0, -590, 90)
    BeginChrThread(0x8, 0, 0, 0)
    SetChrPos(0x9, 10910, 0, -710, 270)
    SetChrPos(0xB, 9740, 0, -1840, 0)
    SetChrPos(0xA, 9850, 0, 700, 180)
    SetChrFlags(0x8, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_68C")
    SetChrFlags(0x9, 0x10)

    label("loc_68C")

    SetChrFlags(0xB, 0x10)
    SetChrFlags(0xA, 0x10)
    Jump("loc_991")

    label("loc_69B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_738")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0x8, 11500, 0, -3660, 225)
    BeginChrThread(0x8, 0, 0, 0)
    SetChrPos(0xA, 11110, 0, -5220, 315)
    SetChrPos(0xB, 9940, 0, -4200, 135)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0x8, 0x10)
    SetChrPos(0x9, 7030, 0, -50, 225)
    SetChrPos(0xC, 5200, 0, -850, 90)
    SetChrPos(0xD, 7320, 0, -1690, 315)
    SetChrFlags(0x9, 0x10)
    SetChrFlags(0xC, 0x10)
    SetChrFlags(0xD, 0x10)
    Jump("loc_991")

    label("loc_738")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_7D5")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0x8, 11500, 0, -3660, 225)
    BeginChrThread(0x8, 0, 0, 0)
    SetChrPos(0xA, 11110, 0, -5220, 0)
    SetChrPos(0xB, 9940, 0, -4200, 90)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0x8, 0x10)
    SetChrPos(0x9, 7030, 0, -50, 225)
    SetChrPos(0xC, 5200, 0, -850, 90)
    SetChrPos(0xD, 7320, 0, -1690, 315)
    SetChrFlags(0x9, 0x10)
    SetChrFlags(0xC, 0x10)
    SetChrFlags(0xD, 0x10)
    Jump("loc_991")

    label("loc_7D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_865")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0x9, 7030, 0, -50, 225)
    SetChrPos(0xC, 5200, 0, -850, 90)
    SetChrPos(0xD, 7320, 0, -1690, 315)
    SetChrFlags(0x9, 0x10)
    SetChrFlags(0xC, 0x10)
    SetChrFlags(0xD, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_83E")
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    Jump("loc_860")

    label("loc_83E")

    SetChrPos(0xA, 11110, 0, -5220, 315)
    SetChrPos(0xB, 9940, 0, -4200, 135)

    label("loc_860")

    Jump("loc_991")

    label("loc_865")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_8E5")
    SetChrPos(0x8, 7030, 0, -50, 225)
    BeginChrThread(0x8, 0, 0, 0)
    SetChrPos(0xC, 5200, 0, -850, 90)
    SetChrPos(0x9, 7320, 0, -1690, 315)
    SetChrPos(0xA, 11110, 0, -5220, 315)
    SetChrPos(0xB, 9940, 0, -4200, 135)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xB, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14D, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8E0")
    Event(0, 9)

    label("loc_8E0")

    Jump("loc_991")

    label("loc_8E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_96F")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0x9, 7030, 0, -50, 225)
    SetChrPos(0xC, 5200, 0, -850, 90)
    SetChrPos(0xD, 7320, 0, -1690, 315)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x137, 4)), scpexpr(EXPR_END)), "loc_939")
    SetChrFlags(0x9, 0x10)
    SetChrFlags(0xD, 0x10)

    label("loc_939")

    SetChrFlags(0xC, 0x10)
    SetChrPos(0xA, 11110, 0, -5220, 315)
    SetChrPos(0xB, 9940, 0, -4200, 135)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xB, 0x10)
    Jump("loc_991")

    label("loc_96F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_991")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)

    label("loc_991")

    Return()

    # Function_2_2F7 end

    def Function_3_992(): pass

    label("Function_3_992")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14D, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9AF")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_9AF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_9C8")
    OP_10(0x0, 0x0)
    OP_10(0x1, 0x1)
    Jump("loc_9CE")

    label("loc_9C8")

    OP_10(0x0, 0x1)
    OP_10(0x1, 0x0)

    label("loc_9CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9EF")
    Sound(128, 1, 50, 0)

    label("loc_9EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A06")
    OP_7D(0xD2, 0xD2, 0xE6, 0x0, 0x0)

    label("loc_A06")

    Return()

    # Function_3_992 end

    def Function_4_A07(): pass

    label("Function_4_A07")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_B68")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_ADA")

    ChrTalk(
        0xFE,
        "Yeeeeah, yeeeah～～～!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Who cares if I'm uneasy～～!!\x01",
            "I don't have time to care about\x01",
            "incomprehensible things～!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I could even sing a song,\x01",
            "Yeeees～～!! Yahhoo～～!!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_B63")

    label("loc_ADA")


    ChrTalk(
        0xFE,
        (
            "What kind of wind brought that huge\x01",
            "tree! I don't care if I'm uneasy～～!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I could even sing a song,\x01",
            "Yeeees～～!! Yahhoo～～!!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B63")

    Jump("loc_102D")

    label("loc_B68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_B76")
    Jump("loc_102D")

    label("loc_B76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_B84")
    Jump("loc_102D")

    label("loc_B84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_B92")
    Jump("loc_102D")

    label("loc_B92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_C0D")

    ChrTalk(
        0xFE,
        (
            "Woooah, ack, I'm\x01",
            "somehow irritated!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "An armed group at Mainz!?\x01",
            "More importantly, where's\x01",
            "Mr. Wald!?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_102D")

    label("loc_C0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_C50")

    ChrTalk(
        0xFE,
        (
            "Hmph, let me just say this.\x01",
            "You owe me a punch.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_102D")

    label("loc_C50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_CD7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16E, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C6B")
    Call(0, 5)
    Jump("loc_CD2")

    label("loc_C6B")


    ChrTalk(
        0xFE,
        (
            "Mr. Wald... Did he hit\x01",
            "it big at the casino?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But if that's the case,\x01",
            "why didn't he tell me!?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CD2")

    Jump("loc_102D")

    label("loc_CD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_D33")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CF2")
    Call(0, 6)
    Jump("loc_D2E")

    label("loc_CF2")


    ChrTalk(
        0xFE,
        (
            "*sigh*, even so, it's boring\x01",
            "when Mr. Wald's not here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D2E")

    Jump("loc_102D")

    label("loc_D33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_D44")
    Call(0, 7)
    Jump("loc_102D")

    label("loc_D44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_D55")
    Call(0, 8)
    Jump("loc_102D")

    label("loc_D55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_E96")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E1B")

    ChrTalk(
        0xFE,
        (
            "Mr. Wald～～!! I'm begging\x01",
            "you! Show your face!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We'll buy you alcohol, so\x01",
            "let's enjoy it heeere～～!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Without you here, nothing\x01",
            "can begin, you know～～!?!?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_E91")

    label("loc_E1B")


    ChrTalk(
        0xFE,
        (
            "We'll buy you alcohol, so\x01",
            "let's enjoy it heeere～～!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Without you here, nothing\x01",
            "can begin, you know～～!?!?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E91")

    Jump("loc_102D")

    label("loc_E96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_F1B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14D, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EB1")
    Call(0, 9)
    Jump("loc_F16")

    label("loc_EB1")


    ChrTalk(
        0xFE,
        (
            "I don't believe this...\x01",
            "I won't ever believe it!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As if such an absurdity\x01",
            "could happen...!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F16")

    Jump("loc_102D")

    label("loc_F1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1024")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FB7")

    ChrTalk(
        0xFE,
        "Yeeeah, yeeeah～～!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Those damn Testaments!\x01",
            "Now it's our chance to take them out!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#4S...Yeeeeah～～!! Yahhoo!!#3S\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_101F")

    label("loc_FB7")


    ChrTalk(
        0xFE,
        (
            "Those damn Testaments!\x01",
            "Now it's our chance to take them out!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#4S...Yeeeeah～～!! Yahhoo!!#3S\x02",
    )

    CloseMessageWindow()

    label("loc_101F")

    Jump("loc_102D")

    label("loc_1024")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_102D")

    label("loc_102D")

    TalkEnd(0xFE)
    Return()

    # Function_4_A07 end

    def Function_5_1031(): pass

    label("Function_5_1031")

    OP_4B(0xD, 0xFF)
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_4B(0xA, 0xFF)
    OP_4B(0xC, 0xFF)

    ChrTalk(
        0x9,
        (
            "Hey, you guys. \x01",
            "How's that investigation?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "O-Oss...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "It was a week ago...\x01",
            "That Kanon kid said\x01",
            "he saw Mr. Wald...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "And, looks like he was\x01",
            "using a small communicator\x01",
            "called an ENIGMA.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "According to the exchange\x01",
            "shop owner, one of those\x01",
            "costs 100,000 mira, but...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xB,
        "A hundr... 100,000 miraaa!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Whoa, seriously?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "M-Mr. Wald... Just where \x01",
            "did he get that kind of mira...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I'm worried about that, but...\x01",
            "Kｷki, did you say communicator?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "In other words...\x01",
            "Mr. Wald's been in\x01",
            "contact with someone.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xC,
        (
            "Yeah. As you can expect,\x01",
            "I didn't get the details from\x01",
            "that brat, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Yeah, but he said it seemed like\x01",
            "Mr. Wald was smiling happily...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "...H-He smiled?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "I guess something good happened...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I can't believe Mr. \x01",
            "Wald abandoned us...\x01",
            "That can't be right, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hey, Slash.\x01",
            "Shut your traps.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "But if you wanna die, I guess \x01",
            "it's a different story.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xB)
    TurnDirection(0xB, 0x8, 0)

    ChrTalk(
        0xB,
        "S-Sorry!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001F(So Wald has an ENIGMA, huh...\x01",
            "That's indeed worrying.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F(Yes. Not that many\x01",
            "ENIGMAs have been sold to\x01",
            "the general public yet...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10303F(...Wald...)\x02",
    )

    CloseMessageWindow()
    OP_4C(0x8, 0xFF)
    OP_4C(0xD, 0xFF)
    OP_4C(0x9, 0xFF)
    OP_4C(0xB, 0xFF)
    OP_4C(0xA, 0xFF)
    OP_4C(0xC, 0xFF)
    OP_93(0x8, 0x5A, 0x0)
    OP_93(0xD, 0x10E, 0x0)
    OP_93(0x9, 0x10E, 0x0)
    OP_93(0xB, 0x5A, 0x0)
    OP_93(0xA, 0x5A, 0x0)
    OP_93(0xC, 0x10E, 0x0)
    SetScenarioFlags(0x16E, 4)
    Return()

    # Function_5_1031 end

    def Function_6_15AB(): pass

    label("Function_6_15AB")

    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_4B(0xA, 0xFF)

    ChrTalk(
        0x8,
        (
            "Hey Jed. Have\x01",
            "Kｷki or Dino\x01",
            "come by yet?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Well, just wait.. They need to\x01",
            "do an additional investigation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "By the way, yours seems it\x01",
            "didn't go well, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Well, you see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "S-Sorry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "We looked around where we thought\x01",
            "he could be, but it seems that no one\x01",
            "has seen him at all as of late...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "...I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Mr. Wald... Seriously,\x01",
            "where has he gone.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    SetScenarioFlags(0x0, 1)
    SetScenarioFlags(0x0, 3)
    SetScenarioFlags(0x0, 2)
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    OP_4C(0xB, 0xFF)
    OP_4C(0xA, 0xFF)
    ClearChrFlags(0x9, 0x10)
    Return()

    # Function_6_15AB end

    def Function_7_1754(): pass

    label("Function_7_1754")

    OP_4B(0x8, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_4B(0xA, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1801")

    ChrTalk(
        0x8,
        (
            "Ah, I guess we'll\x01",
            "look in places Mr.\x01",
            "Wald might have gone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The search area is the whole\x01",
            "city. Look everywhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Oss!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Roger!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_189B")

    label("loc_1801")


    ChrTalk(
        0x8,
        (
            "If you spot Mr. Wald, get back\x01",
            "here immediately and report.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you spoke to him he could\x01",
            "ignore you again, so don't fail.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Oss!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Roger!\x02",
    )

    CloseMessageWindow()

    label("loc_189B")

    OP_4C(0x8, 0xFF)
    OP_4C(0xB, 0xFF)
    OP_4C(0xA, 0xFF)
    Return()

    # Function_7_1754 end

    def Function_8_18A8(): pass

    label("Function_8_18A8")

    OP_4B(0x8, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_4B(0xA, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AC3")

    ChrTalk(
        0x8,
        "And? What did they do?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Y-Yeah. About that, \x01",
            "they honestly apologised...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "When they use and attitude like that,\x01",
            "you can't belittle them more...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Honestly, how hopeless you are!\x01",
            "Those blue baldies can have there faults,\x01",
            "but even you, you lack fighting spirit!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Times like those is when you have to\x01",
            "provoke them. I'll teach you my\x01",
            "favorite fightin' words, so listen up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            ""Your mama's so fat!"\x01",
            "...Now say it!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0xB, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xA,
        "U-Umm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "O-Oss!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1B1D")

    label("loc_1AC3")


    ChrTalk(
        0xA,
        "Y-Your mama's...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "S-So fat..., huh.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Hey hey hey!  Your voices are too low!!\x02",
    )

    CloseMessageWindow()

    label("loc_1B1D")

    OP_4C(0x8, 0xFF)
    OP_4C(0xB, 0xFF)
    OP_4C(0xA, 0xFF)
    Return()

    # Function_8_18A8 end

    def Function_9_1B2A(): pass

    label("Function_9_1B2A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(1400, 1000, 0, 0)
    MoveCamera(30, 17, 0, 0)
    OP_6E(380, 0)
    SetCameraDistance(24500, 0)
    SetChrPos(0x101, 2400, 0, -700, 90)
    SetChrPos(0x105, 2400, 0, 700, 90)
    SetChrPos(0x102, 1100, 0, -700, 90)
    SetChrPos(0x109, 1100, 0, 700, 90)
    SetChrPos(0x104, 100, 0, 700, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_4B(0xC, 0xFF)
    OP_68(3400, 1000, 0, 4000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    ChrTalk(
        0x9,
        (
            "Kｷki... \x01",
            "Is that story?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Well, that's what\x01",
            "the brat said, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I don't believe it. \x01",
            "No, I'll never believe it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "For Mr. Wald to get\x01",
            "beaten like that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105F(This... Are they\x01",
            "talking about the fight\x01",
            "on that rainy day?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F(Yeah... Must be.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10303F(......)\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x9, 0x105, 500)

    ChrTalk(
        0x9,
        (
            "Y-You... How can you have\x01",
            "the face to come here!?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_1DA7():
        TurnDirection(0x8, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1DA7)
    TurnDirection(0xC, 0x105, 500)

    ChrTalk(
        0xC,
        "W-Wazy...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Hyaha, is it our turns now, eh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Fine, stick out that face!\x01",
            "I'm gonna waste you!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FH-Hey...!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 500)

    ChrTalk(
        0x9,
        "―Luganov, stop!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Even if what the brat said was true,\x01",
            "if we fought here we'd make \x01",
            "Mr. Wald look bad...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "And, it's not what would\x01",
            "make Mr. Wald happy!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Tch, shit...!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x105, 500)

    ChrTalk(
        0xC,
        (
            "I don't know why\x01",
            "you're here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "We don't feel like fighting\x01",
            "you, so get out, ok?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "But if you're here to pick a\x01",
            "fight, that's a different story.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303FNo, I have no such intentions.\x02\x03",
            "#10300FSorry to have bothered you.\x01",
            "...Let's go, everyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FY-Yeah...\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0xE1, 0x0)
    OP_93(0x9, 0x13B, 0x0)
    OP_93(0xC, 0x87, 0x0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    OP_4C(0xC, 0xFF)
    SetScenarioFlags(0x14D, 0)
    EventEnd(0x5)
    Return()

    # Function_9_1B2A end

    def Function_10_2046(): pass

    label("Function_10_2046")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_21AE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_212A")

    ChrTalk(
        0xFE,
        (
            "I still haven't forgiven\x01",
            "Mr. Wald.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...That's not the case, but...\x01",
            "It's certain the Saber Viper\x01",
            "was a super fun place to be.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As a Vipers' leader... That's\x01",
            "reason enough to protect it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_21A9")

    label("loc_212A")


    ChrTalk(
        0xFE,
        (
            "I still haven't forgiven\x01",
            "Mr. Wald, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As a Viper leader, protecting\x01",
            "this precious place is the\x01",
            "way it has to be.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21A9")

    Jump("loc_2611")

    label("loc_21AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_224C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21C9")
    Call(0, 11)
    Jump("loc_2247")

    label("loc_21C9")


    ChrTalk(
        0xFE,
        (
            "...Damn. Cooperating\x01",
            "with those blue baldies,\x01",
            "of all things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Luganov, Kｷki, Dino... \x01",
            "What're those guys thinking...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2247")

    Jump("loc_2611")

    label("loc_224C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_225A")
    Jump("loc_2611")

    label("loc_225A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2268")
    Jump("loc_2611")

    label("loc_2268")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2329")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2283")
    Call(0, 12)
    Jump("loc_2324")

    label("loc_2283")


    ChrTalk(
        0xFE,
        (
            "Hm? The Support Section... It seems\x01",
            "there're no developments on either side.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Now listen here. Next time\x01",
            "you see Mr. Wald, you let\x01",
            "us know immediately.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2324")

    Jump("loc_2611")

    label("loc_2329")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_242F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23E0")

    ChrTalk(
        0xFE,
        (
            "...Luganov more or less said\x01",
            "what we want to say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There's nothing else to discuss.\x01",
            "...Make yourselves scarce, for today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10303F............\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_242A")

    label("loc_23E0")


    ChrTalk(
        0xFE,
        (
            "We've got nothing else to say.\x01",
            "...Make yourselves scarce, for today.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_242A")

    Jump("loc_2611")

    label("loc_242F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_247F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16E, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_244A")
    Call(0, 5)
    Jump("loc_247A")

    label("loc_244A")


    ChrTalk(
        0xFE,
        (
            "Mr. Wald...\x01",
            "What the heck happened to you?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_247A")

    Jump("loc_2611")

    label("loc_247F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_24CE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_249A")
    Call(0, 6)
    Jump("loc_24C9")

    label("loc_249A")


    ChrTalk(
        0xFE,
        (
            "Mr. Wald... Seriously,\x01",
            "where has he gone.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24C9")

    Jump("loc_2611")

    label("loc_24CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_24DF")
    Call(0, 13)
    Jump("loc_2611")

    label("loc_24DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_24F0")
    Call(0, 14)
    Jump("loc_2611")

    label("loc_24F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2501")
    Call(0, 16)
    Jump("loc_2611")

    label("loc_2501")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_25AB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14D, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_251C")
    Call(0, 9)
    Jump("loc_25A6")

    label("loc_251C")


    ChrTalk(
        0xFE,
        (
            "We've got no quarrel with you,\x01",
            "so get out of here already...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you stick around any longer, \x01",
            "I can't be sure what will happen.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25A6")

    Jump("loc_2611")

    label("loc_25AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2608")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x137, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25C6")
    Call(0, 17)
    Jump("loc_2603")

    label("loc_25C6")


    ChrTalk(
        0xFE,
        (
            "Listen, Wazy... \x01",
            "Don't think you'll\x01",
            "get away with this.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2603")

    Jump("loc_2611")

    label("loc_2608")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2611")

    label("loc_2611")

    TalkEnd(0xFE)
    Return()

    # Function_10_2046 end

    def Function_11_2615(): pass

    label("Function_11_2615")

    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)

    ChrTalk(
        0x9,
        (
            "Those guys... To be\x01",
            "working with them,\x01",
            "of all things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "...Mr. Jed. Shouldn't\x01",
            "we cooperate with\x01",
            "them too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Hyaha, the heck are you saying,\x01",
            "Huey!? Vipers strangle\x01",
            "their traitors...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...Didn't he say Saber\x01",
            "Viper is no more, idiot!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xB)

    ChrTalk(
        0xB,
        "S-Sorry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...Anyway, I'm thinking about it.\x01",
            "Don't go doing just whatever you want.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    ClearChrFlags(0xA, 0x10)
    ClearChrFlags(0xB, 0x10)
    SetScenarioFlags(0x0, 1)
    Return()

    # Function_11_2615 end

    def Function_12_279C(): pass

    label("Function_12_279C")

    OP_4B(0x9, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_4B(0xA, 0xFF)

    ChrTalk(
        0x9,
        (
            "Tch. I don't get it, but\x01",
            "it's noisy out there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Yeah. It seems like everyone in the city's\x01",
            "talking about how Mainz is occupied.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "It can't be...\x01",
            "Mr. Wald won't get involved\x01",
            "with the incident, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Well, I don't think so, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Anyway guys, let's get fired\x01",
            "up today too and collect info.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#2POss!\x02",
    )


    ChrTalk(
        0xB,
        "#3POss!\x02",
    )

    OP_57(0x1)
    SetScenarioFlags(0x0, 1)
    SetScenarioFlags(0x0, 3)
    SetScenarioFlags(0x0, 2)
    ClearChrFlags(0x9, 0x10)
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0xA, 0x10)
    OP_4C(0x9, 0xFF)
    OP_4C(0xB, 0xFF)
    OP_4C(0xA, 0xFF)
    Return()

    # Function_12_279C end

    def Function_13_291F(): pass

    label("Function_13_291F")

    OP_4B(0xD, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_4B(0xC, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B85")

    ChrTalk(
        0xC,
        (
            "Mr. Wald... I wonder what\x01",
            "he's doing around now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Heck if I know...\x01",
            "It seems he hasn't returned\x01",
            "to his home for a while too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "It's been three days\x01",
            "since I've seen him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "The last was when Mr. Huey and the\x01",
            "others saw him in Waterfront Area...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Yeah, and when we called out\x01",
            "to him, he ignored us...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...Anyhow, something's\x01",
            "happened to Mr. Wald. \x01",
            "Let's split up and look for clues.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "You two handle Downtown. \x01",
            "Be sure to speak with everyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Oss!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Roger!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F(Wald... They don't\x01",
            "know where he is?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10303F(I wonder why... I'm worried.)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2BFA")

    label("loc_2B85")


    ChrTalk(
        0x9,
        (
            "Luganov and I will\x01",
            "focus on Ignis in turns.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "If you find anything, return and report.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Oss!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Roger!\x02",
    )

    CloseMessageWindow()

    label("loc_2BFA")

    OP_4C(0xD, 0xFF)
    OP_4C(0x9, 0xFF)
    OP_4C(0xC, 0xFF)
    Return()

    # Function_13_291F end

    def Function_14_2C07(): pass

    label("Function_14_2C07")

    OP_4B(0xD, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_4B(0xC, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CCA")

    ChrTalk(
        0x9,
        (
            "Well, have you seen Mr.\x01",
            "Wald since yesterday?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "No, not at all...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "M-Me neither.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Well from the look of it, I thought\x01",
            "he was drunk yesterday, but...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2D2F")

    label("loc_2CCA")


    ChrTalk(
        0x9,
        (
            "Right...I'll go check\x01",
            "back at his home later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "You guys come too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Oss!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Of course!\x02",
    )

    CloseMessageWindow()

    label("loc_2D2F")

    OP_4C(0xD, 0xFF)
    OP_4C(0x9, 0xFF)
    OP_4C(0xC, 0xFF)
    Return()

    # Function_14_2C07 end

    def Function_15_2D3C(): pass

    label("Function_15_2D3C")

    EventBegin(0x0)
    Fade(500)
    OP_68(5960, 1000, -720, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18000, 0)
    SetChrPos(0x101, 1660, 0, -200, 90)
    SetChrPos(0x102, 1860, 0, 1200, 90)
    SetChrPos(0x104, 1660, 0, -1610, 90)
    SetChrPos(0x109, 730, 0, 610, 90)
    SetChrPos(0x105, 330, 0, -1000, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_4B(0xD, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_4B(0xC, 0xFF)
    OP_4B(0x8, 0xFF)
    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_0D()

    ChrTalk(
        0x9,
        "I see... So Mr. Wald is...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Yes, he didn't even give us a glance\x01",
            "and went to the store while wobbling...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "He bought a lot,\x01",
            "so maybe he's\x01",
            "drinking at home...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Honestly... \x01",
            "I didn't want to see\x01",
            "Mr. Wald like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I don't believe that guy has...\x01",
            "...Been swallowed up by alcohol...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "...Yeah, I feel the same.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Anyway... Getting\x01",
            "smashed in the middle of\x01",
            "the street isn't good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Let's keep that in\x01",
            "mind, everybody.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Oss!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Roger!\x02",
    )

    CloseMessageWindow()
    OP_68(1930, 1000, -40, 1500)
    OP_6F(0x1)

    ChrTalk(
        0x101,
        "#00005FWald did that...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#00301FDrinkin' away one's worries, they call it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FBecause of the amount, \x01",
            "I'm concerned for his health...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10308F............\x02",
    )

    CloseMessageWindow()
    OP_5A()
    OP_4C(0xD, 0xFF)
    OP_4C(0x9, 0xFF)
    OP_4C(0xC, 0xFF)
    OP_4C(0x8, 0xFF)
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    SetScenarioFlags(0x14D, 1)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 500, 0, 0, 90)
    ModifyEventFlags(0, 0, 0x80)
    EventEnd(0x5)
    Return()

    # Function_15_2D3C end

    def Function_16_30CB(): pass

    label("Function_16_30CB")

    OP_4B(0xD, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_4B(0xC, 0xFF)

    ChrTalk(
        0x9,
        (
            "Listen up! If anything happens, you\x01",
            "call Luganov or I immediately. Got it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Oss!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Roger!\x02",
    )

    CloseMessageWindow()
    OP_4C(0xD, 0xFF)
    OP_4C(0x9, 0xFF)
    OP_4C(0xC, 0xFF)
    Return()

    # Function_16_30CB end

    def Function_17_314A(): pass

    label("Function_17_314A")

    OP_4B(0xD, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_4B(0xC, 0xFF)
    TurnDirection(0xD, 0x0, 0)
    TurnDirection(0xC, 0x0, 0)
    TurnDirection(0x9, 0x0, 0)

    ChrTalk(
        0xD,
        "Y-You guys...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "The Special Support Section... And Wazy!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...Looks like you guys aren't going\x01",
            "to be able to see Mr. Wald.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x105,
        "#10305FWhat's wrong with Wald?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Y-You see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Shut up, Dino. We've\x01",
            "nothing to say to cowardly\x01",
            "police dogs like them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "If you got it, get out of here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10303F...Oh boy.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x137, 4)
    OP_93(0x9, 0xE1, 0x0)
    OP_93(0xC, 0x87, 0x0)
    OP_93(0xD, 0x13B, 0x0)
    ClearChrFlags(0x9, 0x10)
    ClearChrFlags(0xD, 0x10)
    OP_4C(0xD, 0xFF)
    OP_4C(0x9, 0xFF)
    OP_4C(0xC, 0xFF)
    Return()

    # Function_17_314A end

    def Function_18_32F4(): pass

    label("Function_18_32F4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3305")
    Jump("loc_36AD")

    label("loc_3305")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_3353")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3320")
    Call(0, 11)
    Jump("loc_334E")

    label("loc_3320")


    ChrTalk(
        0xFE,
        (
            "(Somehow, Mr. Jed\x01",
            "looks hesitant too...)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_334E")

    Jump("loc_36AD")

    label("loc_3353")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3361")
    Jump("loc_36AD")

    label("loc_3361")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_336F")
    Jump("loc_36AD")

    label("loc_336F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_33FB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_338A")
    Call(0, 12)
    Jump("loc_33F6")

    label("loc_338A")


    ChrTalk(
        0xFE,
        (
            "An unidentified armed group, huh...\x01",
            "If we were to attack them, we'd get\x01",
            "our asses handed to us, I bet.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33F6")

    Jump("loc_36AD")

    label("loc_33FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3435")

    ChrTalk(
        0xFE,
        (
            "Mr. Luganov... \x01",
            "He was seriously cool.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36AD")

    label("loc_3435")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3498")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16E, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3450")
    Call(0, 5)
    Jump("loc_3493")

    label("loc_3450")


    ChrTalk(
        0xFE,
        (
            "100,000 mira... Just how did he get\x01",
            "his hands on that sum...?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3493")

    Jump("loc_36AD")

    label("loc_3498")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3531")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34B3")
    Call(0, 6)
    Jump("loc_352C")

    label("loc_34B3")


    ChrTalk(
        0xFE,
        (
            "I tried asking people,\x01",
            "but no one's seen him\x01",
            "around recently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't want to think he's\x01",
            "left the city, but...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_352C")

    Jump("loc_36AD")

    label("loc_3531")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3542")
    Call(0, 7)
    Jump("loc_36AD")

    label("loc_3542")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3553")
    Call(0, 8)
    Jump("loc_36AD")

    label("loc_3553")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3646")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3607")

    ChrTalk(
        0xFE,
        (
            "*sigh*... That weird\x01",
            "guy back there dampened\x01",
            "our spirits, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...It won't happen again.\x01",
            "We'll remember this, Wazy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10303F............\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3641")

    label("loc_3607")


    ChrTalk(
        0xFE,
        (
            "...It won't happen again.\x01",
            "We'll remember this, Wazy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3641")

    Jump("loc_36AD")

    label("loc_3646")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3693")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3661")
    Call(0, 19)
    Jump("loc_368E")

    label("loc_3661")


    ChrTalk(
        0xFE,
        (
            "Y-You... Think a\x01",
            "little more seriously!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_368E")

    Jump("loc_36AD")

    label("loc_3693")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_36A4")
    Call(0, 20)
    Jump("loc_36AD")

    label("loc_36A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_36AD")

    label("loc_36AD")

    TalkEnd(0xFE)
    Return()

    # Function_18_32F4 end

    def Function_19_36B1(): pass

    label("Function_19_36B1")

    OP_4B(0xB, 0xFF)
    OP_4B(0xA, 0xFF)

    ChrTalk(
        0xA,
        "And, any good ideas?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Yeah! This morning, I spotted\x01",
            "a Sister carrying a mountain\x01",
            "of bread here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "And, she was super cute!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "...Yeah? And just how\x01",
            "is Mr. Wald going to\x01",
            "be connected with that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "And so, I was thinking\x01",
            "we'd go to the church to\x01",
            "hit up on this Sister...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xA,
        "Are you high!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Just why the hell would\x01",
            "we ever go to a church!?\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xB, 0xFF)
    OP_4C(0xA, 0xFF)
    SetScenarioFlags(0x0, 2)
    SetScenarioFlags(0x0, 3)
    Return()

    # Function_19_36B1 end

    def Function_20_384A(): pass

    label("Function_20_384A")

    OP_4B(0xB, 0xFF)
    OP_4B(0xA, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A16")

    ChrTalk(
        0xB,
        (
            "*sigh*, Mr. Wald was\x01",
            "really scary this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "And... Just why is Mr.\x01",
            "Wald so obsessed over\x01",
            "that jerk of Wazy?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Anyway, the most annoying\x01",
            "guy has gone away. Shouldn't\x01",
            "he rather be celebrating...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Hey, Slash! Don't say\x01",
            "anything careless.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "We're a million years too early\x01",
            "to be questioning Mr. Wald.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "More importantly, we've gotta think\x01",
            "of how to get him out of this mood!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Y-Yeah. But I\x01",
            "have no idea...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3A8C")

    label("loc_3A16")


    ChrTalk(
        0xA,
        (
            "Man, what if Mr. Wald heard you!\x01",
            "He'd beat you half to death, right?\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "S-Sorry. I won't say\x01",
            "anything more...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A8C")

    OP_4C(0xB, 0xFF)
    OP_4C(0xA, 0xFF)
    Return()

    # Function_20_384A end

    def Function_21_3A95(): pass

    label("Function_21_3A95")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3AA6")
    Jump("loc_3E0E")

    label("loc_3AA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_3AE0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3AC1")
    Call(0, 11)
    Jump("loc_3ADB")

    label("loc_3AC1")


    ChrTalk(
        0xFE,
        "Hyaha, he got mad...\x02",
    )

    CloseMessageWindow()

    label("loc_3ADB")

    Jump("loc_3E0E")

    label("loc_3AE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3AEE")
    Jump("loc_3E0E")

    label("loc_3AEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3AFC")
    Jump("loc_3E0E")

    label("loc_3AFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3B7A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B17")
    Call(0, 12)
    Jump("loc_3B75")

    label("loc_3B17")


    ChrTalk(
        0xFE,
        (
            "Umm... Where'd I put\x01",
            "the hammer and nails?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Let's reinforce our\x01",
            "clubs, just in case.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B75")

    Jump("loc_3E0E")

    label("loc_3B7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3BAC")

    ChrTalk(
        0xFE,
        (
            "Man, our seniors\x01",
            "are the best!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E0E")

    label("loc_3BAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3C0A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16E, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BC7")
    Call(0, 5)
    Jump("loc_3C05")

    label("loc_3BC7")


    ChrTalk(
        0xFE,
        (
            "But there's a lot I don't get.\x01",
            "Someone explain it to me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C05")

    Jump("loc_3E0E")

    label("loc_3C0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3C87")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C25")
    Call(0, 6)
    Jump("loc_3C82")

    label("loc_3C25")


    ChrTalk(
        0xFE,
        (
            "As usual, it looks like he's\x01",
            "not come back at his home... \x01",
            "I wonder where he's staying.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C82")

    Jump("loc_3E0E")

    label("loc_3C87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3C98")
    Call(0, 7)
    Jump("loc_3E0E")

    label("loc_3C98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3CA9")
    Call(0, 8)
    Jump("loc_3E0E")

    label("loc_3CA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3D99")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D3F")

    ChrTalk(
        0xFE,
        (
            "Hyaha. There's weird people\x01",
            "all over this world, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Huh? Come to think of it,\x01",
            "weren't Huey and me fighting?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3D94")

    label("loc_3D3F")


    ChrTalk(
        0xFE,
        "...Well, I won't sweat the small stuff.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've got to think of\x01",
            "Mr. Wald now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D94")

    Jump("loc_3E0E")

    label("loc_3D99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3DF4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DB4")
    Call(0, 19)
    Jump("loc_3DEF")

    label("loc_3DB4")


    ChrTalk(
        0xFE,
        (
            "I-It's because you aren't\x01",
            "giving me proper ideas too!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3DEF")

    Jump("loc_3E0E")

    label("loc_3DF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3E05")
    Call(0, 20)
    Jump("loc_3E0E")

    label("loc_3E05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3E0E")

    label("loc_3E0E")

    TalkEnd(0xFE)
    Return()

    # Function_21_3A95 end

    def Function_22_3E12(): pass

    label("Function_22_3E12")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3EB3")

    ChrTalk(
        0xFE,
        (
            "Until Mr. Wald gets back,\x01",
            "leaders Jed and Luganov are\x01",
            "holding the Vipers together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We've got to work together\x01",
            "and protect the Vipers.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_40E3")

    label("loc_3EB3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_3EC1")
    Jump("loc_40E3")

    label("loc_3EC1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3ECF")
    Jump("loc_40E3")

    label("loc_3ECF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3EDD")
    Jump("loc_40E3")

    label("loc_3EDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3F2E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3EF8")
    Call(0, 23)
    Jump("loc_3F29")

    label("loc_3EF8")


    ChrTalk(
        0xFE,
        (
            "I wonder what Mr. Wald's\x01",
            "doing right now...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F29")

    Jump("loc_40E3")

    label("loc_3F2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3FDA")

    ChrTalk(
        0xFE,
        (
            "Now that I think about it,\x01",
            "our leaders have been in the\x01",
            "Vipers since its founding.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They're probably even more worried\x01",
            "about Mr. Wald than we are...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_40E3")

    label("loc_3FDA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_4032")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16E, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3FF5")
    Call(0, 5)
    Jump("loc_402D")

    label("loc_3FF5")


    ChrTalk(
        0xFE,
        (
            "Mr. Wald... Who could you be\x01",
            "with instead of us...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_402D")

    Jump("loc_40E3")

    label("loc_4032")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4040")
    Jump("loc_40E3")

    label("loc_4040")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4051")
    Call(0, 13)
    Jump("loc_40E3")

    label("loc_4051")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4062")
    Call(0, 14)
    Jump("loc_40E3")

    label("loc_4062")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4073")
    Call(0, 16)
    Jump("loc_40E3")

    label("loc_4073")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_40A9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14D, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_408E")
    Call(0, 9)
    Jump("loc_40A4")

    label("loc_408E")


    ChrTalk(
        0xFE,
        "S-Scram already!\x02",
    )

    CloseMessageWindow()

    label("loc_40A4")

    Jump("loc_40E3")

    label("loc_40A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_40DA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x137, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_40C4")
    Call(0, 17)
    Jump("loc_40D5")

    label("loc_40C4")


    ChrTalk(
        0xFE,
        "Mr. Wald...\x02",
    )

    CloseMessageWindow()

    label("loc_40D5")

    Jump("loc_40E3")

    label("loc_40DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_40E3")

    label("loc_40E3")

    TalkEnd(0xFE)
    Return()

    # Function_22_3E12 end

    def Function_23_40E7(): pass

    label("Function_23_40E7")

    OP_4B(0xD, 0xFF)
    OP_4B(0xC, 0xFF)

    ChrTalk(
        0xD,
        (
            "Mr. Wald... As expected,\x01",
            "he's not around today too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "That's right... There's\x01",
            "some kind of huge ruckus.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "...Anyway, I\x01",
            "hope he's safe.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    SetScenarioFlags(0x0, 5)
    ClearChrFlags(0xD, 0x10)
    ClearChrFlags(0xC, 0x10)
    OP_4C(0xD, 0xFF)
    OP_4C(0xC, 0xFF)
    Return()

    # Function_23_40E7 end

    def Function_24_419A(): pass

    label("Function_24_419A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_41AB")
    Jump("loc_46BF")

    label("loc_41AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_41B9")
    Jump("loc_46BF")

    label("loc_41B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_41C7")
    Jump("loc_46BF")

    label("loc_41C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_44E6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18D, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4497")
    OP_4B(0xFE, 0xFF)

    ChrTalk(
        0xFE,
        "Mr. Wald... Everyone...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108F...Dino...\x02",
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xFE, 0x0, 500)

    ChrTalk(
        0xFE,
        "...Oh, the Special Support Section, huh.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FYour other members are...\x01",
            "...Still hospitalized, aren't they?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Yeah, everyone but me...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Mr. Kｷki had it especially bad...\x01",
            "He's in a different room than\x01",
            "everyone else... *cry*...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008FI'm sorry... That was a little insensitive.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*cry*... I... I don't\x01",
            "need your sympathy!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The others have to endure this\x01",
            "pain! Why was only I spared!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*cry*... Dammit! Why... Why\x01",
            "did it have to be like this...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00208F(Mr. Lloyd. We should\x01",
            "leave him alone right now.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003F(Yeah... I agree.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10308F(............)\x02",
    )

    CloseMessageWindow()
    OP_93(0xFE, 0x87, 0x0)
    OP_4C(0xFE, 0xFF)
    SetScenarioFlags(0x18D, 3)
    Jump("loc_44E1")

    label("loc_4497")


    ChrTalk(
        0xFE,
        "Mr. Wald... Everyone...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Why... Why'd it have to be like this...\x02",
    )

    CloseMessageWindow()

    label("loc_44E1")

    Jump("loc_46BF")

    label("loc_44E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_455C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4501")
    Call(0, 23)
    Jump("loc_4557")

    label("loc_4501")


    ChrTalk(
        0xFE,
        "Gnosis, huh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Revache's not around\x01",
            "anymore though, so\x01",
            "just where did he...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4557")

    Jump("loc_46BF")

    label("loc_455C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_45D6")

    ChrTalk(
        0xFE,
        "Hehe, our seniors are so great.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The times are what they're, but...\x01",
            "I'm kinda glad they're around.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_46BF")

    label("loc_45D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_463E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16E, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_45F1")
    Call(0, 5)
    Jump("loc_4639")

    label("loc_45F1")


    ChrTalk(
        0xFE,
        (
            "Ooh... Mr. Wald. I can't believe\x01",
            "he's doing something dangerous...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4639")

    Jump("loc_46BF")

    label("loc_463E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_464F")
    Call(0, 13)
    Jump("loc_46BF")

    label("loc_464F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4660")
    Call(0, 14)
    Jump("loc_46BF")

    label("loc_4660")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4671")
    Call(0, 16)
    Jump("loc_46BF")

    label("loc_4671")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_46BF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x137, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_468C")
    Call(0, 17)
    Jump("loc_46BF")

    label("loc_468C")


    ChrTalk(
        0xFE,
        (
            "L-Like Mr. Jed says, \x01",
            "we have nothing to say.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_46BF")

    TalkEnd(0xFE)
    Return()

    # Function_24_419A end

    def Function_25_46C3(): pass

    label("Function_25_46C3")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(8510, 900, 300, 0)
    MoveCamera(48, 19, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18000, 0)
    SetChrPos(0x101, 1000, 0, -700, 90)
    SetChrPos(0x105, 1000, 0, 700, 90)
    SetChrPos(0x102, 500, 0, -700, 90)
    SetChrPos(0x103, 500, 0, 700, 90)
    SetChrPos(0x109, 0, 0, -700, 90)
    SetChrPos(0x104, 0, 0, 700, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    FadeToBright(500, 0)
    OP_0D()
    Sleep(500)

    def lambda_4789():
        OP_96(0xFE, 0x1C20, 0x0, 0xFFFFFD44, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4789)
    Sleep(400)

    def lambda_47A6():
        OP_96(0xFE, 0x1CE8, 0x0, 0x2BC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_47A6)
    Sleep(400)

    def lambda_47C3():
        OP_96(0xFE, 0x170C, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_47C3)
    Sleep(400)

    def lambda_47E0():
        OP_96(0xFE, 0x1900, 0x0, 0x4B0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_47E0)
    Sleep(400)

    def lambda_47FD():
        OP_96(0xFE, 0x12C0, 0x0, 0xFFFFFD44, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_47FD)
    Sleep(400)

    def lambda_481A():
        OP_96(0xFE, 0x13EC, 0x0, 0x2BC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_481A)
    Sleep(400)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x105, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x109, 1)
    WaitChrThread(0x104, 1)
    OP_4B(0xD, 0xFF)
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_4B(0xA, 0xFF)
    OP_4B(0xC, 0xFF)
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_48A0():

        label("loc_48A0")

        TurnDirection(0xFE, 0x0, 500)
        Yield()
        Jump("loc_48A0")

    QueueWorkItem2(0x9, 2, lambda_48A0)

    def lambda_48B2():

        label("loc_48B2")

        TurnDirection(0xFE, 0x0, 500)
        Yield()
        Jump("loc_48B2")

    QueueWorkItem2(0xC, 2, lambda_48B2)

    def lambda_48C4():

        label("loc_48C4")

        TurnDirection(0xFE, 0x0, 500)
        Yield()
        Jump("loc_48C4")

    QueueWorkItem2(0xD, 2, lambda_48C4)

    ChrTalk(
        0x9,
        "#11PThe fuzz... So you're here again.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#11PCould you be looking for new info?\x02",
    )

    CloseMessageWindow()

    def lambda_492D():

        label("loc_492D")

        TurnDirection(0xFE, 0x0, 500)
        Yield()
        Jump("loc_492D")

    QueueWorkItem2(0x8, 2, lambda_492D)

    def lambda_493F():

        label("loc_493F")

        TurnDirection(0xFE, 0x0, 500)
        Yield()
        Jump("loc_493F")

    QueueWorkItem2(0xB, 2, lambda_493F)

    def lambda_4951():

        label("loc_4951")

        TurnDirection(0xFE, 0x0, 500)
        Yield()
        Jump("loc_4951")

    QueueWorkItem2(0xA, 2, lambda_4951)
    OP_63(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_497E():

        label("loc_497E")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_497E")

    QueueWorkItem2(0xD, 2, lambda_497E)

    ChrTalk(
        0xD,
        "#11P...Hey, you're Wazy!\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x105,
        "#6P#10308F............\x02",
    )

    CloseMessageWindow()

    def lambda_4A51():

        label("loc_4A51")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_4A51")

    QueueWorkItem2(0x8, 2, lambda_4A51)

    def lambda_4A63():

        label("loc_4A63")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_4A63")

    QueueWorkItem2(0xB, 2, lambda_4A63)

    def lambda_4A75():

        label("loc_4A75")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_4A75")

    QueueWorkItem2(0xA, 2, lambda_4A75)

    def lambda_4A87():

        label("loc_4A87")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_4A87")

    QueueWorkItem2(0x9, 2, lambda_4A87)

    def lambda_4A99():

        label("loc_4A99")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_4A99")

    QueueWorkItem2(0xC, 2, lambda_4A99)

    ChrTalk(
        0xA,
        "#5PY-You...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5PHow shameless...\x01",
            "It's because of you that Mr. Wald...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00001F(Damn... They're sure in a bad mood.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#00208F(It might have been a bad idea to come...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5P............\x02",
    )

    CloseMessageWindow()
    EndChrThread(0x8, 0x2)
    SetChrFlags(0x8, 0x40)

    def lambda_4B8A():
        OP_96(0xFE, 0x215C, 0x0, 0x2BC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_4B8A)
    WaitChrThread(0x8, 1)
    TurnDirection(0x8, 0x105, 500)
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(30)
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(30)
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(30)
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(30)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(30)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(30)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(30)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(30)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x9,
        "#11PHey, Luganov?\x02",
    )

    CloseMessageWindow()

    def lambda_4C83():

        label("loc_4C83")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_4C83")

    QueueWorkItem2(0x101, 2, lambda_4C83)

    def lambda_4C95():

        label("loc_4C95")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_4C95")

    QueueWorkItem2(0x102, 2, lambda_4C95)

    def lambda_4CA7():

        label("loc_4CA7")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_4CA7")

    QueueWorkItem2(0x103, 2, lambda_4CA7)

    def lambda_4CB9():

        label("loc_4CB9")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_4CB9")

    QueueWorkItem2(0x109, 2, lambda_4CB9)

    def lambda_4CCB():

        label("loc_4CCB")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_4CCB")

    QueueWorkItem2(0x104, 2, lambda_4CCB)

    def lambda_4CDD():

        label("loc_4CDD")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_4CDD")

    QueueWorkItem2(0x105, 2, lambda_4CDD)

    def lambda_4CEF():
        OP_95(0xFE, 8039, 0, 570, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_4CEF)
    Sleep(50)
    WaitChrThread(0x8, 1)
    EndChrThread(0x105, 0x2)
    SetChrFlags(0x105, 0x20)
    SetChrFlags(0x105, 0x4)
    Sound(802, 0, 100, 0)

    def lambda_4D24():
        OP_A6(0xFE, 0x0, 0x64, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_4D24)

    def lambda_4D3D():
        OP_96(0xFE, 0x1CE8, 0xC8, 0x2BC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_4D3D)
    WaitChrThread(0x105, 1)
    WaitChrThread(0x105, 2)
    ClearChrFlags(0x105, 0x20)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    BeginChrThread(0x101, 3, 0, 26)
    Sleep(50)
    BeginChrThread(0x102, 3, 0, 26)
    Sleep(50)
    BeginChrThread(0x103, 3, 0, 26)
    Sleep(50)
    BeginChrThread(0x109, 3, 0, 26)
    Sleep(50)
    BeginChrThread(0x104, 3, 0, 26)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x109, 3)
    WaitChrThread(0x104, 3)
    Sleep(1000)

    ChrTalk(
        0x105,
        "#6P#10310F............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00011FH-Hey...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10111FWazy...!\x02",
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    ChrTalk(
        0x8,
        (
            "#4S#11PHey, Wazy!\x01",
            "You know, don't you!?\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    ChrTalk(
        0x8,
        (
            "#4S#11POf all things, Mr. Wald\x01",
            "took that drug!?\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    ChrTalk(
        0x8,
        (
            "#4S#11PThis is your fault too...\x01",
            "Everything is all your fault!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00101F(L-Lloyd... How much\x01",
            "did you tell them...?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003F(Well, I definitely didn't tell\x01",
            "them about demonize, but...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#N#10108F(...But, we told them there's a possibility\x01",
            "Wald may have been dosed with Gnosis.)\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x8,
        (
            "#11P...Two years ago... If you\x01",
            "hadn't come then, we would've\x01",
            "had our fun this whole time...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PBut then you came along...\x01",
            "And now you're with the police\x01",
            "for some strange reason.\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    ChrTalk(
        0x8,
        "#11P#4S...You get it, right?!!#3S\x02",
    )

    CloseMessageWindow()

    def lambda_519D():
        OP_A6(0xFE, 0x32, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_519D)
    WaitChrThread(0x105, 2)

    ChrTalk(
        0x105,
        (
            "#6P#10303F...It wasn't for no reason. \x01",
            "I chose this path because there's\x01",
            "something I need to do.\x02\x03",
            "#10308FWald becoming like that\x01",
            "as a result...was an\x01",
            "unforeseen consequence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00303F...Wazy...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11P...So you don't deny it?\x02",
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    ChrTalk(
        0x8,
        "#11P#4SBring it on! I'll destroy you!#3S\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#00210F!!\x02",
    )

    CloseMessageWindow()

    def lambda_52FA():
        OP_A6(0xFE, 0x32, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_52FA)
    WaitChrThread(0x105, 2)
    Sleep(500)
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xFFFF)
    Sound(811, 0, 100, 0)

    def lambda_5338():
        OP_9D(0xFE, 0x1A2C, 0x0, 0x2BC, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5338)
    ClearChrFlags(0x105, 0x4)
    ClearChrFlags(0x8, 0x40)
    WaitChrThread(0x105, 1)
    Sleep(500)

    ChrTalk(
        0x102,
        "#N#6P#00105FAh...\x02",
    )

    CloseMessageWindow()
    OP_5A()

    def lambda_537E():

        label("loc_537E")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_537E")

    QueueWorkItem2(0x101, 2, lambda_537E)

    def lambda_5390():

        label("loc_5390")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_5390")

    QueueWorkItem2(0x102, 2, lambda_5390)

    def lambda_53A2():

        label("loc_53A2")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_53A2")

    QueueWorkItem2(0x103, 2, lambda_53A2)

    def lambda_53B4():

        label("loc_53B4")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_53B4")

    QueueWorkItem2(0x109, 2, lambda_53B4)

    def lambda_53C6():

        label("loc_53C6")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_53C6")

    QueueWorkItem2(0x104, 2, lambda_53C6)

    ChrTalk(
        0xC,
        "#11PHuh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10305F...What're you planning?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P...We're just speaking our mind.\x01",
            "Our voices can't reach him right\x01",
            "now. If anyone's can... it's yours.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P...Listen up, you owe me a punch.\x01",
            "Instead of punching you...\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    ChrTalk(
        0x8,
        (
            "#4S#11PTake responsibility, and\x01",
            "wake up Mr. Wald for us!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11PLuganov...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#11PS-Senior...\x02",
    )

    CloseMessageWindow()
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x105)

    ChrTalk(
        0x105,
        (
            "#6P#10308F...Hu hu, so that's how it is.\x02\x03",
            "#10303F............\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5599():

        label("loc_5599")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_5599")

    QueueWorkItem2(0x101, 2, lambda_5599)

    def lambda_55AB():

        label("loc_55AB")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_55AB")

    QueueWorkItem2(0x102, 2, lambda_55AB)

    def lambda_55BD():

        label("loc_55BD")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_55BD")

    QueueWorkItem2(0x103, 2, lambda_55BD)

    def lambda_55CF():

        label("loc_55CF")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_55CF")

    QueueWorkItem2(0x109, 2, lambda_55CF)

    def lambda_55E1():

        label("loc_55E1")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_55E1")

    QueueWorkItem2(0x104, 2, lambda_55E1)

    ChrTalk(
        0x101,
        "#12P#00005FWazy...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10303F...I can't promise you anything, but...\x01",
            "I'll do everything in my power to.\x02\x03",
            "#10301FIn the sense that...\x01",
            "I will settle things properly\x01",
            "as the Testaments' leader.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x109, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x109, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x8, 0x2)
    EndChrThread(0x9, 0x2)
    EndChrThread(0xA, 0x2)
    EndChrThread(0xB, 0x2)
    EndChrThread(0xC, 0x2)
    EndChrThread(0xD, 0x2)
    EndChrThread(0x8, 0x1)
    EndChrThread(0x9, 0x1)
    EndChrThread(0xA, 0x1)
    EndChrThread(0xB, 0x1)
    EndChrThread(0xC, 0x1)
    EndChrThread(0xD, 0x1)
    SetChrPos(0x8, 16290, 1000, -1650, 315)
    SetChrPos(0x9, 15290, 1000, -650, 135)
    SetChrPos(0xA, 11110, 0, -5220, 315)
    SetChrPos(0xB, 9940, 0, -4200, 135)
    SetChrPos(0xC, 7030, 0, -50, 180)
    SetChrPos(0xD, 7320, 0, -1690, 0)
    OP_4C(0x8, 0xFF)
    OP_4C(0xD, 0xFF)
    OP_4C(0x9, 0xFF)
    OP_4C(0xB, 0xFF)
    OP_4C(0xA, 0xFF)
    OP_4C(0xC, 0xFF)
    SetChrPos(0x0, 2500, 0, -590, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x16F, 1)
    EventEnd(0x5)
    Return()

    # Function_25_46C3 end

    def Function_26_57C6(): pass

    label("Function_26_57C6")


    def lambda_57CB():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFE0C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_57CB)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_26_57C6 end

    SaveToFile()

Try(main)
