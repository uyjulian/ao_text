from ScenarioHelper import *

def main():
    CreateScenaFile(
        "e4010.bin",                # FileName
        "e4010",                    # MapName
        "e4010",                    # Location
        0x0000,                     # MapIndex
        "ed7000",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    )

    BuildStringList((
        "e4010",                  # 0
        "Blond hair youth",             # 1
        "Black hair soldier",             # 2
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(216, 0)                                        # 0

    ScpFunction((
        "Function_0_D8",           # 00, 0
        "Function_1_E8",           # 01, 1
        "Function_2_E9",           # 02, 2
    ))


    def Function_0_D8(): pass

    label("Function_0_D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_E7")
    ClearScenarioFlags(0x22, 0)
    Event(0, 2)

    label("loc_E7")

    Return()

    # Function_0_D8 end

    def Function_1_E8(): pass

    label("Function_1_E8")

    Return()

    # Function_1_E8 end

    def Function_2_E9(): pass

    label("Function_2_E9")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch11102.itc", 0x1E)
    LoadChrToIndex("chr/ch11300.itc", 0x1F)
    LoadChrToIndex("apl/ch51205.itc", 0x20)
    CreatePortrait(0, 16, 20, 528, 84, 0, 0, 512, 64, 0, 0, 512, 64, 0xFFFFFF, 0x0, "c_vis503.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu07300.itp")
    CreatePortrait(2, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu07200.itp")
    SetChrPos(0x0, -7000, 0, 2000, 0)
    SetChrPos(0x1, -7000, 0, 2000, 0)
    SetChrPos(0x2, -7000, 0, 2000, 0)
    SetChrPos(0x3, -7000, 0, 2000, 0)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 0, 50, 7100, 180)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, -7500, 0, -3000, 90)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Sleep(500)
    Sound(103, 0, 100, 0)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Voice of a young man")

    AnonymousTalk(
        0xFF,
        "─ ─ Are you still awake?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapObjFlags(0x3, 0x10)
    OP_70(0x3, 0x5)
    OP_68(-6000, 1000, -3000, 0)
    MoveCamera(309, 21, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21500, 0)
    PlayBGM("ed7515", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x203), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1000, 0)
    OP_68(0, 1000, 5900, 8000)
    MoveCamera(315, 21, 0, 8000)
    SetCameraDistance(18500, 8000)

    def lambda_2D6():
        OP_95(0xFE, -4000, 0, -3000, 1800, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2D6)

    def lambda_2F0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_2F0)
    Sleep(1000)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    WaitChrThread(0x9, 1)

    def lambda_31B():
        OP_95(0xFE, 0, 0, 4300, 1800, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_31B)
    Sound(104, 0, 100, 0)
    OP_71(0x3, 0x5, 0x0, 0x0, 0x0)
    Sleep(3500)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    WaitChrThread(0x9, 1)
    TurnDirection(0x9, 0x8, 500)
    OP_6F(0x79)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x9,
        (
            "I am leaving early tomorrow.\x01",
            "How bad, how about going to bed?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)

    ChrTalk(
        0x8,
        (
            "#11P#07208F#30WOh … yeah ….\x02\x03",
            "#07203FOnce, also in this report\x01",
            "I want to keep it through.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6P#07303FMilitary academy? ….\x02\x03",
            "#07302FYou surely will not\x01",
            "It is nice to seriously take care of your duties.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#07204FHough, to the last\x01",
            "It is only a nominally director, though.\x02\x03",
            "#07200FThey seem to be doing their best,\x01",
            "I have to do this much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6P#07304FFu … Well it will be nice.\x02\x03",
            "#07300F─ ─ But apparently\x01",
            "The story of the example seems to be certain.\x02\x03",
            "The hand of the Duke of Cayenne\x01",
            "It seems that she is secretly turning his hand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#07206FThat human … ….\x01",
            "I thought it was such a place though.\x02\x03",
            "#07200FDo you grasp the scale?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6P#07303FNo, that is unknown.\x02\x03",
            "#07300FThe information station is also around here\x01",
            "It seems like I misplaced you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#07209FAhaha, though it is self-owned\x01",
            "The Prime Minister is also a disaster.\x02\x03",
            "#07202FHuh, unexpectedly got together\x01",
            "Are you planning to target?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6P#07306F…… It is not stylish.\x02\x03",
            "#07301FAgain the escort from the seventh division\x01",
            "Is not it better to increase the number?\x02\x03",
            "It will be possible to screw in from now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#07204FNo, it does not reach that.\x02\x03",
            "Regardless of the cabinet minister,\x01",
            "I will do it with my character\x01",
            "It will also spoil the image we have built.\x02\x03",
            "#07202FAnd besides\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(400)
    Sound(822, 0, 100, 0)
    OP_63(0x8, 0x12C, 1300, 0x36, 0x39, 0xFA, 0x0)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x8, 0x2)
    SetChrFlags(0x8, 0x20)
    SetCameraDistance(18200, 400)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0x8, 0x20)
    SetChrSubChip(0x8, 0x0)
    Sleep(100)
    SetChrSubChip(0x8, 0x1)
    Sleep(800)

    ChrTalk(
        0x8,
        (
            "#11P#07209FBecause I have you There is a jet\x02\x03",
            "#07212FIf you can protect in your arms\x01",
            "Already enough for that!\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x8)
    OP_63(0x8, 0x0, 1700, 0xA, 0xB, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1200)
    OP_93(0x9, 0xB4, 0x1F4)

    ChrTalk(
        0x9,
        "#11P#07303F─ ─ Well, I also want to sleep early.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0x8, 0x2)
    ClearChrFlags(0x8, 0x20)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    OP_0D()
    Sleep(100)

    ChrTalk(
        0x8,
        (
            "#11P#07206FSumimasen, I rode.\x02\x03",
            "#07200FEither way, within tomorrow\x01",
            "I wish I could talk to Hime Hime.\x02\x03",
            "How 's your arrangement?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x9, 0x0, 0x1F4)

    ChrTalk(
        0x9,
        (
            "#6P#07304FOh, I got in touch with Associate.\x02\x03",
            "#07302FAfter the luncheon tomorrow ─ ─\x01",
            "It will be about evening.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#07202FReally……\x01",
            "It's about 1 year ago.\x02\x03",
            "#07206FIf the esters you left\x01",
            "I could open an alumni association.\x02\x03",
            "#07208FBecause Shella seems too busy\x01",
            "I can not afford a business trip.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#6P#07303F… … That's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#07204FWell, at the most you\x01",
            "A state-of-the-art urban resort\x01",
            "I will assume that I will fully enjoy it.\x02\x03",
            "#07212FOh, I have an association between you and the Associate\x01",
            "I will not disturb you.\x01",
            "Before relieving me spray\x02\x03",
            "#07209FWhat on earth rumor theme park\x01",
            "How about going out?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6P#07306F── It is unnecessary care, fool.\x02\x03",
            "#07303FBut more than usual\x01",
            "It seems that there are a lot of downplay drama.\x02\x03",
            "#07301F…… No wonder thing\x01",
            "You probably do not think so?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#07211FGiggle\x02\x03",
            "#07209FHa ha ha, Yadanabe.\x01",
            "Sonna Wake ni Yanaika.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6P#07308F(… … tomorrow on the neck\x01",
            "Would you like to attach rope too? )\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x8,
        (
            "─ ─ Maybe,\x01",
            "This will be the last outing.\x02\x03",
            "While exploring the aim of the Chancellor,\x01",
            "Also see trends across continents …\x02\x03",
            "I still struggle as usual\x01",
            "Regards, I'm counting on you.\x02",
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

    ChrTalk(
        0x9,
        "#6P#07304FHuh, of course.\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(18700, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    OP_CC(0x1, 0xFF, 0x0)
    Sleep(1000)
    SetScenarioFlags(0x22, 0)
    NewScene("e430B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_2_E9 end

    SaveToFile()

Try(main)
