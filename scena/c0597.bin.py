from ScenarioHelper import *

def main():
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
        "Kirika",                 # 1
        "Rector",               # 2
        "dummy",                 # 3
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
        "Function_3_43A",          # 03, 3
        "Function_4_2AF1",         # 04, 4
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
            "#00003F#11P(Imperial Army Information Department affiliation,\x01",
            "Recta Arenddor? )\x02\x03",
            "#00013F(It is not an opponent you can care about … …\x01",
            "Let's set a mind if you enter. )\x02",
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
            "Once in the room\x01",
            "For a while to equip equipment, items and the auction\x01",
            "You will not be able to arrange.\x02\x03",
            "Also, the remaining quests\x01",
            "Please be careful as it all ends.\x07\x00\x02",
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
            "【There are still other things to do】\x01",            # 0
            "[Open the door and enter the room]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_36E"),
        (0, "loc_41D"),
        (SWITCH_DEFAULT, "loc_439"),
    )


    label("loc_36E")

    Sound(103, 0, 100, 0)
    OP_71(0x10, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x10)
    StopBGM(0xFA0)
    FadeToDark(1000, 0, -1)

    def lambda_397():
        OP_96(0xFE, 0x0, 0x0, 0x105B8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_397)
    Sleep(300)

    def lambda_3B4():
        OP_96(0xFE, 0x0, 0x0, 0x105B8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3B4)
    Sleep(300)

    def lambda_3D1():
        OP_96(0xFE, 0x0, 0x0, 0x105B8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3D1)
    Sleep(300)

    def lambda_3EE():
        OP_96(0xFE, 0x0, 0x0, 0x105B8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3EE)
    OP_0D()
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x102, 0xFF)
    EndChrThread(0x104, 0xFF)
    EndChrThread(0x103, 0xFF)
    WaitBGM()
    Call(0, 3)
    Jump("loc_439")

    label("loc_41D")

    SetChrPos(0x0, 0, 30, 61800, 180)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Jump("loc_439")

    label("loc_439")

    Return()

    # Function_2_13E end

    def Function_3_43A(): pass

    label("Function_3_43A")

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

    def lambda_5C0():
        OP_97(0x101, 0x0, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_5C0)
    Sleep(100)

    def lambda_5DD():
        OP_97(0x102, 0x0, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_5DD)
    Sleep(100)

    def lambda_5FA():
        OP_97(0x104, 0x0, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_5FA)
    Sleep(100)

    def lambda_617():
        OP_97(0x103, 0x0, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_617)
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
            "Yo. Nice to see you\x02\x03",
            "Apparently the people of the Defense Army\x01",
            "You do not seem to get along?\x02",
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
            "#12P#00001FThat is why\x01",
            "I'm going to catch you\x01",
            "You better not think that it is not?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101FThe task of \"red constellation\" ……\x01",
            "It is not related to you\x01",
            "I will not say that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#5P#03504F…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#12PI will ask you straight away.\x01",
            "Why did it appear in the crossbell?\x02\x03",
            "#00311FBesides that, my uncle … …\x01",
            "Where did \"red constellation\" go?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00201FIf it is a client\x01",
            "Of course you know, are not you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P#03506FSo, first of all,\x01",
            "Shall I answer you?\x02\x03",
            "#03508FToday I came … …\x01",
            "It is the first departure from Teito.\x02\x03",
            "#03501FOf course Gillius's Osan\x01",
            "It is based on instructions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108FThe Ironblood Chancellor…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00001FWhat is your goal?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P#03504FBefore that, to you\x01",
            "Let me tell you all the information that I hear.\x02\x03",
            "#03501F── About this afternoon\x01",
            "Imperial troops will invade you.\x02",
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
        "#00105FWhat!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#00211FThat's a bad joke…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F#12PNo … In this situation,\x01",
            "It is strange even if it is true.\x02\x03",
            "#00301FFrom Bellguard Gate of course\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P#03504FOh, already at the Galleria Fortress\x01",
            "Armored divisions are gathered.\x02\x03",
            "#03508FWell, at least the First Division\x02\x03",
            "#03501FBecause the latest heavy tanks are complete\x01",
            "About the crossbell armored car\x01",
            "I'm going to kick in as much as I can.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00010FUgh\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00107FWell, immediately to the guard ----\x01",
            "No … I have to tell the Defense Forces … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P#03508FDisagreeable?\x01",
            "It was transmitted over time.\x02\x03",
            "#03503FOnce, advance notice\x01",
            "I am going to the autonomous state government.\x02",
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
            "#5P#03506FNevertheless Dieter Osan\x01",
            "I do not withdraw IBC 's asset freeze,\x01",
            "I was appointed to the president.\x02\x03",
            "It is to prevent the invading Imperial Army\x01",
            "You ought to know that it is impossible.\x02\x03",
            "#03502F── That is my fate again.\x01",
            "That is why I entered the crossbell.\x02",
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

    def lambda_E1F():
        TurnDirection(0x104, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_E1F)
    Sleep(30)

    def lambda_E2F():
        TurnDirection(0x102, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_E2F)
    Sleep(30)

    def lambda_E3F():
        TurnDirection(0x103, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_E3F)
    Sleep(30)

    def lambda_E4F():
        TurnDirection(0x101, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_E4F)
    Sleep(30)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x101, 0)

    ChrTalk(
        0x104,
        (
            "#00301F#11POi, what is this\x02\x03",
            "In that situation, Arios' Osan\x01",
            "What will happen if you appoint a defense army director?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00006FI don't know…\x02\x03",
            "No matter how much Arios is\x01",
            "There is no way I can fight tank opponents.\x02\x03",
            "#00008FWhatever you think, something trump card\x01",
            "Although it is a judgment that I can only think there is … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00200FSomewhat reconciled with the Republic\x01",
            "Check on the Imperial Army … …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00106FNo, if so\x01",
            "To the Republic thing in the presidential speech\x01",
            "I can not blame it like that … …\x02\x03",
            "#00108FTo the end Calvado\x01",
            "I'm going to confront you seriously.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x80)

    NpcTalk(
        0x8,
        "Female voice",
        "Yes, that must be\x02",
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

    def lambda_110E():
        TurnDirection(0x101, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_110E)
    Sleep(50)

    def lambda_111E():
        TurnDirection(0x102, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_111E)
    Sleep(50)

    def lambda_112E():
        TurnDirection(0x103, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_112E)
    Sleep(50)

    def lambda_113E():
        TurnDirection(0x104, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_113E)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    Sleep(1000)
    Sound(103, 0, 100, 0)

    def lambda_1167():
        OP_96(0xFE, 0x0, 0x0, 0x18C7C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1167)

    def lambda_1181():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1181)
    WaitChrThread(0x8, 1)
    Sound(104, 0, 60, 0)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#00005FHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00205FYou are…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5P#N#00305FKilika…!?\x02",
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
            "Long time no see\x02\x03",
            "Captain Alaindor also.\x01",
            "I was late for it.\x02",
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

    def lambda_12B4():
        OP_96(0xFE, 0xFFFFFE70, 0x0, 0x1A5E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_12B4)
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

    def lambda_1348():

        label("loc_1348")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_1348")

    QueueWorkItem2(0x101, 2, lambda_1348)

    def lambda_135A():

        label("loc_135A")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_135A")

    QueueWorkItem2(0x102, 2, lambda_135A)

    def lambda_136C():

        label("loc_136C")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_136C")

    QueueWorkItem2(0x103, 2, lambda_136C)

    def lambda_137E():

        label("loc_137E")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_137E")

    QueueWorkItem2(0x104, 2, lambda_137E)

    def lambda_1390():
        OP_98(0xFE, 0x1F4, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1390)
    Sleep(100)

    def lambda_13AD():
        OP_98(0xFE, 0x1F4, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_13AD)
    Sleep(100)

    def lambda_13CA():
        OP_98(0xFE, 0x1F4, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_13CA)
    Sleep(100)

    def lambda_13E7():
        OP_98(0xFE, 0x1F4, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_13E7)
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
            "#5P#03504FWell, I just came here\x01",
            "Do not mind.\x02\x03",
            "#03500FWhat's your status?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12P#03403FGenerally it's all moving as we expected.\x02\x03",
            "#03401FCurrently in the outskirts of Altair City\x01",
            "Airborne armored division is developing.\x02",
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
        "#00108FT-the Republic too..\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00310FWhat is the Airborne Armored Division ……\x01",
            "It's a mixed unit of tanks and flying boats! Is it?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x5A, 0x1F4)

    ChrTalk(
        0x8,
        (
            "#6P#03403FYes, with a new tank with mobility\x01",
            "Military boat#6RGunship#It is a combination.\x02\x03",
            "#03400FAmong Calvert's troops\x01",
            "I boast of the best mobility.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#00013FNo way…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#00208FSo it's a pincer attack on both sides?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6P#03400FYeah, for you\x01",
            "It may be unwilling.\x02\x03",
            "#03403F─ ─ But, this situation is\x01",
            "You should understand it if you think a little.\x02\x03",
            "in spite of\x01",
            "Dieter Croise\x01",
            "I got into a hard-line posture without any compromise.\x02\x03",
            "#03402FWhat in the world is that\x02",
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
            "#5P#03504FAnd one more thing\x02\x03",
            "#03502FAbout the second question\x01",
            "Let's answer with a big service.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_185A():
        TurnDirection(0x101, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_185A)
    Sleep(50)

    def lambda_186A():
        TurnDirection(0x104, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_186A)
    Sleep(50)

    def lambda_187A():
        TurnDirection(0x102, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_187A)
    Sleep(50)

    def lambda_188A():
        TurnDirection(0x103, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_188A)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)

    ChrTalk(
        0x101,
        "#11P#00008FSecond…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#00301FAbout where Red Constellation went\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P#03505FYes. The answer is simple\x02\x03",
            "#03506F─ ─ Empire Government#8ROreuta#Because\x01",
            "I do not know at all, this is it.\x02",
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
        "#00107FN-no way!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00211FPut it all over so far\x01",
            "If it is not … ….?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00310FHappy, after going crazy with a crossbell,\x01",
            "I guess the contract has ended! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00011FN-no, wait a minute\x02\x03",
            "#00003F\"Red constellation\", at the time of the Trade Council,\x01",
            "I had a contract with the Imperial Government … …\x02\x03",
            "Contents of the contract aim at the life of the prime minister\x01",
            "The annihilation of terrorists … …\x02\x03",
            "#00013FThat's true, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#5P#03504FYes. They said that themselves right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00008FBut then could it be…\x02\x03",
            "#00010FContract with the Imperial Government\x01",
            "At that moment#8R噵 噵 噵 噵#Was it expired?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_1C24():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1C24)
    Sleep(50)

    def lambda_1C34():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1C34)
    Sleep(50)

    def lambda_1C44():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1C44)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)

    ChrTalk(
        0x102,
        "#00105FHuh-\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#00205FThat is…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#00301FNo way..\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P#03504FEheheh\x02\x03",
            "#03502FLloyd, after all,\x01",
            "Perhaps it is suitable for intelligence.\x02\x03",
            "#03509FIf only your personality wasn't so stiff.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#00007FS-so then!\x02",
    )

    CloseMessageWindow()

    def lambda_1D61():
        TurnDirection(0x102, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1D61)
    Sleep(50)

    def lambda_1D71():
        TurnDirection(0x104, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1D71)
    Sleep(50)

    def lambda_1D81():
        TurnDirection(0x103, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1D81)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x103, 0)

    ChrTalk(
        0x9,
        (
            "#5P#03503FThe answer is Yes.\x02\x03",
            "Since the trade meeting, the Imperial Government\x01",
            "It is not related to \"red constellation\".\x02\x03",
            "#03508FIn spite of the,\x01",
            "They remained in Crossbell\x01",
            "I thought that was also strange here, but ….\x02\x03",
            "#03501FNo way No way\x01",
            "I do not care whiskey suddenly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00106FNo way…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00308FWell then why\x01",
            "Your uncle, you imitate that … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00201F…… No way, \"Society\"\x01",
            "Did you sign a new contract?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6P#03403FNo, that's too strange\x02\x03",
            "#03401FOnce in Ribeire's strange\x01",
            "They are called \"strengthened hunters\"\x01",
            "He operated his own combat unit.\x02\x03",
            "If you attack the Crossbell\x01",
            "I guess that made them into troops.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1FDA():
        TurnDirection(0x103, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1FDA)
    Sleep(50)

    def lambda_1FEA():
        TurnDirection(0x102, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1FEA)
    Sleep(50)

    def lambda_1FFA():
        TurnDirection(0x101, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1FFA)
    Sleep(50)

    def lambda_200A():
        TurnDirection(0x104, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_200A)
    Sleep(50)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x104, 0)

    ChrTalk(
        0x103,
        "#12P#00200FI see…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108FTake the trouble to bring out external hunting soldiers\x01",
            "Is not it necessary to hire?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00008F#30W… … Then that … …\x01",
            "Other candidates are narrowed down.\x02\x03",
            "#00003FEspecially the Imperial government\x01",
            "In a situation that seems to be a masterpiece … …\x02\x03",
            "Let me attack Crossbell City\x01",
            "Forces that did some \"gaining\" ……\x02\x03",
            "And with the highest ranked hunting soldiers\x01",
            "It is enough to make a long-term contract\x01",
            "Forces that have huge financial resources ……\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xBB8)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        "#11P#00011FHuh? <Who would it be?>\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7203", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xCB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0x9,
        "#5P#03504FWell, that would be it\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6P#03401F…… It is a possibility that is hard to believe\x01",
            "Often the truth is hiding.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105FW-wait a minute!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#00208FIf you continue thinking along those lines…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00307FWhat is likely to be applicable\x01",
            "I guess it's only one! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#11PNo……\x01",
            "As expected, it is bad.\x02\x03",
            "#00006FSecretary Lechter, Kilika…\x02\x03",
            "Thank you for providing information\x01",
            "Your position is also the position.\x02\x03",
            "#00013FFrom here on we will-\x02",
        )
    )

    CloseMessageWindow()
    Sound(803, 2, 100, 0)
    Sleep(300)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_23A7():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_23A7)
    Sleep(50)

    def lambda_23B7():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_23B7)
    Sleep(50)

    def lambda_23C7():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_23C7)
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
            "Mission support section, at Bannings ──\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Female voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "OK, good day!\x01",
            "It is connected properly ……\x02\x03",
            "Lloyd, this is Cecil!\x02",
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
            "#00001FIn such a hurry ……\x01",
            "Did something happen?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Cecil's voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Th-that is\x02\x03",
            "Mr. Arios earlier\x01",
            "I came to this building.\x02",
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
    SetChrName("Cecil's voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A-and then\x02\x03",
            "Take Kea-chan\x01",
            "I just left as it is ……\x02",
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
    SetChrName("Cecil's voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "I also tried to stop it\x01",
            "Ka'a-chan …\x02\x03",
            "Can you come back anyway?\x01",
            "I will explain the detailed situation!\x02",
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
            "#00010FWow, I understand!\x01",
            "Please wait as it is!\x02",
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
        "#00101FWhat happened?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#00301FYou, what the hell…\x02",
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
            "#5P#00013FArios came to the support department\x01",
            "I took Ka'aa …!\x02",
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
        "#12P#00307F#4SWHAT!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#00201FWhy!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#00010FAnyway we're going back to the SSS\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 500)

    ChrTalk(
        0x101,
        (
            "#11P#00007FMr. Kirika, Lecter!\x01",
            "We will rude with this!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#6P#03400FYes, take care\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#5P#03509FWell, do your best!\x02",
    )

    CloseMessageWindow()

    def lambda_2964():

        label("loc_2964")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_2964")

    QueueWorkItem2(0x8, 2, lambda_2964)
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
            "#03506F#5PAfter all that little girl\x01",
            "Was it all \"key\"?\x02\x03",
            "#03508FYou think they'll make it in time?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#03401F#5PHmm…\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x8)
    Sleep(500)

    ChrTalk(
        0x8,
        "#03403F#5PIt think it will be hard\x02",
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

    # Function_3_43A end

    def Function_4_2AF1(): pass

    label("Function_4_2AF1")

    OP_92(0xFE, 0x0, 0x18894, 0x1F4)

    def lambda_2B03():
        OP_95(0xFE, 0, 0, 101000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2B03)
    WaitChrThread(0xFE, 1)

    def lambda_2B21():
        OP_95(0xFE, 0, 0, 98000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2B21)

    def lambda_2B3B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2B3B)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_4_2AF1 end

    SaveToFile()

Try(main)
