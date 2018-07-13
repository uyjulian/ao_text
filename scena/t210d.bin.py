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
        "Function_4_3AE",          # 04, 4
        "Function_5_609",          # 05, 5
        "Function_6_814",          # 06, 6
        "Function_7_940",          # 07, 7
        "Function_8_AD5",          # 08, 8
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
            "Since you have too many, you gave it up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x2, 0x1E, 0x0, 0x0, 0x0)

    label("loc_353")

    Jump("loc_3A2")

    label("loc_358")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is nothing in the chest. \x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_3A2")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_25C end

    def Function_4_3AE(): pass

    label("Function_4_3AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AC, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BC")
    Call(0, 8)
    Return()

    label("loc_3BC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_55E")

    ChrTalk(
        0x8,
        (
            "#10600FRegarding the future course of action,\x01",
            "Vice Commander Douglas has gone to\x01",
            "discuss it with Chairman MacDowell.\x02\x03",
            "As the commanding officer of a regular army,\x01",
            "I have to make full preparations against the\x01",
            "Empire and Republic.\x02\x03",
            "#10603FAfter everything is over, I still\x01",
            "don't know what I'll do, but...\x02\x03",
            "#10600FAt any rate, for now I'll only do as much\x01",
            "as possible as the commanding officer.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_605")

    label("loc_55E")


    ChrTalk(
        0x8,
        (
            "#10603FAfter everything is over, I still\x01",
            "don't know what I'll do, but...\x02\x03",
            "#10600FAt any rate, for now I'll only do as much\x01",
            "as possible as the commanding officer.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_605")

    TalkEnd(0xFE)
    Return()

    # Function_4_3AE end

    def Function_5_609(): pass

    label("Function_5_609")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_743")

    ChrTalk(
        0x9,
        (
            "It seems that in the Empire,\x01",
            "in the course of the civil war,\x01",
            ""airwarships" were developed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If they add such things to the\x01",
            "Imperial Army armored division,\x01",
            "honestly, things will be out of hand...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If we had those "Aions"...\x01",
            "I wonder if I'm the only one\x01",
            "who's thinking like that...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_810")

    label("loc_743")


    ChrTalk(
        0x9,
        (
            "If they add an "airwarship" thing to\x01",
            "the Imperial Army armored division,\x01",
            "honestly, things will be out of hand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If we had those "Aions"...\x01",
            "I wonder if I'm the only one\x01",
            "who's thinking like that...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_810")

    TalkEnd(0xFE)
    Return()

    # Function_5_609 end

    def Function_6_814(): pass

    label("Function_6_814")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_89C")

    ChrTalk(
        0xA,
        (
            "I'm glad we lost\x01",
            "the "Aions".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I can't think someone like\x01",
            "us could ever use weapons\x01",
            "with that much power.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_93C")

    label("loc_89C")


    ChrTalk(
        0xA,
        (
            ""Aions"...I think it would be impossible\x01",
            "for us to use something like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "...Looking at Garrelia Fortress state,\x01",
            "chills run down my spine even now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_93C")

    TalkEnd(0xFE)
    Return()

    # Function_6_814 end

    def Function_7_940(): pass

    label("Function_7_940")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_AD1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A40")

    ChrTalk(
        0xB,
        (
            "Thinking to go back to the Empire somehow,\x01",
            "I came to Bellguard Gate, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "W-Who could've thought that "Garrelia\x01",
            "Fortress" would've turned into that...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "N-Now going home has become\x01",
            "impossible no matter what...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_AD1")

    label("loc_A40")


    ChrTalk(
        0xB,
        (
            "W-Who could've thought that "Garrelia\x01",
            "Fortress" would've turned into that...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "N-Now going home has become\x01",
            "impossible no matter what...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AD1")

    TalkEnd(0xFE)
    Return()

    # Function_7_940 end

    def Function_8_AD5(): pass

    label("Function_8_AD5")

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
            "#12P#00002FCommander Sonya...\x01",
            "So you were here.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x5A, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x8,
        "#10605F#5PYou guys...\x02",
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
            "#00301F...Great state, huh?\x02\x03",
            "#00303FWe saw footage of that white doll\x01",
            "erasin' the Railway Cannons\x01",
            "without a trace, but...\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    AnonymousTalk(
        0x101,
        (
            "#00008F...It was indirectly, but\x01",
            "this happened due to\x01",
            "KeA's power...\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    AnonymousTalk(
        0x8,
        (
            "#10603F...This is uncertain intel\x01",
            "we have received from\x01",
            "the Empire side, but...\x02\x03",
            "#10600FIt seems that in that "Aion" attack\x01",
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
            "#12P#00105FC-Considering the situation,\x01",
            "I can only say it was a miracle...\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    AnonymousTalk(
        0x8,
        (
            "#10600FBecause we can't confirm the truth,\x01",
            "we don't know the actual facts, but...\x02\x03",
            "#10604FIt could've been a power that\x01",
            "erases only inorganic substance\x01",
            "without involving human beings.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    AnonymousTalk(
        0x103,
        (
            "#12P#00202FIf that is true, KeA could\x01",
            "have meddled with the\x01",
            ""miracle" unconsciously.\x02\x03",
            "#00204FAlthough there is no doubt that the\x01",
            "Empire received enormous damage...\x01",
            "I am just a little relieved.\x02",
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
            "#10604F#5P...I've heard the news.\x02\x03",
            "#10602FIt seems that the Crossbell City\x01",
            "liberation operation went well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#00309FHa ha, honestly, you did too much.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1160")

    ChrTalk(
        0x109,
        (
            "#12P#10104FIt's thanks to you, Commander Sonya!\x02\x03",
            "#10102FBecause we had your advice,\x01",
            "we were able to find out the option of\x01",
            "the independence declaration of invalidity!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12DF")

    label("loc_1160")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_122C")

    ChrTalk(
        0x105,
        (
            "#12P#10400FHu hu, that too was thanks to you, Commander.\x02\x03",
            "#10404FBecause we had your advice,\x01",
            "we were able to find out the option of\x01",
            "the independence declaration of invalidity...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12DF")

    label("loc_122C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_12DF")

    ChrTalk(
        0x106,
        (
            "#12P#10704FI think it's thanks to you.\x02\x03",
            "#10702FBecause we had your advice,\x01",
            "we were able to find out the option of\x01",
            "the independence declaration of invalidity.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12DF")


    ChrTalk(
        0x8,
        (
            "#10602F#5PUh uh, I didn't do anything.\x01",
            "You achieved everything yourselves...\x02\x03",
            "#10603F...If you want to say something I did,\x01",
            "it was only making use of the State Guard\x01",
            "going with the flow of the President's plan.\x02\x03",
            "#10608FNow that the legality of the independent state\x01",
            "has been crushed, I think that a person like\x01",
            "me has no right to be the commanding officer.\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_153E")

    ChrTalk(
        0x10A,
        (
            "#12P#00606F...I think you don't have to\x01",
            "think about it to that extent.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15FB")

    label("loc_153E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_15A6")

    ChrTalk(
        0x105,
        (
            "#12P#10406F...I think you don't have to\x01",
            "think about it to that extent, right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15FB")

    label("loc_15A6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_15FB")

    ChrTalk(
        0x109,
        (
            "#12P#10113FYou don't have to think\x01",
            "about it to that extent...!?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15FB")


    ChrTalk(
        0x8,
        (
            "#10602F#5PUh uh, of course now I'm well\x01",
            "aware about what I should do.\x02\x03",
            "#10604FAfter everything is over, I still\x01",
            "don't know what I'll do, but...\x02\x03",
            "#10600FAt any rate, for now I'll only do as much\x01",
            "as possible as the commanding officer.\x02",
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

    # Function_8_AD5 end

    SaveToFile()

Try(main)
