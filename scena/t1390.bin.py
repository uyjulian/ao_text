from ScenarioHelper import *

def main():
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
        "Staff Hanks",           # 1
        "Middle-aged man",               # 2
        "Mischief head",             # 3
    ))

    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(256, 0)                                        # 0

    ScpFunction((
        "Function_0_100",          # 00, 0
        "Function_1_127",          # 01, 1
        "Function_2_13A",          # 02, 2
        "Function_3_1437",         # 03, 3
        "Function_4_1482",         # 04, 4
        "Function_5_14CD",         # 05, 5
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
            "#05200FHow do I look \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FSuper cute \x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10109FYeah it suits you!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05206F(Because it covers the whole body\x01",
            "It looks nice, nothing … …)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FHow 's your comfort?\x01",
            "It seems to be somewhat hot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05201FAh……\x01",
            "I'm pretty enthusiastic\x01",
            "It seems to be muffled.\x02\x03",
            "#05203FAlso, the verticals match\x01",
            "Pretty shabby\x01",
            "It may be difficult to move.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FThe details are\x01",
            "Is not it?\x02\x03",
            "#00306FHey, envious.\x01",
            "Casually with fans girls\x01",
            "I do not know why.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05211FTo, do not make funny expressions!\x01",
            "Absolutely …\x02\x03",
            "#05205F……that?\x01",
            "By the way, is Tio?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FBy the way, just a while ago\x01",
            "Talk to the staff\x01",
            "I have gone somewhere … ….\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(30, 120, -1, -1)
    SetChrName("Voice of Tio")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "I'm here \x02",
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

    def lambda_5C7():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5C7)
    Sleep(50)

    def lambda_5D7():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5D7)
    Sleep(50)

    def lambda_5E7():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5E7)
    Sleep(50)

    def lambda_5F7():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5F7)
    Sleep(50)

    def lambda_607():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_607)
    OP_6F(0x79)
    Sound(121, 0, 100, 0)
    Sleep(500)
    BeginChrThread(0x103, 3, 0, 3)
    Sleep(500)
    BeginChrThread(0x8, 3, 0, 4)

    def lambda_62E():

        label("loc_62E")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_62E")

    QueueWorkItem2(0x101, 1, lambda_62E)

    def lambda_640():

        label("loc_640")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_640")

    QueueWorkItem2(0x102, 1, lambda_640)

    def lambda_652():

        label("loc_652")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_652")

    QueueWorkItem2(0x104, 1, lambda_652)

    def lambda_664():

        label("loc_664")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_664")

    QueueWorkItem2(0x109, 1, lambda_664)

    def lambda_676():

        label("loc_676")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_676")

    QueueWorkItem2(0x105, 1, lambda_676)
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
            "#05205FHuh……\x01",
            "Te, is it Tio?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#2679VMishishi\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xA77)
    OP_C9(0x1, 0x80000000)

    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "If you are older brother,\x01",
            "Did you forget my face?\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00305FWell, this is ….\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_812")
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
            "#1K◆ Between the curtains? (for test)\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "I met you\x01",          # 0
            "[I have not seen you]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_812")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_970")

    ChrTalk(
        0x102,
        (
            "#00102FTiny……\x01",
            "Cute one, Tio!\x02\x03",
            "#00105Fin addition,\x01",
            "That character is certain ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05522FYeah, my little sister's\x01",
            "It is \"Mie.\"\x02\x03",
            "#05524FBrother with just Doshi\x01",
            "Always watching warmly\x01",
            "He is a lonely girl.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05212F(Awesome)\x02\x03",
            "#05203Fby the way,\x01",
            "Even when I came to MWL before\x01",
            "I was seeing you …\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_ABB")

    label("loc_970")


    ChrTalk(
        0x102,
        (
            "#00102FTiny……\x01",
            "Cute one, Tio!\x02\x03",
            "#00105FBut this character\x01",
            "What the hell\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05522FYeah, my little sister's\x01",
            "It is \"Mie.\"\x02\x03",
            "#05524FBrother with just Doshi\x01",
            "Always watching warmly\x01",
            "He is a lonely girl.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05212F(Awesome)\x02\x03",
            "#05203Fby the way,\x01",
            "I have a Mister's sister\x01",
            "I heard it before ….\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ABB")


    ChrTalk(
        0x8,
        (
            "Well, suddenly\x01",
            "Lend me it\x01",
            "I was asked to do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you are a\x01",
            "I had plenty of shift\x01",
            "It was OK.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105FI see…\x02\x03",
            "But, suddenly\x01",
            "It means that it appeared on wearing ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05524FOnly Lloyd san,\x01",
            "I will support in the face.\x02\x03",
            "#05521FIf you do something Poca,\x01",
            "Because I can kick mercilessly.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x105,
        (
            "#10309FHaha, is it my sister's love of love?\x01",
            "Hey being loved Hey, Onii-chan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05206FAlmost too realistic \x07\x00\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05201F…… Or, like acting guidance\x01",
            "Can you do it?\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    def lambda_CF6():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_CF6)
    Sleep(50)

    def lambda_D06():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_D06)
    Sleep(50)

    def lambda_D16():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_D16)
    Sleep(50)

    def lambda_D26():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_D26)
    Sleep(50)

    def lambda_D36():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_D36)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "It's bad,\x01",
            "I wonder if there is such a time to go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It is almost time for Mitsuino\x01",
            "The patrol time is close.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "What is it like to behave like that\x01",
            "If you have a good heart, you manage to do something, maybe!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05206F(I'm worried)\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Also, after the patrol in the morning,\x01",
            "At the square in the theme park\x01",
            "There is a Mitsushi dance show.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Only there, for me\x01",
            "I went through the performance manual.\x01",
            "…… Please read and remember.\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Dance manual\x01",
            "I showed it.\x07\x00\x02",
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
            "Passionately, but still\x01",
            "You should dance to fancy.\x01\x01",
            "* To the last Kismethif,\x01",
            "\"Enjoy Michishi ☆\" and\x01",
            "Do not forget to scream.\x07\x00\x02",
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
        "#00306FThis is\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10112FI can not believe it\x01",
            "It is about …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "To tell the truth,\x01",
            "Michishi's character is\x01",
            "Leave it to the person of the actor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Since the creation of the theme park,\x01",
            "The best manual\x01",
            "I did not make anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, if I make a mistake\x01",
            "At that time, I will do that.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05524FMore than I will oversee\x01",
            "I will not forgive mistakes, though.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05206FI'll do my best…\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "Oops … It's time.\x01",
            "I will ask for preparation soon.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_11EC():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_11EC)
    Sleep(50)

    def lambda_11FC():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_11FC)
    Sleep(50)

    def lambda_120C():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_120C)
    Sleep(50)

    def lambda_121C():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_121C)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#00100FWell then, we\x01",
            "While doing a patrol in the park\x01",
            "You're killing time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10300FHaha good luck \x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05520FSo shall we go Lloyd?\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05205FS-sure \x02\x03",
            "#05203F(Anyway … I got it so far\x01",
            "An image of Misashi\x01",
            "I have no choice but to squeeze out. )\x02\x03",
            "#05200F(And … and the dance's watchword is\x01",
            "\"Enjoy Miserie ☆\", or?\x01",
            "You seemed better to remember. )\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well then,\x01",
            "For the children's dream\x01",
            "Good luck! It is!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'm counting on you!\x01",
            "Miss you, Meeee! It is!\x02",
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

    def Function_3_1437(): pass

    label("Function_3_1437")


    def lambda_143C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_143C)

    def lambda_144D():
        OP_95(0xFE, 370, 0, -2050, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_144D)
    WaitChrThread(0x103, 1)
    OP_95(0x103, -1210, 0, -1620, 2000, 0x0)
    TurnDirection(0x103, 0x101, 500)
    Return()

    # Function_3_1437 end

    def Function_4_1482(): pass

    label("Function_4_1482")


    def lambda_1487():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1487)

    def lambda_1498():
        OP_95(0xFE, 370, 0, -2050, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1498)
    WaitChrThread(0x8, 1)
    OP_95(0x8, -10, 0, -300, 2000, 0x0)
    OP_93(0x8, 0x10E, 0x1F4)
    Return()

    # Function_4_1482 end

    def Function_5_14CD(): pass

    label("Function_5_14CD")

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
            "#05520FOk then\x07\x00\x02",
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
        "#05526FOh I'm so sweaty\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009Fmy mother……\x01",
            "It seems I tried hard.\x02\x03",
            "#00000FNice job, Tio\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x176, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x176, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x176, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_17C8")

    ChrTalk(
        0x103,
        (
            "#05522FNo, Mr. Lloyd only\x01",
            "It was impeccable.\x02\x03",
            "#05524F…, that last dance too\x01",
            "It was fun to dance with me ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FEr, Hahaha ….\x01",
            "Do not be shy about it.\x02\x03",
            "#00003FWell, with.\x01",
            "It is almost time for everyone\x01",
            "I'd like to join you.\x02\x03",
            "#00005FActor only, the actor is\x01",
            "Is not it yet yet?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18E2")

    label("loc_17C8")


    ChrTalk(
        0x103,
        (
            "#05522FMr. Lloyd also.\x01",
            "It is a rough cut, but well\x01",
            "I think that it has done.\x02\x03",
            "#05524FIt is worthwhile that I also supervised\x01",
            "It was that it was there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000Fmy mother……\x01",
            "True, it was saved.\x02\x03",
            "#00003FWell, with.\x01",
            "It is almost time for everyone\x01",
            "I'd like to join you.\x02\x03",
            "#00005FActor only, the actor is\x01",
            "Is not it yet yet?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18E2")


    ChrTalk(
        0x103,
        "#05520FOh right where are they\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(30, 120, -1, -1)
    SetChrName("Middle-aged male voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#4S── Ga ha ha ha!\x01",
            "I kept you waiting!\x02",
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

    def lambda_19A0():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_19A0)
    Sleep(50)

    def lambda_19B0():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_19B0)
    OP_6F(0x1)
    Sound(121, 0, 100, 0)
    ClearChrFlags(0x9, 0x80)

    def lambda_19CA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_19CA)

    def lambda_19DB():
        OP_95(0xFE, 370, 0, -2050, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_19DB)
    WaitChrThread(0x9, 1)
    Sleep(300)

    ChrTalk(
        0x101,
        "#00011FHuh!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#05521F?!\x02",
    )

    CloseMessageWindow()
    OP_93(0x9, 0x13B, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x9,
        "Howdy!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x9,
        "Oh sorry sorry\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "The medicine I got is after meal\x01",
            "I guess you can not drink it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Because breakfast was also pulling out,\x01",
            "Attacked by all means\x01",
            "I got it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "……, Oretch's costume is\x01",
            "Is it a locker there?\x02",
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
            "Are you okay?\x01",
            "What did you do with your eyes full circled?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Well, I saw it somewhere.\x01",
            "It looks like a face ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Well, whatever, I will wear it.\x01",
            "Monday in Wonderland\x01",
            "It's essential.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I have a hole without me\x01",
            "You buried well.\x01",
            "Gas ha ha …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Oops, I do not have time to dabble.\x01",
            "Change your clothes quickly\x01",
            "I have to prepare in the afternoon.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-720, 1600, -10, 3000)

    def lambda_1C92():

        label("loc_1C92")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_1C92")

    QueueWorkItem2(0x101, 1, lambda_1C92)

    def lambda_1CA4():

        label("loc_1CA4")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_1CA4")

    QueueWorkItem2(0x103, 1, lambda_1CA4)
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
        "Missi",
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "── Transform complete ~ ☆\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x9,
        "Missi",
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "My older brother girl,\x01",
            "Thank you so much!\x01",
            "I am saved, Yo ~!\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x9,
        "Missi",
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "Leave it to me later!\x01",
            "Oh, that's it.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_68(1590, 1600, -1210, 3000)
    OP_95(0x9, -2860, 0, -1350, 2000, 0x0)
    OP_95(0x9, 370, 0, -2050, 2000, 0x0)

    def lambda_1E53():
        OP_95(0xFE, 210, 0, -4420, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1E53)
    Sound(121, 0, 100, 0)
    Sleep(500)

    def lambda_1E76():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1E76)
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
            "#00005F(P, Pro, … ….\x01",
            "Voice color is completely different … …)\x02\x03",
            "#00006F(Too so perfectly\x01",
            "Mitsida … … but …).\x02",
        )
    )

    CloseMessageWindow()
    Sleep(1000)
    OP_82(0xC8, 0x0, 0xBB8, 0x320)

    ChrTalk(
        0x101,
        (
            "#00011F#4S(Image and\x01",
            "It is completely different! It is! )\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00006FAhem, uhhh\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)

    ChrTalk(
        0x101,
        (
            "#00012FAnyway\x01",
            "Shall I return to everyone?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#05520F….\x02",
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

    # Function_5_14CD end

    SaveToFile()

Try(main)
