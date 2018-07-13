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
            "Afterwards, Lloyd and the others were\x01",
            "guided to Sister Ries' private room...\x02\x03",
            "They explained in general to her the\x01",
            "story about the Azure Flowers and\x01",
            "their arguing with the Archbishop.\x07\x00\x02",
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
            "#04406F#11P──I see.\x02\x03",
            "#04408FIndeed, being the Archbishop it can't be\x01",
            "helped that he doesn't want to talk about them.\x02",
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
        "#00005F#12PHuh...!?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7C, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9FD")

    ChrTalk(
        0x104,
        "#00305F#12PMiss Sister, do you know something!?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x102, 500)

    ChrTalk(
        0x8,
        (
            "#04403F#5PBefore that...\x02\x03",
            "#04402F...Miss Elie.\x01",
            "It seems you haven't told\x01",
            "them about my status yet...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#11PNo, I haven't...\x01",
            "I wondered about how to express\x01",
            "that in a roundabout way...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#04404F#5PUh uh...thank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10105F#12PEhhm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00201F#6PWhat could that status be...?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 500)

    ChrTalk(
        0x8,
        (
            "#04403F#5PIt appears it was already slightly\x01",
            "sensed by the Archbishop, but...\x02\x03",
            "I belong to a special organization\x01",
            "among the Church.\x02\x03",
            "#04400F──The "Gralsritter".\x01",
            "It's an organization that collect Artifacts.\x01",
            "It belongs to the Congregation for the Sacraments.\x02",
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
        "#00011F#12PThe Gralsritter...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10111F#12PThey helped us at\x01",
            "the Altair Lodge...!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04404F#5PKevin Graham, right?\x02\x03",
            "#04402FSpeaking about him, I have the \x01",
            "rank of "squire" and I support him.\x02\x03",
            "#04406FOriginally, the plan was for\x01",
            "him to come to Crossbell for\x01",
            "various investigations, but...\x02\x03",
            "#04400FBeing not very liked by the Archbishop,\x01",
            "I was dispatched as intelligence\x01",
            "gatherer instead of him.\x02",
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
        "#00102F#11PIs that so...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#12POr like, it seems that even the Church\x01",
            "has got a variety of restraints.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04403F#5PYes, it's very embarrassing.\x02\x03",
            "#04408F──Going back to the subject,\x01",
            "the flowers you all picked up...\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x10E, 0x1F4)
    Sleep(300)
    Jump("loc_A66")

    label("loc_9FD")


    ChrTalk(
        0x104,
        "#00305F#12PDear Ries, do you know something!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#04408F#11PYes, the flowers you all picked up...\x02",
    )

    CloseMessageWindow()

    label("loc_A66")

    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Sleep(300)

    AnonymousTalk(
        0x8,
        (
            "#04403FIt's indeed highly likely they're those\x01",
            "mentioned in a certain Testaments.\x02\x03",
            "#04401FAlthough I should say they're not the official\x01",
            "Testaments but the so called "Apocrypha".\x02",
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
            "#10301FIn other words, an alternative\x01",
            "version not officially approved...?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x8,
        (
            "#04403FYes. Even in the Church, their reading\x01",
            "is allowed only to limited individuals.\x02\x03",
            "#04400FHowever, the reading of those Apocrypha is\x01",
            "allowed to those belonging to the "Gralsritter".\x02\x03",
            "After all, they record the existence\x01",
            "of many dangerous Artifacts.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x101,
        "#00005FI understand...\x02",
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
            "#00101F#11PThen, these Azure Flowers...\x01",
            "Where're they mentioned...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04403F#11PIn the "Book of Rader", one of the Apocrypha, \x01",
            "there's the depiction of Azure Flowers.\x02\x03",
            "#04408FThey bloom right above Septium veins,\x01",
            "mysterious flowers that brings both\x01",
            "good and ill omens...\x02\x03",
            "#04401FTheir name is also recorded: "Pleroma Grass".\x02",
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
        "#00007F#4S#12PWHA...!?\x02",
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
            "#10305FIsn't that the name left in the "Cult" terminals,\x01",
            "the name of the plant used as Gnosis ingredient?\x02",
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
            "#00301FTo think we'd hear than\x01",
            "name in such a place...\x02",
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
            "#04401FThe mysteries left behind by that Cult haven't \x01",
            "almost been explained by the Church too.\x02\x03",
            "There're also Archbishop Eralda's ideas,\x01",
            "and so even the incident Joachim Gｸnther\x01",
            "has cause hasn't been quite researched...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10111F#12PP-Please, wait a moment.\x02\x03",
            "#10106FIf those flowers are really\x01",
            "the ingredient of that\x01",
            "drug called Gnosis...\x02\x03",
            "#10101FWell, what meaning could it have\x01",
            "that's been spotted in all places...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#11PY-You have a point...\x01",
            "I'm also worried about the "Cryptids" showing up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F#6PFlowers that bloom right above Septium veins...\x02\x03",
            "#00201FFurthermore, flowers that bring\x01",
            "both good and ill omens...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00306F#12PYeah, quite the bad coincidence.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00003F#11P──In any case, it doesn't seem a\x01",
            "matter that we alone can deal with.\x02\x03",
            "Let's return to the Support Section for now and\x01",
            "try to put together a detailed written report.\x02\x03",
            "#00001FMiss Ries.\x01",
            "Can we convey what you told us\x01",
            "to the CGF and the Guild too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04403F#5PLet's see...\x02\x03",
            "#04400FIf you can do me the favor to\x01",
            "not mention my name at all...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#12PHu hu, for the Archbishop\x01",
            "you'll be like a spy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F#11POf course, we'll be considerate\x01",
            "about that as much as possible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04404F#5PThen, I have no problem with that.\x02\x03",
            "#04402FAfter I contact the Gralsritter, I too\x01",
            "intend to join the investigation.\x02\x03",
            "What do you say if we exchange information\x01",
            "with each other if there're any progresses?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002F#12PYes, gladly.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00202F#6PThank you very much.\x02",
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
            "Afterwards, Lloyd and the other returned to the SSS.\x01",
            "They urgently put together a detailed written report \x01",
            "about Cryptids and the Azure Flowers──"Pleroma Grass".\x02\x03",
            "After sending the report through the orbal net\x01",
            "to the CGF Commander and the Guild reception...\x02\x03",
            "Being tired for having gone around all places, after having\x01",
            "had a late dinner with the Chief and KeA, they went back to\x01",
            "their rooms and decided to rest early.\x07\x00\x02",
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
