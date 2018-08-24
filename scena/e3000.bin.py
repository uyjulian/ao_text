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
        "Function_4_ABE",          # 04, 4
        "Function_5_D1C",          # 05, 5
        "Function_6_D3A",          # 06, 6
        "Function_7_1061",         # 07, 7
        "Function_8_11C1",         # 08, 8
        "Function_9_123E",         # 09, 9
        "Function_10_2870",        # 0A, 10
        "Function_11_2890",        # 0B, 11
        "Function_12_28B0",        # 0C, 12
        "Function_13_312F",        # 0D, 13
        "Function_14_32C1",        # 0E, 14
        "Function_15_3F68",        # 0F, 15
        "Function_16_3F7F",        # 10, 16
        "Function_17_4003",        # 11, 17
        "Function_18_4029",        # 12, 18
        "Function_19_4040",        # 13, 19
        "Function_20_4066",        # 14, 20
        "Function_21_4093",        # 15, 21
        "Function_22_40A5",        # 16, 22
        "Function_23_40B0",        # 17, 23
        "Function_24_40CF",        # 18, 24
        "Function_25_40EE",        # 19, 25
        "Function_26_4201",        # 1A, 26
        "Function_27_5266",        # 1B, 27
        "Function_28_528C",        # 1C, 28
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
    Jump("loc_ABA")

    label("loc_486")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_494")
    Jump("loc_ABA")

    label("loc_494")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_4A4")
    Jump("loc_ABA")

    label("loc_4A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_4B2")
    Jump("loc_ABA")

    label("loc_4B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_4C0")
    Jump("loc_ABA")

    label("loc_4C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_4CE")
    Jump("loc_ABA")

    label("loc_4CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_4DC")
    Jump("loc_ABA")

    label("loc_4DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_4EA")
    Jump("loc_ABA")

    label("loc_4EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_ABA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15A, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A36")

    ChrTalk(
        0x8,
        (
            "#00204F*ahem*. Anyway, I hope we\x01",
            "enjoy our first day off in a\x01",
            "long time today.\x02\x03",
            "#00200FLast time we investigated\x01",
            "that "auction" and had hardly\x01",
            "any time to enjoy ourselves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FYou're certainly right\x01",
            "about that. This our first\x01",
            "trip to Michelam for fun.\x02\x03",
            "#00009FHaha. You must be looking\x01",
            "forward to the theme park,\x01",
            "I guess?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#00204FOf course.\x02\x03",
            "Michelam Wonderland...\x02\x03",
            "―MWL for short.\x02\x03",
            "#00202FI'm looking forward to\x01",
            "meeting Mishy.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 4)), scpexpr(EXPR_END)), "loc_8F1")
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00004F...By the way, um. That\x01",
            "promise, do you remember it?\x02\x03",
            "#00002FAfter the cult incident, I said\x01",
            "we'd look for a chance and\x01",
            "visit the theme park together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#00204F...Of course I remember.\x02\x03",
            "First with the support\x01",
            "section... And after that,\x01",
            "with just you and I.\x02\x03",
            "#00200FIn a way, you could say with\x01",
            "this invitation, we've finally\x01",
            "reached the first phase.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHaha. I don't get that\x01",
            "expression, but...\x02\x03",
            "#00000FWe'll definitely come\x01",
            "again soon, just the two\x01",
            "of us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#00209FHaha... I'm looking\x01",
            "forward to it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A2E")

    label("loc_8F1")


    ChrTalk(
        0x101,
        (
            "#00004FYou're particularly\x01",
            "knowledgeable about\x01",
            "Mishy, Tio.\x02\x03",
            "#00002FWill you teach me about\x01",
            "him when we get to the\x01",
            "theme park?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#00204F...Roger.\x02\x03",
            "#00202FBut first, I have to drill things\x01",
            "like secret of Mishy's birth and his\x01",
            "family structure into your head...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FN-No, there's no need to\x01",
            "go that far.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A2E")

    SetScenarioFlags(0x15A, 0)
    Jump("loc_ABA")

    label("loc_A36")


    ChrTalk(
        0x8,
        (
            "#00202FI'll tell you all about\x01",
            "Mishy once we get to the\x01",
            "theme park.\x02\x03",
            "#00204FFor now, I think you\x01",
            "should speak with the\x01",
            "others.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ABA")

    TalkEnd(0xFE)
    Return()

    # Function_3_475 end

    def Function_4_ABE(): pass

    label("Function_4_ABE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_ACF")
    Jump("loc_D18")

    label("loc_ACF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_ADD")
    Jump("loc_D18")

    label("loc_ADD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_AEB")
    Jump("loc_D18")

    label("loc_AEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_AF9")
    Jump("loc_D18")

    label("loc_AF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_B07")
    Jump("loc_D18")

    label("loc_B07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_B15")
    Jump("loc_D18")

    label("loc_B15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_B23")
    Jump("loc_D18")

    label("loc_B23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_D18")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CBB")
    OP_4B(0x8, 0xFF)

    ChrTalk(
        0x9,
        "#01203FGrrrowl... Woof.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 500)

    ChrTalk(
        0x8,
        (
            "#00204FHonestly, what a handful\x01",
            "of a leader, he says.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FHaha. That hurts, coming\x01",
            "from Zeit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#00211FHe also says "he's too\x01",
            "thick headed" and "be a\x01",
            "little more thoughtful."\x02",
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
            "#00006F...Hey, aren't those\x01",
            "kind of subjective?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#00203FI don't know what you're\x01",
            "talking about.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x5A, 0x0)
    SetScenarioFlags(0x0, 4)
    OP_4C(0x8, 0xFF)
    Jump("loc_D18")

    label("loc_CBB")


    ChrTalk(
        0x9,
        "#01203F...Grrowl...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F(I wonder if Zeit's\x01",
            "looking forward to\x01",
            "Michelam too...)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D18")

    TalkEnd(0xFE)
    Return()

    # Function_4_ABE end

    def Function_5_D1C(): pass

    label("Function_5_D1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D33")
    Call(0, 14)
    Return()

    label("loc_D33")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_5_D1C end

    def Function_6_D3A(): pass

    label("Function_6_D3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D51")
    Call(0, 12)
    Return()

    label("loc_D51")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_D62")
    Jump("loc_105D")

    label("loc_D62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_D70")
    Jump("loc_105D")

    label("loc_D70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_D7E")
    Jump("loc_105D")

    label("loc_D7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_D8C")
    Jump("loc_105D")

    label("loc_D8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_D9A")
    Jump("loc_105D")

    label("loc_D9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_DA8")
    Jump("loc_105D")

    label("loc_DA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_DB6")
    Jump("loc_105D")

    label("loc_DB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_105D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DCE")
    Jump("loc_105D")

    label("loc_DCE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F95")

    ChrTalk(
        0xA,
        (
            "#10304FAlright then. It's been a while since\x01",
            "I came outside of my host job, so I'm\x01",
            "going to rest my wings today, I guess.\x02\x03",
            "#10300FI'll head to the restaurant at some\x01",
            "point. Want to join me for drinks?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F...Now look here. I feel like I've said\x01",
            "it a million times, but I can't approve\x01",
            "of a minor drinking, now can I.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#10309FHehe. Why so strict? Cut\x01",
            "loose a little more.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FStrict or not, that's\x01",
            "not the point.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_105D")

    label("loc_F95")


    ChrTalk(
        0xA,
        (
            "#10309FWhy so strict? Cut loose a little\x01",
            "more, you.\x02\x03",
            "#10302FIf you like, how about I teach\x01",
            "you a host's basic techniques for\x01",
            "making girls fall for you, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FD-Don't try to bribe\x01",
            "me...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_105D")

    TalkEnd(0xFE)
    Return()

    # Function_6_D3A end

    def Function_7_1061(): pass

    label("Function_7_1061")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_11BD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1138")

    ChrTalk(
        0xC,
        (
            "Everyone in the city was\x01",
            "talking about "independence"\x01",
            "or something for some reason.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Because we came from out of\x01",
            "state, we don't really get it,\x01",
            "but... Is it something serious?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_11BD")

    label("loc_1138")


    ChrTalk(
        0xC,
        (
            "I wonder what this\x01",
            ""independence" the city\x01",
            "folk were talking about.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I don't really get it,\x01",
            "but... Is it something\x01",
            "serious?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11BD")

    TalkEnd(0xFE)
    Return()

    # Function_7_1061 end

    def Function_8_11C1(): pass

    label("Function_8_11C1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_123A")

    ChrTalk(
        0xD,
        (
            "Hey hey, more importantly,\x01",
            "isn't that one sitting in\x01",
            "front cute?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Should we pick him up?\x01",
            "Should we?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_123A")

    TalkEnd(0xFE)
    Return()

    # Function_8_11C1 end

    def Function_9_123E(): pass

    label("Function_9_123E")

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
            "#30WIt was two weeks after the trade conference─\x01",
            "Crossbell City was enveloped in a quiet enthusiasm.\x02\x03",
            "The other autonomous states of Lｳman, Ored and North Ambria,\x01",
            "having been recognized by the Holy Nation of Arteria, were\x01",
            "seen as having sovereignty equal to that of a nation.\x02\x03",
            "However, Crossbell State was acknowledged only as a buffer\x01",
            "zone between the Empire and Republic.\x02\x03",
            "(Incidentally, a 10% tax was assessed by both the Empire and\x01",
            "Republic under the guise of an "occupation fee".)\x02\x03",
            "The more Crossbell grew as a trade and finance center, the\x01",
            "more its political foundation weakened.\x02\x03",
            "Which in turn brought interference from foreign nations and\x01",
            "crime syndicates to Crossbell.\x02\x03",
            "Mayor Dieter's bold proposal, "independence as a sovereign\x01",
            "nation" to defeat that crooked situation, resonated with\x01",
            "many.\x02\x03",
            "Many were also concerned with the intentions of the major\x01",
            "powers. And so, arguments over "independence" broke out here\x01",
            "and there.\x02",
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
            "#00006F#5P#30W...*sigh*...\x02\x03",
            "#00008FIt's no good... It's\x01",
            "been almost half a month\x01",
            "since then, and yet...\x02",
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
            "What should a leader do in\x01",
            "times like these?\x02\x03",
            "Randy of course, but also Elie\x01",
            "and Noｱl seem to be thinking\x01",
            "about a lot of things...\x02\x03",
            "#00006F...It seems to be making KeA\x01",
            "worry too.\x02",
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
            "#3060V#40WGrrrrrowl... Woof.\x02",
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
            "#00005F#11P#30WUmm... Are you saying\x01",
            "something?\x02\x03",
            "#00012FHaha, sorry. I'm being\x01",
            "weird...\x02",
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
            "#2674V#5P#N#30W#35AIn times like these,\x01",
            "don't think logically.\x02\x03",
            "#2675V#25ASimply speak your mind.\x02\x03",
            "#4108V#N#15A─He says.\x02",
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

    def lambda_1CB6():

        label("loc_1CB6")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_1CB6")

    QueueWorkItem2(0x101, 2, lambda_1CB6)
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
            "We rarely get vacations so I'm glad\x01",
            "the weather is nice today.\x02",
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
            "#00004F#5PThat reminds me...\x02\x03",
            "#00000FI wondered what was\x01",
            "going on when Mariabell\x01",
            "invited us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#00202F#5PHaha, did you think it\x01",
            "was some kind of trap?\x02\x03",
            "It seems she still sees\x01",
            "you as a bit of a\x01",
            "threat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#5PHaha. Actually, I\x01",
            "thought about that a\x01",
            "bit.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00006F#5P...Sorry to you too,\x01",
            "Tio.\x02\x03",
            "#00008FYou just got back and\x01",
            "had to see me in this\x01",
            "pathetic state.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#00206F#5P...I think it's only\x01",
            "natural.\x02\x03",
            "#00208FYou saw so many pass\x01",
            "away right in front of\x01",
            "you...\x02\x03",
            "#00200FAnyone would be shocked.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#5PWell, having become a\x01",
            "detective, I thought I\x01",
            "was prepared for it.\x02\x03",
            "#00001F...After the Joachim case\x01",
            "I'd even gotten used to\x01",
            "it somehow, but...\x02\x03",
            "#00006FIt seems I was\x01",
            "unprepared. As both a\x01",
            "detective and a leader.\x02",
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
            "#00200F#11P─Being used to something\x01",
            "and being prepared aren't\x01",
            "all that related, right?\x02\x03",
            "If you say that, then\x01",
            "someone like me is fully\x01",
            "prepared.\x02\x03",
            "#00203FAfter me, Randy is\x01",
            "probably the most "used"\x01",
            "to death.\x02",
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
            "#00206F#11PHowever, I'm nowhere near as\x01",
            "qualified to be a detective\x01",
            "as you are, Lloyd...\x02\x03",
            "Nor as qualified to be a\x01",
            "leader, of course.\x02\x03",
            "#00201F─I think everyone is looking\x01",
            "for something different from\x01",
            "you, most likely.\x02",
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
            "#00006F#6P...Yeah. You might be\x01",
            "right about that.\x02\x03",
            "#00008FLooks like I mistook the\x01",
            "shock I suffered with\x01",
            "lack of preparation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#00204F#11PThen please, go.\x02\x03",
            "#00202FYou don't get a vacation\x01",
            "with all of us every\x01",
            "day...\x02\x03",
            "Isn't it your duty as\x01",
            "leader to make sure\x01",
            "everyone enjoys it?\x02",
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
            "#00000FI'll have a little chat\x01",
            "with the others.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#00206F#11PR-Right. That's a good\x01",
            "idea.\x02\x03",
            "#00208F#30W...But... Uhm...\x02",
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
        "#00205F#11P#40W...Oh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#6PHaha. I wasn't trying to\x01",
            "treat you like a child,\x01",
            "I wanted to thank you...\x02",
        )
    )

    CloseMessageWindow()
    OP_A1(0x8, 0x5DC, 0x3, 0x7, 0x8, 0x9)

    ChrTalk(
        0x8,
        (
            "#00206F#11PNo, don't worry about\x01",
            "it.\x02\x03",
            "#00208F#30WActually it was kind\x01",
            "of...\x02",
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
        "#00201F#11P...It's nothing!\x02",
    )

    CloseMessageWindow()
    OP_A1(0x8, 0x5DC, 0x2, 0xC, 0xD)

    ChrTalk(
        0x8,
        (
            "#00203F#11PPlease, quickly go to\x01",
            "the others.\x02",
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
        "#01203F#6P#30WGrrrrowl... (oh brother)\x02",
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

    # Function_9_123E end

    def Function_10_2870(): pass

    label("Function_10_2870")

    SetChrFlags(0xFE, 0x2)
    SetChrChipByIndex(0xFE, 0x1E)
    OP_A1(0xFE, 0x3E8, 0x3, 0x0, 0x1, 0x2)
    OP_A1(0xFE, 0x3E8, 0x7, 0x2, 0x3, 0x4, 0x5, 0x4, 0x3, 0x2)
    Return()

    # Function_10_2870 end

    def Function_11_2890(): pass

    label("Function_11_2890")

    SetChrFlags(0xFE, 0x2)
    SetChrChipByIndex(0xFE, 0x1F)
    OP_A1(0xFE, 0x3E8, 0x3, 0x0, 0x1, 0x2)
    OP_A1(0xFE, 0x3E8, 0x7, 0x2, 0x3, 0x4, 0x5, 0x4, 0x3, 0x2)
    Return()

    # Function_11_2890 end

    def Function_12_28B0(): pass

    label("Function_12_28B0")

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
            "#30W─Hey, Lloyd.\x02\x03",
            "Here to give me a pep talk?\x02",
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
            "#00012F#6PHaha, I guess.\x02\x03",
            "#00000F...But you look fine,\x01",
            "right Wazy?\x02\x03",
            "I could say you're cool\x01",
            "as always.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#10304F#5PWell, that's my selling\x01",
            "point, after all.\x02\x03",
            "#10308FAnd, it's not the case\x01",
            "that I haven't witnessed\x01",
            "pointless killing.\x02\x03",
            "#10303FThat was before I came\x01",
            "to Crossbell though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008F#6PIs that right...\x02\x03",
            "#00005F...Hey, that's the first\x01",
            "time I've heard you talk\x01",
            "about your past.\x02\x03",
            "#00000FI think I heard that you\x01",
            "aren't from Crossbell\x01",
            "somewhere, though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#10309F#5PHehe, I guess that's a\x01",
            "trade secret.\x02\x03",
            "#10300FBut... I've lived in\x01",
            "slums before, too.\x02\x03",
            "A trash heap far more\x01",
            "hopeless than Downtown,\x01",
            "you know.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x6F), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2CCE")

    ChrTalk(
        0x101,
        (
            "#00006F#6P...I see...\x02\x03",
            "#00008FSully of Arc-en-Ciel\x01",
            "seems to be from a far-\x01",
            "away slum as well...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D38")

    label("loc_2CCE")


    ChrTalk(
        0x101,
        (
            "#00006F#6P...I see...\x02\x03",
            "#00008FThat Arc-en-Ciel newcomer\x01",
            "seems to be from a far-\x01",
            "away slum as well...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D38")


    ChrTalk(
        0xA,
        (
            "#10305F#5PAh, that North Ambria girl,\x01",
            "right?\x02\x03",
            "#10306FIt's awful there... They barely\x01",
            "scrape by on the money their\x01",
            "jaegers make outside the country.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#6PYeah, I heard the\x01",
            "rumors, but...\x02\x03",
            "#00005F...Hey, you talk as if\x01",
            "you've been there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#10304F#5PHehe, I wonder.\x02\x03",
            "#10308F#30W............\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F#6P???\x02\x03",
            "#00003FI said you looked fine,\x01",
            "but you look a little\x01",
            "out of it...\x02\x03",
            "#00001F...Did something happen?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#10304F#5PTo me, not really.\x02\x03",
            "#10300FIt's just, it looks like\x01",
            "the Vipers have a lot\x01",
            "going on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001F#6PThe Vipers... You mean\x01",
            "Wald and the others.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#10304F#5PWell, since I left the way I\x01",
            "did, they're probably a bit\x01",
            "curious.\x02\x03",
            "#10302FAfter all, I'm a cool beauty\x01",
            "whose mysterious charisma is\x01",
            "his selling point.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#6PDon't talk about\x01",
            "yourself like that...\x02\x03",
            "#00008F...But I'm a little\x01",
            "worried about Wald too.\x02\x03",
            "#00000FLet's go check on him\x01",
            "when we have some free\x01",
            "time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#10304F#5PHehe. That would help me\x01",
            "out as well, I guess.\x02",
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

    # Function_12_28B0 end

    def Function_13_312F(): pass

    label("Function_13_312F")

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
            "#00002F#5P(KeA... I wondered where\x01",
            "she was.)\x02\x03",
            "#00006F(...I must have worried\x01",
            "her a bit.)\x02",
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

    # Function_13_312F end

    def Function_14_32C1(): pass

    label("Function_14_32C1")

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
        "#00002F#6PKeA, so here you are.\x02",
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
            "#3611V#40WAh... Lloyd...\x02\x03",
            "#3612V#30WEhehe... Will we be there soon?\x02",
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
            "#00004F#6PYeah, in a little bit.\x02\x03",
            "#00000FThere's a theme park there\x01",
            "too, so let's enjoy it\x01",
            "when we get there, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#01102F#11PYeah!\x02\x03",
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
            "#00006F#6P...Sorry, KeA.\x02\x03",
            "#00008FLately, I've made you\x01",
            "feel so lonely...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#01121F#11P...Uh-uh. I'm totally fine.\x02\x03",
            "#01106FI don't know the details,\x01",
            "but... I get that everyone's\x01",
            "feeling down for some reason...\x02\x03",
            "#01108FKeA wanted to cheer everyone up\x01",
            "too...\x02\x03",
            "But in the end, she couldn't do\x01",
            "anything...\x02",
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
        "#01105F#11PAh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#6PYou're cheering us up\x01",
            "plenty.\x02\x03",
            "#00002FBy staying by our side,\x01",
            "KeA...\x02\x03",
            "How much strength and\x01",
            "energy do you think that\x01",
            "gives us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#01105F#11PReally?\x02\x03",
            "#01108F...I wonder if that's\x01",
            "really true...\x02",
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
            "#01109F#11P...Ehehe. Somehow I\x01",
            "don't get it anymore.\x02\x03",
            "#01105FAh, but it looks like\x01",
            "everyone cheered up a\x01",
            "little, huh.\x02\x03",
            "#01104FEhehe. I always knew you\x01",
            "were amazing, Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#6PUh, I don't think I\x01",
            "really did anything,\x01",
            "but...\x02\x03",
            "#00002FSince we're here, let's\x01",
            "enjoy ourselves to the\x01",
            "fullest.\x02\x03",
            "I bet you're really\x01",
            "looking forward to the\x01",
            "theme park, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_A1(0xB, 0x4B0, 0x4, 0x8, 0x9, 0x8, 0x3)

    ChrTalk(
        0xB,
        "#01109F#11PYeah!\x02",
    )

    CloseMessageWindow()
    OP_A1(0xB, 0x4B0, 0x6, 0xB, 0xC, 0xD, 0xE, 0xD, 0xC)

    ChrTalk(
        0xB,
        (
            "#01110F#11PKeA wants to ride on the\x01",
            "ferris wheel!\x02\x03",
            "After, I want to "Kick\x01",
            "Mishy" with Tio, too!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00011F#6PKick Mishy, she said...\x01",
            "Is that what kids are\x01",
            "into these days?\x02\x03",
            "#00012FHmm, but Tio seems to be\x01",
            "a little over the age\x01",
            "limit.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x103,
        (
            "#00211F#6P#N─I intend to mind my\x01",
            "manners in that regard.\x02",
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
        (
            "#00005F#5PTio, and everyone else,\x01",
            "too...\x02",
        )
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
            "#00109F#12P*giggle*. We all met up\x01",
            "somehow...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#12PAnd, it looks like we're\x01",
            "arriving soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002F#5PYeah, I see.\x02",
    )

    CloseMessageWindow()

    def lambda_3D53():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3D53)
    Sleep(50)

    def lambda_3D63():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3D63)
    Sleep(50)

    def lambda_3D73():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_3D73)
    Sleep(50)

    def lambda_3D83():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_3D83)
    Sleep(50)

    def lambda_3D93():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_3D93)
    Sleep(50)

    def lambda_3DA3():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_3DA3)
    Sleep(50)

    def lambda_3DB3():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_3DB3)
    Sleep(50)
    SetChrFlags(0x9, 0x20)

    def lambda_3DC8():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_3DC8)
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
            "#10109F#6P#NToday's weather is\x01",
            "perfect!\x02",
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

    # Function_14_32C1 end

    def Function_15_3F68(): pass

    label("Function_15_3F68")

    OP_9B(0x0, 0xFE, 0x0, 0x15E0, 0x898, 0x0)
    TurnDirection(0xFE, 0x101, 500)
    Return()

    # Function_15_3F68 end

    def Function_16_3F7F(): pass

    label("Function_16_3F7F")

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

    # Function_16_3F7F end

    def Function_17_4003(): pass

    label("Function_17_4003")

    OP_9B(0x0, 0xFE, 0x0, 0x1D4C, 0x898, 0x1)
    OP_9B(0x0, 0xFE, 0xFFC4, 0x7D0, 0x898, 0x0)
    TurnDirection(0xFE, 0x101, 500)
    Return()

    # Function_17_4003 end

    def Function_18_4029(): pass

    label("Function_18_4029")

    OP_9B(0x0, 0xFE, 0x0, 0x2008, 0x898, 0x0)
    TurnDirection(0xFE, 0x101, 500)
    Return()

    # Function_18_4029 end

    def Function_19_4040(): pass

    label("Function_19_4040")

    OP_9B(0x0, 0xFE, 0x0, 0x21FC, 0x898, 0x1)
    OP_9B(0x0, 0xFE, 0xFFD3, 0x320, 0x898, 0x0)
    TurnDirection(0xFE, 0x101, 500)
    Return()

    # Function_19_4040 end

    def Function_20_4066(): pass

    label("Function_20_4066")

    OP_9B(0x0, 0xFE, 0x0, 0x238C, 0x898, 0x1)
    OP_9B(0x0, 0xFE, 0xF, 0x640, 0x898, 0x0)
    OP_93(0xFE, 0x87, 0x1F4)
    TurnDirection(0xFE, 0xB, 500)
    Return()

    # Function_20_4066 end

    def Function_21_4093(): pass

    label("Function_21_4093")

    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(1500)
    OP_93(0xFE, 0x13B, 0x1F4)
    Return()

    # Function_21_4093 end

    def Function_22_40A5(): pass

    label("Function_22_40A5")

    Sleep(1000)
    OP_93(0xFE, 0x13B, 0x1F4)
    Return()

    # Function_22_40A5 end

    def Function_23_40B0(): pass

    label("Function_23_40B0")

    SetChrFlags(0xFE, 0x2)
    SetChrChipByIndex(0xFE, 0x20)
    OP_A1(0xFE, 0x3E8, 0x3, 0x1, 0x2, 0x3)
    OP_A1(0xFE, 0x3E8, 0x6, 0x4, 0x5, 0x6, 0x5, 0x4, 0x3)
    Return()

    # Function_23_40B0 end

    def Function_24_40CF(): pass

    label("Function_24_40CF")

    SetChrFlags(0xFE, 0x2)
    SetChrChipByIndex(0xFE, 0x21)
    OP_A1(0xFE, 0x3E8, 0x3, 0x1, 0x2, 0x3)
    OP_A1(0xFE, 0x3E8, 0x6, 0x4, 0x5, 0x6, 0x5, 0x4, 0x3)
    Return()

    # Function_24_40CF end

    def Function_25_40EE(): pass

    label("Function_25_40EE")

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

    # Function_25_40EE end

    def Function_26_4201(): pass

    label("Function_26_4201")

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
        "#01104F#3619V#5P#30W#15AHmm, hm hmm...♪\x02",
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    Sleep(300)
    TurnDirection(0x101, 0xB, 500)
    Sleep(150)

    ChrTalk(
        0x101,
        (
            "#00012F#12PHaha... You're in a good\x01",
            "mood, KeA.\x02\x03",
            "#00002FSomehow many things\x01",
            "happened, but... Did you\x01",
            "enjoy it?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x101, 500)

    ChrTalk(
        0xB,
        (
            "#01109F#5PYeah!\x02\x03",
            "#01110FI want to go out with\x01",
            "everyone again!\x02\x03",
            "Maybe to Armorica\x01",
            "Village next time...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#12PHaha, that might be nice.\x02\x03",
            "#00004F(...Based on how she was\x01",
            "acting last night, I thought\x01",
            "something happened, but...)\x02\x03",
            "(She looks completely\x01",
            "fine... Maybe I shouldn't\x01",
            "worry so much?)\x02\x03",
            "#00008F(Rather, I should worry\x01",
            "about Ouroboros' actions...)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xB,
        "#01105F#5PHm? Lloyd, what's wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#12PNo, it's nothing.\x02\x03",
            "#00008F...More importantly, KeA.\x01",
            "Did you really not see a\x01",
            "weird guy last night?\x02\x03",
            "#00001FSomeone who wore a pink\x01",
            "colored outfit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#01112F#5PHmmm... I don't think I\x01",
            "saw him.\x02\x03",
            "#01106FBut KeA was half asleep,\x01",
            "so she isn't very sure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#12PI see... Well, it\x01",
            "doesn't matter then.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xE, 0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 7)), scpexpr(EXPR_END)), "loc_4745")
    OP_C9(0x0, 0x80000000)

    NpcTalk(
        0xE,
        "Mariabell's Voice",
        (
            "#3802V#2P#30WMy, so this is where you\x01",
            "were.\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    Jump("loc_4779")

    label("loc_4745")


    NpcTalk(
        0xE,
        "Girl's Voice",
        (
            "#2PMy, so this is where you\x01",
            "were.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4779")

    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xB, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(2000, 5100, -7500, 4000)
    MoveCamera(147, 22, 0, 4000)

    def lambda_47C1():

        label("loc_47C1")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_47C1")

    QueueWorkItem2(0x101, 2, lambda_47C1)

    def lambda_47D3():

        label("loc_47D3")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_47D3")

    QueueWorkItem2(0xB, 2, lambda_47D3)
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
            "#00002F#5PMariabell, thank you for\x01",
            "your hard work.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4963")

    ChrTalk(
        0xE,
        (
            "#02902F#12PHuhu, it's all of you who\x01",
            "work hard, am I right?\x02\x03",
            "#02906FStill, Ouroboros, was it\x01",
            "called? To think there\x01",
            "were jokers amongst them.\x02\x03",
            "#02903FOne of their members\x01",
            "kidnapped my dolls too!\x02\x03",
            "#02910FThe Security Department's\x01",
            "measures need to be\x01",
            "thorough!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A36")

    label("loc_4963")


    ChrTalk(
        0xE,
        (
            "#02902F#12PHuhu, it's all of you who\x01",
            "work hard, am I right?\x02\x03",
            "#02906FStill, Ouroboros, was it\x01",
            "called? To think there\x01",
            "were jokers amongst them.\x02\x03",
            "#02901FThe Security Department's\x01",
            "measures need to be\x01",
            "thorough!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A36")


    ChrTalk(
        0x101,
        (
            "#00012F#5PY-You're right...\x02\x03",
            "#00008F(Though I don't think he's\x01",
            "anyone a private security\x01",
            "guard could handle...)\x02\x03",
            "#00013F(...As I thought, we're\x01",
            "the ones who need to be\x01",
            "careful.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#02904F#12P─Well, that aside.\x02\x03",
            "#02900FLloyd, KeA.\x02\x03",
            "It just occurred to me, but why\x01",
            "don't you take a commemorative\x01",
            "picture with everyone?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xB, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00002F#5PYeah, great idea!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x101, 500)
    Sleep(100)

    ChrTalk(
        0xB,
        (
            "#01105F#5PEhm, did you take a\x01",
            ""commemorative picture"\x01",
            "with everyone before?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xB, 500)
    Sleep(100)

    ChrTalk(
        0x101,
        (
            "#00004F#11PYeah, it's to save all\x01",
            "of our memories together\x01",
            "in a picture, see?\x02\x03",
            "#00000FAnd whenever you look at\x01",
            "it, it'll remind you of\x01",
            "our vacation.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0xB,
        "#01107F#4S#5PYeah, I wanna take one!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#02909F#12PYou heard her.\x02\x03",
            "#02905FIn that case... Would here\x01",
            "on the deck be better than\x01",
            "inside the ship?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xE, 500)

    ChrTalk(
        0x101,
        (
            "#00009F#5PYou're right. And\x01",
            "there's good weather\x01",
            "today too.\x02\x03",
            "#00002FI'll go call everyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#02904F#12PYes, please do.\x02\x03",
            "#02902FAlso, please get the tour\x01",
            "guide inside for me.\x02\x03",
            "Commemorative pictures are\x01",
            "free of charge. She will\x01",
            "take it for you immediately.\x02",
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

    def lambda_4EEF():

        label("loc_4EEF")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_4EEF")

    QueueWorkItem2(0xB, 2, lambda_4EEF)

    def lambda_4F01():
        OP_93(0xFE, 0xA, 0x12C)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_4F01)
    Sleep(1500)
    SetMessageWindowPos(250, 180, -1, -1)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0xB,
        "#01105F#3620V#30W#10A#11P#NAh─\x02",
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
            "#02913F#3775V#12P#30W#NHaha...\x02\x03",
            "#3776V─You don't want to cause\x01",
            "unnecessary worries to the\x01",
            "people important to you.\x02\x03",
            "#02902F#3777VBeing a good woman is\x01",
            "hard, eh?\x02",
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
            "#02913F#3778V#5P#40W#30AYou are troubled by\x01",
            "something, right?\x02\x03",
            "#02912F#3779V#35A─If you are fine with\x01",
            "me, I may be able to be\x01",
            "of some help.\x02",
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

    # Function_26_4201 end

    def Function_27_5266(): pass

    label("Function_27_5266")

    OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0xFFD3, 0x5DC, 0x7D0, 0x0)
    TurnDirection(0xFE, 0xB, 0)
    Return()

    # Function_27_5266 end

    def Function_28_528C(): pass

    label("Function_28_528C")

    OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0xFFE7, 0x1F40, 0x7D0, 0x1)
    OP_96(0xFE, 0xA50, 0x1004, 0x11C6, 0x7D0, 0x0)
    Sound(100, 0, 100, 0)
    OP_70(0x0, 0x5)
    OP_71(0x0, 0x0, 0x5, 0x0, 0x8)
    OP_79(0x0)

    def lambda_52DC():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_52DC)
    Sleep(300)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    WaitChrThread(0xFE, 1)
    Sound(100, 0, 100, 0)
    OP_71(0x0, 0x5, 0x0, 0x0, 0x8)
    OP_79(0x0)
    SetChrPos(0x101, 0, 0, 0, 0)
    Return()

    # Function_28_528C end

    SaveToFile()

Try(main)
