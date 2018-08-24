from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t1390.bin",                # FileName
        "t1390",                    # MapName
        "t1390",                    # Location
        0x0000,                     # MapIndex
        "ed7565",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    )

    BuildStringList((
        "t1390",                  # 0
        "Staffer Hanks",          # 1
        "Middle-Aged Man",        # 2
        "Miichie's Head",         # 3
    ))

    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(256, 0)                                        # 0

    ScpFunction((
        "Function_0_100",          # 00, 0
        "Function_1_127",          # 01, 1
        "Function_2_13A",          # 02, 2
        "Function_3_14B1",         # 03, 3
        "Function_4_14FC",         # 04, 4
        "Function_5_1547",         # 05, 5
    ))


    def Function_0_100(): pass

    label("Function_0_100")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_114")
    ClearScenarioFlags(0x22, 0)
    Event(0, 2)
    Jump("loc_126")

    label("loc_114")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_126")
    ClearScenarioFlags(0x22, 1)
    SetScenarioFlags(0x0, 0)
    Event(0, 5)

    label("loc_126")

    Return()

    # Function_0_100 end

    def Function_1_127(): pass

    label("Function_1_127")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_139")
    VolumeBGM(0x50, 0x32)
    ClearScenarioFlags(0x0, 0)

    label("loc_139")

    Return()

    # Function_1_127 end

    def Function_2_13A(): pass

    label("Function_2_13A")

    EventBegin(0x0)
    VolumeBGM(0x50, 0x3E8)
    FadeToDark(0, 0, -1)
    OP_68(-3080, 2600, -370, 0)
    MoveCamera(315, 20, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19020, 0)
    LoadChrToIndex("chr/ch10200.itc", 0x1E)
    LoadChrToIndex("chr/ch45400.itc", 0x1F)
    LoadChrToIndex("chr/ch28100.itc", 0x20)
    SoundLoad(2679)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x103, 0x1F)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x8, 0x20)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x101, -4170, 0, 610, 90)
    SetChrPos(0x102, -2300, 0, 570, 270)
    SetChrPos(0x104, -2550, 0, 1990, 225)
    SetChrPos(0x109, -3870, 0, 2290, 180)
    SetChrPos(0x105, -3280, 0, -1000, 315)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x103, 210, 0, -4420, 0)
    SetChrPos(0x8, 210, 0, -4420, 0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(-3080, 1600, -370, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05200F...H-How is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FHaha, it's cute.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10109FYes, you look amazing!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05206F(It covers my whole\x01",
            "body, so whether it\x01",
            "looks good on me is...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FHehe, how do you feel?\x01",
            "It looks hot though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05201FYeah... I guess this\x01",
            "thing does trap quite a\x01",
            "bit of heat inside.\x02\x03",
            "#05203FAlso, it's the right\x01",
            "height but it's baggy and\x01",
            "might be hard to move in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FDon't sweat the small\x01",
            "stuff, eh?\x02\x03",
            "#00306FTch, it must be nice.\x01",
            "You'll be able to casually\x01",
            "touch all those fangirls...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05211FD-Don't say it in such a\x01",
            "weird way! Honestly...\x02\x03",
            "#05205F...Oh? By the way,\x01",
            "where's Tio?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FNow that you mention it, she\x01",
            "spoke with the staff member\x01",
            "earlier and went off somewhere...\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(30, 120, -1, -1)
    SetChrName("Tio's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "─I'm here.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(-910, 1600, -2190, 3000)
    MoveCamera(289, 20, 0, 3000)

    def lambda_5F3():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5F3)
    Sleep(50)

    def lambda_603():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_603)
    Sleep(50)

    def lambda_613():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_613)
    Sleep(50)

    def lambda_623():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_623)
    Sleep(50)

    def lambda_633():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_633)
    OP_6F(0x79)
    Sound(121, 0, 100, 0)
    Sleep(500)
    BeginChrThread(0x103, 3, 0, 3)
    Sleep(500)
    BeginChrThread(0x8, 3, 0, 4)

    def lambda_65A():

        label("loc_65A")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_65A")

    QueueWorkItem2(0x101, 1, lambda_65A)

    def lambda_66C():

        label("loc_66C")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_66C")

    QueueWorkItem2(0x102, 1, lambda_66C)

    def lambda_67E():

        label("loc_67E")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_67E")

    QueueWorkItem2(0x104, 1, lambda_67E)

    def lambda_690():

        label("loc_690")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_690")

    QueueWorkItem2(0x109, 1, lambda_690)

    def lambda_6A2():

        label("loc_6A2")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_6A2")

    QueueWorkItem2(0x105, 1, lambda_6A2)
    OP_68(-1670, 1600, -1050, 3000)
    MoveCamera(305, 23, 0, 3000)
    OP_6E(500, 3000)
    SetCameraDistance(17980, 3000)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x8, 3)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x109, 0x1)
    EndChrThread(0x105, 0x1)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05205FHuh... I-Is that you,\x01",
            "Tio?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#2679VMishishi, I'm Mishette,\x01",
            "you know?☆\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xA77)
    OP_C9(0x1, 0x80000000)

    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "Oh big brother, did you\x01",
            "forget my face?\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00305F*sigh*, well...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_84E")
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K◆During the\x01",
            "Intermission,\x01",
            "I...(debug)\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[Met Mishette]\x01",         # 0
            "[Didn't Meet Her]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_84E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_9C5")

    ChrTalk(
        0x102,
        (
            "#00102FCute... So cute, Tio!\x02\x03",
            "#00105FAlso, if I remember\x01",
            "correctly, that\x01",
            "character is...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05522FYes, she is "Mishette",\x01",
            "Mishy's little sister.\x02\x03",
            "#05524FA courageous girl who amicably\x01",
            "watches over her brother who\x01",
            "makes nothing but blunders.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05212F(A-Amicably...)\x02\x03",
            "#05203FCome to think of it, we\x01",
            "met her when we came to\x01",
            "M.W.L. before...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B1B")

    label("loc_9C5")


    ChrTalk(
        0x102,
        (
            "#00102FCute... So cute, Tio!\x02\x03",
            "#00105FBut... Who is this\x01",
            "character?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05522FYes, she is "Mishette",\x01",
            "Mishy's little sister.\x02\x03",
            "#05524FA courageous girl who amicably\x01",
            "watches over her brother who\x01",
            "makes nothing but blunders.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05212F(A-Amicably...)\x02\x03",
            "#05203FCome to think of it, I\x01",
            "think I heard Mishy did\x01",
            "have a little sister...\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B1B")


    ChrTalk(
        0x8,
        (
            "Well you see, she just\x01",
            "suddenly asked me to\x01",
            "lend her that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Mishette has some free\x01",
            "time in her schedule, so\x01",
            "I OK'd it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105FI-I see...\x02\x03",
            "But suddenly appearing\x01",
            "in that means...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05524FI will secretly support\x01",
            "to Lloyd's Mishy act.\x02\x03",
            "#05521FIf he makes some\x01",
            "blunder, I will\x01",
            "mercilessly kick him.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x105,
        (
            "#10309FAhaha, a little sister's\x01",
            "lashings of love, eh? Don't\x01",
            "you feel loved, big brother?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05206FI'd wish she cut me some\x01",
            "slack, though...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05201F......Wait, I don't get\x01",
            "any acting direction?\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    def lambda_D58():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D58)
    Sleep(50)

    def lambda_D68():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_D68)
    Sleep(50)

    def lambda_D78():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_D78)
    Sleep(50)

    def lambda_D88():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_D88)
    Sleep(50)

    def lambda_D98():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_D98)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "I'm sorry, but we simply\x01",
            "don't have the time for\x01",
            "anything like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It's almost time for\x01",
            "Mishy's tour, you see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Come on, if you just try to speak\x01",
            "and act like him, everything will\x01",
            "work itself out, probably!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05206F(I-I'm not sure about\x01",
            "this...)\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Then, after the morning\x01",
            "tour, you have the Mishy\x01",
            "dance show at the plaza.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I prepared an acting\x01",
            "manual just for that.\x01",
            "...Memorize it quickly.\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "You were showed the\x01",
            "dance manual.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(18, 0, 100, 0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Dance passionately yet fancily.\x01",
            "※Don't forget to shout "Enjoy\x01",
            "Mishy☆", his closing catchphrase.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_63(0x101, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x104,
        "#00306FW-Well, this is...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10112FIt's unbelievably\x01",
            "vague...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "To tell you the truth, we leave\x01",
            "everything up to the actor for\x01",
            "the character's personality.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Since the theme park's\x01",
            "founding, there hasn't been\x01",
            "a single decent manual made.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, deal with any\x01",
            "mistakes as they happen.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05524FSince I'm supervising, I\x01",
            "won't tolerate mistakes.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05206FW-What am I gonna do...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "Oh...it's time. Take\x01",
            "care of the\x01",
            "preparations.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1297():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1297)
    Sleep(50)

    def lambda_12A7():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_12A7)
    Sleep(50)

    def lambda_12B7():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_12B7)
    Sleep(50)

    def lambda_12C7():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_12C7)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#00100FThen, we'll pass the\x01",
            "time walking around the\x01",
            "park.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10300FHehe, best of luck.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05520FThen, let's go, Lloyd.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05205FR-Right...\x02\x03",
            "#05203F(In any case... I guess all\x01",
            "I can do is bring out my\x01",
            "own image of Mishy.)\x02\x03",
            "#05200F(And the dance slogan,\x01",
            ""Enjoy Mishy☆", huh. I\x01",
            "should try to remember it.)\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Alright then, do your\x01",
            "best, for all the\x01",
            "children's dreams!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'm counting on you!\x01",
            "Mishy, Mishette!!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    Sleep(10)
    VolumeBGM(0x64, 0x0)
    OP_29(0x86, 0x1, 0x0)
    SetScenarioFlags(0x22, 1)
    NewScene("t1030", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_2_13A end

    def Function_3_14B1(): pass

    label("Function_3_14B1")


    def lambda_14B6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_14B6)

    def lambda_14C7():
        OP_95(0xFE, 370, 0, -2050, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_14C7)
    WaitChrThread(0x103, 1)
    OP_95(0x103, -1210, 0, -1620, 2000, 0x0)
    TurnDirection(0x103, 0x101, 500)
    Return()

    # Function_3_14B1 end

    def Function_4_14FC(): pass

    label("Function_4_14FC")


    def lambda_1501():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1501)

    def lambda_1512():
        OP_95(0xFE, 370, 0, -2050, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1512)
    WaitChrThread(0x8, 1)
    OP_95(0x8, -10, 0, -300, 2000, 0x0)
    OP_93(0x8, 0x10E, 0x1F4)
    Return()

    # Function_4_14FC end

    def Function_5_1547(): pass

    label("Function_5_1547")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch10200.itc", 0x1E)
    LoadChrToIndex("chr/ch45400.itc", 0x1F)
    LoadChrToIndex("apl/ch51403.itc", 0x20)
    LoadChrToIndex("chr/ch47300.itc", 0x22)
    SoundLoad(802)
    SetChrChipByIndex(0x103, 0x1F)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0xA, 0x20)
    SetChrSubChip(0xA, 0x1)
    SetChrFlags(0xA, 0x8000)
    SetChrChipByIndex(0x9, 0x22)
    SetChrFlags(0x9, 0x8000)
    OP_68(1860, 2600, 260, 0)
    MoveCamera(320, 22, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(15130, 0)
    SetChrPos(0x101, 380, 0, 1140, 90)
    SetChrPos(0x103, 2500, 0, 1020, 270)
    SetChrPos(0x9, 210, 0, -4420, 0)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x104, 0x80)
    SetChrFlags(0x109, 0x80)
    SetChrFlags(0x105, 0x80)
    OP_68(1860, 1600, 260, 3000)
    FadeToBright(1000, 0)
    OP_6F(0x1)
    OP_0D()

    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05520F...Oopsie-daisy.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrFlags(0x103, 0x20)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 1370, 200, 310, 180)
    Sound(802, 0, 100, 0)
    OP_0D()

    ChrTalk(
        0x103,
        (
            "#05526F*sigh*... I'm drenched\x01",
            "in sweat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHaha... It seems you\x01",
            "worked really hard.\x02\x03",
            "#00000FNice work, Tio.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x176, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x176, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x176, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1850")

    ChrTalk(
        0x103,
        (
            "#05522FNo, your interpretation\x01",
            "of Mishy left no room\x01",
            "for criticism.\x02\x03",
            "#05524F...Also, that final\x01",
            "dance together was a lot\x01",
            "of fun...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FUmm, haha... You're\x01",
            "making me blush.\x02\x03",
            "#00003F...Well then. I think\x01",
            "it's about time we meet\x01",
            "up with everyone.\x02\x03",
            "#00005FIs the real Mishy actor\x01",
            "not here yet?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1974")

    label("loc_1850")


    ChrTalk(
        0x103,
        (
            "#05522FYou too. It was rough\x01",
            "around the edges, but I\x01",
            "think it was well done.\x02\x03",
            "#05524FSupervising you was\x01",
            "worth it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FHaha... Thanks, you\x01",
            "really helped me out.\x02\x03",
            "#00003F...Well then. I think\x01",
            "it's about time we meet\x01",
            "up with everyone.\x02\x03",
            "#00005FIs the real Mishy actor\x01",
            "not here yet?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1974")


    ChrTalk(
        0x103,
        (
            "#05520FNow that you mention it,\x01",
            "he seems to be lat──\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(30, 120, -1, -1)
    SetChrName("Middle-Aged Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#4S──Gwah hah hah hah ha!\x01",
            "Sorry to have kept ya\x01",
            "waitin'!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(1590, 1600, -1210, 3000)

    def lambda_1A5A():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1A5A)
    Sleep(50)

    def lambda_1A6A():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1A6A)
    OP_6F(0x1)
    Sound(121, 0, 100, 0)
    ClearChrFlags(0x9, 0x80)

    def lambda_1A84():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1A84)

    def lambda_1A95():
        OP_95(0xFE, 370, 0, -2050, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1A95)
    WaitChrThread(0x9, 1)
    Sleep(300)

    ChrTalk(
        0x101,
        "#00011FHuh.........?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#05521F............!?\x02",
    )

    CloseMessageWindow()
    OP_93(0x9, 0x13B, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x9,
        "*burp*...!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x9,
        (
            "Gwah hah ha, my bad, my\x01",
            "bad!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Seems ya can't take da\x01",
            "medicines I got after\x01",
            "eatin', ya know!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I skipped breakfast too,\x01",
            "so I unintentionally ate\x01",
            "tons!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...So, is my costume in\x01",
            "that locker?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x103)

    ChrTalk(
        0x9,
        (
            "...Huh? What's wrong? Ya\x01",
            "look really surprised?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "By the way, it seems I\x01",
            "saw yer faces\x01",
            "somewhere...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Well, anyhow, I owe ya one.\x01",
            "Mishy is indispensable to\x01",
            "Wonderland, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Ya filled in fo' me\x01",
            "well. Gwah hah ha...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Oops, got no time to chit\x01",
            "chat. Gotta change at once and\x01",
            "prepare for the afternoon.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-720, 1600, -10, 3000)

    def lambda_1D5E():

        label("loc_1D5E")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_1D5E")

    QueueWorkItem2(0x101, 1, lambda_1D5E)

    def lambda_1D70():

        label("loc_1D70")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_1D70")

    QueueWorkItem2(0x103, 1, lambda_1D70)
    OP_95(0x9, -2860, 0, -1350, 2000, 0x0)
    OP_95(0x9, -4080, 0, 260, 2000, 0x0)
    OP_93(0x9, 0x10E, 0x1F4)
    Sleep(1000)
    OP_6F(0x1)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x103)
    VolumeBGM(0x46, 0x3E8)
    FadeToDark(500, 0, -1)
    OP_0D()
    SetChrChipByIndex(0x9, 0x1E)
    SetChrSubChip(0x9, 0x0)
    Sleep(1000)
    Sound(802, 0, 100, 0)
    Sound(898, 0, 100, 0)
    Sleep(1000)
    Sound(1000, 0, 100, 0)
    Sleep(1000)
    FadeToBright(500, 0)
    OP_0D()
    VolumeBGM(0x50, 0x3E8)
    OP_93(0x9, 0x5A, 0x1F4)

    NpcTalk(
        0x9,
        "Mishy",
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "─Transformation,\x01",
            "complete☆\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x9,
        "Mishy",
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "Thank you mister and\x01",
            "missy! You saved me!\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x9,
        "Mishy",
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "Leave the rest to me!\x01",
            "Mishishi, see you.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_68(1590, 1600, -1210, 3000)
    OP_95(0x9, -2860, 0, -1350, 2000, 0x0)
    OP_95(0x9, 370, 0, -2050, 2000, 0x0)

    def lambda_1F04():
        OP_95(0xFE, 210, 0, -4420, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1F04)
    Sound(121, 0, 100, 0)
    Sleep(500)

    def lambda_1F27():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1F27)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x103, 0x1)
    OP_93(0x103, 0xB4, 0x1F4)
    OP_6F(0x1)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    Sound(890, 0, 100, 0)
    Sleep(1000)
    OP_64(0x101)
    OP_64(0x103)

    ChrTalk(
        0x101,
        (
            "#00005F(W-What a pro... Even\x01",
            "the timbre of his voice\x01",
            "is totally different...)\x02\x03",
            "#00006F(He's so perfect as\x01",
            "Mishy, how...ever...)\x02",
        )
    )

    CloseMessageWindow()
    Sleep(1000)
    OP_82(0xC8, 0x0, 0xBB8, 0x320)

    ChrTalk(
        0x101,
        (
            "#00011F#4S(Isn't that man's image\x01",
            "totally different from\x01",
            "Mishy's!!?)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00006F...*ahem*, umm...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)

    ChrTalk(
        0x101,
        (
            "#00012FA-Anyway, let's head\x01",
            "back to the others.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#05520F............\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    VolumeBGM(0x64, 0x3E8)
    Sleep(1000)
    SetScenarioFlags(0x22, 3)
    NewScene("t1000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_5_1547 end

    SaveToFile()

Try(main)
