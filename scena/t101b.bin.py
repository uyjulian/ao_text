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
        "Function_6_4FF",          # 06, 6
        "Function_7_5C9",          # 07, 7
        "Function_8_6E2",          # 08, 8
        "Function_9_77F",          # 09, 9
        "Function_10_9A7",         # 0A, 10
        "Function_11_B52",         # 0B, 11
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
    Jump("loc_4FB")

    label("loc_473")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_4AC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15A, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_48B")
    Jump("loc_4A7")

    label("loc_48B")


    ChrTalk(
        0xC,
        "#01200FGrrrowl...woof.\x02",
    )

    CloseMessageWindow()

    label("loc_4A7")

    Jump("loc_4FB")

    label("loc_4AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_4BA")
    Jump("loc_4FB")

    label("loc_4BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_4C8")
    Jump("loc_4FB")

    label("loc_4C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_4D6")
    Jump("loc_4FB")

    label("loc_4D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_4E4")
    Jump("loc_4FB")

    label("loc_4E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_4F2")
    Jump("loc_4FB")

    label("loc_4F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_4FB")

    label("loc_4FB")

    TalkEnd(0xFE)
    Return()

    # Function_5_44B end

    def Function_6_4FF(): pass

    label("Function_6_4FF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_5AE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_51D")
    Call(0, 7)
    Jump("loc_5A9")

    label("loc_51D")


    ChrTalk(
        0x8,
        (
            "Oh Zell... You're first class\x01",
            "only in gentlemanly behavior.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "B-But nevertheless,\x01",
            "you're far off from being\x01",
            "an amazing husband yet.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A9")

    Jump("loc_5C5")

    label("loc_5AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_5BC")
    Jump("loc_5C5")

    label("loc_5BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_5C5")

    label("loc_5C5")

    TalkEnd(0xFE)
    Return()

    # Function_6_4FF end

    def Function_7_5C9(): pass

    label("Function_7_5C9")

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
            "Like I told you at noon, from now on\x01",
            "you'll do your best at studying and sports.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I-I know already.\x01",
            "I'm Amy's fiancｳe, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I don't know how it'll turn out yet,\x01",
            "but I'll do my best efforts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "............*blusssh*\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x10)
    SetScenarioFlags(0x0, 2)
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    Return()

    # Function_7_5C9 end

    def Function_8_6E2(): pass

    label("Function_8_6E2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_764")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_700")
    Call(0, 7)
    Jump("loc_75F")

    label("loc_700")

    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)

    ChrTalk(
        0x9,
        (
            "Then, Amy.\x01",
            "It's cold at night,\x01",
            "you have to stay warm.\x02",
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

    label("loc_75F")

    Jump("loc_77B")

    label("loc_764")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_772")
    Jump("loc_77B")

    label("loc_772")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_77B")

    label("loc_77B")

    TalkEnd(0xFE)
    Return()

    # Function_8_6E2 end

    def Function_9_77F(): pass

    label("Function_9_77F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_97E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8D7")

    ChrTalk(
        0xA,
        (
            "Recently, when it grows dark I try to not\x01",
            "go out strolling as much as possible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Previously, when I was walking in the middle\x01",
            "of the night, I had a dreadful experience due to\x01",
            "the sudden appearance of the mafia military dogs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "You all too, if you have some business\x01",
            "finish it at once and go back home.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_979")

    label("loc_8D7")


    ChrTalk(
        0xA,
        (
            "Recently, when it grows dark I try to not\x01",
            "I decide to go back home at once.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "...So to not have to speed my wheels\x01",
            "in case military dogs suddenly appear.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_979")

    Jump("loc_9A3")

    label("loc_97E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_98C")
    Jump("loc_9A3")

    label("loc_98C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_99A")
    Jump("loc_9A3")

    label("loc_99A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_9A3")

    label("loc_9A3")

    TalkEnd(0xFE)
    Return()

    # Function_9_77F end

    def Function_10_9A7(): pass

    label("Function_10_9A7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_B37")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A9B")

    ChrTalk(
        0xB,
        (
            "It seems that tonight Mayor Dieter\x01",
            "is going to visit the guest house.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I hear he's quite busy too after\x01",
            "the independence proposal...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "In the end, what will the course \x01",
            "of events to its realization be?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_B32")

    label("loc_A9B")


    ChrTalk(
        0xB,
        (
            "I hear that Mayor Dieter is quite busy\x01",
            "after the independence proposal...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "In the end, what will the course \x01",
            "of events to its realization be?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B32")

    Jump("loc_B4E")

    label("loc_B37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_B45")
    Jump("loc_B4E")

    label("loc_B45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_B4E")

    label("loc_B4E")

    TalkEnd(0xFE)
    Return()

    # Function_10_9A7 end

    def Function_11_B52(): pass

    label("Function_11_B52")

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
        "#5P#01200FGrrowl...woof.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FSister Cecil, and Zeit.\x01",
            "So you were here.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 2)), scpexpr(EXPR_END)), "loc_C9F")

    ChrTalk(
        0x102,
        (
            "#12P#00100FWhat an unusual combination.\x02\x03",
            "You haven't gone to\x01",
            "the guest house yet?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E25")

    label("loc_C9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 3)), scpexpr(EXPR_END)), "loc_CFF")

    ChrTalk(
        0x103,
        (
            "#12P#00200FAn unusual combination.\x02\x03",
            "You haven't gone to\x01",
            "the guest house yet?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E25")

    label("loc_CFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 4)), scpexpr(EXPR_END)), "loc_D63")

    ChrTalk(
        0x104,
        (
            "#12P#00300FWhat a strange combination.\x02\x03",
            "Haven't you gone to\x01",
            "the guest house yet?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E25")

    label("loc_D63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 5)), scpexpr(EXPR_END)), "loc_DC8")

    ChrTalk(
        0x109,
        (
            "#12P#10100FWhat an unusual combination.\x02\x03",
            "You haven't gone to\x01",
            "the guest house yet?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E25")

    label("loc_DC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 6)), scpexpr(EXPR_END)), "loc_E25")

    ChrTalk(
        0x105,
        (
            "#12P#10300FWhat an unusual combination.\x02\x03",
            "Didn't you go to\x01",
            "the guest house yet?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E25")


    ChrTalk(
        0xD,
        (
            "#5P#05909FNo, Zeit took me\x01",
            "here some time ago.\x02\x03",
            "#05904FIt's quite far from the theme park\x01",
            "and I thought to cool off a bit here.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xD)

    ChrTalk(
        0x101,
        (
            "#12P#00003FSister Cecil...\x01",
            "Is there something worrying you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#5P#05904F...Uh uh, no.\x01",
            "It's not that, but...\x02\x03",
            "#05901FThat's right, maybe I should\x01",
            "talk about it to you all.\x02",
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
            "#5P#05903FThe truth is that Shizuku's\x01",
            "next surgery has been decided.\x02\x03",
            "#05901FAn eyesight recovery surgery\x01",
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
            "#5P#05908FFrom the start, Shizuku has undergone\x01",
            "many surgeries until now in order to\x01",
            "recover her eyesight, however...\x02\x03",
            "#05903FBeing her condition a complex problem\x01",
            "entwining internal medicine, surgery and\x01",
            "neurology, a complete recovery is difficult.\x02\x03",
            "#05900FSo, it seems that Professor Seiland\x01",
            "will try to test a new technique she\x01",
            "has been researching for a long time.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 2)), scpexpr(EXPR_END)), "loc_1223")

    ChrTalk(
        0x102,
        "#12P#00105FA new technique, is it?\x02",
    )

    CloseMessageWindow()
    Jump("loc_12E7")

    label("loc_1223")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 3)), scpexpr(EXPR_END)), "loc_1254")

    ChrTalk(
        0x103,
        "#12P#00205FA new technique...\x02",
    )

    CloseMessageWindow()
    Jump("loc_12E7")

    label("loc_1254")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 4)), scpexpr(EXPR_END)), "loc_1283")

    ChrTalk(
        0x104,
        "#12P#00305FA new technique?\x02",
    )

    CloseMessageWindow()
    Jump("loc_12E7")

    label("loc_1283")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 5)), scpexpr(EXPR_END)), "loc_12B5")

    ChrTalk(
        0x109,
        "#12P#10105FA new technique...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_12E7")

    label("loc_12B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 6)), scpexpr(EXPR_END)), "loc_12E7")

    ChrTalk(
        0x105,
        "#12P#10305FHm, a new technique, eh?\x02",
    )

    CloseMessageWindow()

    label("loc_12E7")


    ChrTalk(
        0xD,
        (
            "#5P#05903FI too don't know all the details, but...\x02\x03",
            "#05902FIt seems to be a technique that only the\x01",
            "professor can perform being a neurology \x01",
            "authority and having surgery knowledge too.\x02\x03",
            "#05903FPreparations need to be perfect, so it seems\x01",
            "that recently she ordered the latest\x01",
            "medical equipment from Remiferia.\x02\x03",
            "#05908F...According to Professor Seiland...\x01",
            "Even so, she said that the probability\x01",
            "of success maybe is fifty-fifty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00003FDespite all that...fifty-fifty...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 2)), scpexpr(EXPR_END)), "loc_14F9")

    ChrTalk(
        0x102,
        "#12P#00108F...That's a worry.\x02",
    )

    CloseMessageWindow()
    Jump("loc_15BE")

    label("loc_14F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 3)), scpexpr(EXPR_END)), "loc_152C")

    ChrTalk(
        0x103,
        "#12P#00208F...That's a concern.\x02",
    )

    CloseMessageWindow()
    Jump("loc_15BE")

    label("loc_152C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 4)), scpexpr(EXPR_END)), "loc_155B")

    ChrTalk(
        0x104,
        "#12P#00303F...What a worry.\x02",
    )

    CloseMessageWindow()
    Jump("loc_15BE")

    label("loc_155B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 5)), scpexpr(EXPR_END)), "loc_158B")

    ChrTalk(
        0x109,
        "#12P#10108FThat's a worry...\x02",
    )

    CloseMessageWindow()
    Jump("loc_15BE")

    label("loc_158B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 6)), scpexpr(EXPR_END)), "loc_15BE")

    ChrTalk(
        0x105,
        (
            "#12P#10308FI see.\x01",
            "...That's a worry.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15BE")


    ChrTalk(
        0xD,
        (
            "#5P#05903FThinking about all the failures\x01",
            "until now, there's no doubt\x01",
            "it's quite promising, though.\x02\x03",
            "#05908FI really hope it\x01",
            "succeeds, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003FRight...\x01",
            "We owe Mr. Arios\x01",
            "a lot too.\x02\x03",
            "#00000FWe too will pray the Goddess\x01",
            "for the surgery success.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#5P#05909FUh uh, thank you.\x01",
            "I'll tell Shizuku about it.\x02",
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
            "#NOh, Cecil.\x01",
            "You were still there?\x02",
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

    def lambda_17D1():

        label("loc_17D1")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_17D1")

    QueueWorkItem2(0x101, 2, lambda_17D1)

    def lambda_17E3():

        label("loc_17E3")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_17E3")

    QueueWorkItem2(0xEF, 2, lambda_17E3)

    def lambda_17F5():
        OP_95(0xFE, 250, -3800, -12220, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_17F5)
    WaitChrThread(0xE, 1)
    OP_93(0xE, 0x10E, 0x1F4)
    EndChrThread(0x101, 0xFF)
    EndChrThread(0xEF, 0xFF)

    ChrTalk(
        0xD,
        "#5P#05905FIlya, is something wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#01706FFor crying out loud...\x02\x03",
            "#01700FYou said you'd come later\x01",
            "but since you never came,\x01",
            "I came on purpose to pick you up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#5P#05902FUh uh, I'm sorry.\x01",
            "I'll come immediately.\x02\x03",
            "#05904FYes, thanks to having talked to you,\x01",
            "I could sort out my feelings a lot...\x01",
            "I believe I'll go now.\x02\x03",
            "#05900FYou probably have many problems too, but...\x01",
            "Both Shizuku and I are cheering for you.\x02\x03",
            "#05909FSo no matter what happens,\x01",
            "do your best without being discouraged.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1A16():
        TurnDirection(0x101, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1A16)
    Sleep(50)

    def lambda_1A26():
        TurnDirection(0xEF, 0xD, 500)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_1A26)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0xEF, 0)

    ChrTalk(
        0x101,
        "#12P#00000FYeah, thank you sister Cecil.\x02",
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

    def lambda_1AA0():
        OP_95(0xFE, -580, -3800, -12220, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1AA0)
    WaitChrThread(0xD, 1)

    ChrTalk(
        0xD,
        "#5P#05900FLet's go then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#01705FTell me, tell me, did you have a sexy conversation\x01",
            "with the younger brother and friend?\x02\x03",
            "#01709FLet me hear about it too...\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x0, 0x1F4)
    OP_93(0xEF, 0x0, 0x1F4)

    def lambda_1B72():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_1B72)
    OP_93(0xD, 0x0, 0x1F4)

    def lambda_1B86():
        OP_95(0xFE, 250, -1800, -440, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1B86)

    def lambda_1BA0():
        OP_95(0xFE, -580, -1800, -440, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1BA0)
    OP_68(-20, -2000, -16100, 5000)
    MoveCamera(344, 18, 0, 5000)
    OP_6E(400, 5000)
    SetCameraDistance(20110, 5000)
    WaitChrThread(0xD, 1)
    WaitChrThread(0xE, 1)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)

    def lambda_1BFA():
        TurnDirection(0xFE, 0xEF, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1BFA)
    TurnDirection(0xEF, 0x101, 500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 2)), scpexpr(EXPR_END)), "loc_1C76")

    ChrTalk(
        0x102,
        (
            "#12P#00102F*giggle*, we intended to cheer her up,\x01",
            "but on the contrary, she encouraged us.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DF0")

    label("loc_1C76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 3)), scpexpr(EXPR_END)), "loc_1CD4")

    ChrTalk(
        0x103,
        (
            "#12P#00202FWe intended to cheer her up,\x01",
            "but conversely, she encouraged us.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DF0")

    label("loc_1CD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 4)), scpexpr(EXPR_END)), "loc_1D3D")

    ChrTalk(
        0x104,
        (
            "#12P#00302FHa ha, we planned to cheer her up,\x01",
            "but on the contrary, she encouraged us.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DF0")

    label("loc_1D3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 5)), scpexpr(EXPR_END)), "loc_1DA5")

    ChrTalk(
        0x109,
        (
            "#12P#10102FUh uh, we wanted to cheer her up,\x01",
            "but on the contrary, she encouraged us.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DF0")

    label("loc_1DA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 6)), scpexpr(EXPR_END)), "loc_1DF0")

    ChrTalk(
        0x105,
        (
            "#12P#10302FHu hu, now I don't know who\x01",
            "of us was encouraged.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DF0")


    ChrTalk(
        0x101,
        (
            "#6P#00004FYeah, typical of sister Cecil.\x02\x03",
            "#00000F...Alright, it should be time for us\x01",
            "too to go to the guest house.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#5P#01200FGrrowl...woof.\x02",
    )

    CloseMessageWindow()

    def lambda_1E8C():
        TurnDirection(0x101, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1E8C)
    Sleep(50)

    def lambda_1E9C():
        TurnDirection(0xEF, 0xC, 500)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_1E9C)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0xEF, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 2)), scpexpr(EXPR_END)), "loc_1EE0")

    ChrTalk(
        0x102,
        "#12P#00100FWe're going, Zeit.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1FC4")

    label("loc_1EE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 3)), scpexpr(EXPR_END)), "loc_1F18")

    ChrTalk(
        0x103,
        (
            "#12P#00200FYes...\x01",
            "We're going, Zeit.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FC4")

    label("loc_1F18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 4)), scpexpr(EXPR_END)), "loc_1F47")

    ChrTalk(
        0x104,
        "#12P#00300FWe're off, Zeit.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1FC4")

    label("loc_1F47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 5)), scpexpr(EXPR_END)), "loc_1F78")

    ChrTalk(
        0x109,
        "#12P#10100FWe're going, Zeit.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1FC4")

    label("loc_1F78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 6)), scpexpr(EXPR_END)), "loc_1FC4")

    ChrTalk(
        0x105,
        (
            "#12P#10300FHu hu, are you seeing us off?\x01",
            "See you later, Zeit.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FC4")

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

    # Function_11_B52 end

    SaveToFile()

Try(main)
