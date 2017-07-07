from ScenarioHelper import *

def main():
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
        "Lady Isis",             # 1
        "Felic",             # 2
        "Cindy",               # 3
        "Henry",                 # 4
        "Yanks",               # 5
        "Marietta",             # 6
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
        "Function_9_193B",         # 09, 9
        "Function_10_1A30",        # 0A, 10
        "Function_11_1B2D",        # 0B, 11
        "Function_12_1C10",        # 0C, 12
        "Function_13_1D29",        # 0D, 13
        "Function_14_289B",        # 0E, 14
        "Function_15_34C1",        # 0F, 15
        "Function_16_36E5",        # 10, 16
        "Function_17_38CB",        # 11, 17
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_9C6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_953")

    ChrTalk(
        0xFE,
        (
            "After all, at this kind of time\x01",
            "You have to stay with your family.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, my son and couple\x01",
            "I am glad that it was safe.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_9C1")

    label("loc_953")


    ChrTalk(
        0xFE,
        (
            "It is the main pillar of the family\x01",
            "息子夫婦がI am glad that it was safe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After all, at this kind of time\x01",
            "You have to stay with your family.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9C1")

    Jump("loc_1937")

    label("loc_9C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_B77")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AC6")

    ChrTalk(
        0xFE,
        (
            "What is important is that at any time\x01",
            "It is to be dignified.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As long as it is dignified,\x01",
            "Fears and uneasiness which tend to be transmitted to others are also\x01",
            "It will probably blow away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Children, son and couple things are\x01",
            "I wonder why … ….\x01",
            "I have to be firm.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_B72")

    label("loc_AC6")


    ChrTalk(
        0xFE,
        (
            "As long as it is dignified,\x01",
            "Fears and uneasiness which tend to be transmitted to others are also\x01",
            "It will probably blow away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Children, son and couple things are\x01",
            "I wonder why … ….\x01",
            "I have to be firm.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B72")

    Jump("loc_1937")

    label("loc_B77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_CD0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C48")

    ChrTalk(
        0xFE,
        (
            "Before this, crossbell\x01",
            "It will be a serious thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But, as our family all together\x01",
            "it must be no problem……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No matter what happens\x01",
            "Everyone together,\x01",
            "I have to get through it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_CCB")

    label("loc_C48")


    ChrTalk(
        0xFE,
        (
            "Before this, crossbell\x01",
            "It will be a serious thing … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No matter what happens\x01",
            "Everyone together,\x01",
            "I have to get through it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CCB")

    Jump("loc_1937")

    label("loc_CD0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_D83")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CEB")
    Call(0, 9)
    Jump("loc_D7E")

    label("loc_CEB")


    ChrTalk(
        0xFE,
        (
            "息子もMariettaさんも、\x01",
            "Because I was working on the destroyed IBC\x01",
            "You're pretty busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Do not break your body\x01",
            "I want you to be careful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D7E")

    Jump("loc_1937")

    label("loc_D83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_EE1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E57")

    ChrTalk(
        0xFE,
        (
            "It's an armed group\x01",
            "Where did you boil it out?\x01",
            "I do not know but ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can not involve innocent people\x01",
            "I can not forgive you very much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To the guard, as soon as possible\x01",
            "People in Mainz\x01",
            "I want you to rescue me.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_EDC")

    label("loc_E57")


    ChrTalk(
        0xFE,
        (
            "I can not involve innocent people\x01",
            "I can not forgive you very much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To the guard, as soon as possible\x01",
            "武装集団からPeople in Mainz\x01",
            "I want you to rescue me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EDC")

    Jump("loc_1937")

    label("loc_EE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_100C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F97")

    ChrTalk(
        0xFE,
        (
            "今日はHenryも\x01",
            "You seem to be out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "At home about a rainy day,\x01",
            "I will not tell you ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Do not catch a cold as it gets wet\x01",
            "I want you to be careful.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1007")

    label("loc_F97")


    ChrTalk(
        0xFE,
        (
            "At home about a rainy day,\x01",
            "I will not tell you ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Do not catch a cold as it gets wet\x01",
            "I want you to be careful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1007")

    Jump("loc_1937")

    label("loc_100C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_108B")

    ChrTalk(
        0xFE,
        (
            "さっきまでCindyに\x01",
            "Tips on a little dish\x01",
            "I was taught.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Fuu …\x01",
            "The tea after the work is extraordinary.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1937")

    label("loc_108B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_10F2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10A6")
    Call(0, 10)
    Jump("loc_10ED")

    label("loc_10A6")


    ChrTalk(
        0xFE,
        (
            "Wait for the rest to burn up later.\x01",
            "Do it yourself.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10ED")

    Jump("loc_1937")

    label("loc_10F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_127C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11EC")

    ChrTalk(
        0xFE,
        (
            "Crossbell is national independent …\x01",
            "If it is realized it will be incredible\x01",
            "I think, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Of course, the Empire and the Republic\x01",
            "I will put pressure on it\x01",
            "It will be quite difficult.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To Mayor Dieter,\x01",
            "I wonder if it is also a good measure ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1277")

    label("loc_11EC")


    ChrTalk(
        0xFE,
        (
            "Crossbell is national independent …\x01",
            "If it is realized it will be incredible\x01",
            "I think, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To Mayor Dieter,\x01",
            "I wonder if it is also a good measure ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1277")

    Jump("loc_1937")

    label("loc_127C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_13C0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_134E")

    ChrTalk(
        0xFE,
        (
            "Cindyは今日はおとなりに\x01",
            "It seems like I'm going out for fun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To Hayworth's wife\x01",
            "Well, at cooking classes etc.\x01",
            "It seems that you are indebted to … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I have to thank you next time.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_13BB")

    label("loc_134E")


    ChrTalk(
        0xFE,
        (
            "To Hayworth's wife\x01",
            "Cindyがよくお世話になっています。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I have to thank you next time.\x02",
    )

    CloseMessageWindow()

    label("loc_13BB")

    Jump("loc_1937")

    label("loc_13C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_1448")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13DB")
    Call(0, 11)
    Jump("loc_1443")

    label("loc_13DB")


    ChrTalk(
        0xFE,
        (
            "Mariettaさんも\x01",
            "It seems to be busy ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To eat with the whole family\x01",
            "It is going to be a while ago.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1443")

    Jump("loc_1937")

    label("loc_1448")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1601")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1571")

    ChrTalk(
        0xFE,
        (
            "The state of the unveiling ceremony is\x01",
            "I could see it from this residential area, though ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Such a high building etc. is built,\x01",
            "It was not thought in the past.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The inside facilities are also the old town hall\x01",
            "It is not comparable\x01",
            "I say that it is in order … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Indeed, that unveiling ceremony\x01",
            "Change of history\x01",
            "It seemed to be expressing.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_15FC")

    label("loc_1571")


    ChrTalk(
        0xFE,
        (
            "Orchis Tower……\x01",
            "Such a high building etc. is built,\x01",
            "It was not thought in the past.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Technological progress,\x01",
            "It is really amazing.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15FC")

    Jump("loc_1937")

    label("loc_1601")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1750")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16C9")

    ChrTalk(
        0xFE,
        (
            "During this time I moved,\x01",
            "Children from the Republic ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Apparently annoying people\x01",
            "There are fish that are enjoying it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It is deplorable … …\x01",
            "I wonder what kind of education it was.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_174B")

    label("loc_16C9")


    ChrTalk(
        0xFE,
        (
            "How children grow\x01",
            "It depends on one parenting method.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Child does not go wrong way\x01",
            "I think that it is also the duty of parents to guide them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_174B")

    Jump("loc_1937")

    label("loc_1750")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_17F7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_176B")
    Call(0, 12)
    Jump("loc_17F2")

    label("loc_176B")


    ChrTalk(
        0xFE,
        (
            "Felicは言葉が荒いし\x01",
            "Although it can not be said that it is polite,\x01",
            "It is a kind and gentle child.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hehuu, you grew up as a good boy\x01",
            "I'm glad.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17F2")

    Jump("loc_1937")

    label("loc_17F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1937")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18A5")

    ChrTalk(
        0xFE,
        (
            "Henryは最近、遊ぶだけでなく\x01",
            "A considerable motivation for study\x01",
            "It began to show off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Huhu, even a good competitor at Sunday school\x01",
            "I wonder if I could do it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1937")

    label("loc_18A5")


    ChrTalk(
        0xFE,
        (
            "Play well, learn well …\x01",
            "That's the way a child should be\x01",
            "I think.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Henryには、\x01",
            "To play and study hard\x01",
            "I want you to work on it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1937")

    TalkEnd(0xFE)
    Return()

    # Function_8_8CF end

    def Function_9_193B(): pass

    label("Function_9_193B")

    OP_4B(0x8, 0xFF)
    OP_4B(0xD, 0xFF)

    ChrTalk(
        0x8,
        "Mariettaさん、よく戻ってきたわね。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Yes, the IBC head office\x01",
            "Because it became such a thing … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Today I went to the Orkis Tower like this\x01",
            "I am going to help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Yes … … It seems to be busy\x01",
            "Do not break your body.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0xD, 0x10)
    OP_4C(0x8, 0xFF)
    OP_4C(0xD, 0xFF)
    SetScenarioFlags(0x0, 0)
    Return()

    # Function_9_193B end

    def Function_10_1A30(): pass

    label("Function_10_1A30")

    OP_4B(0x8, 0xFF)
    OP_4B(0xA, 0xFF)

    ChrTalk(
        0xA,
        (
            "Oh, great!\x01",
            "Cookies are also frying pans\x01",
            "It's burning!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Do not stick cloth\x01",
            "As long as you are careful,\x01",
            "The basics are the same.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Tools\x01",
            "I can hear the substitution as much as you want.\x01",
            "You should remember it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Just a big grandson!\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x10)
    OP_4C(0x8, 0xFF)
    OP_4C(0xA, 0xFF)
    SetScenarioFlags(0x0, 0)
    Return()

    # Function_10_1A30 end

    def Function_11_1B2D(): pass

    label("Function_11_1B2D")


    ChrTalk(
        0x8,
        (
            "そういえばYanks、\x01",
            "Mariettaさんは帰国の目処は\x01",
            "I wonder if it is attached?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Well, it may be difficult for a while.\x01",
            "She seems to be pretty busy … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "so……\x01",
            "To eat with the whole family\x01",
            "It is going to be a while ago.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0xC, 0x10)
    SetScenarioFlags(0x0, 0)
    Return()

    # Function_11_1B2D end

    def Function_12_1C10(): pass

    label("Function_12_1C10")

    OP_4B(0x9, 0xFF)

    ChrTalk(
        0x8,
        (
            "…… Aita.\x01",
            "On rainy days my eyes sore.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Ursula hospital\x01",
            "I have to go get some medicine\x01",
            "It will not be ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Grandma, is it okay?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I wonder why I to the hospital\x01",
            "Shall I attend?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x2)

    ChrTalk(
        0x8,
        "ふふ、ありがとうFelic。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "But it's fine, because I can go alone.\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0x9, 0x10)
    OP_4C(0x9, 0xFF)
    SetScenarioFlags(0x0, 0)
    SetScenarioFlags(0x0, 1)
    Return()

    # Function_12_1C10 end

    def Function_13_1D29(): pass

    label("Function_13_1D29")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1D3A")
    Jump("loc_2897")

    label("loc_1D3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1D9E")

    ChrTalk(
        0xFE,
        (
            "Outside you are such a thing\x01",
            "I am lying … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you are a father\x01",
            "Surely it's okay …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2897")

    label("loc_1D9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1E2F")

    ChrTalk(
        0xFE,
        (
            "Somehow the crossbell is\x01",
            "It is becoming strange.\x01",
            "Looks like it …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, there is a grandmother in my house ……\x01",
            "No matter what happens, I'm fine.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2897")

    label("loc_1E2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1E8D")

    ChrTalk(
        0xFE,
        (
            "Mother, this time\x01",
            "It's been since the memorial festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hey, looks fine\x01",
            "Anything else.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2897")

    label("loc_1E8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1F03")

    ChrTalk(
        0xFE,
        (
            "An outrageous incident\x01",
            "I wish it had happened …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, for a party\x01",
            "It is not a case where you are participating.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2897")

    label("loc_1F03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1F87")

    ChrTalk(
        0xFE,
        (
            "Moisture is a natural enemy of a suit.\x01",
            "I especially care about rainy days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's a suit to wear to a party,\x01",
            "I should take care of it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2897")

    label("loc_1F87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2103")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_207E")

    ChrTalk(
        0xFE,
        (
            "Cindyが作ったクッキーを\x01",
            "If you pinch it, you are bad manners\x01",
            "My grandmother is scolded.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, to the society at the latest\x01",
            "Even though I'm in and out, it is bad manners\x01",
            "It is slightly fatal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "From now on you should be careful.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_20FE")

    label("loc_207E")


    ChrTalk(
        0xFE,
        (
            "Cindyが作ったクッキーを\x01",
            "If you pinch it, you are bad manners\x01",
            "My grandmother is scolded.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "From now on you should be careful.\x02",
    )

    CloseMessageWindow()

    label("loc_20FE")

    Jump("loc_2897")

    label("loc_2103")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2187")

    ChrTalk(
        0xFE,
        (
            "Oh, somehow from below\x01",
            "It smells sweet and has a smell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder if you are making sweets too.\x01",
            "I gotta catch a tip.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2897")

    label("loc_2187")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_22DC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2261")

    ChrTalk(
        0xFE,
        (
            "Even at the party of the business people who last night,\x01",
            "Independent topics were on the verge of flight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But I, I do not know well\x01",
            "I can not keep up with the story.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Asking Mr. grandma,\x01",
            "I wonder if I will study something.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_22D7")

    label("loc_2261")


    ChrTalk(
        0xFE,
        (
            "I can not keep up with the topic of the current time,\x01",
            "It is left out in society.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Independence is\x01",
            "A girl can let me tell you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22D7")

    Jump("loc_2897")

    label("loc_22DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2367")

    ChrTalk(
        0xFE,
        (
            "ちぇっ、Cindyのやつに\x01",
            "I was forced to do housework.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, is there a way?\x01",
            "I occasionally do it properly\x01",
            "I have to stop doing housework.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2897")

    label("loc_2367")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_2455")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_240A")

    ChrTalk(
        0xFE,
        (
            "A busy father at work,\x01",
            "For dinner time after a long absence\x01",
            "I came back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh yeah, that's right.\x01",
            "Chairs are missing.\x01",
            "I have to get out of the storeroom …\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2450")

    label("loc_240A")


    ChrTalk(
        0xFE,
        (
            "Oh yeah, that's right.\x01",
            "Chairs are missing.\x01",
            "I have to get out of the storeroom …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2450")

    Jump("loc_2897")

    label("loc_2455")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_25BB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_252E")

    ChrTalk(
        0xFE,
        (
            "Tonight our heads of countries\x01",
            "It seems to be going to see the alkane shell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Then at the Michelin guesthouse\x01",
            "I hear there is a small dinner.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Sounds good.\x01",
            "I will someday at such a party\x01",
            "I want to participate.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_25B6")

    label("loc_252E")


    ChrTalk(
        0xFE,
        (
            "The leaders of each country,\x01",
            "After seeing the alkane shell\x01",
            "It seems that we will eat at the guest house.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Sounds good.\x01",
            "I will someday at such a party\x01",
            "I want to participate.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25B6")

    Jump("loc_2897")

    label("loc_25BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2646")

    ChrTalk(
        0xFE,
        (
            "フフ、Cindy。\x01",
            "Why did you too?\x01",
            "Join the party and try it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Surely new values\x01",
            "I guarantee to wake up.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2897")

    label("loc_2646")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_26D7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2661")
    Call(0, 12)
    Jump("loc_26D2")

    label("loc_2661")


    ChrTalk(
        0xFE,
        (
            "Hey, my grandmother is\x01",
            "I'm gonna crush it\x01",
            "Even though I'm telling you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, it seems to be a grandmother\x01",
            "I do not mind.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26D2")

    Jump("loc_2897")

    label("loc_26D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2897")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2810")

    ChrTalk(
        0xFE,
        (
            "My father,\x01",
            "He is the boss of IBC's business department.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The society also has a connection,\x01",
            "A party invitation etc. often arrives.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, my father is pretty busy.\x01",
            "Because I'm worried so I will act on behalf of\x01",
            "I am attended.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No, thanks.\x01",
            "I can study a lot about society\x01",
            "Every day is fulfilling.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2897")

    label("loc_2810")


    ChrTalk(
        0xFE,
        (
            "Participating in the party,\x01",
            "I know a lot about society\x01",
            "It is fun ~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This is also thanks to my father's connection.\x01",
            "Well, it is a profitable one.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2897")

    TalkEnd(0xFE)
    Return()

    # Function_13_1D29 end

    def Function_14_289B(): pass

    label("Function_14_289B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2928")

    ChrTalk(
        0xFE,
        (
            "Sophia's family also\x01",
            "From Almorika village\x01",
            "She seems to have returned.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hehe, it was good.\x01",
            "Also tell me your dishes\x01",
            "I gotta get it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34BD")

    label("loc_2928")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2A61")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29F0")

    ChrTalk(
        0xFE,
        (
            "Dad and mother, too,\x01",
            "To the IBC Division of Orkis Tower\x01",
            "I was working … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "While I went to work I got up like this,\x01",
            "I have not come back yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "What shall I do, okay?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2A5C")

    label("loc_29F0")


    ChrTalk(
        0xFE,
        (
            "Dad and mother,\x01",
            "As I go to work at the Orkis Tower\x01",
            "I have not come back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "What shall I do, okay?\x02",
    )

    CloseMessageWindow()

    label("loc_2A5C")

    Jump("loc_34BD")

    label("loc_2A61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2BF9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B5E")

    ChrTalk(
        0xFE,
        (
            "I work for IBC Division\x01",
            "Dad and mother, too,\x01",
            "It seems pretty busy right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because I got a story about asset freezing\x01",
            "It affects various directions\x01",
            "I mean I'm out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because it's such a time\x01",
            "Everyone wanted to be together ….\x01",
            "It can not be helped.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2BF4")

    label("loc_2B5E")


    ChrTalk(
        0xFE,
        (
            "I work for IBC Division\x01",
            "Dad and mother, too,\x01",
            "It seems pretty busy right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because it's such a time\x01",
            "Everyone wanted to be together ….\x01",
            "It can not be helped.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BF4")

    Jump("loc_34BD")

    label("loc_2BF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2C8B")

    ChrTalk(
        0xFE,
        (
            "My mother came back from abroad.\x01",
            "…… I feel relieved somewhat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There was such an incident,\x01",
            "I am worried that my family is separated.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34BD")

    label("loc_2C8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2D18")

    ChrTalk(
        0xFE,
        (
            "Listen to the news of the incident\x01",
            "I was surprised.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The guard's armored car also\x01",
            "It seems that many units are passing ……\x01",
            "Uh, I'm scared of all that.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34BD")

    label("loc_2D18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2E55")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DD0")

    ChrTalk(
        0xFE,
        (
            "I do not have a cooking class today ……\x01",
            "Should I take it slow at home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's right, I guess I made it yesterday.\x01",
            "Studying cookie arrangements\x01",
            "It might be fun.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2E50")

    label("loc_2DD0")


    ChrTalk(
        0xFE,
        (
            "To the fabric of cookie\x01",
            "Chocolate chips\x01",
            "Let's mix it ~ ~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Huhu, Once completed\x01",
            "Even my grandmother called me\x01",
            "Elegant tea time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E50")

    Jump("loc_34BD")

    label("loc_2E55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2FA8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F28")

    ChrTalk(
        0xFE,
        (
            "To Mr. Sofia\x01",
            "On my way to delivering cookies,\x01",
            "I heard an ambulance siren.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you go hurriedly to see it,\x01",
            "A pretty good number goes through … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh dear, even in a big accident\x01",
            "I wonder if there was.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2FA3")

    label("loc_2F28")


    ChrTalk(
        0xFE,
        (
            "… Well someday.\x01",
            "Surely not to think deeply.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, Mr. Colin\x01",
            "Cookies I made\x01",
            "It was nice to be pleased.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FA3")

    Jump("loc_34BD")

    label("loc_2FA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3055")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FC3")
    Call(0, 10)
    Jump("loc_3050")

    label("loc_2FC3")


    ChrTalk(
        0xFE,
        (
            "You are old lady right.\x01",
            "Even without using an oven\x01",
            "I do not have cookies.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Huhu, later to Ms. Sofia\x01",
            "I gotta have a look at the work.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3050")

    Jump("loc_34BD")

    label("loc_3055")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_316F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30EC")

    ChrTalk(
        0xFE,
        "Oh, the oven is broken … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To Mr. Sofia with a great deal\x01",
            "Although I learned how to cook cookies,\x01",
            "I can not burn this …\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_316A")

    label("loc_30EC")


    ChrTalk(
        0xFE,
        (
            "はあ、To Mr. Sofia with a great deal\x01",
            "You taught me how to cook cookies.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The oven is broken,\x01",
            "For the time being, I can not practice it … …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_316A")

    Jump("loc_34BD")

    label("loc_316F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_317D")
    Jump("loc_34BD")

    label("loc_317D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_32AC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3278")

    ChrTalk(
        0xFE,
        (
            "Henry、Orchise Tower\x01",
            "You saw it near, did not you?\x01",
            "How was it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After all it was big?\x01",
            "Was it that Mira was hitting you?\x01",
            "There were lots of people?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Wait a minute, older sister.\x01",
            "Even if you ask so much at once\x01",
            "I could not answer ~.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_32A7")

    label("loc_3278")


    ChrTalk(
        0xFE,
        (
            "Not good.\x01",
            "Please do not talk, do tell me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32A7")

    Jump("loc_34BD")

    label("loc_32AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3340")

    ChrTalk(
        0xFE,
        (
            "Henryは友達と一緒に\x01",
            "Orchise Tower\x01",
            "I guess I went to see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, bother.\x01",
            "To go when it is crowded,\x01",
            "Children are powerful ~ are not they?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34BD")

    label("loc_3340")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3395")

    ChrTalk(
        0xFE,
        (
            "brother,\x01",
            "Is it party tonight?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I do not get tired of it anymore.\x02",
    )

    CloseMessageWindow()
    Jump("loc_34BD")

    label("loc_3395")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_33A3")
    Jump("loc_34BD")

    label("loc_33A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_34BD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3440")

    ChrTalk(
        0xFE,
        "Yeah, a good seasoning ☆\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For me, food is steadily expanding\x01",
            "I am getting better.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hehu, this is also Ms. Sofia's\x01",
            "Thanks for the teaching.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_34BD")

    label("loc_3440")


    ChrTalk(
        0xFE,
        (
            "I, next door Sophia\x01",
            "It's open on a regular basis\x01",
            "I go to the cooking classroom.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hehe, thanks to you.\x01",
            "My cooking skill has improved a lot.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34BD")

    TalkEnd(0xFE)
    Return()

    # Function_14_289B end

    def Function_15_34C1(): pass

    label("Function_15_34C1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_356A")

    ChrTalk(
        0xFE,
        (
            "We are with our staff\x01",
            "At the Orkis Tower\x01",
            "It was confined.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For children and bags\x01",
            "I was worried,\x01",
            "I am glad I managed to come back somehow.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36E1")

    label("loc_356A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_3578")
    Jump("loc_36E1")

    label("loc_3578")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_364F")

    ChrTalk(
        0xFE,
        (
            "The thing like an attack incident during this time\x01",
            "I do not even know when I will get up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No, rather than what happens\x01",
            "It may be a strange situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As I am also the main pillar of the family,\x01",
            "I have to protect my family securely.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36E1")

    label("loc_364F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3661")
    Call(0, 11)
    Jump("loc_36E1")

    label("loc_3661")


    ChrTalk(
        0xFE,
        (
            "妻のMariettaは\x01",
            "I am working at a foreign IBC branch office.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems to be busy and busy,\x01",
            "It is still ahead to come back … …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36E1")

    TalkEnd(0xFE)
    Return()

    # Function_15_34C1 end

    def Function_16_36E5(): pass

    label("Function_16_36E5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3775")

    ChrTalk(
        0xFE,
        (
            "While we are away,\x01",
            "Your mother-in-law has children\x01",
            "It seems I was encouraging.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Huhu, to your mother-in-law\x01",
            "It really does not go up.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38C7")

    label("loc_3775")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_3783")
    Jump("loc_38C7")

    label("loc_3783")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3820")

    ChrTalk(
        0xFE,
        (
            "I had such a speech,\x01",
            "With my husband and two people special permission,\x01",
            "I came to see the state of the house.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Huhu, you're a reliable mother-in-law\x01",
            "I will really be saved.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38C7")

    label("loc_3820")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_38C7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_383B")
    Call(0, 9)
    Jump("loc_38C7")

    label("loc_383B")


    ChrTalk(
        0xFE,
        (
            "Huhu, both my sons and my mother-\x01",
            "I was not hurt by an attack\x01",
            "It was really good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well … Finally\x01",
            "To help IBC Division\x01",
            "I have to go.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38C7")

    TalkEnd(0xFE)
    Return()

    # Function_16_36E5 end

    def Function_17_38CB(): pass

    label("Function_17_38CB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_38DC")
    Jump("loc_3B7F")

    label("loc_38DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_394D")

    ChrTalk(
        0xFE,
        (
            "Government-\x01",
            "I have not come from martial law.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "If this situation continues, it is tough, is not it?\x02",
    )

    CloseMessageWindow()
    Jump("loc_3B7F")

    label("loc_394D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_395B")
    Jump("loc_3B7F")

    label("loc_395B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_3A60")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39E6")

    ChrTalk(
        0xFE,
        "Munching …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, everyone in the support department.\x01",
            "Is it for something in my house?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Together with you\x01",
            "Are you going to have dinner?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3A5B")

    label("loc_39E6")


    ChrTalk(
        0xFE,
        (
            "Anyway, the unveiling ceremony at noon\x01",
            "It was amazing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The police guys\x01",
            "It will be busy,\x01",
            "Please do your best.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A5B")

    Jump("loc_3B7F")

    label("loc_3A60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3B7F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3AFC")

    ChrTalk(
        0xFE,
        (
            "Yesterday at Sunday School\x01",
            "I got a lot of homework.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Recently, in terms of testing\x01",
            "I am losing to Ka'aa,\x01",
            "I have to do self-study neatly.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3B7F")

    label("loc_3AFC")


    ChrTalk(
        0xFE,
        (
            "\"What is important is self-study\"\x01",
            "My grandma also said that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Next is a test\x01",
            "To beat Ka'aa,\x01",
            "I have to study firmly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B7F")

    TalkEnd(0xFE)
    Return()

    # Function_17_38CB end

    SaveToFile()

Try(main)
