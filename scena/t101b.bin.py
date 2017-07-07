from ScenarioHelper import *

def main():
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
        "Emmy",                 # 1
        "Gel",                   # 2
        "Kabiran",               # 3
        "Loumann",             # 4
        "Zeit",               # 5
        "Cecil",                 # 6
        "Ilia",                 # 7
        "Directions to Kaikan",             # 8
        "Destination to Hotel · Delfinia",# 9
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

    PlaceName(-5.0, 0.0, 81.0, 0x0000, 0x0000, "Directions to Kaikan")
    PlaceName(65.0, 0.0, 0.0, 0x0000, 0x0000, "Destination to Hotel · Delfinia")

    ChipFrameInfo(456, 0)                                        # 0

    ScpFunction((
        "Function_0_1C8",          # 00, 0
        "Function_1_280",          # 01, 1
        "Function_2_2E1",          # 02, 2
        "Function_3_39E",          # 03, 3
        "Function_4_3C6",          # 04, 4
        "Function_5_44B",          # 05, 5
        "Function_6_504",          # 06, 6
        "Function_7_5BB",          # 07, 7
        "Function_8_6B5",          # 08, 8
        "Function_9_765",          # 09, 9
        "Function_10_911",         # 0A, 10
        "Function_11_A70",         # 0B, 11
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
    Jump("loc_500")

    label("loc_473")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_4B1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15A, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_48B")
    Jump("loc_4AC")

    label("loc_48B")


    ChrTalk(
        0xC,
        "#01200FGurururu …… won.\x02",
    )

    CloseMessageWindow()

    label("loc_4AC")

    Jump("loc_500")

    label("loc_4B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_4BF")
    Jump("loc_500")

    label("loc_4BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_4CD")
    Jump("loc_500")

    label("loc_4CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_4DB")
    Jump("loc_500")

    label("loc_4DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_4E9")
    Jump("loc_500")

    label("loc_4E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_4F7")
    Jump("loc_500")

    label("loc_4F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_500")

    label("loc_500")

    TalkEnd(0xFE)
    Return()

    # Function_5_44B end

    def Function_6_504(): pass

    label("Function_6_504")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_5A0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_522")
    Call(0, 7)
    Jump("loc_59B")

    label("loc_522")


    ChrTalk(
        0x8,
        (
            "Gelったら……\x01",
            "Only gentlemanly behavior is first class.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "But, that's why\x01",
            "To a still wonderful husband\x01",
            "I am far from it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_59B")

    Jump("loc_5B7")

    label("loc_5A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_5AE")
    Jump("loc_5B7")

    label("loc_5AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_5B7")

    label("loc_5B7")

    TalkEnd(0xFE)
    Return()

    # Function_6_504 end

    def Function_7_5BB(): pass

    label("Function_7_5BB")

    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)

    ChrTalk(
        0x8,
        "いいこと、Gel？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "As I said in the daytime,\x01",
            "From now on I will do my best for both study and exercise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Well, I know.\x01",
            "僕はEmmyの許婚だからね。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I do not know what will happen yet,\x01",
            "I will make efforts as appropriate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "………… ぽ っ.\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x10)
    SetScenarioFlags(0x0, 2)
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    Return()

    # Function_7_5BB end

    def Function_8_6B5(): pass

    label("Function_8_6B5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_74A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6D3")
    Call(0, 7)
    Jump("loc_745")

    label("loc_6D3")

    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)

    ChrTalk(
        0x9,
        (
            "それじゃあね、Emmy。\x01",
            "Because it cools down in the middle of the night\x01",
            "You have to warm it up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "I know, I know.\x02",
    )

    CloseMessageWindow()
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)

    label("loc_745")

    Jump("loc_761")

    label("loc_74A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_758")
    Jump("loc_761")

    label("loc_758")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_761")

    label("loc_761")

    TalkEnd(0xFE)
    Return()

    # Function_8_6B5 end

    def Function_9_765(): pass

    label("Function_9_765")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_8E8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_85F")

    ChrTalk(
        0xA,
        (
            "Recently, as long as it gets dark\x01",
            "I try not to go out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Previously, if I took a walk in the middle of the night\x01",
            "Suddenly a mafia military dog appeared,\x01",
            "I have a scary feeling.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "If you have use\x01",
            "Come home and go home at once.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_8E3")

    label("loc_85F")


    ChrTalk(
        0xA,
        (
            "Recently, when it gets dark\x01",
            "I decided to go home quickly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "…… suddenly when a military dog or something appeared\x01",
            "Just like you do not have to warm yourself.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8E3")

    Jump("loc_90D")

    label("loc_8E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_8F6")
    Jump("loc_90D")

    label("loc_8F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_904")
    Jump("loc_90D")

    label("loc_904")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_90D")

    label("loc_90D")

    TalkEnd(0xFE)
    Return()

    # Function_9_765 end

    def Function_10_911(): pass

    label("Function_10_911")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_A55")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9D6")

    ChrTalk(
        0xB,
        (
            "Tonight at the guest house\x01",
            "It seems that Mayor Dieter will visit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "From independent proposition he also\x01",
            "I hear that you are quite busy … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Indeed, for the realization\x01",
            "I wonder how the success is.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_A50")

    label("loc_9D6")


    ChrTalk(
        0xB,
        (
            "Mayor Dieter from independent advocacy\x01",
            "I hear that you are quite busy … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Indeed, for the realization\x01",
            "I wonder how the success is.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A50")

    Jump("loc_A6C")

    label("loc_A55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_A63")
    Jump("loc_A6C")

    label("loc_A63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_A6C")

    label("loc_A6C")

    TalkEnd(0xFE)
    Return()

    # Function_10_911 end

    def Function_11_A70(): pass

    label("Function_11_A70")

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
        "#5P#01200FGuru …… Won.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FCecil姉、それにZeit。\x01",
            "Have you been in such a place?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 2)), scpexpr(EXPR_END)), "loc_BC4")

    ChrTalk(
        0x102,
        (
            "#12P#00100FIt is an unusual combination.\x02\x03",
            "At the guest house\x01",
            "Are not you going yet?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D29")

    label("loc_BC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 3)), scpexpr(EXPR_END)), "loc_C24")

    ChrTalk(
        0x103,
        (
            "#12P#00200FIt is an unusual combination.\x02\x03",
            "The guest house\x01",
            "Are not you going yet?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D29")

    label("loc_C24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 4)), scpexpr(EXPR_END)), "loc_C7E")

    ChrTalk(
        0x104,
        (
            "#12P#00300FIt is an unusual combination.\x02\x03",
            "At the guest house\x01",
            "Is not it going yet?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D29")

    label("loc_C7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 5)), scpexpr(EXPR_END)), "loc_CD8")

    ChrTalk(
        0x109,
        (
            "#12P#10100FIt is an unusual combination.\x02\x03",
            "At the guest house\x01",
            "Are not you going yet?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D29")

    label("loc_CD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 6)), scpexpr(EXPR_END)), "loc_D29")

    ChrTalk(
        0x105,
        (
            "#12P#10300FIt is an unusual combination.\x02\x03",
            "At the guest house\x01",
            "Are not you going yet?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D29")


    ChrTalk(
        0xD,
        (
            "#5P#05909Fええ、さっきZeit君が\x01",
            "Bring me here.\x02\x03",
            "#05904FIt is quiet away from the theme park,\x01",
            "I thought that it would be cool for a while.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xD)

    ChrTalk(
        0x101,
        (
            "#12P#00003FCecil姉……\x01",
            "Is it also a matter of trouble?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#5P#05904F…, Huhu, no.\x01",
            "It's not like that ….\x02\x03",
            "#05901FWell, to Lloyd's\x01",
            "You may as well talk about it.\x02",
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
            "#5P#05903FActually this time, Shizuoka\x01",
            "I was to have surgery.\x02\x03",
            "#05901FProfessor Seyland,\x01",
            "Surgery that restored vision.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xEF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#12P#0005FShizuku-chan …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#5P#05908FOriginally, Shizuoka\x01",
            "In order to recover vision several times ever\x01",
            "I was undergoing surgery, but ….\x02\x03",
            "#05903FHer symptoms are internal medicine and surgery,\x01",
            "The neurological problem is involved in complexity,\x01",
            "It was difficult to recover.\x02\x03",
            "#05900FSo, Professor Seyland\x01",
            "A new technique to be studied from a long time ago\x01",
            "She seems to have tried it.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 2)), scpexpr(EXPR_END)), "loc_10D9")

    ChrTalk(
        0x102,
        "#12P#00105FIs it a new operation ceremony?\x02",
    )

    CloseMessageWindow()
    Jump("loc_1198")

    label("loc_10D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 3)), scpexpr(EXPR_END)), "loc_1106")

    ChrTalk(
        0x103,
        "#12P#00205FA new operation formula …\x02",
    )

    CloseMessageWindow()
    Jump("loc_1198")

    label("loc_1106")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 4)), scpexpr(EXPR_END)), "loc_1139")

    ChrTalk(
        0x104,
        "#12P#00305FA new technique, something.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1198")

    label("loc_1139")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 5)), scpexpr(EXPR_END)), "loc_1168")

    ChrTalk(
        0x109,
        "#12P#10105FA new operation formula …?\x02",
    )

    CloseMessageWindow()
    Jump("loc_1198")

    label("loc_1168")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 6)), scpexpr(EXPR_END)), "loc_1198")

    ChrTalk(
        0x105,
        "#12P#10305FHmm, a new operation ceremony.\x02",
    )

    CloseMessageWindow()

    label("loc_1198")


    ChrTalk(
        0xD,
        (
            "#5P#05903FI am not too familiar with it though ….\x02\x03",
            "#05902FUnder the authority of the neurology department, there is a knowledge of surgery\x01",
            "It seems like a professor to be the only technique to take.\x02\x03",
            "#05903FIt seems necessary to prepare thoroughly,\x01",
            "In the meantime, from the remiferia the latest formula\x01",
            "I seem to have ordered medical equipment.\x02\x03",
            "#05908F…… According to Professor Seyland,\x01",
            "Nevertheless the probability would probably be more than half\x01",
            "Although it was a story.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00003FIs it even fifty-seven so far …?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 2)), scpexpr(EXPR_END)), "loc_133E")

    ChrTalk(
        0x102,
        "#12P#00108F… … I am worried about that.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1410")

    label("loc_133E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 3)), scpexpr(EXPR_END)), "loc_136F")

    ChrTalk(
        0x103,
        "#12P#00208F……Makes you worry, right.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1410")

    label("loc_136F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 4)), scpexpr(EXPR_END)), "loc_13A4")

    ChrTalk(
        0x104,
        "#12P#00303F… … That's a worrying question.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1410")

    label("loc_13A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 5)), scpexpr(EXPR_END)), "loc_13D7")

    ChrTalk(
        0x109,
        "#12P#10108FI am worried about that … ….\x02",
    )

    CloseMessageWindow()
    Jump("loc_1410")

    label("loc_13D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 6)), scpexpr(EXPR_END)), "loc_1410")

    ChrTalk(
        0x105,
        (
            "#12P#10308FI see.\x01",
            "… … I am worried about that.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1410")


    ChrTalk(
        0xD,
        (
            "#5P#05903FGiven the failure to date\x01",
            "There is considerable hope\x01",
            "It seems that there is no mistake.\x02\x03",
            "#05908FTruly, if you succeed\x01",
            "I do not mind ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003FThat's right.\x01",
            "To Arios very much\x01",
            "I am indebted to you.\x02\x03",
            "#00000FWe also do the success of the operation\x01",
            "I pray to the goddess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#5P#05909FHehe, Thank you.\x01",
            "I will tell Shizuoka too.\x02",
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
        "Female voice",
        (
            "#Nあら、Cecil。\x01",
            "Have you been here yet?\x02",
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

    def lambda_162C():

        label("loc_162C")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_162C")

    QueueWorkItem2(0x101, 2, lambda_162C)

    def lambda_163E():

        label("loc_163E")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_163E")

    QueueWorkItem2(0xEF, 2, lambda_163E)

    def lambda_1650():
        OP_95(0xFE, 250, -3800, -12220, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1650)
    WaitChrThread(0xE, 1)
    OP_93(0xE, 0x10E, 0x1F4)
    EndChrThread(0x101, 0xFF)
    EndChrThread(0xEF, 0xFF)

    ChrTalk(
        0xD,
        "#5P#05905FIlia、どうしたの？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#01706FWhatever happens … …\x02\x03",
            "#01700FSay it will come later\x01",
            "Because I will never come\x01",
            "I came all the way to pick him up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#5P#05902FHehe, I'm sorry,\x01",
            "I will go soon.\x02\x03",
            "#05904FYes, thanks to Lloyd's\x01",
            "I could also organize the feeling of Oita ……\x01",
            "I guess I will go soon.\x02\x03",
            "#05900FYou guys will also be seriously hard … …\x01",
            "I and I support you too.\x02\x03",
            "#05909FSo, no matter what happens\x01",
            "Do your best and do your best.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_183F():
        TurnDirection(0x101, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_183F)
    Sleep(50)

    def lambda_184F():
        TurnDirection(0xEF, 0xD, 500)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_184F)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0xEF, 0)

    ChrTalk(
        0x101,
        "#12P#00000Fああ、ありがとうCecil姉。\x02",
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

    def lambda_18C6():
        OP_95(0xFE, -580, -3800, -12220, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_18C6)
    WaitChrThread(0xD, 1)

    ChrTalk(
        0xD,
        "#5P#05900FWell then, let's go.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#01705FWhat, my brother with you\x01",
            "You were talking about sexy?\x02\x03",
            "#01709FPlease let me know as well.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x0, 0x1F4)
    OP_93(0xEF, 0x0, 0x1F4)

    def lambda_1975():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_1975)
    OP_93(0xD, 0x0, 0x1F4)

    def lambda_1989():
        OP_95(0xFE, 250, -1800, -440, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1989)

    def lambda_19A3():
        OP_95(0xFE, -580, -1800, -440, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_19A3)
    OP_68(-20, -2000, -16100, 5000)
    MoveCamera(344, 18, 0, 5000)
    OP_6E(400, 5000)
    SetCameraDistance(20110, 5000)
    WaitChrThread(0xD, 1)
    WaitChrThread(0xE, 1)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)

    def lambda_19FD():
        TurnDirection(0xFE, 0xEF, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_19FD)
    TurnDirection(0xEF, 0x101, 500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 2)), scpexpr(EXPR_END)), "loc_1A5E")

    ChrTalk(
        0x102,
        (
            "#12P#00102FHuhu, I'm going to cheer you up.\x01",
            "On the other hand I was encouraged.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BAD")

    label("loc_1A5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 3)), scpexpr(EXPR_END)), "loc_1AAE")

    ChrTalk(
        0x103,
        (
            "#12P#00202FI am planning to cheer you up.\x01",
            "On the contrary it was encouraged.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BAD")

    label("loc_1AAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 4)), scpexpr(EXPR_END)), "loc_1B04")

    ChrTalk(
        0x104,
        (
            "#12P#00302FHaha, I intended to cheer you up.\x01",
            "On the contrary it got encouraged.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BAD")

    label("loc_1B04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 5)), scpexpr(EXPR_END)), "loc_1B58")

    ChrTalk(
        0x109,
        (
            "#12P#10102FHuhu, I'm going to cheer you up.\x01",
            "On the other hand, I was encouraged.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BAD")

    label("loc_1B58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 6)), scpexpr(EXPR_END)), "loc_1BAD")

    ChrTalk(
        0x105,
        (
            "#12P#10302FHuh, I was energizing\x01",
            "I do not know which one it is.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BAD")


    ChrTalk(
        0x101,
        (
            "#6P#00004Fああ、Cecil姉らしいよ。\x02\x03",
            "#00000F… … Well, we're almost done.\x01",
            "Shall we go to the guest house?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#5P#01200FGuru …… Won.\x02",
    )

    CloseMessageWindow()

    def lambda_1C38():
        TurnDirection(0x101, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1C38)
    Sleep(50)

    def lambda_1C48():
        TurnDirection(0xEF, 0xC, 500)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_1C48)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0xEF, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 2)), scpexpr(EXPR_END)), "loc_1C94")

    ChrTalk(
        0x102,
        "#12P#00100F行ってくるわね、Zeit。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1D93")

    label("loc_1C94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 3)), scpexpr(EXPR_END)), "loc_1CD6")

    ChrTalk(
        0x103,
        (
            "#12P#00200FYeah ….\x01",
            "行ってきますね、Zeit。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D93")

    label("loc_1CD6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 4)), scpexpr(EXPR_END)), "loc_1D0D")

    ChrTalk(
        0x104,
        "#12P#00300F行ってくるぜ、Zeit。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1D93")

    label("loc_1D0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 5)), scpexpr(EXPR_END)), "loc_1D46")

    ChrTalk(
        0x109,
        "#12P#10100F行ってくるね、Zeit君。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1D93")

    label("loc_1D46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 6)), scpexpr(EXPR_END)), "loc_1D93")

    ChrTalk(
        0x105,
        (
            "#12P#10300FHuh, are you waiting for me?\x01",
            "また後で、Zeit。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D93")

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

    # Function_11_A70 end

    SaveToFile()

Try(main)
