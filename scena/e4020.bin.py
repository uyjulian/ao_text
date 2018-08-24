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
        "Function_3_13A0",         # 03, 3
        "Function_4_13F5",         # 04, 4
        "Function_5_144A",         # 05, 5
        "Function_6_149F",         # 06, 6
        "Function_7_14F4",         # 07, 7
        "Function_8_1549",         # 08, 8
        "Function_9_159E",         # 09, 9
        "Function_10_2856",        # 0A, 10
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
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_315")

    ChrTalk(
        0x101,
        "#00005F#5P(That's...)\x02",
    )

    CloseMessageWindow()
    Jump("loc_3F8")

    label("loc_315")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_343")

    ChrTalk(
        0x102,
        "#00105F#5P(That's...)\x02",
    )

    CloseMessageWindow()
    Jump("loc_3F8")

    label("loc_343")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_371")

    ChrTalk(
        0x103,
        "#00205F#5P(That's...)\x02",
    )

    CloseMessageWindow()
    Jump("loc_3F8")

    label("loc_371")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A2")

    ChrTalk(
        0x104,
        "#00301F#5P(What the...?)\x02",
    )

    CloseMessageWindow()
    Jump("loc_3F8")

    label("loc_3A2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D1")

    ChrTalk(
        0x109,
        "#10105F#5P(W-What...?)\x02",
    )

    CloseMessageWindow()
    Jump("loc_3F8")

    label("loc_3D1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F8")

    ChrTalk(
        0x105,
        "#10302F#5P(Huh...?)\x02",
    )

    CloseMessageWindow()

    label("loc_3F8")

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
            "#5P#07004FI see... So it was with\x01",
            "Lucy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#12P#11506FYeah... It happened\x01",
            "suddenly when I was on a\x01",
            "trip to Remiferia.\x02\x03",
            "I tried to run away but\x01",
            "she caught me.\x02\x03",
            "#11501FHow many times do you\x01",
            "think she hit me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#07002FNot even once.\x02\x03",
            "#07009FShe held you tightly and\x01",
            "cried... right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#12P#11501FYeah.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#07004FHaha... I understand how she\x01",
            "feels.\x02\x03",
            "#07001FShe probably has no idea of\x01",
            "the kinds of dangerous things\x01",
            "you do on a regular basis.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#12P#11506FMan. Women are scarily\x01",
            "perceptive every so\x01",
            "often.\x02\x03",
            "#11510FI couldn't help it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#07004FHaha, you reap what you sow.\x02\x03",
            "#07008F...That really takes me back.\x02\x01",
            "#07002FI haven't seen Leo either. I'd love\x01",
            "to have a class reunion at some point.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#12P#11501F...............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#07003F...Is there something wrong\x01",
            "with him?\x02\x03",
            "#07002FHere's where you say "Yeah,\x01",
            "let's have a huuuuge party\x01",
            "at Michelam!"\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#12P#11504FHaha... You got me\x01",
            "there.\x02\x03",
            "#11500FI can't promise\x01",
            "anything, but I will try\x01",
            "my very best.\x02\x03",
            "So don't get your hopes\x01",
            "up, and wait patiently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#07009FI understand. I'll look\x01",
            "forward to it.\x02\x03",
            "#07002FI take my leave here\x01",
            "then. Excuse me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#12P#11509FOh yeah, say hi to Sieg\x01",
            "for me.\x02",
        )
    )

    CloseMessageWindow()
    OP_92(0x8, 0xFFFF379C, 0xFFFFFC18, 0x15E)
    Sleep(300)
    OP_68(-52720, 1100, -2590, 3500)
    MoveCamera(133, 18, 0, 3500)
    SetCameraDistance(13270, 3500)

    def lambda_981():
        OP_95(0xFE, -51300, 0, -1000, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_981)
    WaitChrThread(0x8, 1)
    OP_93(0x8, 0x5A, 0x1F4)
    Sound(103, 0, 100, 0)
    ClearMapObjFlags(0x1, 0x10)
    OP_71(0x1, 0x0, 0x5, 0x0, 0x0)
    OP_79(0x1)

    def lambda_9C1():
        OP_95(0xFE, -48300, 0, -1000, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_9C1)
    Sleep(1000)

    def lambda_9DE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_9DE)
    WaitChrThread(0x8, 1)
    Sound(104, 0, 100, 0)
    OP_71(0x1, 0x5, 0x0, 0x0, 0x0)
    OP_79(0x1)
    Sleep(300)

    ChrTalk(
        0x9,
        (
            "#11P#11506FWow, she's really grown\x01",
            "up.\x02\x03",
            "#11500FShe's just how a crown\x01",
            "princess should be. ─Don't\x01",
            "you guys think so, too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00011F...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10302FHehe, you noticed us.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(-55530, 1100, -1440, 3000)
    MoveCamera(125, 21, 0, 3000)
    OP_6E(550, 3000)
    SetCameraDistance(16650, 3000)

    def lambda_AEE():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_AEE)
    SetChrPos(0x101, -56200, 0, 7600, 180)
    SetChrPos(0x102, -54900, 0, 7600, 180)
    SetChrPos(0x103, -55900, 0, 8700, 180)
    SetChrPos(0x104, -54600, 0, 8700, 180)
    SetChrPos(0x109, -56200, 0, 9800, 180)
    SetChrPos(0x105, -54900, 0, 9800, 180)

    def lambda_B61():
        OP_97(0x101, 0x0, 0x0, 0xFFFFE0C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_B61)
    Sleep(50)

    def lambda_B7E():
        OP_97(0x102, 0x0, 0x0, 0xFFFFE0C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_B7E)
    Sleep(50)

    def lambda_B9B():
        OP_97(0x103, 0x0, 0x0, 0xFFFFE0C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_B9B)
    Sleep(50)

    def lambda_BB8():
        OP_97(0x104, 0x0, 0x0, 0xFFFFE0C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_BB8)
    Sleep(50)

    def lambda_BD5():
        OP_97(0x109, 0x0, 0x0, 0xFFFFE0C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_BD5)
    Sleep(50)

    def lambda_BF2():
        OP_97(0x105, 0x0, 0x0, 0xFFFFE0C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_BF2)
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
            "#6P#00006FSorry, we didn't intend\x01",
            "to eavesdrop.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103F#6PIt just sort of...\x01",
            "happened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00202FYou seem curious about\x01",
            "it, Elie.\x02",
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
            "#00309F#6PWell I'm curious too.\x02\x03",
            "#00302FYou sure are on good\x01",
            "terms with the princess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11503F#11PYeah, I was her senior\x01",
            "at school.\x02\x03",
            "#11500FNot at Sunday School\x01",
            "though, it was at Jenis\x01",
            "Royal Academy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10305F#6PJenis Royal Academy...\x01",
            "That a famous high school\x01",
            "in Liberl if I recall.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#6PYes. It's certainly true that\x01",
            "they accept many students from\x01",
            "foreign countries, but...\x02",
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
            "─Giliath Osborne's\x01",
            "pocket money.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00013F!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11504F#11PWell then, allow me to\x01",
            "take my leave here as\x01",
            "well.\x02\x03",
            "#11505FOh, that's right. You\x01",
            "foxes got those\x01",
            "invitations, right?\x02\x03",
            "#11509FNeither is too easy to\x01",
            "deal with, so be\x01",
            "careful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00011FAh...\x02",
    )

    CloseMessageWindow()

    def lambda_FDA():

        label("loc_FDA")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_FDA")

    QueueWorkItem2(0x101, 2, lambda_FDA)

    def lambda_FEC():

        label("loc_FEC")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_FEC")

    QueueWorkItem2(0x102, 2, lambda_FEC)

    def lambda_FFE():

        label("loc_FFE")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_FFE")

    QueueWorkItem2(0x103, 2, lambda_FFE)

    def lambda_1010():

        label("loc_1010")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_1010")

    QueueWorkItem2(0x109, 2, lambda_1010)

    def lambda_1022():

        label("loc_1022")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_1022")

    QueueWorkItem2(0x105, 2, lambda_1022)

    def lambda_1034():

        label("loc_1034")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_1034")

    QueueWorkItem2(0x104, 2, lambda_1034)

    def lambda_1046():
        OP_95(0xFE, -57100, 0, -1400, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1046)
    WaitChrThread(0x9, 1)

    def lambda_1064():
        OP_95(0xFE, -57100, 0, 1900, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1064)
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

    def lambda_1150():
        OP_95(0xFE, -55500, 0, 112500, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1150)
    WaitChrThread(0x9, 1)

    def lambda_116E():
        OP_95(0xFE, -51500, 0, 112500, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_116E)
    WaitChrThread(0x9, 1)

    def lambda_118C():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFEC78, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_118C)
    Sleep(500)

    def lambda_11A9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_11A9)
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
        "#12P#00211FHe's suspicious as ever.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F#11PSo that intelligence\x01",
            "officer is an acquaintance\x01",
            "of Liberl's next queen...\x02\x03",
            "#10302FHehe, this just keeps\x01",
            "getting better and better.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003F...In any case, it's certain\x01",
            "he acts as the Blood and Iron\x01",
            "Chancellor's subordinate.\x02\x03",
            "#00001FAs for what he's really\x01",
            "after... It seems we'll need\x01",
            "to figure that out.\x02",
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

    def Function_3_13A0(): pass

    label("Function_3_13A0")


    def lambda_13A5():
        OP_96(0xFE, 0xFFFE2C08, 0x0, 0x324B0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_13A5)

    def lambda_13BF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_13BF)
    WaitChrThread(0xFE, 1)

    def lambda_13D4():
        OP_95(0xFE, -122600, 0, 205400, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_13D4)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_3_13A0 end

    def Function_4_13F5(): pass

    label("Function_4_13F5")


    def lambda_13FA():
        OP_96(0xFE, 0xFFFE2C08, 0x0, 0x324B0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_13FA)

    def lambda_1414():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1414)
    WaitChrThread(0xFE, 1)

    def lambda_1429():
        OP_95(0xFE, -122600, 0, 206600, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1429)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_4_13F5 end

    def Function_5_144A(): pass

    label("Function_5_144A")


    def lambda_144F():
        OP_96(0xFE, 0xFFFE2C08, 0x0, 0x324B0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_144F)

    def lambda_1469():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1469)
    WaitChrThread(0xFE, 1)

    def lambda_147E():
        OP_95(0xFE, -121500, 0, 204600, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_147E)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_5_144A end

    def Function_6_149F(): pass

    label("Function_6_149F")


    def lambda_14A4():
        OP_96(0xFE, 0xFFFE2C08, 0x0, 0x324B0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_14A4)

    def lambda_14BE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_14BE)
    WaitChrThread(0xFE, 1)

    def lambda_14D3():
        OP_95(0xFE, -121500, 0, 207400, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_14D3)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_6_149F end

    def Function_7_14F4(): pass

    label("Function_7_14F4")


    def lambda_14F9():
        OP_96(0xFE, 0xFFFE2C08, 0x0, 0x324B0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_14F9)

    def lambda_1513():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1513)
    WaitChrThread(0xFE, 1)

    def lambda_1528():
        OP_95(0xFE, -120800, 0, 205400, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1528)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_7_14F4 end

    def Function_8_1549(): pass

    label("Function_8_1549")


    def lambda_154E():
        OP_96(0xFE, 0xFFFE2C08, 0x0, 0x324B0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_154E)

    def lambda_1568():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1568)
    WaitChrThread(0xFE, 1)

    def lambda_157D():
        OP_95(0xFE, -120800, 0, 206600, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_157D)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_8_1549 end

    def Function_9_159E(): pass

    label("Function_9_159E")

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
            "#00003F#11P─Excuse us, Mr.\x01",
            "President.\x02\x03",
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
            "#6P#07509FOh, thank you for\x01",
            "coming.\x02\x03",
            "#07500FPlease, have a seat.\x02",
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
        "#00104F#11PThen, if you say so...\x02",
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
            "Wahaha, are you surprised?\x02\x03",
            "Ah, but sorry for taking up your\x01",
            "time.\x02\x03",
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
        (
            "#6P#00011FN-No, don't worry about\x01",
            "it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102FIt's an honor to receive\x01",
            "your invitation.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 0x1)
    Sleep(300)

    ChrTalk(
        0xA,
        (
            "#07505F#5PYou're Chairman\x01",
            "MacDowell's\x01",
            "granddaughter, correct?\x02\x03",
            "Didn't I see you at some\x01",
            "celebration a while\x01",
            "back?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104FYes. I spoke with you once when\x01",
            "I had the chance to visit the\x01",
            "Republic with my grandfather.\x02\x03",
            "#00100FIt was the year before last.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#07509F#5POh, that's right.\x02\x03",
            "#07500FSo that MacDowell's\x01",
            "resigned the mayorship\x01",
            "and become chairman...\x02\x03",
            "#07504FHe's passionate for his\x01",
            "age. A model statesman\x01",
            "if I do say so myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109FHaha, I'm sure my\x01",
            "grandfather will be thrilled\x01",
            "to hear that from you.\x02\x03",
            "#00108FBy the way Mr. President─\x01",
            "What is your business with\x01",
            "us today?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 0x0)
    Sleep(300)

    ChrTalk(
        0xA,
        (
            "#07509F#5PHahaha, I heard about all\x01",
            "of you from Kilika.\x02\x03",
            "#07500FThat Schwarz Auktion\x01",
            "incident... Wasn't it just\x01",
            "so exciting?\x02\x03",
            "#07503FPrevious Chairman Hartmann\x01",
            "was just so intolerable,\x01",
            "if I do say so myself.\x02\x03",
            "#07500FI wanted to personally\x01",
            "meet the team that caused\x01",
            "his downfall.\x02",
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
            "#12P#00306FWell if pushed, I say he\x01",
            "just self-destructed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00208F...That's right. He was\x01",
            "finished as soon as he got\x01",
            "involved with that cult.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#07505F#5PYes, yes, there was that cult, too.\x02\x03",
            "#07503FThe D∴G Cult─ They did evil throughout\x01",
            "the continent, but the greatest victim\x01",
            "of their treachery was my own country.\x02\x03",
            "#07501FI wanted to thank you also for putting\x01",
            "a stop to their activities, once and\x01",
            "for all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00011FS-Sure... We just did\x01",
            "what we had to, though.\x02\x03",
            "#00004FThere were many others\x01",
            "who contributed as well.\x01",
            "We did barely anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#07509F#5PWahaha! Quit being so humble.\x02\x03",
            "I'm told the situation was so\x01",
            "critical that even your Guardian\x01",
            "Force was being controlled.\x02\x03",
            "#07502FIn the middle of that, you\x01",
            "protected the girl and faced off\x01",
            "against the evil cult...\x02\x03",
            "That's no small achievement!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00012FYeah... We're honored.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FThank you for your kind\x01",
            "words.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#07506F#5PHonestly, if Crossbell fell to\x01",
            "the cult, I'm not sure what we'd\x01",
            "do.\x02\x03",
            "If the evil cult occupied IBC,\x01",
            "international trade and finance\x01",
            "would come to a stop...\x02\x03",
            "#07501F─If that happened, there would\x01",
            "be serious damage to the\x01",
            "Republican economy, no question.\x02",
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
            "#07509FOk, as soon as I get back,\x01",
            "I'll prepare something\x01",
            "excellent for all of you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00011FN-No! Hold on a minute,\x01",
            "please.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00211FIt seems a bit strange for\x01",
            "Crossbell citizens to\x01",
            "receive a Republican award.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00306FWe already received a\x01",
            "commendation from old\x01",
            "man MacDowell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#07504F#5PWhat? There's nothing strange\x01",
            "about it!\x02\x03",
            "#07502F─Because Crossbell is a subject\x01",
            "state, their problems are\x01",
            "naturally our problems as well.\x02",
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
            "#07509F#5PHa ha ha. There's no need to\x01",
            "make such faces.\x02\x03",
            "#07502FYou received an invitation\x01",
            "from the Blood and Iron\x01",
            "Chancellor as well, right?\x02\x03",
            "I wanted to talk with you all\x01",
            "a bit more, but it's about\x01",
            "time for you to be going.\x02\x03",
            "#07504F─I'll definitely get that\x01",
            "award for you all, so please\x01",
            "look forward to it.\x02",
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

    # Function_9_159E end

    def Function_10_2856(): pass

    label("Function_10_2856")

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
            "Are your eyes better\x01",
            "now?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_68(26500, 1000, 25480, 3000)
    SetCameraDistance(14500, 3000)

    def lambda_2C0E():
        OP_95(0xFE, 26500, 0, 24900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_2C0E)
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
            "#30WYes... I'm not dizzy anymore and I\x01",
            "can even see colors...\x02\x03",
            "Everything... is thanks to you,\x01",
            "KeA.\x02\x03",
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
            "#12302FBut you and the hospital\x01",
            "staff have been doing their\x01",
            "best this whole time, right?\x02\x03",
            "KeA just gave it the final\x01",
            "push.\x07\x00\x02",
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
            "#5P#12304FAlso, since I have this\x01",
            ""power", it would be a waste if\x01",
            "I didn't put it to good use.\x02\x03",
            "#12314FEhehe. If I could heal your\x01",
            "eyes, it was worth becoming\x01",
            "like this─\x02",
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
        "#11P#11232F#4S──But!\x02",
    )

    CloseMessageWindow()

    def lambda_2EE7():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_2EE7)
    WaitChrThread(0xC, 2)
    Sleep(300)

    ChrTalk(
        0xC,
        (
            "#11P#11226F#30W...I-I'm happy, you\x01",
            "know...?\x02\x03",
            "It was anxious not being\x01",
            "able to see... ...I was a\x01",
            "burden on father...\x02\x03",
            "#11228FI became your friend, and\x01",
            "yet I didn't even know\x01",
            "your face...!\x02\x03",
            "#11227FBeing able to see your\x01",
            "face like this... I'm so\x01",
            "happy I could cry, but...!\x02",
        )
    )

    CloseMessageWindow()
    OP_68(26500, 1000, 25870, 600)
    SetChrChipByIndex(0xC, 0x1F)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x10)
    ClearChrFlags(0xC, 0x2)
    ClearChrFlags(0xC, 0x20)

    def lambda_3042():
        OP_95(0xFE, 26500, 0, 25400, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_3042)
    WaitChrThread(0xC, 1)
    Sound(812, 0, 100, 0)
    OP_6F(0x79)
    Sleep(150)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0xC,
        (
            "#11P#11232F#4SBut... KeA, are you really\x01",
            "fine with all this?\x02\x03",
            "#3SBeing apart from Lloyd and\x01",
            "the others, being made to\x01",
            "do strange things...!\x02\x03",
            "#11227FI...I think that all this\x01",
            "is completely wrong!\x02\x03",
            "Miss Mariabell and Mr.\x01",
            "Dieter are wrong too!\x02\x03",
            "#11232F#40W...And also...#500W...#40W\x01",
            "My father too...!\x02",
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

    def lambda_31E1():
        OP_95(0xFE, 26500, 0, 26000, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_31E1)
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
            "#5P#12304F#40WThank you... I really\x01",
            "love you, Shizuku.\x02\x03",
            "#12302FBut... I'm fine.\x02\x03",
            "I've decided this on my\x01",
            "own, after understanding\x01",
            "everything...\x02\x03",
            "#12309FSo... Don't be so\x01",
            "worried about me─\x07\x00\x02",
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

    # Function_10_2856 end

    SaveToFile()

Try(main)
