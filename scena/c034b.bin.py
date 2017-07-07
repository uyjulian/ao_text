from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c034b.bin",                # FileName
        "c034b",                    # MapName
        "c034b",                    # Location
        0x002D,                     # MapIndex
        "ed7513",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 3, 0, 4],
    )

    BuildStringList((
        "c034b",                  # 0
        "Lady Isis",             # 1
        "Felic",             # 2
        "Cindy",               # 3
        "Henry",                 # 4
        "Yanks",               # 5
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

    DeclNpc(40669,   0,       9600,    360,  261,  0x0, 0,   0,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(32659,   0,       5679,    180,  261,  0x0, 0,   2,   0,   0,   2,   0,   7,   255,  0)
    DeclNpc(4980,    0,       8989,    89,   261,  0x0, 0,   3,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(5329,    0,       3990,    90,   389,  0x0, 0,   4,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(689,     0,       990,     225,  389,  0x0, 0,   5,   0,   0,   0,   0,   10,  255,  0)

    ChipFrameInfo(372, 0)                                        # 0

    ScpFunction((
        "Function_0_174",          # 00, 0
        "Function_1_224",          # 01, 1
        "Function_2_24C",          # 02, 2
        "Function_3_277",          # 03, 3
        "Function_4_33E",          # 04, 4
        "Function_5_33F",          # 05, 5
        "Function_6_3C0",          # 06, 6
        "Function_7_4A3",          # 07, 7
        "Function_8_58A",          # 08, 8
        "Function_9_6B2",          # 09, 9
        "Function_10_7B0",         # 0A, 10
    ))


    def Function_0_174(): pass

    label("Function_0_174")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_1AC"),
        (1, "loc_1B8"),
        (2, "loc_1C4"),
        (3, "loc_1D0"),
        (4, "loc_1DC"),
        (5, "loc_1E8"),
        (6, "loc_1F4"),
        (SWITCH_DEFAULT, "loc_200"),
    )


    label("loc_1AC")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_20C")

    label("loc_1B8")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_20C")

    label("loc_1C4")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_20C")

    label("loc_1D0")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_20C")

    label("loc_1DC")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_20C")

    label("loc_1E8")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_20C")

    label("loc_1F4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_20C")

    label("loc_200")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_20C")

    label("loc_20C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_223")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_20C")

    label("loc_223")

    Return()

    # Function_0_174 end

    def Function_1_224(): pass

    label("Function_1_224")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_24B")
    OP_94(0xFE, 0x14D2, 0xFFFFFCAE, 0xFFFFF6B4, 0x94C, 0x3E8)
    Jump("Function_1_224")

    label("loc_24B")

    Return()

    # Function_1_224 end

    def Function_2_24C(): pass

    label("Function_2_24C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_276")
    OP_94(0xFE, 0x7738, 0x1126, 0x852A, 0x1D38, 0x3E8)
    Sleep(300)
    Jump("Function_2_24C")

    label("loc_276")

    Return()

    # Function_2_24C end

    def Function_3_277(): pass

    label("Function_3_277")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D4")
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0xC, 0x10)

    label("loc_2D4")

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
    BeginChrThread(0x9, 0, 0, 1)
    Return()

    # Function_3_277 end

    def Function_4_33E(): pass

    label("Function_4_33E")

    Return()

    # Function_4_33E end

    def Function_5_33F(): pass

    label("Function_5_33F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_354")
    Call(0, 6)
    Jump("loc_3BC")

    label("loc_354")


    ChrTalk(
        0xFE,
        (
            "Marietta also\x01",
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

    label("loc_3BC")

    TalkEnd(0xFE)
    Return()

    # Function_5_33F end

    def Function_6_3C0(): pass

    label("Function_6_3C0")


    ChrTalk(
        0x8,
        (
            "そういえばYanks、\x01",
            "Marietta is the sight of his return home\x01",
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

    # Function_6_3C0 end

    def Function_7_4A3(): pass

    label("Function_7_4A3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_540")

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
    Jump("loc_586")

    label("loc_540")


    ChrTalk(
        0xFE,
        (
            "Oh yeah, that's right.\x01",
            "Chairs are missing.\x01",
            "I have to get out of the storeroom …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_586")

    TalkEnd(0xFE)
    Return()

    # Function_7_4A3 end

    def Function_8_58A(): pass

    label("Function_8_58A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_67F")

    ChrTalk(
        0xFE,
        (
            "Henry、オルキスタワーを\x01",
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
    Jump("loc_6AE")

    label("loc_67F")


    ChrTalk(
        0xFE,
        (
            "Not good.\x01",
            "Please do not talk, do tell me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6AE")

    TalkEnd(0xFE)
    Return()

    # Function_8_58A end

    def Function_9_6B2(): pass

    label("Function_9_6B2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_737")

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
    Jump("loc_7AC")

    label("loc_737")


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

    label("loc_7AC")

    TalkEnd(0xFE)
    Return()

    # Function_9_6B2 end

    def Function_10_7B0(): pass

    label("Function_10_7B0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7C5")
    Call(0, 6)
    Jump("loc_845")

    label("loc_7C5")


    ChrTalk(
        0xFE,
        (
            "My wife Marietta\x01",
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

    label("loc_845")

    TalkEnd(0xFE)
    Return()

    # Function_10_7B0 end

    SaveToFile()

Try(main)
