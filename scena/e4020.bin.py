from ScenarioHelper import *

def main():
    CreateScenaFile(
        "e4020.bin",                # FileName
        "e4020",                    # MapName
        "e4020",                    # Location
        0x0000,                     # MapIndex
        "ed7000",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, -123000, 0, 106000, 0, 0, 1, 1, 0, 0, 0, 1],
    )

    BuildStringList((
        "e4020",                  # 0
        "Claudia Hime",         # 1
        "Lector clerk",         # 2
        "President Lock Smith",     # 3
        "Keya",                 # 4
        "Suzuku",                 # 5
        "Chair",                   # 6
        "Chair",                   # 7
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    246,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    246,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(388, 0)                                        # 0

    ScpFunction((
        "Function_0_184",          # 00, 0
        "Function_1_1B9",          # 01, 1
        "Function_2_1BA",          # 02, 2
        "Function_3_1361",         # 03, 3
        "Function_4_13B6",         # 04, 4
        "Function_5_140B",         # 05, 5
        "Function_6_1460",         # 06, 6
        "Function_7_14B5",         # 07, 7
        "Function_8_150A",         # 08, 8
        "Function_9_155F",         # 09, 9
        "Function_10_26BA",        # 0A, 10
    ))


    def Function_0_184(): pass

    label("Function_0_184")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_198")
    ClearScenarioFlags(0x22, 0)
    Event(0, 9)
    Jump("loc_1A7")

    label("loc_198")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_1A7")
    ClearScenarioFlags(0x22, 1)
    Event(0, 10)

    label("loc_1A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1B8")
    Event(0, 2)

    label("loc_1B8")

    Return()

    # Function_0_184 end

    def Function_1_1B9(): pass

    label("Function_1_1B9")

    Return()

    # Function_1_1B9 end

    def Function_2_1BA(): pass

    label("Function_2_1BA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch11000.itc", 0x1E)
    LoadChrToIndex("chr/ch12400.itc", 0x1F)
    SetChrPos(0x0, -55750, 0, 113000, 180)
    SetChrPos(0x1, -55100, 0, 114400, 180)
    SetChrPos(0x2, -53700, 0, 114400, 180)
    SetChrPos(0x3, -53000, 0, 113300, 270)
    SetChrPos(0x4, -52300, 0, 114700, 270)
    SetChrPos(0x5, -51200, 0, 114200, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, -53000, 0, -2900, 270)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, -55000, 0, -2900, 90)
    OP_68(-54000, 1100, 113000, 0)
    MoveCamera(51, 21, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15820, 0)
    FadeToBright(1000, 0)
    Sleep(500)
    OP_63(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_318")

    ChrTalk(
        0x101,
        "#00005F#5P(That is……)\x02",
    )

    CloseMessageWindow()
    Jump("loc_412")

    label("loc_318")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_34B")

    ChrTalk(
        0x102,
        "#00105F#5P(That one ……)\x02",
    )

    CloseMessageWindow()
    Jump("loc_412")

    label("loc_34B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_380")

    ChrTalk(
        0x103,
        "#00205F#5P(……That is……)\x02",
    )

    CloseMessageWindow()
    Jump("loc_412")

    label("loc_380")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B3")

    ChrTalk(
        0x104,
        "#00301F#5P(what……?)\x02",
    )

    CloseMessageWindow()
    Jump("loc_412")

    label("loc_3B3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E6")

    ChrTalk(
        0x109,
        "#10105F#5P(Okay … ….?\x02",
    )

    CloseMessageWindow()
    Jump("loc_412")

    label("loc_3E6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_412")

    ChrTalk(
        0x105,
        "#10302F#5P(Wow …?.?)\x02",
    )

    CloseMessageWindow()

    label("loc_412")

    StopBGM(0xFA0)
    OP_68(-54000, 1100, 100000, 3000)
    Sleep(1500)
    Fade(1000)
    OP_68(-54000, 1100, 3100, 0)
    MoveCamera(125, 21, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16000, 0)
    OP_68(-54000, 1100, -2900, 3000)
    OP_0D()
    OP_6F(0x79)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7523", 0)
    Sleep(300)
    OP_68(-53970, 1100, -3250, 2000)
    MoveCamera(129, 16, 0, 2000)
    OP_6E(600, 2000)
    SetCameraDistance(14000, 2000)
    OP_6F(0x79)
    MoveCamera(133, 18, 0, 50000)
    SetCameraDistance(13270, 50000)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#5P#07004FIs that so……\x01",
            "With Lucy-senpai.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#12P#11506FOh, before this to Remyferia\x01",
            "When you go on business you will be grunt.\x02\x03",
            "I managed to escape\x01",
            "I was caught flying.\x02\x03",
            "#11501FWhat do you think was beaten up?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#07002F…… One shot.\x02\x03",
            "#07009FInstead, hanging on\x01",
            "Was not it crying?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#12P#11501F……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#07004FHehu ……\x01",
            "Lucy-senpai's feelings\x01",
            "Because I understand.\x02\x03",
            "#07001FPerhaps, seniors usually do,\x01",
            "How dangerous it is doing\x01",
            "I think that I noticed it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#12P#11506FAh, women sometimes\x01",
            "It will be sharp and terrible.\x02\x03",
            "#11510FIt is hard to do and it can not be helped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#07004FHuhu, is it self-owned?\x02\x03",
            "#07008F……nostalgic.\x02\x01",
            "#07002FI have not met Leo seniors,\x01",
            "Anyway I would like to join an alumni association.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#12P#11501F……………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#07003FSenpai, are not you?\x02\x03",
            "#07002FThere is \"O, per Michelam\x01",
            "Do you want to do a luxury par! \"\x01",
            "── I would say that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#12P#11504FHaha … I got a bottle.\x02\x03",
            "#11500F──You can not make a promise\x01",
            "Well, I will try hard.\x02\x03",
            "Do not expect me, please wait.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#07009FI understand.\x01",
            "I am looking forward.\x02\x03",
            "#07002FWell then, I am with this.\x01",
            "Excuse me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#12P#11509FOh, Sieg's bastard\x01",
            "Please say hello.\x02",
        )
    )

    CloseMessageWindow()
    OP_92(0x8, 0xFFFF379C, 0xFFFFFC18, 0x15E)
    Sleep(300)
    OP_68(-52720, 1100, -2590, 3500)
    MoveCamera(133, 18, 0, 3500)
    SetCameraDistance(13270, 3500)

    def lambda_993():
        OP_95(0xFE, -51300, 0, -1000, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_993)
    WaitChrThread(0x8, 1)
    OP_93(0x8, 0x5A, 0x1F4)
    Sound(103, 0, 100, 0)
    ClearMapObjFlags(0x1, 0x10)
    OP_71(0x1, 0x0, 0x5, 0x0, 0x0)
    OP_79(0x1)

    def lambda_9D3():
        OP_95(0xFE, -48300, 0, -1000, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_9D3)
    Sleep(1000)

    def lambda_9F0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_9F0)
    WaitChrThread(0x8, 1)
    Sound(104, 0, 100, 0)
    OP_71(0x1, 0x5, 0x0, 0x0, 0x0)
    OP_79(0x1)
    Sleep(300)

    ChrTalk(
        0x9,
        (
            "#11P#11506FWhew ……\x01",
            "It is growing really.\x02\x03",
            "#11500FAs expected the Queen next year.\x01",
            "─ ─ Do not you agree?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00011F……!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10302FHuh, was you noticed?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(-55530, 1100, -1440, 3000)
    MoveCamera(125, 21, 0, 3000)
    OP_6E(550, 3000)
    SetCameraDistance(16650, 3000)

    def lambda_AFA():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_AFA)
    SetChrPos(0x101, -56200, 0, 7600, 180)
    SetChrPos(0x102, -54900, 0, 7600, 180)
    SetChrPos(0x103, -55900, 0, 8700, 180)
    SetChrPos(0x104, -54600, 0, 8700, 180)
    SetChrPos(0x109, -56200, 0, 9800, 180)
    SetChrPos(0x105, -54900, 0, 9800, 180)

    def lambda_B6D():
        OP_97(0x101, 0x0, 0x0, 0xFFFFE0C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_B6D)
    Sleep(50)

    def lambda_B8A():
        OP_97(0x102, 0x0, 0x0, 0xFFFFE0C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_B8A)
    Sleep(50)

    def lambda_BA7():
        OP_97(0x103, 0x0, 0x0, 0xFFFFE0C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_BA7)
    Sleep(50)

    def lambda_BC4():
        OP_97(0x104, 0x0, 0x0, 0xFFFFE0C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_BC4)
    Sleep(50)

    def lambda_BE1():
        OP_97(0x109, 0x0, 0x0, 0xFFFFE0C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_BE1)
    Sleep(50)

    def lambda_BFE():
        OP_97(0x105, 0x0, 0x0, 0xFFFFE0C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_BFE)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#6P#00006F……Excuse me.\x01",
            "I intend to eavesdrop\x01",
            "I did not have it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103F#6PThat……\x01",
            "I could hear it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00202FBut, Ellie.\x01",
            "You were very curious, were not you?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(
        0x102,
        "#5P#00112FTe, Tio.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309F#6PNo, but, I do not mind.\x02\x03",
            "#00302FTo a princess in one country\x01",
            "You are not cheap enough, are not you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11503F#11POh, it is just a school junior.\x02\x03",
            "#11500FEven though it is not a Sunday school\x01",
            "I am the Royal University of Genes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10305F#6PRoyal University of Genis ……\x01",
            "It is certainly in Ribehr.\x01",
            "Was it a famous high school?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#6PYes, certainly international students\x01",
            "I accept a lot, but …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10105FThen then at the national expense\x01",
            "Did you study abroad?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11504F#11PNo, it is pocket money.\x01",
            "─ ─ Giulious' s Osan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00013FIt is!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11504F#11PThen, I\x01",
            "This will be rude.\x02\x03",
            "#11505FOh, so so\x01",
            "Are they called by raccoons?\x02\x03",
            "#11509FBoth are not straightforward\x01",
            "You should pay attention at best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00011FAh……\x02",
    )

    CloseMessageWindow()

    def lambda_FDB():

        label("loc_FDB")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_FDB")

    QueueWorkItem2(0x101, 2, lambda_FDB)

    def lambda_FED():

        label("loc_FED")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_FED")

    QueueWorkItem2(0x102, 2, lambda_FED)

    def lambda_FFF():

        label("loc_FFF")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_FFF")

    QueueWorkItem2(0x103, 2, lambda_FFF)

    def lambda_1011():

        label("loc_1011")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_1011")

    QueueWorkItem2(0x109, 2, lambda_1011)

    def lambda_1023():

        label("loc_1023")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_1023")

    QueueWorkItem2(0x105, 2, lambda_1023)

    def lambda_1035():

        label("loc_1035")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_1035")

    QueueWorkItem2(0x104, 2, lambda_1035)

    def lambda_1047():
        OP_95(0xFE, -57100, 0, -1400, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1047)
    WaitChrThread(0x9, 1)

    def lambda_1065():
        OP_95(0xFE, -57100, 0, 1900, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1065)
    WaitChrThread(0x9, 1)
    StopBGM(0x1770)
    Fade(500)
    OP_68(-54000, 1100, 103000, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17500, 0)
    SetChrPos(0x101, -56200, 0, 98800, 0)
    SetChrPos(0x102, -54900, 0, 98800, 0)
    SetChrPos(0x103, -55900, 0, 99900, 0)
    SetChrPos(0x104, -54600, 0, 99900, 0)
    SetChrPos(0x109, -56200, 0, 101000, 0)
    SetChrPos(0x105, -54900, 0, 101000, 0)
    SetChrPos(0x9, -55500, 0, 103000, 0)
    ClearChrFlags(0x9, 0x4)
    OP_68(-54000, 1100, 113000, 5000)
    SetCameraDistance(17500, 5000)

    def lambda_1151():
        OP_95(0xFE, -55500, 0, 112500, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1151)
    WaitChrThread(0x9, 1)

    def lambda_116F():
        OP_95(0xFE, -51500, 0, 112500, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_116F)
    WaitChrThread(0x9, 1)

    def lambda_118D():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFEC78, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_118D)
    Sleep(500)

    def lambda_11AA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_11AA)
    WaitChrThread(0x9, 1)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0x109, 0x2)
    EndChrThread(0x105, 0x2)
    SetChrFlags(0x9, 0x80)
    OP_6F(0x79)
    Fade(500)
    OP_68(-55640, 1100, 100200, 0)
    MoveCamera(55, 23, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17500, 0)
    OP_0D()

    ChrTalk(
        0x103,
        (
            "#12P#00211F……As usual\x01",
            "It is a suspicious person with suspiciousness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F#11PThe next Queen of Libert\x01",
            "Is it an information officer who is senior? …\x02\x03",
            "#10302FHuh, it is more and more interesting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003F…… Anyway\x01",
            "As he under the control of \"Chairman of Iron Blood\"\x01",
            "It is certain that it is moving.\x02\x03",
            "#00001FWhat are you aiming at … ….\x01",
            "It seems necessary to find out.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7111", 0)
    SetScenarioFlags(0x142, 2)
    EventEnd(0x5)
    NewScene("c1550", 126, 0, 0)
    IdleLoop()
    Return()

    # Function_2_1BA end

    def Function_3_1361(): pass

    label("Function_3_1361")


    def lambda_1366():
        OP_96(0xFE, 0xFFFE2C08, 0x0, 0x324B0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1366)

    def lambda_1380():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1380)
    WaitChrThread(0xFE, 1)

    def lambda_1395():
        OP_95(0xFE, -122600, 0, 205400, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1395)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_3_1361 end

    def Function_4_13B6(): pass

    label("Function_4_13B6")


    def lambda_13BB():
        OP_96(0xFE, 0xFFFE2C08, 0x0, 0x324B0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_13BB)

    def lambda_13D5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_13D5)
    WaitChrThread(0xFE, 1)

    def lambda_13EA():
        OP_95(0xFE, -122600, 0, 206600, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_13EA)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_4_13B6 end

    def Function_5_140B(): pass

    label("Function_5_140B")


    def lambda_1410():
        OP_96(0xFE, 0xFFFE2C08, 0x0, 0x324B0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1410)

    def lambda_142A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_142A)
    WaitChrThread(0xFE, 1)

    def lambda_143F():
        OP_95(0xFE, -121500, 0, 204600, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_143F)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_5_140B end

    def Function_6_1460(): pass

    label("Function_6_1460")


    def lambda_1465():
        OP_96(0xFE, 0xFFFE2C08, 0x0, 0x324B0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1465)

    def lambda_147F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_147F)
    WaitChrThread(0xFE, 1)

    def lambda_1494():
        OP_95(0xFE, -121500, 0, 207400, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1494)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_6_1460 end

    def Function_7_14B5(): pass

    label("Function_7_14B5")


    def lambda_14BA():
        OP_96(0xFE, 0xFFFE2C08, 0x0, 0x324B0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_14BA)

    def lambda_14D4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_14D4)
    WaitChrThread(0xFE, 1)

    def lambda_14E9():
        OP_95(0xFE, -120800, 0, 205400, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_14E9)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_7_14B5 end

    def Function_8_150A(): pass

    label("Function_8_150A")


    def lambda_150F():
        OP_96(0xFE, 0xFFFE2C08, 0x0, 0x324B0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_150F)

    def lambda_1529():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1529)
    WaitChrThread(0xFE, 1)

    def lambda_153E():
        OP_95(0xFE, -120800, 0, 206600, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_153E)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_8_150A end

    def Function_9_155F(): pass

    label("Function_9_155F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch11712.itc", 0x1E)
    LoadChrToIndex("chr/ch00002.itc", 0x1F)
    LoadChrToIndex("chr/ch00102.itc", 0x20)
    LoadChrToIndex("chr/ch00202.itc", 0x21)
    LoadChrToIndex("chr/ch00302.itc", 0x22)
    LoadChrToIndex("chr/ch02902.itc", 0x23)
    LoadChrToIndex("chr/ch03002.itc", 0x24)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu07500.itp")
    SetChrPos(0x101, -117500, 0, 206000, 270)
    SetChrPos(0x102, -117500, 0, 206000, 270)
    SetChrPos(0x103, -117500, 0, 206000, 270)
    SetChrPos(0x104, -117500, 0, 206000, 270)
    SetChrPos(0x109, -117500, 0, 206000, 270)
    SetChrPos(0x105, -117500, 0, 206000, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0xA, 0x1E)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, -130000, 50, 206000, 90)
    OP_68(-120300, 1100, 206000, 0)
    MoveCamera(55, 13, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17500, 0)
    FadeToBright(1000, 0)
    StopBGM(0x1388)
    ClearMapObjFlags(0x7, 0x10)
    OP_74(0x7, 0x1E)
    OP_71(0x7, 0x0, 0x5, 0x0, 0x0)
    OP_79(0x7)
    OP_68(-126300, 1100, 206000, 5000)
    SetCameraDistance(18500, 5000)
    BeginChrThread(0x101, 3, 0, 3)
    Sleep(700)
    BeginChrThread(0x102, 3, 0, 4)
    Sleep(700)
    BeginChrThread(0x103, 3, 0, 5)
    Sleep(700)
    BeginChrThread(0x104, 3, 0, 6)
    Sleep(700)
    BeginChrThread(0x109, 3, 0, 7)
    Sleep(700)
    BeginChrThread(0x105, 3, 0, 8)
    Sleep(1700)
    Sound(104, 0, 100, 0)
    OP_71(0x7, 0x5, 0x0, 0x0, 0x0)
    OP_79(0x7)
    WaitChrThread(0x105, 3)

    ChrTalk(
        0x101,
        (
            "#00003F#11P── Excuse me, Your Excellency.\x02\x03",
            "#00001FCrossbell Police, Special Affairs Support Division,\x01",
            "We invited you by invitation.\x02",
        )
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7583", 0)

    ChrTalk(
        0xA,
        (
            "#6P#07509FOh, I often came.\x02\x03",
            "#07500FDo not hold back.\x01",
            "Come on, sit down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#11PYes.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00104F#11PThen, please spare your words …\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-128500, 2700, 105900, 0)
    MoveCamera(303, 19, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16500, 0)
    OP_68(-128500, 900, 105900, 3000)
    SetChrChipByIndex(0x101, 0x1F)
    SetChrSubChip(0x101, 0x1)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x2)
    SetChrChipByIndex(0x103, 0x21)
    SetChrSubChip(0x103, 0x1)
    SetChrChipByIndex(0x104, 0x22)
    SetChrSubChip(0x104, 0x2)
    SetChrChipByIndex(0x109, 0x23)
    SetChrSubChip(0x109, 0x1)
    SetChrChipByIndex(0x105, 0x24)
    SetChrSubChip(0x105, 0x1)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x105, 0x4)
    SetChrPos(0x101, -128400, 50, 103900, 0)
    SetChrPos(0x102, -128199, 50, 107200, 200)
    SetChrPos(0x103, -127500, 50, 103900, 0)
    SetChrPos(0x104, -126700, 50, 107200, 200)
    SetChrPos(0x109, -126600, 50, 103900, 0)
    SetChrPos(0x105, -125700, 50, 103900, 0)
    SetChrPos(0xA, -130000, 50, 105900, 90)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xD, 0x80)
    OP_78(0xA, 0xD)
    ClearChrFlags(0xE, 0x80)
    OP_78(0xB, 0xE)
    OP_49()
    SetChrPos(0xD, -128100, 0, 107500, 20)
    OP_D5(0xD, 0x0, 0x4E20, 0x0, 0x0)
    SetChrPos(0xE, -126600, 0, 107500, 20)
    OP_D5(0xE, 0x0, 0x4E20, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    SetCameraDistance(15500, 80000)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0xA,
        (
            "Wait,\x01",
            "Have you been suddenly surprised?\x02\x03",
            "No, this is not the case\x01",
            "I thought that time is good.\x02\x03",
            "I would be busy, Suman.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    ChrTalk(
        0x101,
        "#6P#00011FNo, such a thing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00102FThank you for your consideration.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 0x1)
    Sleep(300)

    ChrTalk(
        0xA,
        (
            "#07505F#5PCertainly, Mayor Mcdael\x01",
            "Was it a grandchild?\x02\x03",
            "Surely before, at a celebration or something\x01",
            "Have not you met up?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104FYes, my grandfather's accompanying the Republic\x01",
            "I am visiting you as soon as I visit.\x02\x03",
            "#00100FIt will be two years ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#07509F#5POh, it certainly was.\x02\x03",
            "#07500FHowever, Mayor Maccdael\x01",
            "Retire now#2RA number#And he is the autonomous state chairman ……\x02\x03",
            "#07504FThat year, that passion.\x01",
            "Indeed the politician's view#2RMirror#It is said.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109FHehe, when my grandfather listens\x01",
            "I am sure you will be delighted.\x02\x03",
            "#00108FBy the way Excellency ──\x01",
            "How do you like it today?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 0x0)
    Sleep(300)

    ChrTalk(
        0xA,
        (
            "#07509F#5PHa ha ha, your story\x01",
            "I heard it from Kirika.\x02\x03",
            "#07500FThe end of the \"black auctioneer\"\x01",
            "I heard that it was painful.\x02\x03",
            "#07503FAs I said,\x01",
            "Previous Chair Hartmann\x01",
            "It was a naughty man.\x02\x03",
            "#07500FI made a chance to make up for my loss\x01",
            "The faces of the meritorious persons are\x01",
            "I wanted to see it once.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00002FI am excited.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00306FWell, either way without permission\x01",
            "It looks like just being destroyed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00208F……I agree.\x01",
            "As I was involved with such a cult\x01",
            "I wonder if it is out ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#07505F#5POh yeah, that and that culture.\x02\x03",
            "#07503F\"D∴G Church\" ──\x01",
            "Although it was doing evil in all over the continent,\x01",
            "The greatest victim is in our country.\x02\x03",
            "#07501FI also stabbed a stop in them\x01",
            "I wanted to thank you again!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00011FNo……\x01",
            "It was just a matter of course.\x02\x03",
            "#00004FMoreover, their contribution etc.\x01",
            "It's just a trivial thing -\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#07509F#5PHa ha ha ha, stop humble.\x02\x03",
            "Everything even the guard was being manipulated\x01",
            "It seems that it was in a crisis situation, is not it?\x02\x03",
            "#07502FIn the meantime, protect one girl\x01",
            "I confronted the evil cults … …\x02\x03",
            "No, nothing can be done inside!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00012FNo … really, I'm afraid.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00103FExcessive words, painfully.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#07506F#5PActually, if that incident failed poorly\x01",
            "It would have been a serious thing.\x02\x03",
            "IBC was also occupied by evil cults,\x01",
            "International trade and finance stop … …\x02\x03",
            "#07501F── So that also in the Republic's economy\x01",
            "It must have been serious damage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00001F……!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108F……that is.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#07505F#5PHmm, when that happens\x01",
            "I ought to give you a medal as well\x01",
            "I do not know how cool it is.\x02\x03",
            "#07509FOK, as soon as I return home\x01",
            "Let me arrange for lots!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00011FNo……!\x01",
            "One moment, please.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00211FEven though it is a case in autonomous province\x01",
            "It is not until you receive a medal from the Republic government\x01",
            "Somewhat funny …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00306FEven from McDowell\x01",
            "I already have a certificate of commendation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#07504F#5PNothing is wrong.\x02\x03",
            "#07502F── The problem of the crossbell is,\x01",
            "Because it is a matter of our country which is a religious country.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#6P#00013F……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108F……Your Honor………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#07509F#5PHa ha ha ha.\x01",
            "I do not have such a face.\x02\x03",
            "#07502FAlso in \"Iraq's Prime Minister\"\x01",
            "Are they called?\x02\x03",
            "I'd like to talk a little more\x01",
            "You should go soon.\x02\x03",
            "#07504F─ ─ Ah, I will arrange the medal surely\x01",
            "Please wait looking forward to it?\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(17000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    StopBGM(0xFA0)
    WaitBGM()
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x103, 0x4)
    ClearChrFlags(0x104, 0x4)
    ClearChrFlags(0x109, 0x4)
    ClearChrFlags(0x105, 0x4)
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x23, 1)
    NewScene("c1550", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_9_155F end

    def Function_10_26BA(): pass

    label("Function_10_26BA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch11600.itc", 0x1E)
    LoadChrToIndex("chr/ch05410.itc", 0x1F)
    LoadChrToIndex("apl/ch51603.itc", 0x20)
    LoadChrToIndex("apl/ch51604.itc", 0x21)
    LoadEffect(0x0, "event\\ev500_00.eff")
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis412.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu12300.itp")
    CreatePortrait(2, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu11202.itp")
    SetChrChipByIndex(0xB, 0x1E)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, 26500, 0, 26800, 0)
    SetChrChipByIndex(0xC, 0x1F)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, 26500, 0, 19000, 0)
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x0, 31000, 0, 23000, 0)
    PlayEffect(0x0, 0xFF, 0xB, 0x1, 0, 750, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetMapObjFrame(0xFF, "wlight_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "toreru", 0x1, 0x1)
    SetMapObjFrame(0xFF, "back_pano", 0x1, 0x1)
    SetMapObjFrame(0xFF, "ent01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "ent02", 0x0, 0x1)
    OP_68(26500, 1000, 26800, 0)
    MoveCamera(41, 19, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16340, 0)
    OP_63(0xB, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    SetCameraDistance(15340, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)
    OP_64(0xB)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#40W…………………………………….\x02",
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

    NpcTalk(
        0xC,
        "Voice of a girl",
        "Keyaちゃん……\x02",
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0xB, 0xB4, 0x1F4)
    Fade(500)
    OP_68(26500, 1000, 24400, 0)
    MoveCamera(137, 17, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15500, 0)
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetMapObjFrame(0xFF, "wlight_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "toreru", 0x0, 0x1)
    SetMapObjFrame(0xFF, "back_pano", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ent01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ent02", 0x1, 0x1)
    OP_68(26500, 1000, 23450, 1500)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12302F#5Pあ、Suzuku……\x02\x03",
            "Is your eyes going well now?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_68(26500, 1000, 25480, 3000)
    SetCameraDistance(14500, 3000)

    def lambda_2A7F():
        OP_95(0xFE, 26500, 0, 24900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_2A7F)
    WaitChrThread(0xC, 1)
    OP_6F(0x79)
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0xC,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#30WYeah … … already dizzy#4Rdizzy#If not,\x01",
            "I got to see the color … ….\x02\x03",
            "All …\x01",
            "Keyaちゃんのおかげだよ。\x02\x03",
            "……Thank you very much.\x02",
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
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#5P#12309FWell … good.\x02\x03",
            "#12302Fでも、Suzukuと病院の人たちが\x01",
            "Because I've been working hard all the time?\x02\x03",
            "Keyaはあくまで\x01",
            "I only did the last push.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#11P#11226Fis that so……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#5P#12304FBesides that, the \"power\" of\x01",
            "It is OK to make effective use.\x02\x03",
            "#12314Fえへへ、Suzukuの目が治せたなら\x01",
            "It was worth it this way …\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(14000, 500)
    Fade(250)
    SetChrChipByIndex(0xC, 0x20)
    SetChrSubChip(0xC, 0x0)
    SetChrFlags(0xC, 0x10)
    SetChrFlags(0xC, 0x2)
    SetChrFlags(0xC, 0x20)
    OP_0D()
    Sleep(150)
    OP_82(0x64, 0x0, 0xBB8, 0xC8)

    ChrTalk(
        0xC,
        "#11P#11232F#4S─ ─ ─ but!\x02",
    )

    CloseMessageWindow()

    def lambda_2D40():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_2D40)
    WaitChrThread(0xC, 2)
    Sleep(300)

    ChrTalk(
        0xC,
        (
            "#11P#11226F#30W…, I'm glad you … ….?\x02\x03",
            "I was anxious because my eyes could not be seen forever ……\x01",
            "…… Become my dad's luggage ……\x02\x03",
            "#11228FKeyaちゃんと友だちになれたのに\x01",
            "I do not know what kind of face it is …!\x02\x03",
            "#11227FIn this way you can see the face\x01",
            "I am glad that tears come out … but …!\x02",
        )
    )

    CloseMessageWindow()
    OP_68(26500, 1000, 25870, 600)
    SetChrChipByIndex(0xC, 0x1F)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x10)
    ClearChrFlags(0xC, 0x2)
    ClearChrFlags(0xC, 0x20)

    def lambda_2E88():
        OP_95(0xFE, 26500, 0, 25400, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_2E88)
    WaitChrThread(0xC, 1)
    Sound(812, 0, 100, 0)
    OP_6F(0x79)
    Sleep(150)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0xC,
        (
            "#11P#11232F#4Sでも……Keyaちゃんは\x01",
            "You can truly keep this as it is! Is it?\x02\x03",
            "#3SSeparate with Lloyd's\x01",
            "I was forced to do something serious … ….!\x02\x03",
            "#11227FI …\x01",
            "I think it is absolutely wrong!\x02\x03",
            "Mariavel and Dieter too!\x02\x03",
            "#11232F#40W……in addition…#500W…#40WDad too …!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#5P#12312F#30WSuzuku……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    OP_68(26500, 1000, 25400, 1000)

    def lambda_3007():
        OP_95(0xFE, 26500, 0, 26000, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_3007)
    WaitChrThread(0xB, 1)
    Sleep(300)
    Fade(500)
    OP_68(26500, 1000, 25800, 0)
    MoveCamera(41, 19, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14000, 0)
    SetMapObjFrame(0xFF, "wlight_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "toreru", 0x1, 0x1)
    SetMapObjFrame(0xFF, "back_pano", 0x1, 0x1)
    SetMapObjFrame(0xFF, "ent01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "ent02", 0x0, 0x1)
    SetCameraDistance(13000, 13000)
    Sleep(300)
    SetChrChipByIndex(0xB, 0x21)
    SetChrSubChip(0xB, 0x0)
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0xB, 0x2)
    SetChrFlags(0xB, 0x20)
    SetChrChipByIndex(0xC, 0x21)
    SetChrSubChip(0xC, 0x10)
    SetChrFlags(0xC, 0x10)
    SetChrFlags(0xC, 0x2)
    SetChrFlags(0xC, 0x20)
    OP_0D()
    Sound(898, 0, 100, 0)
    Sleep(100)
    SetChrSubChip(0xB, 0x1)
    SetChrSubChip(0xC, 0x11)
    Sleep(100)
    SetChrSubChip(0xB, 0x2)
    SetChrSubChip(0xC, 0x12)
    Sleep(100)
    SetChrSubChip(0xB, 0x3)
    SetChrSubChip(0xC, 0x13)
    Sleep(100)
    SetChrSubChip(0xB, 0x4)
    SetChrSubChip(0xC, 0x14)
    Sleep(100)
    SetChrSubChip(0xB, 0x5)
    SetChrSubChip(0xC, 0x15)
    Sleep(100)
    SetChrSubChip(0xB, 0x6)
    SetChrSubChip(0xC, 0x16)
    Sleep(500)

    ChrTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#5P#12304F#40WThank you……\x01",
            "大好きだよ、Suzuku。\x02\x03",
            "#12302FBut … It's okay.\x02\x03",
            "With all the things understood\x01",
            "Because I decided on my own … …\x02\x03",
            "#12309FSo I……?\x01",
            "Do not worry so much - ─\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(13500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_E5(0xA)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_57(0x3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_E5(0xB)
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x22, 0)
    NewScene("t6050", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_10_26BA end

    SaveToFile()

Try(main)
