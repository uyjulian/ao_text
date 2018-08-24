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
        "Function_5_FB9",          # 05, 5
        "Function_6_14F9",         # 06, 6
        "Function_7_167A",         # 07, 7
        "Function_8_17CC",         # 08, 8
        "Function_9_1A1F",         # 09, 9
        "Function_10_1F04",        # 0A, 10
        "Function_11_2494",        # 0B, 11
        "Function_12_262D",        # 0C, 12
        "Function_13_2798",        # 0D, 13
        "Function_14_2A65",        # 0E, 14
        "Function_15_2BA9",        # 0F, 15
        "Function_16_2F31",        # 10, 16
        "Function_17_2FB0",        # 11, 17
        "Function_18_3157",        # 12, 18
        "Function_19_3519",        # 13, 19
        "Function_20_369D",        # 14, 20
        "Function_21_38D9",        # 15, 21
        "Function_22_3C40",        # 16, 22
        "Function_23_3F01",        # 17, 23
        "Function_24_3FAF",        # 18, 24
        "Function_25_44D0",        # 19, 25
        "Function_26_55C4",        # 1A, 26
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_B3C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_ABE")

    ChrTalk(
        0xFE,
        "Yes, yes!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't know if I'm uneasy!! I\x01",
            "don't have time to care about\x01",
            "incomprehensible things!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I could even sing a\x01",
            "song! Yes!! Yahoo!!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_B37")

    label("loc_ABE")


    ChrTalk(
        0xFE,
        (
            "What kind of wind brought\x01",
            "that huge tree! I don't\x01",
            "know if I'm uneasy!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I could even sing a\x01",
            "song! Yes!! Yahoo!!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B37")

    Jump("loc_FB5")

    label("loc_B3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_B4A")
    Jump("loc_FB5")

    label("loc_B4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_B58")
    Jump("loc_FB5")

    label("loc_B58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_B66")
    Jump("loc_FB5")

    label("loc_B66")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_BD8")

    ChrTalk(
        0xFE,
        (
            "Woooah, this is so\x01",
            "irritating!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "An armed group at Mainz!?\x01",
            "More importantly, where's\x01",
            "Wald!?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FB5")

    label("loc_BD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_C1A")

    ChrTalk(
        0xFE,
        (
            "Hmph, let me just say\x01",
            "this. We need his fists.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FB5")

    label("loc_C1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_C9D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16E, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C35")
    Call(0, 5)
    Jump("loc_C98")

    label("loc_C35")


    ChrTalk(
        0xFE,
        (
            "Wald... Did he hit it\x01",
            "big at the casino?\x02",
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

    label("loc_C98")

    Jump("loc_FB5")

    label("loc_C9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_CF5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CB8")
    Call(0, 6)
    Jump("loc_CF0")

    label("loc_CB8")


    ChrTalk(
        0xFE,
        (
            "*sigh*, even so, it's\x01",
            "boring when Wald's not\x01",
            "here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CF0")

    Jump("loc_FB5")

    label("loc_CF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_D06")
    Call(0, 7)
    Jump("loc_FB5")

    label("loc_D06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_D17")
    Call(0, 8)
    Jump("loc_FB5")

    label("loc_D17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_E3C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DCB")

    ChrTalk(
        0xFE,
        (
            "Wald!! I'm begging you!\x01",
            "Show your face!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We'll buy you alcohol,\x01",
            "so let's enjoy it here!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Without you here,\x01",
            "nothing can begin, you\x01",
            "know!?!?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_E37")

    label("loc_DCB")


    ChrTalk(
        0xFE,
        (
            "We'll buy you alcohol,\x01",
            "so let's enjoy it here!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Without you here,\x01",
            "nothing can begin, you\x01",
            "know!?!?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E37")

    Jump("loc_FB5")

    label("loc_E3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_EB6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14D, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E57")
    Call(0, 9)
    Jump("loc_EB1")

    label("loc_E57")


    ChrTalk(
        0xFE,
        (
            "I don't believe this...\x01",
            "I don't believe it!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's a joke I just\x01",
            "can't stand!!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EB1")

    Jump("loc_FB5")

    label("loc_EB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_FAC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F44")

    ChrTalk(
        0xFE,
        "Yes, yes!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Those damn Testaments!\x01",
            "Now it's our chance to\x01",
            "take them out!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#4S...Yeeeeah!! Yahoo!!#3S\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_FA7")

    label("loc_F44")


    ChrTalk(
        0xFE,
        (
            "Those damn Testaments!\x01",
            "Now it's our chance to\x01",
            "take them out!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#4S...Yeeeeah!! Yahoo!!#3S\x02",
    )

    CloseMessageWindow()

    label("loc_FA7")

    Jump("loc_FB5")

    label("loc_FAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_FB5")

    label("loc_FB5")

    TalkEnd(0xFE)
    Return()

    # Function_4_A07 end

    def Function_5_FB9(): pass

    label("Function_5_FB9")

    OP_4B(0xD, 0xFF)
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_4B(0xA, 0xFF)
    OP_4B(0xC, 0xFF)

    ChrTalk(
        0x9,
        (
            "Hey, you guys. How's\x01",
            "that investigation?\x02",
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
            "That Kanon kid said she\x01",
            "saw Wald...\x02",
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
        "Shit, 100,000!?\x02",
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
            "W-Wald... Just where did\x01",
            "he get that kind of\x01",
            "mira?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I'm worried about that,\x01",
            "but... Kｷki, did you say\x01",
            "communicator?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "In other words... Wald's\x01",
            "been in contact with\x01",
            "someone.\x02",
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
            "Yeah. I didn't get the\x01",
            "details from them,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Yeah, but it seemed like\x01",
            "Wald was smiling\x01",
            "happily...\x02",
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
        (
            "I guess something good\x01",
            "happened...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I can't believe Wald\x01",
            "abandoned us... That\x01",
            "can't be right, right?\x02",
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
            "Hey, you and Slash. Shut\x01",
            "your traps.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "But if you wanna die, I\x01",
            "guess it's a different\x01",
            "story.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xB)
    TurnDirection(0xB, 0x8, 0)

    ChrTalk(
        0xB,
        "W-We're sorry!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001F(So Wald has an ENIGMA,\x01",
            "huh... That's indeed\x01",
            "worrying.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F(Yes. Not that many\x01",
            "ENIGMAs have been sold to\x01",
            "the general public yet.)\x02",
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

    # Function_5_FB9 end

    def Function_6_14F9(): pass

    label("Function_6_14F9")

    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_4B(0xA, 0xFF)

    ChrTalk(
        0x8,
        (
            "Hey Jed. Have Kｷki or\x01",
            "Dino come by?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Wait a little longer.\x01",
            "They need to do an\x01",
            "additional investigation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "By the way, it seems\x01",
            "yours didn't go well,\x01",
            "huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Well, I...\x02",
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
            "We looked everywhere we\x01",
            "could think of, but no one\x01",
            "has seen him recently...\x02",
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
            "Wald... Seriously, where\x01",
            "has he gone.\x02",
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

    # Function_6_14F9 end

    def Function_7_167A(): pass

    label("Function_7_167A")

    OP_4B(0x8, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_4B(0xA, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1729")

    ChrTalk(
        0x8,
        (
            "Ah, I guess we'll look\x01",
            "in places Wald might\x01",
            "have gone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The search area is the\x01",
            "whole city. We'll look\x01",
            "everywhere.\x02",
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
    Jump("loc_17BF")

    label("loc_1729")


    ChrTalk(
        0x8,
        (
            "If you spot Wald, get\x01",
            "back here immediately\x01",
            "and report.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you speak to him he\x01",
            "might ignore you again,\x01",
            "so don't fail.\x02",
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

    label("loc_17BF")

    OP_4C(0x8, 0xFF)
    OP_4C(0xB, 0xFF)
    OP_4C(0xA, 0xFF)
    Return()

    # Function_7_167A end

    def Function_8_17CC(): pass

    label("Function_8_17CC")

    OP_4B(0x8, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_4B(0xA, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19BE")

    ChrTalk(
        0x8,
        (
            "And? What are you guys\x01",
            "doing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Y-Yeah. About that, we\x01",
            "came to honestly\x01",
            "apologize...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "When you get like this,\x01",
            "no one could be any\x01",
            "stingier...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Shit, there's no choice\x01",
            "then! Those baldies are no\x01",
            "match for the likes of you!\x02",
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
            "Your mama's so fat!\x01",
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
    Jump("loc_1A12")

    label("loc_19BE")


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
        (
            "Hey hey hey! That's way\x01",
            "too soft!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A12")

    OP_4C(0x8, 0xFF)
    OP_4C(0xB, 0xFF)
    OP_4C(0xA, 0xFF)
    Return()

    # Function_8_17CC end

    def Function_9_1A1F(): pass

    label("Function_9_1A1F")

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
            "Kｷki... That story's\x01",
            "real, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Yeah, that's what the\x01",
            "kid said, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I don't believe it. No,\x01",
            "I can't believe it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "For Wald to get beat\x01",
            "like that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105F(...Are they talking\x01",
            "about the fight on that\x01",
            "rainy day?)\x02",
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
            "Y-You... What kind of\x01",
            "face is that!?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_1C87():
        TurnDirection(0x8, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1C87)
    TurnDirection(0xC, 0x105, 500)

    ChrTalk(
        0xC,
        "W-Wazy...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hyaha, you talkin' to\x01",
            "me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Fine, bring that face!\x01",
            "I'll turn it right back\x01",
            "at ya!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FH-Hey!\x02",
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
            "If we fight those kids\x01",
            "here, it'd make Wald\x01",
            "look bad!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "And, it's not what Wald\x01",
            "would have wanted!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Tch, shit!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x105, 500)

    ChrTalk(
        0xC,
        (
            "I don't know why you're\x01",
            "here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "We don't feel like\x01",
            "fighting you, so get out\x01",
            "of here, ok?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "But if you're here to\x01",
            "pick a fight, that's a\x01",
            "different story.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303FNo, we have no such\x01",
            "intentions.\x02\x03",
            "#10300FWe're bothering you,\x01",
            "huh. ...Let's go,\x01",
            "everyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FA-Alright...\x02",
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

    # Function_9_1A1F end

    def Function_10_1F04(): pass

    label("Function_10_1F04")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2062")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FE2")

    ChrTalk(
        0xFE,
        (
            "I still haven't forgiven\x01",
            "Wald.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...That's not the case, but...\x01",
            "It's certain the Saber Vipers\x01",
            "is a super fun place to be.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As a Viper leader...\x01",
            "That's reason enough to\x01",
            "protect it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_205D")

    label("loc_1FE2")


    ChrTalk(
        0xFE,
        (
            "I still haven't forgiven\x01",
            "Wald, but...\x02",
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

    label("loc_205D")

    Jump("loc_2490")

    label("loc_2062")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_20FB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_207D")
    Call(0, 11)
    Jump("loc_20F6")

    label("loc_207D")


    ChrTalk(
        0xFE,
        (
            "...Damn. Cooperating\x01",
            "with those baldies, of\x01",
            "all things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Luganov, Kｷki, Dino...\x01",
            "I've got to think about\x01",
            "them...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20F6")

    Jump("loc_2490")

    label("loc_20FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2109")
    Jump("loc_2490")

    label("loc_2109")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2117")
    Jump("loc_2490")

    label("loc_2117")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_21CD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2132")
    Call(0, 12)
    Jump("loc_21C8")

    label("loc_2132")


    ChrTalk(
        0xFE,
        (
            "Hmm? The Support Section...\x01",
            "It seems there's no\x01",
            "developments on either side.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Now listen here. If you\x01",
            "see Wald, you let us\x01",
            "know immediately.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21C8")

    Jump("loc_2490")

    label("loc_21CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_22B8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2273")

    ChrTalk(
        0xFE,
        (
            "...Luganov said the gist\x01",
            "of what we want to say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There's nothing else to\x01",
            "say. ...He's gone for\x01",
            "the day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10303F............\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_22B3")

    label("loc_2273")


    ChrTalk(
        0xFE,
        (
            "We've nothing else to\x01",
            "say to us. ...He's gone\x01",
            "for the day.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22B3")

    Jump("loc_2490")

    label("loc_22B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2309")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16E, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22D3")
    Call(0, 5)
    Jump("loc_2304")

    label("loc_22D3")


    ChrTalk(
        0xFE,
        (
            "Wald... Just what the\x01",
            "heck happened to you?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2304")

    Jump("loc_2490")

    label("loc_2309")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2354")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2324")
    Call(0, 6)
    Jump("loc_234F")

    label("loc_2324")


    ChrTalk(
        0xFE,
        (
            "Wald... Seriously, where\x01",
            "has he gone.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_234F")

    Jump("loc_2490")

    label("loc_2354")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2365")
    Call(0, 13)
    Jump("loc_2490")

    label("loc_2365")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2376")
    Call(0, 14)
    Jump("loc_2490")

    label("loc_2376")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2387")
    Call(0, 16)
    Jump("loc_2490")

    label("loc_2387")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_242C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14D, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23A2")
    Call(0, 9)
    Jump("loc_2427")

    label("loc_23A2")


    ChrTalk(
        0xFE,
        (
            "We've no quarrel with\x01",
            "you, so get out of here\x01",
            "already...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you stick around any\x01",
            "longer, I can't be sure\x01",
            "what will happen.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2427")

    Jump("loc_2490")

    label("loc_242C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2487")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x137, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2447")
    Call(0, 17)
    Jump("loc_2482")

    label("loc_2447")


    ChrTalk(
        0xFE,
        (
            "Listen, Wazy... I think\x01",
            "we'll be fine just like\x01",
            "this.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2482")

    Jump("loc_2490")

    label("loc_2487")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2490")

    label("loc_2490")

    TalkEnd(0xFE)
    Return()

    # Function_10_1F04 end

    def Function_11_2494(): pass

    label("Function_11_2494")

    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)

    ChrTalk(
        0x9,
        (
            "Those guys... To be\x01",
            "working with them, of\x01",
            "all things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "...Hey Jed. Isn't it bad\x01",
            "for us to be working\x01",
            "with them?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Hyaha, the heck are you\x01",
            "saying, Huey!? Vipers\x01",
            "strangle their traitors...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...He said he disbanded\x01",
            "the Vipers, didn't he,\x01",
            "idiot!?\x02",
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
            "...Anyway, I'm thinking\x01",
            "about it. Don't go doing\x01",
            "whatever the hell you want.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    ClearChrFlags(0xA, 0x10)
    ClearChrFlags(0xB, 0x10)
    SetScenarioFlags(0x0, 1)
    Return()

    # Function_11_2494 end

    def Function_12_262D(): pass

    label("Function_12_262D")

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
            "Yeah. It seems like everyone\x01",
            "in the city's talking about\x01",
            "how Mainz is occupied.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "It can't be... Is Wald\x01",
            "caught up in the\x01",
            "incident?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Well I don't think so,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Anyway guys, let's get\x01",
            "fired up today and\x01",
            "collect info.\x02",
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

    # Function_12_262D end

    def Function_13_2798(): pass

    label("Function_13_2798")

    OP_4B(0xD, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_4B(0xC, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29E1")

    ChrTalk(
        0xC,
        (
            "Wald... I wonder what\x01",
            "he's doing around now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Heck if I know... I\x01",
            "wonder if he'll be back\x01",
            "when I wake up...\x02",
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
            "The last was when Huey\x01",
            "and the others saw him\x01",
            "in Waterfront Area...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Yeah, and when we called\x01",
            "out to him, he ignored\x01",
            "us...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...Anyhow, something's\x01",
            "happened to Wald. Let's\x01",
            "split up and look for clues.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "You two handle Downtown.\x01",
            "Be sure to speak with\x01",
            "everyone.\x02",
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
            "#00005F(Wald... They don't know\x01",
            "where he is?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303F(I wonder why... I'm\x01",
            "worried.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2A58")

    label("loc_29E1")


    ChrTalk(
        0x9,
        (
            "Luganov and I will take\x01",
            "turns watching Ignis.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If you find anything,\x01",
            "return and report.\x02",
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
        "Right!\x02",
    )

    CloseMessageWindow()

    label("loc_2A58")

    OP_4C(0xD, 0xFF)
    OP_4C(0x9, 0xFF)
    OP_4C(0xC, 0xFF)
    Return()

    # Function_13_2798 end

    def Function_14_2A65(): pass

    label("Function_14_2A65")

    OP_4B(0xD, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_4B(0xC, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B34")

    ChrTalk(
        0x9,
        (
            "Well, have you seen Wald\x01",
            "since yesterday?\x02",
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
        "M-Me either.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Oh yeah. From how he was\x01",
            "yesterday, I think he'd have\x01",
            "a hangover around now, but...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2B9C")

    label("loc_2B34")


    ChrTalk(
        0x9,
        (
            "Right... I'll go check\x01",
            "on him at his home\x01",
            "later.\x02",
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

    label("loc_2B9C")

    OP_4C(0xD, 0xFF)
    OP_4C(0x9, 0xFF)
    OP_4C(0xC, 0xFF)
    Return()

    # Function_14_2A65 end

    def Function_15_2BA9(): pass

    label("Function_15_2BA9")

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
        "I see... So Wald is...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Yeah, he dragged himself\x01",
            "to the store without a\x01",
            "care in the world...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "He bought a lot. I\x01",
            "wonder if he's drinkin'\x01",
            "in bed around now...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Honestly... I didn't\x01",
            "want to see Wald like\x01",
            "that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I don't believe it... To\x01",
            "think that guy'd lose\x01",
            "himself in alcohol...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...Yeah, I feel the\x01",
            "same.\x02",
        )
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
            "Let's keep that in mind,\x01",
            "everybody.\x02",
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
        "#00005FWald did that?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00301FDrinkin' away one's\x01",
            "worries, they call it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FBecause of the amount,\x01",
            "I'm concerned for his\x01",
            "health...\x02",
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

    # Function_15_2BA9 end

    def Function_16_2F31(): pass

    label("Function_16_2F31")

    OP_4B(0xD, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_4B(0xC, 0xFF)

    ChrTalk(
        0x9,
        (
            "Listen up! If anything\x01",
            "happens, you call Luganov\x01",
            "or I immediately. Got it?\x02",
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

    # Function_16_2F31 end

    def Function_17_2FB0(): pass

    label("Function_17_2FB0")

    OP_4B(0xD, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_4B(0xC, 0xFF)
    TurnDirection(0xD, 0x0, 0)
    TurnDirection(0xC, 0x0, 0)
    TurnDirection(0x9, 0x0, 0)

    ChrTalk(
        0xD,
        "Y-You guys!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "The Special Support\x01",
            "Section... And Wazy!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...Looks like you guys\x01",
            "aren't going to be able\x01",
            "to see Wald.\x02",
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
        (
            "If you understand, get\x01",
            "out of here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10303F...Oh man.\x02",
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

    # Function_17_2FB0 end

    def Function_18_3157(): pass

    label("Function_18_3157")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3168")
    Jump("loc_3515")

    label("loc_3168")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_31B5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3183")
    Call(0, 11)
    Jump("loc_31B0")

    label("loc_3183")


    ChrTalk(
        0xFE,
        (
            "(Jed looks hesitant for\x01",
            "some reason...)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31B0")

    Jump("loc_3515")

    label("loc_31B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_31C3")
    Jump("loc_3515")

    label("loc_31C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_31D1")
    Jump("loc_3515")

    label("loc_31D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_325D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31EC")
    Call(0, 12)
    Jump("loc_3258")

    label("loc_31EC")


    ChrTalk(
        0xFE,
        (
            "An unidentified armed group, huh...\x01",
            "If we were to attack them, we'd get\x01",
            "our asses handed to us, I bet.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3258")

    Jump("loc_3515")

    label("loc_325D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3292")

    ChrTalk(
        0xFE,
        (
            "Luganov... He was\x01",
            "seriously cool.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3515")

    label("loc_3292")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_32FB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16E, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32AD")
    Call(0, 5)
    Jump("loc_32F6")

    label("loc_32AD")


    ChrTalk(
        0xFE,
        (
            "100,000 mira... Just how\x01",
            "did he get his hands on\x01",
            "that kind of mira?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32F6")

    Jump("loc_3515")

    label("loc_32FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3394")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3316")
    Call(0, 6)
    Jump("loc_338F")

    label("loc_3316")


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
            "I don't want to think\x01",
            "he's left the city,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_338F")

    Jump("loc_3515")

    label("loc_3394")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_33A5")
    Call(0, 7)
    Jump("loc_3515")

    label("loc_33A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_33B6")
    Call(0, 8)
    Jump("loc_3515")

    label("loc_33B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_34A9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_346A")

    ChrTalk(
        0xFE,
        (
            "*sigh*... That weird guy\x01",
            "back there dampened our\x01",
            "spirits, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...It won't happen\x01",
            "again. We'll remember\x01",
            "this, Wazy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10303F............\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_34A4")

    label("loc_346A")


    ChrTalk(
        0xFE,
        (
            "...It won't happen\x01",
            "again. We'll remember\x01",
            "this, Wazy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34A4")

    Jump("loc_3515")

    label("loc_34A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_34FB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34C4")
    Call(0, 19)
    Jump("loc_34F6")

    label("loc_34C4")


    ChrTalk(
        0xFE,
        (
            "Y-You guys... Think a\x01",
            "little more seriously!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34F6")

    Jump("loc_3515")

    label("loc_34FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_350C")
    Call(0, 20)
    Jump("loc_3515")

    label("loc_350C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3515")

    label("loc_3515")

    TalkEnd(0xFE)
    Return()

    # Function_18_3157 end

    def Function_19_3519(): pass

    label("Function_19_3519")

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
            "Yeah! This morning, I\x01",
            "spotted a sister carrying\x01",
            "a mountain of bread here.\x02",
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
            "...Yeah? And just how is\x01",
            "Wald involved in that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "And so, I was thinking\x01",
            "we'd go to the church to\x01",
            "pick up this sister...\x02",
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

    # Function_19_3519 end

    def Function_20_369D(): pass

    label("Function_20_369D")

    OP_4B(0xB, 0xFF)
    OP_4B(0xA, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3860")

    ChrTalk(
        0xB,
        (
            "*sigh*, Wald was really\x01",
            "scary this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "And... Just why is Wald\x01",
            "so obsessed over that\x01",
            "Wazy guy anyway?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Anyway, the most dangerous\x01",
            "guy isn't here. That's cause\x01",
            "for celebration, I guess...\x02",
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
            "We're a million years\x01",
            "too early to be\x01",
            "questioning Wald.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "More importantly, we've\x01",
            "gotta think of how to get\x01",
            "him out of this mood!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Y-Yeah. But I have no\x01",
            "idea...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_38D0")

    label("loc_3860")


    ChrTalk(
        0xA,
        (
            "Guys! What if Wald heard\x01",
            "us? He'd beat us half to\x01",
            "death, right?\x02",
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

    label("loc_38D0")

    OP_4C(0xB, 0xFF)
    OP_4C(0xA, 0xFF)
    Return()

    # Function_20_369D end

    def Function_21_38D9(): pass

    label("Function_21_38D9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_38EA")
    Jump("loc_3C3C")

    label("loc_38EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_3924")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3905")
    Call(0, 11)
    Jump("loc_391F")

    label("loc_3905")


    ChrTalk(
        0xFE,
        "Hyaha, he got mad...\x02",
    )

    CloseMessageWindow()

    label("loc_391F")

    Jump("loc_3C3C")

    label("loc_3924")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3932")
    Jump("loc_3C3C")

    label("loc_3932")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3940")
    Jump("loc_3C3C")

    label("loc_3940")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_39BE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_395B")
    Call(0, 12)
    Jump("loc_39B9")

    label("loc_395B")


    ChrTalk(
        0xFE,
        (
            "Umm... Where'd I put our\x01",
            "hammer and nails?\x02",
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

    label("loc_39B9")

    Jump("loc_3C3C")

    label("loc_39BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_39F0")

    ChrTalk(
        0xFE,
        (
            "Man, our seniors are the\x01",
            "best!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C3C")

    label("loc_39F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3A4E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16E, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A0B")
    Call(0, 5)
    Jump("loc_3A49")

    label("loc_3A0B")


    ChrTalk(
        0xFE,
        (
            "But there's a lot I\x01",
            "don't get. Someone\x01",
            "explain it to me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A49")

    Jump("loc_3C3C")

    label("loc_3A4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3ACC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A69")
    Call(0, 6)
    Jump("loc_3AC7")

    label("loc_3A69")


    ChrTalk(
        0xFE,
        (
            "As usual, it looks like he\x01",
            "didn't even come back to rest...\x01",
            "I wonder where he's staying.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3AC7")

    Jump("loc_3C3C")

    label("loc_3ACC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3ADD")
    Call(0, 7)
    Jump("loc_3C3C")

    label("loc_3ADD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3AEE")
    Call(0, 8)
    Jump("loc_3C3C")

    label("loc_3AEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3BD8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B82")

    ChrTalk(
        0xFE,
        (
            "Hyaha. There's weird\x01",
            "people all over this\x01",
            "world, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Huh? Come to think of\x01",
            "it, Huey and I aren't\x01",
            "fighting.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3BD3")

    label("loc_3B82")


    ChrTalk(
        0xFE,
        (
            "...Well, I won't sweat\x01",
            "the small stuff.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've got to think of\x01",
            "Wald now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3BD3")

    Jump("loc_3C3C")

    label("loc_3BD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3C22")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BF3")
    Call(0, 19)
    Jump("loc_3C1D")

    label("loc_3BF3")


    ChrTalk(
        0xFE,
        (
            "And... Give me good\x01",
            "ideas too, guys!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C1D")

    Jump("loc_3C3C")

    label("loc_3C22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3C33")
    Call(0, 20)
    Jump("loc_3C3C")

    label("loc_3C33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3C3C")

    label("loc_3C3C")

    TalkEnd(0xFE)
    Return()

    # Function_21_38D9 end

    def Function_22_3C40(): pass

    label("Function_22_3C40")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3CDD")

    ChrTalk(
        0xFE,
        (
            "Until Wald gets back,\x01",
            "leaders Jed and Luganov are\x01",
            "holding the Vipers together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We've got to work\x01",
            "together and protect the\x01",
            "Vipers.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3EFD")

    label("loc_3CDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_3CEB")
    Jump("loc_3EFD")

    label("loc_3CEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3CF9")
    Jump("loc_3EFD")

    label("loc_3CF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3D07")
    Jump("loc_3EFD")

    label("loc_3D07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3D54")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D22")
    Call(0, 23)
    Jump("loc_3D4F")

    label("loc_3D22")


    ChrTalk(
        0xFE,
        (
            "I wonder what Wald's\x01",
            "doing right now...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D4F")

    Jump("loc_3EFD")

    label("loc_3D54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3DFC")

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
            "They're probably even\x01",
            "more worried about Wald\x01",
            "than we are...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3EFD")

    label("loc_3DFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3E50")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16E, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E17")
    Call(0, 5)
    Jump("loc_3E4B")

    label("loc_3E17")


    ChrTalk(
        0xFE,
        (
            "Wald... Who could you be\x01",
            "with instead of us...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E4B")

    Jump("loc_3EFD")

    label("loc_3E50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3E5E")
    Jump("loc_3EFD")

    label("loc_3E5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3E6F")
    Call(0, 13)
    Jump("loc_3EFD")

    label("loc_3E6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3E80")
    Call(0, 14)
    Jump("loc_3EFD")

    label("loc_3E80")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3E91")
    Call(0, 16)
    Jump("loc_3EFD")

    label("loc_3E91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3EC7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14D, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3EAC")
    Call(0, 9)
    Jump("loc_3EC2")

    label("loc_3EAC")


    ChrTalk(
        0xFE,
        "S-Scram already!\x02",
    )

    CloseMessageWindow()

    label("loc_3EC2")

    Jump("loc_3EFD")

    label("loc_3EC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3EF4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x137, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3EE2")
    Call(0, 17)
    Jump("loc_3EEF")

    label("loc_3EE2")


    ChrTalk(
        0xFE,
        "Wald...\x02",
    )

    CloseMessageWindow()

    label("loc_3EEF")

    Jump("loc_3EFD")

    label("loc_3EF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3EFD")

    label("loc_3EFD")

    TalkEnd(0xFE)
    Return()

    # Function_22_3C40 end

    def Function_23_3F01(): pass

    label("Function_23_3F01")

    OP_4B(0xD, 0xFF)
    OP_4B(0xC, 0xFF)

    ChrTalk(
        0xD,
        (
            "Wald... As expected, I\x01",
            "haven't seen him today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "That's right... There's\x01",
            "some kind of huge\x01",
            "ruckus.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "...Anyway, I hope he's\x01",
            "safe.\x02",
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

    # Function_23_3F01 end

    def Function_24_3FAF(): pass

    label("Function_24_3FAF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3FC0")
    Jump("loc_44CC")

    label("loc_3FC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_3FCE")
    Jump("loc_44CC")

    label("loc_3FCE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3FDC")
    Jump("loc_44CC")

    label("loc_3FDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_42E2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18D, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4297")
    OP_4B(0xFE, 0xFF)

    ChrTalk(
        0xFE,
        "Wald... Everyone...\x02",
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
        (
            "...Oh, the Special\x01",
            "Support Section, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FYour other members are...\x01",
            "still hospitalized,\x01",
            "aren't they?\x02",
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
            "Kｷki had it especially bad...\x01",
            "He's in a different room than\x01",
            "everyone else... *cry*...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008FI'm sorry... That was a\x01",
            "little insensitive.\x02",
        )
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
            "The others have to\x01",
            "endure this pain! Why\x01",
            "was only I spared!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*cry*... Dammit! Why...\x01",
            "Why did it have to be\x01",
            "like this...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00208F(Lloyd. We should leave\x01",
            "him alone right now.)\x02",
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
        "#10308F(......)\x02",
    )

    CloseMessageWindow()
    OP_93(0xFE, 0x87, 0x0)
    OP_4C(0xFE, 0xFF)
    SetScenarioFlags(0x18D, 3)
    Jump("loc_42DD")

    label("loc_4297")


    ChrTalk(
        0xFE,
        "Wald... Everyone...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Why... Why'd it have to\x01",
            "be like this...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_42DD")

    Jump("loc_44CC")

    label("loc_42E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_4358")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_42FD")
    Call(0, 23)
    Jump("loc_4353")

    label("loc_42FD")


    ChrTalk(
        0xFE,
        "Gnosis, huh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Revache's not around\x01",
            "anymore though, so just\x01",
            "where did he...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4353")

    Jump("loc_44CC")

    label("loc_4358")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_43D5")

    ChrTalk(
        0xFE,
        (
            "Hehe, our seniors are so\x01",
            "great.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's only in times like\x01",
            "these, but... I'm kinda\x01",
            "glad they're around.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_44CC")

    label("loc_43D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_443E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16E, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_43F0")
    Call(0, 5)
    Jump("loc_4439")

    label("loc_43F0")


    ChrTalk(
        0xFE,
        (
            "Ooh... Wald. I can't\x01",
            "believe you're doing\x01",
            "something so dangerous...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4439")

    Jump("loc_44CC")

    label("loc_443E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_444F")
    Call(0, 13)
    Jump("loc_44CC")

    label("loc_444F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4460")
    Call(0, 14)
    Jump("loc_44CC")

    label("loc_4460")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4471")
    Call(0, 16)
    Jump("loc_44CC")

    label("loc_4471")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_44CC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x137, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_448C")
    Call(0, 17)
    Jump("loc_44CC")

    label("loc_448C")


    ChrTalk(
        0xFE,
        (
            "B-But like Jed says,\x01",
            "that kind of talk is\x01",
            "empty, isn't it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_44CC")

    TalkEnd(0xFE)
    Return()

    # Function_24_3FAF end

    def Function_25_44D0(): pass

    label("Function_25_44D0")

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

    def lambda_4596():
        OP_96(0xFE, 0x1C20, 0x0, 0xFFFFFD44, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4596)
    Sleep(400)

    def lambda_45B3():
        OP_96(0xFE, 0x1CE8, 0x0, 0x2BC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_45B3)
    Sleep(400)

    def lambda_45D0():
        OP_96(0xFE, 0x170C, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_45D0)
    Sleep(400)

    def lambda_45ED():
        OP_96(0xFE, 0x1900, 0x0, 0x4B0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_45ED)
    Sleep(400)

    def lambda_460A():
        OP_96(0xFE, 0x12C0, 0x0, 0xFFFFFD44, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_460A)
    Sleep(400)

    def lambda_4627():
        OP_96(0xFE, 0x13EC, 0x0, 0x2BC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4627)
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

    def lambda_46AD():

        label("loc_46AD")

        TurnDirection(0xFE, 0x0, 500)
        Yield()
        Jump("loc_46AD")

    QueueWorkItem2(0x9, 2, lambda_46AD)

    def lambda_46BF():

        label("loc_46BF")

        TurnDirection(0xFE, 0x0, 500)
        Yield()
        Jump("loc_46BF")

    QueueWorkItem2(0xC, 2, lambda_46BF)

    def lambda_46D1():

        label("loc_46D1")

        TurnDirection(0xFE, 0x0, 500)
        Yield()
        Jump("loc_46D1")

    QueueWorkItem2(0xD, 2, lambda_46D1)

    ChrTalk(
        0x9,
        (
            "#11PThe fuzz... So you're\x01",
            "here again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PCould you be looking for\x01",
            "new info?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_473A():

        label("loc_473A")

        TurnDirection(0xFE, 0x0, 500)
        Yield()
        Jump("loc_473A")

    QueueWorkItem2(0x8, 2, lambda_473A)

    def lambda_474C():

        label("loc_474C")

        TurnDirection(0xFE, 0x0, 500)
        Yield()
        Jump("loc_474C")

    QueueWorkItem2(0xB, 2, lambda_474C)

    def lambda_475E():

        label("loc_475E")

        TurnDirection(0xFE, 0x0, 500)
        Yield()
        Jump("loc_475E")

    QueueWorkItem2(0xA, 2, lambda_475E)
    OP_63(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_478B():

        label("loc_478B")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_478B")

    QueueWorkItem2(0xD, 2, lambda_478B)

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

    def lambda_485E():

        label("loc_485E")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_485E")

    QueueWorkItem2(0x8, 2, lambda_485E)

    def lambda_4870():

        label("loc_4870")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_4870")

    QueueWorkItem2(0xB, 2, lambda_4870)

    def lambda_4882():

        label("loc_4882")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_4882")

    QueueWorkItem2(0xA, 2, lambda_4882)

    def lambda_4894():

        label("loc_4894")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_4894")

    QueueWorkItem2(0x9, 2, lambda_4894)

    def lambda_48A6():

        label("loc_48A6")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_48A6")

    QueueWorkItem2(0xC, 2, lambda_48A6)

    ChrTalk(
        0xA,
        "#5PY-You!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5PHow shameless... It's\x01",
            "because of you that\x01",
            "Wald...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00001F(Damn... They're sure in\x01",
            "a bad mood.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00208F(It might have been a\x01",
            "bad idea to come...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5P......\x02",
    )

    CloseMessageWindow()
    EndChrThread(0x8, 0x2)
    SetChrFlags(0x8, 0x40)

    def lambda_498A():
        OP_96(0xFE, 0x215C, 0x0, 0x2BC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_498A)
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

    def lambda_4A83():

        label("loc_4A83")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_4A83")

    QueueWorkItem2(0x101, 2, lambda_4A83)

    def lambda_4A95():

        label("loc_4A95")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_4A95")

    QueueWorkItem2(0x102, 2, lambda_4A95)

    def lambda_4AA7():

        label("loc_4AA7")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_4AA7")

    QueueWorkItem2(0x103, 2, lambda_4AA7)

    def lambda_4AB9():

        label("loc_4AB9")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_4AB9")

    QueueWorkItem2(0x109, 2, lambda_4AB9)

    def lambda_4ACB():

        label("loc_4ACB")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_4ACB")

    QueueWorkItem2(0x104, 2, lambda_4ACB)

    def lambda_4ADD():

        label("loc_4ADD")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_4ADD")

    QueueWorkItem2(0x105, 2, lambda_4ADD)

    def lambda_4AEF():
        OP_95(0xFE, 8039, 0, 570, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_4AEF)
    Sleep(50)
    WaitChrThread(0x8, 1)
    EndChrThread(0x105, 0x2)
    SetChrFlags(0x105, 0x20)
    SetChrFlags(0x105, 0x4)
    Sound(802, 0, 100, 0)

    def lambda_4B24():
        OP_A6(0xFE, 0x0, 0x64, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_4B24)

    def lambda_4B3D():
        OP_96(0xFE, 0x1CE8, 0xC8, 0x2BC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_4B3D)
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
        "#6P#10310F......\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00011FH-Hey...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10111FWazy!\x02",
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    ChrTalk(
        0x8,
        (
            "#4S#11PHey, Wazy! You know,\x01",
            "don't you!?\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    ChrTalk(
        0x8,
        (
            "#4S#11POf all things, Wald took\x01",
            "that drug!?\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    ChrTalk(
        0x8,
        (
            "#4S#11PThis is your fault\x01",
            "too... Everything is all\x01",
            "your fault!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00101F(L-Lloyd... How much did\x01",
            "you tell them...?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003F(Well, I definitely\x01",
            "didn't tell them about\x01",
            "demonization, but...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#N#10108F(...But, we told them there's\x01",
            "a possibility Wald may have\x01",
            "been dosed with Gnosis.)\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x8,
        (
            "#11P...Two years ago... If you\x01",
            "hadn't come then, we would have\x01",
            "had our fun this whole time!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PBut then you came along... And\x01",
            "now you're with the police for\x01",
            "some strange reason.\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    ChrTalk(
        0x8,
        (
            "#11P#4S...Don't act like you\x01",
            "understand!!#3S\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4F9E():
        OP_A6(0xFE, 0x32, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_4F9E)
    WaitChrThread(0x105, 2)

    ChrTalk(
        0x105,
        (
            "#6P#10303F...It wasn't for no reason. I\x01",
            "chose this path because there's\x01",
            "something I need to do.\x02\x03",
            "#10308FWald becoming like that as a\x01",
            "result... was an unforeseen\x01",
            "consequence.\x02",
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
        (
            "#11P#4SBring it on! I'll\x01",
            "destroy you!#3S\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#00210F!!\x02",
    )

    CloseMessageWindow()

    def lambda_50FB():
        OP_A6(0xFE, 0x32, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_50FB)
    WaitChrThread(0x105, 2)
    Sleep(500)
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xFFFF)
    Sound(811, 0, 100, 0)

    def lambda_5139():
        OP_9D(0xFE, 0x1A2C, 0x0, 0x2BC, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5139)
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

    def lambda_517F():

        label("loc_517F")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_517F")

    QueueWorkItem2(0x101, 2, lambda_517F)

    def lambda_5191():

        label("loc_5191")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_5191")

    QueueWorkItem2(0x102, 2, lambda_5191)

    def lambda_51A3():

        label("loc_51A3")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_51A3")

    QueueWorkItem2(0x103, 2, lambda_51A3)

    def lambda_51B5():

        label("loc_51B5")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_51B5")

    QueueWorkItem2(0x109, 2, lambda_51B5)

    def lambda_51C7():

        label("loc_51C7")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_51C7")

    QueueWorkItem2(0x104, 2, lambda_51C7)

    ChrTalk(
        0xC,
        "#11PHuh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10305F...What are you\x01",
            "planning?\x02",
        )
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
            "#11P...Listen up, I've got a\x01",
            "favor to ask. Instead of\x01",
            "punching you...\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    ChrTalk(
        0x8,
        (
            "#4S#11PTake responsibility, and\x01",
            "wake up Wald for us!\x02",
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
        "#11PLuganov...\x02",
    )

    CloseMessageWindow()
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x105)

    ChrTalk(
        0x105,
        (
            "#6P#10308F...Haha, so that's how\x01",
            "it is.\x02\x03",
            "#10303F............\x02",
        )
    )

    CloseMessageWindow()

    def lambda_539A():

        label("loc_539A")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_539A")

    QueueWorkItem2(0x101, 2, lambda_539A)

    def lambda_53AC():

        label("loc_53AC")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_53AC")

    QueueWorkItem2(0x102, 2, lambda_53AC)

    def lambda_53BE():

        label("loc_53BE")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_53BE")

    QueueWorkItem2(0x103, 2, lambda_53BE)

    def lambda_53D0():

        label("loc_53D0")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_53D0")

    QueueWorkItem2(0x109, 2, lambda_53D0)

    def lambda_53E2():

        label("loc_53E2")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_53E2")

    QueueWorkItem2(0x104, 2, lambda_53E2)

    ChrTalk(
        0x101,
        "#12P#00005FWazy...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10303F...I can't promise you\x01",
            "anything, but... I'll do\x01",
            "everything in my power to.\x02\x03",
            "#10301FAs the leader of the\x01",
            "Testaments... I will bring\x01",
            "him back where he belongs.\x02",
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

    # Function_25_44D0 end

    def Function_26_55C4(): pass

    label("Function_26_55C4")


    def lambda_55C9():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFE0C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_55C9)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_26_55C4 end

    SaveToFile()

Try(main)
