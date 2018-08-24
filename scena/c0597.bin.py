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
        "Function_3_464",          # 03, 3
        "Function_4_2EED",         # 04, 4
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
            "Imperial Army Intelligence\x01",
            "Division.)\x02\x03",
            "#00013F(We can't take him lightly. If\x01",
            "we're going to enter, let's\x01",
            "make sure we're prepared.)\x02",
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
            "Once you enter, you will not\x01",
            "be able to adjust equipment,\x01",
            "items or quartz for a while.\x02\x03",
            "Also, please note that all\x01",
            "remaining quests will close\x01",
            "as well.\x07\x00\x02",
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
            "[We Have Other Things to Do]\x01",      # 0
            "[Open the Door and Enter]\x01",         # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_398"),
        (0, "loc_447"),
        (SWITCH_DEFAULT, "loc_463"),
    )


    label("loc_398")

    Sound(103, 0, 100, 0)
    OP_71(0x10, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x10)
    StopBGM(0xFA0)
    FadeToDark(1000, 0, -1)

    def lambda_3C1():
        OP_96(0xFE, 0x0, 0x0, 0x105B8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3C1)
    Sleep(300)

    def lambda_3DE():
        OP_96(0xFE, 0x0, 0x0, 0x105B8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3DE)
    Sleep(300)

    def lambda_3FB():
        OP_96(0xFE, 0x0, 0x0, 0x105B8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3FB)
    Sleep(300)

    def lambda_418():
        OP_96(0xFE, 0x0, 0x0, 0x105B8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_418)
    OP_0D()
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x102, 0xFF)
    EndChrThread(0x104, 0xFF)
    EndChrThread(0x103, 0xFF)
    WaitBGM()
    Call(0, 3)
    Jump("loc_463")

    label("loc_447")

    SetChrPos(0x0, 0, 30, 61800, 180)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Jump("loc_463")

    label("loc_463")

    Return()

    # Function_2_13E end

    def Function_3_464(): pass

    label("Function_3_464")

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

    def lambda_5EA():
        OP_97(0x101, 0x0, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_5EA)
    Sleep(100)

    def lambda_607():
        OP_97(0x102, 0x0, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_607)
    Sleep(100)

    def lambda_624():
        OP_97(0x104, 0x0, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_624)
    Sleep(100)

    def lambda_641():
        OP_97(0x103, 0x0, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_641)
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
            "Hey, nice work.\x02\x03",
            "I guess you didn't bring those\x01",
            "State Guard with you?\x02",
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
            "#12P#00001F...While that may be true,\x01",
            "you shouldn't assume we\x01",
            "won't arrest you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101FWe can't say you weren't\x01",
            "involved in the actions\x01",
            "of Red Constellation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#5P#03504F...............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#12PI won't beat around the\x01",
            "bush. Why did you show\x01",
            "up in Crossbell?\x02\x03",
            "#00311FAlso, where did my uncle\x01",
            "and the ot... Where did\x01",
            "Red Constellation go?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00201FBeing their client, you\x01",
            "of course know, don't\x01",
            "you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P#03506FHmm, allow me to answer\x01",
            "your first question, will\x01",
            "you?\x02\x03",
            "#03508FI came to Crossbell\x01",
            "today... From the Empire,\x01",
            "on the first train.\x02\x03",
            "#03501FNaturally, under Giliath\x01",
            "Osborne's orders.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108FThe Blood and Iron\x01",
            "Chancellor...\x02",
        )
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
            "#5P#03504FBefore that, I'll give you\x01",
            "some welcome news.\x02\x03",
            "#03501F─Around this afternoon,\x01",
            "the Imperial Army is going\x01",
            "to come to invade you.\x02",
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
        "#12P#00211F...That's not funny.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F#12PNo... Considerin' the\x01",
            "situation, it wouldn't be\x01",
            "strange if it were true.\x02\x03",
            "#00301FYou're of course comin'\x01",
            "from Bellguard Gate,\x01",
            "yeah?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P#03504FYeah, an armored division is already\x01",
            "gathering at Garrelia Fortress.\x02\x03",
            "#03508FWell, one division at most, but...\x02\x03",
            "#03501FBecause they're equipped with the\x01",
            "latest heavy tanks, they'll easily rout\x01",
            "the likes of Crossbell's armored cars.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00010FUgh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00107FW-We must immediately\x01",
            "inform the CGF─ No, the\x01",
            "State Guard...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P#03508FWhy? They already know\x01",
            "that.\x02\x03",
            "#03503FWell, a notification was\x01",
            "sent in advance to the\x01",
            "state government.\x02",
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
            "revoke IBC's asset freeze and\x01",
            "even took office as President.\x02\x03",
            "He should know it's impossible\x01",
            "to defend against the Imperial\x01",
            "Army's invasion.\x02\x03",
            "#03502F─And that's my official reason\x01",
            "for coming to Crossbell.\x02",
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

    def lambda_F35():
        TurnDirection(0x104, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_F35)
    Sleep(30)

    def lambda_F45():
        TurnDirection(0x102, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_F45)
    Sleep(30)

    def lambda_F55():
        TurnDirection(0x103, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_F55)
    Sleep(30)

    def lambda_F65():
        TurnDirection(0x101, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_F65)
    Sleep(30)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x101, 0)

    ChrTalk(
        0x104,
        (
            "#00301F#11PHey... What does that mean?\x02\x03",
            "What do you make of ol' man Arios\x01",
            "bein' appointed Commander of the\x01",
            "State Guard in this situation?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00006F...I don't know.\x02\x03",
            "Even he is Arios,\x01",
            "there's no way he can\x01",
            "fight against tanks.\x02\x03",
            "#00008FI can only think they\x01",
            "have some kind of trump\x01",
            "card...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00200FWhat about reconciling with\x01",
            "the Republic to keep the\x01",
            "Imperial Army in check?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00106FNo. If that were the case, the President\x01",
            "wouldn't have been so critical of the\x01",
            "Republic in his speech...\x02\x03",
            "#00108FHe must intend to seriously confront the\x01",
            "Republic too.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x80)

    NpcTalk(
        0x8,
        "Woman's Voice",
        "─Yes, that's right.\x02",
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

    def lambda_1277():
        TurnDirection(0x101, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1277)
    Sleep(50)

    def lambda_1287():
        TurnDirection(0x102, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1287)
    Sleep(50)

    def lambda_1297():
        TurnDirection(0x103, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1297)
    Sleep(50)

    def lambda_12A7():
        TurnDirection(0x104, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_12A7)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    Sleep(1000)
    Sound(103, 0, 100, 0)

    def lambda_12D0():
        OP_96(0xFE, 0x0, 0x0, 0x18C7C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_12D0)

    def lambda_12EA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_12EA)
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
        "#5P#N#00305FKilika!?\x02",
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
            "─Long time no see.\x02\x03",
            "You too, Captain Arundel. I'm\x01",
            "sorry for being late.\x02",
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

    def lambda_140C():
        OP_96(0xFE, 0xFFFFFE70, 0x0, 0x1A5E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_140C)
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

    def lambda_14A0():

        label("loc_14A0")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_14A0")

    QueueWorkItem2(0x101, 2, lambda_14A0)

    def lambda_14B2():

        label("loc_14B2")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_14B2")

    QueueWorkItem2(0x102, 2, lambda_14B2)

    def lambda_14C4():

        label("loc_14C4")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_14C4")

    QueueWorkItem2(0x103, 2, lambda_14C4)

    def lambda_14D6():

        label("loc_14D6")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_14D6")

    QueueWorkItem2(0x104, 2, lambda_14D6)

    def lambda_14E8():
        OP_98(0xFE, 0x1F4, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_14E8)
    Sleep(100)

    def lambda_1505():
        OP_98(0xFE, 0x1F4, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1505)
    Sleep(100)

    def lambda_1522():
        OP_98(0xFE, 0x1F4, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1522)
    Sleep(100)

    def lambda_153F():
        OP_98(0xFE, 0x1F4, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_153F)
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
            "#5P#03504FWell, I've just arrived\x01",
            "myself, so don't worry\x01",
            "about it.\x02\x03",
            "#03500FHow are things on your\x01",
            "end?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12P#03403FAdvancing as planned in\x01",
            "general.\x02\x03",
            "#03401FAt present, an armored airborne\x01",
            "division has been deployed on\x01",
            "the outskirts of Altair City.\x02",
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
        (
            "#00108FT-The Republican Army\x01",
            "too...!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00310FArmored airborne\x01",
            "division... A mixed unit\x01",
            "of tanks and airships!?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x5A, 0x1F4)

    ChrTalk(
        0x8,
        (
            "#6P#03403FYes, a combination of\x01",
            "new high-mobility tanks\x01",
            "and gunships.\x02\x03",
            "#03400FThey boast the highest\x01",
            "mobility within the\x01",
            "Calvardian Army.\x02",
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
        (
            "#12P#00208FIs it... a pincer\x01",
            "attack?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6P#03400FYes. It's an undesirable\x01",
            "situation for you.\x02\x03",
            "#03403F─However, if you think about it,\x01",
            "you should know what brought\x01",
            "this situation upon yourselves.\x02\x03",
            "It was Dieter Crois'\x01",
            "uncompromising, unyielding\x01",
            "attitude.\x02\x03",
            "#03402FI wonder how things will turn\x01",
            "out?\x02",
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
            "#5P#03504FOh, and one more thing...\x02\x03",
            "#03502FAbout your second\x01",
            "question, I'll do a great\x01",
            "service to you and answer.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1A2C():
        TurnDirection(0x101, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1A2C)
    Sleep(50)

    def lambda_1A3C():
        TurnDirection(0x104, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1A3C)
    Sleep(50)

    def lambda_1A4C():
        TurnDirection(0x102, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1A4C)
    Sleep(50)

    def lambda_1A5C():
        TurnDirection(0x103, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1A5C)
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
        (
            "#12P#00301F...The whereabouts of\x01",
            "Red Constellation?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P#03505FYeah, the answer is\x01",
            "simple.\x02\x03",
            "#03506F─Even we, the Imperial\x01",
            "government, don't know\x01",
            "anything about that.\x02",
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
        "#00107FN-No way!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00211FAfter you've been so\x01",
            "frank with us, that\x01",
            "can't be true, can it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00310FHah! Do you mean that after\x01",
            "havin' rampaged in Crossbell\x01",
            "your contract was over!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00011FN-No─ wait.\x02\x03",
            "#00003FRed Constellation had a contract\x01",
            "with the Imperial government at the\x01",
            "time of the trade conference...\x02\x03",
            "A contract to slaughter the\x01",
            "terrorists who were after at the\x01",
            "chancellor's life...\x02\x03",
            "#00013FAm I correct in that regard?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P#03504FYeah, those guys said\x01",
            "the same thing, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00008F...But, what if...\x02\x03",
            "#00010FThe contract with the\x01",
            "Imperial government\x01",
            "ended at that moment?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_1E72():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1E72)
    Sleep(50)

    def lambda_1E82():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1E82)
    Sleep(50)

    def lambda_1E92():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1E92)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)

    ChrTalk(
        0x102,
        "#00105FWhat─\x02",
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
            "#5P#03504F...Hehehe.\x02\x03",
            "#03502FI knew it. You might be\x01",
            "cut out for this\x01",
            "intelligence stuff, Lloyd.\x02\x03",
            "#03509FIf only we could do\x01",
            "something about that\x01",
            "personality of yours.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#00007FT-Then...!\x02",
    )

    CloseMessageWindow()

    def lambda_1FC2():
        TurnDirection(0x102, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1FC2)
    Sleep(50)

    def lambda_1FD2():
        TurnDirection(0x104, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1FD2)
    Sleep(50)

    def lambda_1FE2():
        TurnDirection(0x103, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1FE2)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x103, 0)

    ChrTalk(
        0x9,
        (
            "#5P#03503F─The answer is yes.\x02\x03",
            "Following the trade conference,\x01",
            "the Imperial government has had no\x01",
            "connection with Red Constellation.\x02\x03",
            "#03508FNevertheless, I too thought it was\x01",
            "weird that those guys remained in\x01",
            "Crossbell...\x02\x03",
            "#03501FI can't believe they did something\x01",
            "like that all of a sudden.\x02",
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
            "#12P#00308FThen, why did uncle and\x01",
            "the others act like\x01",
            "that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00201F...Could they have\x01",
            "signed a new contract\x01",
            "with Ouroboros?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6P#03403FNo, that would be strange too.\x02\x03",
            "#03401FDuring the Liberl incident, they\x01",
            "used a unique fighting unit\x01",
            "called "strengthened jaegers".\x02\x03",
            "If they were attacking\x01",
            "Crossbell, it would be through\x01",
            "the use of such a force.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_22AE():
        TurnDirection(0x103, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_22AE)
    Sleep(50)

    def lambda_22BE():
        TurnDirection(0x102, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_22BE)
    Sleep(50)

    def lambda_22CE():
        TurnDirection(0x101, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_22CE)
    Sleep(50)

    def lambda_22DE():
        TurnDirection(0x104, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_22DE)
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
            "#00108FThen they would have had no need\x01",
            "to go out of their way to employ\x01",
            "an outside jaeger corps...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00008F#30W...In that case... We can narrow it down to\x01",
            "the other candidates.\x02\x03",
            "#00003FIn a situation where the Imperial\x01",
            "government is indeed thought to be the\x01",
            "mastermind...\x02\x03",
            "There's a party who could "earn" something\x01",
            "from having Crossbell attacked...\x02\x03",
            "That party would need to have vast funds to\x01",
            "be able to enter into a long term contract\x01",
            "with jaegers of the highest rank...\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xBB8)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        "#11P#00011F─Huh.\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7203", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xCB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0x9,
        (
            "#5P#03504FWell, I guess that sums\x01",
            "it up?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6P#03401F...Occasionally, the truth\x01",
            "lies right in the hardest\x01",
            "to believe possibility.\x02",
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
        (
            "#12P#00208FC-Considering the flow\x01",
            "of the conversation...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00307FIsn't there only one\x01",
            "candidate that's seems\x01",
            "to fit!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#11PW-Well... As you can\x01",
            "expect, it would be hard\x01",
            "to clearly say it.\x02\x03",
            "#00006F─Captain Lechter, Miss\x01",
            "Kilika.\x02\x03",
            "Thank you for telling\x01",
            "us, but you also have\x01",
            "your own circumstances.\x02\x03",
            "#00013FFrom now on, we will─\x02",
        )
    )

    CloseMessageWindow()
    Sound(803, 2, 100, 0)
    Sleep(300)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_2774():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_2774)
    Sleep(50)

    def lambda_2784():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_2784)
    Sleep(50)

    def lambda_2794():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_2794)
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
            "#00013FYes! Special Support\x01",
            "Section, Bannin─\x02",
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
            "T-Thank goodness! I got\x01",
            "ahold of you...\x02\x03",
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
            "#00011FCecil?\x02\x03",
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
            "Arios came to the\x01",
            "building just now.\x02",
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
            "#00005FArios did!?\x02",
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
            "He left, taking KeA with\x01",
            "him...\x02",
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
            "I tried to stop him too,\x01",
            "but KeA...\x02\x03",
            "In any case, can you\x01",
            "return? I want to\x01",
            "explain the details!\x02",
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
            "#00010FU-Understood! Wait there\x01",
            "for us!\x02",
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
        (
            "#12P#00301FYou're really pale, you\x01",
            "know?\x02",
        )
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
            "#5P#00013FArios came to the\x01",
            "Support Section, took\x01",
            "KeA with him and left!\x02",
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
        "#12P#00307F#4SWhat the hell!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#00201FWhy would he...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00010FAnyhow, let's return to\x01",
            "the Support Section!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 500)

    ChrTalk(
        0x101,
        (
            "#11P#00007FKilika, Lechter! Please\x01",
            "excuse us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#6P#03400FAlright. Be careful.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#5P#03509FWell, do your best～.\x02",
    )

    CloseMessageWindow()

    def lambda_2D2F():

        label("loc_2D2F")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_2D2F")

    QueueWorkItem2(0x8, 2, lambda_2D2F)
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
            "#03506F#5PSo, as we suspected that\x01",
            "little miss was the\x01",
            ""key" to everything, eh?\x02\x03",
            "#03508FSay, do you think\x01",
            "they'll make it in time?\x02",
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
        (
            "#03403F#5P─Perhaps, but it'll be\x01",
            "hard.\x02",
        )
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

    # Function_3_464 end

    def Function_4_2EED(): pass

    label("Function_4_2EED")

    OP_92(0xFE, 0x0, 0x18894, 0x1F4)

    def lambda_2EFF():
        OP_95(0xFE, 0, 0, 101000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2EFF)
    WaitChrThread(0xFE, 1)

    def lambda_2F1D():
        OP_95(0xFE, 0, 0, 98000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2F1D)

    def lambda_2F37():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2F37)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_4_2EED end

    SaveToFile()

Try(main)
