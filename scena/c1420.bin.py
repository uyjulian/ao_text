from ScenarioHelper import *

def main():
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
        "Luganoff",               # 1
        "Jed",                 # 2
        "Huey",               # 3
        "Slash",             # 4
        "Koki",                 # 5
        "Dino",               # 6
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
        "Function_5_1074",         # 05, 5
        "Function_6_164E",         # 06, 6
        "Function_7_17F1",         # 07, 7
        "Function_8_196F",         # 08, 8
        "Function_9_1C0A",         # 09, 9
        "Function_10_2170",        # 0A, 10
        "Function_11_2712",        # 0B, 11
        "Function_12_28C0",        # 0C, 12
        "Function_13_2A34",        # 0D, 13
        "Function_14_2D22",        # 0E, 14
        "Function_15_2E6A",        # 0F, 15
        "Function_16_31FE",        # 10, 16
        "Function_17_326C",        # 11, 17
        "Function_18_3412",        # 12, 18
        "Function_19_37BF",        # 13, 19
        "Function_20_397E",        # 14, 20
        "Function_21_3BDD",        # 15, 21
        "Function_22_3F64",        # 16, 22
        "Function_23_4245",        # 17, 23
        "Function_24_4301",        # 18, 24
        "Function_25_4823",        # 19, 25
        "Function_26_5968",        # 1A, 26
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_B5F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AD2")

    ChrTalk(
        0xFE,
        "Ye, yeah ~ ~ ~! It is!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I do not know whether you are worried ~! It is!\x01",
            "Wake Wakanakanen something\x01",
            "I'm in trouble Hima ~! It is!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ya sing even in the song, blow it away,\x01",
            "I ~ ~ ~ ~ ~ Yahobo ~ ~! It is!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_B5A")

    label("loc_AD2")


    ChrTalk(
        0xFE,
        (
            "Even such a deck tree can not bear farts!\x01",
            "I do not know whether you are worried ~! It is!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ya sing even in the song, blow it away,\x01",
            "I ~ ~ ~ ~ ~ Yahobo ~ ~! It is!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B5A")

    Jump("loc_1070")

    label("loc_B5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_B6D")
    Jump("loc_1070")

    label("loc_B6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_B7B")
    Jump("loc_1070")

    label("loc_B7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_B89")
    Jump("loc_1070")

    label("loc_B89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_C28")

    ChrTalk(
        0xFE,
        (
            "Wow …\x01",
            "Awfully something frustrating!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's a raid incident in Mainz! Is it?\x01",
            "From that,\x01",
            "Where is Mr. Wald? It is!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1070")

    label("loc_C28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_C6D")

    ChrTalk(
        0xFE,
        (
            "Hank it,\x01",
            "Because I am lending it, please.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1070")

    label("loc_C6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_CF7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16E, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C88")
    Call(0, 5)
    Jump("loc_CF2")

    label("loc_C88")


    ChrTalk(
        0xFE,
        (
            "Mr. Waldo ……\x01",
            "Did you do a big hit at the casino too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But why not?\x01",
            "Do not tell me!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CF2")

    Jump("loc_1070")

    label("loc_CF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_D58")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D12")
    Call(0, 6)
    Jump("loc_D53")

    label("loc_D12")


    ChrTalk(
        0xFE,
        (
            "Huh ~, even if it is Valdo\x01",
            "Rice and Majiriman Hey … ….\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D53")

    Jump("loc_1070")

    label("loc_D58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_D69")
    Call(0, 7)
    Jump("loc_1070")

    label("loc_D69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_D7A")
    Call(0, 8)
    Jump("loc_1070")

    label("loc_D7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_ECB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E4C")

    ChrTalk(
        0xFE,
        (
            "Waldo ~ ~ mu!\x01",
            "Seriously please give me a face!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you drink sake, we will buy it\x01",
            "Let's have a drink here!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you do not like it,\x01",
            "Nothing is starting ___ REAL ___ ___ ___ 0 It is!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_EC6")

    label("loc_E4C")


    ChrTalk(
        0xFE,
        (
            "If you drink sake, we will buy it\x01",
            "Let's have a drink here!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you do not like it,\x01",
            "Nothing is starting ___ REAL ___ ___ ___ 0 It is!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EC6")

    Jump("loc_1070")

    label("loc_ECB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_F4B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14D, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EE6")
    Call(0, 9)
    Jump("loc_F46")

    label("loc_EE6")


    ChrTalk(
        0xFE,
        (
            "Do not believe me …\x01",
            "I do not believe you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Such a story that is funny\x01",
            "There is a taste … ___ ___ 0\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F46")

    Jump("loc_1070")

    label("loc_F4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1067")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FF3")

    ChrTalk(
        0xFE,
        "Ye ~, itaaa ~ ~ ugh!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yaro Domeo of Tests!\x01",
            "I am skiing right now too!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#4S…… イ ィ ~ ~ Yahoo!! It is!#3S\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1062")

    label("loc_FF3")


    ChrTalk(
        0xFE,
        (
            "Yaro Domeo of Tests!\x01",
            "I am skiing right now too!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#4S…… イ ィ ~ ~ Yahoo!! It is!#3S\x02",
    )

    CloseMessageWindow()

    label("loc_1062")

    Jump("loc_1070")

    label("loc_1067")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1070")

    label("loc_1070")

    TalkEnd(0xFE)
    Return()

    # Function_4_A07 end

    def Function_5_1074(): pass

    label("Function_5_1074")

    OP_4B(0xD, 0xFF)
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_4B(0xA, 0xFF)
    OP_4B(0xC, 0xFF)

    ChrTalk(
        0x9,
        (
            "And you, Omae et al.\x01",
            "What was the result of the survey?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "O, os …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "It will be a week ago,\x01",
            "Kanon is Mr. Wald\x01",
            "He seems to have seen … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "So, at that time apparently\x01",
            "A small communication terminal of Enigma\x01",
            "It looks like I was using it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "To say the master of the exchange shop\x01",
            "100 thousand mirrors do expensive\x01",
            "He seems to be a silent monster but ….\x02",
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
        "Ju, 100 thousand Mira ~! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Wow, you serious ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Va, Wald,\x01",
            "Where the Mira is ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Certainly it is also worrisome … …\x01",
            "Koki、オマエ通信端末っつったな？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "That means … …\x01",
            "With someone Waldo\x01",
            "Have you contacted me?\x02",
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
            "High, that guy is too cool\x01",
            "I could not catch the content\x01",
            "So it's ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Well, but Mr. Waldo,\x01",
            "Something funny laughing … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "… … Wow, were you laughing?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "I have something good … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Well, no way\x01",
            "Mr. Wald abandoned … …\x01",
            "There is no such thing as it is, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "てめえ、Slash。\x01",
            "You do not mind playing funny.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "If you want to be killed, it will be different but yo?\x02",
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xB)
    TurnDirection(0xB, 0x8, 0)

    ChrTalk(
        0xB,
        "Well, sorry …!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001F(Wald says Enigma, … ….\x01",
            "Certainly I am a little worried. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F(Yes, even if you say Enigma\x01",
            "Generally so many\x01",
            "It is not even a circle that is circulating … …)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10303F(… … Wald ………………)\x02",
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

    # Function_5_1074 end

    def Function_6_164E(): pass

    label("Function_6_164E")

    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_4B(0xA, 0xFF)

    ChrTalk(
        0x8,
        (
            "おう、Jed。\x01",
            "KokiとDinoのヤロウは\x01",
            "Have not you come yet?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Well, wait.\x01",
            "It is said that additional investigation is necessary.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "By the way, those of you\x01",
            "I heard that it was not at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Well …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Well, sorry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "One way street\x01",
            "I went around, but recently\x01",
            "I do not see anything stunningly of things ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "……Really.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Mr. Waldo ……\x01",
            "I wonder where he went by seriously.\x02",
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

    # Function_6_164E end

    def Function_7_17F1(): pass

    label("Function_7_17F1")

    OP_4B(0x8, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_4B(0xA, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18B8")

    ChrTalk(
        0x8,
        (
            "Oh, we are\x01",
            "Anyway, Ms. Wald\x01",
            "I'm looking for a place to go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Range is town Zembu.\x01",
            "Examine it from one end and turn around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Os!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Sure thing!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1962")

    label("loc_18B8")


    ChrTalk(
        0x8,
        (
            "Oh, if you see Waldo\x01",
            "Report back here with Sokko.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Even if Tamele et al.\x01",
            "In addition, it is okiridanaka who is shikato.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Os!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Sure thing!\x02",
    )

    CloseMessageWindow()

    label("loc_1962")

    OP_4C(0x8, 0xFF)
    OP_4C(0xB, 0xFF)
    OP_4C(0xA, 0xFF)
    Return()

    # Function_7_17F1 end

    def Function_8_196F(): pass

    label("Function_8_196F")

    OP_4B(0x8, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_4B(0xA, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B95")

    ChrTalk(
        0x8,
        "Well, what did you get?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Ha, hi.\x01",
            "That was obediently apologizing … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "When I get to such an attitude\x01",
            "I can not beat more than that … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, I can not do anything!\x01",
            "Buddhist guys are also guys,\x01",
            "Temarers are also not satisfied!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, I guess that's a provocation at that time.\x01",
            "From now on I will threaten threats\x01",
            "I will tell you, I remember yo.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "\"Omae no Ka chan, Dave so! \"\x01",
            "… … Sorry, let's say it!\x02",
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
        "Let me see……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Oh, Osu!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1BFD")

    label("loc_1B95")


    ChrTalk(
        0xA,
        "Oh, you mae chan … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "De, daibesoh … っ と.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Oraola, voice will be reduced!\x02",
    )

    CloseMessageWindow()

    label("loc_1BFD")

    OP_4C(0x8, 0xFF)
    OP_4C(0xB, 0xFF)
    OP_4C(0xA, 0xFF)
    Return()

    # Function_8_196F end

    def Function_9_1C0A(): pass

    label("Function_9_1C0A")

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
            "Koki……\x01",
            "I wonder if the story is true.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Yes, guys\x01",
            "Something I'm talking about, but …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Ore Trust the truth,\x01",
            "Do you believe and accumulate?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "That Waldo\x01",
            "I can not do it unilaterally ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105F(is this……\x01",
            "On the rainy day confrontation\x01",
            "I wonder what he is saying? )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F(Oh … it will be.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10303F(………………)\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x9, 0x105, 500)

    ChrTalk(
        0x9,
        (
            "Take care …\x01",
            "Which crane has come down here! Is it?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_1EAC():
        TurnDirection(0x8, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1EAC)
    TurnDirection(0xC, 0x105, 500)

    ChrTalk(
        0xC,
        "Wow, Wadi …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Hiaka, are we supposed to be next time?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Why, get out of front of you!\x01",
            "Let's get back to you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FHey, hey …!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 500)

    ChrTalk(
        0x9,
        "――止めろ、Luganoff！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Even if the story of the gigs is true,\x01",
            "Wandering out here, Ms. Wald's\x01",
            "I will destroy my face …!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Besides, even if you do such a thing\x01",
            "Waldo is not pleased!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "A little, fucking … …!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x105, 500)

    ChrTalk(
        0xC,
        (
            "…… What do you mean?\x01",
            "I do not know if I came here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "If you do not feel like fighting,\x01",
            "Will you go out quickly?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "However, for quarreling\x01",
            "If you came, the story is different, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303FNo, I do not plan to do that.\x02\x03",
            "#10300FYou interfered.\x01",
            "… … Let's go, everyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FOh, ah ……\x02",
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

    # Function_9_1C0A end

    def Function_10_2170(): pass

    label("Function_10_2170")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_22F0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2264")

    ChrTalk(
        0xFE,
        (
            "I still have Mr. Wald\x01",
            "I did not forgive you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… That's not it ……\x01",
            "Saber Viper\x01",
            "It was certainly a fun place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "So as a Viper executive … …\x01",
            "It is a strike to protect it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_22EB")

    label("loc_2264")


    ChrTalk(
        0xFE,
        (
            "I still have Mr. Wald\x01",
            "I did not forgive him … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As a Viper executive,\x01",
            "I will protect this important place\x01",
            "It's streaky.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22EB")

    Jump("loc_270E")

    label("loc_22F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_238B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_230B")
    Call(0, 11)
    Jump("loc_2386")

    label("loc_230B")


    ChrTalk(
        0xFE,
        (
            "… … Damn it.\x01",
            "Better than Blue\x01",
            "I will cooperate …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Luganoff、Koki、Dino……\x01",
            "I will think to Aitana … …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2386")

    Jump("loc_270E")

    label("loc_238B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2399")
    Jump("loc_270E")

    label("loc_2399")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_23A7")
    Jump("loc_270E")

    label("loc_23A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_244C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23C2")
    Call(0, 12)
    Jump("loc_2447")

    label("loc_23C2")


    ChrTalk(
        0xFE,
        (
            "Hmm? Is it the support section …?\x01",
            "Apparently there will be no progress between each other.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Wonder if this time\x01",
            "If you see Waldo\x01",
            "Please speak to us soon.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2447")

    Jump("loc_270E")

    label("loc_244C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2542")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24FE")

    ChrTalk(
        0xFE,
        (
            "…… What we want to say is,\x01",
            "Luganoffが大体言ってくれた。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Do not tell anything else.\x01",
            "…… I can lose the place today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10303F…………………………\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_253D")

    label("loc_24FE")


    ChrTalk(
        0xFE,
        (
            "We do not have to tell you anymore.\x01",
            "…… I can lose the place today.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_253D")

    Jump("loc_270E")

    label("loc_2542")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2595")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16E, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_255D")
    Call(0, 5)
    Jump("loc_2590")

    label("loc_255D")


    ChrTalk(
        0xFE,
        (
            "Mr. Waldo ……\x01",
            "What on earth were you?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2590")

    Jump("loc_270E")

    label("loc_2595")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_25EA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25B0")
    Call(0, 6)
    Jump("loc_25E5")

    label("loc_25B0")


    ChrTalk(
        0xFE,
        (
            "Mr. Waldo ……\x01",
            "I wonder where he went by seriously.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25E5")

    Jump("loc_270E")

    label("loc_25EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_25FB")
    Call(0, 13)
    Jump("loc_270E")

    label("loc_25FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_260C")
    Call(0, 14)
    Jump("loc_270E")

    label("loc_260C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_261D")
    Call(0, 16)
    Jump("loc_270E")

    label("loc_261D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_26AB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14D, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2638")
    Call(0, 9)
    Jump("loc_26A6")

    label("loc_2638")


    ChrTalk(
        0xFE,
        (
            "If you do not want to fight,\x01",
            "Go ahead and go away ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When more than this,\x01",
            "To be honest I do not know what it will be.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26A6")

    Jump("loc_270E")

    label("loc_26AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2705")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x137, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26C6")
    Call(0, 17)
    Jump("loc_2700")

    label("loc_26C6")


    ChrTalk(
        0xFE,
        (
            "Is it okay?\x01",
            "If you can stay safe like this\x01",
            "Do not think.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2700")

    Jump("loc_270E")

    label("loc_2705")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_270E")

    label("loc_270E")

    TalkEnd(0xFE)
    Return()

    # Function_10_2170 end

    def Function_11_2712(): pass

    label("Function_11_2712")

    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)

    ChrTalk(
        0x9,
        (
            "Those people …\x01",
            "Better than the blue sho\x01",
            "I have to cooperate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "……Jedさん。\x01",
            "As a matter of course we also cooperate\x01",
            "Is it not good?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "ヒャハ、何言ってんだHuey！\x01",
            "With Viper, Betrayal Mon\x01",
            "Do it neatly … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "…… Viper has broken up\x01",
            "I am telling you, you idiot!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xB)

    ChrTalk(
        0xB,
        "Su, Senmensen.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "…… Anyway, I am thinking now.\x01",
            "You do not do selfish things.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    ClearChrFlags(0xA, 0x10)
    ClearChrFlags(0xB, 0x10)
    SetScenarioFlags(0x0, 1)
    Return()

    # Function_11_2712 end

    def Function_12_28C0(): pass

    label("Function_12_28C0")

    OP_4B(0x9, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_4B(0xA, 0xFF)

    ChrTalk(
        0x9,
        (
            "Well, well I do not understand\x01",
            "It is becoming noisy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Yes, people in the city also occupied Mainz\x01",
            "From a touch of touching a topic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "まさか、Mr. Waldo ……\x01",
            "I was involved in the incident\x01",
            "You did not do it, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Well, I think that it is not a rockstone … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Anyway Temée et al.\x01",
            "Today I will not gather information as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#2POs!\x02",
    )


    ChrTalk(
        0xB,
        "#3POs!\x02",
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

    # Function_12_28C0 end

    def Function_13_2A34(): pass

    label("Function_13_2A34")

    OP_4B(0xD, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_4B(0xC, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C96")

    ChrTalk(
        0xC,
        (
            "Mr. Waldo ……\x01",
            "What are you doing now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I do not know……\x01",
            "For those who sleep for a while\x01",
            "It seems I have not returned home ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I got a glimpse of it,\x01",
            "It is already three days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "港湾区の方でHueyさんたちが\x01",
            "Finally saw it … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Oh, it also took a voice\x01",
            "It was a neglected story … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "…… Anyway, to Mr. Wald\x01",
            "If something happens, it will be fine.\x01",
            "You will find it for you by hand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Two of you are this old city.\x01",
            "Listen to various people from one end and turn around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Os!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "OK!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F(Wald ……\x01",
            "I do not know where I am …? )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10303F(What is it … I do not mind.)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2D15")

    label("loc_2C96")


    ChrTalk(
        0x9,
        (
            "イグニスには、俺とLuganoffが\x01",
            "I will fill it in turn.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "If something happens, come over to report soon.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Os!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "OK!\x02",
    )

    CloseMessageWindow()

    label("loc_2D15")

    OP_4C(0xD, 0xFF)
    OP_4C(0x9, 0xFF)
    OP_4C(0xC, 0xFF)
    Return()

    # Function_13_2A34 end

    def Function_14_2D22(): pass

    label("Function_14_2D22")

    OP_4B(0xD, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_4B(0xC, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DE8")

    ChrTalk(
        0x9,
        (
            "How about it, yesterday from that\x01",
            "Did you see Mr. Wald?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "No, my person is not at all …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Oh, well.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "That's right, from a state of yesterday\x01",
            "I think that it's a hangover … …\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2E5D")

    label("loc_2DE8")


    ChrTalk(
        0x9,
        (
            "That's right … later again\x01",
            "Would you like to go see a sleeping appearance?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Come along with us, too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Os!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Of course!\x02",
    )

    CloseMessageWindow()

    label("loc_2E5D")

    OP_4C(0xD, 0xFF)
    OP_4C(0x9, 0xFF)
    OP_4C(0xC, 0xFF)
    Return()

    # Function_14_2D22 end

    def Function_15_2E6A(): pass

    label("Function_15_2E6A")

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
        "That's right …… Wald … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Yes,\x01",
            "To the shop while doing a fluffy … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I bought a considerable amount\x01",
            "Now by the sleeping people again\x01",
            "I guess they are drinking … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "To be honest …\x01",
            "The figure of such Waldo,\x01",
            "I did not want to see it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "No way … that person …\x01",
            "I drank it by sake …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "…… Oh, I feel the same.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "anyway……\x01",
            "Being drunk on the street\x01",
            "It is likely to be various Mazui.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Subsequently,\x01",
            "All will care it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Os!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "I understand.\x02",
    )

    CloseMessageWindow()
    OP_68(1930, 1000, -40, 1500)
    OP_6F(0x1)

    ChrTalk(
        0x101,
        "#00005FWald said so ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#00301FSo-called abandonment#4RYakke#Sake you a drunkard.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FIf it is too much\x01",
            "I'm worried about the body ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10308F………………………………\x02",
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

    # Function_15_2E6A end

    def Function_16_31FE(): pass

    label("Function_16_31FE")

    OP_4B(0xD, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_4B(0xC, 0xFF)

    ChrTalk(
        0x9,
        (
            "Wonder if there is something\x01",
            "すぐに俺かLuganoffを呼べよ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Os!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "I understand.\x02",
    )

    CloseMessageWindow()
    OP_4C(0xD, 0xFF)
    OP_4C(0x9, 0xFF)
    OP_4C(0xC, 0xFF)
    Return()

    # Function_16_31FE end

    def Function_17_326C(): pass

    label("Function_17_326C")

    OP_4B(0xD, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_4B(0xC, 0xFF)
    TurnDirection(0xD, 0x0, 0)
    TurnDirection(0xC, 0x0, 0)
    TurnDirection(0x9, 0x0, 0)

    ChrTalk(
        0xD,
        "O, you guys …!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Special Affairs Support Division … Wadi on it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Apparently, to Wald\x01",
            "It seems you have not met yet.\x02",
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
        "Well, that is ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "黙ってろ、Dino。\x01",
            "To a coward shake a tail to a suzuki\x01",
            "Nothing to talk about.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Lost if you can understand.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10303F… …. Good luck.\x02",
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

    # Function_17_326C end

    def Function_18_3412(): pass

    label("Function_18_3412")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3423")
    Jump("loc_37BB")

    label("loc_3423")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_3486")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_343E")
    Call(0, 11)
    Jump("loc_3481")

    label("loc_343E")


    ChrTalk(
        0xFE,
        (
            "(Whatever you say,\x01",
            "  Jedさんも迷ってるみたいだな……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3481")

    Jump("loc_37BB")

    label("loc_3486")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3494")
    Jump("loc_37BB")

    label("loc_3494")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_34A2")
    Jump("loc_37BB")

    label("loc_34A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_351E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34BD")
    Call(0, 12)
    Jump("loc_3519")

    label("loc_34BD")


    ChrTalk(
        0xFE,
        (
            "Is it an unidentified armed group ……\x01",
            "Even if it is attacked, it will be like running water\x01",
            "Do not go back to rushing down.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3519")

    Jump("loc_37BB")

    label("loc_351E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_355B")

    ChrTalk(
        0xFE,
        (
            "Luganoffさん……\x01",
            "It was serious and cool.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37BB")

    label("loc_355B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_35AC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16E, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3576")
    Call(0, 5)
    Jump("loc_35A7")

    label("loc_3576")


    ChrTalk(
        0xFE,
        (
            "100 thousand mirrors,\x01",
            "How to do such a big money ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35A7")

    Jump("loc_37BB")

    label("loc_35AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3651")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35C7")
    Call(0, 6)
    Jump("loc_364C")

    label("loc_35C7")


    ChrTalk(
        0xFE,
        (
            "I listened to various things but ……\x01",
            "Recently, seriously no one\x01",
            "I do not say you are not watching it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I thought that I left the city as though it was a treasure stone\x01",
            "I do not want to think but …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_364C")

    Jump("loc_37BB")

    label("loc_3651")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3662")
    Call(0, 7)
    Jump("loc_37BB")

    label("loc_3662")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3673")
    Call(0, 8)
    Jump("loc_37BB")

    label("loc_3673")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3750")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_371E")

    ChrTalk(
        0xFE,
        (
            "Happy\x01",
            "A moment ago\x01",
            "I could not get rid of it … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… Hey next time.\x01",
            "Remember, Wadi.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10303F………………………………\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_374B")

    label("loc_371E")


    ChrTalk(
        0xFE,
        (
            "…… Hey next time.\x01",
            "Remember, Wadi.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_374B")

    Jump("loc_37BB")

    label("loc_3750")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_37A1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_376B")
    Call(0, 19)
    Jump("loc_379C")

    label("loc_376B")


    ChrTalk(
        0xFE,
        (
            "Take care …\x01",
            "Think about a better way!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_379C")

    Jump("loc_37BB")

    label("loc_37A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_37B2")
    Call(0, 20)
    Jump("loc_37BB")

    label("loc_37B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_37BB")

    label("loc_37BB")

    TalkEnd(0xFE)
    Return()

    # Function_18_3412 end

    def Function_19_37BF(): pass

    label("Function_19_37BF")

    OP_4B(0xB, 0xFF)
    OP_4B(0xA, 0xFF)

    ChrTalk(
        0xA,
        "So, have you thought of a good plan?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Ow! Actually before I came here this morning\x01",
            "A sister holding a lot of bread\x01",
            "I saw it but yo.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "What is that cute it is already!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "… …. Ah? How about that story?\x01",
            "To Mr. Wald's mood\x01",
            "You mean connecting?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Oh, so\x01",
            "Next time to sneak that sister\x01",
            "You are going to church … …\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xA,
        "You are crazy, are not you! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Why are we in the church\x01",
            "You have to go!\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xB, 0xFF)
    OP_4C(0xA, 0xFF)
    SetScenarioFlags(0x0, 2)
    SetScenarioFlags(0x0, 3)
    Return()

    # Function_19_37BF end

    def Function_20_397E(): pass

    label("Function_20_397E")

    OP_4B(0xB, 0xFF)
    OP_4B(0xA, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B57")

    ChrTalk(
        0xB,
        (
            "Ha, Mr. Wald of this morning,\x01",
            "It was serious and I was scared.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Uchimasu … …\x01",
            "What is Mr. Waldo so far\x01",
            "Do you stick to a fucker?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Anyway the most troubling guy is\x01",
            "It's gone.\x01",
            "Rather be pleased … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "おいコラ、Slash！\x01",
            "Rare thing to do with your mouth.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "We are Mr. Wald\x01",
            "I will make an opinion a million years ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "More than that\x01",
            "Think about how you can fix Kigen!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Oh, oh.\x01",
            "I do not know ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3BD4")

    label("loc_3B57")


    ChrTalk(
        0xA,
        (
            "Want to talk about it now\x01",
            "Ask Mr. Wald to ask him.\x01",
            "You should not kill him at all! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "That was bad.\x01",
            "I do not say it anymore ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3BD4")

    OP_4C(0xB, 0xFF)
    OP_4C(0xA, 0xFF)
    Return()

    # Function_20_397E end

    def Function_21_3BDD(): pass

    label("Function_21_3BDD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3BEE")
    Jump("loc_3F60")

    label("loc_3BEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_3C2E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C09")
    Call(0, 11)
    Jump("loc_3C29")

    label("loc_3C09")


    ChrTalk(
        0xFE,
        "Hiakha, I got angry … …\x02",
    )

    CloseMessageWindow()

    label("loc_3C29")

    Jump("loc_3F60")

    label("loc_3C2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3C3C")
    Jump("loc_3F60")

    label("loc_3C3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3C4A")
    Jump("loc_3F60")

    label("loc_3C4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3CCA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C65")
    Call(0, 12)
    Jump("loc_3CC5")

    label("loc_3C65")


    ChrTalk(
        0xFE,
        (
            "Er …\x01",
            "Where did you get the Tonkachi and the nails?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Just in case,\x01",
            "I suppose that I will reinforce the clubs.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3CC5")

    Jump("loc_3F60")

    label("loc_3CCA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3D05")

    ChrTalk(
        0xFE,
        (
            "Well ~\x01",
            "Seniors are really cool!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F60")

    label("loc_3D05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3D62")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16E, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D20")
    Call(0, 5)
    Jump("loc_3D5D")

    label("loc_3D20")


    ChrTalk(
        0xFE,
        (
            "Well, I've become able to understand.\x01",
            "Someone please explain.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D5D")

    Jump("loc_3F60")

    label("loc_3D62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3DDC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D7D")
    Call(0, 6)
    Jump("loc_3DD7")

    label("loc_3D7D")


    ChrTalk(
        0xFE,
        (
            "As usual, even for sleeping people\x01",
            "It looks like he is not home but …\x01",
            "Where do you go to sleep?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3DD7")

    Jump("loc_3F60")

    label("loc_3DDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3DED")
    Call(0, 7)
    Jump("loc_3F60")

    label("loc_3DED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3DFE")
    Call(0, 8)
    Jump("loc_3F60")

    label("loc_3DFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3EED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E93")

    ChrTalk(
        0xFE,
        (
            "Hiakha, in the world\x01",
            "There is a hen fellow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……あれ、そういえば俺とHuey、\x01",
            "I was not fighting.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3EE8")

    label("loc_3E93")


    ChrTalk(
        0xFE,
        "… Well, can not you do small things?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Now I will tell you about Wald\x01",
            "Think about it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3EE8")

    Jump("loc_3F60")

    label("loc_3EED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3F46")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F08")
    Call(0, 19)
    Jump("loc_3F41")

    label("loc_3F08")


    ChrTalk(
        0xFE,
        (
            "That's it.\x01",
            "I'm sorry for the bad idea!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F41")

    Jump("loc_3F60")

    label("loc_3F46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3F57")
    Call(0, 20)
    Jump("loc_3F60")

    label("loc_3F57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3F60")

    label("loc_3F60")

    TalkEnd(0xFE)
    Return()

    # Function_21_3BDD end

    def Function_22_3F64(): pass

    label("Function_22_3F64")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_401E")

    ChrTalk(
        0xFE,
        (
            "Until Ms. Wald returns,\x01",
            "幹部のJedさんとLuganoffさんが\x01",
            "I decided to pull the saber viper.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Cooperate with everyone, get Viper\x01",
            "I have to protect you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4241")

    label("loc_401E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_402C")
    Jump("loc_4241")

    label("loc_402C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_403A")
    Jump("loc_4241")

    label("loc_403A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4048")
    Jump("loc_4241")

    label("loc_4048")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_4095")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4063")
    Call(0, 23)
    Jump("loc_4090")

    label("loc_4063")


    ChrTalk(
        0xFE,
        (
            "Mr. Wald,\x01",
            "I wonder what he is doing now ….\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4090")

    Jump("loc_4241")

    label("loc_4095")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4132")

    ChrTalk(
        0xFE,
        (
            "Think twice, the two of the executives\x01",
            "From the time of forming Saber Viper\x01",
            "It is a member …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Better than something\x01",
            "Always with Mr. Wald … …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4241")

    label("loc_4132")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_4185")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16E, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_414D")
    Call(0, 5)
    Jump("loc_4180")

    label("loc_414D")


    ChrTalk(
        0xFE,
        (
            "Mr. Waldo ……\x01",
            "Who on earth except me ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4180")

    Jump("loc_4241")

    label("loc_4185")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4193")
    Jump("loc_4241")

    label("loc_4193")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_41A4")
    Call(0, 13)
    Jump("loc_4241")

    label("loc_41A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_41B5")
    Call(0, 14)
    Jump("loc_4241")

    label("loc_41B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_41C6")
    Call(0, 16)
    Jump("loc_4241")

    label("loc_41C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4202")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14D, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_41E1")
    Call(0, 9)
    Jump("loc_41FD")

    label("loc_41E1")


    ChrTalk(
        0xFE,
        "Let's go somewhere soon!\x02",
    )

    CloseMessageWindow()

    label("loc_41FD")

    Jump("loc_4241")

    label("loc_4202")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_4238")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x137, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_421D")
    Call(0, 17)
    Jump("loc_4233")

    label("loc_421D")


    ChrTalk(
        0xFE,
        "Mr. Waldo ……\x02",
    )

    CloseMessageWindow()

    label("loc_4233")

    Jump("loc_4241")

    label("loc_4238")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4241")

    label("loc_4241")

    TalkEnd(0xFE)
    Return()

    # Function_22_3F64 end

    def Function_23_4245(): pass

    label("Function_23_4245")

    OP_4B(0xD, 0xFF)
    OP_4B(0xC, 0xFF)

    ChrTalk(
        0xD,
        (
            "Mr. Waldo ……\x01",
            "As expected after all it is not seen today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "That's right.\x01",
            "It also became a fuss about something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "……Anyways,\x01",
            "You should be safe.\x02",
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

    # Function_23_4245 end

    def Function_24_4301(): pass

    label("Function_24_4301")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4312")
    Jump("loc_481F")

    label("loc_4312")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_4320")
    Jump("loc_481F")

    label("loc_4320")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_432E")
    Jump("loc_481F")

    label("loc_432E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_463A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18D, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_45EF")
    OP_4B(0xFE, 0xFF)

    ChrTalk(
        0xFE,
        "Mr. Wald … … everyone ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108F……Dino君…………\x02",
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xFE, 0x0, 500)

    ChrTalk(
        0xFE,
        "…… What is the Special Affairs Division?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FThe other members ……\x01",
            "I am still in the hospital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Oh, all the members except me … ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "特にKokiさんが酷くて……\x01",
            "…… Even now everyone's in a different room ……\x01",
            "Huh, huh ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008FSorry … I was a little insensitive.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Higuri …. Beb … separately …\x01",
            "I do not need to care for something!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My seniors have a strong feeling\x01",
            "I am doing only safe ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Wow … damn!\x01",
            "Why … … why is this ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00208F(Mr. Lloyd ……\x01",
            "Let's make it one person now. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003F(Oh … I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10308F(…………………………)\x02",
    )

    CloseMessageWindow()
    OP_93(0xFE, 0x87, 0x0)
    OP_4C(0xFE, 0xFF)
    SetScenarioFlags(0x18D, 3)
    Jump("loc_4635")

    label("loc_45EF")


    ChrTalk(
        0xFE,
        "Mr. Wald … … everyone ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Why … … why is this ….\x02",
    )

    CloseMessageWindow()

    label("loc_4635")

    Jump("loc_481F")

    label("loc_463A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_46BA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4655")
    Call(0, 23)
    Jump("loc_46B5")

    label("loc_4655")


    ChrTalk(
        0xFE,
        "Gnostic, or …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Mr. Wald,\x01",
            "I do not even have Rubache\x01",
            "Where on earth are you …?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_46B5")

    Jump("loc_481F")

    label("loc_46BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_472F")

    ChrTalk(
        0xFE,
        "Hello, seniors are great, after all.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What's the time like this ……\x01",
            "I am somewhat glad a bit.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_481F")

    label("loc_472F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_4790")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16E, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_474A")
    Call(0, 5)
    Jump("loc_478B")

    label("loc_474A")


    ChrTalk(
        0xFE,
        (
            "Wow … Mr. Wald.\x01",
            "You are doing a dangerous job, no doubt ….\x02",
        )
    )

    CloseMessageWindow()

    label("loc_478B")

    Jump("loc_481F")

    label("loc_4790")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_47A1")
    Call(0, 13)
    Jump("loc_481F")

    label("loc_47A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_47B2")
    Call(0, 14)
    Jump("loc_481F")

    label("loc_47B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_47C3")
    Call(0, 16)
    Jump("loc_481F")

    label("loc_47C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_481F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x137, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_47DE")
    Call(0, 17)
    Jump("loc_481F")

    label("loc_47DE")


    ChrTalk(
        0xFE,
        (
            "ジェ、Jedさんの言う通り\x01",
            "It is because there is nothing to talk about.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_481F")

    TalkEnd(0xFE)
    Return()

    # Function_24_4301 end

    def Function_25_4823(): pass

    label("Function_25_4823")

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

    def lambda_48E9():
        OP_96(0xFE, 0x1C20, 0x0, 0xFFFFFD44, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_48E9)
    Sleep(400)

    def lambda_4906():
        OP_96(0xFE, 0x1CE8, 0x0, 0x2BC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_4906)
    Sleep(400)

    def lambda_4923():
        OP_96(0xFE, 0x170C, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4923)
    Sleep(400)

    def lambda_4940():
        OP_96(0xFE, 0x1900, 0x0, 0x4B0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4940)
    Sleep(400)

    def lambda_495D():
        OP_96(0xFE, 0x12C0, 0x0, 0xFFFFFD44, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_495D)
    Sleep(400)

    def lambda_497A():
        OP_96(0xFE, 0x13EC, 0x0, 0x2BC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_497A)
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

    def lambda_4A00():

        label("loc_4A00")

        TurnDirection(0xFE, 0x0, 500)
        Yield()
        Jump("loc_4A00")

    QueueWorkItem2(0x9, 2, lambda_4A00)

    def lambda_4A12():

        label("loc_4A12")

        TurnDirection(0xFE, 0x0, 500)
        Yield()
        Jump("loc_4A12")

    QueueWorkItem2(0xC, 2, lambda_4A12)

    def lambda_4A24():

        label("loc_4A24")

        TurnDirection(0xFE, 0x0, 500)
        Yield()
        Jump("loc_4A24")

    QueueWorkItem2(0xD, 2, lambda_4A24)

    ChrTalk(
        0x9,
        "#11PSatsu … … you came again.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#11PPerhaps even new information ……\x02",
    )

    CloseMessageWindow()

    def lambda_4A82():

        label("loc_4A82")

        TurnDirection(0xFE, 0x0, 500)
        Yield()
        Jump("loc_4A82")

    QueueWorkItem2(0x8, 2, lambda_4A82)

    def lambda_4A94():

        label("loc_4A94")

        TurnDirection(0xFE, 0x0, 500)
        Yield()
        Jump("loc_4A94")

    QueueWorkItem2(0xB, 2, lambda_4A94)

    def lambda_4AA6():

        label("loc_4AA6")

        TurnDirection(0xFE, 0x0, 500)
        Yield()
        Jump("loc_4AA6")

    QueueWorkItem2(0xA, 2, lambda_4AA6)
    OP_63(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_4AD3():

        label("loc_4AD3")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_4AD3")

    QueueWorkItem2(0xD, 2, lambda_4AD3)

    ChrTalk(
        0xD,
        "#11P…… Waa, you are!\x02",
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
        "#6P#10308F…………………………\x02",
    )

    CloseMessageWindow()

    def lambda_4BB0():

        label("loc_4BB0")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_4BB0")

    QueueWorkItem2(0x8, 2, lambda_4BB0)

    def lambda_4BC2():

        label("loc_4BC2")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_4BC2")

    QueueWorkItem2(0xB, 2, lambda_4BC2)

    def lambda_4BD4():

        label("loc_4BD4")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_4BD4")

    QueueWorkItem2(0xA, 2, lambda_4BD4)

    def lambda_4BE6():

        label("loc_4BE6")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_4BE6")

    QueueWorkItem2(0x9, 2, lambda_4BE6)

    def lambda_4BF8():

        label("loc_4BF8")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_4BF8")

    QueueWorkItem2(0xC, 2, lambda_4BF8)

    ChrTalk(
        0xA,
        "#5PTake it … …!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5POh well, misunderstood ……\x01",
            "Because of you, Mr. Waldo!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00001F(Cure … … It is a terrible mood indeed.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#00208F(Was it bad that I came …?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5P……………….\x02",
    )

    CloseMessageWindow()
    EndChrThread(0x8, 0x2)
    SetChrFlags(0x8, 0x40)

    def lambda_4CEC():
        OP_96(0xFE, 0x215C, 0x0, 0x2BC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_4CEC)
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
        "#11Pおい、Luganoff……？\x02",
    )

    CloseMessageWindow()

    def lambda_4DEC():

        label("loc_4DEC")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_4DEC")

    QueueWorkItem2(0x101, 2, lambda_4DEC)

    def lambda_4DFE():

        label("loc_4DFE")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_4DFE")

    QueueWorkItem2(0x102, 2, lambda_4DFE)

    def lambda_4E10():

        label("loc_4E10")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_4E10")

    QueueWorkItem2(0x103, 2, lambda_4E10)

    def lambda_4E22():

        label("loc_4E22")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_4E22")

    QueueWorkItem2(0x109, 2, lambda_4E22)

    def lambda_4E34():

        label("loc_4E34")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_4E34")

    QueueWorkItem2(0x104, 2, lambda_4E34)

    def lambda_4E46():

        label("loc_4E46")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_4E46")

    QueueWorkItem2(0x105, 2, lambda_4E46)

    def lambda_4E58():
        OP_95(0xFE, 8039, 0, 570, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_4E58)
    Sleep(50)
    WaitChrThread(0x8, 1)
    EndChrThread(0x105, 0x2)
    SetChrFlags(0x105, 0x20)
    SetChrFlags(0x105, 0x4)
    Sound(802, 0, 100, 0)

    def lambda_4E8D():
        OP_A6(0xFE, 0x0, 0x64, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_4E8D)

    def lambda_4EA6():
        OP_96(0xFE, 0x1CE8, 0xC8, 0x2BC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_4EA6)
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
        "#6P#10310F…………….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00011FHey, hey …!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10111FWas your …!\x02",
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    ChrTalk(
        0x8,
        (
            "#4S#11PYo, Wasi!\x01",
            "I understand you!\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    ChrTalk(
        0x8,
        (
            "#4S#11PMore than that, Mr. Valdo\x01",
            "Hand out to the medicine just right! Is it?\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    ChrTalk(
        0x8,
        (
            "#4S#11PThis also Zembu …\x01",
            "Zem, it's because of Teme!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00101F(B, Lloyd … ….\x01",
            "How far have you taught them? )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003F(Oh, it's a demonicization indeed\x01",
            "I have not said that until then … …)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#N#10108F(…, but I took Gnostic\x01",
            "I talked about the possibilities. )\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x8,
        (
            "#11P…… 2 years ago, if you must come\x01",
            "We have been … …\x01",
            "I was doing it for a long time …!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PTeme suddenly came there … …\x01",
            "I will enter Satsu this time on Omake\x01",
            "I do not understand Wake. Because of freakiness ……\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    ChrTalk(
        0x8,
        "#11P#4S… … Do you understand Kora! It is!#3S\x02",
    )

    CloseMessageWindow()

    def lambda_532B():
        OP_A6(0xFE, 0x32, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_532B)
    WaitChrThread(0x105, 2)

    ChrTalk(
        0x105,
        (
            "#6P#10303F…… I do not mean to be freaky.\x01",
            "Because it was necessary for me,\x01",
            "It is just that he chose this path.\x02\x03",
            "#10308FAs a result, Waldo\x01",
            "What happened to such a thing ……\x01",
            "It was unexpected to falling though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00303F… … Wadi …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11P…… So I said I will not resist it?\x02",
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    ChrTalk(
        0x8,
        "#11P#4S…… High-ranking, beat me to death!#3S\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#00210FIt is! It is!\x02",
    )

    CloseMessageWindow()

    def lambda_54A4():
        OP_A6(0xFE, 0x32, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_54A4)
    WaitChrThread(0x105, 2)
    Sleep(500)
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xFFFF)
    Sound(811, 0, 100, 0)

    def lambda_54E2():
        OP_9D(0xFE, 0x1A2C, 0x0, 0x2BC, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_54E2)
    ClearChrFlags(0x105, 0x4)
    ClearChrFlags(0x8, 0x40)
    WaitChrThread(0x105, 1)
    Sleep(500)

    ChrTalk(
        0x102,
        "#N#6P#00105FAh……\x02",
    )

    CloseMessageWindow()
    OP_5A()

    def lambda_5529():

        label("loc_5529")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_5529")

    QueueWorkItem2(0x101, 2, lambda_5529)

    def lambda_553B():

        label("loc_553B")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_553B")

    QueueWorkItem2(0x102, 2, lambda_553B)

    def lambda_554D():

        label("loc_554D")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_554D")

    QueueWorkItem2(0x103, 2, lambda_554D)

    def lambda_555F():

        label("loc_555F")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_555F")

    QueueWorkItem2(0x109, 2, lambda_555F)

    def lambda_5571():

        label("loc_5571")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_5571")

    QueueWorkItem2(0x104, 2, lambda_5571)

    ChrTalk(
        0xC,
        "#11PHuh……?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10305F………… What are you going to do?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PBukkake\x01",
            "I do not get my voice to that person now.\x01",
            "If it were to reach … only the voice of Teme.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P…… OK, I owe her.\x01",
            "Instead of Genko Ichi … …\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    ChrTalk(
        0x8,
        (
            "#4S#11PTemée has responsibility,\x01",
            "Please let Wald 's eyes wake up!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11PLuganoff……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#11PSenpai …\x02",
    )

    CloseMessageWindow()
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x105)

    ChrTalk(
        0x105,
        (
            "#6P#10308F…… Huh, that sort of thing.\x02\x03",
            "#10303F………………………………\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5744():

        label("loc_5744")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_5744")

    QueueWorkItem2(0x101, 2, lambda_5744)

    def lambda_5756():

        label("loc_5756")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_5756")

    QueueWorkItem2(0x102, 2, lambda_5756)

    def lambda_5768():

        label("loc_5768")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_5768")

    QueueWorkItem2(0x103, 2, lambda_5768)

    def lambda_577A():

        label("loc_577A")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_577A")

    QueueWorkItem2(0x109, 2, lambda_577A)

    def lambda_578C():

        label("loc_578C")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_578C")

    QueueWorkItem2(0x104, 2, lambda_578C)

    ChrTalk(
        0x101,
        "#12P#00005FWadi\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10303F…… I can not make a promise, but …\x01",
            "I will have as much hand as I can.\x02\x03",
            "#10301FAs a head of the testament ……\x01",
            "Kejime that failed him\x01",
            "Even in the meaning of attaching it again.\x02",
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

    # Function_25_4823 end

    def Function_26_5968(): pass

    label("Function_26_5968")


    def lambda_596D():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFE0C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_596D)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_26_5968 end

    SaveToFile()

Try(main)
