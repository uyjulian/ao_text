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
        "Function_3_14F7",         # 03, 3
        "Function_4_1542",         # 04, 4
        "Function_5_158D",         # 05, 5
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
        "#00100FPfft, it's cute.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10109FYes, it suits you a lot!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05206F(It covers my whole body,\x01",
            "so if it suits me or not is...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FHu hu, how do you feel it?\x01",
            "Somehow it looks hot to wear it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05201FYeah...\x01",
            "I guess that quite a lot\x01",
            "of heat will stay inside.\x02\x03",
            "#05203FAlso, the height fits,\x01",
            "but being pretty baggy,\x01",
            "it could be hard to move in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FDon't sweat the\x01",
            "small stuff, huh?\x02\x03",
            "#00306FTch, it must be nice.\x01",
            "You'll be able to nonchalantly\x01",
            "touch all the fangirls...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05211FD-Don't say such weird things!\x01",
            "Honestly...\x02\x03",
            "#05205F...Oh?\x01",
            "By the way, where's Tio?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FNow that you mention it,\x01",
            "she talked to the staff member\x01",
            "just before and went somewhere...\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(30, 120, -1, -1)
    SetChrName("Tio's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "──I am here.\x02",
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

    def lambda_5FC():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5FC)
    Sleep(50)

    def lambda_60C():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_60C)
    Sleep(50)

    def lambda_61C():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_61C)
    Sleep(50)

    def lambda_62C():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_62C)
    Sleep(50)

    def lambda_63C():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_63C)
    OP_6F(0x79)
    Sound(121, 0, 100, 0)
    Sleep(500)
    BeginChrThread(0x103, 3, 0, 3)
    Sleep(500)
    BeginChrThread(0x8, 3, 0, 4)

    def lambda_663():

        label("loc_663")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_663")

    QueueWorkItem2(0x101, 1, lambda_663)

    def lambda_675():

        label("loc_675")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_675")

    QueueWorkItem2(0x102, 1, lambda_675)

    def lambda_687():

        label("loc_687")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_687")

    QueueWorkItem2(0x104, 1, lambda_687)

    def lambda_699():

        label("loc_699")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_699")

    QueueWorkItem2(0x109, 1, lambda_699)

    def lambda_6AB():

        label("loc_6AB")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_6AB")

    QueueWorkItem2(0x105, 1, lambda_6AB)
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
            "#05205FHuh...\x01",
            "I-Is that you, Tio?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#2679VMishishi, I'm Miichie, you know?☆\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xA77)
    OP_C9(0x1, 0x80000000)

    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "Oh big brother,\x01",
            "did you forget my face?\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00305F*haah*, well...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_858")
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
            "#1K◆During the Intermission, I...(debug)\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[Met Miichie]\x01",             # 0
            "[Didn't met Miichie]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_858")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_9D9")

    ChrTalk(
        0x102,
        (
            "#00102FCute...\x01",
            "So cute, Tio!\x02\x03",
            "#00105FAlso, if I remember correctly,\x01",
            "that character is...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05522FYes, she is "Miichie",\x01",
            "Michey's little sister.\x02\x03",
            "#05524FShe is a gallant girl who always\x01",
            "amicably watches over her brother\x01",
            "who makes nothing but blunders.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05212F(A-Amicably...)\x02\x03",
            "#05203FBy the way, we met\x01",
            "her when we came to\x01",
            "M.W.L. previously too...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B3B")

    label("loc_9D9")


    ChrTalk(
        0x102,
        (
            "#00102FCute...\x01",
            "So cute, Tio!\x02\x03",
            "#00105FBut this character...\x01",
            "Who is it...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05522FYes, she is "Miichie",\x01",
            "Michey's little sister.\x02\x03",
            "#05524FShe is a gallant girl who always\x01",
            "amicably watches over her brother\x01",
            "who makes nothing but blunders.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05212F(A-Amicably...)\x02\x03",
            "#05203FBy the way, I think I\x01",
            "did hear that Michey\x01",
            "had a little sister...\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B3B")


    ChrTalk(
        0x8,
        (
            "Well, you see I was\x01",
            "just asked suddenly\x01",
            "to lend her that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I agreed since\x01",
            "there's time to\x01",
            "Miichie's shift.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105FI-I see...\x02\x03",
            "But suddenly appearing\x01",
            "wearing that, means...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05524FI will secretly give support\x01",
            "to Mr. Lloyd's Michey act.\x02\x03",
            "#05521FIf he makes some blunder,\x01",
            "I will mercilessly kick him.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x105,
        (
            "#10309FAhaha, the little sister's lashings of love, eh?\x01",
            "Aren't you loved, big brother?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05206FI'd wish she cut me some slack, though...\x07\x00\x02",
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

    def lambda_D7A():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D7A)
    Sleep(50)

    def lambda_D8A():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_D8A)
    Sleep(50)

    def lambda_D9A():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_D9A)
    Sleep(50)

    def lambda_DAA():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_DAA)
    Sleep(50)

    def lambda_DBA():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_DBA)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "I'm sorry, but I guess\x01",
            "we don't have time at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Michey's tour hour\x01",
            "is already close.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Come on, if you dedicate to act and move like\x01",
            "the original, somehow you'll be fine, maybe!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05206F(N-Now I feel uneasy...)\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Then, after touring around in\x01",
            "the morning, there's the Michey\x01",
            "dance show at the theme park plaza.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I prepared an acting\x01",
            "manual just for that.\x01",
            "...Read it in a flash and remember it.\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "You were showed\x01",
            "the dance manual.\x07\x00\x02",
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
            "Dance enthusiastically\x01",
            "and yet fancily.\x01\x01",
            "※Don't forget to shout\x01",
            "　"Enjoy Michey☆" as\x01",
            "　the closing line.\x07\x00\x02",
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
            "To tell you the truth,\x01",
            "we leave everything up to the actor\x01",
            "for the character's personality.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Since the theme park founding,\x01",
            "there hasn't been a single\x01",
            "decent manual made.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, if you make a mistake, \x01",
            "think about it when the time comes.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05524FSince I am supervising,\x01",
            "I will not tolerate mistakes.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05206FW-What should I do...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "Oh...it's time.\x01",
            "Take care of the preparations.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_12DA():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_12DA)
    Sleep(50)

    def lambda_12EA():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_12EA)
    Sleep(50)

    def lambda_12FA():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_12FA)
    Sleep(50)

    def lambda_130A():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_130A)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#00100FThen, we will pass the time\x01",
            "while going around the park.\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10300FHu hu, best of luck to you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05520FThen, let's go, Mr. Lloyd.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05205FR-Right...\x02\x03",
            "#05203F(In any case...I can only\x01",
            "force myself to remember\x01",
            "how Michey is.)\x02\x03",
            "#05200F(Also...the slogan is\x01",
            ""Enjoy Michey☆", eh?\x01",
            "Better remember that.)\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Then, do your best\x01",
            "for the sake of the\x01",
            "children's dreams!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'm counting on you!\x01",
            "Michey, Miichie!!\x02",
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

    def Function_3_14F7(): pass

    label("Function_3_14F7")


    def lambda_14FC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_14FC)

    def lambda_150D():
        OP_95(0xFE, 370, 0, -2050, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_150D)
    WaitChrThread(0x103, 1)
    OP_95(0x103, -1210, 0, -1620, 2000, 0x0)
    TurnDirection(0x103, 0x101, 500)
    Return()

    # Function_3_14F7 end

    def Function_4_1542(): pass

    label("Function_4_1542")


    def lambda_1547():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1547)

    def lambda_1558():
        OP_95(0xFE, 370, 0, -2050, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1558)
    WaitChrThread(0x8, 1)
    OP_95(0x8, -10, 0, -300, 2000, 0x0)
    OP_93(0x8, 0x10E, 0x1F4)
    Return()

    # Function_4_1542 end

    def Function_5_158D(): pass

    label("Function_5_158D")

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
        "#05526F*sigh*...I am drenched in sweat.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHa ha...\x01",
            "It seems you worked really hard.\x02\x03",
            "#00000FGood job, Tio.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x176, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x176, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x176, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_18AD")

    ChrTalk(
        0x103,
        (
            "#05522FNo, Mr. Lloyd interpretation of \x01",
            "Michey was really well done too.\x02\x03",
            "#05524F...Also, I had fun dancing\x01",
            "together the last dance too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FEhhm, ha ha...\x01",
            "Somehow you're making me blush.\x02\x03",
            "#00003F...Well then.\x01",
            "I think it's about time\x01",
            "we meet with everyone.\x02\x03",
            "#00005FIs the real actor for\x01",
            "Michey not here yet...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19DC")

    label("loc_18AD")


    ChrTalk(
        0x103,
        (
            "#05522FMr. Lloyd too.\x01",
            "Still rough around the edges,\x01",
            "but I think it was well done.\x02\x03",
            "#05524FIt was worth to\x01",
            "supervise you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FHa ha...\x01",
            "Thank you, you really helped me.\x02\x03",
            "#00003F...Well then.\x01",
            "I think it's about time\x01",
            "we meet with everyone.\x02\x03",
            "#00005FIs the real actor for\x01",
            "Michey not here yet...?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19DC")


    ChrTalk(
        0x103,
        "#05520FNow that you mention it, he seems to be lat──\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(30, 120, -1, -1)
    SetChrName("Middle-Aged Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#4S──Gwah hah hah hah ha!\x01",
            "Sorry to have kept ya waitin'!\x02",
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

    def lambda_1AC2():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1AC2)
    Sleep(50)

    def lambda_1AD2():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1AD2)
    OP_6F(0x1)
    Sound(121, 0, 100, 0)
    ClearChrFlags(0x9, 0x80)

    def lambda_1AEC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1AEC)

    def lambda_1AFD():
        OP_95(0xFE, 370, 0, -2050, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1AFD)
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
        "Gwah hah ha, my bad, my bad!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Seems ya can't take da medicines\x01",
            "I got after eatin', ya know!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I skipped breakfast too, so\x01",
            "I unintentionally ate tons!\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...So, is my costume\x01",
            "in that locker?\x02",
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
            "...Huh? What's wrong?\x01",
            "Ya look really surprised?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "By the way, it seems\x01",
            "I saw yer faces somewhere...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Well, anyhow, I owe ya one.\x01",
            "Michey is indispensable to\x01",
            "Wonderland, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Ya filled fo'\x01",
            "me well.\x01",
            "Gwah hah ha...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Oops, got no time to chit chat.\x01",
            "Gotta change at once and\x01",
            "prepare for the afternoon.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-720, 1600, -10, 3000)

    def lambda_1DC5():

        label("loc_1DC5")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_1DC5")

    QueueWorkItem2(0x101, 1, lambda_1DC5)

    def lambda_1DD7():

        label("loc_1DD7")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_1DD7")

    QueueWorkItem2(0x103, 1, lambda_1DD7)
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
        "Michey",
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "──Transformation, complete☆\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x9,
        "Michey",
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "Thank you mister\x01",
            "and missy!\x01",
            "You saved me!\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x9,
        "Michey",
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

    def lambda_1F70():
        OP_95(0xFE, 210, 0, -4420, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1F70)
    Sound(121, 0, 100, 0)
    Sleep(500)

    def lambda_1F93():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1F93)
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
            "#00005F(W-What a pro... Even the timbre \x01",
            "of his voice is totally different...)\x02\x03",
            "#00006F(He's so perfect as\x01",
            "Michey, how...ever...)\x02",
        )
    )

    CloseMessageWindow()
    Sleep(1000)
    OP_82(0xC8, 0x0, 0xBB8, 0x320)

    ChrTalk(
        0x101,
        (
            "#00011F#4S(Isn't that man's character totally\x01",
            "different from Michey's image!!?)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00006F...*cough*, eeeehm...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)

    ChrTalk(
        0x101,
        (
            "#00012FI-In any case, let's go\x01",
            "back where the others are.\x02",
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

    # Function_5_158D end

    SaveToFile()

Try(main)
