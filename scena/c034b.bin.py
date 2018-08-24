from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "Mrs. Izuri",             # 1
        "Ferric",                 # 2
        "Cindy",                  # 3
        "Henri",                  # 4
        "Yunks",                  # 5
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
        "Function_6_3D3",          # 06, 6
        "Function_7_4E3",          # 07, 7
        "Function_8_62A",          # 08, 8
        "Function_9_77F",          # 09, 9
        "Function_10_89B",         # 0A, 10
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
    Jump("loc_3CF")

    label("loc_354")


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

    label("loc_3CF")

    TalkEnd(0xFE)
    Return()

    # Function_5_33F end

    def Function_6_3D3(): pass

    label("Function_6_3D3")


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

    # Function_6_3D3 end

    def Function_7_4E3(): pass

    label("Function_7_4E3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B7")

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
    Jump("loc_626")

    label("loc_5B7")


    ChrTalk(
        0xFE,
        (
            "Oh, now that I think about it, we\x01",
            "don't have enough chairs. I have to\x01",
            "go get one from the storage room...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_626")

    TalkEnd(0xFE)
    Return()

    # Function_7_4E3 end

    def Function_8_62A(): pass

    label("Function_8_62A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_739")

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
    Jump("loc_77B")

    label("loc_739")


    ChrTalk(
        0xFE,
        (
            "What's wrong with that?\x01",
            "Don't be a cheapskate\x01",
            "and tell me...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_77B")

    TalkEnd(0xFE)
    Return()

    # Function_8_62A end

    def Function_9_77F(): pass

    label("Function_9_77F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_821")

    ChrTalk(
        0xFE,
        "*munch munch*...\x02",
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
    Jump("loc_897")

    label("loc_821")


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

    label("loc_897")

    TalkEnd(0xFE)
    Return()

    # Function_9_77F end

    def Function_10_89B(): pass

    label("Function_10_89B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8B0")
    Call(0, 6)
    Jump("loc_93B")

    label("loc_8B0")


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

    label("loc_93B")

    TalkEnd(0xFE)
    Return()

    # Function_10_89B end

    SaveToFile()

Try(main)
