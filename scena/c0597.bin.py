from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c0597.bin",                # FileName
        "c0597",                    # MapName
        "c0597",                    # Location
        0x0029,                     # MapIndex
        "ed7302",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 41, 0, 0, 0, 1],
    )

    BuildStringList((
        "c0597",                  # 0
        "Kilika",                 # 1
        "Lechter",                # 2
        "Dummy",                  # 3
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    246,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(0,       0,       64000,   1200,    0,       1500,    64000,   0x007C, 0,  2,  0x0000)

    ChipFrameInfo(288, 0)                                        # 0

    ScpFunction((
        "Function_0_120",          # 00, 0
        "Function_1_121",          # 01, 1
        "Function_2_13E",          # 02, 2
        "Function_3_47D",          # 03, 3
        "Function_4_2FDD",         # 04, 4
    ))


    def Function_0_120(): pass

    label("Function_0_120")

    Return()

    # Function_0_120 end

    def Function_1_121(): pass

    label("Function_1_121")

    OP_65(0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_137")
    OP_66(0x0, 0x1)

    label("loc_137")

    ClearMapObjFlags(0x10, 0x10)
    Return()

    # Function_1_121 end

    def Function_2_13E(): pass

    label("Function_2_13E")

    EventBegin(0x0)
    Fade(500)
    OP_68(0, 1150, 63000, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21000, 0)
    SetChrPos(0x101, 0, 30, 62300, 0)
    SetChrPos(0x102, -900, 30, 60400, 0)
    SetChrPos(0x104, 900, 30, 60400, 0)
    SetChrPos(0x103, -300, 30, 59700, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00003F#11P(Lechter Arundel, from the\x01",
            "Imperial Army Intelligence Division.)\x02\x03",
            "#00013F(Someone we must be careful with...\x01",
            "If we're going to enter, let's be really resolute.)\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(814, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "After you enter the room, you will\x01",
            "not be able to adjust equipment,\x01",
            "items and orbments for a while.\x02\x03",
            "Also, please note that all the remaining\x01",
            "opened quests will be closed.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(300)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[We Still Have Something To Do]\x01",      # 0
            "[Open the Door and Enter]\x01",            # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_3B1"),
        (0, "loc_460"),
        (SWITCH_DEFAULT, "loc_47C"),
    )


    label("loc_3B1")

    Sound(103, 0, 100, 0)
    OP_71(0x10, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x10)
    StopBGM(0xFA0)
    FadeToDark(1000, 0, -1)

    def lambda_3DA():
        OP_96(0xFE, 0x0, 0x0, 0x105B8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3DA)
    Sleep(300)

    def lambda_3F7():
        OP_96(0xFE, 0x0, 0x0, 0x105B8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3F7)
    Sleep(300)

    def lambda_414():
        OP_96(0xFE, 0x0, 0x0, 0x105B8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_414)
    Sleep(300)

    def lambda_431():
        OP_96(0xFE, 0x0, 0x0, 0x105B8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_431)
    OP_0D()
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x102, 0xFF)
    EndChrThread(0x104, 0xFF)
    EndChrThread(0x103, 0xFF)
    WaitBGM()
    Call(0, 3)
    Jump("loc_47C")

    label("loc_460")

    SetChrPos(0x0, 0, 30, 61800, 180)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Jump("loc_47C")

    label("loc_47C")

    Return()

    # Function_2_13E end

    def Function_3_47D(): pass

    label("Function_3_47D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50011.itc", 0x1E)
    LoadChrToIndex("chr/ch07300.itc", 0x1F)
    LoadChrToIndex("apl/ch51526.itc", 0x20)
    SoundLoad(803)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis007.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu03500.itp")
    CreatePortrait(2, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu03400.itp")
    SetChrPos(0x101, -700, 30, 101500, 0)
    SetChrPos(0x102, 300, 30, 101500, 0)
    SetChrPos(0x104, 500, 30, 100400, 0)
    SetChrPos(0x103, -900, 30, 100400, 0)
    SetChrPos(0xA, -200, 0, 107950, 0)
    SetChrChipByIndex(0x9, 0x20)
    SetChrSubChip(0x9, 0x0)
    SetChrFlags(0x9, 0x2)
    SetChrFlags(0x9, 0x10)
    SetChrFlags(0x9, 0x20)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, -100, 100, 112500, 180)
    SetChrChipByIndex(0x8, 0x1F)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 0, 0, 98000, 0)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(0, 1000, 112500, 0)
    MoveCamera(27, 19, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16000, 0)

    def lambda_603():
        OP_97(0x101, 0x0, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_603)
    Sleep(100)

    def lambda_620():
        OP_97(0x102, 0x0, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_620)
    Sleep(100)

    def lambda_63D():
        OP_97(0x104, 0x0, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_63D)
    Sleep(100)

    def lambda_65A():
        OP_97(0x103, 0x0, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_65A)
    OP_68(0, 1100, 110500, 3000)
    MoveCamera(33, 17, 0, 3000)
    SetCameraDistance(18000, 3000)
    Sound(104, 0, 60, 0)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    WaitChrThread(0x103, 0)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)

    AnonymousTalk(
        0x9,
        (
            "Hey, thanks for your hard work.\x02\x03",
            "It seems you haven't taken the\x01",
            "State Guard guys with you...?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    PlayBGM("ed7564", 0)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#12P#00001F...While it may be true,\x01",
            "you shouldn't assume we\x01",
            "don't want to arrest you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101FWe can't say that...\x01",
            "You aren't related to what\x01",
            "the "Red Constellation" did.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#5P#03504F............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#12PI won't beat around the bush.\x01",
            "Why did you show up in Crossbell?\x02\x03",
            "#00311FAlso, where did my uncle and the ot...\x01",
            "Where did the "Red Constellation" go?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00201FOf course you know,\x01",
            "since you are their client.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P#03506FHmm, allow myself to answer\x01",
            "your first question, will you?\x02\x03",
            "#03508FI came to Crossbell today...\x01",
            "From the Empire, with the first train.\x02\x03",
            "#03501FNaturally, under Giliath\x01",
            "Osborne's orders.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108FThe "Iron and Blood Chancellor"...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00001F...For what purpose?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P#03504FBefore that, I'll tell\x01",
            "you a welcome news.\x02\x03",
            "#03501F──Around today's afternoon, the Imperial\x01",
            "Army is going to come to invade you.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x101,
        "#12P#00007F!!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105FWha...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#00211F...That is not a funny joke.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F#12PNo...considerin' the situation,\x01",
            "it wouldn't be strange if it were true.\x02\x03",
            "#00301FOf course from Bellguard Gate, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P#03504FYeah, an armored division has already \x01",
            "been gathering at Garrelia Fortress.\x02\x03",
            "#03508FWell, it's just one division at best, but...\x02\x03",
            "#03501FBecause they have the latest heavy tanks, \x01",
            "Crossbell armored vehicles are probably \x01",
            "going to be easily kicked around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00010FCr...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00107FW-We must tell this immediately to\x01",
            "the CGF──no, to the State Guard...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P#03508FWhy?\x01",
            "They already know that.\x02\x03",
            "#03503FWell, a notification was sent in advance\x01",
            "to the autonomous state government.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00011F!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P#03506FAnd yet, ol' man Dieter didn't\x01",
            "revoke the IBC freezing of assets\x01",
            "and even took office as President.\x02\x03",
            "He should know it's impossible to defend \x01",
            "against the Imperial Army's invasion.\x02\x03",
            "#03502F──And that's the reason why\x01",
            "I officially came to Crossbell.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)

    def lambda_FAC():
        TurnDirection(0x104, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_FAC)
    Sleep(30)

    def lambda_FBC():
        TurnDirection(0x102, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_FBC)
    Sleep(30)

    def lambda_FCC():
        TurnDirection(0x103, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_FCC)
    Sleep(30)

    def lambda_FDC():
        TurnDirection(0x101, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_FDC)
    Sleep(30)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x101, 0)

    ChrTalk(
        0x104,
        (
            "#00301F#11PHey...what does that mean?\x02\x03",
            "What do you say about ol' man Arios\x01",
            "bein' appointed Commander in Chief\x01",
            "of the State Guard in this situation?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00006F...I don't know.\x02\x03",
            "Even if it's Mr. Arios, there's\x01",
            "no way he can fight against tanks.\x02\x03",
            "#00008FI can only think they have\x01",
            "some kind of trump card...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00200FWhat about compromising with the Republic\x01",
            "to keep in check the Imperial Army...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00106FNo, if that were the case, the President \x01",
            "wouldn't have been so critic about the \x01",
            "Republic in his speech too...\x02\x03",
            "#00108FHe must intend to seriously\x01",
            "confront the Republic too.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x80)

    NpcTalk(
        0x8,
        "Woman's Voice",
        "──Yes, that's right.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(0, 1100, 102500, 2000)
    SetCameraDistance(17500, 2000)

    def lambda_130B():
        TurnDirection(0x101, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_130B)
    Sleep(50)

    def lambda_131B():
        TurnDirection(0x102, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_131B)
    Sleep(50)

    def lambda_132B():
        TurnDirection(0x103, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_132B)
    Sleep(50)

    def lambda_133B():
        TurnDirection(0x104, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_133B)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    Sleep(1000)
    Sound(103, 0, 100, 0)

    def lambda_1364():
        OP_96(0xFE, 0x0, 0x0, 0x18C7C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1364)

    def lambda_137E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_137E)
    WaitChrThread(0x8, 1)
    Sound(104, 0, 60, 0)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#00005FHuh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00205FYou...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5P#N#00305FMiss Kilika!?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)

    AnonymousTalk(
        0x8,
        (
            "──Long time no see.\x02\x03",
            "You too, Captain Arundel.\x01",
            "I'm sorry for being late.\x02",
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

    def lambda_14A7():
        OP_96(0xFE, 0xFFFFFE70, 0x0, 0x1A5E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_14A7)
    Sleep(1000)
    Fade(500)
    OP_68(760, 1100, 109730, 0)
    MoveCamera(37, 15, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17500, 0)
    SetChrPos(0x101, 800, 30, 108500, 270)
    SetChrPos(0x102, 1800, 30, 108300, 270)
    SetChrPos(0x104, 2300, 30, 107100, 270)
    SetChrPos(0x103, 1000, 30, 107100, 270)

    def lambda_153B():

        label("loc_153B")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_153B")

    QueueWorkItem2(0x101, 2, lambda_153B)

    def lambda_154D():

        label("loc_154D")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_154D")

    QueueWorkItem2(0x102, 2, lambda_154D)

    def lambda_155F():

        label("loc_155F")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_155F")

    QueueWorkItem2(0x103, 2, lambda_155F)

    def lambda_1571():

        label("loc_1571")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_1571")

    QueueWorkItem2(0x104, 2, lambda_1571)

    def lambda_1583():
        OP_98(0xFE, 0x1F4, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1583)
    Sleep(100)

    def lambda_15A0():
        OP_98(0xFE, 0x1F4, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_15A0)
    Sleep(100)

    def lambda_15BD():
        OP_98(0xFE, 0x1F4, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_15BD)
    Sleep(100)

    def lambda_15DA():
        OP_98(0xFE, 0x1F4, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_15DA)
    Sleep(1100)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    WaitChrThread(0x8, 1)
    WaitChrThread(0x102, 1)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)

    ChrTalk(
        0x9,
        (
            "#5P#03504FWell, I've just arrived too,\x01",
            "so don't be worried about it.\x02\x03",
            "#03500FHow are things on your end?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12P#03403FAdvancing as planned in general.\x02\x03",
            "#03401FAt present, an Armored Aviation Division has\x01",
            "been deployed at the Altair City's outskirts.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#11P#00010F!!!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108FT-The Republican Army too...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00310FArmored Aviation Division...\x01",
            "A mixed unit of tanks and airships!?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x5A, 0x1F4)

    ChrTalk(
        0x8,
        (
            "#6P#03403FYes, a combination of mobile new\x01",
            "tank models and gunships.\x02\x03",
            "#03400FThey boast the highest mobility\x01",
            "even among the Calvardian Army.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#00013FNo way...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#00208FIs it a...pincer attack?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6P#03400FYes. It's an undesirable\x01",
            "situation for you.\x02\x03",
            "#03403F──However, if you think about it a little, you\x01",
            "should know what brought upon this situation.\x02\x03",
            "It was Dieter Crois'\x01",
            "uncompromising\x01",
            "drastic attitude.\x02\x03",
            "#03402FI wonder how things will turn out?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)

    ChrTalk(
        0x9,
        (
            "#5P#03504FAlso, regarding the other one...\x02\x03",
            "#03502FAbout your second question,\x01",
            "I'll do a great service to you and answer.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1ACD():
        TurnDirection(0x101, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1ACD)
    Sleep(50)

    def lambda_1ADD():
        TurnDirection(0x104, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1ADD)
    Sleep(50)

    def lambda_1AED():
        TurnDirection(0x102, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1AED)
    Sleep(50)

    def lambda_1AFD():
        TurnDirection(0x103, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1AFD)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)

    ChrTalk(
        0x101,
        "#11P#00008FThe second...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#00301F...The "Red Constellation" whereabouts?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P#03505FYeah, the answer is simple.\x02\x03",
            "#03506F──Even us, the Imperial government,\x01",
            "don't know at all about that.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x102,
        "#00107FT-There's no way...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00211FYou can't tell us that after having \x01",
            "been so frank, don't you think...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00310FHah! Do you mean that after havin' rampaged\x01",
            "in Crossbell your contract was over!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00011FN-No──wait.\x02\x03",
            "#00003FThe "Red Constellation" had a contract \x01",
            "with the Imperial government at the time\x01",
            "of the Trade Conference...\x02\x03",
            "The content of that was to slaughter the terrorists \x01",
            "who were aiming at the Chancellor's life...\x02\x03",
            "#00013FAm I correct in that regard?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#5P#03504FYeah, those guys said the same too, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00008F...But, what if...\x02\x03",
            "#00010FThe contract with the Imperial government\x01",
            "ended at that moment?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_1F3A():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1F3A)
    Sleep(50)

    def lambda_1F4A():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1F4A)
    Sleep(50)

    def lambda_1F5A():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1F5A)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)

    ChrTalk(
        0x102,
        "#00105FWhat────\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#00205FYou mean...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#00301F...No way...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P#03504F...Eheheheh.\x02\x03",
            "#03502FLloyd, as I thought you're kinda\x01",
            "suited for intelligence.\x02\x03",
            "#03509FIf only you had a little worse personality, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#00007FT-Then...!\x02",
    )

    CloseMessageWindow()

    def lambda_207D():
        TurnDirection(0x102, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_207D)
    Sleep(50)

    def lambda_208D():
        TurnDirection(0x104, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_208D)
    Sleep(50)

    def lambda_209D():
        TurnDirection(0x103, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_209D)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x103, 0)

    ChrTalk(
        0x9,
        (
            "#5P#03503F──The answer is yes.\x02\x03",
            "After the Trade Conference, the\x01",
            "Imperial government hasn't had any\x01",
            "relation with "Red Constellation".\x02\x03",
            "#03508FNevertheless, I too thought it\x01",
            "was weird that those guys\x01",
            "remained in Crossbell...\x02\x03",
            "#03501FI can't believe they suddenly\x01",
            "did such a thing...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00106FNo way...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00308FThen, why uncle and the\x01",
            "others acted like that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00201F...Could it be that they signed a\x01",
            "new contract with the "Society"?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6P#03403FNo, that would be strange too.\x02\x03",
            "#03401FAt the time of the Liberl phenomenon,\x01",
            "they made use of a unique fighting\x01",
            "unit called "strengthened jaegers".\x02\x03",
            "If they had attacked Crossbell,\x01",
            "they would've left it to such a unit.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_236F():
        TurnDirection(0x103, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_236F)
    Sleep(50)

    def lambda_237F():
        TurnDirection(0x102, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_237F)
    Sleep(50)

    def lambda_238F():
        TurnDirection(0x101, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_238F)
    Sleep(50)

    def lambda_239F():
        TurnDirection(0x104, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_239F)
    Sleep(50)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x104, 0)

    ChrTalk(
        0x103,
        "#12P#00200F...I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108FDoes it mean they didn't have the need to\x01",
            "employ an outside jaeger corps on purpose...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00008F#30W...In that case...\x01",
            "We can narrow down to other candidates.\x02\x03",
            "#00003FIn a situation where the Imperial government\x01",
            "is indeed thought to be the mastermind...\x02\x03",
            "There's a party who could "earn" something\x01",
            "from having Crossbell attacked...\x02\x03",
            "And that can also have vast funds power\x01",
            "to be able to enter into a long term\x01",
            "contract with the highest rank jaegers...\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xBB8)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        "#11P#00011F──Huh.\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7203", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xCB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0x9,
        "#5P#03504FWell, I guess that sums it up?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6P#03401F...Occasionally, the truth lies right\x01",
            "in the hardest to believe possibility.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105FPlease, w-wait a moment!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#00208FC-Considering the flow of the conversation...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00307FIsn't there only one candidate\x01",
            "that's likely to correspond!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#11PW-Well...\x01",
            "As you expect, it would be hard to clearly say it.\x02\x03",
            "#00006F──Captain Lechter, Miss Kilika.\x02\x03",
            "Thank you for the information exchange,\x01",
            "but you also have your own situations.\x02\x03",
            "#00013FFrom now on, we will──\x02",
        )
    )

    CloseMessageWindow()
    Sound(803, 2, 100, 0)
    Sleep(300)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_283A():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_283A)
    Sleep(50)

    def lambda_284A():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_284A)
    Sleep(50)

    def lambda_285A():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_285A)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    Fade(250)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    Sound(802, 0, 100, 0)
    Sleep(500)
    SetChrSubChip(0x101, 0x1)
    OP_24(0x323)
    Sound(804, 0, 100, 0)
    Sleep(300)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CC(0x0, 0x0, 0x3)
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00013FYes!\x01",
            "Special Support Section, Bannin──\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Woman's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "T-Thank goodness!\x01",
            "I could reach you...\x02\x03",
            "Lloyd, it's Cecil!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00011FSister Cecil?\x02\x03",
            "#00001FYou're so flustered...\x01",
            "Has something happened?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Cecil's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "W-Well...\x02\x03",
            "Mr. Arios came to\x01",
            "the building just now.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00005FMr. Arios did!?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Cecil's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A-And then...\x02\x03",
            "He went away\x01",
            "taking KeA with him...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00007F#4S!?\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Cecil's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "I tried to stop\x01",
            "him too, but KeA...\x02\x03",
            "In any case, can you return?\x01",
            "I want to explain the details!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00010FU-Understood!\x01",
            "Wait there for us!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sound(813, 0, 40, 0)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    OP_CC(0x0, 0x0, 0x3)
    SetChrSubChip(0x101, 0x1)
    Sound(804, 0, 100, 0)

    ChrTalk(
        0x102,
        "#00101FW-What's wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#00301FYou're really pale, you know?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Sound(802, 0, 100, 0)
    OP_0D()
    TurnDirection(0x101, 0x104, 500)

    ChrTalk(
        0x101,
        (
            "#5P#00013FMr. Arios came to the Support Section,\x01",
            "took KeA with him and went away...!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x102,
        "#00105F#4S!?\x02",
    )

    CloseMessageWindow()
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x104,
        "#12P#00307F#4SWhat the hel!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#00201FWhy would he...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#00010FAt any rate, let's return to the Support Section!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 500)

    ChrTalk(
        0x101,
        (
            "#11P#00007FMiss Kilika, Mr. Lechter!\x01",
            "Please excuse us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#6P#03400FYes, be careful.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#5P#03509FWell, do your best.\x02",
    )

    CloseMessageWindow()

    def lambda_2E1C():

        label("loc_2E1C")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_2E1C")

    QueueWorkItem2(0x8, 2, lambda_2E1C)
    OP_68(400, 1100, 103800, 3000)
    MoveCamera(30, 15, 0, 3000)
    SetCameraDistance(19500, 3000)
    BeginChrThread(0x103, 3, 0, 4)
    Sleep(250)
    BeginChrThread(0x104, 3, 0, 4)
    Sleep(250)
    BeginChrThread(0x101, 3, 0, 4)
    Sleep(250)
    BeginChrThread(0x102, 3, 0, 4)
    Sleep(600)
    Sound(103, 0, 100, 0)
    WaitChrThread(0x102, 3)
    Sound(104, 0, 100, 0)
    EndChrThread(0x8, 0x2)
    OP_6F(0x79)
    Sleep(500)
    Fade(500)
    OP_68(0, 1100, 110450, 0)
    MoveCamera(30, 13, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18000, 0)
    SetChrSubChip(0x9, 0x1)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x9,
        (
            "#03506F#5PSo, as we suspected that little miss \x01",
            "was the "key" to everything, eh?\x02\x03",
            "#03508FSay, do you think they'll make it in time?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#03401F#5PLet's see...\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x8)
    Sleep(500)

    ChrTalk(
        0x8,
        "#03403F#5P──Perhaps, but it'll be hard.\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(18500, 2000)
    FadeToDark(1500, 0, -1)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    Sleep(500)
    SetScenarioFlags(0x23, 6)
    NewScene("c0110", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_3_47D end

    def Function_4_2FDD(): pass

    label("Function_4_2FDD")

    OP_92(0xFE, 0x0, 0x18894, 0x1F4)

    def lambda_2FEF():
        OP_95(0xFE, 0, 0, 101000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2FEF)
    WaitChrThread(0xFE, 1)

    def lambda_300D():
        OP_95(0xFE, 0, 0, 98000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_300D)

    def lambda_3027():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3027)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_4_2FDD end

    SaveToFile()

Try(main)
