from ScenarioHelper import *

def main():
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
        "Sister · Lease",       # 1
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
            "After that, Lloyd's\x01",
            "It was guided to Sister · Lease's private room … …\x02\x03",
            "History of picking a blue flower\x01",
            "On the interaction with Archbishop Ellarda\x01",
            "I explained to her all the way.\x07\x00\x02",
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
            "#04406F#11PI see\x02\x03",
            "#04408FCertainly this is the Archbishop\x01",
            "It is also impossible to close your mouth.\x02",
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
        "#00005F#12P!?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7C, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_93D")

    ChrTalk(
        0x104,
        "#00305F#12PDo you understand, Mr. Sister! Is it?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x102, 500)

    ChrTalk(
        0x8,
        (
            "#04403F#5Pbefore that……\x02\x03",
            "#04402F…… Ellie.\x01",
            "About my status yet\x01",
            "Does not it seem to explain?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#11PYeah ….\x01",
            "To say too much\x01",
            "Please feel it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#04404F#5PHehe … … I thank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10105F#12PEr …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00201F#6PIs that status alright …?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 500)

    ChrTalk(
        0x8,
        (
            "#04403F#5PTo the Archbishop is thin,\x01",
            "It seems to have been hit … …\x02\x03",
            "Even within the church,\x01",
            "I belong to a special organization.\x02\x03",
            "#04400F── \"Star Cup Order\".\x01",
            "It belongs to the institution named Seaplane Province\x01",
            "Ancient artifacts#8RArtifact#It is an organization that collects.\x02",
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
        "#00011F#12PKnights of the Star Cup … …!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10111F#12PAt Altair Lodge\x01",
            "He lent me a hand …! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04404F#5PIt is Kevin Graham.\x02\x03",
            "#04402FBy the way, I support him,\x01",
            "It is on the rank of \"Adjunctor\".\x02\x03",
            "#04406FOriginally, for various investigations\x01",
            "He himself enters the crossbell\x01",
            "Although it was a line, … ….\x02\x03",
            "#04400FBecause there was an archbishop's eyes\x01",
            "Instead I as an information collector\x01",
            "It was dispatched.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F#12PI see, I see … ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00102F#11PIs that so……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#12PSomehow, church too\x01",
            "You seem to have a lot of distortions?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04403F#5PYeah, shy.\x02\x03",
            "#04408F── I will return the story\x01",
            "Flowers from which everyone collected …\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x10E, 0x1F4)
    Sleep(300)
    Jump("loc_99B")

    label("loc_93D")


    ChrTalk(
        0x104,
        "#00305F#12PYou know it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#04408F#11PYes. The flower you found\x02",
    )

    CloseMessageWindow()

    label("loc_99B")

    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Sleep(300)

    AnonymousTalk(
        0x8,
        (
            "#04403FCertainly, it is in a certain scripture\x01",
            "The possibility that it is a flower seems to be high.\x02\x03",
            "#04401FAlthough it is not an official scripture\x01",
            "The so-called \"foreign civilization#4RGesshin#\"Although it corresponds to.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x109,
        "#10105FEvil scripture…\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x105,
        (
            "#10301FIn other words, what is formal\x01",
            "Is not it an unauthorized opposition?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x8,
        (
            "#04403FYes, only limited people in the church\x01",
            "Browsing is not allowed.\x02\x03",
            "#04400FBut who belongs to the \"knights\"\x01",
            "You are allowed to browse such a censure.\x02\x03",
            "The existence of dangerous artifacts\x01",
            "It is because there are many things written.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x101,
        "#00005FI see\x02",
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
            "#00101F#11PSo, that blue flower\x01",
            "How is it written …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04403F#11POne of the outer writings \"ladder note\"\x01",
            "There is a depiction about the blue flower.\x02\x03",
            "#04408FIt blooms right above the seven angels,\x01",
            "Kichiro is a mysterious flower that can be taken as an obsession … …\x02\x03",
            "#04401FIt's called the Pleroma Flower\x02",
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
        "#00007F#4S#12PAh!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00107F#11PThat name is!\x02",
    )

    CloseMessageWindow()
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(300)

    AnonymousTalk(
        0x109,
        "#10101FThat is…\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x105,
        (
            "#10305FIt was left in the terminal of \"cult\"\x01",
            "Is it the name of the plant that became the source of Gnostic?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x103,
        "#00206FRight..\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x104,
        (
            "#00301FNo way, at such a place\x01",
            "I do not hear that name … …\x02",
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
            "#04403F#5PI see, so that's it\x02\x03",
            "#04401FAbout the mystery left by the faction\x01",
            "Almost nothing has been elucidated in the church.\x02\x03",
            "There was also the intention of Archbishop Ellarda,\x01",
            "Also the incident caused by Joachim Gunter\x01",
            "Although almost not investigated … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10111F#12PW-wait a second \x02\x03",
            "#10106FThat flower really\x01",
            "Examples of drugs of Gnostic\x01",
            "As a raw material ……\x02\x03",
            "#10101FIt was discovered in various places\x01",
            "What does it mean?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#11PWell, well …\x01",
            "The emergence of \"Phantom beast\" is also anxious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F#6PA flower right above the church\x02\x03",
            "#00201FBesides, both\x01",
            "Is it a flower that I can take?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00306F#12PIt gives you a bad feeling\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00003F#11P─ ─ Anyway, only us\x01",
            "It does not seem to be a manageable problem.\x02\x03",
            "Once you return to the support department\x01",
            "Let's summarize the detailed report.\x02\x03",
            "#00001FMr. Lease.\x01",
            "The information you have taught me\x01",
            "Even if you tell the guard or guild?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04403F#5PWell\x02\x03",
            "#04400FMake my name as possible\x01",
            "If you can not give it out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#12PFor Huff, Archbishop\x01",
            "It is like a spy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F#11POf course, that\x01",
            "We will consider as much as possible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04404F#5PIn that case there's no problem\x02\x03",
            "#04402FSince I also contacted the Order,\x01",
            "I am planning to enter the survey.\x02\x03",
            "If there is any progress with each other\x01",
            "How is it to exchange information?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002F#12PYes, gladly\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00202F#6PThanks for your help\x02",
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
            "After that, Lloyd's returned to support section\x01",
            "Phantom Beast and Blue Flower - About \"Praroma Grass\"\x01",
            "I summarized the detailed report in a hurry.\x02\x03",
            "For the command of the Guard and the reception of the guild\x01",
            "After sending the report through the power net … …\x02\x03",
            "Lloyds who were tired after traveling around the world\x01",
            "After having taken a late dinner with the section chief and Kaoru\x01",
            "I decided to go back to the room and take a day off.\x07\x00\x02",
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
