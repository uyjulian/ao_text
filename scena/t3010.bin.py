from ScenarioHelper import *

def main():
    CreateScenaFile(
        "t3010.bin",                # FileName
        "t3010",                    # MapName
        "t3010",                    # Location
        0x005B,                     # MapIndex
        "ed7000",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x1E,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 91, 0, 0, 0, 1],
    )

    BuildStringList((
        "t3010",                  # 0
        "Guide doll",               # 1
        "Jorgg Aged",             # 2
        "Pate Mate",               # 3
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(332, 0)                                        # 0

    ScpFunction((
        "Function_0_14C",          # 00, 0
        "Function_1_17A",          # 01, 1
        "Function_2_1AA",          # 02, 2
        "Function_3_2EC8",         # 03, 3
        "Function_4_2F07",         # 04, 4
        "Function_5_2F6A",         # 05, 5
        "Function_6_2FF7",         # 06, 6
        "Function_7_3083",         # 07, 7
        "Function_8_30CD",         # 08, 8
        "Function_9_3107",         # 09, 9
        "Function_10_3147",        # 0A, 10
        "Function_11_3191",        # 0B, 11
        "Function_12_31CB",        # 0C, 12
        "Function_13_320B",        # 0D, 13
        "Function_14_3255",        # 0E, 14
        "Function_15_328F",        # 0F, 15
        "Function_16_32CF",        # 10, 16
        "Function_17_3319",        # 11, 17
        "Function_18_3353",        # 12, 18
        "Function_19_3393",        # 13, 19
        "Function_20_33DD",        # 14, 20
        "Function_21_3417",        # 15, 21
        "Function_22_3457",        # 16, 22
        "Function_23_34A1",        # 17, 23
        "Function_24_34DB",        # 18, 24
    ))


    def Function_0_14C(): pass

    label("Function_0_14C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_165")
    SetScenarioFlags(0x0, 4)
    Event(0, 2)
    Jump("loc_179")

    label("loc_165")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_179")
    SetScenarioFlags(0x0, 5)
    Event(0, 24)

    label("loc_179")

    Return()

    # Function_0_14C end

    def Function_1_17A(): pass

    label("Function_1_17A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_194")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0xCA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 4)
    Jump("loc_1A9")

    label("loc_194")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_1A9")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0xFB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 5)

    label("loc_1A9")

    Return()

    # Function_1_17A end

    def Function_2_1AA(): pass

    label("Function_2_1AA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch06600.itc", 0x1E)
    LoadChrToIndex("chr/ch47400.itc", 0x1F)
    SoundLoad(957)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis256.itp")
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrChipByIndex(0x9, 0x1E)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrChipByIndex(0x8, 0x1F)
    OP_52(0x8, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x226), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x226), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x226), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xA, 0x80)
    OP_78(0x1, 0xA)
    OP_49()
    OP_74(0x1, 0xF)
    OP_70(0x1, 0x65)
    SetChrPos(0xA, 8730, 250, 0, 270)
    OP_D5(0xA, 0x0, 0x41EB0, 0x0, 0x0)
    ClearMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x4, 0x1000)
    SetChrPos(0x101, 0, 0, 87500, 0)
    SetChrPos(0x102, 500, 0, 87000, 0)
    SetChrPos(0x103, -750, 0, 86000, 0)
    SetChrPos(0x104, 0, 0, 85500, 0)
    SetChrPos(0x109, 750, 0, 84750, 0)
    SetChrPos(0x105, 1250, 0, 86000, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x8, 0, 0, 90000, 0)
    OP_68(0, 600, 88000, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20000, 0)
    BeginChrThread(0x8, 1, 0, 3)
    Sleep(50)
    BeginChrThread(0x101, 1, 0, 6)
    Sleep(30)
    BeginChrThread(0x102, 1, 0, 9)
    Sleep(50)
    BeginChrThread(0x103, 1, 0, 12)
    Sleep(50)
    BeginChrThread(0x104, 1, 0, 15)
    Sleep(50)
    BeginChrThread(0x105, 1, 0, 21)
    Sleep(50)
    BeginChrThread(0x109, 1, 0, 18)
    Sound(957, 2, 40, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(14000)
    StopSound(957, 1000, 30)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Thus, Lloyd's\x01",
            "Guided by the guide doll's automatic doll … ….\x02\x03",
            "It's complicated like a labyrinth\x01",
            "It was guided to a corner of the underground studio.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EndChrThread(0x8, 0x1)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x105, 0x1)
    EndChrThread(0x109, 0x1)
    SetChrPos(0x101, 0, 0, 7000, 180)
    SetChrPos(0x102, 250, 0, 7000, 180)
    SetChrPos(0x103, -250, 0, 7000, 180)
    SetChrPos(0x104, 0, 0, 7000, 180)
    SetChrPos(0x109, 250, 0, 7000, 180)
    SetChrPos(0x105, -500, 0, 7000, 180)
    SetChrPos(0x8, 0, 0, 7000, 180)
    SetChrPos(0x9, -2000, 0, -4700, 180)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    PlayBGM("ed7304", 0)
    OP_68(0, 600, 7000, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20000, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(107, 0, 100, 0)
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x0)
    OP_68(0, 600, 4000, 4000)
    BeginChrThread(0x8, 1, 0, 4)
    Sleep(3000)
    BeginChrThread(0x101, 1, 0, 7)
    Sleep(500)
    BeginChrThread(0x103, 1, 0, 13)
    Sleep(500)
    BeginChrThread(0x102, 1, 0, 10)
    Sleep(500)
    BeginChrThread(0x104, 1, 0, 16)
    Sleep(500)
    BeginChrThread(0x105, 1, 0, 22)
    Sleep(500)
    BeginChrThread(0x109, 1, 0, 19)
    Sleep(1000)
    Sound(107, 0, 100, 0)
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0xA, 0x0, 0x0, 0x0)
    OP_79(0x0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    EndChrThread(0x101, 0x1)

    def lambda_65D():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_65D)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)

    def lambda_672():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_672)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x105, 0x1)
    EndChrThread(0x109, 0x1)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x103, 2)

    ChrTalk(
        0x101,
        "#00013F#5PHere, here …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00205F#5P… … It is amazing …\x02",
    )

    CloseMessageWindow()
    Fade(500)
    BeginChrThread(0x9, 1, 0, 5)
    OP_68(-2000, 600, -4700, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20000, 0)
    OP_68(4250, 1000, 2300, 10000)
    MoveCamera(75, 15, 0, 10000)
    OP_6E(500, 10000)
    SetCameraDistance(28000, 10000)
    PlaceName2(340, 200, "c_plac16", 0x0, 3000)
    OP_0D()
    OP_6F(0x79)

    def lambda_74C():
        OP_93(0x101, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_74C)
    Sleep(50)

    def lambda_75C():
        OP_93(0x102, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_75C)
    Sleep(50)

    def lambda_76C():
        OP_93(0x103, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_76C)
    Sleep(50)

    def lambda_77C():
        OP_93(0x104, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_77C)
    Sleep(50)

    def lambda_78C():
        OP_93(0x109, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_78C)
    Sleep(50)

    def lambda_79C():
        OP_93(0x105, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_79C)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x109,
        "#10111F#6P#4SWhat? Is it?\x02",
    )

    CloseMessageWindow()
    OP_68(8730, 4000, 0, 3000)
    MoveCamera(72, 20, 0, 3000)
    SetCameraDistance(20000, 3000)
    OP_6F(0x79)
    Sleep(300)

    ChrTalk(
        0x105,
        (
            "#10301F#6P#NPossibly …\x01",
            "Are you the huge doll that you said?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00006F#6P#NAh……\x01",
            "Len was using it\x01",
            "\"Patel = Mattel\" But …\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        "#00108F#6P#NYou kept it here …\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#00306F#6P#NBut no, in the basement of this mansion\x01",
            "It is said that there was such a place ……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(4250, 1000, 2300, 0)
    MoveCamera(75, 15, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(28000, 0)
    OP_0D()
    OP_93(0x103, 0x13B, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            "#00208F#11PWhat mind guiding the net\x01",
            "There are also things that look like terminals … ….\x02\x03",
            "#00201F…… No way No kitten is from here\x01",
            "Intervening wirelessly on the net … ….?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x9,
        "Voice of an old man",
        "── So, what is it for?\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_ABF():
        TurnDirection(0x101, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_ABF)
    Sleep(50)

    def lambda_ACF():
        TurnDirection(0x102, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_ACF)
    Sleep(50)

    def lambda_ADF():
        TurnDirection(0x103, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_ADF)
    Sleep(50)

    def lambda_AEF():
        TurnDirection(0x104, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_AEF)
    Sleep(50)

    def lambda_AFF():
        TurnDirection(0x109, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_AFF)
    Sleep(50)

    def lambda_B0F():
        TurnDirection(0x105, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_B0F)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    OP_68(-6000, 700, -650, 5000)
    MoveCamera(23, 17, 0, 5000)
    OP_6E(500, 5000)
    SetCameraDistance(20580, 5000)
    BeginChrThread(0x101, 1, 0, 8)
    BeginChrThread(0x103, 1, 0, 14)
    BeginChrThread(0x102, 1, 0, 11)
    BeginChrThread(0x104, 1, 0, 17)
    BeginChrThread(0x109, 1, 0, 20)
    BeginChrThread(0x105, 1, 0, 23)
    OP_6F(0x79)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x105, 1)
    WaitChrThread(0x109, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 4)), scpexpr(EXPR_END)), "loc_C29")

    ChrTalk(
        0x101,
        (
            "#00003F#5PThat……\x01",
            "Take your time\x01",
            "Thank you very much.\x02\x03",
            "#00001FActually, some of you\x01",
            "There was something I wanted to ask.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D04")

    label("loc_C29")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x30, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_CA1")

    ChrTalk(
        0x101,
        (
            "#00003F#5PThat……\x01",
            "It is long time no see.\x02\x03",
            "#00001FActually, some of you\x01",
            "There was something I wanted to ask.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D04")

    label("loc_CA1")


    ChrTalk(
        0x101,
        (
            "#00006F#5PThat……\x01",
            "Hello nice to meet.\x02\x03",
            "#00001FActually, some of you\x01",
            "There was something I wanted to ask.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D04")


    ChrTalk(
        0x9,
        (
            "#03903F#12PHun …\x02\x03",
            "#03900FOita, Campanella\x01",
            "Is it a place that I sprinkled a bit?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00013F#5P……!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00301F#5PGrandfather, you ….\x02",
    )

    CloseMessageWindow()
    OP_93(0x9, 0x1E, 0x1F4)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x30, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_EEB")

    ChrTalk(
        0x9,
        (
            "#03903F#6PDo not make a difference.\x02\x03",
            "#03900FCertainly it is an official of \"association\"\x01",
            "It is nothing but a puppeteer to the last.\x02\x03",
            "To the plan of \"association\" itself\x01",
            "It is not directly related.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FA9")

    label("loc_EEB")


    ChrTalk(
        0x9,
        (
            "#03903F#6PDo not make a difference.\x02\x03",
            "#03900FAs I heard from Len\x01",
            "Certainly it is an official of \"association\"\x01",
            "It is nothing but a puppeteer to the last.\x02\x03",
            "To the plan of \"association\" itself\x01",
            "It is not directly related.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FA9")


    ChrTalk(
        0x101,
        (
            "#00006F#5PWell then, then …\x02\x03",
            "#00001FThat boy named Campanella\x01",
            "What are you trying to do?\x01",
            "If you do not know ……?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#03900F#6PI do not know and I am in no position to know.\x02\x03",
            "#03903FHowever……\x01",
            "He is not an \"apostle\" but an \"enforcer\".\x02\x03",
            "Actually \"association\" is about to proceed\x01",
            "It is not in the position to propose \"plan\".\x02\x03",
            "#03901FIt is planning and planning it\x01",
            "To the end it means \"an apostle\".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00101F#11PWait a minute ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F#11PSomething is going on too fast\x01",
            "Understanding can not catch up ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10305F#11PIt looks like important internal information\x01",
            "Can I speak easily?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#03903F#6PGiggle\x01",
            "It is not forbidden separately.\x02\x03",
            "#03900FAnd, if this degree of information\x01",
            "Those who know it will be as it is.\x02\x03",
            "If it is a church, a guild, an intelligence agency of a great country\x01",
            "I should have grabbed it a long time ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F#5P…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00201F#5PNevertheless, you are here\x01",
            "I can keep making dolls ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#03903F#6PIn the first place, the whole picture of \"association\"\x01",
            "I do not have a position to know.\x02\x03",
            "#03900FFor example, puppet weapons#8ROvermuppet#Even\x01",
            "From the technology of several studio other than here\x01",
            "It is an established substitute.\x02\x03",
            "In other words, there are countless numbers here\x01",
            "One of the tails of a huge \"snake\" ……\x02\x03",
            "#03903FGuild and church per area\x01",
            "It is not easy to get in\x01",
            "I guess there are reasons for that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#5PI see……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F#5PJust to caution\x01",
            "Extract information as necessary …\x02\x03",
            "#00300FIs that person more useful?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#03903F#6PYes, in addition to that\x01",
            "This workshop also has \"preparation\".\x02\x03",
            "#03901FIf you take an arrest warrant\x01",
            "When stepping on here …\x02\x03",
            "Probably you can discover\x01",
            "It is probably just a studio of grapes.\x02\x03",
            "That \"Patel = Mattel\" is also included.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0x109)
    OP_64(0x105)

    ChrTalk(
        0x9,
        (
            "#03903F#6PHuff, what if now on this occasion\x01",
            "Do you try to detain me?\x02\x03",
            "#03900FIt might be a unique occasion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#5P─ ─ No, I will hold back.\x02\x03",
            "#00001FCertainly from you ……\x01",
            "It seems better to just ask a story.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108F#11P…… Lloyd ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FChi#11PA little\x01",
            "I can not convince you ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#03903F#6PHehe, you're wise.\x02\x03",
            "#03900FApparently variously\x01",
            "There seems to be something I want to hear … …\x02\x03",
            "Let's narrow down to three.\x01",
            "Let's answer if it can be answered.\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xBB8)

    ChrTalk(
        0x101,
        (
            "#00003F#5P……I understand.\x02\x03",
            "#00008F(Things I want to hear from this old man,\x01",
            "that is……)\x02",
        )
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7580", 0)
    SetCameraDistance(18000, 120000)
    ClearScenarioFlags(0x0, 3)
    ClearScenarioFlags(0x0, 0)
    ClearScenarioFlags(0x0, 1)
    ClearScenarioFlags(0x0, 2)

    label("loc_1842")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B33")
    FadeToDark(300, 0, 100)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_18E0")

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【About the \"apostles\" of the association】\x01",        # 0
            "【About the plan of the association】\x01",        # 1
            "【About relationship between association and cult】\x01",      # 2
            "【Quit question】\x01",                  # 3
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Jump("loc_1942")

    label("loc_18E0")


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【About the \"apostles\" of the association】\x01",        # 0
            "【About the plan of the association】\x01",        # 1
            "【About relationship between association and cult】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)

    label("loc_1942")

    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_196E"),
        (0, "loc_1D0F"),
        (2, "loc_2698"),
        (3, "loc_2B26"),
        (SWITCH_DEFAULT, "loc_2B2E"),
    )


    label("loc_196E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C84")

    ChrTalk(
        0x9,
        (
            "#03903F#6PAs I said earlier\x01",
            "I do not know the details either.\x02\x03",
            "However, according to the stories heard\x01",
            "It seems that it is called like this.\x02\x03",
            "#03901F─ ─ \"Phantomhurst#4RNuclear power plant#Plan \".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#5P\"Phantomhurgh#4RNuclear power plant#plan\"……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10301F#11P… … It's a meaningful name ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101F#11P… … The plan is …\x01",
            "An incident like Libert one year ago\x01",
            "What brings to Crossbell?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10107F#11PWell, if so … …\x01",
            "Absolutely not recognized!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#03903F#6PAgain, I do not know the details.\x02\x03",
            "#03900FHowever, if I could say one thing\x01",
            "Intervention of \"association\" as Ribeel\x01",
            "It is not large scale.\x02\x03",
            "Originally \"association\" is the existence of darkness ……\x01",
            "Originally it will not come out much to the front stage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00101F#11P…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#5PSomehow,\x01",
            "I do not feel at ease at all … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00211F#5PRather, only name\x01",
            "On the contrary it seems to fuel anxiety … …\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1D0A")

    label("loc_1C84")


    ChrTalk(
        0x9,
        (
            "#03903F#6PI do not know the outline either.\x02\x03",
            "However, according to the stories heard\x01",
            "It seems that it is called like this.\x02\x03",
            "#03901F─ ─ \"Phantomhurst#4RNuclear power plant#Plan \".\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D0A")

    Jump("loc_2B2E")

    label("loc_1D0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2560")
    Sleep(150)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(500)
    SetMessageWindowPos(280, 170, -1, -1)

    AnonymousTalk(
        0x9,
        (
            "#3C#30W\"The Apostle of the Snake#8RAnxious#\"──\x02\x03",
            "A great \"lord\"#4RMaster#\"Received the intention of,\x01",
            "It is about seven executives who realize the plan.\x02\x03",
            "About all of us also\x01",
            "Although I do not know in detail … …\x02\x03",
            "I will visit this crossbell soon\x01",
            "The apostles do not know.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00013F#5PWell, that is ……\x01",
            "Who the hell are you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#03900F#6P……………………………………\x02\x03",
            "#03903FOne person made \"the sixth pillar\"\x01",
            "It is a technology network of the association\x01",
            "He is the man who oversees the \"Thirteen Studio\".\x02\x03",
            "Let's be a theorist of association\x01",
            "A greedy engineer#6REngineer#… ….\x02\x03",
            "#03901FWell, just as a bad guy\x01",
            "I will tell you.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x103,
        "#00206F#5P…… Even though it is said like that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10101F#11PHow are you wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#03903F#6PBetter or bad, I want my intellectual curiosity\x01",
            "It is a man who only considers it.\x02\x03",
            "For what purpose this land\x01",
            "I do not know if I am going to visit … …\x02\x03",
            "#03901FFor at least Crossbell\x01",
            "It is hard to say that it is a good precursor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108F#11P……………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#5P…… Certainly as long as I heard,\x01",
            "There seems to be bad tatashi.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#03903F#6P… … And another one ……\x02\x03",
            "#03900F\"steel#2RGlasses#\"The seventh pillar\" bearing the name of\x01",
            "There is information that it goes into the crossbell.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005F#5P\"steel#2RGlasses#\"……?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301F#5PWhat is it?\x01",
            "It sounds like a bit of a jerk?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#03903F#6PHuh … … a little mysterious person.\x02\x03",
            "#03900FIf one could say it\x01",
            "Even if you all challenge by becoming a bunch\x01",
            "Is not it like an enemy master?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x32, 0x0, 0x7D0, 0xC8)

    ChrTalk(
        0x101,
        "#00011F#5PEven we all …! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#11POh\x01",
            "I'm pretty confident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#03903F#6PWell, remember the advice.\x02\x03",
            "Unlike the \"sixth pillar\"\x01",
            "I heard that he is a noble character … …\x02\x03",
            "#03901FIf you challenge you badly\x01",
            "It will definitely get caught back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00013F#5P…………………….\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2693")

    label("loc_2560")


    ChrTalk(
        0x9,
        (
            "#03903F#6PI do not know the details, but to crossbell\x01",
            "There are two \"apostles\" who are said to come.\x02\x03",
            "#03900FOne person is \"the sixth pillar\" -\x01",
            "I am supervising \"The Thirteen Studio\"\x01",
            "Bad technical person#6REngineer#It is.\x02\x03",
            "And one person is \"the seventh pillar\" ──\x01",
            "\"steel#2RGlasses#\"It is the strongest user with the name of.\x02\x03",
            "#03903FWell, neither of you\x01",
            "It will not be a handsy opponent.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2693")

    Jump("loc_2B2E")

    label("loc_2698")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A23")

    ChrTalk(
        0x9,
        (
            "#03903F#6P\"D∴G Church\"?\x02\x03",
            "#03901FAs far as I know, direct ties are\x01",
            "It seems there has never been.\x02\x03",
            "The bases of the people who had Ren#4RLodge#To\x01",
            "Although there was the fact that \"society\" was destroyed … …\x02",
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
    OP_82(0x32, 0x0, 0x7D0, 0xC8)

    ChrTalk(
        0x101,
        "#00011F#5PWell ……! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00101F#11PThat \"paradise\" … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#03900F#6PWell, powerful people from all over the world\x01",
            "It seems that it was a place to capture.\x02\x03",
            "Oita, \"Society\" breathed a breath\x01",
            "Because it targeted influential people,\x01",
            "It probably became the object of annihilation.\x02\x03",
            "#03903FLen survived\x01",
            "Honor#4RCompetition#There is no other way than to say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00208F#5P……………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#5PBut even though \"association\" is said\x01",
            "I do not think it is very much Matumo … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10301F#11PTo be honest, just such an explanation\x01",
            "I do not seem to be convinced, though?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#03903F#6PHuh, I guess.\x01",
            "To the best of my knowledge.\x02\x03",
            "#03900FHow you judge depends on you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2B21")

    label("loc_2A23")


    ChrTalk(
        0x9,
        (
            "#03903F#6P\"D∴G Church\" ──\x01",
            "As far as I know, \"association\" and direct\x01",
            "It seems there has never been a connection.\x02\x03",
            "#03900FThe bases of the people who had Ren#4RLodge#To\x01",
            "Although there was the fact that \"society\" was destroyed … …\x02\x03",
            "\"Society\" breathed a breath\x01",
            "Because the influential people were handed\x01",
            "It was just an object of annihilation.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B21")

    Jump("loc_2B2E")

    label("loc_2B26")

    SetScenarioFlags(0x0, 3)
    Jump("loc_2B2E")

    label("loc_2B2E")

    Jump("loc_1842")

    label("loc_2B33")


    ChrTalk(
        0x9,
        (
            "#03900F#6PHmm, this is three?\x02\x03",
            "#03903F─ ─ It took time.\x01",
            "I should hope for taking over soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00013F#5PWell …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00107F#11PBut,\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10108F#11PRo, Mr. Lloyd ……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00006F#5PIt is such a promise.\x01",
            "Let's raise it this time this time.\x02\x03",
            "#00000FAlso, if you have the opportunity\x01",
            "Do you mind if I come and talk?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#03903F#6PWell, I should be careful.\x02\x03",
            "#03901FInitially, for you\x01",
            "We do not care alone.\x02\x03",
            "Before the \"national independence\" and before,\x01",
            "The power that we have to watch out for is\x01",
            "Is not there any other thing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00011F#5PWell, that is ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00303F#5P… Well, certainly.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#11PMovement of such power\x01",
            "I heard that they all know, is not it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#03903F#6PHuh, Alright.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TurnDirection(0x8, 0x9, 500)
    OP_68(-6150, 700, -850, 1500)
    MoveCamera(25, 25, 0, 1500)
    OP_6E(500, 1500)
    SetCameraDistance(19000, 1500)
    Sound(957, 2, 40, 0)
    OP_95(0x8, -3750, 0, 4000, 2000, 0x0)
    StopSound(957, 300, 30)
    OP_6F(0x79)

    ChrTalk(
        0x9,
        (
            "#03900F#6P── Come on, return home\x01",
            "You should follow that child.\x02\x03",
            "When it gets stranded\x01",
            "You guarantee your safety?\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(19500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_CC(0x1, 0xFF, 0x0)
    OP_24(0x3BD)
    SetScenarioFlags(0x22, 0)
    NewScene("t3000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_2_1AA end

    def Function_3_2EC8(): pass

    label("Function_3_2EC8")

    OP_95(0xFE, 0, 0, 102000, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    StopSound(957, 300, 30)
    Sleep(1000)
    Sound(957, 2, 40, 0)
    OP_95(0xFE, -21450, 0, 102000, 2000, 0x0)
    Return()

    # Function_3_2EC8 end

    def Function_4_2F07(): pass

    label("Function_4_2F07")

    Sound(957, 2, 40, 0)

    def lambda_2F12():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_2F12)
    OP_95(0xFE, 0, 0, 5000, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    StopSound(957, 300, 30)
    Sleep(1000)
    Sound(957, 2, 40, 0)
    OP_95(0xFE, -2750, 0, 6300, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    StopSound(957, 300, 30)
    Return()

    # Function_4_2F07 end

    def Function_5_2F6A(): pass

    label("Function_5_2F6A")

    Sleep(1000)
    OP_95(0xFE, 500, 0, -4700, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(1000)
    OP_95(0xFE, -2000, 0, -4700, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(1000)
    OP_95(0xFE, -3450, 0, -500, 2000, 0x0)
    ClearChrFlags(0xFE, 0x4)
    OP_95(0xFE, -7500, -250, -500, 2000, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_95(0xFE, -7500, -250, -3350, 2000, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_5_2F6A end

    def Function_6_2FF7(): pass

    label("Function_6_2FF7")

    OP_68(0, 600, 101000, 7000)
    SetCameraDistance(22000, 7000)
    OP_95(0xFE, 0, 0, 100000, 2000, 0x0)

    def lambda_302A():

        label("loc_302A")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_302A")

    QueueWorkItem2(0xFE, 2, lambda_302A)
    Sleep(2000)
    EndChrThread(0xFE, 0x2)
    OP_68(-10000, 600, 102000, 8000)
    MoveCamera(40, 20, 0, 8000)
    OP_95(0xFE, -2000, 0, 102000, 2000, 0x0)
    OP_95(0xFE, -21450, 0, 102000, 2000, 0x0)
    Return()

    # Function_6_2FF7 end

    def Function_7_3083(): pass

    label("Function_7_3083")


    def lambda_3088():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3088)
    OP_95(0xFE, 0, 0, 2500, 2000, 0x0)

    label("loc_30A8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_30CC")
    OP_93(0xFE, 0x87, 0x1F4)
    Sleep(1500)
    OP_93(0xFE, 0xE1, 0x1F4)
    Sleep(1500)
    Jump("loc_30A8")

    label("loc_30CC")

    Return()

    # Function_7_3083 end

    def Function_8_30CD(): pass

    label("Function_8_30CD")

    TurnDirection(0xFE, 0x9, 500)
    Sleep(100)
    OP_95(0xFE, -3450, 0, -500, 2000, 0x0)
    OP_95(0xFE, -6500, -250, -1500, 2000, 0x0)
    OP_93(0xFE, 0xD2, 0x1F4)
    Return()

    # Function_8_30CD end

    def Function_9_3107(): pass

    label("Function_9_3107")

    OP_95(0xFE, 500, 0, 99500, 2000, 0x0)
    Sleep(2000)
    OP_95(0xFE, -2000, 0, 102500, 2000, 0x0)
    OP_95(0xFE, -21450, 0, 102500, 2000, 0x0)
    Return()

    # Function_9_3107 end

    def Function_10_3147(): pass

    label("Function_10_3147")


    def lambda_314C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_314C)
    OP_95(0xFE, 750, 0, 3500, 2000, 0x0)

    label("loc_316C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3190")
    OP_93(0xFE, 0x87, 0x1F4)
    Sleep(1500)
    OP_93(0xFE, 0x5A, 0x1F4)
    Sleep(1500)
    Jump("loc_316C")

    label("loc_3190")

    Return()

    # Function_10_3147 end

    def Function_11_3191(): pass

    label("Function_11_3191")

    TurnDirection(0xFE, 0x9, 500)
    Sleep(200)
    OP_95(0xFE, -3450, 0, -1000, 2000, 0x0)
    OP_95(0xFE, -5500, -250, -1150, 2000, 0x0)
    OP_93(0xFE, 0xD2, 0x1F4)
    Return()

    # Function_11_3191 end

    def Function_12_31CB(): pass

    label("Function_12_31CB")

    OP_95(0xFE, -750, 0, 99000, 2000, 0x0)
    Sleep(2100)
    OP_95(0xFE, -2000, 0, 101250, 2000, 0x0)
    OP_95(0xFE, -21450, 0, 101250, 2000, 0x0)
    Return()

    # Function_12_31CB end

    def Function_13_320B(): pass

    label("Function_13_320B")


    def lambda_3210():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3210)
    OP_95(0xFE, -1000, 0, 3000, 2000, 0x0)

    label("loc_3230")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3254")
    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(1500)
    OP_93(0xFE, 0xE1, 0x1F4)
    Sleep(1500)
    Jump("loc_3230")

    label("loc_3254")

    Return()

    # Function_13_320B end

    def Function_14_3255(): pass

    label("Function_14_3255")

    TurnDirection(0xFE, 0x9, 500)
    Sleep(500)
    OP_95(0xFE, -3450, 0, 500, 2000, 0x0)
    OP_95(0xFE, -6650, -250, -300, 2000, 0x0)
    OP_93(0xFE, 0xD2, 0x1F4)
    Return()

    # Function_14_3255 end

    def Function_15_328F(): pass

    label("Function_15_328F")

    OP_95(0xFE, 0, 0, 98000, 2000, 0x0)
    Sleep(2000)
    OP_95(0xFE, -2000, 0, 102000, 2000, 0x0)
    OP_95(0xFE, -21450, 0, 102000, 2000, 0x0)
    Return()

    # Function_15_328F end

    def Function_16_32CF(): pass

    label("Function_16_32CF")


    def lambda_32D4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_32D4)
    OP_95(0xFE, -250, 0, 4000, 2000, 0x0)

    label("loc_32F4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3318")
    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(1500)
    OP_93(0xFE, 0x5A, 0x1F4)
    Sleep(1500)
    Jump("loc_32F4")

    label("loc_3318")

    Return()

    # Function_16_32CF end

    def Function_17_3319(): pass

    label("Function_17_3319")

    TurnDirection(0xFE, 0x9, 500)
    Sleep(400)
    OP_95(0xFE, -3450, 0, -500, 2000, 0x0)
    OP_95(0xFE, -5450, -250, 300, 2000, 0x0)
    OP_93(0xFE, 0xD2, 0x1F4)
    Return()

    # Function_17_3319 end

    def Function_18_3353(): pass

    label("Function_18_3353")

    OP_95(0xFE, 750, 0, 97250, 2000, 0x0)
    Sleep(2100)
    OP_95(0xFE, -2000, 0, 102250, 2000, 0x0)
    OP_95(0xFE, -21450, 0, 102250, 2000, 0x0)
    Return()

    # Function_18_3353 end

    def Function_19_3393(): pass

    label("Function_19_3393")


    def lambda_3398():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3398)
    OP_95(0xFE, 500, 0, 5500, 2000, 0x0)

    label("loc_33B8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_33DC")
    OP_93(0xFE, 0x87, 0x1F4)
    Sleep(1500)
    OP_93(0xFE, 0xE1, 0x1F4)
    Sleep(1500)
    Jump("loc_33B8")

    label("loc_33DC")

    Return()

    # Function_19_3393 end

    def Function_20_33DD(): pass

    label("Function_20_33DD")

    TurnDirection(0xFE, 0x9, 500)
    Sleep(500)
    OP_95(0xFE, -3450, 0, -1000, 2000, 0x0)
    OP_95(0xFE, -4250, 0, -850, 2000, 0x0)
    OP_93(0xFE, 0xD2, 0x1F4)
    Return()

    # Function_20_33DD end

    def Function_21_3417(): pass

    label("Function_21_3417")

    OP_95(0xFE, 1250, 0, 98500, 2000, 0x0)
    Sleep(2000)
    OP_95(0xFE, -2000, 0, 102750, 2000, 0x0)
    OP_95(0xFE, -21450, 0, 102750, 2000, 0x0)
    Return()

    # Function_21_3417 end

    def Function_22_3457(): pass

    label("Function_22_3457")


    def lambda_345C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_345C)
    OP_95(0xFE, -1000, 0, 4500, 2000, 0x0)

    label("loc_347C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_34A0")
    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(1500)
    OP_93(0xFE, 0x13B, 0x1F4)
    Sleep(1500)
    Jump("loc_347C")

    label("loc_34A0")

    Return()

    # Function_22_3457 end

    def Function_23_34A1(): pass

    label("Function_23_34A1")

    TurnDirection(0xFE, 0x9, 500)
    Sleep(1000)
    OP_95(0xFE, -3450, 0, 500, 2000, 0x0)
    OP_95(0xFE, -4300, 0, 500, 2000, 0x0)
    OP_93(0xFE, 0xD2, 0x1F4)
    Return()

    # Function_23_34A1 end

    def Function_24_34DB(): pass

    label("Function_24_34DB")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch06600.itc", 0x1E)
    LoadChrToIndex("chr/ch47400.itc", 0x1F)
    LoadEffect(0x0, "event/ev622_00.eff")
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu03900.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu01200.itp")
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrChipByIndex(0x9, 0x1E)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrChipByIndex(0x8, 0x1F)
    OP_52(0x8, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x226), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x226), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x226), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xA, 0x80)
    OP_78(0x1, 0xA)
    OP_49()
    OP_74(0x1, 0xF)
    OP_70(0x1, 0x65)
    SetChrPos(0xA, 8730, -2400, 0, 270)
    OP_D5(0xA, 0x0, 0x41EB0, 0x0, 0x0)
    SetMapObjFrame(0x1, "pm_body:Layer1(5)", 0x0, 0x1)
    SetMapObjFrame(0x1, "pm_head:Layer1(4)", 0x1, 0x1)
    SetMapObjFrame(0x1, "pm_body:Layer3(7)", 0x1, 0x1)
    SetMapObjFrame(0x1, "pm_body:Layer3(8)", 0x1, 0x1)
    SetMapObjFrame(0x1, "pm_backpack:Layer1(9)", 0x1, 0x1)
    SetMapObjFrame(0x1, "pm_arm:Layer1(20)", 0x1, 0x1)
    SetMapObjFrame(0x1, "pm_arm:Layer1(29)", 0x1, 0x1)
    SetMapObjFrame(0x1, "pm_giar:Layer1(38)", 0x1, 0x1)
    SetMapObjFrame(0x1, "pm_giar:Layer1(39)", 0x1, 0x1)
    SetMapObjFrame(0x1, "Null_chest_ball(71)", 0x1, 0x1)
    ClearMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x2, 0x1000)
    ClearMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x3, 0x1000)
    StopBGM(0xFA0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7304", 0)
    SetChrPos(0x9, 6100, 500, -50, 270)
    SetChrPos(0x8, -2750, 0, 6300, 180)
    SetChrPos(0x101, 3300, 0, -50, 90)
    SetChrPos(0x107, 2750, 0, 900, 90)
    SetChrPos(0x103, 1750, 0, 300, 90)
    SetChrPos(0x105, 3500, 0, -1750, 45)
    SetChrPos(0x106, 2750, 0, -1000, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrSubChip(0x107, 0x5)
    OP_68(4740, 1400, -130, 0)
    MoveCamera(50, 20, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(22000, 0)
    MoveCamera(55, 20, 0, 3000)
    SetCameraDistance(20000, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x9,
        (
            "─ ─ um.\x01",
            "There were rare visitors as well.\x02\x03",
            "It's been a long time, Holy Wolf\x02",
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
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x107,
        (
            "#3CThat is true, child of man\x02\x03",
            "Truly nasty\x01",
            "It seems I got old for a long time.\x02\x03",
            "As usual \"snakes\"\x01",
            "It seems to be involved.\x02",
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
        0x9,
        (
            "#03903F#11PWho is it?\x01",
            "Even if not a worldly thing.\x02\x03",
            "#03900FWith the \"odds\" that bound the nakedness\x01",
            "Is it the same thing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#01201F#6P#3CHaha, that is true\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x106, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x103,
        (
            "#00211F#6P(Somehow unexpectedly\x01",
            "Like a distant story … …)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#6P(Oh, the same world\x01",
            "I do not think it is a conversation … …)\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x9, 0xE1, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x9,
        (
            "#03903F#5PBut to the guardian knight of the star,\x01",
            "I was about to invade here\x01",
            "Is it a devil from the eastern people street? …\x02\x03",
            "#03900FThere is quite a unique feeling\x01",
            "Are not they gathering up?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10402F#12PAh, true\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#10710F#6PI apologize for the last time I was here\x02",
    )

    CloseMessageWindow()
    Sleep(150)

    ChrTalk(
        0x101,
        (
            "#00006F#6PGeorge Maester\x02\x03",
            "#00001FAs we said, we now,\x01",
            "To manage this situation\x01",
            "It is moving.\x02\x03",
            "Especially about the movement of \"association\" ……\x01",
            "Do you know something?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x9, 0x10E, 0x1F4)
    Sleep(150)

    ChrTalk(
        0x9,
        (
            "#03900F#11PHmm\x02\x03",
            "#03903F── Maybe you already know\x01",
            "\"Society\" is the purpose of the Clois family this time\x01",
            "It is just a position to cooperate.\x02\x03",
            "Plan of \"Society\" - \"Phantom#4RNuclear power plant#Plan\x01",
            "It seems that it has already shifted to the next stage.\x02\x03",
            "#03901FIn other words, the Erebonia Empire\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00011F#6PHuh!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10406F#12PIn fact, other apostles and enforcers\x01",
            "You started moving around there.\x02\x03",
            "#10401FThe knights#6RBokura#To crossbell\x01",
            "Not to break the strength so far\x01",
            "The neighborhood is the reason.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008F#6PI see..\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#6P…… There are various things throughout the continent\x01",
            "It seems to have happened too much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#03903F#11PBut, very troublesome three people\x01",
            "It still remains in the crossbell.\x02\x03",
            "#03901FEven in the association\x01",
            "It is one of the most powerful people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#6PCampanella the Clown\x02\x03",
            "#00013FAnd called \"apostle\"\x01",
            "With Dr. Novartis\x01",
            "It is a woman named Ariane Road.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10708F#6P…\x02\x03",
            "#10706FWhat in the world is that woman?\x02\x03",
            "#10701FThat movement and reaction ─\x01",
            "Very human work#2RWork#I do not think.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#03903F#11PI don't know the details\x02\x03",
            "However, using an awesome spear technique,\x01",
            "Hitoshi Atsushi also#2RBuddy#As a person\x01",
            "It is known for \"association\".\x02\x03",
            "#03900FAll the battle warriors that accompany it,\x01",
            "Where is she?#4RIzuko#On finding out from\x01",
            "She seems to be practicing.\x02\x03",
            "Every person is an \"enforcer\"\x01",
            "It seems to have enough ability to approach it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00205F#6PLike that Renne girl\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10403F#12PWell, the ability of \"enforcer\"\x01",
            "It looks like it's not just battle … …\x02\x03",
            "#10408FEven so, in total six people\x01",
            "Is a troublesome partner cooperating?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F#6PBut …\x01",
            "Just being cooperating is that.\x02\x03",
            "#00001FIn some cases,\x01",
            "In the future situation of Crossbell\x01",
            "Is there a possibility not to get deep?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#03900F#11PYes that might be\x02\x03",
            "#03903FMost of all, Novartis's youth is\x01",
            "To the dolls who received the power of \"treasure\"\x01",
            "It looks interesting.\x02\x03",
            "#03901FAnyway, in my information\x01",
            "I do not know their future plans.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#6PI see…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#6PIt's quite easy\x01",
            "I do not think he will go.\x02\x03",
            "#00200F… … By the way, from the previous time\x01",
            "I am a little worried.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(6200, 1200, -50, 2000)
    MoveCamera(90, 10, 0, 2000)
    OP_6E(500, 2000)
    SetCameraDistance(20600, 2000)
    OP_6F(0x79)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            "#00200F#6P\"Patel-Mattel\"\x01",
            "Is it being repaired?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    Sound(859, 0, 70, 0)
    OP_87(0x0, 0xFF, 0x1, "pm_head:Layer1(4)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    Sleep(500)
    Sound(903, 0, 100, 0)
    Sleep(1500)

    ChrTalk(
        0x101,
        "#00011F#6PWaa\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#10712F#12PI-It talked?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#03903F#5PWell, hey.\x01",
            "It's like maintenance.\x02\x03",
            "Novartis's youth build\x01",
            "Extremely conscious of this aircraft#4RThe weekend#Was.\x02\x03",
            "#03901FNow I seem to be absorbed in a new doll\x01",
            "I do not think I'm worried … …\x02\x03",
            "If you come to rob it, let it escape\x01",
            "I thought that I should just prepare.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F#6PI-I see\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10404F#12PThere is an \"annihilating angel\" in the event\x01",
            "Are you going to Libert?\x02\x03",
            "#10400FBut as long as you hear it\x01",
            "You seem to be very close with that doctor, are not you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#03903F#5PHmm. I don't deny it\x02\x03",
            "Originally this \"Goldias grade\"\x01",
            "It was developed by multiplying all of my items.\x02\x03",
            "#03900FI took it away on the way,\x01",
            "To the triumph of up to the connection test\x01",
            "To infants like Ren#2RAddressed#What I did ….\x02\x03",
            "Although somehow the connection succeeded,\x01",
            "The attempt itself is an unacceptable business.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008F#6PRight..\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#6P…… Experiments done by the cult and\x01",
            "It may not differ much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#03903F#5PBesides, without treasure\x01",
            "I can not operate satisfactorily\x01",
            "Develop successors without permission ……\x02\x03",
            "We call it \"Gordias class\"\x01",
            "Shamelessly say \"Final type\" etc.\x01",
            "Awesome … …!\x02\x03",
            "#03901FIf you are in this place, that fine head\x01",
            "It is a place to tighten up …!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012F#6PI-I see…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#01203F#6P#3CWell, settle down\x02\x03",
            "#01200FAs usual it will be a work thing\x01",
            "It seems I can not keep calm.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#03903F#5PKohon ……\x01",
            "Well, anyway.\x02\x03",
            "#03900FNo matter how thick face shame,\x01",
            "Through the application and strengthening technology\x01",
            "It is certain to have a genius brain.\x02\x03",
            "I also developed puppet weapons\x01",
            "After being remodeled and strengthened to afternoon\x01",
            "I heard that it is mass-produced.\x02\x03",
            "In rumors, those airframes\x01",
            "Also in \"tower\" and \"monastery\"\x01",
            "It seems to be deployed.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x106, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AF, 4)), scpexpr(EXPR_END)), "loc_4B66")

    ChrTalk(
        0x105,
        "#10401F#12PHe who was in front of that tower … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#6P…… certainly tough times\x01",
            "It was a strong doll.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4BAD")

    label("loc_4B66")


    ChrTalk(
        0x101,
        "#00001F#6PIs that right\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10403F#12PThat's the first we've heard of that\x02",
    )

    CloseMessageWindow()

    label("loc_4BAD")


    ChrTalk(
        0x103,
        (
            "#00208F#6PBut in those places\x01",
            "To be deployed …\x02\x03",
            "#00201FAgain the example \"big bell\"\x01",
            "Are they protecting?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#03903F#5PThat is very likely\x02\x03",
            "#03900FIt seems that artifact\x01",
            "About \"big bell\"\x01",
            "I am also studying it personally.\x02\x03",
            "If you know something you also\x01",
            "You can tell me.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00011F#6PR-really!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10402F#12POh ….?\x01",
            "As expected, is not it too generous?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#03903F#5PHun …#4RThis time#About the end of\x01",
            "I also have a few head minded.\x02\x03",
            "#03901FThat Nobaltisse brat aside\x02\x03",
            "I cooperated with \"the theater company#4RAlkane shell#The\x01",
            "Sometimes I was made casually.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#10708F#12PAh…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#6Pby the way……\x01",
            "Stage equipment and automatic dolls#8RAuto meta#Also\x01",
            "It seems that everything was destroyed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#03903F#5PRight. I have to remake all of them\x02\x03",
            "#03901FIn that sense, \"red constellation\" and\x01",
            "The owner of the Clois family who hired it also\x01",
            "Personally I can not forgive.\x02\x03",
            "#03903FMy daughter, my doll\x01",
            "Enthusiastic collector#6Rcollector#It seems like ……\x01",
            "And that is different from this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10404F#12PEhe, I see\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#6P……I understand.\x01",
            "To be honest, it is very helpful.\x02\x03",
            "#00000FIf you know something about \"big bell\"\x01",
            "Come and contact us.\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(21600, 2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    SetScenarioFlags(0x22, 1)
    NewScene("t3000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_24_34DB end

    SaveToFile()

Try(main)
