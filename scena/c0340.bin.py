from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c0340.bin",                # FileName
        "c0340",                    # MapName
        "c0340",                    # Location
        0x002D,                     # MapIndex
        "ed7150",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 45, 0, 6, 0, 7],
    )

    BuildStringList((
        "c0340",                  # 0
        "Mrs. Izuri",             # 1
        "Ferric",                 # 2
        "Cindy",                  # 3
        "Henri",                  # 4
        "Yunks",                  # 5
        "Marietta",               # 6
    ))

    AddCharChip((
        "chr/ch21700.itc",                   # 00
        "chr/ch21702.itc",                   # 01
        "chr/ch22000.itc",                   # 02
        "chr/ch22100.itc",                   # 03
        "chr/ch22200.itc",                   # 04
        "chr/ch27600.itc",                   # 05
        "chr/ch21900.itc",                   # 06
        "chr/ch22102.itc",                   # 07
        "chr/ch22202.itc",                   # 08
        "chr/ch27602.itc",                   # 09
    ))

    DeclNpc(40669,   0,       9600,    360,  261,  0x0, 0,   0,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(32659,   0,       5679,    180,  261,  0x0, 0,   2,   0,   0,   3,   0,   13,  255,  0)
    DeclNpc(4980,    0,       8989,    89,   261,  0x0, 0,   3,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(5329,    0,       3990,    90,   389,  0x0, 0,   4,   0,   0,   0,   0,   17,  255,  0)
    DeclNpc(689,     0,       990,     225,  389,  0x0, 0,   5,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(4294963586, 0,       5789,    225,  389,  0x0, 0,   6,   0,   0,   0,   0,   16,  255,  0)

    ChipFrameInfo(428, 0)                                        # 0

    ScpFunction((
        "Function_0_1AC",          # 00, 0
        "Function_1_264",          # 01, 1
        "Function_2_28F",          # 02, 2
        "Function_3_2B7",          # 03, 3
        "Function_4_2E2",          # 04, 4
        "Function_5_32F",          # 05, 5
        "Function_6_35A",          # 06, 6
        "Function_7_84E",          # 07, 7
        "Function_8_8CF",          # 08, 8
        "Function_9_1A9C",         # 09, 9
        "Function_10_1B9E",        # 0A, 10
        "Function_11_1CB1",        # 0B, 11
        "Function_12_1DD5",        # 0C, 12
        "Function_13_1EF1",        # 0D, 13
        "Function_14_2BA2",        # 0E, 14
        "Function_15_3982",        # 0F, 15
        "Function_16_3BC5",        # 10, 16
        "Function_17_3DE3",        # 11, 17
    ))


    def Function_0_1AC(): pass

    label("Function_0_1AC")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_1EC"),
        (1, "loc_1F8"),
        (2, "loc_204"),
        (3, "loc_210"),
        (4, "loc_21C"),
        (5, "loc_228"),
        (6, "loc_234"),
        (SWITCH_DEFAULT, "loc_240"),
    )


    label("loc_1EC")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_24C")

    label("loc_1F8")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_24C")

    label("loc_204")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_24C")

    label("loc_210")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_24C")

    label("loc_21C")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_24C")

    label("loc_228")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_24C")

    label("loc_234")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_24C")

    label("loc_240")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_24C")

    label("loc_24C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_263")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_24C")

    label("loc_263")

    Return()

    # Function_0_1AC end

    def Function_1_264(): pass

    label("Function_1_264")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_28E")
    OP_94(0xFE, 0xFFFFF510, 0xFFFFFF56, 0x11D0, 0x94C, 0x3E8)
    Sleep(300)
    Jump("Function_1_264")

    label("loc_28E")

    Return()

    # Function_1_264 end

    def Function_2_28F(): pass

    label("Function_2_28F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2B6")
    OP_94(0xFE, 0x14D2, 0xFFFFFCAE, 0xFFFFF6B4, 0x94C, 0x3E8)
    Jump("Function_2_28F")

    label("loc_2B6")

    Return()

    # Function_2_28F end

    def Function_3_2B7(): pass

    label("Function_3_2B7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2E1")
    OP_94(0xFE, 0x7738, 0x1126, 0x852A, 0x1D38, 0x3E8)
    Sleep(300)
    Jump("Function_3_2B7")

    label("loc_2E1")

    Return()

    # Function_3_2B7 end

    def Function_4_2E2(): pass

    label("Function_4_2E2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_32E")
    OP_95(0xFE, 1790, 0, 500, 900, 0x0)
    Sleep(500)
    OP_93(0xFE, 0x0, 0x1F4)
    OP_95(0xFE, 1790, 0, 1500, 900, 0x0)
    Sleep(500)
    OP_93(0xFE, 0xB4, 0x1F4)
    Jump("Function_4_2E2")

    label("loc_32E")

    Return()

    # Function_4_2E2 end

    def Function_5_32F(): pass

    label("Function_5_32F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_359")
    OP_94(0xFE, 0xF32, 0x2C6, 0x139C, 0x2634, 0x3E8)
    Sleep(300)
    Jump("Function_5_32F")

    label("loc_359")

    Return()

    # Function_5_32F end

    def Function_6_35A(): pass

    label("Function_6_35A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3BB")
    SetChrFlags(0x9, 0x80)
    SetChrPos(0x8, 36820, 200, 2990, 270)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 34130, 0, 4390, 135)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 32200, 0, 4080, 135)
    Jump("loc_84D")

    label("loc_3BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_3F0")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 2500, 200, 3760, 315)
    SetChrChipByIndex(0xB, 0x8)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    Jump("loc_84D")

    label("loc_3F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_45D")
    SetChrPos(0x8, 36820, 200, 2990, 270)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 34130, 0, 4390, 135)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 32200, 0, 4080, 135)
    SetChrPos(0xA, 32200, 0, 1340, 45)
    Jump("loc_84D")

    label("loc_45D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4BD")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 40600, 0, 8220, 270)
    SetChrPos(0x8, 38120, 0, 8230, 90)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A1")
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0xD, 0x10)

    label("loc_4A1")

    SetChrPos(0x9, 36730, 0, 7190, 90)
    BeginChrThread(0x9, 0, 0, 0)
    Jump("loc_84D")

    label("loc_4BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_4ED")
    SetChrPos(0x8, 36820, 200, 2990, 270)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    Jump("loc_84D")

    label("loc_4ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_534")
    SetChrPos(0x8, 36820, 200, 2990, 270)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    SetChrPos(0x9, 40670, 0, 9600, 0)
    BeginChrThread(0x9, 0, 0, 0)
    Jump("loc_84D")

    label("loc_534")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_58C")
    SetChrPos(0x8, 2560, 350, 6660, 225)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    SetChrPos(0xA, 3620, 0, 9800, 0)
    SetChrPos(0x9, 2370, 0, 9290, 45)
    BeginChrThread(0x9, 0, 0, 0)
    Jump("loc_84D")

    label("loc_58C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5D0")
    SetChrPos(0x8, 2370, 0, 9290, 45)
    SetChrFlags(0x8, 0x10)
    SetChrPos(0xA, 3620, 0, 9800, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5CB")
    SetChrFlags(0xA, 0x10)

    label("loc_5CB")

    Jump("loc_84D")

    label("loc_5D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_611")
    SetChrPos(0x8, 36820, 200, 2990, 270)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    SetChrPos(0xA, 3620, 0, 9800, 0)
    Jump("loc_84D")

    label("loc_611")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_646")
    SetChrPos(0x8, 36820, 200, 2990, 270)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    SetChrFlags(0xA, 0x80)
    Jump("loc_84D")

    label("loc_646")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_71A")
    SetChrPos(0x8, 2560, 350, 6660, 225)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, -630, 200, 6750, 135)
    SetChrChipByIndex(0xC, 0x9)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6AC")
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0xC, 0x10)

    label("loc_6AC")

    SetChrPos(0xA, 2380, 200, 3690, 315)
    SetChrChipByIndex(0xA, 0x7)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    SetChrSubChip(0xA, 0x1)
    SetChrFlags(0xA, 0x10)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -380, 200, 3780, 45)
    SetChrChipByIndex(0xB, 0x8)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    SetChrPos(0x9, 700, 0, 0, 270)
    BeginChrThread(0x9, 0, 0, 2)
    Jump("loc_84D")

    label("loc_71A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_74A")
    SetChrPos(0x8, 36820, 200, 2990, 270)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    Jump("loc_84D")

    label("loc_74A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_7AC")
    SetChrPos(0x8, 36820, 200, 2990, 270)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    SetChrPos(0x9, 4590, 0, 7300, 0)
    BeginChrThread(0x9, 0, 0, 0)
    SetChrFlags(0x9, 0x10)
    SetChrPos(0xA, 4590, 0, 9050, 180)
    SetChrFlags(0xA, 0x10)
    Jump("loc_84D")

    label("loc_7AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_822")
    SetChrPos(0x8, 2560, 350, 6660, 225)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    SetChrPos(0x9, 1000, 0, 7830, 135)
    BeginChrThread(0x9, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_802")
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x9, 0x10)

    label("loc_802")

    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 34000, 0, 6920, 90)
    Jump("loc_84D")

    label("loc_822")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_84D")
    SetChrPos(0x8, 36820, 200, 2990, 270)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)

    label("loc_84D")

    Return()

    # Function_6_35A end

    def Function_7_84E(): pass

    label("Function_7_84E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_893")
    SetMapObjFrame(0xFF, "light01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "model05_light", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_893")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8CE")
    OP_7D(0xD2, 0xD2, 0xE6, 0x0, 0x0)
    SetMapObjFrame(0xFF, "light01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "model05_light", 0x0, 0x1)

    label("loc_8CE")

    Return()

    # Function_7_84E end

    def Function_8_8CF(): pass

    label("Function_8_8CF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_9F0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_970")

    ChrTalk(
        0xFE,
        (
            "It's in times like these that people\x01",
            "should be with their families.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, thank goodness my\x01",
            "son and his wife are safe.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_9EB")

    label("loc_970")


    ChrTalk(
        0xFE,
        (
            "Thank goodness my son\x01",
            "and his wife are safe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's in times like these that people\x01",
            "should be with their families.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9EB")

    Jump("loc_1A98")

    label("loc_9F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_BC8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B02")

    ChrTalk(
        0xFE,
        (
            "What's important at any time\x01",
            "is to be confident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you're confident, contagious \x01",
            "things like fear and uneasiness\x01",
            "will be blown off for sure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The kids must be worried about\x01",
            "their parents too, but... \x01",
            "I have to pull myself together.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_BC3")

    label("loc_B02")


    ChrTalk(
        0xFE,
        (
            "If you're confident, contagious \x01",
            "things like fear and uneasiness\x01",
            "will be blown off for sure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The kids must be worried about\x01",
            "their parents too, but... \x01",
            "I have to pull myself together.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BC3")

    Jump("loc_1A98")

    label("loc_BC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_D6E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CC9")

    ChrTalk(
        0xFE,
        (
            "Terrible things will happen\x01",
            "to Crossbell going forward.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But, if our family sticks together,\x01",
            "I'm sure we'll be all right...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No matter what happens, if we\x01",
            "combine our strengths, we'll be\x01",
            "able to get through anything.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_D69")

    label("loc_CC9")


    ChrTalk(
        0xFE,
        (
            "Terrible things will happen\x01",
            "to Crossbell going forward...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No matter what happens, if we\x01",
            "combine our strengths, we'll be\x01",
            "able to get through anything.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D69")

    Jump("loc_1A98")

    label("loc_D6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_E40")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D89")
    Call(0, 9)
    Jump("loc_E3B")

    label("loc_D89")


    ChrTalk(
        0xFE,
        (
            "Because both my son and Mrs. Marietta\x01",
            "worked at the destroyed IBC building, \x01",
            "they are both very busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh*, I wish they would take better\x01",
            "care of themselves, though.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E3B")

    Jump("loc_1A98")

    label("loc_E40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_FD6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F35")

    ChrTalk(
        0xFE,
        (
            "An armed group? I don't\x01",
            "know where they came from\x01",
            "or why they're there, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because they involved innocent\x01",
            "people, they can't be forgiven.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I hope the CGF help\x01",
            "the people of Mainz\x01",
            "as soon as possible.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_FD1")

    label("loc_F35")


    ChrTalk(
        0xFE,
        (
            "Because they involved innocent\x01",
            "people, they can't be forgiven.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I hope the CGF help the people\x01",
            "of Mainz from that armed group\x01",
            "as soon as possible.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FD1")

    Jump("loc_1A98")

    label("loc_FD6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_10FF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_108A")

    ChrTalk(
        0xFE,
        (
            "It seems Henri went\x01",
            "out today, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Stay home on rainy days,\x01",
            "I told him, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I want him to be careful not\x01",
            "to get wet and catch a cold.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_10FA")

    label("loc_108A")


    ChrTalk(
        0xFE,
        (
            "Stay home on rainy days,\x01",
            "I told him, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I want him to be careful not\x01",
            "to get wet and catch a cold.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10FA")

    Jump("loc_1A98")

    label("loc_10FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_118F")

    ChrTalk(
        0xFE,
        (
            "I was teaching a cooking\x01",
            "trick to Cindy until\x01",
            "some time ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh*... Tea is especially\x01",
            "good after a bit of hard work.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A98")

    label("loc_118F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1205")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11AA")
    Call(0, 10)
    Jump("loc_1200")

    label("loc_11AA")


    ChrTalk(
        0xFE,
        (
            "All that's left is to wait for the baking\x01",
            "to be finished. Try doing it yourself.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1200")

    Jump("loc_1A98")

    label("loc_1205")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_138C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1304")

    ChrTalk(
        0xFE,
        (
            "Crossbell state\x01",
            "independence... I think it's\x01",
            "best if it's implemented.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Naturally, it will be\x01",
            "difficult due to opposition\x01",
            "by the Empire and Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But, knowing Mayor Dieter, I'm\x01",
            "sure he has some kind of plan...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1387")

    label("loc_1304")


    ChrTalk(
        0xFE,
        (
            "Crossbell state\x01",
            "independence... I think it's\x01",
            "best if it's implemented.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder if Mayor Dieter\x01",
            "has some kind of plan...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1387")

    Jump("loc_1A98")

    label("loc_138C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_14B7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1453")

    ChrTalk(
        0xFE,
        (
            "It seems that Cindy went\x01",
            "to visit our neighbor today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems she's often taking\x01",
            "cooking lessons from\x01",
            "Mr. Hayworth's wife...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I have to thank her next time.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_14B2")

    label("loc_1453")


    ChrTalk(
        0xFE,
        (
            "Mr. Hayworth's wife is often\x01",
            "taking care of my Cindy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I have to thank her next time.\x02",
    )

    CloseMessageWindow()

    label("loc_14B2")

    Jump("loc_1A98")

    label("loc_14B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_1557")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14D2")
    Call(0, 11)
    Jump("loc_1552")

    label("loc_14D2")


    ChrTalk(
        0xFE,
        (
            "Mrs. Marietta seems\x01",
            "to be busy too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems that it will be some time\x01",
            "before the entire family will dine together.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1552")

    Jump("loc_1A98")

    label("loc_1557")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_174B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16B7")

    ChrTalk(
        0xFE,
        (
            "You could see the inauguration ceremony\x01",
            "from Residential District too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A building so tall... It would've been\x01",
            "unthinkable to build it in the past.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They say the facilities\x01",
            "inside can't be compared with\x01",
            "those in the old City Hall...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems the inauguration\x01",
            "ceremony truly represents\x01",
            "an historic change.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1746")

    label("loc_16B7")


    ChrTalk(
        0xFE,
        (
            "Orchis Tower...\x01",
            "A building so tall would've been\x01",
            "unthinkable to build in the past.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Technological progress is\x01",
            "truly an amazing thing.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1746")

    Jump("loc_1A98")

    label("loc_174B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_18C9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1814")

    ChrTalk(
        0xFE,
        (
            "The other day, some kids from\x01",
            "the Republic moved here...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems they take pleasure\x01",
            "in annoying others.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh*, how sad... I wonder\x01",
            "how they were brought up.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_18C4")

    label("loc_1814")


    ChrTalk(
        0xFE,
        (
            "How children turn out depends entirely\x01",
            "on the way their parents raise them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think it's the parents' duty to make sure\x01",
            "their children do not go down the wrong path.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18C4")

    Jump("loc_1A98")

    label("loc_18C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_195A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18E4")
    Call(0, 12)
    Jump("loc_1955")

    label("loc_18E4")


    ChrTalk(
        0xFE,
        (
            "Ferric is often impolite,\x01",
            "but he's a considerate\x01",
            "and nice boy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uh uh, I'm happy \x01",
            "he's such a good kid.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1955")

    Jump("loc_1A98")

    label("loc_195A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1A98")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A0D")

    ChrTalk(
        0xFE,
        (
            "Henri does more than just\x01",
            "play lately. It seems he's\x01",
            "more focused on his studies.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uh uh. Maybe he has some good\x01",
            "competition at Sunday School.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1A98")

    label("loc_1A0D")


    ChrTalk(
        0xFE,
        (
            "Often playing and often\x01",
            "studying...that's how\x01",
            "children should be.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I want Henri to do\x01",
            "his very best at both\x01",
            "playing and studying.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A98")

    TalkEnd(0xFE)
    Return()

    # Function_8_8CF end

    def Function_9_1A9C(): pass

    label("Function_9_1A9C")

    OP_4B(0x8, 0xFF)
    OP_4B(0xD, 0xFF)

    ChrTalk(
        0x8,
        "Mrs. Marietta, you have returned.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Yes. It is because the IBC\x01",
            "main office was destroyed...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Today, I am planning to\x01",
            "help out at Orchis Tower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I understand... I know you are busy,\x01",
            "but take care of yourself, hm?\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0xD, 0x10)
    OP_4C(0x8, 0xFF)
    OP_4C(0xD, 0xFF)
    SetScenarioFlags(0x0, 0)
    Return()

    # Function_9_1A9C end

    def Function_10_1B9E(): pass

    label("Function_10_1B9E")

    OP_4B(0x8, 0xFF)
    OP_4B(0xA, 0xFF)

    ChrTalk(
        0xA,
        (
            "Oh, wow! You can\x01",
            "make cookies even\x01",
            "in a frypan!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Although you have to be careful\x01",
            "and make sure it doesn't stick,\x01",
            "the basic principle is the same.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Any number of tools\x01",
            "can be substituted.\x01",
            "You should remember that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "That's my grandma!\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x10)
    OP_4C(0x8, 0xFF)
    OP_4C(0xA, 0xFF)
    SetScenarioFlags(0x0, 0)
    Return()

    # Function_10_1B9E end

    def Function_11_1CB1(): pass

    label("Function_11_1CB1")


    ChrTalk(
        0x8,
        (
            "By the way, Yunks, I wonder\x01",
            "if you have a rough idea about\x01",
            "when Mrs. Marietta will return?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Hmm, maybe it will be difficult for the time being.\x01",
            "It seems she is really busy...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I see...\x01",
            "It seems that it will be some time\x01",
            "before the entire family will dine together.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0xC, 0x10)
    SetScenarioFlags(0x0, 0)
    Return()

    # Function_11_1CB1 end

    def Function_12_1DD5(): pass

    label("Function_12_1DD5")

    OP_4B(0x9, 0xFF)

    ChrTalk(
        0x8,
        (
            "...Ouchie, ouchie.\x01",
            "My joints ache on rainy days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I need some medicine\x01",
            "from St. Ursula\x01",
            "Hospital, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Grandma, you ok?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I'll take you to the\x01",
            "hospital, if you like.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x2)

    ChrTalk(
        0x8,
        "Uh uh. Thank you, Ferric.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "But, I'm fine, I can go by myself.\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0x9, 0x10)
    OP_4C(0x9, 0xFF)
    SetScenarioFlags(0x0, 0)
    SetScenarioFlags(0x0, 1)
    Return()

    # Function_12_1DD5 end

    def Function_13_1EF1(): pass

    label("Function_13_1EF1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1F02")
    Jump("loc_2B9E")

    label("loc_1F02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1F72")

    ChrTalk(
        0xFE,
        (
            "Those monsters are prowling\x01",
            "around outside, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm sure my parents\x01",
            "are all right...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B9E")

    label("loc_1F72")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_201C")

    ChrTalk(
        0xFE,
        (
            "It seems like strange things\x01",
            "are happening in Crossbell,\x01",
            "one after the next...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, grandma's here...\x01",
            "We'll be all right no matter what happens.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B9E")

    label("loc_201C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_208F")

    ChrTalk(
        0xFE,
        (
            "I haven't seen my mom since\x01",
            "the Anniversary Festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hehe, I'm just glad\x01",
            "she's all right.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B9E")

    label("loc_208F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_20ED")

    ChrTalk(
        0xFE,
        (
            "Something unthinkable\x01",
            "has happened...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This is no time\x01",
            "to be partying.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B9E")

    label("loc_20ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_21A1")

    ChrTalk(
        0xFE,
        (
            "Moisture is the natural enemy of suits.\x01",
            "You have to be especially careful on rainy days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've got to take good care of the\x01",
            "suit I'm wearing to the parties.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B9E")

    label("loc_21A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_232E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22A7")

    ChrTalk(
        0xFE,
        (
            "When I snatched the cookies\x01",
            "Cindy made, grandma scolded\x01",
            "me for poor manners.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm. Although I'm somehow\x01",
            "moving up in the world of high society,\x01",
            "poor manners are somewhat deadly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'll have to pay more attention next time.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2329")

    label("loc_22A7")


    ChrTalk(
        0xFE,
        (
            "When I snatched the cookies\x01",
            "Cindy made, grandma scolded\x01",
            "me for poor manners.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'll have to pay more attention next time.\x02",
    )

    CloseMessageWindow()

    label("loc_2329")

    Jump("loc_2B9E")

    label("loc_232E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_23BF")

    ChrTalk(
        0xFE,
        (
            "Oh, I think there's a sweet\x01",
            "smell coming up from downstairs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder if someone's making\x01",
            "sweets. I'll try to score one.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B9E")

    label("loc_23BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2548")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24C5")

    ChrTalk(
        0xFE,
        (
            "At the bankers' party I went to last night,\x01",
            "the topic of state independence came up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But I had no idea what was going on and\x01",
            "couldn't follow the conversation at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Maybe I'll follow grandma's\x01",
            "advice and read up on it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2543")

    label("loc_24C5")


    ChrTalk(
        0xFE,
        (
            "If I can't follow current topics,\x01",
            "I'll be left behind by high society.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think I'll ask grandma\x01",
            "about independence.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2543")

    Jump("loc_2B9E")

    label("loc_2548")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_25DF")

    ChrTalk(
        0xFE,
        (
            "Tch, that Cindy forced\x01",
            "the housework onto me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I guess I just gotta do it.\x01",
            "It'll do me good to do\x01",
            "housework every now and then.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B9E")

    label("loc_25DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_2730")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26BC")

    ChrTalk(
        0xFE,
        (
            "My father, who is busy with work,\x01",
            "has come back for dinner\x01",
            "after a long time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, now that I think about it,\x01",
            "we don't have enough chairs.\x01",
            "I must bring out one from the storage room...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_272B")

    label("loc_26BC")


    ChrTalk(
        0xFE,
        (
            "Oh, now that I think about it,\x01",
            "we don't have enough chairs.\x01",
            "I must bring out one from the storage room...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_272B")

    Jump("loc_2B9E")

    label("loc_2730")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_28B8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2819")

    ChrTalk(
        0xFE,
        (
            "The heads of state are going\x01",
            "to see the Arc-en-ciel tonight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After that, they're having a dinner\x01",
            "party at the Michelam guest house.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Must be nice. \x01",
            "I want to attend a party\x01",
            "like that someday.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_28B3")

    label("loc_2819")


    ChrTalk(
        0xFE,
        (
            "I heard the heads of state\x01",
            "are going to see the Arc-en-ciel\x01",
            "and have a dinner party.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Must be nice. \x01",
            "I want to attend a party\x01",
            "like that someday.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28B3")

    Jump("loc_2B9E")

    label("loc_28B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_293A")

    ChrTalk(
        0xFE,
        (
            "Hu hu, Cindy. If you\x01",
            "like, you can come\x01",
            "to the party, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm sure it will awaken\x01",
            "new values within you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B9E")

    label("loc_293A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_29C8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2955")
    Call(0, 12)
    Jump("loc_29C3")

    label("loc_2955")


    ChrTalk(
        0xFE,
        (
            "Tch, and I was just\x01",
            "saying I'll carry\x01",
            "grandma...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, that's very like her, \x01",
            "so I guess it's fine.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29C3")

    Jump("loc_2B9E")

    label("loc_29C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2B9E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B06")

    ChrTalk(
        0xFE,
        (
            "My father is in an IBC\x01",
            "Management Division official.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He has connections in high society too,\x01",
            "and often gets invited to parties.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But he's pretty busy,\x01",
            "so he lets me attend\x01",
            "the parties instead.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ah, but thanks to that, I'm\x01",
            "learning about high society\x01",
            "and improve every day.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2B9E")

    label("loc_2B06")


    ChrTalk(
        0xFE,
        (
            "Attending parties and\x01",
            "learning about high\x01",
            "society sure is fun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This is thanks to my father's connections.\x01",
            "Maybe this is what you call a perk.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B9E")

    TalkEnd(0xFE)
    Return()

    # Function_13_1EF1 end

    def Function_14_2BA2(): pass

    label("Function_14_2BA2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2C4B")

    ChrTalk(
        0xFE,
        (
            "It looks like Mrs. Sophia's\x01",
            "family is back from\x01",
            "Armorica Village.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uh uh, thank goodness. \x01",
            "I've got to get her to teach\x01",
            "me more about cooking.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_397E")

    label("loc_2C4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2DCC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D3A")

    ChrTalk(
        0xFE,
        (
            "Both my father and mother work\x01",
            "at Orchis Tower in IBC's\x01",
            "Management Division.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They went to work as usual, then this\x01",
            "happened. And they're not back yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "What should I do? I hope they're all right...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2DC7")

    label("loc_2D3A")


    ChrTalk(
        0xFE,
        (
            "My father and mother went to\x01",
            "work at Orchis Tower as usual\x01",
            "and they're not back yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "What should I do? I hope they're all right...\x02",
    )

    CloseMessageWindow()

    label("loc_2DC7")

    Jump("loc_397E")

    label("loc_2DCC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2FD3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F0B")

    ChrTalk(
        0xFE,
        (
            "My father and mother both work\x01",
            "at IBC' Management Division.\x01",
            "They're currently quite busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ever since talk of the asset\x01",
            "freeze appeared, it's affected\x01",
            "all manner of different things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "At a time like this I'd want\x01",
            "everyone to work together, but...\x01",
            "I guess we don't have a choice.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2FCE")

    label("loc_2F0B")


    ChrTalk(
        0xFE,
        (
            "My father and mother both work\x01",
            "at IBC' Management Division.\x01",
            "They're currently quite busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "At a time like this I'd want\x01",
            "everyone to work together, but...\x01",
            "I guess we don't have a choice.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FCE")

    Jump("loc_397E")

    label("loc_2FD3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_306F")

    ChrTalk(
        0xFE,
        (
            "Mother is back from her trip\x01",
            "abroad. ...That's a relief.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That incident happened and I'm worried\x01",
            "with my family separated like this.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_397E")

    label("loc_306F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_311D")

    ChrTalk(
        0xFE,
        (
            "I was frightened when I first\x01",
            "heard the news about the incident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It looks like a lot of CGF armored \x01",
            "vehicles were dispatched too... \x01",
            "Ooh, how scary.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_397E")

    label("loc_311D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3261")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31D6")

    ChrTalk(
        0xFE,
        (
            "There's no cooking class today... \x01",
            "So I was thinking of taking it easy at home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh yeah, maybe I should\x01",
            "try arranging the cookies\x01",
            "I made yesterday.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_325C")

    label("loc_31D6")


    ChrTalk(
        0xFE,
        (
            "Maybe I'll try mixing\x01",
            "chocolate chips into\x01",
            "the cookie batter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uh uh, once they're\x01",
            "done, I'll invite my\x01",
            "grandma to tea time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_325C")

    Jump("loc_397E")

    label("loc_3261")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_33CE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_335A")

    ChrTalk(
        0xFE,
        (
            "Just when I was delivering\x01",
            "cookies at Mrs. Sophia's\x01",
            "house, I heard some sirens.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When I turned to look, there were\x01",
            "quite a few ambulances passing by...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This isn't good. I wonder if\x01",
            "a large accident occurred.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_33C9")

    label("loc_335A")


    ChrTalk(
        0xFE,
        (
            "...Well, whatever. I won't\x01",
            "think too hard about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, I'm glad\x01",
            "Colin liked the\x01",
            "cookies I made.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33C9")

    Jump("loc_397E")

    label("loc_33CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3482")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33E9")
    Call(0, 10)
    Jump("loc_347D")

    label("loc_33E9")


    ChrTalk(
        0xFE,
        (
            "That's grandma for you.\x01",
            "To think you can make cookies\x01",
            "even without an oven!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uh uh. I think I'll show this\x01",
            "technique to Mrs. Sophia later.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_347D")

    Jump("loc_397E")

    label("loc_3482")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_35AC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_352B")

    ChrTalk(
        0xFE,
        "Huh? The oven's broken...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And just when Mrs. Sophia showed\x01",
            "me a cookies baking method. \x01",
            "At this rate, I won't be baking anything...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_35A7")

    label("loc_352B")


    ChrTalk(
        0xFE,
        (
            "*sigh*, and just when Mrs. Sophia\x01",
            "showed me a cookies baking method.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The oven's broken, and\x01",
            "I can't try it out...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35A7")

    Jump("loc_397E")

    label("loc_35AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_35BA")
    Jump("loc_397E")

    label("loc_35BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_371B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36D4")

    ChrTalk(
        0xFE,
        (
            "Henri, you went to see\x01",
            "Orchis Tower from up close, right?\x01",
            "How was it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Was it big like I think?\x01",
            "It seemed to have cost a lot of mira?\x01",
            "Were there a lot of people?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "W-Wait a moment, big sister.\x01",
            "I can't answer if you ask\x01",
            "so many things at once.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3716")

    label("loc_36D4")


    ChrTalk(
        0xFE,
        (
            "What's wrong with that?\x01",
            "Don't be a cheapskate and tell me...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3716")

    Jump("loc_397E")

    label("loc_371B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_37BE")

    ChrTalk(
        0xFE,
        (
            "Looks like Henri went\x01",
            "with his friend to go\x01",
            "see Orchis Tower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, to go even though\x01",
            "it was so crowded...\x01",
            "Children have a lot of stamina.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_397E")

    label("loc_37BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3827")

    ChrTalk(
        0xFE,
        (
            "Brother, are you going\x01",
            "to a party tonight?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "You never get tired of those, do you.\x02",
    )

    CloseMessageWindow()
    Jump("loc_397E")

    label("loc_3827")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3835")
    Jump("loc_397E")

    label("loc_3835")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_397E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38E6")

    ChrTalk(
        0xFE,
        "Yeah, this is a great flavor☆\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My cooking just keeps\x01",
            "getting better and better.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uh uh. It's probably because\x01",
            "of Mrs. Sophia's lessons.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_397E")

    label("loc_38E6")


    ChrTalk(
        0xFE,
        (
            "Our neighbor, Mrs. Sophia, \x01",
            "has been giving me cooking \x01",
            "lessons every now and then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uh uh. Thanks to her, my cooking\x01",
            "has gotten a lot better.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_397E")

    TalkEnd(0xFE)
    Return()

    # Function_14_2BA2 end

    def Function_15_3982(): pass

    label("Function_15_3982")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3A3E")

    ChrTalk(
        0xFE,
        (
            "We were locked up inside\x01",
            "Orchis Tower alongside\x01",
            "the other staff members.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Although I worried my children\x01",
            "and mother, thank goodness I\x01",
            "was able to return somehow.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3BC1")

    label("loc_3A3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_3A4C")
    Jump("loc_3BC1")

    label("loc_3A4C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3B24")

    ChrTalk(
        0xFE,
        (
            "We don't know when an attack like\x01",
            "the other day will come again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And in this situation, it wouldn't\x01",
            "be strange if something did happen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As the breadwinner, I've\x01",
            "got to protect my family.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3BC1")

    label("loc_3B24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B36")
    Call(0, 11)
    Jump("loc_3BC1")

    label("loc_3B36")


    ChrTalk(
        0xFE,
        (
            "My wife Marietta works\x01",
            "at an IBC branch abroad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She seems to be busy there, so it won't be\x01",
            "anytime soon when she'll come home...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3BC1")

    TalkEnd(0xFE)
    Return()

    # Function_15_3982 end

    def Function_16_3BC5(): pass

    label("Function_16_3BC5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3C62")

    ChrTalk(
        0xFE,
        (
            "While we were gone, it seems\x01",
            "my mother-in-law was taking\x01",
            "well care our children.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uh uh, I'm really no match\x01",
            "for my mother-in-law.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3DDF")

    label("loc_3C62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_3C70")
    Jump("loc_3DDF")

    label("loc_3C70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3D12")

    ChrTalk(
        0xFE,
        (
            "Since the address, my husband\x01",
            "and I got special permission\x01",
            "to come check on our home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uh uh. I'm thankful I can\x01",
            "rely on my mother-in-law.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3DDF")

    label("loc_3D12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3DDF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D2D")
    Call(0, 9)
    Jump("loc_3DDF")

    label("loc_3D2D")


    ChrTalk(
        0xFE,
        (
            "Uh uh. I am relieved to learn my\x01",
            "children and my mother-in-law as\x01",
            "well weren't hurt in the attack.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Now then... I have to\x01",
            "hurry and go help the IBC\x01",
            "Management Division.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3DDF")

    TalkEnd(0xFE)
    Return()

    # Function_16_3BC5 end

    def Function_17_3DE3(): pass

    label("Function_17_3DE3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3DF4")
    Jump("loc_40F4")

    label("loc_3DF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_3E9C")

    ChrTalk(
        0xFE,
        (
            "The government's food allowance hasn't come\x01",
            "in ever since martial law was declared.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "It'll be tough if this situation goes on too much longer...\x02",
    )

    CloseMessageWindow()
    Jump("loc_40F4")

    label("loc_3E9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3EAA")
    Jump("loc_40F4")

    label("loc_3EAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_3FD2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F53")

    ChrTalk(
        0xFE,
        "*munch munch*...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, everyone from the Support Section.\x01",
            "Do you need something from me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Would you like to\x01",
            "have dinner together?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3FCD")

    label("loc_3F53")


    ChrTalk(
        0xFE,
        (
            "By the way, the noon's\x01",
            "inauguration was amazing, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You policemen are probably busy,\x01",
            "but please do your best.\x01\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3FCD")

    Jump("loc_40F4")

    label("loc_3FD2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_40F4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4076")

    ChrTalk(
        0xFE,
        (
            "I got a lot of homework from\x01",
            "Sunday School yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Lately, KeA has been\x01",
            "beating me on our tests.\x01",
            "I'll have to study harder.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_40F4")

    label("loc_4076")


    ChrTalk(
        0xFE,
        (
            ""What's important is self-study."\x01",
            "My grandma says that too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll study hard, in\x01",
            "order to beat KeA\x01",
            "on our next test.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_40F4")

    TalkEnd(0xFE)
    Return()

    # Function_17_3DE3 end

    SaveToFile()

Try(main)
