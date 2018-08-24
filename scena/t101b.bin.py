from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t101b.bin",                # FileName
        "t101b",                    # MapName
        "t101b",                    # Location
        0x0045,                     # MapIndex
        "ed7513",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x02,                       # PlaceNameNumber
        0x1A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 69, 0, 2, 0, 3],
    )

    BuildStringList((
        "t101b",                  # 0
        "Amy",                    # 1
        "Zell",                   # 2
        "Cabilan",                # 3
        "Loogman",                # 4
        "Zeit",                   # 5
        "Cecil",                  # 6
        "Ilya",                   # 7
        "To Guest House",         # 8
        "To Hotel Delphinia",     # 9
    ))

    AddCharChip((
        "chr/ch22300.itc",                   # 00
        "chr/ch22200.itc",                   # 01
        "chr/ch33100.itc",                   # 02
        "chr/ch33000.itc",                   # 03
        "chr/ch02708.itc",                   # 04
        "chr/ch07502.itc",                   # 05
    ))

    DeclNpc(4294964546, 4294965296, 33099,   180,  389,  0x0, 0,   0,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(4294964546, 4294965296, 31899,   0,    389,  0x0, 0,   1,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(26860,   4294965296, 2200,    270,  385,  0x0, 0,   2,   0,   0,   1,   0,   9,   255,  0)
    DeclNpc(4294960367, 4294965497, 52110,   45,   389,  0x0, 0,   3,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(4294964126, 4294963497, 4294953937, 135,  405,  0x0, 0,   4,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(4294965377, 4294963596, 4294954866, 180,  389,  0x0, 0,   5,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    PlaceName(-5.0, 0.0, 81.0, 0x0000, 0x0000, "To Guest House")
    PlaceName(65.0, 0.0, 0.0, 0x0000, 0x0000, "To Hotel Delphinia")

    ChipFrameInfo(456, 0)                                        # 0

    ScpFunction((
        "Function_0_1C8",          # 00, 0
        "Function_1_280",          # 01, 1
        "Function_2_2E1",          # 02, 2
        "Function_3_39E",          # 03, 3
        "Function_4_3C6",          # 04, 4
        "Function_5_44B",          # 05, 5
        "Function_6_500",          # 06, 6
        "Function_7_5C8",          # 07, 7
        "Function_8_6DA",          # 08, 8
        "Function_9_777",          # 09, 9
        "Function_10_98B",         # 0A, 10
        "Function_11_AF5",         # 0B, 11
    ))


    def Function_0_1C8(): pass

    label("Function_0_1C8")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_208"),
        (1, "loc_214"),
        (2, "loc_220"),
        (3, "loc_22C"),
        (4, "loc_238"),
        (5, "loc_244"),
        (6, "loc_250"),
        (SWITCH_DEFAULT, "loc_25C"),
    )


    label("loc_208")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_268")

    label("loc_214")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_268")

    label("loc_220")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_268")

    label("loc_22C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_268")

    label("loc_238")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_268")

    label("loc_244")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_268")

    label("loc_250")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_268")

    label("loc_25C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_268")

    label("loc_268")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_27F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_268")

    label("loc_27F")

    Return()

    # Function_0_1C8 end

    def Function_1_280(): pass

    label("Function_1_280")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2E0")
    OP_95(0xFE, 26860, -2000, 2200, 2000, 0x0)
    OP_95(0xFE, -4019, -1800, 2200, 2000, 0x0)
    OP_95(0xFE, -3510, -1800, -1500, 2000, 0x0)
    OP_95(0xFE, 26860, -2000, -2060, 2000, 0x0)
    Jump("Function_1_280")

    label("loc_2E0")

    Return()

    # Function_1_280 end

    def Function_2_2E1(): pass

    label("Function_2_2E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_2EF")
    Jump("loc_39D")

    label("loc_2EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 7)), scpexpr(EXPR_END)), "loc_2FD")
    Jump("loc_39D")

    label("loc_2FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_34E")
    ClearChrFlags(0xC, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15A, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32B")
    ClearChrFlags(0xD, 0x80)
    SetChrChipByIndex(0xD, 0x5)
    SetChrSubChip(0xD, 0x0)
    EndChrThread(0xD, 0x0)
    SetChrBattleFlags(0xD, 0x4)

    label("loc_32B")

    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x10)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x10)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    Jump("loc_39D")

    label("loc_34E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_35C")
    Jump("loc_39D")

    label("loc_35C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_36A")
    Jump("loc_39D")

    label("loc_36A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_378")
    Jump("loc_39D")

    label("loc_378")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_386")
    Jump("loc_39D")

    label("loc_386")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_394")
    Jump("loc_39D")

    label("loc_394")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_39D")

    label("loc_39D")

    Return()

    # Function_2_2E1 end

    def Function_3_39E(): pass

    label("Function_3_39E")

    OP_52(0xC, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(126, 1, 80, 0)
    Return()

    # Function_3_39E end

    def Function_4_3C6(): pass

    label("Function_4_3C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15A, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3DD")
    Call(0, 11)
    Return()

    label("loc_3DD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_3EE")
    Jump("loc_447")

    label("loc_3EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_406")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15A, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_401")

    label("loc_401")

    Jump("loc_447")

    label("loc_406")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_414")
    Jump("loc_447")

    label("loc_414")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_422")
    Jump("loc_447")

    label("loc_422")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_430")
    Jump("loc_447")

    label("loc_430")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_43E")
    Jump("loc_447")

    label("loc_43E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_447")

    label("loc_447")

    TalkEnd(0xFE)
    Return()

    # Function_4_3C6 end

    def Function_5_44B(): pass

    label("Function_5_44B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15A, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_462")
    Call(0, 11)
    Return()

    label("loc_462")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_473")
    Jump("loc_4FC")

    label("loc_473")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_4AD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15A, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_48B")
    Jump("loc_4A8")

    label("loc_48B")


    ChrTalk(
        0xC,
        "#01200FGrrrowl... Woof.\x02",
    )

    CloseMessageWindow()

    label("loc_4A8")

    Jump("loc_4FC")

    label("loc_4AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_4BB")
    Jump("loc_4FC")

    label("loc_4BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_4C9")
    Jump("loc_4FC")

    label("loc_4C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_4D7")
    Jump("loc_4FC")

    label("loc_4D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_4E5")
    Jump("loc_4FC")

    label("loc_4E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_4F3")
    Jump("loc_4FC")

    label("loc_4F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_4FC")

    label("loc_4FC")

    TalkEnd(0xFE)
    Return()

    # Function_5_44B end

    def Function_6_500(): pass

    label("Function_6_500")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_5AD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_51E")
    Call(0, 7)
    Jump("loc_5A8")

    label("loc_51E")


    ChrTalk(
        0x8,
        (
            "Oh Zell... You're first\x01",
            "class only in\x01",
            "gentlemanly behavior.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "B-But nevertheless,\x01",
            "you're still far from\x01",
            "being an amazing husband.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A8")

    Jump("loc_5C4")

    label("loc_5AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_5BB")
    Jump("loc_5C4")

    label("loc_5BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_5C4")

    label("loc_5C4")

    TalkEnd(0xFE)
    Return()

    # Function_6_500 end

    def Function_7_5C8(): pass

    label("Function_7_5C8")

    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)

    ChrTalk(
        0x8,
        "Listen, Zell?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Like I told you at noon, you'll\x01",
            "do your best at studying and\x01",
            "sports from now on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I-I know that already.\x01",
            "I'm your fiancｳ, after\x01",
            "all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I don't know how it'll\x01",
            "turn out yet, but I'll\x01",
            "do my best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "............*blush*\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x10)
    SetScenarioFlags(0x0, 2)
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    Return()

    # Function_7_5C8 end

    def Function_8_6DA(): pass

    label("Function_8_6DA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_75C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6F8")
    Call(0, 7)
    Jump("loc_757")

    label("loc_6F8")

    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)

    ChrTalk(
        0x9,
        (
            "Then, Amy. It's cold at\x01",
            "night, you have to stay\x01",
            "warm.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "I-I know that.\x02",
    )

    CloseMessageWindow()
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)

    label("loc_757")

    Jump("loc_773")

    label("loc_75C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_76A")
    Jump("loc_773")

    label("loc_76A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_773")

    label("loc_773")

    TalkEnd(0xFE)
    Return()

    # Function_8_6DA end

    def Function_9_777(): pass

    label("Function_9_777")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_962")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8DB")

    ChrTalk(
        0xA,
        (
            "Recently, I try to avoid\x01",
            "walking when it gets dark\x01",
            "as much as possible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Previously, when I was walking in the middle of\x01",
            "the night, I had a dreadful experience due to the\x01",
            "sudden appearance of the mafia's military dogs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "You guys should too. If you have\x01",
            "some business here, finish it\x01",
            "immediately and go back home.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_95D")

    label("loc_8DB")


    ChrTalk(
        0xA,
        (
            "Lately, I've been\x01",
            "deciding to go home right\x01",
            "away when it gets dark.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "...So I won't have to\x01",
            "rush if military dogs\x01",
            "appear.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_95D")

    Jump("loc_987")

    label("loc_962")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_970")
    Jump("loc_987")

    label("loc_970")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_97E")
    Jump("loc_987")

    label("loc_97E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_987")

    label("loc_987")

    TalkEnd(0xFE)
    Return()

    # Function_9_777 end

    def Function_10_98B(): pass

    label("Function_10_98B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_ADA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A57")

    ChrTalk(
        0xB,
        (
            "It seems Mayor Dieter\x01",
            "will visit the guest\x01",
            "house tonight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I hear he's been rather\x01",
            "busy after his\x01",
            "independence proposal...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "In the end, how will it\x01",
            "be realized?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_AD5")

    label("loc_A57")


    ChrTalk(
        0xB,
        (
            "I hear Mayor Dieter has been\x01",
            "quite busy following his\x01",
            "independence proposal...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "In the end, how will it\x01",
            "be realized?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AD5")

    Jump("loc_AF1")

    label("loc_ADA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_AE8")
    Jump("loc_AF1")

    label("loc_AE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_AF1")

    label("loc_AF1")

    TalkEnd(0xFE)
    Return()

    # Function_10_98B end

    def Function_11_AF5(): pass

    label("Function_11_AF5")

    EventBegin(0x0)
    Fade(500)
    LoadChrToIndex("chr/ch05100.itc", 0x1E)
    LoadChrToIndex("chr/ch07500.itc", 0x1F)
    OP_68(-1560, -2000, -14560, 0)
    MoveCamera(351, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(20110, 0)
    SetChrPos(0x101, -1020, -3800, -14130, 315)
    SetChrPos(0xEF, 0, -3800, -13600, 315)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0xC, 0x8000)
    OP_4B(0xC, 0xFF)
    SetChrSubChip(0xD, 0x1)
    OP_0D()

    ChrTalk(
        0xD,
        "#5P#05902FOh, Lloyd.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#5P#01200FGrrowl... Woof.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FCecil, and Zeit too. So\x01",
            "this is where you were.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 2)), scpexpr(EXPR_END)), "loc_C4B")

    ChrTalk(
        0x102,
        (
            "#12P#00100FThat's an unusual\x01",
            "combination.\x02\x03",
            "You haven't gone to the\x01",
            "guest house yet?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DDB")

    label("loc_C4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 3)), scpexpr(EXPR_END)), "loc_CB2")

    ChrTalk(
        0x103,
        (
            "#12P#00200FThat's an unusual\x01",
            "combination.\x02\x03",
            "You haven't gone to the\x01",
            "guest house yet?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DDB")

    label("loc_CB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 4)), scpexpr(EXPR_END)), "loc_D17")

    ChrTalk(
        0x104,
        (
            "#12P#00300FWhat an unusual\x01",
            "combination.\x02\x03",
            "Haven't you gone to the\x01",
            "guest house yet?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DDB")

    label("loc_D17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 5)), scpexpr(EXPR_END)), "loc_D7E")

    ChrTalk(
        0x109,
        (
            "#12P#10100FThat's an unusual\x01",
            "combination.\x02\x03",
            "You haven't gone to the\x01",
            "guest house yet?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DDB")

    label("loc_D7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 6)), scpexpr(EXPR_END)), "loc_DDB")

    ChrTalk(
        0x105,
        (
            "#12P#10300FWhat an unusual\x01",
            "combination.\x02\x03",
            "Didn't you go to the\x01",
            "guest house yet?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DDB")


    ChrTalk(
        0xD,
        (
            "#5P#05909FNo, Zeit took me here some\x01",
            "time ago.\x02\x03",
            "#05904FIt's far from the theme park\x01",
            "and quiet, so I thought to\x01",
            "cool off here a bit.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xD)

    ChrTalk(
        0x101,
        (
            "#12P#00003FCecil... Are you worried\x01",
            "about something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#5P#05904FHaha, no. That's not it,\x01",
            "but...\x02\x03",
            "#05901FHmm, maybe it's better\x01",
            "to tell you all about it\x01",
            "after all.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0xEF, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xD,
        (
            "#5P#05903FTruth is, Shizuku decided\x01",
            "to undergo her next\x01",
            "surgery.\x02\x03",
            "#05901FAn eyesight recovery\x01",
            "operation, to be performed\x01",
            "by Professor Seiland.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xEF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#12P#0005FShizuku is...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#5P#05908FShizuku has already undergone many surgeries\x01",
            "to recover her eyesight already. However...\x02\x03",
            "#05903FHer condition being a complex problem\x01",
            "involving internal medicine, surgery and\x01",
            "neurology, a complete recovery is difficult.\x02\x03",
            "#05900FAnd so, it seems Professor Seiland will test\x01",
            "out the new technique she has been\x01",
            "researching for a long time.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 2)), scpexpr(EXPR_END)), "loc_11D0")

    ChrTalk(
        0x102,
        "#12P#00105FA new technique, is it?\x02",
    )

    CloseMessageWindow()
    Jump("loc_1294")

    label("loc_11D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 3)), scpexpr(EXPR_END)), "loc_1201")

    ChrTalk(
        0x103,
        "#12P#00205FA new technique...\x02",
    )

    CloseMessageWindow()
    Jump("loc_1294")

    label("loc_1201")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 4)), scpexpr(EXPR_END)), "loc_1230")

    ChrTalk(
        0x104,
        "#12P#00305FA new technique?\x02",
    )

    CloseMessageWindow()
    Jump("loc_1294")

    label("loc_1230")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 5)), scpexpr(EXPR_END)), "loc_1262")

    ChrTalk(
        0x109,
        "#12P#10105FA new technique...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_1294")

    label("loc_1262")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 6)), scpexpr(EXPR_END)), "loc_1294")

    ChrTalk(
        0x105,
        "#12P#10305FHm, a new technique, eh?\x02",
    )

    CloseMessageWindow()

    label("loc_1294")


    ChrTalk(
        0xD,
        (
            "#5P#05903FI don't know all the details either,\x01",
            "but...\x02\x03",
            "#05902FIt seems to be a technique that only\x01",
            "the professor can perform, being both\x01",
            "a neurology authority and a surgeon.\x02\x03",
            "#05903FPreparations need to be perfect, so it\x01",
            "seems she ordered the latest medical\x01",
            "equipment from Remiferia recently.\x02\x03",
            "#05908FDespite that, her chances of success\x01",
            "are 50-50, according to Professor\x01",
            "Seiland.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003FFifty-fifty despite all\x01",
            "that, huh...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 2)), scpexpr(EXPR_END)), "loc_147D")

    ChrTalk(
        0x102,
        "#12P#00108F...That's worrying.\x02",
    )

    CloseMessageWindow()
    Jump("loc_154B")

    label("loc_147D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 3)), scpexpr(EXPR_END)), "loc_14B1")

    ChrTalk(
        0x103,
        "#12P#00208F...That's concerning.\x02",
    )

    CloseMessageWindow()
    Jump("loc_154B")

    label("loc_14B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 4)), scpexpr(EXPR_END)), "loc_14E9")

    ChrTalk(
        0x104,
        (
            "#12P#00303F...I'm worried about\x01",
            "her.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_154B")

    label("loc_14E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 5)), scpexpr(EXPR_END)), "loc_151A")

    ChrTalk(
        0x109,
        "#12P#10108FThat's worrying...\x02",
    )

    CloseMessageWindow()
    Jump("loc_154B")

    label("loc_151A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 6)), scpexpr(EXPR_END)), "loc_154B")

    ChrTalk(
        0x105,
        "#12P#10308FI see. That's worrying.\x02",
    )

    CloseMessageWindow()

    label("loc_154B")


    ChrTalk(
        0xD,
        (
            "#5P#05903FThinking about all the failures\x01",
            "until now, it's certain that there's\x01",
            "quite a bit of hope this time.\x02\x03",
            "#05908FI really hope it succeeds, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003FRight... We owe Arios a\x01",
            "lot too.\x02\x03",
            "#00000FWe'll pray to the Goddess\x01",
            "that the surgery will be\x01",
            "a success as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#5P#05909FHaha, thank you. I'll\x01",
            "tell Shizuku.\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0xE, 0x1E)
    SetChrSubChip(0xE, 0x0)
    SetChrFlags(0xE, 0x8000)
    ClearChrFlags(0xE, 0x4)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 250, -1800, -440, 180)

    NpcTalk(
        0xE,
        "Woman's Voice",
        (
            "#NOh, Cecil. You're still\x01",
            "here?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xEF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(-860, -2000, -14160, 3000)
    MoveCamera(344, 18, 0, 3000)
    OP_6E(400, 3000)
    SetCameraDistance(20110, 3000)

    def lambda_1767():

        label("loc_1767")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_1767")

    QueueWorkItem2(0x101, 2, lambda_1767)

    def lambda_1779():

        label("loc_1779")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_1779")

    QueueWorkItem2(0xEF, 2, lambda_1779)

    def lambda_178B():
        OP_95(0xFE, 250, -3800, -12220, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_178B)
    WaitChrThread(0xE, 1)
    OP_93(0xE, 0x10E, 0x1F4)
    EndChrThread(0x101, 0xFF)
    EndChrThread(0xEF, 0xFF)

    ChrTalk(
        0xD,
        (
            "#5P#05905FIlya, is something\x01",
            "wrong?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#01706FFor crying out loud...\x02\x03",
            "#01700FYou said you'd come later but I\x01",
            "waited forever and you never\x01",
            "did, so I came to come get you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#5P#05902FHaha, sorry. I'll be right there.\x02\x03",
            "#05904FYes, thanks to having talked to both of\x01",
            "you, I sorted out my feelings quite a\x01",
            "bit... I believe it's time for me to go.\x02\x03",
            "#05900FYou both probably have it hard in many\x01",
            "ways, but both Shizuku and I are\x01",
            "cheering for you.\x02\x03",
            "#05909FSo no matter what happens, don't lose\x01",
            "heart and do your best.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_19C1():
        TurnDirection(0x101, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_19C1)
    Sleep(50)

    def lambda_19D1():
        TurnDirection(0xEF, 0xD, 500)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_19D1)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0xEF, 0)

    ChrTalk(
        0x101,
        "#12P#00000FYeah, thanks Cecil.\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    SetChrChipByIndex(0xD, 0x1F)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x4)
    SetChrFlags(0xD, 0x40)
    SetChrPos(0xD, -1920, -3800, -13130, 180)
    OP_0D()
    Sleep(300)
    OP_93(0xD, 0x5A, 0x1F4)

    def lambda_1A41():
        OP_95(0xFE, -580, -3800, -12220, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1A41)
    WaitChrThread(0xD, 1)

    ChrTalk(
        0xD,
        "#5P#05900FLet's go then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#01705FTell me, tell me, did you have\x01",
            "a sexy conversation with little\x01",
            "bro and his friend here?\x02\x03",
            "#01709FLet me hear about it too...\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x0, 0x1F4)
    OP_93(0xEF, 0x0, 0x1F4)

    def lambda_1B13():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_1B13)
    OP_93(0xD, 0x0, 0x1F4)

    def lambda_1B27():
        OP_95(0xFE, 250, -1800, -440, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1B27)

    def lambda_1B41():
        OP_95(0xFE, -580, -1800, -440, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1B41)
    OP_68(-20, -2000, -16100, 5000)
    MoveCamera(344, 18, 0, 5000)
    OP_6E(400, 5000)
    SetCameraDistance(20110, 5000)
    WaitChrThread(0xD, 1)
    WaitChrThread(0xE, 1)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)

    def lambda_1B9B():
        TurnDirection(0xFE, 0xEF, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1B9B)
    TurnDirection(0xEF, 0x101, 500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 2)), scpexpr(EXPR_END)), "loc_1C17")

    ChrTalk(
        0x102,
        (
            "#12P#00102F*giggle*, we intended to\x01",
            "cheer her up, but on the\x01",
            "contrary, she encouraged us.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D8D")

    label("loc_1C17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 3)), scpexpr(EXPR_END)), "loc_1C75")

    ChrTalk(
        0x103,
        (
            "#12P#00202FWe intended to cheer her\x01",
            "up, but conversely, she\x01",
            "encouraged us.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D8D")

    label("loc_1C75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 4)), scpexpr(EXPR_END)), "loc_1CDD")

    ChrTalk(
        0x104,
        (
            "#12P#00302FHaha. We planned to cheer\x01",
            "her up, but on the contrary,\x01",
            "she encouraged us.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D8D")

    label("loc_1CDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 5)), scpexpr(EXPR_END)), "loc_1D44")

    ChrTalk(
        0x109,
        (
            "#12P#10102FHaha. We wanted to cheer her\x01",
            "up, but on the contrary, she\x01",
            "encouraged us.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D8D")

    label("loc_1D44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 6)), scpexpr(EXPR_END)), "loc_1D8D")

    ChrTalk(
        0x105,
        (
            "#12P#10302FHehe, now I don't know\x01",
            "which us was encouraged.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D8D")


    ChrTalk(
        0x101,
        (
            "#6P#00004FYeah, that's typical of\x01",
            "Cecil.\x02\x03",
            "#00000FAlright, it's about time\x01",
            "for us to be going to\x01",
            "the guest house.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#5P#01200FGrrowl... Woof.\x02",
    )

    CloseMessageWindow()

    def lambda_1E27():
        TurnDirection(0x101, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1E27)
    Sleep(50)

    def lambda_1E37():
        TurnDirection(0xEF, 0xC, 500)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_1E37)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0xEF, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 2)), scpexpr(EXPR_END)), "loc_1E7B")

    ChrTalk(
        0x102,
        "#12P#00100FWe're going, Zeit.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1F5E")

    label("loc_1E7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 3)), scpexpr(EXPR_END)), "loc_1EB3")

    ChrTalk(
        0x103,
        (
            "#12P#00200FYes... We're going,\x01",
            "Zeit.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F5E")

    label("loc_1EB3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 4)), scpexpr(EXPR_END)), "loc_1EE2")

    ChrTalk(
        0x104,
        "#12P#00300FWe're off, Zeit.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1F5E")

    label("loc_1EE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 5)), scpexpr(EXPR_END)), "loc_1F13")

    ChrTalk(
        0x109,
        "#12P#10100FWe're going, Zeit.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1F5E")

    label("loc_1F13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 6)), scpexpr(EXPR_END)), "loc_1F5E")

    ChrTalk(
        0x105,
        (
            "#12P#10300FHehe. Are you seeing us\x01",
            "off? See you later,\x01",
            "Zeit.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F5E")

    OP_5A()
    SetScenarioFlags(0x15A, 2)
    ClearChrFlags(0xC, 0x8000)
    OP_4C(0xC, 0xFF)
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -1020, -3800, -14130, 0)
    EventEnd(0x5)
    Return()

    # Function_11_AF5 end

    SaveToFile()

Try(main)
