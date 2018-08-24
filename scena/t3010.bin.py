from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "Guide Doll",             # 1
        "Meister Jｶrg",          # 2
        "Patemate",               # 3
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(332, 0)                                        # 0

    ScpFunction((
        "Function_0_14C",          # 00, 0
        "Function_1_17A",          # 01, 1
        "Function_2_1AA",          # 02, 2
        "Function_3_31E8",         # 03, 3
        "Function_4_3227",         # 04, 4
        "Function_5_328A",         # 05, 5
        "Function_6_3317",         # 06, 6
        "Function_7_33A3",         # 07, 7
        "Function_8_33ED",         # 08, 8
        "Function_9_3427",         # 09, 9
        "Function_10_3467",        # 0A, 10
        "Function_11_34B1",        # 0B, 11
        "Function_12_34EB",        # 0C, 12
        "Function_13_352B",        # 0D, 13
        "Function_14_3575",        # 0E, 14
        "Function_15_35AF",        # 0F, 15
        "Function_16_35EF",        # 10, 16
        "Function_17_3639",        # 11, 17
        "Function_18_3673",        # 12, 18
        "Function_19_36B3",        # 13, 19
        "Function_20_36FD",        # 14, 20
        "Function_21_3737",        # 15, 21
        "Function_22_3777",        # 16, 22
        "Function_23_37C1",        # 17, 23
        "Function_24_37FB",        # 18, 24
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
            "And so, Lloyd and the\x01",
            "others were shown inside\x01",
            "by the automaton guide...\x02\x03",
            "They were led to a to a\x01",
            "corner of the studio's\x01",
            "maze-like basement.\x07\x00\x02",
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

    def lambda_67F():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_67F)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)

    def lambda_694():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_694)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x105, 0x1)
    EndChrThread(0x109, 0x1)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x103, 2)

    ChrTalk(
        0x101,
        "#00013F#5PW-What is this place...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00205F#5P...Amazing...\x02",
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

    def lambda_774():
        OP_93(0x101, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_774)
    Sleep(50)

    def lambda_784():
        OP_93(0x102, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_784)
    Sleep(50)

    def lambda_794():
        OP_93(0x103, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_794)
    Sleep(50)

    def lambda_7A4():
        OP_93(0x104, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_7A4)
    Sleep(50)

    def lambda_7B4():
        OP_93(0x109, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_7B4)
    Sleep(50)

    def lambda_7C4():
        OP_93(0x105, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_7C4)
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
        "#10111F#6P#4SWhaaat...!?\x02",
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
            "#10301F#6P#NCould that be... The\x01",
            "giant doll you were\x01",
            "talking about?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00006F#6P#NYeah... It's Pater-Mater\x01",
            "that Renne was using...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        "#00108F#6P#NSo it's kept here...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#00306F#6P#NStill, to think that there\x01",
            "was a place like this\x01",
            "beneath the studio...\x02",
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
            "#00208F#11PThere appears to be\x01",
            "orbal net terminals here\x01",
            "as well...\x02\x03",
            "#00201FCould "Kitty" have\x01",
            "hacked the net\x01",
            "wirelessly from here?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x9,
        "Elderly Voice",
        "─So, what do you need?\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_AED():
        TurnDirection(0x101, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_AED)
    Sleep(50)

    def lambda_AFD():
        TurnDirection(0x102, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_AFD)
    Sleep(50)

    def lambda_B0D():
        TurnDirection(0x103, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_B0D)
    Sleep(50)

    def lambda_B1D():
        TurnDirection(0x104, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_B1D)
    Sleep(50)

    def lambda_B2D():
        TurnDirection(0x109, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_B2D)
    Sleep(50)

    def lambda_B3D():
        TurnDirection(0x105, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_B3D)
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 4)), scpexpr(EXPR_END)), "loc_C64")

    ChrTalk(
        0x101,
        (
            "#00003F#5PUmm... Thank you very\x01",
            "much for taking the time\x01",
            "to speak with us.\x02\x03",
            "#00001FActually, we have a few\x01",
            "things we'd like to ask\x01",
            "you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D42")

    label("loc_C64")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x30, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_CE0")

    ChrTalk(
        0x101,
        (
            "#00003F#5PUhhm... It's been a long\x01",
            "time.\x02\x03",
            "#00001FActually, we have a few\x01",
            "things we'd like to ask\x01",
            "you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D42")

    label("loc_CE0")


    ChrTalk(
        0x101,
        (
            "#00006F#5PUmm... How do you do.\x02\x03",
            "#00001FActually, we have a few\x01",
            "things we'd like to ask\x01",
            "you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D42")


    ChrTalk(
        0x9,
        (
            "#03903F#12PHmph...\x02\x03",
            "#03900FPerhaps it's about what\x01",
            "Campanella is trying to\x01",
            "do.\x02",
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
        "#00013F#5P...!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00301F#5POld man, you...\x02",
    )

    CloseMessageWindow()
    OP_93(0x9, 0x1E, 0x1F4)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x30, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_F35")

    ChrTalk(
        0x9,
        (
            "#03903F#6P─Don't misunderstand.\x02\x03",
            "#03900FIt's true I'm Ouroboros\x01",
            "staff, but in the end I\x01",
            "am a mere doll maker.\x02\x03",
            "It's not the case that\x01",
            "I'm directly involved in\x01",
            "Ouroboros' plan.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1002")

    label("loc_F35")


    ChrTalk(
        0x9,
        (
            "#03903F#6P─Don't misunderstand.\x02\x03",
            "#03900FAs you heard from Renne, I am\x01",
            "indeed Ouroboros staff, but in\x01",
            "the end I am a mere doll maker.\x02\x03",
            "It's not the case that I'm\x01",
            "directly involved in Ouroboros'\x01",
            "plan.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1002")


    ChrTalk(
        0x101,
        (
            "#00006F#5PT-Then...\x02\x03",
            "#00001FYou don't know what that\x01",
            "boy, Campanella, is\x01",
            "trying to do...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#03900F#6PI don't, nor am I in a\x01",
            "position to know.\x02\x03",
            "#03903FHowever... He isn't an\x01",
            "Anguis, but an Enforcer.\x02\x03",
            "He isn't in a position to\x01",
            "propose a "plan" Ouroboros\x01",
            "would advance.\x02\x03",
            "#03901FAfter all, it is the Anguis\x01",
            "who design and draft the\x01",
            "plans of Ouroboros.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101F#11PP-Please wait a\x01",
            "moment...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F#11PS-Somehow this talk is\x01",
            "too sudden and I can't\x01",
            "keep up with it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10305F#11PThis seems like important\x01",
            "inside information... Can you\x01",
            "tell us such things so easily?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#03903F#6PHehe... It's not exactly prohibited.\x02\x03",
            "#03900FAnd, there's a fair number of people\x01",
            "who know this level of information\x01",
            "already.\x02\x03",
            "The Church, guild and the major powers'\x01",
            "intelligence agencies should've figured\x01",
            "it out a long time ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F#5P............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00201F#5PNevertheless, you\x01",
            "continue to make dolls\x01",
            "here...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#03903F#6PTo begin with, I'm in no position to\x01",
            "know the full details of Ouroboros.\x02\x03",
            "#03900FFor instance, even my archaisms are made\x01",
            "using the technology of many different\x01",
            "workshops other than this one.\x02\x03",
            "In a manner of speaking, this place is\x01",
            "but one tail of a giant Snake...\x02\x03",
            "#03903FThat's also a reason why the Church and\x01",
            "guild don't simply march in here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#5PI see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F#5PExtractin' info as\x01",
            "needed instead of just\x01",
            "exposin' you...\x02\x03",
            "#00300FI guess you're more\x01",
            "useful that way, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#03903F#6PRight, and in addition,\x01",
            "this studio even has a\x01",
            ""guard".\x02\x03",
            "#03901FIf you were to get an\x01",
            "arrest warrant and break\x01",
            "in here...\x02\x03",
            "You would most likely\x01",
            "discover nothing more\x01",
            "than an empty studio.\x02\x03",
            "Pater-Mater included.\x02",
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
            "#03903F#6PHehe, would you like to\x01",
            "try to take me into\x01",
            "custody here and now?\x02\x03",
            "#03900FThis may be your only\x01",
            "chance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#5P─No, we'll pass.\x02\x03",
            "#00001FIt really seems\x01",
            "better... to just ask\x01",
            "for information.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108F#11P...Lloyd...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FW#11P-Wait... I can't\x01",
            "really agree, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#03903F#6PHaha, a wise decision.\x02\x03",
            "#03900FIt seems you have many\x01",
            "specific things you want\x01",
            "to ask me, but...\x02\x03",
            "Narrow them down to\x01",
            "three. I'll answer if\x01",
            "I'm able.\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xBB8)

    ChrTalk(
        0x101,
        (
            "#00003F#5P...I understand.\x02\x03",
            "#00008F(What I want to know\x01",
            "from the Meister is...)\x02",
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

    label("loc_1942")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DCD")
    FadeToDark(300, 0, 100)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_19E4")

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[About Ouroboros' Anguis]\x01",                    # 0
            "[About Ouroboros' Plan]\x01",                      # 1
            "[Ouroboros' Relationship with the Cult]\x01",      # 2
            "[Quit Asking]\x01",                                # 3
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Jump("loc_1A4D")

    label("loc_19E4")


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[About Ouroboros' Anguis]\x01",                    # 0
            "[About Ouroboros' Plan]\x01",                      # 1
            "[Ouroboros' Relationship with the Cult]\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)

    label("loc_1A4D")

    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_1A79"),
        (0, "loc_1E8A"),
        (2, "loc_2896"),
        (3, "loc_2DC0"),
        (SWITCH_DEFAULT, "loc_2DC8"),
    )


    label("loc_1A79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DFA")

    ChrTalk(
        0x9,
        (
            "#03903F#6PLike I told you before,\x01",
            "I don't know the\x01",
            "details.\x02\x03",
            "But, according to what\x01",
            "I've heard, it's called\x01",
            "this.\x02\x03",
            "#03901F─The "Phantasmal Blaze\x01",
            "Plan".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F#5PThe Phantasmal Blaze\x01",
            "Plan...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10301F#11PA name with hidden\x01",
            "meaning...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101F#11PThis plan... Do they intend to\x01",
            "bring an incident like the one in\x01",
            "Liberl a year ago to Crossbell?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10107F#11PI-If that's the case...\x01",
            "I'll never allow it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#03903F#6PI'm repeating myself, but I don't\x01",
            "know the details.\x02\x03",
            "#03900FBut if I could just say one thing,\x01",
            "the intervention of Ouroboros is on a\x01",
            "smaller scale than it was in Liberl.\x02\x03",
            "Ouroboros is a shady existence...\x01",
            "They don't normally appear center\x01",
            "stage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00101F#11P............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#5PHow to say it... That\x01",
            "doesn't make me feel any\x01",
            "better...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00211F#5POn the contrary, It's like\x01",
            "the name makes me feel more\x01",
            "anxious all by itself...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1E85")

    label("loc_1DFA")


    ChrTalk(
        0x9,
        (
            "#03903F#6PI don't even know the\x01",
            "outline.\x02\x03",
            "But, according to what\x01",
            "I've heard, it's called\x01",
            "this.\x02\x03",
            "#03901F─The "Phantasmal Blaze\x01",
            "Plan".\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E85")

    Jump("loc_2DC8")

    label("loc_1E8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2749")
    Sleep(150)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(500)
    SetMessageWindowPos(280, 170, -1, -1)

    AnonymousTalk(
        0x9,
        (
            "#3C#30WThe Anguis─\x02\x03",
            "Seven leaders who learn the\x01",
            "great Grandmaster's ideas\x01",
            "and implement his plans.\x02\x03",
            "I don't know the details of\x01",
            "each either, but...\x02\x03",
            "I do know the Anguis who\x01",
            "are going to come to\x01",
            "Crossbell before long.\x02",
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
            "#00013F#5PT-Then... What kind of\x01",
            "people are they?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#03900F#6P...............\x02\x03",
            "#03903FOne of them is a man who, as the 6th\x01",
            "Anguis, supervises the Thirteen\x01",
            "Workshops, Ouroboros' technology network.\x02\x03",
            "Ouroboros' leading theorist and their\x01",
            "greediest engineer...\x02\x03",
            "#03901FWell, let's just say he's a nasty man.\x02",
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
        (
            "#00206F#5PEven if you say it like\x01",
            "that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10101F#11PN-Nasty in what sense?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#03903F#6PFor better or worse, he's a man\x01",
            "who thinks only of satisfying\x01",
            "his intellectual curiosity.\x02\x03",
            "I don't know what he hopes to\x01",
            "achieve by coming here, but...\x02\x03",
            "#03901FAt the very least, I can be\x01",
            "sure it's nothing good for\x01",
            "Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108F#11P...............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#5PBased on what you told\x01",
            "us, he does seem nasty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#03903F#6P...There's one more...\x02\x03",
            "#03900FI have information that the 7th\x01",
            "Anguis, crowned with the name\x01",
            "of Steel, will enter Crossbell.\x02",
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
        "#00005F#5PSteel...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301F#5PHow to say this... Don't\x01",
            "they sound a little\x01",
            "dangerous?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#03903F#6PHehe... They're a bit of a mysterious\x01",
            "character.\x02\x03",
            "#03900FIf I could say one thing, it's that they are\x01",
            "a master of such a level, even all of you\x01",
            "together could never hope to match them.\x02",
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
        (
            "#00011F#5PEven all of us\x01",
            "together!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#11PWow, you seem pretty\x01",
            "confident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#03903F#6PWell, think of it as a warning.\x02\x03",
            "I heard they are a noble character\x01",
            "unlike the 6th Anguis, but...\x02\x03",
            "#03901FIf you're foolish enough to\x01",
            "challenge them, you'll end up\x01",
            "getting yourselves killed for sure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00013F#5P......\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2891")

    label("loc_2749")


    ChrTalk(
        0x9,
        (
            "#03903F#6PI don't know the details, but\x01",
            "I heard two Anguis are coming\x01",
            "to Crossbell.\x02\x03",
            "#03900FOne is the 6th Anguis─ A\x01",
            "nasty engineer who supervises\x01",
            "the Thirteen Workshops.\x02\x03",
            "The other is the 7th Anguis─\x01",
            "The strongest master crowned\x01",
            "with the name of Steel.\x02\x03",
            "#03903FI suppose neither is an\x01",
            "opponent you could handle,\x01",
            "though.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2891")

    Jump("loc_2DC8")

    label("loc_2896")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C8A")

    ChrTalk(
        0x9,
        (
            "#03903F#6PThe D∴G Cult, huh.\x02\x03",
            "#03901FBased on what I know, it\x01",
            "seems they didn't have\x01",
            "any direct ties.\x02\x03",
            "Although it's a fact that\x01",
            "Ouroboros destroyed the\x01",
            "lodge where Renne was...\x02",
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
        "#00011F#5PHuh!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101F#11PThe one called\x01",
            "Paradise...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#03900F#6PYes, it appears to have been place\x01",
            "for winning over influential people\x01",
            "across the continent.\x02\x03",
            "It became a target for annihilation\x01",
            "most likely because it began\x01",
            "targeting Ouroboros' supporters.\x02\x03",
            "#03903FThe fact that Renne survived can be\x01",
            "said to be nothing other than sheer\x01",
            "luck.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00208F#5P...............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#5PI really can't consider Ouroboros\x01",
            "to be an upstanding organization\x01",
            "just because of that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10301F#11PHonestly, we can't\x01",
            "accept it just with that\x01",
            "explanation, you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#03903F#6PHehe, didn't I tell you?\x01",
            ""Based on what I know."\x02\x03",
            "#03900FIt's up to you all how\x01",
            "to judge it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2DBB")

    label("loc_2C8A")


    ChrTalk(
        0x9,
        (
            "#03903F#6PThe D∴G Cult─ Based on what I know, it\x01",
            "seems they didn't have any direct ties\x01",
            "with Ouroboros.\x02\x03",
            "#03900FAlthough it's a fact that Ouroboros\x01",
            "destroyed the lodge where Renne was...\x02\x03",
            "It likely became a target for\x01",
            "extermination after they started targeting\x01",
            "Ouroboros' supporters. Nothing more.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DBB")

    Jump("loc_2DC8")

    label("loc_2DC0")

    SetScenarioFlags(0x0, 3)
    Jump("loc_2DC8")

    label("loc_2DC8")

    Jump("loc_1942")

    label("loc_2DCD")


    ChrTalk(
        0x9,
        (
            "#03900F#6PHmm, I suppose this\x01",
            "makes three.\x02\x03",
            "#03903F─My time is valuable. I\x01",
            "think it's time I asked\x01",
            "you to leave.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00013F#5P......\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00107F#11PB-But...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10108F#11PL-Lloyd...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00006F#5P─That was our agreement.\x01",
            "We'll leave it here,\x01",
            "this time.\x02\x03",
            "#00000FDo you mind if we come\x01",
            "again, if we get a\x01",
            "chance?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#03903F#6PWell, if I feel like it.\x02\x03",
            "#03901FBut to it's not only us you should be\x01",
            "concerned with in the first place.\x02\x03",
            "Aren't there a bunch of different forces\x01",
            "you have to look out for in advance of\x01",
            "your "state independence" or whatever?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00011F#5PW-Well...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00303F#5P...Well, that's true.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#11PYou seem to know all\x01",
            "those forces' respective\x01",
            "actions, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#03903F#6PHehe, I wonder.\x02",
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
            "#03900F#6P─Alright then, stay close\x01",
            "to that little one on\x01",
            "your way back as well.\x02\x03",
            "I can't guarantee your\x01",
            "safety if you lose sight\x01",
            "of her, you know?\x02",
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

    def Function_3_31E8(): pass

    label("Function_3_31E8")

    OP_95(0xFE, 0, 0, 102000, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    StopSound(957, 300, 30)
    Sleep(1000)
    Sound(957, 2, 40, 0)
    OP_95(0xFE, -21450, 0, 102000, 2000, 0x0)
    Return()

    # Function_3_31E8 end

    def Function_4_3227(): pass

    label("Function_4_3227")

    Sound(957, 2, 40, 0)

    def lambda_3232():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3232)
    OP_95(0xFE, 0, 0, 5000, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    StopSound(957, 300, 30)
    Sleep(1000)
    Sound(957, 2, 40, 0)
    OP_95(0xFE, -2750, 0, 6300, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    StopSound(957, 300, 30)
    Return()

    # Function_4_3227 end

    def Function_5_328A(): pass

    label("Function_5_328A")

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

    # Function_5_328A end

    def Function_6_3317(): pass

    label("Function_6_3317")

    OP_68(0, 600, 101000, 7000)
    SetCameraDistance(22000, 7000)
    OP_95(0xFE, 0, 0, 100000, 2000, 0x0)

    def lambda_334A():

        label("loc_334A")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_334A")

    QueueWorkItem2(0xFE, 2, lambda_334A)
    Sleep(2000)
    EndChrThread(0xFE, 0x2)
    OP_68(-10000, 600, 102000, 8000)
    MoveCamera(40, 20, 0, 8000)
    OP_95(0xFE, -2000, 0, 102000, 2000, 0x0)
    OP_95(0xFE, -21450, 0, 102000, 2000, 0x0)
    Return()

    # Function_6_3317 end

    def Function_7_33A3(): pass

    label("Function_7_33A3")


    def lambda_33A8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_33A8)
    OP_95(0xFE, 0, 0, 2500, 2000, 0x0)

    label("loc_33C8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_33EC")
    OP_93(0xFE, 0x87, 0x1F4)
    Sleep(1500)
    OP_93(0xFE, 0xE1, 0x1F4)
    Sleep(1500)
    Jump("loc_33C8")

    label("loc_33EC")

    Return()

    # Function_7_33A3 end

    def Function_8_33ED(): pass

    label("Function_8_33ED")

    TurnDirection(0xFE, 0x9, 500)
    Sleep(100)
    OP_95(0xFE, -3450, 0, -500, 2000, 0x0)
    OP_95(0xFE, -6500, -250, -1500, 2000, 0x0)
    OP_93(0xFE, 0xD2, 0x1F4)
    Return()

    # Function_8_33ED end

    def Function_9_3427(): pass

    label("Function_9_3427")

    OP_95(0xFE, 500, 0, 99500, 2000, 0x0)
    Sleep(2000)
    OP_95(0xFE, -2000, 0, 102500, 2000, 0x0)
    OP_95(0xFE, -21450, 0, 102500, 2000, 0x0)
    Return()

    # Function_9_3427 end

    def Function_10_3467(): pass

    label("Function_10_3467")


    def lambda_346C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_346C)
    OP_95(0xFE, 750, 0, 3500, 2000, 0x0)

    label("loc_348C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_34B0")
    OP_93(0xFE, 0x87, 0x1F4)
    Sleep(1500)
    OP_93(0xFE, 0x5A, 0x1F4)
    Sleep(1500)
    Jump("loc_348C")

    label("loc_34B0")

    Return()

    # Function_10_3467 end

    def Function_11_34B1(): pass

    label("Function_11_34B1")

    TurnDirection(0xFE, 0x9, 500)
    Sleep(200)
    OP_95(0xFE, -3450, 0, -1000, 2000, 0x0)
    OP_95(0xFE, -5500, -250, -1150, 2000, 0x0)
    OP_93(0xFE, 0xD2, 0x1F4)
    Return()

    # Function_11_34B1 end

    def Function_12_34EB(): pass

    label("Function_12_34EB")

    OP_95(0xFE, -750, 0, 99000, 2000, 0x0)
    Sleep(2100)
    OP_95(0xFE, -2000, 0, 101250, 2000, 0x0)
    OP_95(0xFE, -21450, 0, 101250, 2000, 0x0)
    Return()

    # Function_12_34EB end

    def Function_13_352B(): pass

    label("Function_13_352B")


    def lambda_3530():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3530)
    OP_95(0xFE, -1000, 0, 3000, 2000, 0x0)

    label("loc_3550")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3574")
    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(1500)
    OP_93(0xFE, 0xE1, 0x1F4)
    Sleep(1500)
    Jump("loc_3550")

    label("loc_3574")

    Return()

    # Function_13_352B end

    def Function_14_3575(): pass

    label("Function_14_3575")

    TurnDirection(0xFE, 0x9, 500)
    Sleep(500)
    OP_95(0xFE, -3450, 0, 500, 2000, 0x0)
    OP_95(0xFE, -6650, -250, -300, 2000, 0x0)
    OP_93(0xFE, 0xD2, 0x1F4)
    Return()

    # Function_14_3575 end

    def Function_15_35AF(): pass

    label("Function_15_35AF")

    OP_95(0xFE, 0, 0, 98000, 2000, 0x0)
    Sleep(2000)
    OP_95(0xFE, -2000, 0, 102000, 2000, 0x0)
    OP_95(0xFE, -21450, 0, 102000, 2000, 0x0)
    Return()

    # Function_15_35AF end

    def Function_16_35EF(): pass

    label("Function_16_35EF")


    def lambda_35F4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_35F4)
    OP_95(0xFE, -250, 0, 4000, 2000, 0x0)

    label("loc_3614")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3638")
    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(1500)
    OP_93(0xFE, 0x5A, 0x1F4)
    Sleep(1500)
    Jump("loc_3614")

    label("loc_3638")

    Return()

    # Function_16_35EF end

    def Function_17_3639(): pass

    label("Function_17_3639")

    TurnDirection(0xFE, 0x9, 500)
    Sleep(400)
    OP_95(0xFE, -3450, 0, -500, 2000, 0x0)
    OP_95(0xFE, -5450, -250, 300, 2000, 0x0)
    OP_93(0xFE, 0xD2, 0x1F4)
    Return()

    # Function_17_3639 end

    def Function_18_3673(): pass

    label("Function_18_3673")

    OP_95(0xFE, 750, 0, 97250, 2000, 0x0)
    Sleep(2100)
    OP_95(0xFE, -2000, 0, 102250, 2000, 0x0)
    OP_95(0xFE, -21450, 0, 102250, 2000, 0x0)
    Return()

    # Function_18_3673 end

    def Function_19_36B3(): pass

    label("Function_19_36B3")


    def lambda_36B8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_36B8)
    OP_95(0xFE, 500, 0, 5500, 2000, 0x0)

    label("loc_36D8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_36FC")
    OP_93(0xFE, 0x87, 0x1F4)
    Sleep(1500)
    OP_93(0xFE, 0xE1, 0x1F4)
    Sleep(1500)
    Jump("loc_36D8")

    label("loc_36FC")

    Return()

    # Function_19_36B3 end

    def Function_20_36FD(): pass

    label("Function_20_36FD")

    TurnDirection(0xFE, 0x9, 500)
    Sleep(500)
    OP_95(0xFE, -3450, 0, -1000, 2000, 0x0)
    OP_95(0xFE, -4250, 0, -850, 2000, 0x0)
    OP_93(0xFE, 0xD2, 0x1F4)
    Return()

    # Function_20_36FD end

    def Function_21_3737(): pass

    label("Function_21_3737")

    OP_95(0xFE, 1250, 0, 98500, 2000, 0x0)
    Sleep(2000)
    OP_95(0xFE, -2000, 0, 102750, 2000, 0x0)
    OP_95(0xFE, -21450, 0, 102750, 2000, 0x0)
    Return()

    # Function_21_3737 end

    def Function_22_3777(): pass

    label("Function_22_3777")


    def lambda_377C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_377C)
    OP_95(0xFE, -1000, 0, 4500, 2000, 0x0)

    label("loc_379C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_37C0")
    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(1500)
    OP_93(0xFE, 0x13B, 0x1F4)
    Sleep(1500)
    Jump("loc_379C")

    label("loc_37C0")

    Return()

    # Function_22_3777 end

    def Function_23_37C1(): pass

    label("Function_23_37C1")

    TurnDirection(0xFE, 0x9, 500)
    Sleep(1000)
    OP_95(0xFE, -3450, 0, 500, 2000, 0x0)
    OP_95(0xFE, -4300, 0, 500, 2000, 0x0)
    OP_93(0xFE, 0xD2, 0x1F4)
    Return()

    # Function_23_37C1 end

    def Function_24_37FB(): pass

    label("Function_24_37FB")

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
            "─Hmm. Some rare guests have\x01",
            "arrived as well.\x02\x03",
            "Been a while, Divine Wolf.\x02",
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
            "#3CYes it has, child of man.\x02\x03",
            "It looks like you've aged quite a\x01",
            "bit yourself.\x02\x03",
            "It appears you're involved with\x01",
            "those Snake folks like always.\x02",
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
            "#03903F#11PTies are things that\x01",
            "follow you around until\x01",
            "you wither away into dust.\x02\x03",
            "#03900FThe Oath that binds you is\x01",
            "similar, correct?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#01201F#6P#3CHaha, for certain.\x02",
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
            "#00211F#6P(Looks like they're\x01",
            "talking about an\x01",
            "extremely old story...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#6P(Yeah, I can't imagine\x01",
            "it's a conversation about\x01",
            "our current world...)\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x9, 0xE1, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x9,
        (
            "#03903F#5PIn any case, a Gralsritter Dominion\x01",
            "and the Demon of the Eastern Quarter\x01",
            "who tried to infiltrate this place...\x02\x03",
            "#03900FQuite the eccentric ensemble of\x01",
            "people we have here, hm?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10402F#12PHaha, that's true.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10710F#6P...I apologise for\x01",
            "before.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)

    ChrTalk(
        0x101,
        (
            "#00006F#6P─Meister Jｶrg.\x02\x03",
            "#00001FLike we told you, we're\x01",
            "currently trying to do\x01",
            "something about this situation.\x02\x03",
            "Don't you know anything...?\x01",
            "Especially about Ouroboros'\x01",
            "actions...\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x9, 0x10E, 0x1F4)
    Sleep(150)

    ChrTalk(
        0x9,
        (
            "#03900F#11PHmm...\x02\x03",
            "#03903F─You may already know this, but Ouroboros'\x01",
            "current position is nothing more than one of\x01",
            "cooperation to achieve the Crois clan's goals.\x02\x03",
            "It appears that Ouroboros' plan─ the\x01",
            ""Phantasmal Blaze Plan" has already moved on\x01",
            "to the next stage.\x02\x03",
            "#03901FIn other words, to the Erebonian Empire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00011F#6PHuh...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10406F#12PActually, the other Anguis\x01",
            "and Enforcers have already\x01",
            "begun to act over there.\x02\x03",
            "#10401FThat's also the reason why\x01",
            "we knights couldn't risk so\x01",
            "many forces in Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008F#6PI see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#6P...It seems that too many\x01",
            "things are happening all\x01",
            "over Zemuria.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#03903F#11PHowever, three extremely\x01",
            "troublesome individuals\x01",
            "still remain in Crossbell.\x02\x03",
            "#03901FThey're also prominent\x01",
            "figures among the Society.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#6PCampanella The Fool...\x02\x03",
            "#00013FAnd the Anguis: The doctor\x01",
            "known as Novartis and the\x01",
            "woman called Arianrhod.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10708F#6P............\x02\x03",
            "#10706FWho in the world is that\x01",
            "woman?\x02\x03",
            "#10701FThose movements and\x01",
            "reactions─ They're nothing\x01",
            "like a human's at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#03903F#11PI myself don't know all the\x01",
            "details.\x02\x03",
            "However, she's known in the Society\x01",
            "as a fierce lance wielder and as a\x01",
            "person with a strong moral code.\x02\x03",
            "#03900FI heard that not only did she\x01",
            "discover the valkyries who follow\x01",
            "her, but she also trained them.\x02\x03",
            "It seems that each of them has a\x01",
            "strength that rivals that of an\x01",
            "Enforcer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00205F#6PJust like Renne from\x01",
            "before...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10403F#12PWell, it appears that the\x01",
            "abilities of an Enforcer\x01",
            "aren't limited to combat...\x02\x03",
            "#10408FNevertheless, we have six\x01",
            "troublesome enemies working\x01",
            "together, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F#6P...However, they're just collaborating for\x01",
            "now.\x02\x03",
            "#00001FDepending on the circumstances, isn't it\x01",
            "possible that they won't involve themselves\x01",
            "further with the situation in Crossbell?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#03900F#11PHmm. That could very well be the case.\x02\x03",
            "#03903FAlthough that youngster Novartis seems\x01",
            "to be extremely interested in the dolls\x01",
            "that received the Sept-Terrion's power.\x02\x03",
            "#03901FIn any event, with the information I\x01",
            "have, I don't know what their future\x01",
            "plans are.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#6PI see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#6PIt seems we won't be\x01",
            "able to deal with them\x01",
            "through ordinary means.\x02\x03",
            "#00200F...By the way, there's\x01",
            "something that's been on\x01",
            "my mind for some time...\x02",
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
            "#00200F#6PAre you currently\x01",
            "repairing Pater-Mater?\x02",
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
        "#00011F#6PWhoa...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#10712F#12PI-It talked...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#03903F#5PWell, it's just simple\x01",
            "maintenance.\x02\x03",
            "That young Novartis fellow was\x01",
            "quite fond of this machine.\x02\x03",
            "#03901FHe's currently focused on the\x01",
            "new dolls, so I think there's\x01",
            "nothing to worry about, but...\x02\x03",
            "In case he comes to steal it,\x01",
            "I'm just fixing it up so it\x01",
            "can escape.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F#6PI-I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10404F#12PSo in case of an emergency, he'll\x01",
            "be able to retreat to Liberl,\x01",
            "where the Angel of Slaughter is.\x02\x03",
            "#10400FAnyway, based on what I'm\x01",
            "hearing, you don't get along with\x01",
            "that doctor at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#03903F#5PHmph, I won't deny it.\x02\x03",
            "Originally, this Gordias-class was an\x01",
            "invention that I gave my all to develop.\x02\x03",
            "#03900FHe took it away in the middle of development\x01",
            "and gave it to a little kid like Renne to\x01",
            "operate, and in the end he even performed\x01",
            "inhumane compatibility tests...\x02\x03",
            "Although a connection between the subject\x01",
            "and machine was formed in the end, the tests\x01",
            "themselves were an unforgivable act.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008F#6PIndeed...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#6P...Virtually the same thing\x01",
            "can be said of the experiments\x01",
            "the cult performed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#03903F#5POn top of that, he developed a successor\x01",
            "unit that can't even functionally operate\x01",
            "without a Sept-Terrion on his own...\x02\x03",
            "And the impudence to brazenly call it the\x01",
            "'Final Model' of the Gordias-class!\x02\x03",
            "#03901FWhen he showed his face here, I was about\x01",
            "to strangle that tiny neck of his!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012F#6PI-I see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#01203F#6P#3CNow, now, calm down.\x02\x03",
            "#01200FAs always, it appears that\x01",
            "you can't stay calm when it\x01",
            "comes to your creations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#03903F#5P*cough*... Well, be that as it may.\x02\x03",
            "#03900FHowever shameless he is, it's certain that he\x01",
            "has the mind of a genius when it comes to the\x01",
            "development and application of technology.\x02\x03",
            "I heard that, after remodeling and powering\x01",
            "up the archaism I developed, he even mass\x01",
            "produced it.\x02\x03",
            "According to rumor, those units have been\x01",
            "deployed at the Tower, Temple and so on.\x02",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AF, 4)), scpexpr(EXPR_END)), "loc_5256")

    ChrTalk(
        0x105,
        (
            "#10401F#12PThose ones in front of\x01",
            "the Tower, huh...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#6P...It's true that the dolls\x01",
            "there seemed to exude\x01",
            "overwhelming strength...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_52A7")

    label("loc_5256")


    ChrTalk(
        0x101,
        "#00001F#6PI see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10403F#12P... That's the first\x01",
            "I've heard of this.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_52A7")


    ChrTalk(
        0x103,
        (
            "#00208F#6PAnyway, about the places\x01",
            "they're deployed...\x02\x03",
            "#00201FAs suspected, they're\x01",
            "protecting those Great\x01",
            "Bells, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#03903F#5PIt's highly likely.\x02\x03",
            "#03900FI have been privately\x01",
            "researching those\x01",
            "Artifact-like Great Bells.\x02\x03",
            "If I figure something out,\x01",
            "I'll let you know.\x02",
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
        "#00011F#6PR-Really!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10402F#12PHuh...? Don't you think\x01",
            "you're being a little\x01",
            "generous?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#03903F#5PHmph... Now that things have come\x01",
            "to this, I've grown a bit angry.\x02\x03",
            "#03901FThere's that Novartis brat to\x01",
            "deal with, too.\x02\x03",
            "And the fact that Arc-en-Ciel,\x01",
            "who I've been collaborating with,\x01",
            "has been made a mess of as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#10708F#12PAh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#6PNow that you mention it...\x01",
            "The stage setting and the\x01",
            "automatas were all broken.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#03903F#5PYes, I'll remake all of them.\x02\x03",
            "#03901FIn that sense, it's personally hard to\x01",
            "forgive the head of the Crois clan who\x01",
            "employed Red Constellation...\x02\x03",
            "#03903FThe Crois daughter is a passionate\x01",
            "collector of my dolls, I suppose... But\x01",
            "this and that are separate matters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10404F#12PHehe, I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#6P... I understand. Honestly,\x01",
            "you're really a big help.\x02\x03",
            "#00000FIf you figure out something\x01",
            "about the Great Bells, by\x01",
            "all means, contact us.\x02",
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

    # Function_24_37FB end

    SaveToFile()

Try(main)
