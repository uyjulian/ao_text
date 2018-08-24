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
        "Function_9_1A36",         # 09, 9
        "Function_10_1B27",        # 0A, 10
        "Function_11_1C3A",        # 0B, 11
        "Function_12_1D4A",        # 0C, 12
        "Function_13_1E61",        # 0D, 13
        "Function_14_2AD8",        # 0E, 14
        "Function_15_3800",        # 0F, 15
        "Function_16_3A43",        # 10, 16
        "Function_17_3C56",        # 11, 17
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
            "It's in times like these\x01",
            "that people should be\x01",
            "with their families.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, thank goodness\x01",
            "my son and his wife are\x01",
            "safe.\x02",
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
            "It's in times like these\x01",
            "that people should be\x01",
            "with their families.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9EB")

    Jump("loc_1A32")

    label("loc_9F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_B84")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AEC")

    ChrTalk(
        0xFE,
        (
            "No matter the situation,\x01",
            "you have to keep what's\x01",
            "important to you close.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you're confident,\x01",
            "it'll rub off on others.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The kids must be worried about\x01",
            "my son and his wife, but... I\x01",
            "have to pull myself together.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_B7F")

    label("loc_AEC")


    ChrTalk(
        0xFE,
        (
            "If you're confident,\x01",
            "it'll rub off on others.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The kids must be worried about\x01",
            "my son and his wife, but... I\x01",
            "have to pull myself together.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B7F")

    Jump("loc_1A32")

    label("loc_B84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_D2A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C85")

    ChrTalk(
        0xFE,
        (
            "Terrible things will\x01",
            "happen to Crossbell\x01",
            "going forward.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But, if our family sticks\x01",
            "together, I'm sure we'll\x01",
            "be all right...\x02",
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
    Jump("loc_D25")

    label("loc_C85")


    ChrTalk(
        0xFE,
        (
            "Terrible things will\x01",
            "happen to Crossbell\x01",
            "going forward...\x02",
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

    label("loc_D25")

    Jump("loc_1A32")

    label("loc_D2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_DF1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D45")
    Call(0, 9)
    Jump("loc_DEC")

    label("loc_D45")


    ChrTalk(
        0xFE,
        (
            "Because both my son and Marietta\x01",
            "worked at the destroyed IBC\x01",
            "building, they're both very busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh*, I wish they'd\x01",
            "take better care of\x01",
            "themselves, though.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DEC")

    Jump("loc_1A32")

    label("loc_DF1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_F88")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EE6")

    ChrTalk(
        0xFE,
        (
            "An armed group? I don't\x01",
            "know where they came from\x01",
            "or why they're here, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because they involved\x01",
            "innocent people, they\x01",
            "can't be forgiven.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I hope the CGF helps the\x01",
            "people of Mainz as soon\x01",
            "as possible.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_F83")

    label("loc_EE6")


    ChrTalk(
        0xFE,
        (
            "Because they involved\x01",
            "innocent people, they\x01",
            "can't be forgiven.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I hope the CGF saves the people\x01",
            "of Mainz from that armed group\x01",
            "as soon as possible.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F83")

    Jump("loc_1A32")

    label("loc_F88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_10AF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_103B")

    ChrTalk(
        0xFE,
        (
            "It seems Henri went out\x01",
            "today, too.\x02",
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
            "I want him to take care\x01",
            "not to get wet and catch\x01",
            "a cold.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_10AA")

    label("loc_103B")


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
            "I want him to take care\x01",
            "not to get wet and catch\x01",
            "a cold.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10AA")

    Jump("loc_1A32")

    label("loc_10AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1132")

    ChrTalk(
        0xFE,
        (
            "Cindy was teaching me a\x01",
            "cooking trick just now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh*... Tea is\x01",
            "especially good after a\x01",
            "bit of hard work.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A32")

    label("loc_1132")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_11A7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_114D")
    Call(0, 10)
    Jump("loc_11A2")

    label("loc_114D")


    ChrTalk(
        0xFE,
        (
            "All that's left is to wait\x01",
            "for the baking to finish.\x01",
            "Look at what I did myself.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11A2")

    Jump("loc_1A32")

    label("loc_11A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_132E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12A6")

    ChrTalk(
        0xFE,
        (
            "Crossbell State\x01",
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
            "But, knowing Mayor\x01",
            "Dieter, I'm sure he has\x01",
            "some kind of plan...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1329")

    label("loc_12A6")


    ChrTalk(
        0xFE,
        (
            "Crossbell State\x01",
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

    label("loc_1329")

    Jump("loc_1A32")

    label("loc_132E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_144F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13ED")

    ChrTalk(
        0xFE,
        (
            "It seems Cindy went to\x01",
            "visit our neighbor\x01",
            "today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems she often takes\x01",
            "cooking lessons from Mr.\x01",
            "Hayworth's wife...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I have to thank her next\x01",
            "time.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_144A")

    label("loc_13ED")


    ChrTalk(
        0xFE,
        (
            "Mr. Hayworth's wife\x01",
            "Cindy is always helping\x01",
            "me out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I have to thank her next\x01",
            "time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_144A")

    Jump("loc_1A32")

    label("loc_144F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_14EA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_146A")
    Call(0, 11)
    Jump("loc_14E5")

    label("loc_146A")


    ChrTalk(
        0xFE,
        (
            "Marietta seems to be\x01",
            "busy too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems that it will be\x01",
            "some time before the entire\x01",
            "family will dine together.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14E5")

    Jump("loc_1A32")

    label("loc_14EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_16EA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1649")

    ChrTalk(
        0xFE,
        (
            "I saw the unveiling\x01",
            "ceremony from Residential\x01",
            "District, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because the building is so tall,\x01",
            "they must've been thinking about\x01",
            "building it for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They say the facilities\x01",
            "inside can't be compared with\x01",
            "those in the old City Hall.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems the unveiling\x01",
            "ceremony truly represents\x01",
            "a historic change.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_16E5")

    label("loc_1649")


    ChrTalk(
        0xFE,
        (
            "Orchis Tower... Because it's so\x01",
            "tall, they must've been thinking\x01",
            "about building it for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Technological progress\x01",
            "is truly an amazing\x01",
            "thing.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16E5")

    Jump("loc_1A32")

    label("loc_16EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1865")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17B3")

    ChrTalk(
        0xFE,
        (
            "The other day, some kids\x01",
            "from the Republic moved\x01",
            "here...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems they take\x01",
            "pleasure in annoying\x01",
            "others.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh*, how sad... I\x01",
            "wonder how they were\x01",
            "brought up.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1860")

    label("loc_17B3")


    ChrTalk(
        0xFE,
        (
            "How children turn out\x01",
            "depends entirely on the way\x01",
            "their parents raise them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think it's a parents duty to\x01",
            "make sure their children do\x01",
            "not go down the wrong path.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1860")

    Jump("loc_1A32")

    label("loc_1865")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_18F4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1880")
    Call(0, 12)
    Jump("loc_18EF")

    label("loc_1880")


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
            "Haha, I'm happy he's\x01",
            "such a good kid.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18EF")

    Jump("loc_1A32")

    label("loc_18F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1A32")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19A6")

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
            "Haha. Maybe he has some\x01",
            "good competition at\x01",
            "Sunday School.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1A32")

    label("loc_19A6")


    ChrTalk(
        0xFE,
        (
            "Often playing and often\x01",
            "studying... that's how\x01",
            "children should be.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I want Henri to do his\x01",
            "very best at both\x01",
            "playing and studying.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A32")

    TalkEnd(0xFE)
    Return()

    # Function_8_8CF end

    def Function_9_1A36(): pass

    label("Function_9_1A36")

    OP_4B(0x8, 0xFF)
    OP_4B(0xD, 0xFF)

    ChrTalk(
        0x8,
        (
            "Marietta, you've\x01",
            "returned.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Yes. It's because the\x01",
            "IBC main office was\x01",
            "destroyed...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Today, I'm planning to\x01",
            "help out at Orchis\x01",
            "Tower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I see... I know you're\x01",
            "busy, but take care of\x01",
            "yourself, ok?\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0xD, 0x10)
    OP_4C(0x8, 0xFF)
    OP_4C(0xD, 0xFF)
    SetScenarioFlags(0x0, 0)
    Return()

    # Function_9_1A36 end

    def Function_10_1B27(): pass

    label("Function_10_1B27")

    OP_4B(0x8, 0xFF)
    OP_4B(0xA, 0xFF)

    ChrTalk(
        0xA,
        (
            "Oh, wow! You can make\x01",
            "cookies even in a\x01",
            "frypan!\x02",
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
            "Any number of tools can\x01",
            "be substituted. You\x01",
            "should remember that.\x02",
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

    # Function_10_1B27 end

    def Function_11_1C3A(): pass

    label("Function_11_1C3A")


    ChrTalk(
        0x8,
        (
            "By the way, Yunks, I wonder if\x01",
            "you have a rough idea about\x01",
            "when Marietta will return?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Hmm. It might be difficult\x01",
            "for the time being. She\x01",
            "seems really busy...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I see... It seems that it\x01",
            "will be some time before our\x01",
            "entire family dines together.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0xC, 0x10)
    SetScenarioFlags(0x0, 0)
    Return()

    # Function_11_1C3A end

    def Function_12_1D4A(): pass

    label("Function_12_1D4A")

    OP_4B(0x9, 0xFF)

    ChrTalk(
        0x8,
        (
            "...Ouchie, ouchie. My\x01",
            "joints ache on rainy\x01",
            "days.\x02",
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
        "Haha. Thank you, Ferric.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "But, I'm fine going by\x01",
            "myself.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0x9, 0x10)
    OP_4C(0x9, 0xFF)
    SetScenarioFlags(0x0, 0)
    SetScenarioFlags(0x0, 1)
    Return()

    # Function_12_1D4A end

    def Function_13_1E61(): pass

    label("Function_13_1E61")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1E72")
    Jump("loc_2AD4")

    label("loc_1E72")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1EE2")

    ChrTalk(
        0xFE,
        (
            "Those monsters are\x01",
            "prowling around outside,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm sure my parents are\x01",
            "all right...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AD4")

    label("loc_1EE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1F8E")

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
            "Well, my grandma's\x01",
            "here... I'll be all right\x01",
            "no matter what happens.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AD4")

    label("loc_1F8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1FFF")

    ChrTalk(
        0xFE,
        (
            "My parents celebrated\x01",
            "their anniversary\x01",
            "recently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hehe, I'm just glad\x01",
            "they're all right.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AD4")

    label("loc_1FFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2057")

    ChrTalk(
        0xFE,
        (
            "The unthinkable has\x01",
            "happened...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This is no time to be\x01",
            "partying.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AD4")

    label("loc_2057")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_210A")

    ChrTalk(
        0xFE,
        (
            "Moisture is the natural enemy of\x01",
            "suits. You have to be especially\x01",
            "careful on rainy days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've got to take good\x01",
            "care of the suit I'm\x01",
            "wearing to that party.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AD4")

    label("loc_210A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_226E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21EC")

    ChrTalk(
        0xFE,
        (
            "When I ate the cookies\x01",
            "Cindy made, grandma scolded\x01",
            "me for poor manners.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm. Somehow, in the\x01",
            "world of high society,\x01",
            "poor manners are deadly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll have to pay more\x01",
            "attention next time.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2269")

    label("loc_21EC")


    ChrTalk(
        0xFE,
        (
            "When I ate the cookies\x01",
            "Cindy made, grandma scolded\x01",
            "me for poor manners.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll have to pay more\x01",
            "attention next time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2269")

    Jump("loc_2AD4")

    label("loc_226E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_22FF")

    ChrTalk(
        0xFE,
        (
            "Oh, I think there's a\x01",
            "sweet smell coming up\x01",
            "from downstairs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder if someone's\x01",
            "making sweets. I'll try\x01",
            "to score one.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AD4")

    label("loc_22FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2488")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2405")

    ChrTalk(
        0xFE,
        (
            "At the bankers' party I went\x01",
            "to last night, the topic of\x01",
            "state independence came up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But I had no idea what was\x01",
            "going on and couldn't follow\x01",
            "the conversation at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Maybe I'll follow\x01",
            "grandma's advice and\x01",
            "read up on it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2483")

    label("loc_2405")


    ChrTalk(
        0xFE,
        (
            "If I can't follow current\x01",
            "topics, I'll be left\x01",
            "behind by high society.\x02",
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

    label("loc_2483")

    Jump("loc_2AD4")

    label("loc_2488")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_251F")

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
    Jump("loc_2AD4")

    label("loc_251F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_266D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25F9")

    ChrTalk(
        0xFE,
        (
            "Father, who is busy with\x01",
            "work, has come home for\x01",
            "dinner after a long time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, now that I think about it, we\x01",
            "don't have enough chairs. I have to\x01",
            "go get one from the storage room...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2668")

    label("loc_25F9")


    ChrTalk(
        0xFE,
        (
            "Oh, now that I think about it, we\x01",
            "don't have enough chairs. I have to\x01",
            "go get one from the storage room...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2668")

    Jump("loc_2AD4")

    label("loc_266D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_27F1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2757")

    ChrTalk(
        0xFE,
        (
            "The heads of state are\x01",
            "going to see Arc-en-Ciel\x01",
            "tonight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After that, they're having\x01",
            "a dinner party at the\x01",
            "Michelam state guest house.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Must be nice. I want to\x01",
            "attend a party like that\x01",
            "someday.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_27EC")

    label("loc_2757")


    ChrTalk(
        0xFE,
        (
            "I heard the heads of state\x01",
            "are going to see Arc-en-Ciel\x01",
            "and have a dinner party.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Must be nice. I want to\x01",
            "attend a party like that\x01",
            "someday.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27EC")

    Jump("loc_2AD4")

    label("loc_27F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2872")

    ChrTalk(
        0xFE,
        (
            "Haha, Cindy. If you\x01",
            "like, you can come to\x01",
            "the party, too.\x02",
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
    Jump("loc_2AD4")

    label("loc_2872")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_28FD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_288D")
    Call(0, 12)
    Jump("loc_28F8")

    label("loc_288D")


    ChrTalk(
        0xFE,
        (
            "Tch, and I was just\x01",
            "saying I'd take\x01",
            "grandma...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, that's very like\x01",
            "her, so I guess it's\x01",
            "fine.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28F8")

    Jump("loc_2AD4")

    label("loc_28FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2AD4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A3B")

    ChrTalk(
        0xFE,
        (
            "My old man is an IBC\x01",
            "operations department\x01",
            "official.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He has connections in high\x01",
            "society too, and often\x01",
            "gets invited to parties.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But he's pretty busy. So\x01",
            "he lets me attend the\x01",
            "parties instead.\x02",
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
    Jump("loc_2AD4")

    label("loc_2A3B")


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
            "This is thanks to my old\x01",
            "man's connections. Maybe this\x01",
            "is what you call a perk.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2AD4")

    TalkEnd(0xFE)
    Return()

    # Function_13_1E61 end

    def Function_14_2AD8(): pass

    label("Function_14_2AD8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2B7A")

    ChrTalk(
        0xFE,
        (
            "It looks like Sophia's\x01",
            "family is back from\x01",
            "Armorica Village.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha, thank goodness. I've\x01",
            "got to get her to teach me\x01",
            "more about cooking.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37FC")

    label("loc_2B7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2CF9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C69")

    ChrTalk(
        0xFE,
        (
            "Both my mom and dad work\x01",
            "at Orchis Tower in IBC's\x01",
            "Operations Department.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They went to work as\x01",
            "usual, then this happened.\x01",
            "And they're not back yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What should I do? Oh, I\x01",
            "hope they're all\x01",
            "right...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2CF4")

    label("loc_2C69")


    ChrTalk(
        0xFE,
        (
            "My mom and dad went to work\x01",
            "at Orchis Tower as usual\x01",
            "and they're not back yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What should I do? Oh, I\x01",
            "hope they're all\x01",
            "right...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CF4")

    Jump("loc_37FC")

    label("loc_2CF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2EB0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E10")

    ChrTalk(
        0xFE,
        (
            "What should I do? Oh, I\x01",
            "hope they're all\x01",
            "right...\x02",
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
    Jump("loc_2EAB")

    label("loc_2E10")


    ChrTalk(
        0xFE,
        (
            "What should I do? Oh, I\x01",
            "hope they're all\x01",
            "right...\x02",
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

    label("loc_2EAB")

    Jump("loc_37FC")

    label("loc_2EB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2F4A")

    ChrTalk(
        0xFE,
        (
            "Mom is back from her\x01",
            "trip abroad. ...That's a\x01",
            "relief.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That incident happened, and\x01",
            "I'm worried with my family\x01",
            "separated like this.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37FC")

    label("loc_2F4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2FF2")

    ChrTalk(
        0xFE,
        (
            "I was frightened when I\x01",
            "first heard the news\x01",
            "about the incident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It looks like a lot of CGF\x01",
            "armored cars were dispatched\x01",
            "too... Ooh, how scary.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37FC")

    label("loc_2FF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3135")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30AA")

    ChrTalk(
        0xFE,
        (
            "There's no cooking class\x01",
            "today... So I was thinking\x01",
            "of taking it easy at home.\x02",
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
    Jump("loc_3130")

    label("loc_30AA")


    ChrTalk(
        0xFE,
        (
            "Maybe I'll try mixing\x01",
            "chocolate chips into the\x01",
            "cookie batter~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha, once they're done,\x01",
            "I'll invite my grandma\x01",
            "to tea time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3130")

    Jump("loc_37FC")

    label("loc_3135")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3284")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3210")

    ChrTalk(
        0xFE,
        (
            "Just when Sophia was\x01",
            "delivering cookies, she\x01",
            "heard sirens.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When she turned to look,\x01",
            "there were quite a few\x01",
            "ambulances...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This isn't good. I\x01",
            "wonder if a large\x01",
            "accident occurred.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_327F")

    label("loc_3210")


    ChrTalk(
        0xFE,
        (
            "...Well, whatever. I\x01",
            "won't think too hard\x01",
            "about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, I'm glad Colin\x01",
            "liked the cookies I\x01",
            "made.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_327F")

    Jump("loc_37FC")

    label("loc_3284")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3332")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_329F")
    Call(0, 10)
    Jump("loc_332D")

    label("loc_329F")


    ChrTalk(
        0xFE,
        (
            "That's grandma for you. To\x01",
            "think you can make cookies\x01",
            "even without an oven!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha. I think I'll show\x01",
            "this technique to Sophia\x01",
            "later.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_332D")

    Jump("loc_37FC")

    label("loc_3332")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3449")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33D1")

    ChrTalk(
        0xFE,
        (
            "Huh? The oven's\x01",
            "broken...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And just when Sophia showed me\x01",
            "this baking method. At this rate,\x01",
            "I won't be baking anything~...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3444")

    label("loc_33D1")


    ChrTalk(
        0xFE,
        (
            "*sigh*, and just when\x01",
            "Sophia showed me this\x01",
            "baking method.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The oven's broken, and I\x01",
            "can't try it out~...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3444")

    Jump("loc_37FC")

    label("loc_3449")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3457")
    Jump("loc_37FC")

    label("loc_3457")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_35B3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_356C")

    ChrTalk(
        0xFE,
        (
            "Henri, you went to see\x01",
            "Orchis Tower from up\x01",
            "close, right? How was it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Was it big like I think? It\x01",
            "seemed to have cost a lot of\x01",
            "mira? Were there a lot of people?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "W-Wait a moment, Cindy. I\x01",
            "can't answer if you ask\x01",
            "so many things at once.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_35AE")

    label("loc_356C")


    ChrTalk(
        0xFE,
        (
            "What's wrong with that?\x01",
            "Don't be a cheapskate\x01",
            "and tell me...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35AE")

    Jump("loc_37FC")

    label("loc_35B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3647")

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
            "Ah, to go even though\x01",
            "it's so crowded.\x01",
            "Children are powerful.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37FC")

    label("loc_3647")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_36B3")

    ChrTalk(
        0xFE,
        (
            "Ferric, you're going to\x01",
            "a party again tonight?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You never get tired of\x01",
            "them, do you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37FC")

    label("loc_36B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_36C1")
    Jump("loc_37FC")

    label("loc_36C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_37FC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_376D")

    ChrTalk(
        0xFE,
        (
            "Yeah, this is a great\x01",
            "flavor☆\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My cooking just keeps\x01",
            "getting better and\x01",
            "better~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha. It's probably\x01",
            "because of Sophia's\x01",
            "lessons.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_37FC")

    label("loc_376D")


    ChrTalk(
        0xFE,
        (
            "Our neighbor Sophia has\x01",
            "been giving me cooking\x01",
            "lessons every now and then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha. Thanks to them, my\x01",
            "cooking has gotten a lot\x01",
            "better.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37FC")

    TalkEnd(0xFE)
    Return()

    # Function_14_2AD8 end

    def Function_15_3800(): pass

    label("Function_15_3800")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_38BC")

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
    Jump("loc_3A3F")

    label("loc_38BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_38CA")
    Jump("loc_3A3F")

    label("loc_38CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_39A2")

    ChrTalk(
        0xFE,
        (
            "We don't know when an\x01",
            "attack like the other\x01",
            "day will come again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And in this situation,\x01",
            "it wouldn't be strange\x01",
            "if something did happen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As the breadwinner, I've\x01",
            "got to protect my\x01",
            "family.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A3F")

    label("loc_39A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39B4")
    Call(0, 11)
    Jump("loc_3A3F")

    label("loc_39B4")


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
            "She seems to be busy there,\x01",
            "so it won't be anytime soon\x01",
            "when she'll come home...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A3F")

    TalkEnd(0xFE)
    Return()

    # Function_15_3800 end

    def Function_16_3A43(): pass

    label("Function_16_3A43")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3AD6")

    ChrTalk(
        0xFE,
        (
            "It seems my mother-in-law\x01",
            "took care of our children\x01",
            "when we were gone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha, I'm really no\x01",
            "match for my mother-in-\x01",
            "law.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C52")

    label("loc_3AD6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_3AE4")
    Jump("loc_3C52")

    label("loc_3AE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3B83")

    ChrTalk(
        0xFE,
        (
            "Since the address, my wife\x01",
            "and I got special permission\x01",
            "to come check on our home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha. I'm thankful I can\x01",
            "rely on my mother-in-\x01",
            "law.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C52")

    label("loc_3B83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3C52")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B9E")
    Call(0, 9)
    Jump("loc_3C52")

    label("loc_3B9E")


    ChrTalk(
        0xFE,
        (
            "Haha. I'm relieved to learn my\x01",
            "children and my mother-in-law as\x01",
            "well weren't hurt in the attack.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Now then... I've got to\x01",
            "hurry and go help the IBC\x01",
            "operations department.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C52")

    TalkEnd(0xFE)
    Return()

    # Function_16_3A43 end

    def Function_17_3C56(): pass

    label("Function_17_3C56")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3C67")
    Jump("loc_3F62")

    label("loc_3C67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_3D0F")

    ChrTalk(
        0xFE,
        (
            "The government's food allowance\x01",
            "hasn't come in ever since\x01",
            "martial law was declared.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It'll be tough if this\x01",
            "situation goes on too\x01",
            "much longer...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F62")

    label("loc_3D0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3D1D")
    Jump("loc_3F62")

    label("loc_3D1D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_3E42")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DC7")

    ChrTalk(
        0xFE,
        "*crunch, munch*...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, everyone from the\x01",
            "Support Section. Do you\x01",
            "need something from me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Would you like to have\x01",
            "dinner with me?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3E3D")

    label("loc_3DC7")


    ChrTalk(
        0xFE,
        (
            "By the way, the noon's\x01",
            "unveiling was amazing,\x01",
            "eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Policemen are probably\x01",
            "busy, but please do your\x01",
            "best, eh?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E3D")

    Jump("loc_3F62")

    label("loc_3E42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3F62")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3EE6")

    ChrTalk(
        0xFE,
        (
            "I got a lot of homework\x01",
            "from Sunday School\x01",
            "yesterday.\x02",
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
    Jump("loc_3F62")

    label("loc_3EE6")


    ChrTalk(
        0xFE,
        (
            "What's important is\x01",
            "self-study. My grandma\x01",
            "says that too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll study hard, in\x01",
            "order to beat KeA on our\x01",
            "next test.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F62")

    TalkEnd(0xFE)
    Return()

    # Function_17_3C56 end

    SaveToFile()

Try(main)
