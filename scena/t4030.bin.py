from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t4030.bin",                # FileName
        "t4030",                    # MapName
        "t4030",                    # Location
        0x0000,                     # MapIndex
        "ed7124",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x1F,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    )

    BuildStringList((
        "t4030",                  # 0
        "Sister Ries",            # 1
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(188, 0)                                        # 0

    ScpFunction((
        "Function_0_BC",           # 00, 0
        "Function_1_CF",           # 01, 1
        "Function_2_E5",           # 02, 2
    ))


    def Function_0_BC(): pass

    label("Function_0_BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_CE")
    ClearScenarioFlags(0x22, 0)
    SetScenarioFlags(0x0, 0)
    Event(0, 2)

    label("loc_CE")

    Return()

    # Function_0_BC end

    def Function_1_CF(): pass

    label("Function_1_CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_E4")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 0)

    label("loc_E4")

    Return()

    # Function_1_CF end

    def Function_2_E5(): pass

    label("Function_2_E5")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch14000.itc", 0x1E)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis253.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis254.itp")
    OP_68(-1080, 3200, 2970, 0)
    MoveCamera(40, 21, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(23880, 0)
    SetChrPos(0x101, -1100, 0, 2650, 0)
    SetChrPos(0x102, -200, 0, 2350, 315)
    SetChrPos(0x103, -2400, 0, 2200, 45)
    SetChrPos(0x104, -950, 0, 750, 0)
    SetChrPos(0x109, -1750, 0, 1250, 0)
    SetChrPos(0x105, 200, 0, 1100, 315)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, -1100, 0, 4000, 270)
    SetChrPos(0x8, -800, 0, 4030, 270)
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Afterwards, Lloyd and the\x01",
            "others were shown to Sister\x01",
            "Ries' room...\x02\x03",
            "They told her about the\x01",
            "flowers they picked and their\x01",
            "arguments with the Archbishop.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    PlayBGM("ed7573", 0)
    OP_68(-1080, 1200, 2970, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x8,
        (
            "#04406F#11P─I see.\x02\x03",
            "#04408FIndeed. It's understandable\x01",
            "that the Archbishop won't\x01",
            "tell you about them.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005F#12PHuh!?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7C, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9B0")

    ChrTalk(
        0x104,
        (
            "#00305F#12PYou know something,\x01",
            "Sister!?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x102, 500)

    ChrTalk(
        0x8,
        (
            "#04403F#5PBefore that...\x02\x03",
            "#04402FElie. It seems you\x01",
            "haven't told them about\x01",
            "my position?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#11PThat's right... I was\x01",
            "thinking of telling them\x01",
            "indirectly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#04404F#5PHaha... Thank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10105F#12PUmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00201F#6PWhat could your position\x01",
            "be?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 500)

    ChrTalk(
        0x8,
        (
            "#04403F#5PIt seems the Archbishop already has\x01",
            "a vague idea, but...\x02\x03",
            "I am a member of a special\x01",
            "organization even within the Church.\x02\x03",
            "#04400F─The "Gralsritter". An organization\x01",
            "that collects artifacts, and part of\x01",
            "the Congregation for the Sacraments.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00011F#12PThe Gralsritter!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10111F#12PThey helped us at Altair\x01",
            "Lodge!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04404F#5PKevin Graham, right?\x02\x03",
            "#04402FBy the way, I hold the rank of "squire" and\x01",
            "support him.\x02\x03",
            "#04406FOriginally, the plan was for Kevin himself\x01",
            "to come to Crossbell for various\x01",
            "investigations, but...\x02\x03",
            "#04400FBecause of the watchful eyes of the\x01",
            "Archbishop, I was dispatched as a temporary\x01",
            "sister to gather intelligence instead.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F#12PI-I see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00102F#11PSo that's what it was...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#12POr like, it seems the\x01",
            "Church has its own\x01",
            "various restraints.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04403F#5PYes, although it's\x01",
            "embarrassing to admit.\x02\x03",
            "#04408F─Getting back to the\x01",
            "subject, the flowers you\x01",
            "all picked up...\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x10E, 0x1F4)
    Sleep(300)
    Jump("loc_A09")

    label("loc_9B0")


    ChrTalk(
        0x104,
        "#00305F#12PYou know them, Ries!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04408F#11PYes, the flowers you all\x01",
            "picked...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A09")

    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Sleep(300)

    AnonymousTalk(
        0x8,
        (
            "#04403FIndeed, it's likely they're the\x01",
            "same flowers mentioned in a\x01",
            "certain volume of the Testaments.\x02\x03",
            "#04401FNot an official one, but rather\x01",
            "one of the so-called "Apocrypha".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x109,
        "#10105FApocrypha...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x105,
        (
            "#10301FIn other words, a\x01",
            "Testament that isn't\x01",
            "recognized as official?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x8,
        (
            "#04403FYes. Even within the\x01",
            "Church, only a select few\x01",
            "are permitted to read them.\x02\x03",
            "#04400FHowever, members of the\x01",
            ""Gralsritter" are allowed\x01",
            "to read them.\x02\x03",
            "After all, the existence of\x01",
            "many dangerous artifacts is\x01",
            "recorded therein.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x101,
        "#00005FI see...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    ChrTalk(
        0x102,
        (
            "#00101F#11PThen, what is written\x01",
            "about these azure\x01",
            "flowers?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04403F#11PThey're described in "The Book\x01",
            "of Rader", one of the apocrypha.\x02\x03",
            "#04408FBlooming atop septium veins,\x01",
            "they are mysterious flowers seen\x01",
            "as both good and bad omens.\x02\x03",
            "#04401FTheir name is also recorded:\x01",
            ""Pleroma Grass".\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x101,
        "#00007F#4S#12PWha...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00107F#11PThat name...!\x02",
    )

    CloseMessageWindow()
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(300)

    AnonymousTalk(
        0x109,
        "#10101FI-Isn't that...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x105,
        (
            "#10305FIsn't that the name of the plant\x01",
            "used as a Gnosis ingredient left\x01",
            "behind in the "Cult's" terminals?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x103,
        "#00206F...Yes...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x104,
        (
            "#00301FTo think we'd hear that\x01",
            "name in a place like\x01",
            "this...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    TurnDirection(0x8, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#04403F#5P...I understand, so that's what happened.\x02\x03",
            "#04401FVery few of the mysteries left behind by\x01",
            "that cult have been explained by the\x01",
            "Church.\x02\x03",
            "Archbishop Eralda has his ideas, but\x01",
            "there's been very little investigation into\x01",
            "the incident Joachim Gｸnther caused...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10111F#12PP-Please, wait a moment.\x02\x03",
            "#10106FIf those flowers really\x01",
            "were an ingredient of that\x01",
            "Gnosis drug...\x02\x03",
            "#10101FWell, what meaning could it\x01",
            "have that we found it in\x01",
            "all those different places?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#11PT-That's right... I'm\x01",
            "also worried about\x01",
            "Cryptids showing up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F#6PFlowers that bloom atop\x01",
            "septium veins...\x02\x03",
            "#00201FFurthermore, they bring\x01",
            "both good and ill\x01",
            "omens...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#12PYeah, quite the bad\x01",
            "coincidence.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00003F#11P─Anyhow, this doesn't seem\x01",
            "like a problem we can deal\x01",
            "with alone.\x02\x03",
            "Let's return to the Support\x01",
            "Section for now and try to put\x01",
            "together a detailed report.\x02\x03",
            "#00001FRies. Can we convey what you\x01",
            "told us to the CGF and guild\x01",
            "as well?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04403F#5PLet's see...\x02\x03",
            "#04400FIf you can do me the\x01",
            "favor of not mentioning\x01",
            "my name at all...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#12PHehe. To the Archbishop,\x01",
            "you're like a spy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F#11POf course, we'll be as\x01",
            "careful as we can be.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04404F#5PIn that case there's no\x01",
            "problem.\x02\x03",
            "#04402FAfter I contact the\x01",
            "Gralsritter, I intend to join\x01",
            "the investigation as well.\x02\x03",
            "Why don't we exchange\x01",
            "information if there's any\x01",
            "progress?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002F#12PYes, we'd be happy to.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00202F#6PWe're counting on you.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Afterwards, Lloyd and the others returned to the Support\x01",
            "Section and hurriedly put together a report about the\x01",
            "Cryptids and azure flowers─ the Pleroma Grass.\x02\x03",
            "After sending the report through the orbal net to the\x01",
            "CGF commander and guild reception desk...\x02\x03",
            "Tired from having gone all over the state, after a late\x01",
            "dinner with Chief and KeA, they returned to their rooms\x01",
            "and decided to rest early that night.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_32(0xFF, 0xFE, 0x0)
    OP_CC(0x1, 0xFF, 0x0)
    Sleep(1000)
    SetScenarioFlags(0x22, 0)
    NewScene("m0001", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_2_E5 end

    SaveToFile()

Try(main)
