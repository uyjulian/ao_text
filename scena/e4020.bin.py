from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "Princess Klaudia",       # 1
        "Secretary Lechter",      # 2
        "President Rocksmith",    # 3
        "KeA",                    # 4
        "Shizuku",                # 5
        "椅子",                   # 6
        "椅子",                   # 7
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
        "Function_3_13FE",         # 03, 3
        "Function_4_1453",         # 04, 4
        "Function_5_14A8",         # 05, 5
        "Function_6_14FD",         # 06, 6
        "Function_7_1552",         # 07, 7
        "Function_8_15A7",         # 08, 8
        "Function_9_15FC",         # 09, 9
        "Function_10_2932",        # 0A, 10
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
        "#00005F#5P(Those are...)\x02",
    )

    CloseMessageWindow()
    Jump("loc_407")

    label("loc_318")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_349")

    ChrTalk(
        0x102,
        "#00105F#5P(Those are...)\x02",
    )

    CloseMessageWindow()
    Jump("loc_407")

    label("loc_349")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_380")

    ChrTalk(
        0x103,
        "#00205F#5P(......Those are...)\x02",
    )

    CloseMessageWindow()
    Jump("loc_407")

    label("loc_380")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B1")

    ChrTalk(
        0x104,
        "#00301F#5P(What the...?)\x02",
    )

    CloseMessageWindow()
    Jump("loc_407")

    label("loc_3B1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E0")

    ChrTalk(
        0x109,
        "#10105F#5P(W-What...?)\x02",
    )

    CloseMessageWindow()
    Jump("loc_407")

    label("loc_3E0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_407")

    ChrTalk(
        0x105,
        "#10302F#5P(Eeh...?)\x02",
    )

    CloseMessageWindow()

    label("loc_407")

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
            "#5P#07004FI see...\x01",
            "Senior Lucy then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#12P#11506FYeah... It happened suddenly when\x01",
            "I was on a trip to Remiferia.\x02\x03",
            "I tried to run away\x01",
            "but she caught me.\x02\x03",
            "#11501FHow many times do you think she hit me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#07002F...Not even once.\x02\x03",
            "#07009FShe held you tightly\x01",
            "and cried...right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#12P#11501F...Yeah.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#07004FUh uh... \x01",
            "I understand how\x01",
            "senior Lucy feels.\x02\x03",
            "#07001FShe probably has no idea of\x01",
            "the kind of dangerous things\x01",
            "you do on a regular basis.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#12P#11506FMan. Women are scarily\x01",
            "perceptive every so often.\x02\x03",
            "#11510FThat's tricky.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#07004F*giggle*, you reap what you sow.\x02\x03",
            "#07008F...That really takes me back.\x02\x01",
            "#07002FI haven't seen senior Leo either. I'd love\x01",
            "to have a class reunion at some point.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#12P#11501F............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#07003F...Is there something wrong, senior?\x02\x03",
            "#07002FHere is where you would say \x01",
            ""Yeah, let's have a huuuuge \x01",
            "party in Michelam!".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#12P#11504FHa ha... You got me there.\x02\x03",
            "#11500F──I can't promise anything,\x01",
            "but I will try my very best.\x02\x03",
            "Wait without getting your hopes up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#07009FI understand. \x01",
            "I will look forward to it.\x02\x03",
            "#07002FI will take my leave here then. \x01",
            "──Excuse me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#12P#11509FOh yeah, say hi\x01",
            "to Sieg for me.\x02",
        )
    )

    CloseMessageWindow()
    OP_92(0x8, 0xFFFF379C, 0xFFFFFC18, 0x15E)
    Sleep(300)
    OP_68(-52720, 1100, -2590, 3500)
    MoveCamera(133, 18, 0, 3500)
    SetCameraDistance(13270, 3500)

    def lambda_9AD():
        OP_95(0xFE, -51300, 0, -1000, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_9AD)
    WaitChrThread(0x8, 1)
    OP_93(0x8, 0x5A, 0x1F4)
    Sound(103, 0, 100, 0)
    ClearMapObjFlags(0x1, 0x10)
    OP_71(0x1, 0x0, 0x5, 0x0, 0x0)
    OP_79(0x1)

    def lambda_9ED():
        OP_95(0xFE, -48300, 0, -1000, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_9ED)
    Sleep(1000)

    def lambda_A0A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_A0A)
    WaitChrThread(0x8, 1)
    Sound(104, 0, 100, 0)
    OP_71(0x1, 0x5, 0x0, 0x0, 0x0)
    OP_79(0x1)
    Sleep(300)

    ChrTalk(
        0x9,
        (
            "#11P#11506FOh man, she's\x01",
            "really grown up.\x02\x03",
            "#11500FShe's just how a Crown Princess should be.\x01",
            "──Don't you guys think so, too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00011F...!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10302FHu hu, we were noticed.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(-55530, 1100, -1440, 3000)
    MoveCamera(125, 21, 0, 3000)
    OP_6E(550, 3000)
    SetCameraDistance(16650, 3000)

    def lambda_B22():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_B22)
    SetChrPos(0x101, -56200, 0, 7600, 180)
    SetChrPos(0x102, -54900, 0, 7600, 180)
    SetChrPos(0x103, -55900, 0, 8700, 180)
    SetChrPos(0x104, -54600, 0, 8700, 180)
    SetChrPos(0x109, -56200, 0, 9800, 180)
    SetChrPos(0x105, -54900, 0, 9800, 180)

    def lambda_B95():
        OP_97(0x101, 0x0, 0x0, 0xFFFFE0C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_B95)
    Sleep(50)

    def lambda_BB2():
        OP_97(0x102, 0x0, 0x0, 0xFFFFE0C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_BB2)
    Sleep(50)

    def lambda_BCF():
        OP_97(0x103, 0x0, 0x0, 0xFFFFE0C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_BCF)
    Sleep(50)

    def lambda_BEC():
        OP_97(0x104, 0x0, 0x0, 0xFFFFE0C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_BEC)
    Sleep(50)

    def lambda_C09():
        OP_97(0x109, 0x0, 0x0, 0xFFFFE0C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_C09)
    Sleep(50)

    def lambda_C26():
        OP_97(0x105, 0x0, 0x0, 0xFFFFE0C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_C26)
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
            "#6P#00006F...Sorry, we\x01",
            "didn't intend\x01",
            "to eavesdrop.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103F#6PIt just sort\x01",
            "of...happened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00202FYou seemed very curious\x01",
            "about it, Miss Elie.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(
        0x102,
        "#5P#00112FT-Tio!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309F#6PWell, I'm curious too.\x02\x03",
            "#00302FYou sure are on good\x01",
            "terms with the princess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11503F#11PYeah, I was her senior at school.\x02\x03",
            "#11500FNot at Sunday School though,\x01",
            "it was at Jenis Royal Academy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10305F#6PJenis Royal Academy...\x01",
            "It's a famous high school\x01",
            "in Liberl if I recall.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#6PYes. It's certainly true that they accept\x01",
            "many students from foreign countries, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10105FThen, you studied there\x01",
            "on the Imperial dime?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11504F#11PNo, it was pocket money.\x01",
            "──Giliath Osborne's pocket money.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00013F!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11504F#11PWell then, allow me to take\x01",
            "my leave here as well.\x02\x03",
            "#11505FOh, that's right. You were summoned\x01",
            "by those old foxes, right?\x02\x03",
            "#11509FThey're both not easy to\x01",
            "deal with, so be careful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00011FAh...\x02",
    )

    CloseMessageWindow()

    def lambda_1025():

        label("loc_1025")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_1025")

    QueueWorkItem2(0x101, 2, lambda_1025)

    def lambda_1037():

        label("loc_1037")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_1037")

    QueueWorkItem2(0x102, 2, lambda_1037)

    def lambda_1049():

        label("loc_1049")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_1049")

    QueueWorkItem2(0x103, 2, lambda_1049)

    def lambda_105B():

        label("loc_105B")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_105B")

    QueueWorkItem2(0x109, 2, lambda_105B)

    def lambda_106D():

        label("loc_106D")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_106D")

    QueueWorkItem2(0x105, 2, lambda_106D)

    def lambda_107F():

        label("loc_107F")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_107F")

    QueueWorkItem2(0x104, 2, lambda_107F)

    def lambda_1091():
        OP_95(0xFE, -57100, 0, -1400, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1091)
    WaitChrThread(0x9, 1)

    def lambda_10AF():
        OP_95(0xFE, -57100, 0, 1900, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_10AF)
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

    def lambda_119B():
        OP_95(0xFE, -55500, 0, 112500, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_119B)
    WaitChrThread(0x9, 1)

    def lambda_11B9():
        OP_95(0xFE, -51500, 0, 112500, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_11B9)
    WaitChrThread(0x9, 1)

    def lambda_11D7():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFEC78, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_11D7)
    Sleep(500)

    def lambda_11F4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_11F4)
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
            "#12P#00211F...As always, he is a heap \x01",
            "of suspiciousness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F#11PSo that intelligence officer is a\x01",
            "senior of Liberl's next queen...\x02\x03",
            "#10302FHu hu, this just keeps getting better and better.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003F...In any case, it's certain\x01",
            "he acts as the "Blood and Iron\x01",
            "Chancellor"'s subordinate.\x02\x03",
            "#00001FAs for what he's really after... \x01",
            "It seems we'll need to figure that out.\x02",
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

    def Function_3_13FE(): pass

    label("Function_3_13FE")


    def lambda_1403():
        OP_96(0xFE, 0xFFFE2C08, 0x0, 0x324B0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1403)

    def lambda_141D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_141D)
    WaitChrThread(0xFE, 1)

    def lambda_1432():
        OP_95(0xFE, -122600, 0, 205400, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1432)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_3_13FE end

    def Function_4_1453(): pass

    label("Function_4_1453")


    def lambda_1458():
        OP_96(0xFE, 0xFFFE2C08, 0x0, 0x324B0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1458)

    def lambda_1472():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1472)
    WaitChrThread(0xFE, 1)

    def lambda_1487():
        OP_95(0xFE, -122600, 0, 206600, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1487)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_4_1453 end

    def Function_5_14A8(): pass

    label("Function_5_14A8")


    def lambda_14AD():
        OP_96(0xFE, 0xFFFE2C08, 0x0, 0x324B0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_14AD)

    def lambda_14C7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_14C7)
    WaitChrThread(0xFE, 1)

    def lambda_14DC():
        OP_95(0xFE, -121500, 0, 204600, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_14DC)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_5_14A8 end

    def Function_6_14FD(): pass

    label("Function_6_14FD")


    def lambda_1502():
        OP_96(0xFE, 0xFFFE2C08, 0x0, 0x324B0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1502)

    def lambda_151C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_151C)
    WaitChrThread(0xFE, 1)

    def lambda_1531():
        OP_95(0xFE, -121500, 0, 207400, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1531)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_6_14FD end

    def Function_7_1552(): pass

    label("Function_7_1552")


    def lambda_1557():
        OP_96(0xFE, 0xFFFE2C08, 0x0, 0x324B0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1557)

    def lambda_1571():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1571)
    WaitChrThread(0xFE, 1)

    def lambda_1586():
        OP_95(0xFE, -120800, 0, 205400, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1586)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_7_1552 end

    def Function_8_15A7(): pass

    label("Function_8_15A7")


    def lambda_15AC():
        OP_96(0xFE, 0xFFFE2C08, 0x0, 0x324B0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_15AC)

    def lambda_15C6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_15C6)
    WaitChrThread(0xFE, 1)

    def lambda_15DB():
        OP_95(0xFE, -120800, 0, 206600, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_15DB)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_8_15A7 end

    def Function_9_15FC(): pass

    label("Function_9_15FC")

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
            "#00003F#11P──Excuse us, Mr. President.\x02\x03",
            "#00001FThank you for inviting\x01",
            "the Support Section.\x02",
        )
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7583", 0)

    ChrTalk(
        0xA,
        (
            "#6P#07509FOh, thank you for coming.\x02\x03",
            "#07500FNo need to be reserved,\x01",
            "come on, have a seat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#11PR-Right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00104F#11PThen, we will accept your suggestion...\x02",
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
            "Wah hah ha, are\x01",
            "you surprised?\x02\x03",
            "Ah, but sorry for\x01",
            "taking up your time.\x02\x03",
            "You all must be so busy.\x02",
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
        "#6P#00011FN-No, that's not it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00102FIt's an honor to receive your invitation.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 0x1)
    Sleep(300)

    ChrTalk(
        0xA,
        (
            "#07505F#5PYou're Chairman MacDowell's\x01",
            "granddaughter, correct?\x02\x03",
            "Didn't I see you at some\x01",
            "celebration awhile back?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104FYes. I spoke with you once when I had the chance\x01",
            "to visit the Republic with my grandfather.\x02\x03",
            "#00100FIt was the year before last.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#07509F#5POh, that's right.\x02\x03",
            "#07500FSo that MacDowell's resigned the\x01",
            "mayorship and become Chairman...\x02\x03",
            "#07504FHe's passionate for his age. \x01",
            "A model statesman, if I do say so myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109F*giggle*, I'm sure grandfather would\x01",
            "be thrilled to hear that from you.\x02\x03",
            "#00108FBy the way, Mr. President──\x01",
            "What is your business with us today?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 0x0)
    Sleep(300)

    ChrTalk(
        0xA,
        (
            "#07509F#5PHa ha ha, I heard about\x01",
            "all of you from Kilika.\x02\x03",
            "#07500FThat "Schwarz Auktion" incident...\x01",
            "Wasn't it just so intense?\x02\x03",
            "#07503FFormer Chairman Hartmann\x01",
            "was just so intolerable,\x01",
            "if I do say so myself.\x02\x03",
            "#07500FI wanted to personally\x01",
            "meet the team that\x01",
            "caused his downfall.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00002FW-We're honored.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00306FWell, if pushed, I'd say\x01",
            "he just self-destructed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00208F...You are right. He was\x01",
            "finished as soon as he got\x01",
            "involved with that Cult.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#07505F#5PYes, yes, there was that Cult, too.\x02\x03",
            "#07503FThe "D∴G Cult"── They did evil throughout\x01",
            "the continent, but the greatest victim of\x01",
            "their treachery was my own country.\x02\x03",
            "#07501FI wanted to thank you also for putting a\x01",
            "stop to their activities, once and for all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00011FN-No... We just did\x01",
            "what we had to, though.\x02\x03",
            "#00004FThere were many others who contributed\x01",
            "as well. We did barely anything──\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#07509F#5PWah ha ha! Quit being so humble.\x02\x03",
            "I'm told the situation was so critical that even\x01",
            "your Guardian Force was being controlled.\x02\x03",
            "#07502FIn the middle of that, you protected a young\x01",
            "girl and faced off against the evil Cult...\x02\x03",
            "Dear me, that's no small achievement!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00012FWell... We're very honored by your words.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00103FThank you for your kind words.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#07506F#5PHonestly, if Crossbell had fallen to the Cult,\x01",
            "I'm not sure what we would've done.\x02\x03",
            "If the evil Cult had occupied IBC, international\x01",
            "trade and finance would've come to a stop...\x02\x03",
            "#07501F─If that had happened, there would've been serious\x01",
            "damage to the Republican economy, no question.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00001F...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108FThat's...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#07505F#5PHmm... That being the case,\x01",
            "I'd like to award you all\x01",
            "with medals for your service.\x02\x03",
            "#07509FOk, as soon as I get back, I'll prepare\x01",
            "something excellent for all of you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00011FN-No! Hold on a\x01",
            "minute, please.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00211FIt seems a bit strange for\x01",
            "Crossbell citizens to receive\x01",
            "a Republican award...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00306FWe already received commendation\x01",
            "from old man MacDowell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#07504F#5PWhat? There's nothing strange about it!\x02\x03",
            "#07502F──Naturally, Crossbell problems are ours \x01",
            "as well, since we're your suzerain state.\x02",
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
        "#6P#00013F......\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108F...Mr. President...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#07509F#5PHah hah hah. There's no\x01",
            "need to make such faces.\x02\x03",
            "#07502FYou received an invitation from the \x01",
            ""Blood and Iron Chancellor" as well, right?\x02\x03",
            "I wanted to talk with you all a bit more,\x01",
            "but it's about time for you to be going.\x02\x03",
            "#07504F──I'll definitely get that award for\x01",
            "you all, so please look forward to it.\x02",
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

    # Function_9_15FC end

    def Function_10_2932(): pass

    label("Function_10_2932")

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
            "#40W............\x02",
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
        "Young Girl's Voice",
        "KeA...\x02",
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
            "#12302F#5PAh, Shizuku...\x02\x03",
            "Are your eyes fine now?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_68(26500, 1000, 25480, 3000)
    SetCameraDistance(14500, 3000)

    def lambda_2CE8():
        OP_95(0xFE, 26500, 0, 24900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_2CE8)
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
            "#30WYes... I'm not dizzy anymore\x01",
            "and I can even see colors...\x02\x03",
            "Everything...\x01",
            "Is thanks to you, KeA.\x02\x03",
            "...Really, thank you.\x02",
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
            "#5P#12309FEhehe... I'm glad.\x02\x03",
            "#12302FBut Shizuku and the hospital's people\x01",
            "have always done their best, right?\x02\x03",
            "KeA just gave it\x01",
            "the final push.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#11P#11226FI see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#5P#12304FAlso, since I have this "power", it would\x01",
            "be a waste if I didn't put it at good use.\x02\x03",
            "#12314FEheheh, if I could heal your eyes,\x01",
            "it was worth becoming like this──\x02",
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
        "#11P#11232F#4S────But!\x02",
    )

    CloseMessageWindow()

    def lambda_2FC0():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_2FC0)
    WaitChrThread(0xC, 2)
    Sleep(300)

    ChrTalk(
        0xC,
        (
            "#11P#11226F#30W...I-I'm happy, you know...?\x02\x03",
            "I was uneasy to not be able to see...\x01",
            "...I became a burden for father...\x02\x03",
            "#11228FI became your friend, and yet I didn't\x01",
            "even know what face you had...!\x02\x03",
            "#11227FBeing able to see your face like this...\x01",
            "I'm so happy that I'd cry, but...!\x02",
        )
    )

    CloseMessageWindow()
    OP_68(26500, 1000, 25870, 600)
    SetChrChipByIndex(0xC, 0x1F)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x10)
    ClearChrFlags(0xC, 0x2)
    ClearChrFlags(0xC, 0x20)

    def lambda_3126():
        OP_95(0xFE, 26500, 0, 25400, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_3126)
    WaitChrThread(0xC, 1)
    Sound(812, 0, 100, 0)
    OP_6F(0x79)
    Sleep(150)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0xC,
        (
            "#11P#11232F#4SBut...KeA, are you \x01",
            "really fine with all this?\x02\x03",
            "#3SBeing apart from Mr. Lloyd and the others,\x01",
            "being made to do strange things...!\x02\x03",
            "#11227FI...I think that all this\x01",
            "is completely wrong!\x02\x03",
            "Miss Mariabell and Mr. Dieter are wrong too!\x02\x03",
            "#11232F#40W...And also...#500W...#40Wmy father too...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#5P#12312F#30WShizuku...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    OP_68(26500, 1000, 25400, 1000)

    def lambda_32C8():
        OP_95(0xFE, 26500, 0, 26000, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_32C8)
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
            "#5P#12304F#40WThank you...\x01",
            "I really love you, Shizuku.\x02\x03",
            "#12302FBut... I'm fine.\x02\x03",
            "I've decided this on my own,\x01",
            "after having understood everything...\x02\x03",
            "#12309FSo...\x01",
            "Don't be so worried about me──\x07\x00\x02",
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

    # Function_10_2932 end

    SaveToFile()

Try(main)
