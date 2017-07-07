from ScenarioHelper import *

def main():
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
        "Tio",                 # 1
        "Zeit",               # 2
        "Waji",                   # 3
        "Keya",                 # 4
        "tourist",                 # 5
        "tourist",                 # 6
        "Marybele",             # 7
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
        "Function_4_AA2",          # 04, 4
        "Function_5_D10",          # 05, 5
        "Function_6_D2E",          # 06, 6
        "Function_7_103E",         # 07, 7
        "Function_8_115D",         # 08, 8
        "Function_9_11CA",         # 09, 9
        "Function_10_2719",        # 0A, 10
        "Function_11_2739",        # 0B, 11
        "Function_12_2759",        # 0C, 12
        "Function_13_2F59",        # 0D, 13
        "Function_14_30FE",        # 0E, 14
        "Function_15_3DCC",        # 0F, 15
        "Function_16_3DE3",        # 10, 16
        "Function_17_3E67",        # 11, 17
        "Function_18_3E8D",        # 12, 18
        "Function_19_3EA4",        # 13, 19
        "Function_20_3ECA",        # 14, 20
        "Function_21_3EF7",        # 15, 21
        "Function_22_3F09",        # 16, 22
        "Function_23_3F14",        # 17, 23
        "Function_24_3F33",        # 18, 24
        "Function_25_3F52",        # 19, 25
        "Function_26_4065",        # 1A, 26
        "Function_27_4FE5",        # 1B, 27
        "Function_28_500B",        # 1C, 28
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
    Jump("loc_A9E")

    label("loc_486")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_494")
    Jump("loc_A9E")

    label("loc_494")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_4A4")
    Jump("loc_A9E")

    label("loc_4A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_4B2")
    Jump("loc_A9E")

    label("loc_4B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_4C0")
    Jump("loc_A9E")

    label("loc_4C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_4CE")
    Jump("loc_A9E")

    label("loc_4CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_4DC")
    Jump("loc_A9E")

    label("loc_4DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_4EA")
    Jump("loc_A9E")

    label("loc_4EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_A9E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15A, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A0D")

    ChrTalk(
        0x8,
        (
            "#00204FThis, anyway …\x01",
            "Today we had a long vacation\x01",
            "I hope you enjoy it.\x02\x03",
            "#00200FThere was also an investigation of \"auction house\" in the front,\x01",
            "Most of the time I enjoy\x01",
            "There was not it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FCertainly, in Michelin\x01",
            "What I go to play properly\x01",
            "This was my first time.\x02\x03",
            "#00009FHahaha, after all\x01",
            "Tioのお目当ては\x01",
            "Is it a theme park?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#00204FIt is Ron of the mochi.\x02\x03",
            "\"Michelin · Wonderland\"\x01",
            "(MICHLLAM WONDER LAND) ……\x02\x03",
            "- M. W · L for short.\x02\x03",
            "#00202FI am looking forward to seeing Missi.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 4)), scpexpr(EXPR_END)), "loc_8F2")
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00004F…. That reminds me.\x01",
            "Do you remember the story of the example \"promise\"?\x02\x03",
            "#00002FAfter the cult incident came to an end,\x01",
            "Look at the theme park\x01",
            "It was a story to go for fun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#00204F… … Of course, I remember.\x02\x03",
            "\"First of all, everyone in the support section ……\x01",
            "After that, with Mr. Lloyd and me. \"\x02\x03",
            "#00200FIn that sense, with this invitation\x01",
            "Finally I shifted to Phase 1,\x01",
            "You can say that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FThe meaning of the phrase is\x01",
            "I do not quite understand it … ….\x02\x03",
            "#00000FNext time,\x01",
            "I definitely have to come by themselves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#00209FHehu ……\x01",
            "Yes, I am looking forward to it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A05")

    label("loc_8F2")


    ChrTalk(
        0x101,
        (
            "#00004FTioはみっしぃについて\x01",
            "We are special in detail.\x02\x03",
            "#00002FWhen you arrive at the theme park,\x01",
            "Tell me a lot?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#00204F……OK.\x02\x03",
            "#00202FSo, first, Mr. Lloyd\x01",
            "Missi's birth privacy, family composition, etc.\x01",
            "Thoroughly devastating … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006FNo, no, that's fine.\x02",
    )

    CloseMessageWindow()

    label("loc_A05")

    SetScenarioFlags(0x15A, 0)
    Jump("loc_A9E")

    label("loc_A0D")


    ChrTalk(
        0x8,
        (
            "#00202FIf it's about Mitsushi,\x01",
            "From reaching the theme park\x01",
            "I will teach you variously.\x02\x03",
            "#00204FNow, go to everyone's place\x01",
            "Would you like me to talk to you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A9E")

    TalkEnd(0xFE)
    Return()

    # Function_3_475 end

    def Function_4_AA2(): pass

    label("Function_4_AA2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_AB3")
    Jump("loc_D0C")

    label("loc_AB3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_AC1")
    Jump("loc_D0C")

    label("loc_AC1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_ACF")
    Jump("loc_D0C")

    label("loc_ACF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_ADD")
    Jump("loc_D0C")

    label("loc_ADD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_AEB")
    Jump("loc_D0C")

    label("loc_AEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_AF9")
    Jump("loc_D0C")

    label("loc_AF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_B07")
    Jump("loc_D0C")

    label("loc_B07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_D0C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CAD")
    OP_4B(0x8, 0xFF)

    ChrTalk(
        0x9,
        "#01203FGurururu …… won.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 500)

    ChrTalk(
        0x8,
        (
            "#00204F\"Wow, it's a hands-on leader,\"\x01",
            "It seems to be saying that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012Fはは、Zeitに言われると\x01",
            "There is no stands.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#00211FAlso, \"Too bad\"\x01",
            "\"Become a more nice man\"\x01",
            "It seems to be said.\x02",
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
            "#00006F…. That, is not it?\x01",
            "Is not there a subjectivity?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#00203FWell, for what thing.\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0x5A, 0x0)
    SetScenarioFlags(0x0, 4)
    OP_4C(0x8, 0xFF)
    Jump("loc_D0C")

    label("loc_CAD")


    ChrTalk(
        0x9,
        "#01203F… …. Gurururu ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F（Zeitもミシュラムを\x01",
            "I wonder if you are looking forward to it …).)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D0C")

    TalkEnd(0xFE)
    Return()

    # Function_4_AA2 end

    def Function_5_D10(): pass

    label("Function_5_D10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D27")
    Call(0, 14)
    Return()

    label("loc_D27")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_5_D10 end

    def Function_6_D2E(): pass

    label("Function_6_D2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D45")
    Call(0, 12)
    Return()

    label("loc_D45")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_D56")
    Jump("loc_103A")

    label("loc_D56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_D64")
    Jump("loc_103A")

    label("loc_D64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_D72")
    Jump("loc_103A")

    label("loc_D72")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_D80")
    Jump("loc_103A")

    label("loc_D80")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_D8E")
    Jump("loc_103A")

    label("loc_D8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_D9C")
    Jump("loc_103A")

    label("loc_D9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_DAA")
    Jump("loc_103A")

    label("loc_DAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_103A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DC2")
    Jump("loc_103A")

    label("loc_DC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F6E")

    ChrTalk(
        0xA,
        (
            "#10304FWell, except for host work\x01",
            "It's been a while since I came to Michelin,\x01",
            "May I have my feather rested today.\x02\x03",
            "#10300FAt some point in time\x01",
            "I am planning to go to a restaurant,\x01",
            "Are you going to have a drink?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F…… Huh, that seems to say many times\x01",
            "You can not accept underage drinking?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#10309FHuh, I'm talking about it.\x01",
            "Please do not remove more fucking, you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FFor example,\x01",
            "That's not it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_103A")

    label("loc_F6E")


    ChrTalk(
        0xA,
        (
            "#10309FKata is a fun thing to say.\x01",
            "Please do not remove more fucking, you.\x02\x03",
            "#10302FWhat to do, drop a girl\x01",
            "The basic technique of the host\x01",
            "You can teach me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006FDo not try to acquire … …\x02",
    )

    CloseMessageWindow()

    label("loc_103A")

    TalkEnd(0xFE)
    Return()

    # Function_6_D2E end

    def Function_7_103E(): pass

    label("Function_7_103E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_1159")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10ED")

    ChrTalk(
        0xC,
        (
            "Something, everyone in town\x01",
            "Dokitsu was talking about something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "We are from abroad\x01",
            "I do not quite understand it ….\x01",
            "Is it something serious?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1159")

    label("loc_10ED")


    ChrTalk(
        0xC,
        (
            "People in the street were talking\x01",
            "I wonder what is Dokuritsu?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I do not quite understand it ….\x01",
            "Is it something serious?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1159")

    TalkEnd(0xFE)
    Return()

    # Function_7_103E end

    def Function_8_115D(): pass

    label("Function_8_115D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_11C6")

    ChrTalk(
        0xD,
        (
            "Hey, than that\x01",
            "Is that cute of the front seat, is not it cute?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Do you reverse it? Do it?\x02",
    )

    CloseMessageWindow()

    label("loc_11C6")

    TalkEnd(0xFE)
    Return()

    # Function_8_115D end

    def Function_9_11CA(): pass

    label("Function_9_11CA")

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
            "#30WTwo weeks after the trade meeting ─ ─\x01",
            "Crossbell City was wrapped in quiet heat.\x02\x03",
            "Other autonomous states ─\x01",
            "Leman, Oled, Northern Buria\x01",
            "Under the approval of the Alteria law country,\x01",
            "Sovereignty equivalent to that of the state is recognized.\x02\x03",
            "But in Crossbell Autonomous Region\x01",
            "From the Imperial Republic, as a buffer zone\x01",
            "Only the autonomy right was approved.\x02\x03",
            "(By the way, 10 of tax revenue,\x01",
            "With the term \"mandate and governing expenses\"\x01",
            "It is paid to both the empire and the republic. )\x02\x03",
            "Development as a trade and financial center,\x01",
            "Vulnerability of political infrastructure inversely proportional to it -\x02\x03",
            "As a result, it is possible that foreign interference and\x01",
            "Brought the rise of mafia and others.\x02\x03",
            "To break down that distorted situation\x01",
            "\"It will be independent as a sovereign state\"\x01",
            "To Mayor Dieter's daring advocate,\x01",
            "Many citizens felt empathy … …\x02\x03",
            "Many are concerned about the intention of the two major powers,\x01",
            "Discussion on the pros and cons of 'independence'\x01",
            "It was supposed to be done here and there.\x02",
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
        "#00008F#5P#30W………………………….\x02",
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
            "#00006F#5P#30W…………. Ha ……………\x02\x03",
            "#00008FIt is useless, from that\x01",
            "Even though nearly half a month passed ……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(3052, 255, 80, 0)

    ChrTalk(
        0x9,
        "#01200F#6P#30Wwon?\x02",
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
            "#00012F#11P#30WSorry about sighs.\x02\x03",
            "#00008F……なあ、Zeit。\x02\x03",
            "At a time like this\x01",
            "What should I do?\x02\x03",
            "Not to mention Randy,\x01",
            "Eli and Noel thoughtfully\x01",
            "It seems to be doing … …\x02\x03",
            "#00006F……Keyaにも気を\x01",
            "You seem to have sent me.\x02",
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
            "#3054V#30Wwon.\x02\x03",
            "#3060V#40WGurururururu … …. won.\x02",
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
            "#00005F#11P#30WEr …\x01",
            "What are you saying?\x02\x03",
            "#00012FHaha, I'm sorry.\x01",
            "Shake it from here …\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearChrFlags(0x8, 0x8)
    OP_C9(0x0, 0x80000000)

    NpcTalk(
        0xA,
        "Voice of a girl",
        (
            "#2674V#5P#N#30W#35A\"At times like this\x01",
            "Do not think in theory. \"\x02\x03",
            "#2675V#25A\"From yourself\x01",
            "Try to talk. \"\x02\x03",
            "#4108V#N#15AIt seems to be ─ ─.\x02",
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
        "#00005F#12PTio……\x02",
    )

    CloseMessageWindow()
    OP_68(-1350, 5100, 12250, 2500)
    MoveCamera(210, 23, 0, 2500)
    SetCameraDistance(19330, 2500)

    def lambda_1BAF():

        label("loc_1BAF")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_1BAF")

    QueueWorkItem2(0x101, 2, lambda_1BAF)
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
            "#30W… … It is a nice wind.\x02\x03",
            "Awesome vacation#4RVacation#Is not it\x01",
            "It was sunny and really good.\x02",
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
            "#00004F#5PThat's right.\x02\x03",
            "#00000FMarybeleさんに招待された時は\x01",
            "I thought something was wrong.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#00202F#5PHuhu, did you think that something was a trap?\x02\x03",
            "Still a bit\x01",
            "It seems to be enemy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012F#5PHaha, actually I thought a bit.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00006F#5P……ゴメンな、Tioも。\x02\x03",
            "#00008FI just came back.\x01",
            "Show me such a miserable place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#00206F#5P…… I think that it is unreasonable.\x02\x03",
            "#00208FEveryone in front of you\x01",
            "Because I passed away ……\x02\x03",
            "#00200FI think that it is shock if it is normal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#5PNo, as I became an investigator,\x01",
            "It was somewhere prepared for something.\x02\x03",
            "#00001F…… Because there was also Joachim's case\x01",
            "I was going to get used to somehow ……\x02\x03",
            "#00006FAs an investigator, as a leader\x01",
            "There seems to have been insufficient preparedness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#00203F#5P#40WFuu …\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#00200F#11P─ ─ to get used to\x01",
            "Does not it have much to do with preparation?\x02\x03",
            "If it says it, I\x01",
            "It is supposed to be completed.\x02\x03",
            "#00203FPerhaps, after Randy's\x01",
            "Because I am \"accustomed\" to the death of a person.\x02",
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
        "#00008F#6P……Really………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#00206F#11PBut, I am from Lloyd\x01",
            "I think that it is suitable for an investigator\x01",
            "I do not think so much ……\x02\x03",
            "I can do a leader\x01",
            "I do not even think that I am prepared.\x02\x03",
            "#00201F── Everyone Mr. Lloyd\x01",
            "I think that I am probably different.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#6PTio……\x02",
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00006F#6P… … That's right.\x01",
            "It may be true.\x02\x03",
            "#00008FShock received, with lack of preparedness\x01",
            "It seems I mistook it and it became immovable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#00204F#11PThen please please move.\x02\x03",
            "#00202FVacation with all those rare#4RVacation#… ….\x02\x03",
            "To make everyone enjoy it,\x01",
            "What role does the leader take care?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002F#6POh, yes.\x02",
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
        "#00205F#11P……! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009F#6Pサンキュー、Tio。\x02\x03",
            "#00000FHey everyone\x01",
            "I will speak lightly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#00206F#11PWell, yeah.\x01",
            "I wonder if that is good.\x02\x03",
            "#00208F#30W… … but that … ….\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00011F#6POh, bad bad.\x02",
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
        "#00205F#11P#40W…… Ah ………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#6PHe was not treated like a child,\x01",
            "I mean going to appreciate … ….\x02",
        )
    )

    CloseMessageWindow()
    OP_A1(0x8, 0x5DC, 0x3, 0x7, 0x8, 0x9)

    ChrTalk(
        0x8,
        (
            "#00206F#11PNo, I do not mind.\x02\x03",
            "#00208F#30WThat … … rather a bit … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#6PHuh?\x02",
    )

    CloseMessageWindow()
    OP_A1(0x8, 0x5DC, 0x2, 0xA, 0xB)
    Sleep(150)
    OP_82(0x32, 0x0, 0x7D0, 0xC8)

    ChrTalk(
        0x8,
        "#00201F#11PWh … … nothing!\x02",
    )

    CloseMessageWindow()
    OP_A1(0x8, 0x5DC, 0x2, 0xC, 0xD)

    ChrTalk(
        0x8,
        (
            "#00203F#11PEarly for everyone\x01",
            "Please go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#6POh, oh ……?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(150)
    Sound(3053, 255, 60, 0)

    ChrTalk(
        0x9,
        "#01203F#6P#30WGururuluru … (Good night)\x02",
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

    # Function_9_11CA end

    def Function_10_2719(): pass

    label("Function_10_2719")

    SetChrFlags(0xFE, 0x2)
    SetChrChipByIndex(0xFE, 0x1E)
    OP_A1(0xFE, 0x3E8, 0x3, 0x0, 0x1, 0x2)
    OP_A1(0xFE, 0x3E8, 0x7, 0x2, 0x3, 0x4, 0x5, 0x4, 0x3, 0x2)
    Return()

    # Function_10_2719 end

    def Function_11_2739(): pass

    label("Function_11_2739")

    SetChrFlags(0xFE, 0x2)
    SetChrChipByIndex(0xFE, 0x1F)
    OP_A1(0xFE, 0x3E8, 0x3, 0x0, 0x1, 0x2)
    OP_A1(0xFE, 0x3E8, 0x7, 0x2, 0x3, 0x4, 0x5, 0x4, 0x3, 0x2)
    Return()

    # Function_11_2739 end

    def Function_12_2759(): pass

    label("Function_12_2759")

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
            "#30W── Hey, Lloyd.\x02\x03",
            "Apparently active\x01",
            "You seem to have it put in?\x02",
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
            "#00012F#6PHa ha, well.\x02\x03",
            "#00000F……Wajiの方は\x01",
            "Does not it look like pretty?\x02\x03",
            "As usual\x01",
            "Is it cool?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#10304F#5PWell, that's because I sell it.\x02\x03",
            "#10308FBesides that,\x01",
            "I came across unreasonable death\x01",
            "I do not have experience.\x02\x03",
            "#10303FI am in front of the crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008F#6PIs it so……\x02\x03",
            "#00005F……って、Wajiの口から\x01",
            "I heard about the old days for the first time.\x02\x03",
            "#00000FI'm not from Crossbell\x01",
            "I was asking somehow … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#10309F#5PHuh, it is a company secret?\x02\x03",
            "#10300FBut …\x01",
            "Sometimes I lived in a slum.\x02\x03",
            "Far away than the old city\x01",
            "It is a garbage storage that will not be saved.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x6F), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2B3B")

    ChrTalk(
        0x101,
        (
            "#00006F#6P……Really……\x02\x03",
            "#00008FShuri of the alkane shell\x01",
            "She seems to be from the slums of the frontier … …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B9B")

    label("loc_2B3B")


    ChrTalk(
        0x101,
        (
            "#00006F#6P……Really……\x02\x03",
            "#00008FAlcan Shell's rookie's child also\x01",
            "She seems to be from the slums of the frontier … …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B9B")


    ChrTalk(
        0xA,
        (
            "#10305F#5POh, it is a child of Northern Buria.\x02\x03",
            "#10306FThat's terrible ……\x01",
            "With remittances of those who are hunting outside\x01",
            "Go somehow#4RHere#I'm about to surpass.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#6POh, I heard rumors, but ….\x02\x03",
            "#00005F…… as if I went\x01",
            "You talk like one?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#10304F#5PHuh, Well.\x02\x03",
            "#10308F#30W………………………………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F#6PIs it? Is it?\x02\x03",
            "#00003FAlthough I told you it was okay\x01",
            "I mean there is not a little sharpness … …\x02\x03",
            "#00001F……Did something happen?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#10304F#5PBesides myself.\x02\x03",
            "#10300FHowever, in the case of Vipers\x01",
            "There seems to be various things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001F#6PViper ……\x01",
            "It's about Waldo.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#10304F#5PWell, that was how we broke up.\x01",
            "As expected it is somewhat concerned.\x02\x03",
            "#10302FMysterious charisma seems to sell\x01",
            "Even Cool Beauty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#6PDo not say it yourself …\x02\x03",
            "#00008F… But, as for Waldo\x01",
            "I was a little worried.\x02\x03",
            "#00000FEven when time is available\x01",
            "Let's go over to see a little.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#10304F#5PHuh, if you do it\x01",
            "I wonder if this will be helpful as well.\x02",
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

    # Function_12_2759 end

    def Function_13_2F59(): pass

    label("Function_13_2F59")

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
            "#00002F#5P（Keya……\x01",
            "I wonder where I am. )\x02\x03",
            "#00006F(… after all a bit\x01",
            "It seems I was worried. )\x02",
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

    # Function_13_2F59 end

    def Function_14_30FE(): pass

    label("Function_14_30FE")

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
        "#01108F#5P………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002F#6PKeya、ここにいたのか。\x02",
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
            "#3611V#40WAh … … Lloyd … ….\x02\x03",
            "#3612V#30WErr …\x01",
            "I guess it will arrive soon?\x02",
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
            "#00004F#6POh, a little more.\x02\x03",
            "#00000FThere is also a theme park\x01",
            "Let's play a lot of eyes when you arrive?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#01102F#11PWow!\x02\x03",
            "#01122F…… Eh … …\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00006F#6P……ごめんな、Keya。\x02\x03",
            "#00008FRecently, I've been lonely\x01",
            "It seems I was letting him … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#01121F#11P……No.\x01",
            "It is all Hakey.\x02\x03",
            "#01106FI do not know the details, but …\x01",
            "Everyone is depressed\x01",
            "Somehow I understood … ….\x02\x03",
            "#01108FKeyaの方こそみんなを\x01",
            "I wanted to cheer you up ……\x02\x03",
            "I can not do anything …\x02",
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
        "#01105F#11PAh……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#6PI am well, I'm fine.\x02\x03",
            "#00002FKeyaが側に居てくれること……\x02\x03",
            "To how much of it we all\x01",
            "Do you think they are giving me strength and energy?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#01105F#11PIs that so …?\x02\x03",
            "#01108F…… I wonder if that is the case ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#6P……?\x02",
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
            "#01109F#11P…… Hehe.\x01",
            "I have lost something.\x02\x03",
            "#01105FOh, but everyone is a bit\x01",
            "You seem to be getting better?\x02\x03",
            "#01104FHehe.\x01",
            "After all Lloyd is amazing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#6PNo, it's because of me\x01",
            "I do not think so ….\x02\x03",
            "#00002FBut, because it's no problem\x01",
            "Let's have a lot of eyes with everyone.\x02\x03",
            "Theme park,\x01",
            "You looked forward a lot?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_A1(0xB, 0x4B0, 0x4, 0x8, 0x9, 0x8, 0x3)

    ChrTalk(
        0xB,
        "#01109F#11PWow!\x02",
    )

    CloseMessageWindow()
    OP_A1(0xB, 0x4B0, 0x6, 0xB, 0xC, 0xD, 0xE, 0xD, 0xC)

    ChrTalk(
        0xB,
        (
            "#01110F#11PKeya、観覧車に乗りたいー！\x02\x03",
            "あと、Tioといっしょに\x01",
            "I want to do \"Mickey Kick\" ~!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00011F#6P\"Mick exactly kick\" ……\x01",
            "Is it popular among children?\x02\x03",
            "#00012Fうーん、Tioはちょっと\x01",
            "It seems to be caught on age restriction.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x103,
        (
            "#00211F#6P#N─ ─ Manners around that\x01",
            "I intend to make it clear.\x02",
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
        "#00005F#5PTio、それにみんな……\x02",
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
        "#01200F#11Pwon.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109F#12PHuhu, somehow everyone\x01",
            "I mean they got together ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#12PBesides, soon\x01",
            "It seems to arrive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002F#5POh, I see.\x02",
    )

    CloseMessageWindow()

    def lambda_3BA7():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3BA7)
    Sleep(50)

    def lambda_3BB7():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3BB7)
    Sleep(50)

    def lambda_3BC7():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_3BC7)
    Sleep(50)

    def lambda_3BD7():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_3BD7)
    Sleep(50)

    def lambda_3BE7():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_3BE7)
    Sleep(50)

    def lambda_3BF7():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_3BF7)
    Sleep(50)

    def lambda_3C07():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_3C07)
    Sleep(50)
    SetChrFlags(0x9, 0x20)

    def lambda_3C1C():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_3C1C)
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
        "#01109F#6P#N#4SWow ~!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xBD9)

    ChrTalk(
        0x102,
        "#00102F#6P#NThat's pretty …\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x109,
        "#10109F#6P#NIt is a fine weather today, is a day out for holidays!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#00309F#6P#NWell, Gangan,\x01",
            "Tension has come up!\x02",
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

    # Function_14_30FE end

    def Function_15_3DCC(): pass

    label("Function_15_3DCC")

    OP_9B(0x0, 0xFE, 0x0, 0x15E0, 0x898, 0x0)
    TurnDirection(0xFE, 0x101, 500)
    Return()

    # Function_15_3DCC end

    def Function_16_3DE3(): pass

    label("Function_16_3DE3")

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

    # Function_16_3DE3 end

    def Function_17_3E67(): pass

    label("Function_17_3E67")

    OP_9B(0x0, 0xFE, 0x0, 0x1D4C, 0x898, 0x1)
    OP_9B(0x0, 0xFE, 0xFFC4, 0x7D0, 0x898, 0x0)
    TurnDirection(0xFE, 0x101, 500)
    Return()

    # Function_17_3E67 end

    def Function_18_3E8D(): pass

    label("Function_18_3E8D")

    OP_9B(0x0, 0xFE, 0x0, 0x2008, 0x898, 0x0)
    TurnDirection(0xFE, 0x101, 500)
    Return()

    # Function_18_3E8D end

    def Function_19_3EA4(): pass

    label("Function_19_3EA4")

    OP_9B(0x0, 0xFE, 0x0, 0x21FC, 0x898, 0x1)
    OP_9B(0x0, 0xFE, 0xFFD3, 0x320, 0x898, 0x0)
    TurnDirection(0xFE, 0x101, 500)
    Return()

    # Function_19_3EA4 end

    def Function_20_3ECA(): pass

    label("Function_20_3ECA")

    OP_9B(0x0, 0xFE, 0x0, 0x238C, 0x898, 0x1)
    OP_9B(0x0, 0xFE, 0xF, 0x640, 0x898, 0x0)
    OP_93(0xFE, 0x87, 0x1F4)
    TurnDirection(0xFE, 0xB, 500)
    Return()

    # Function_20_3ECA end

    def Function_21_3EF7(): pass

    label("Function_21_3EF7")

    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(1500)
    OP_93(0xFE, 0x13B, 0x1F4)
    Return()

    # Function_21_3EF7 end

    def Function_22_3F09(): pass

    label("Function_22_3F09")

    Sleep(1000)
    OP_93(0xFE, 0x13B, 0x1F4)
    Return()

    # Function_22_3F09 end

    def Function_23_3F14(): pass

    label("Function_23_3F14")

    SetChrFlags(0xFE, 0x2)
    SetChrChipByIndex(0xFE, 0x20)
    OP_A1(0xFE, 0x3E8, 0x3, 0x1, 0x2, 0x3)
    OP_A1(0xFE, 0x3E8, 0x6, 0x4, 0x5, 0x6, 0x5, 0x4, 0x3)
    Return()

    # Function_23_3F14 end

    def Function_24_3F33(): pass

    label("Function_24_3F33")

    SetChrFlags(0xFE, 0x2)
    SetChrChipByIndex(0xFE, 0x21)
    OP_A1(0xFE, 0x3E8, 0x3, 0x1, 0x2, 0x3)
    OP_A1(0xFE, 0x3E8, 0x6, 0x4, 0x5, 0x6, 0x5, 0x4, 0x3)
    Return()

    # Function_24_3F33 end

    def Function_25_3F52(): pass

    label("Function_25_3F52")

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

    # Function_25_3F52 end

    def Function_26_4065(): pass

    label("Function_26_4065")

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
        "#01104F#3619V#5P#30W#15Aふ ふ フ ふ ー ♪ ♪\x02",
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    Sleep(300)
    TurnDirection(0x101, 0xB, 500)
    Sleep(150)

    ChrTalk(
        0x101,
        (
            "#00012F#12Pmy mother……\x01",
            "Keya、ご機嫌だな。\x02\x03",
            "#00002FThere were various things … ….\x01",
            "Did you enjoy it properly?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x101, 500)

    ChrTalk(
        0xB,
        (
            "#01109F#5PWow!\x02\x03",
            "#01110FAlso we all together\x01",
            "I want to go out!\x02\x03",
            "Next time it is almorica village and so on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#12PIt may be nice.\x02\x03",
            "#00004F(… from the appearance of yesterday\x01",
            "I thought there was something … …)\x02\x03",
            "(It seems to be fine,\x01",
            "Do not you worry so much? )\x02\x03",
            "#00008F(Rather it should be worried\x01",
            "Is it about the movement of \"association\" …?)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xB,
        (
            "#01105F#5PHmm?\x01",
            "Lloyd, what's wrong?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#12PNo, nothing.\x02\x03",
            "#00008F……それよりKeya。\x01",
            "Really yesterday night, a weird guy\x01",
            "You are not seeing or are you?\x02\x03",
            "#00001FHe or she wearing pink clothes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#01112F#5PHmm……\x01",
            "I think that I have not seen it.\x02\x03",
            "#01106FKeya、寝ぼけてたみたいだから\x01",
            "I do not feel a bit confident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#12PI see……\x01",
            "No, that's fine.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xE, 0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 7)), scpexpr(EXPR_END)), "loc_4570")
    OP_C9(0x0, 0x80000000)

    NpcTalk(
        0xE,
        "Marybeleの声",
        "#3802V#2P#30WOh, were you here?\x02",
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    Jump("loc_459A")

    label("loc_4570")


    NpcTalk(
        0xE,
        "Daughter's voice",
        "#2POh, were you here?\x02",
    )

    CloseMessageWindow()

    label("loc_459A")

    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xB, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(2000, 5100, -7500, 4000)
    MoveCamera(147, 22, 0, 4000)

    def lambda_45E2():

        label("loc_45E2")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_45E2")

    QueueWorkItem2(0x101, 2, lambda_45E2)

    def lambda_45F4():

        label("loc_45F4")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_45F4")

    QueueWorkItem2(0xB, 2, lambda_45F4)
    BeginChrThread(0xE, 3, 0, 27)
    WaitChrThread(0xE, 3)
    EndChrThread(0x101, 0x2)
    EndChrThread(0xB, 0x2)
    OP_6F(0x79)

    ChrTalk(
        0xB,
        "#01110F#5POh, it's a bell.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#5PMarybeleさん。\x01",
            "Thank you very much.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4783")

    ChrTalk(
        0xE,
        (
            "#02902F#12PHello, thanks for your effort\x01",
            "You guys are.\x02\x03",
            "#02906FBut I wonder if it is \"association\".\x01",
            "There were also people who played around.\x02\x03",
            "#02903FSweep away my dolls#2RFurther#Also\x01",
            "It is a story that they are members!\x02\x03",
            "#02910FThis is a security system of the security department\x01",
            "I need to be thorough … …!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4841")

    label("loc_4783")


    ChrTalk(
        0xE,
        (
            "#02902F#12PHello, thanks for your effort\x01",
            "You guys are.\x02\x03",
            "#02906FBut I wonder if it is \"association\".\x01",
            "There were also people who played around.\x02\x03",
            "#02901FThis is a security system of the security department\x01",
            "I need to be thorough … …!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4841")


    ChrTalk(
        0x101,
        (
            "#00012F#5PThat's right.\x02\x03",
            "#00008F(Bear the hands of private security guards\x01",
            "I do not think he's a guy ……)\x02\x03",
            "#00013F(… after all our people\x01",
            "You need to be careful. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#02904F#12P─ ─ Well, anyway.\x02\x03",
            "#02900Fロイドさん、Keyaさん。\x02\x03",
            "Suddenly I thought,\x01",
            "Does not everyone take a commemorative photo?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xB, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00002F#5POh, good!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x101, 500)
    Sleep(100)

    ChrTalk(
        0xB,
        (
            "#01105F#5PWell, memorial photos,\x01",
            "Did you take it with everyone before?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xB, 500)
    Sleep(100)

    ChrTalk(
        0x101,
        (
            "#00004F#11POh, memories with everyone\x01",
            "I will leave it in the picture.\x02\x03",
            "#00000FLooking at it, I will have a vacation this time.\x01",
            "You can remember anytime.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0xB,
        "#01107F#4S#5PWell, I want to shoot!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#02909F#12PIt's a rule.\x02\x03",
            "#02905FThen …\x01",
            "Deck from inside the ship#4RHere#I wonder if it is better?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xE, 500)

    ChrTalk(
        0x101,
        (
            "#00009F#5PI agree.\x01",
            "It's fine weather.\x02\x03",
            "#00002FI will call on everyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#02904F#12PYes, please.\x02\x03",
            "#02902FAnd on board the ship\x01",
            "Please speak to a tour operator.\x02\x03",
            "If it is a commemorative photo service\x01",
            "It will be accepted soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#5PI understand.\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x19, 0x1F4)
    OP_68(3000, 5100, 0, 5000)
    MoveCamera(30, 25, 0, 5000)
    OP_6E(400, 5000)
    SetCameraDistance(22000, 5000)
    BeginChrThread(0x101, 3, 0, 28)

    def lambda_4C9B():

        label("loc_4C9B")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_4C9B")

    QueueWorkItem2(0xB, 2, lambda_4C9B)

    def lambda_4CAD():
        OP_93(0xFE, 0xA, 0x12C)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_4CAD)
    Sleep(1500)
    SetMessageWindowPos(250, 180, -1, -1)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0xB,
        "#01105F#3620V#30W#10A#11P#NAh\x02",
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
        "#01112F#40W#12P#N…………………………………….\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0xE,
        (
            "#02913F#3775V#12P#30W#NHehu ……\x02\x03",
            "#3776V── For important people\x01",
            "I do not want to worry too much.\x02\x03",
            "#02902F#3777VA good woman is a tough one, is not he?\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xEC1)
    OP_C9(0x1, 0x80000000)
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xB,
        "#01105F#12P#NIt is!\x02",
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
            "#02913F#3778V#5P#40W#30AIs there something to worry about?\x02\x03",
            "#02912F#3779V#35AIf it is me\x01",
            "It might be power.\x02",
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

    # Function_26_4065 end

    def Function_27_4FE5(): pass

    label("Function_27_4FE5")

    OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0xFFD3, 0x5DC, 0x7D0, 0x0)
    TurnDirection(0xFE, 0xB, 0)
    Return()

    # Function_27_4FE5 end

    def Function_28_500B(): pass

    label("Function_28_500B")

    OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0xFFE7, 0x1F40, 0x7D0, 0x1)
    OP_96(0xFE, 0xA50, 0x1004, 0x11C6, 0x7D0, 0x0)
    Sound(100, 0, 100, 0)
    OP_70(0x0, 0x5)
    OP_71(0x0, 0x0, 0x5, 0x0, 0x8)
    OP_79(0x0)

    def lambda_505B():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_505B)
    Sleep(300)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    WaitChrThread(0xFE, 1)
    Sound(100, 0, 100, 0)
    OP_71(0x0, 0x5, 0x0, 0x0, 0x8)
    OP_79(0x0)
    SetChrPos(0x101, 0, 0, 0, 0)
    Return()

    # Function_28_500B end

    SaveToFile()

Try(main)
