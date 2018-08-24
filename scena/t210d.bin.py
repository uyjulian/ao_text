from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t210d.bin",                # FileName
        "t210d",                    # MapName
        "t210d",                    # Location
        0x0059,                     # MapIndex
        "ed7151",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x1C,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 2],
    )

    BuildStringList((
        "t210d",                  # 0
        "Commander Sonya",        # 1
        "Soldier Broude ",        # 2
        "Soldier Dahlia ",        # 3
        "Tourist",                # 4
    ))

    AddCharChip((
        "chr/ch12200.itc",                   # 00
        "chr/ch41400.itc",                   # 01
        "chr/ch41800.itc",                   # 02
        "chr/ch33000.itc",                   # 03
    ))

    DeclNpc(4294957296, 10000,   0,       270,  261,  0x0, 0,   0,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(4294953467, 10000,   4294964336, 270,  261,  0x0, 0,   1,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(4294953236, 10000,   2900,    270,  261,  0x0, 0,   2,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(4294948696, 5000,    4294950126, 270,  389,  0x0, 0,   3,   0,   0,   0,   0,   7,   255,  0)

    DeclActor(1500,    5050,    4294947296, 1200,    1500,    6050,    4294947296, 0x007C, 0,  3,  0x0000)

    ChipFrameInfo(348, 0)                                        # 0

    ScpFunction((
        "Function_0_15C",          # 00, 0
        "Function_1_20C",          # 01, 1
        "Function_2_21B",          # 02, 2
        "Function_3_25C",          # 03, 3
        "Function_4_3AD",          # 04, 4
        "Function_5_5CD",          # 05, 5
        "Function_6_7C3",          # 06, 6
        "Function_7_8F1",          # 07, 7
        "Function_8_A64",          # 08, 8
    ))


    def Function_0_15C(): pass

    label("Function_0_15C")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_194"),
        (1, "loc_1A0"),
        (2, "loc_1AC"),
        (3, "loc_1B8"),
        (4, "loc_1C4"),
        (5, "loc_1D0"),
        (6, "loc_1DC"),
        (SWITCH_DEFAULT, "loc_1E8"),
    )


    label("loc_194")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_1F4")

    label("loc_1A0")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_1F4")

    label("loc_1AC")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_1F4")

    label("loc_1B8")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_1F4")

    label("loc_1C4")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_1F4")

    label("loc_1D0")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_1F4")

    label("loc_1DC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1F4")

    label("loc_1E8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1F4")

    label("loc_1F4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_20B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1F4")

    label("loc_20B")

    Return()

    # Function_0_15C end

    def Function_1_20C(): pass

    label("Function_1_20C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_21A")
    ClearChrFlags(0xB, 0x80)

    label("loc_21A")

    Return()

    # Function_1_20C end

    def Function_2_21B(): pass

    label("Function_2_21B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_22D")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x236), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_22D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_244")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    Jump("loc_244")

    label("loc_244")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1ED, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_257")
    OP_70(0x2, 0x0)
    Jump("loc_25B")

    label("loc_257")

    OP_70(0x2, 0x1E)

    label("loc_25B")

    Return()

    # Function_2_21B end

    def Function_3_25C(): pass

    label("Function_3_25C")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1ED, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_358")
    Sound(14, 0, 100, 0)
    OP_74(0x2, 0x1E)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1F4, 1)"), scpexpr(EXPR_END)), "loc_2E1")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1F4),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1ED, 6)
    OP_E0(0x5, 0x0)
    Jump("loc_353")

    label("loc_2E1")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1F4),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " is inside the chest.\x01",
            "Since you have too many,\x01",
            "you gave it up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x2, 0x1E, 0x0, 0x0, 0x0)

    label("loc_353")

    Jump("loc_3A1")

    label("loc_358")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is nothing in the\x01",
            "chest.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_3A1")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_25C end

    def Function_4_3AD(): pass

    label("Function_4_3AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AC, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BB")
    Call(0, 8)
    Return()

    label("loc_3BB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_53F")

    ChrTalk(
        0x8,
        (
            "#10600FRegarding our response going forward,\x01",
            "Vice Commander Douglas has gone to\x01",
            "discuss it with Chairman MacDowell.\x02\x03",
            "As the commanding officer of a regular\x01",
            "army, I have to make full preparations\x01",
            "against the Empire and Republic.\x02\x03",
            "#10603FAfter everything is over, I'm not\x01",
            "exactly sure, but...\x02\x03",
            "#10600FFor now, I'll do everything I can as\x01",
            "their commanding officer.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_5C9")

    label("loc_53F")


    ChrTalk(
        0x8,
        (
            "#10603FAfter everything is over,\x01",
            "I'm not exactly sure,\x01",
            "but...\x02\x03",
            "#10600FFor now, I'll do\x01",
            "everything I can as their\x01",
            "commanding officer.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5C9")

    TalkEnd(0xFE)
    Return()

    # Function_4_3AD end

    def Function_5_5CD(): pass

    label("Function_5_5CD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6F9")

    ChrTalk(
        0x9,
        (
            "In the Empire, it seems\x01",
            ""Gunships" were developed during\x01",
            "the course of the civil war.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If they add them to the Imperial\x01",
            "Army armored division, things\x01",
            "will honestly get out of hand...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If only we had those Aions...\x01",
            "I wonder if I'm the only one\x01",
            "who thinks that way...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_7BF")

    label("loc_6F9")


    ChrTalk(
        0x9,
        (
            "If they add those "Gunships" to the\x01",
            "Imperial Army armored division,\x01",
            "things will honestly get out of hand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If only we had those Aions...\x01",
            "I wonder if I'm the only one\x01",
            "who thinks that way...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7BF")

    TalkEnd(0xFE)
    Return()

    # Function_5_5CD end

    def Function_6_7C3(): pass

    label("Function_6_7C3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_848")

    ChrTalk(
        0xA,
        (
            "I'm glad we lost the\x01",
            "Aions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I can't think people like\x01",
            "us could ever use weapons\x01",
            "with that much power.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_8ED")

    label("loc_848")


    ChrTalk(
        0xA,
        (
            "Aions... I think it would\x01",
            "be impossible for us to\x01",
            "use anything like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "...Looking at the state of\x01",
            "Garrelia Fortress, chills\x01",
            "run down my spine even now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8ED")

    TalkEnd(0xFE)
    Return()

    # Function_6_7C3 end

    def Function_7_8F1(): pass

    label("Function_7_8F1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_A60")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9E4")

    ChrTalk(
        0xB,
        (
            "Thinking I wanted to return\x01",
            "to the Empire somehow, I came\x01",
            "to Bellguard Gate, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "W-Who could've thought\x01",
            "that would happen to\x01",
            "Garrelia Fortress...!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I guess it's impossible\x01",
            "to go home now, huh...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_A60")

    label("loc_9E4")


    ChrTalk(
        0xB,
        (
            "W-Who could've thought\x01",
            "that would happen to\x01",
            "Garrelia Fortress...!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I guess it's impossible\x01",
            "to go home now, huh...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A60")

    TalkEnd(0xFE)
    Return()

    # Function_7_8F1 end

    def Function_8_A64(): pass

    label("Function_8_A64")

    EventBegin(0x0)
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x236), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(-6780, 12170, -1160, 0)
    MoveCamera(303, 28, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(12280, 0)
    SetChrPos(0x101, -8000, 10000, 500, 270)
    SetChrPos(0x102, -7900, 10000, -500, 270)
    SetChrPos(0x103, -7000, 10000, 1400, 270)
    SetChrPos(0x104, -6800, 10000, -1500, 270)
    SetChrPos(0xF4, -6000, 10000, 500, 270)
    SetChrPos(0xF5, -5800, 10000, -500, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x8, 0xFF)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#12P#00002FCommander Sonya... So\x01",
            "this is where you were.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x5A, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x8,
        "#10605F#5PYou all...\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(-68290, 12670, -3030, 0)
    MoveCamera(239, 21, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(127990, 0)
    OP_0D()
    MoveCamera(303, 17, 0, 40000)
    Sleep(1000)
    SetMessageWindowPos(14, 280, -1, 3)

    AnonymousTalk(
        0x104,
        (
            "#00301F...Nice view, eh?\x02\x03",
            "#00303FWe saw footage of that white\x01",
            "doll erasin' the railway\x01",
            "cannons without a trace, but...\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    AnonymousTalk(
        0x101,
        (
            "#00008F...It was indirect, but\x01",
            "this happened due to\x01",
            "KeA's power...\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    AnonymousTalk(
        0x8,
        (
            "#10603F...This is uncertain intel we have\x01",
            "received from the Imperial side,\x01",
            "but...\x02\x03",
            "#10600FIt seems that in that Aion attack,\x01",
            "there were almost no casualties\x01",
            "among the Imperial Army.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    AnonymousTalk(
        0x101,
        "#12P#00005FR-Really!?\x02",
    )

    CloseMessageWindow()
    OP_5A()

    AnonymousTalk(
        0x102,
        (
            "#12P#00105FC-Considering the\x01",
            "situation, I can only\x01",
            "say it was a miracle...\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    AnonymousTalk(
        0x8,
        (
            "#10600FBecause we can't confirm the\x01",
            "truth, we don't know the actual\x01",
            "facts, but...\x02\x03",
            "#10604FIt could've been a power that\x01",
            "erases only inorganic substances\x01",
            "without affecting humans.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    AnonymousTalk(
        0x103,
        (
            "#12P#00202FIf that's true, KeA could have\x01",
            "interfered with the Miracle\x01",
            "unconsciously.\x02\x03",
            "#00204FAlthough there is no doubt that the\x01",
            "Empire received enormous damage...\x01",
            "I'm just a little relieved.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Fade(500)
    OP_68(-6780, 12170, -1160, 0)
    MoveCamera(303, 28, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(12280, 0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#10604F#5P...I heard the news.\x02\x03",
            "#10602FIt seems that the\x01",
            "Crossbell City liberation\x01",
            "operation went well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00309FHaha. Honestly, you did\x01",
            "too much.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10D3")

    ChrTalk(
        0x109,
        (
            "#12P#10104FIt was thanks to you, Commander\x01",
            "Sonya!\x02\x03",
            "#10102FIt was your advice that gave us\x01",
            "the option of the independence\x01",
            "invalidity declaration!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1235")

    label("loc_10D3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_118B")

    ChrTalk(
        0x105,
        (
            "#12P#10400FHehe. That may have been\x01",
            "because of you, Commander.\x02\x03",
            "#10404FIt was your advice that gave us\x01",
            "the option of the independence\x01",
            "invalidity declaration.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1235")

    label("loc_118B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1235")

    ChrTalk(
        0x106,
        (
            "#12P#10704FI think it was because of you.\x02\x03",
            "#10702FIt was because of your advice that\x01",
            "we found the option of the\x01",
            "independence invalidity declaration.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1235")


    ChrTalk(
        0x8,
        (
            "#10602F#5PI didn't do a thing. You all achieved\x01",
            "everything yourselves...\x02\x03",
            "#10603F...If there was something I did do, it was\x01",
            "allowing the State Guard to go along with the\x01",
            "President's plan.\x02\x03",
            "#10608FNow that the legality of the independent state\x01",
            "has been crushed, I think that someone like me\x01",
            "has no right to be commanding officer.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(10)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(10)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x4, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(10)
    OP_63(0x5, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#12P#00011FT-That's...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_146F")

    ChrTalk(
        0x10A,
        (
            "#12P#00606FThere's no need for you\x01",
            "to be so hard on\x01",
            "yourself.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1521")

    label("loc_146F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_14CE")

    ChrTalk(
        0x105,
        (
            "#12P#10406FThere's no need for you\x01",
            "to be so hard on\x01",
            "yourself, right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1521")

    label("loc_14CE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1521")

    ChrTalk(
        0x109,
        (
            "#12P#10113FThere's no need for you\x01",
            "to be so hard on\x01",
            "yourself!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1521")


    ChrTalk(
        0x8,
        (
            "#10602F#5PBut of course. I'm well\x01",
            "aware of what I should\x01",
            "do.\x02\x03",
            "#10604FAfter everything is over,\x01",
            "I'm not exactly sure,\x01",
            "but...\x02\x03",
            "#10600FFor now, I'll do\x01",
            "everything I can as their\x01",
            "commanding officer.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_4C(0x8, 0xFF)
    OP_93(0x8, 0x10E, 0x0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x1AC, 0)
    EventEnd(0x5)
    Return()

    # Function_8_A64 end

    SaveToFile()

Try(main)
