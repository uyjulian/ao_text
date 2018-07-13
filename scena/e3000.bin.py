from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "e3000.bin",                # FileName
        "e3000",                    # MapName
        "e3000",                    # Location
        0x00A1,                     # MapIndex
        "ed7565",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0xFF,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 161, 0, 1, 0, 2],
    )

    BuildStringList((
        "e3000",                  # 0
        "Tio",                    # 1
        "Zeit",                   # 2
        "Wazy",                   # 3
        "KeA",                    # 4
        "Tourist",                # 5
        "Tourist",                # 6
        "Mariabell",              # 7
    ))

    AddCharChip((
        "chr/ch00200.itc",                   # 00
        "chr/ch02707.itc",                   # 01
        "chr/ch03002.itc",                   # 02
        "chr/ch08200.itc",                   # 03
        "chr/ch24502.itc",                   # 04
        "chr/ch21302.itc",                   # 05
        "chr/ch00000.itc",                   # 06
        "chr/ch00000.itc",                   # 07
        "chr/ch00000.itc",                   # 08
        "chr/ch00000.itc",                   # 09
        "chr/ch00000.itc",                   # 0A
        "chr/ch00000.itc",                   # 0B
        "chr/ch00000.itc",                   # 0C
        "chr/ch00000.itc",                   # 0D
        "chr/ch00000.itc",                   # 0E
        "chr/ch00000.itc",                   # 0F
        "chr/ch00000.itc",                   # 10
        "chr/ch00000.itc",                   # 11
        "chr/ch00000.itc",                   # 12
        "chr/ch00000.itc",                   # 13
        "chr/ch00000.itc",                   # 14
        "chr/ch00000.itc",                   # 15
        "chr/ch00000.itc",                   # 16
        "chr/ch00000.itc",                   # 17
        "chr/ch00000.itc",                   # 18
        "chr/ch00000.itc",                   # 19
        "chr/ch00000.itc",                   # 1A
        "chr/ch00000.itc",                   # 1B
        "chr/ch00000.itc",                   # 1C
        "chr/ch00000.itc",                   # 1D
    ))

    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   0,   0,   0,   3,   255,  0)
    DeclNpc(0,       0,       0,       0,    404,  0x0, 0,   1,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(0,       0,       0,       0,    388,  0x0, 0,   2,   0,   255, 255, 0,   6,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   3,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(2210,    4250,    899,     180,  453,  0x0, 0,   4,   0,   255, 255, 0,   7,   255,  0)
    DeclNpc(1029,    4250,    899,     180,  453,  0x0, 0,   5,   0,   255, 255, 0,   8,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(580, 0)                                        # 0

    ScpFunction((
        "Function_0_244",          # 00, 0
        "Function_1_2F4",          # 01, 1
        "Function_2_408",          # 02, 2
        "Function_3_475",          # 03, 3
        "Function_4_B44",          # 04, 4
        "Function_5_DFE",          # 05, 5
        "Function_6_E1C",          # 06, 6
        "Function_7_114C",         # 07, 7
        "Function_8_12A9",         # 08, 8
        "Function_9_1322",         # 09, 9
        "Function_10_2A4C",        # 0A, 10
        "Function_11_2A6C",        # 0B, 11
        "Function_12_2A8C",        # 0C, 12
        "Function_13_3351",        # 0D, 13
        "Function_14_34ED",        # 0E, 14
        "Function_15_41E1",        # 0F, 15
        "Function_16_41F8",        # 10, 16
        "Function_17_427C",        # 11, 17
        "Function_18_42A2",        # 12, 18
        "Function_19_42B9",        # 13, 19
        "Function_20_42DF",        # 14, 20
        "Function_21_430C",        # 15, 21
        "Function_22_431E",        # 16, 22
        "Function_23_4329",        # 17, 23
        "Function_24_4348",        # 18, 24
        "Function_25_4367",        # 19, 25
        "Function_26_447A",        # 1A, 26
        "Function_27_550E",        # 1B, 27
        "Function_28_5534",        # 1C, 28
    ))


    def Function_0_244(): pass

    label("Function_0_244")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_27C"),
        (1, "loc_288"),
        (2, "loc_294"),
        (3, "loc_2A0"),
        (4, "loc_2AC"),
        (5, "loc_2B8"),
        (6, "loc_2C4"),
        (SWITCH_DEFAULT, "loc_2D0"),
    )


    label("loc_27C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_2DC")

    label("loc_288")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_2DC")

    label("loc_294")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_2DC")

    label("loc_2A0")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_2DC")

    label("loc_2AC")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_2DC")

    label("loc_2B8")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_2DC")

    label("loc_2C4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2DC")

    label("loc_2D0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2DC")

    label("loc_2DC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2F3")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2DC")

    label("loc_2F3")

    Return()

    # Function_0_244 end

    def Function_1_2F4(): pass

    label("Function_1_2F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_38A")
    SetChrPos(0x8, -500, 4100, 11000, 90)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x9, 1000, 4100, 11000, 180)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0xA, -2250, 4250, -2100, 180)
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xA, 0x2)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    ClearChrFlags(0xC, 0x80)
    SetChrChipByIndex(0xC, 0x4)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    ClearChrFlags(0xD, 0x80)
    SetChrChipByIndex(0xD, 0x5)
    SetChrSubChip(0xD, 0x0)
    EndChrThread(0xD, 0x0)
    SetChrBattleFlags(0xD, 0x4)
    SetChrFlags(0xD, 0x10)
    SetChrSubChip(0xD, 0x1)

    label("loc_38A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3AE")
    SetChrPos(0xB, 3000, 4100, -8000, 180)
    ClearChrFlags(0xB, 0x80)

    label("loc_3AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_3C8")
    ClearScenarioFlags(0x22, 0)
    SetScenarioFlags(0x0, 0)
    SetScenarioFlags(0x0, 1)
    Event(0, 9)
    Jump("loc_3EE")

    label("loc_3C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_3DF")
    ClearScenarioFlags(0x22, 1)
    SetScenarioFlags(0x0, 1)
    Event(0, 25)
    Jump("loc_3EE")

    label("loc_3DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_3EE")
    ClearScenarioFlags(0x22, 2)
    Event(0, 26)

    label("loc_3EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_407")
    Event(0, 13)

    label("loc_407")

    Return()

    # Function_1_2F4 end

    def Function_2_408(): pass

    label("Function_2_408")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_422")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 0)
    Jump("loc_43A")

    label("loc_422")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 0)), scpexpr(EXPR_END)), "loc_43A")
    SetScenarioFlags(0x0, 1)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x25, 0)

    label("loc_43A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_44E")
    OP_24(0x1DF)
    ClearScenarioFlags(0x0, 1)
    Jump("loc_454")

    label("loc_44E")

    Sound(479, 1, 100, 0)

    label("loc_454")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_474")
    OP_63(0xB, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_474")

    Return()

    # Function_2_408 end

    def Function_3_475(): pass

    label("Function_3_475")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_486")
    Jump("loc_B40")

    label("loc_486")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_494")
    Jump("loc_B40")

    label("loc_494")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_4A4")
    Jump("loc_B40")

    label("loc_4A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_4B2")
    Jump("loc_B40")

    label("loc_4B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_4C0")
    Jump("loc_B40")

    label("loc_4C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_4CE")
    Jump("loc_B40")

    label("loc_4CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_4DC")
    Jump("loc_B40")

    label("loc_4DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_4EA")
    Jump("loc_B40")

    label("loc_4EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_B40")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15A, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A94")

    ChrTalk(
        0x8,
        (
            "#00204F*cough*, anyway...\x01",
            "Today we should enjoy a\x01",
            "day off after a long time.\x02\x03",
            "#00200FBefore we were investigating the\x01",
            ""auction" and didn't have barely\x01",
            "any time to have fun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FIndeed, this is the first\x01",
            "time I came to properly\x01",
            "have fun at Michelam.\x02\x03",
            "#00009FHa ha, as I suspect,\x01",
            "your goal is the\x01",
            "theme park, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#00204FOf course it is.\x02\x03",
            ""Michelam Wonderland"...\x01",
            "...M.W.L. for short.\x02\x03",
            "I can't wait.\x02\x03",
            "#00202FI am looking forward to see Michey.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 4)), scpexpr(EXPR_END)), "loc_931")
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00004F...By the way, uhhm...\x01",
            "Do you remember that "promise"?\x02\x03",
            "#00002FWe talked about finding the right\x01",
            "time after the Cult incident was over\x01",
            "to come have fun at the theme park.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#00204F...Naturally, I remember.\x02\x03",
            ""First with everyone in the Support\x01",
            "Section and then Mr. Lloyd and I."\x02\x03",
            "#00200FIn a certain sense, due to this\x01",
            "invitation it can be said we\x01",
            "finally moved to phase 1.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHa ha, I don't understand well\x01",
            "the meaning of that phrase, but...\x02\x03",
            "#00000FThe next time we'll have\x01",
            "to come the two of us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#00209FUh uh...\x01",
            "Yes, I am looking forward to it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A8C")

    label("loc_931")


    ChrTalk(
        0x101,
        (
            "#00004FTio, you're particularly\x01",
            "knowledgeable about Michey.\x02\x03",
            "#00002FTeach me a lot of things when\x01",
            "we're at the theme park, ok?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#00204F...Roger that.\x02\x03",
            "#00202FThen, first I will thoroughly cram the secret\x01",
            "story of Michey's birth, his family structure\x01",
            "and so on into your head, Mr. Lloyd...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006FN-No, you don't have to go that far.\x02",
    )

    CloseMessageWindow()

    label("loc_A8C")

    SetScenarioFlags(0x15A, 0)
    Jump("loc_B40")

    label("loc_A94")


    ChrTalk(
        0x8,
        (
            "#00202FI will teach you many things\x01",
            "about Michey after we arrive\x01",
            "at the theme park, Mr. Lloyd.\x02\x03",
            "#00204FI think you should go to where\x01",
            "the others are and talk to them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B40")

    TalkEnd(0xFE)
    Return()

    # Function_3_475 end

    def Function_4_B44(): pass

    label("Function_4_B44")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_B55")
    Jump("loc_DFA")

    label("loc_B55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_B63")
    Jump("loc_DFA")

    label("loc_B63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_B71")
    Jump("loc_DFA")

    label("loc_B71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_B7F")
    Jump("loc_DFA")

    label("loc_B7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_B8D")
    Jump("loc_DFA")

    label("loc_B8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_B9B")
    Jump("loc_DFA")

    label("loc_B9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_BA9")
    Jump("loc_DFA")

    label("loc_BA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_DFA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DA0")
    OP_4B(0x8, 0xFF)

    ChrTalk(
        0x9,
        "#01203FGrrrowl...woof.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 500)

    ChrTalk(
        0x8,
        (
            "#00204F"Honestly, what a handful of a leader"...\x01",
            "It seems he is saying that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FHa ha, getting told that by Zeit\x01",
            "puts me in an awkward position.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#00211F"He's too much of a dullard" and\x01",
            ""Become a little more thoughtful man!"...\x01",
            "He also seems to be saying that.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x101, 0x8, 500)

    ChrTalk(
        0x101,
        (
            "#00006F...Isn't some subjectivity\x01",
            "included in there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#00203FWell, I wonder what you are talking about.\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0x5A, 0x0)
    SetScenarioFlags(0x0, 4)
    OP_4C(0x8, 0xFF)
    Jump("loc_DFA")

    label("loc_DA0")


    ChrTalk(
        0x9,
        "#01203F...Grrrowl...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F(Could Zeit be looking forward\x01",
            "to Michelam too...?)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DFA")

    TalkEnd(0xFE)
    Return()

    # Function_4_B44 end

    def Function_5_DFE(): pass

    label("Function_5_DFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E15")
    Call(0, 14)
    Return()

    label("loc_E15")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_5_DFE end

    def Function_6_E1C(): pass

    label("Function_6_E1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E33")
    Call(0, 12)
    Return()

    label("loc_E33")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_E44")
    Jump("loc_1148")

    label("loc_E44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_E52")
    Jump("loc_1148")

    label("loc_E52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_E60")
    Jump("loc_1148")

    label("loc_E60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_E6E")
    Jump("loc_1148")

    label("loc_E6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_E7C")
    Jump("loc_1148")

    label("loc_E7C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_E8A")
    Jump("loc_1148")

    label("loc_E8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_E98")
    Jump("loc_1148")

    label("loc_E98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_1148")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EB0")
    Jump("loc_1148")

    label("loc_EB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1085")

    ChrTalk(
        0xA,
        (
            "#10304FIt's been a long time since I came to\x01",
            "Michelam aside from my host job, so\x01",
            "I guess that today I'll relax myself.\x02\x03",
            "#10300FAt some point I intend to go\x01",
            "to the restaurant, so do you\x01",
            "want to join me for drinks too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F...Listen, you can say it how many times you want,\x01",
            "but I can't approve of a minor drinking, you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#10309FHu hu, do not say such formal things.\x01",
            "Cut loose more.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FFormal or not,\x01",
            "that's not the point.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1148")

    label("loc_1085")


    ChrTalk(
        0xA,
        (
            "#10309FDo not say such formal things.\x01",
            "Cut loose more.\x02\x03",
            "#10302FThen I could initiate you to the \x01",
            "hosts' basic techniques to make \x01",
            "girls fall, you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006FD-Don't try to bribe me...\x02",
    )

    CloseMessageWindow()

    label("loc_1148")

    TalkEnd(0xFE)
    Return()

    # Function_6_E1C end

    def Function_7_114C(): pass

    label("Function_7_114C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_12A5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1215")

    ChrTalk(
        0xC,
        (
            "Somehow everyone in the city was\x01",
            "talking about "independence" or something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Because we came from abroad,\x01",
            "we don't really get it, but...\x01",
            "Is it something serious?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_12A5")

    label("loc_1215")


    ChrTalk(
        0xC,
        (
            "I wonder what's this "independence"\x01",
            "the people of the city were talking about.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I don't really get it, but...\x01",
            "Is it something serious?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12A5")

    TalkEnd(0xFE)
    Return()

    # Function_7_114C end

    def Function_8_12A9(): pass

    label("Function_8_12A9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_131E")

    ChrTalk(
        0xD,
        (
            "Hey hey, more importantly, isn't\x01",
            "that one sit in front cute?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Should we pick him up? Should we?\x02",
    )

    CloseMessageWindow()

    label("loc_131E")

    TalkEnd(0xFE)
    Return()

    # Function_8_12A9 end

    def Function_9_1322(): pass

    label("Function_9_1322")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_32(0xFF, 0xFE, 0x0)
    RemoveParty(0x1, 0xFF)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x3, 0xFF)
    RemoveParty(0x8, 0xFF)
    RemoveParty(0x4, 0xFF)
    LoadChrToIndex("apl/ch51300.itc", 0x1E)
    LoadChrToIndex("apl/ch51301.itc", 0x1F)
    SoundLoad(479)
    SoundLoad(2674)
    SoundLoad(2675)
    SoundLoad(2676)
    SoundLoad(4108)
    SoundLoad(3054)
    SoundLoad(3060)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis245.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis091.itp")
    CreatePortrait(2, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu00201.itp")
    CreatePortrait(3, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu01200.itp")
    SetChrPos(0x101, -750, 4100, 12500, 0)
    ClearChrFlags(0x9, 0x80)
    OP_4B(0x9, 0xFF)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 1000, 4100, 11000, 0)
    BeginChrThread(0x9, 3, 0, 0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, -2250, 4250, -2100, 180)
    ClearChrFlags(0x8, 0x80)
    OP_4B(0x8, 0xFF)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 0, 4100, 5000, 0)
    SetChrFlags(0x8, 0x8)
    ClearChrFlags(0xC, 0x80)
    SetChrChipByIndex(0xC, 0x4)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    ClearChrFlags(0xD, 0x80)
    SetChrChipByIndex(0xD, 0x5)
    SetChrSubChip(0xD, 0x0)
    EndChrThread(0xD, 0x0)
    SetChrBattleFlags(0xD, 0x4)
    SetChrFlags(0xD, 0x10)
    SetChrSubChip(0xD, 0x1)
    Sleep(1000)
    OP_C9(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            "#30WTwo weeks after the Trade Conference──\x01",
            "Crossbell City was enveloped in a quiet enthusiasm.\x02\x03",
            "As for the other autonomous states──\x01",
            "Leman, Ord and North Ambria sovereignty\x01",
            "as states was accepted after the Holy\x01",
            "Nation of Arteria acknowledged it.\x02\x03",
            "But to the autonomous state of Crossbell\x01",
            "was only recognized the right to self-govern\x01",
            "from the Empire and Republic as a buffer zone.\x02\x03",
            "(Incidentally, 10% of revenues were paid\x01",
            "to both the Empire and Republic as\x01",
            "nominal "mandate costs".)\x02\x03",
            "The growth as a trade and financial center\x01",
            "and the fragility of the political foundation\x01",
            "inversionally proposed to that──\x02\x03",
            "Brought, as a result, interferences from \x01",
            "abroad and the rise of mafia and so on.\x02\x03",
            "Many citizens sympathized with \x01",
            "Mayor Dieter's drastic proposal of \x01",
            ""Being independent as a sovereign state"\x01",
            "to abolish that crooked situation, however...\x02\x03",
            "Many were concerned about the two major powers \x01",
            "intentions and so arguments about the "independence"\x01",
            "pros and cons occurred here and there.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x800)
    PlayBGM("ed7515", 0)
    OP_68(0, 4100, -15000, 0)
    MoveCamera(340, 6, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(45000, 0)
    OP_68(0, 4100, 45000, 12000)
    Sound(479, 2, 20, 0)
    Sleep(100)
    OP_25(0x1DF, 0x1E)
    Sleep(100)
    OP_25(0x1DF, 0x28)
    Sleep(100)
    OP_25(0x1DF, 0x32)
    Sleep(200)
    FadeToBright(2000, 0)
    Sleep(10500)
    OP_0D()
    Fade(1000)
    OP_68(-750, 5100, 12500, 0)
    MoveCamera(225, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(22000, 0)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x6)
    SetCameraDistance(21000, 2000)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x101,
        "#00008F#5P#30W............\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    Sleep(500)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(800)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00006F#5P#30W......*sigh*......\x02\x03",
            "#00008FIt's no good... It's been almost\x01",
            "half a month since then, and yet...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(3052, 255, 80, 0)

    ChrTalk(
        0x9,
        "#01200F#6P#30WWoof?\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x7)
    Sleep(100)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Sleep(100)
    TurnDirection(0x101, 0x9, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00012F#11P#30WSorry, I let out a sigh.\x02\x03",
            "#00008F...Say, Zeit.\x02\x03",
            "What should a leader\x01",
            "do in such a time?\x02\x03",
            "Randy...and Elie and Noｱl\x01",
            "too seem they're thinking\x01",
            "a lot about things...\x02\x03",
            "#00006F...This seems to be making\x01",
            "KeA worry too.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x3, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x3, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x3, 0x3)
    OP_CC(0x0, 0x3, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    OP_C9(0x0, 0x80000000)

    AnonymousTalk(
        0x9,
        (
            "#3054V#30WWoof.\x02\x03",
            "#3060V#40WGrrrrrowl...woof.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xBF4)
    OP_C9(0x1, 0x80000000)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x3, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x3, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x3, 0x3)
    OP_CC(0x0, 0x3, 0x0)

    ChrTalk(
        0x101,
        (
            "#00005F#11P#30WEhhm...\x01",
            "What're you saying?\x02\x03",
            "#00012FHa ha, sorry.\x01",
            "I'm being eccentric...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearChrFlags(0x8, 0x8)
    OP_C9(0x0, 0x80000000)

    NpcTalk(
        0xA,
        "Young Girl's Voice",
        (
            "#2674V#5P#N#30W#35A"In times like this,\x01",
            "don't think logically."\x02\x03",
            "#2675V#25A"Just speak what you\x01",
            "have on your mind."\x02\x03",
            "#4108V#N#15A──He seems to be saying that.\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x101, 0xB4, 0x1F4)
    OP_68(-350, 5100, 11350, 2500)
    OP_9B(0x0, 0x8, 0x0, 0x1194, 0x7D0, 0x0)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#00005F#12PTio...\x02",
    )

    CloseMessageWindow()
    OP_68(-1350, 5100, 12250, 2500)
    MoveCamera(210, 23, 0, 2500)
    SetCameraDistance(19330, 2500)

    def lambda_1DF3():

        label("loc_1DF3")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_1DF3")

    QueueWorkItem2(0x101, 2, lambda_1DF3)
    OP_96(0x8, 0xFFFFF894, 0x1004, 0x2F76, 0x7D0, 0x0)
    EndChrThread(0x101, 0x2)
    OP_6F(0x79)
    SetCameraDistance(18360, 20000)
    Sound(2676, 255, 80, 0)
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x8,
        (
            "#30W...What a nice breeze.\x02\x03",
            "It's a rare holiday so\x01",
            "I'm glad the weather is nice.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)
    OP_93(0x101, 0x0, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00004F#5PYou're right...\x02\x03",
            "#00000FAlthough I thought what was going on\x01",
            "when we were invited by Miss Mariabell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#00202F#5PUh uh, did you think it was some kind of trap?\x02\x03",
            "Even now it seems she is looking\x01",
            "at you a little as hostile.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012F#5PHa ha, actually, I thought about that a bit.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00006F#5P...I'm sorry, Tio.\x02\x03",
            "#00008FYou've just come back and yet\x01",
            "you see me in this pathetic state.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#00206F#5P...I think it can't be helped.\x02\x03",
            "#00208FYou saw so many persons\x01",
            "dying in front of you...\x02\x03",
            "#00200FIt would be a shock, normally.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#5PNo, after I became a detective,\x01",
            "I was prepared in some respects.\x02\x03",
            "#00001F...After what happened with Joachim too\x01",
            "I thought I somehow got used to it, but...\x02\x03",
            "#00006FIt seems that I was still lacking\x01",
            "preparedness as a detective and as a leader.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#00203F#5P#40W*sigh*...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#00200F#11P──Getting used to it doesn't really\x01",
            "relate to preparedness, right?\x02\x03",
            "If you say that, it would make someone\x01",
            "like me fully prepared.\x02\x03",
            "#00203FAnd probably Mr. Randy is\x01",
            ""used" to people's deaths.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x101, 0x8, 500)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(1000)
    SetCameraDistance(18360, 0)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)

    ChrTalk(
        0x101,
        "#00008F#6P...I see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#00206F#11PHowever, I can't really think\x01",
            "someone is more suited to be a\x01",
            "detective than you, Mr. Lloyd...\x02\x03",
            "Naturally I don't think you have the\x01",
            "preparedness to do the leader.\x02\x03",
            "#00201F──I think that what everyone seeks\x01",
            "in you, Mr. Lloyd, is different.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#6PTio...\x02",
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00006F#6P...You're right.\x01",
            "It could really be like that.\x02\x03",
            "#00008FIt seems I couldn't move, misunderstanding the\x01",
            "shock I received for lack of preparedness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#00204F#11PThen, please move.\x02\x03",
            "#00202FIt is a rare chance for a vacation with everyone...\x02\x03",
            "It is the duty of a leader to be concerned\x01",
            "that everyone enjoys it, isn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002F#6PYeah, you have a point.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetCameraDistance(18060, 1000)
    OP_9B(0x0, 0x101, 0x0, 0x1F4, 0x3E8, 0x0)
    OP_6F(0x79)
    Fade(250)
    BeginChrThread(0x101, 3, 0, 10)
    BeginChrThread(0x8, 3, 0, 11)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x8, 3)
    OP_0D()
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7565", 0)

    ChrTalk(
        0x8,
        "#00205F#11P...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009F#6PThanks, Tio.\x02\x03",
            "#00000FI'll go talk a little\x01",
            "to the others.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#00206F#11PY-Yes.\x01",
            "I think that is a good idea.\x02\x03",
            "#00208F#30W...But...uhm...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00011F#6PAh, sorry, sorry.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    OP_A1(0x101, 0x4E2, 0x2, 0x1, 0x0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x101, 0x2)
    OP_9B(0x1, 0x101, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
    OP_0D()
    Sound(2274, 255, 60, 0)

    ChrTalk(
        0x8,
        "#00205F#11P#40W......Oh......\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#6PHa ha, I didn't want to treat you like a child\x01",
            "but I wanted to express my gratitude...\x02",
        )
    )

    CloseMessageWindow()
    OP_A1(0x8, 0x5DC, 0x3, 0x7, 0x8, 0x9)

    ChrTalk(
        0x8,
        (
            "#00206F#11PNo, don't worry about it.\x02\x03",
            "#00208F#30WUhm...rather...a little more...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#6PEh?\x02",
    )

    CloseMessageWindow()
    OP_A1(0x8, 0x5DC, 0x2, 0xA, 0xB)
    Sleep(150)
    OP_82(0x32, 0x0, 0x7D0, 0xC8)

    ChrTalk(
        0x8,
        "#00201F#11P...It's nothing!\x02",
    )

    CloseMessageWindow()
    OP_A1(0x8, 0x5DC, 0x2, 0xC, 0xD)

    ChrTalk(
        0x8,
        (
            "#00203F#11PPlease go where the\x01",
            "others are, quick.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#6PY-Yeah...?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(150)
    Sound(3053, 255, 60, 0)

    ChrTalk(
        0x9,
        "#01203F#6P#30WGrrrrowl......(oh boy)\x02",
    )

    CloseMessageWindow()
    OP_24(0xBED)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x2)
    OP_49()
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_CC(0x1, 0xFF, 0x0)
    SetChrPos(0x8, -500, 4100, 11000, 90)
    ClearChrFlags(0x8, 0x8000)
    OP_4C(0x8, 0xFF)
    EndChrThread(0x9, 0x3)
    SetChrChipByIndex(0x9, 0x1)
    SetChrSubChip(0x9, 0x0)
    SetChrPos(0x9, 1000, 4100, 11000, 180)
    ClearChrFlags(0x9, 0x8000)
    OP_4C(0x9, 0xFF)
    ClearChrFlags(0xA, 0x8000)
    SetChrPos(0xA, -2250, 4250, -2100, 180)
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xA, 0x2)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    SetChrPos(0x0, 0, 4100, 8000, 180)
    SetScenarioFlags(0x144, 0)
    OP_29(0xA5, 0x4, 0x2)
    OP_29(0xA5, 0x1, 0x0)
    ClearChrFlags(0xA, 0x8)
    OP_25(0x1DF, 0x64)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_9_1322 end

    def Function_10_2A4C(): pass

    label("Function_10_2A4C")

    SetChrFlags(0xFE, 0x2)
    SetChrChipByIndex(0xFE, 0x1E)
    OP_A1(0xFE, 0x3E8, 0x3, 0x0, 0x1, 0x2)
    OP_A1(0xFE, 0x3E8, 0x7, 0x2, 0x3, 0x4, 0x5, 0x4, 0x3, 0x2)
    Return()

    # Function_10_2A4C end

    def Function_11_2A6C(): pass

    label("Function_11_2A6C")

    SetChrFlags(0xFE, 0x2)
    SetChrChipByIndex(0xFE, 0x1F)
    OP_A1(0xFE, 0x3E8, 0x3, 0x0, 0x1, 0x2)
    OP_A1(0xFE, 0x3E8, 0x7, 0x2, 0x3, 0x4, 0x5, 0x4, 0x3, 0x2)
    Return()

    # Function_11_2A6C end

    def Function_12_2A8C(): pass

    label("Function_12_2A8C")

    EventBegin(0x0)
    Fade(500)
    OP_68(-2250, 5100, -2100, 0)
    MoveCamera(320, 20, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16450, 0)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu10301.itp")
    SetChrPos(0x101, -1050, 4100, -2900, 315)
    SetChrSubChip(0xA, 0x1)
    OP_0D()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    Sound(2911, 255, 100, 0)

    AnonymousTalk(
        0xA,
        (
            "#30W──Hi, Lloyd.\x02\x03",
            "It looks like you feel\x01",
            "alive again, eh?\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xB5F)
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
            "#00012F#6PHa ha, more or less.\x02\x03",
            "#00000F...You look \x01",
            "quite fine, Wazy.\x02\x03",
            "Same coolness\x01",
            "as always...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#10304F#5PWell, that's my selling point, after all.\x02\x03",
            "#10308FAlso, it's not that I had no experience\x01",
            "until now about having seen pointless\x01",
            "deaths.\x02\x03",
            "#10303FBefore coming to Crossbell, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008F#6PIs that so...?\x02\x03",
            "#00005F...Wait, it's the first time I heard\x01",
            "something about your past, Wazy.\x02\x03",
            "#00000FI had somehow heard that\x01",
            "you aren't from Crossbell...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#10309F#5PHu hu, I guess that's a trade secret.\x02\x03",
            "#10300FBut...\x01",
            "I also lived in the slums once.\x02\x03",
            "It's a far more hopeless garbage dump\x01",
            "than something like Downtown, you know.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x6F), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2EC5")

    ChrTalk(
        0x101,
        (
            "#00006F#6P...I see...\x02\x03",
            "#00008FSully too of the Arc-en-ciel seems\x01",
            "to be from a frontier slum...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F29")

    label("loc_2EC5")


    ChrTalk(
        0x101,
        (
            "#00006F#6P...I see...\x02\x03",
            "#00008FThe Arc-en-ciel newcomer too seems\x01",
            "to be from a frontier slum...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F29")


    ChrTalk(
        0xA,
        (
            "#10305F#5PAh, the North Ambria girl, eh?\x02\x03",
            "#10306FOver there it's awful...\x01",
            "Somehow they barely make a living with the money\x01",
            "the guys make by working as jaegers outside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#6PYeah, I had heard the rumors...\x02\x03",
            "#00005F...Wait, by the way you speak,\x01",
            "it's like you went there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#10304F#5PHu hu, I wonder.\x02\x03",
            "#10308F#30W............\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F#6P???\x02\x03",
            "#00003FI said you're looking fine, but...\x01",
            "It's like you're a little lackluster...\x02\x03",
            "#00001F...Did something happen?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#10304F#5PTo me personally, nothing.\x02\x03",
            "#10300FHowever, many things\x01",
            "to the Vipers, it seems.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001F#6PThe Vipers...\x01",
            "Wald and the others?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#10304F#5PWell, since I left them in that way,\x01",
            "I'm a little concerned.\x02\x03",
            "#10302FI'm a cool beauty who they say his selling\x01",
            "point is his mysterious charisma.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#6PDon't tell you that yourself...\x02\x03",
            "#00008F...However, I'm a little \x01",
            "concerned about Wald too.\x02\x03",
            "#00000FLet's go see how he's doing\x01",
            "when we have some spare time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#10304F#5PHu hu, if you did me that\x01",
            "favor you'd really help me.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, -1050, 4100, -3100, 180)
    SetChrSubChip(0xA, 0x0)
    SetChrSubChip(0xD, 0x1)
    SetScenarioFlags(0x144, 1)
    OP_CC(0x1, 0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_12_2A8C end

    def Function_13_3351(): pass

    label("Function_13_3351")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x101, 2640, 4100, 4150, 180)
    SetChrPos(0xB, 3000, 4100, -8000, 180)
    ClearChrFlags(0xB, 0x80)
    OP_63(0xB, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    ClearMapObjFlags(0x0, 0x10)
    OP_70(0x0, 0x5)
    OP_68(2700, 5100, 3350, 0)
    MoveCamera(52, 26, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18200, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(17700, 2000)
    Sleep(500)
    Sound(100, 0, 100, 0)
    OP_71(0x0, 0x5, 0x0, 0x0, 0x8)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_6F(0x79)
    OP_68(3000, 5100, -8000, 3000)
    SetCameraDistance(18000, 3000)
    OP_6F(0x79)
    Sleep(1500)
    Fade(500)
    OP_68(2700, 5100, 3350, 0)
    MoveCamera(52, 26, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00002F#5P(KeA...\x01",
            "So she was here.)\x02\x03",
            "#00006F(...As I thought, it seems\x01",
            "I made her worry a little.)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x101, 2640, 4100, 4150, 180)
    SetMapObjFlags(0x0, 0x10)
    SetScenarioFlags(0x144, 4)
    EventEnd(0x5)
    Return()

    # Function_13_3351 end

    def Function_14_34ED(): pass

    label("Function_14_34ED")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    AddParty(0x8, 0xFF, 0xFF)
    AddParty(0x4, 0xFF, 0xFF)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_64(0xB)
    LoadChrToIndex("chr/ch02710.itc", 0x1E)
    LoadChrToIndex("chr/ch02702.itc", 0x1F)
    LoadChrToIndex("apl/ch51302.itc", 0x20)
    LoadChrToIndex("apl/ch51355.itc", 0x21)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu01103.itp")
    SoundLoad(3611)
    SoundLoad(3612)
    OP_4B(0xB, 0xFF)
    SetChrPos(0x101, 3000, 4100, -6800, 180)
    SetChrPos(0x102, 0, 4100, 2000, 180)
    SetChrPos(0x103, 3550, 4100, 0, 180)
    SetChrPos(0x104, 3550, 4100, 4000, 180)
    SetChrPos(0x109, 0, 4100, 3200, 180)
    SetChrPos(0x105, 0, 4100, 4400, 180)
    SetChrPos(0x9, 0, 4100, 0, 180)
    OP_4B(0x9, 0xFF)
    SetChrChipByIndex(0x9, 0x1E)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x10)
    SetChrFlags(0x9, 0x1)
    SetChrFlags(0xA, 0x8)
    SetChrFlags(0x8, 0x8)
    OP_68(3000, 5100, -7400, 0)
    MoveCamera(135, 26, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18500, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(17500, 2000)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0xB,
        "#01108F#5P............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002F#6PKeA, so that's where you were.\x02",
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_93(0xB, 0x0, 0x1F4)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)
    OP_C9(0x0, 0x80000000)

    AnonymousTalk(
        0xB,
        (
            "#3611V#40WAh...Lloyd...\x02\x03",
            "#3612V#30WEhehe...\x01",
            "Is it time we arrive there?\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xE1C)
    OP_C9(0x1, 0x80000000)
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
            "#00004F#6PYeah, in a little while.\x02\x03",
            "#00000FThere's also a theme park, so\x01",
            "let's play a lot when we arrive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#01102F#11PYes!\x02\x03",
            "#01122F...Ehehe...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00006F#6P...I'm sorry, KeA.\x02\x03",
            "#00008FIt seems that lately I only\x01",
            "gave you sad thoughts...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#01121F#11P...No.\x01",
            "I'm totally fine.\x02\x03",
            "#01106FI don't know the details, but...\x01",
            "I've got it that everyone is\x01",
            "somehow feeling down...\x02\x03",
            "#01108FKeA too wanted to cheer\x01",
            "you all up, and yet...\x02\x03",
            "She couldn't do anything, in the end...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetCameraDistance(17200, 750)
    OP_9B(0x0, 0x101, 0x0, 0x1F4, 0x3E8, 0x0)
    OP_6F(0x79)
    Fade(250)
    BeginChrThread(0x101, 3, 0, 23)
    BeginChrThread(0xB, 3, 0, 24)
    WaitChrThread(0x101, 3)
    WaitChrThread(0xB, 3)
    OP_0D()

    ChrTalk(
        0xB,
        "#01105F#11PAh... \x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#6PYou're cheering us up plenty.\x02\x03",
            "#00002FBy staying by our side, KeA...\x02\x03",
            "How much do you think that cheers\x01",
            "us up and gives us all strength?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#01105F#11PIs that so...?\x02\x03",
            "#01108F...I wonder if it's really so...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#6P...?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_A1(0x101, 0x514, 0x2, 0x2, 0x1)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x101, 0x2)
    OP_9B(0x1, 0x101, 0x0, 0xFFFFFF06, 0x1F4, 0x0)

    ChrTalk(
        0xB,
        (
            "#01109F#11P...Ehehe. \x01",
            "Somehow I don't get it anymore.\x02\x03",
            "#01105FAh, but it seems that everyone\x01",
            "has cheered up a little, eh?\x02\x03",
            "#01104FEhehe. \x01",
            "As I thought, you're amazing Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#6PI don't think it's\x01",
            "because of me...\x02\x03",
            "#00002FBut since we're here, let's\x01",
            "have a lot of fun with everyone.\x02\x03",
            "You're really looking forward\x01",
            "to the theme park, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_A1(0xB, 0x4B0, 0x4, 0x8, 0x9, 0x8, 0x3)

    ChrTalk(
        0xB,
        "#01109F#11PYes!\x02",
    )

    CloseMessageWindow()
    OP_A1(0xB, 0x4B0, 0x6, 0xB, 0xC, 0xD, 0xE, 0xD, 0xC)

    ChrTalk(
        0xB,
        (
            "#01110F#11PKeA wants to ride on the ferris wheel!\x02\x03",
            "And then, I guess I'd like to\x01",
            ""Kick Michey" with Tio too!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00011F#6P"Kick Michey"....\x01",
            "Was that in vogue among the children?\x02\x03",
            "#00012FUhhm, although Tio seems to be\x01",
            "a little over the age limit...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x103,
        (
            "#00211F#6P#N──I will bear in mind to mind\x01",
            "my manners in that regard.\x02",
        )
    )

    CloseMessageWindow()
    OP_A1(0xB, 0x5DC, 0x2, 0xC, 0xF)
    SetChrChipByIndex(0xB, 0x3)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x2)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xB, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Fade(500)
    OP_68(3000, 4800, -5400, 0)
    OP_68(3000, 4800, -7400, 6000)
    MoveCamera(150, 28, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20350, 0)
    ClearChrFlags(0x9, 0x800)
    BeginChrThread(0x101, 3, 0, 21)
    BeginChrThread(0xB, 3, 0, 22)
    BeginChrThread(0x103, 3, 0, 15)
    BeginChrThread(0x9, 3, 0, 16)
    Sleep(1000)
    BeginChrThread(0x102, 3, 0, 17)
    Sleep(50)
    BeginChrThread(0x104, 3, 0, 18)
    Sleep(500)
    BeginChrThread(0x109, 3, 0, 19)
    Sleep(50)
    BeginChrThread(0x105, 3, 0, 20)
    WaitChrThread(0x101, 3)
    WaitChrThread(0xB, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x9, 3)
    WaitChrThread(0x102, 3)

    ChrTalk(
        0x101,
        "#00005F#5PTio...and everyone...\x02",
    )

    WaitChrThread(0x104, 3)
    WaitChrThread(0x109, 3)
    WaitChrThread(0x105, 3)
    OP_6F(0x79)
    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#01105F#11POh, what's wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#01200F#11PWoof.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109F#12P*giggle*, somehow we\x01",
            "met each other...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#12PFurthermore, it seems it's\x01",
            "time for our arrival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002F#5PYeah, I see.\x02",
    )

    CloseMessageWindow()

    def lambda_3FB3():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3FB3)
    Sleep(50)

    def lambda_3FC3():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3FC3)
    Sleep(50)

    def lambda_3FD3():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_3FD3)
    Sleep(50)

    def lambda_3FE3():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_3FE3)
    Sleep(50)

    def lambda_3FF3():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_3FF3)
    Sleep(50)

    def lambda_4003():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_4003)
    Sleep(50)

    def lambda_4013():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_4013)
    Sleep(50)
    SetChrFlags(0x9, 0x20)

    def lambda_4028():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_4028)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x104, 2)
    WaitChrThread(0x109, 2)
    WaitChrThread(0x105, 2)
    WaitChrThread(0xB, 2)
    WaitChrThread(0x9, 2)
    Sleep(200)
    Fade(500)
    OP_68(3000, 4800, -7400, 0)
    MoveCamera(159, 0, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(47500, 0)
    OP_93(0x101, 0xE1, 0x0)
    OP_93(0x102, 0xE1, 0x0)
    OP_93(0x103, 0xE1, 0x0)
    OP_93(0x104, 0xE1, 0x0)
    OP_93(0x109, 0xE1, 0x0)
    OP_93(0x105, 0xE1, 0x0)
    OP_93(0xB, 0xE1, 0x0)
    OP_93(0x9, 0xE1, 0x0)
    OP_68(0, 7800, -25000, 6000)
    OP_6F(0x79)
    OP_0D()
    Sleep(300)
    Sound(3029, 255, 100, 0)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0xB,
        "#01109F#6P#N#4SWooow...!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xBD9)

    ChrTalk(
        0x102,
        "#00102F#6P#NHow pretty...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x109,
        (
            "#10109F#6P#NToday the weather is fine,\x01",
            "it's ideal for an outing!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#00309F#6P#NAaalright, now I'm\x01",
            "really hyped!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopSound(479, 2000, 100)
    FadeToDark(2000, 0, -1)
    OP_68(0, 7800, -26000, 2000)
    OP_6F(0x79)
    OP_0D()
    SetScenarioFlags(0x22, 0)
    NewScene("t1000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_14_34ED end

    def Function_15_41E1(): pass

    label("Function_15_41E1")

    OP_9B(0x0, 0xFE, 0x0, 0x15E0, 0x898, 0x0)
    TurnDirection(0xFE, 0x101, 500)
    Return()

    # Function_15_41E1 end

    def Function_16_41F8(): pass

    label("Function_16_41F8")

    OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x898, 0x1)
    SetChrFlags(0xFE, 0x800)
    OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x898, 0x1)
    ClearChrFlags(0xFE, 0x800)
    OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x898, 0x1)
    SetChrFlags(0xFE, 0x800)
    OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x898, 0x1)
    ClearChrFlags(0xFE, 0x800)
    OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x898, 0x1)
    OP_9B(0x0, 0xFE, 0xFFD3, 0x7D0, 0x898, 0x0)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    BeginChrThread(0xFE, 1, 0, 0)
    TurnDirection(0xFE, 0xB, 500)
    Return()

    # Function_16_41F8 end

    def Function_17_427C(): pass

    label("Function_17_427C")

    OP_9B(0x0, 0xFE, 0x0, 0x1D4C, 0x898, 0x1)
    OP_9B(0x0, 0xFE, 0xFFC4, 0x7D0, 0x898, 0x0)
    TurnDirection(0xFE, 0x101, 500)
    Return()

    # Function_17_427C end

    def Function_18_42A2(): pass

    label("Function_18_42A2")

    OP_9B(0x0, 0xFE, 0x0, 0x2008, 0x898, 0x0)
    TurnDirection(0xFE, 0x101, 500)
    Return()

    # Function_18_42A2 end

    def Function_19_42B9(): pass

    label("Function_19_42B9")

    OP_9B(0x0, 0xFE, 0x0, 0x21FC, 0x898, 0x1)
    OP_9B(0x0, 0xFE, 0xFFD3, 0x320, 0x898, 0x0)
    TurnDirection(0xFE, 0x101, 500)
    Return()

    # Function_19_42B9 end

    def Function_20_42DF(): pass

    label("Function_20_42DF")

    OP_9B(0x0, 0xFE, 0x0, 0x238C, 0x898, 0x1)
    OP_9B(0x0, 0xFE, 0xF, 0x640, 0x898, 0x0)
    OP_93(0xFE, 0x87, 0x1F4)
    TurnDirection(0xFE, 0xB, 500)
    Return()

    # Function_20_42DF end

    def Function_21_430C(): pass

    label("Function_21_430C")

    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(1500)
    OP_93(0xFE, 0x13B, 0x1F4)
    Return()

    # Function_21_430C end

    def Function_22_431E(): pass

    label("Function_22_431E")

    Sleep(1000)
    OP_93(0xFE, 0x13B, 0x1F4)
    Return()

    # Function_22_431E end

    def Function_23_4329(): pass

    label("Function_23_4329")

    SetChrFlags(0xFE, 0x2)
    SetChrChipByIndex(0xFE, 0x20)
    OP_A1(0xFE, 0x3E8, 0x3, 0x1, 0x2, 0x3)
    OP_A1(0xFE, 0x3E8, 0x6, 0x4, 0x5, 0x6, 0x5, 0x4, 0x3)
    Return()

    # Function_23_4329 end

    def Function_24_4348(): pass

    label("Function_24_4348")

    SetChrFlags(0xFE, 0x2)
    SetChrChipByIndex(0xFE, 0x21)
    OP_A1(0xFE, 0x3E8, 0x3, 0x1, 0x2, 0x3)
    OP_A1(0xFE, 0x3E8, 0x6, 0x4, 0x5, 0x6, 0x5, 0x4, 0x3)
    Return()

    # Function_24_4348 end

    def Function_25_4367(): pass

    label("Function_25_4367")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0xB, 0xFF)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0x101, 2500, 4100, -8000, 180)
    SetChrPos(0xB, 3500, 4100, -8000, 180)
    OP_68(0, 5100, -18500, 0)
    MoveCamera(35, 3, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(25000, 0)
    OP_68(0, 2100, 18000, 15000)
    MoveCamera(40, 30, 0, 15000)
    SetCameraDistance(25000, 15000)
    FadeToBright(1000, 0)
    Sound(479, 2, 10, 0)
    Sleep(100)
    OP_25(0x1DF, 0x14)
    Sleep(100)
    OP_25(0x1DF, 0x1E)
    Sleep(100)
    OP_25(0x1DF, 0x28)
    Sleep(100)
    OP_25(0x1DF, 0x32)
    Sleep(100)
    OP_25(0x1DF, 0x3C)
    Sleep(100)
    OP_25(0x1DF, 0x46)
    Sleep(100)
    OP_25(0x1DF, 0x50)
    Sleep(100)
    OP_25(0x1DF, 0x5A)
    Sleep(100)
    OP_25(0x1DF, 0x64)
    OP_0D()
    Sleep(8000)
    StopSound(479, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 0)
    NewScene("e0510", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_25_4367 end

    def Function_26_447A(): pass

    label("Function_26_447A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    LoadChrToIndex("chr/ch05500.itc", 0x1E)
    SoundLoad(3802)
    SoundLoad(3775)
    SoundLoad(3776)
    SoundLoad(3777)
    SoundLoad(3778)
    SoundLoad(3779)
    SoundLoad(3619)
    SoundLoad(3620)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis407.itp")
    OP_4B(0xB, 0xFF)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0x101, 2500, 4100, -8000, 180)
    SetChrPos(0xB, 3500, 4100, -8000, 180)
    ClearChrFlags(0xE, 0x80)
    SetChrChipByIndex(0xE, 0x1E)
    SetChrSubChip(0xE, 0x0)
    SetChrFlags(0xE, 0x8000)
    SetChrPos(0xE, 0, 4100, 1000, 180)
    SetChrFlags(0xE, 0x8)
    ClearMapObjFlags(0x0, 0x10)
    OP_68(3160, 5100, -6140, 0)
    MoveCamera(145, 29, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(20900, 0)
    FadeToBright(1000, 0)
    OP_68(3160, 5100, -8140, 3000)
    Sleep(2500)
    OP_63(0xB, 0x0, 1700, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1000)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0xB,
        "#01104F#3619V#5P#30W#15AHum hu hum...♪\x02",
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    Sleep(300)
    TurnDirection(0x101, 0xB, 500)
    Sleep(150)

    ChrTalk(
        0x101,
        (
            "#00012F#12PHa ha...\x01",
            "You're in a good mood, KeA.\x02\x03",
            "#00002FSomehow many things happened, but...\x01",
            "Did you enjoy it?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x101, 500)

    ChrTalk(
        0xB,
        (
            "#01109F#5PYes!\x02\x03",
            "#01110FI want to go out with\x01",
            "everyone again!\x02\x03",
            "Maybe to Armorica Village next time...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#12PHa ha, that could be nice.\x02\x03",
            "#00004F(...Judging from last night I thought\x01",
            "that something had happened, but...)\x02\x03",
            "(She looks completely fine...\x01",
            "Maybe I shouldn't worry that much?)\x02\x03",
            "#00008F(Rather, I should be worrying\x01",
            "about the "Society" actions...)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xB,
        (
            "#01105F#5PHm?\x01",
            "Lloyd, what's wrong?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#12PNo, it's nothing.\x02\x03",
            "#00008F...More importantly, KeA.\x01",
            "Did you really not spot a\x01",
            "weird guy last night?\x02\x03",
            "#00001FSomeone who wore a pink colored outfit...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#01112F#5PHmmm...\x01",
            "I don't think I saw him.\x02\x03",
            "#01106FBecause KeA was half asleep,\x01",
            "she isn't very sure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#12PI see...\x01",
            "Well, it doesn't matter then.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xE, 0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 7)), scpexpr(EXPR_END)), "loc_49BD")
    OP_C9(0x0, 0x80000000)

    NpcTalk(
        0xE,
        "Mariabell's Voice",
        "#3802V#2P#30WMy, so you were here?\x02",
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    Jump("loc_49E8")

    label("loc_49BD")


    NpcTalk(
        0xE,
        "Girl's Voice",
        "#2PMy, so you were here?\x02",
    )

    CloseMessageWindow()

    label("loc_49E8")

    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xB, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(2000, 5100, -7500, 4000)
    MoveCamera(147, 22, 0, 4000)

    def lambda_4A30():

        label("loc_4A30")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_4A30")

    QueueWorkItem2(0x101, 2, lambda_4A30)

    def lambda_4A42():

        label("loc_4A42")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_4A42")

    QueueWorkItem2(0xB, 2, lambda_4A42)
    BeginChrThread(0xE, 3, 0, 27)
    WaitChrThread(0xE, 3)
    EndChrThread(0x101, 0x2)
    EndChrThread(0xB, 0x2)
    OP_6F(0x79)

    ChrTalk(
        0xB,
        "#01110F#5PAh, it's Bell.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#5PMiss Mariabell, thank\x01",
            "you for your hard work.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4BE8")

    ChrTalk(
        0xE,
        (
            "#02902F#12PHu hu, it's you all who\x01",
            "work hard, am I not right?\x02\x03",
            "#02906FStill, the "Society", was it called?\x01",
            "To think there were jokers among them.\x02\x03",
            "#02903FOne of their members\x01",
            "abducted my dolls too!\x02\x03",
            "#02910FThe safety system of the security\x01",
            "department needs to be thorough...!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4CCD")

    label("loc_4BE8")


    ChrTalk(
        0xE,
        (
            "#02902F#12PHu hu, it's you all who\x01",
            "work hard, am I not right?\x02\x03",
            "#02906FStill, the "Society", was it called?\x01",
            "To think there were jokers among them.\x02\x03",
            "#02901FThe safety system of the security\x01",
            "department needs to be thorough...!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4CCD")


    ChrTalk(
        0x101,
        (
            "#00012F#5PY-You're right...\x02\x03",
            "#00008F(Although I think it's not a guy who\x01",
            "private guards could manage...)\x02\x03",
            "#00013F(...As I thought, we're the ones\x01",
            "who need to be careful.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#02904F#12P──Well, that aside.\x02\x03",
            "#02900FMr. Lloyd, Miss KeA.\x02\x03",
            "It just occurred to me, but why don't you take \x01",
            "a commemorative picture with everyone?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xB, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00002F#5PYeah, that's nice!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x101, 500)
    Sleep(100)

    ChrTalk(
        0xB,
        (
            "#01105F#5PEhm, did you take a "commemorative\x01",
            "picture" before with everyone?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xB, 500)
    Sleep(100)

    ChrTalk(
        0x101,
        (
            "#00004F#11PYeah, it's something to leave the memories\x01",
            "with everyone in a picture.\x02\x03",
            "#00000FIt means that when you look at it, you'll be\x01",
            "always remembered about this vacation.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0xB,
        "#01107F#4S#5PYes, I want to take one!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#02909F#12PIt's decided.\x02\x03",
            "#02905FThen... Could the deck here\x01",
            "be more suited than inboard?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xE, 500)

    ChrTalk(
        0x101,
        (
            "#00009F#5PYou're right.\x01",
            "And the weather is nice too.\x02\x03",
            "#00002FI'll go call everyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#02904F#12PYes, please.\x02\x03",
            "#02902FAlso, please tell about this\x01",
            "to the tour guide inside.\x02\x03",
            "Commemorative pictures are free of charge,\x01",
            "she will accept to take one immediately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#5PAlright.\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x19, 0x1F4)
    OP_68(3000, 5100, 0, 5000)
    MoveCamera(30, 25, 0, 5000)
    OP_6E(400, 5000)
    SetCameraDistance(22000, 5000)
    BeginChrThread(0x101, 3, 0, 28)

    def lambda_5198():

        label("loc_5198")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_5198")

    QueueWorkItem2(0xB, 2, lambda_5198)

    def lambda_51AA():
        OP_93(0xFE, 0xA, 0x12C)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_51AA)
    Sleep(1500)
    SetMessageWindowPos(250, 180, -1, -1)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0xB,
        "#01105F#3620V#30W#10A#11P#NAh──\x02",
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    WaitChrThread(0x101, 3)
    EndChrThread(0xB, 0x2)
    EndChrThread(0xE, 0x2)
    OP_6F(0x79)
    StopBGM(0x1770)

    ChrTalk(
        0xB,
        "#01112F#40W#12P#N............\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0xE,
        (
            "#02913F#3775V#12P#30W#NUh uh...\x02\x03",
            "#3776V──You don't want to cause unnecessary\x01",
            "worries to the people important to you.\x02\x03",
            "#02902F#3777VBeing a good woman is hard, eh?\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xEC1)
    OP_C9(0x1, 0x80000000)
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xB,
        "#01105F#12P#N!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    TurnDirection(0xB, 0xE, 0)
    OP_68(2000, 5100, -7500, 0)
    MoveCamera(300, 21, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23000, 0)
    SetCameraDistance(22000, 1500)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    Sleep(500)
    TurnDirection(0xE, 0xB, 350)
    OP_6F(0x79)
    CancelBlur(0)
    SetCameraDistance(21000, 20000)
    Sleep(300)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0xE,
        (
            "#02913F#3778V#5P#40W#30AYou are troubled by something, right?\x02\x03",
            "#02912F#3779V#35A──If you are fine with me,\x01",
            "maybe I could be of help.\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xEC3)
    OP_C9(0x1, 0x80000000)
    StopSound(479, 3000, 80)
    FadeToDark(2000, 0, -1)
    SetCameraDistance(20700, 2000)
    OP_6F(0x79)
    OP_0D()
    WaitBGM()
    Sleep(2500)
    OP_29(0xA5, 0x1, 0xD)
    OP_29(0xA5, 0x4, 0x10)
    OP_32(0xFF, 0xFE, 0x0)
    OP_E5(0xA)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_57(0x3)
    OP_E5(0x3)
    Sleep(100)
    MiniGame(0x2B, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_E0(0x1F, 0x0)
    Sleep(100)
    OP_68(-1000000, 0, 0, 0)
    OP_C9(0x0, 0x10)
    OP_C9(0x0, 0x10000)
    SetScenarioFlags(0x25, 0)
    OP_50(0x50, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_50(0x31, (scpexpr(EXPR_PUSH_LONG, 0x99), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ShowSaveMenu()
    ClearScenarioFlags(0x25, 0)
    MiniGame(0x2B, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_49()
    OP_CC(0x1, 0xFF, 0x0)
    OP_C9(0x1, 0x10)
    OP_E5(0xB)
    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 0)
    NewScene("e4600", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_26_447A end

    def Function_27_550E(): pass

    label("Function_27_550E")

    OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0xFFD3, 0x5DC, 0x7D0, 0x0)
    TurnDirection(0xFE, 0xB, 0)
    Return()

    # Function_27_550E end

    def Function_28_5534(): pass

    label("Function_28_5534")

    OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0xFFE7, 0x1F40, 0x7D0, 0x1)
    OP_96(0xFE, 0xA50, 0x1004, 0x11C6, 0x7D0, 0x0)
    Sound(100, 0, 100, 0)
    OP_70(0x0, 0x5)
    OP_71(0x0, 0x0, 0x5, 0x0, 0x8)
    OP_79(0x0)

    def lambda_5584():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5584)
    Sleep(300)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    WaitChrThread(0xFE, 1)
    Sound(100, 0, 100, 0)
    OP_71(0x0, 0x5, 0x0, 0x0, 0x8)
    OP_79(0x0)
    SetChrPos(0x101, 0, 0, 0, 0)
    Return()

    # Function_28_5534 end

    SaveToFile()

Try(main)
