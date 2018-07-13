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
        "Function_3_3274",         # 03, 3
        "Function_4_32B3",         # 04, 4
        "Function_5_3316",         # 05, 5
        "Function_6_33A3",         # 06, 6
        "Function_7_342F",         # 07, 7
        "Function_8_3479",         # 08, 8
        "Function_9_34B3",         # 09, 9
        "Function_10_34F3",        # 0A, 10
        "Function_11_353D",        # 0B, 11
        "Function_12_3577",        # 0C, 12
        "Function_13_35B7",        # 0D, 13
        "Function_14_3601",        # 0E, 14
        "Function_15_363B",        # 0F, 15
        "Function_16_367B",        # 10, 16
        "Function_17_36C5",        # 11, 17
        "Function_18_36FF",        # 12, 18
        "Function_19_373F",        # 13, 19
        "Function_20_3789",        # 14, 20
        "Function_21_37C3",        # 15, 21
        "Function_22_3803",        # 16, 22
        "Function_23_384D",        # 17, 23
        "Function_24_3887",        # 18, 24
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
            "Thus, Lloyd and the others,\x01",
            "lead by the automata guide...\x02\x03",
            "Were guided to the underground studio\x01",
            "section, intricated like a maze.\x07\x00\x02",
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

    def lambda_674():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_674)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)

    def lambda_689():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_689)
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

    def lambda_769():
        OP_93(0x101, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_769)
    Sleep(50)

    def lambda_779():
        OP_93(0x102, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_779)
    Sleep(50)

    def lambda_789():
        OP_93(0x103, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_789)
    Sleep(50)

    def lambda_799():
        OP_93(0x104, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_799)
    Sleep(50)

    def lambda_7A9():
        OP_93(0x109, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_7A9)
    Sleep(50)

    def lambda_7B9():
        OP_93(0x105, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_7B9)
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
            "#10301F#6P#NCould it be...\x01",
            "The giant doll you were talking about?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00006F#6P#NYeah...\x01",
            "It's the "Pater-Mater"\x01",
            "Renne was using...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        "#00108F#6P#NSo it's been kept here...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#00306F#6P#NStill, to think that there was such\x01",
            "a place underground the mansion...\x02",
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
            "#00208F#11PThere are also some orbal net\x01",
            "computer-like things...\x02\x03",
            "#00201F...Could "Kitty" have hacked\x01",
            "the net wirelessly from here...?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x9,
        "Elderly Voice",
        "──So, what do you need?\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_AEC():
        TurnDirection(0x101, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_AEC)
    Sleep(50)

    def lambda_AFC():
        TurnDirection(0x102, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_AFC)
    Sleep(50)

    def lambda_B0C():
        TurnDirection(0x103, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_B0C)
    Sleep(50)

    def lambda_B1C():
        TurnDirection(0x104, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_B1C)
    Sleep(50)

    def lambda_B2C():
        TurnDirection(0x109, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_B2C)
    Sleep(50)

    def lambda_B3C():
        TurnDirection(0x105, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_B3C)
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 4)), scpexpr(EXPR_END)), "loc_C5D")

    ChrTalk(
        0x101,
        (
            "#00003F#5PUhhm...\x01",
            "Thank you very much\x01",
            "for sparing time for us.\x02\x03",
            "#00001FActually, we have a few things\x01",
            "we would like to ask you...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D4D")

    label("loc_C5D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x30, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_CE1")

    ChrTalk(
        0x101,
        (
            "#00003F#5PUhhm...\x01",
            "It has been a long time.\x02\x03",
            "#00001FActually, we have a few things\x01",
            "we would like to ask you...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D4D")

    label("loc_CE1")


    ChrTalk(
        0x101,
        (
            "#00006F#5PUhhm...\x01",
            "Nice to meet you.\x02\x03",
            "#00001FActually, we have a few things\x01",
            "we would like to ask you...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D4D")


    ChrTalk(
        0x9,
        (
            "#03903F#12PHmph...\x02\x03",
            "#03900FPerhaps, about what Campanella\x01",
            "has been meddling into?\x02",
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
        "#00013F#5P...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00301F#5POld man...\x02",
    )

    CloseMessageWindow()
    OP_93(0x9, 0x1E, 0x1F4)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x30, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_F4E")

    ChrTalk(
        0x9,
        (
            "#03903F#6P──Don't get me wrong.\x02\x03",
            "#03900FIt's true that I'm connected to the "Society",\x01",
            "but after all, I'm a mere doll maker.\x02\x03",
            "It's not that I'm directly involved\x01",
            "in the "Society" plan itself.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1035")

    label("loc_F4E")


    ChrTalk(
        0x9,
        (
            "#03903F#6P──Don't get me wrong.\x02\x03",
            "#03900FLike you have heard from Renne,\x01",
            "It's true that I'm connected to the "Society",\x01",
            "but after all, I'm a mere doll maker.\x02\x03",
            "It's not that I'm directly involved\x01",
            "in the "Society" plan itself.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1035")


    ChrTalk(
        0x101,
        (
            "#00006F#5PT-Then...\x02\x03",
            "#00001FYou don't know what\x01",
            "that boy, Campanella,\x01",
            "is trying to do...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#03900F#6PI don't, nor I'm in a position to know.\x02\x03",
            "#03903FHowever...\x01",
            "He isn't an "Anguis", but an "Enforcer".\x02\x03",
            "He virtually isn't in a position to propose\x01",
            "a "plan" the "Society" would advance.\x02\x03",
            "#03901FWho schemes and drafts\x01",
            "those are only the "Anguis".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00101F#11PP-Please wait a moment...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F#11PS-Somehow this talk is too sudden\x01",
            "and I can't keep up with it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10305F#11PThis seems important inside information...\x01",
            "Can you simply talk about it like that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#03903F#6PUh uh...\x01",
            "It's not prohibited at all.\x02\x03",
            "#03900FAlso, there's a moderate number of people \x01",
            "who know about this kind of information.\x02\x03",
            "The Church, Guild and the major powers intelligence\x01",
            "agencies should've figured this out since long ago.\x02",
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
            "#00201F#5PNevertheless, you continue\x01",
            "to make dolls here...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#03903F#6PTo begin with, I'm in no position\x01",
            "to know all the "Society" details.\x02\x03",
            "#03900FFor instance, even the archaisms\x01",
            "are goods made from the technology\x01",
            "of many workshops other than here.\x02\x03",
            "So to speak, this is just one tail of\x01",
            "a giant "Snake" which has countless...\x02\x03",
            "#03903FThat's also a reason why\x01",
            "the Church and Guild don't\x01",
            "simply march in here.\x02",
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
            "#00303F#5PGettin' out info as necessary\x01",
            "instead of just exposin' them...\x02\x03",
            "#00300FI guess that's useful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#03903F#6PRight, and in addition to that,\x01",
            "even this studio has a "purpose".\x02\x03",
            "#03901FIn case you got an arrest warrant\x01",
            "and broke into here...\x02\x03",
            "What you could discover\x01",
            "is just an empty studio.\x02\x03",
            "Including the "Pater-Mater".\x02",
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
            "#03903F#6PUh uh, if you like, do yo want to\x01",
            "try to take me into custody now?\x02\x03",
            "#03900FMaybe this will be your only chance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#5P──No, we'll pass on it.\x02\x03",
            "#00001FIt really would seem better...\x01",
            "To only ask you things.\x02",
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
            "#10106FW#11P-Wait...\x01",
            "I can't really agree, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#03903F#6PUh uh, a wise decision.\x02\x03",
            "#03900FIt seems you have many specific\x01",
            "things you want to ask me, but...\x02\x03",
            "Narrow them down to three.\x01",
            "If I can answer them, I'll do.\x02",
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

    label("loc_1971")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E65")
    FadeToDark(300, 0, 100)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1A1C")

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[About the Society's "Anguis"]\x01",              # 0
            "[About the Society's "Plan"]\x01",                # 1
            "[About the relationship with the Cult]\x01",      # 2
            "[Quit Asking]\x01",                               # 3
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Jump("loc_1A8E")

    label("loc_1A1C")


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[About the Society's "Anguis"]\x01",              # 0
            "[About the Society's "Plan"]\x01",                # 1
            "[About the relationship with the Cult]\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)

    label("loc_1A8E")

    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_1ABA"),
        (0, "loc_1ED3"),
        (2, "loc_28D2"),
        (3, "loc_2E58"),
        (SWITCH_DEFAULT, "loc_2E60"),
    )


    label("loc_1ABA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E2F")

    ChrTalk(
        0x9,
        (
            "#03903F#6PLike I told you before,\x01",
            "I too don't know the details.\x02\x03",
            "However, according to what I've heard \x01",
            "by hearsay, it seems they call it...\x02\x03",
            "#03901F──"Phantasmal Blaze Plan".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#5P"Phantasmal Blaze Plan"...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10301F#11P...An abstruse name...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101F#11P...About that plan...\x01",
            "Is it to cause in Crossbell a phenomenon\x01",
            "like the Liberl one, one year ago?\x02",
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
            "#03903F#6PI repeat, I too don't know the details.\x02\x03",
            "#03900FHowever, if I can say one thing,\x01",
            "it doesn't seem something large-\x01",
            "scale like that of Liberl.\x02\x03",
            "First of all, the "Society" is a shady existence...\x01",
            "By nature, it doesn't show up on the front stage.\x02",
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
            "#00306F#5PRather, this can't make me\x01",
            "feel reassured at all...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00211F#5PIf anything, just the name \x01",
            "conversely stirs up unrest...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1ECE")

    label("loc_1E2F")


    ChrTalk(
        0x9,
        (
            "#03903F#6PI too don't know the outline.\x02\x03",
            "However, according to what I've heard \x01",
            "by hearsay, it seems they call it...\x02\x03",
            "#03901F──"Phantasmal Blaze Plan".\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1ECE")

    Jump("loc_2E60")

    label("loc_1ED3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_277C")
    Sleep(150)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(500)
    SetMessageWindowPos(280, 170, -1, -1)

    AnonymousTalk(
        0x9,
        (
            "#3C#30WThe "Anguis"──\x02\x03",
            "They're seven leaders who follow and\x01",
            "realize the "Grandmaster"'s plans.\x02\x03",
            "I too don't know all\x01",
            "of them in detail, but...\x02\x03",
            "I know the Anguis who are going\x01",
            "to come to Crossbell before long.\x02",
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
            "#00013F#5PT-Then...\x01",
            "What kind of persons are they?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#03900F#6P............\x02\x03",
            "#03903FOne is a man who, as the "6th Anguis", \x01",
            "supervises the "Thirteen Workshops",\x01",
            "which are the Society technology network.\x02\x03",
            "The Society most theoretician,\x01",
            "an extremely greedy engineer...\x02\x03",
            "#03901FWell, let's only say that\x01",
            "he's a nasty man.\x02",
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
        "#00206F#5P...You have a high opinion of him.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10101F#11PI-In what sense, "nasty"?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#03903F#6PFor better or worse, he's a man who only thinks\x01",
            "about satisfying his intellectual curiosity.\x02\x03",
            "I don't know with what aim he's\x01",
            "coming to Crossbell, but...\x02\x03",
            "#03901FI can at least surely say that nothing\x01",
            "good is going to come to Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108F#11P............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#5P...From what you told us, it\x01",
            "really seems to be nasty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#03903F#6P...Then, the other one...\x02\x03",
            "#03900FI know that the "7th Anguis", crowned with\x01",
            "the name of "Steel", is coming to Crossbell.\x02",
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
        "#00005F#5P"Steel"...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301F#5PSay guys...\x01",
            "Doesn't it ring a little dangerous?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#03903F#6PUh uh...a little mysterious person.\x02\x03",
            "#03900FIf I had to say one thing, that's\x01",
            "a master you'd be no match for\x01",
            "even if you attacked all together.\x02",
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
        "#00011F#5PEven all together we...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#11PEeh...\x01",
            "Aren't you quite confident?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#03903F#6PWell, consider it just a warning.\x02\x03",
            "Unlike the "6th Anguis", I heard the\x01",
            "7th is a person of high principles, but...\x02\x03",
            "#03901FIf faced ineptly, you'd end up\x01",
            "getting yourselves killed for sure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00013F#5P............\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_28CD")

    label("loc_277C")


    ChrTalk(
        0x9,
        (
            "#03903F#6PI don't know the full details, but I heard\x01",
            "that two "Anguis" are coming to Crossbell.\x02\x03",
            "#03900FOne is the "6th Anguis"──\x01",
            "A nasty engineer who supervises\x01",
            "the "Thirteen Workshops".\x02\x03",
            "The other one is the "7th Anguis"──\x01",
            "The strongest master who is named "Steel".\x02\x03",
            "#03903FWell, both of them are too\x01",
            "great opponents for you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28CD")

    Jump("loc_2E60")

    label("loc_28D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CF5")

    ChrTalk(
        0x9,
        (
            "#03903F#6PThe "D∴G Cult", eh?\x02\x03",
            "#03901FBased on what I know, it seems \x01",
            "they didn't have any direct ties.\x02\x03",
            "Although it's a fact that the "Society" \x01",
            "crushed the lodge where Renne was...\x02",
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
        "#00011F#5PEeh...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00101F#11PThe one that was called "Paradise"...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#03900F#6PHm, it appears it was a place to take advantage\x01",
            "of influential persons from all places.\x02\x03",
            "Perhaps it became subject to extermination\x01",
            "because it targeted influential persons who\x01",
            "had the "Society"'s backing.\x02\x03",
            "#03903FThe fact that Renne survived is nothing more\x01",
            "than what could be said to be a goddesssend.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00208F#5P............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#5PNevertheless, I can't really consider\x01",
            "the "Society" as somethin' upright...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10301F#11PHonestly, it's very unlikely you can persuade\x01",
            "us with just that explanation, you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#03903F#6PUh uh, didn't I tell you?\x01",
            ""Based on what I know".\x02\x03",
            "#03900FIt's up to you all how to judge it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2E53")

    label("loc_2CF5")


    ChrTalk(
        0x9,
        (
            "#03903F#6PThe "D∴G Cult"──\x01",
            "Based on what I know, it seems they didn't \x01",
            "have any direct ties with the "Society".\x02\x03",
            "#03900FAlthough it's a fact that the "Society" \x01",
            "crushed the lodge where Renne was...\x02\x03",
            "It could've been nothing more than a subject\x01",
            "for extermination after influential persons who\x01",
            "had the "Society"'s backing got involved with it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E53")

    Jump("loc_2E60")

    label("loc_2E58")

    SetScenarioFlags(0x0, 3)
    Jump("loc_2E60")

    label("loc_2E60")

    Jump("loc_1971")

    label("loc_2E65")


    ChrTalk(
        0x9,
        (
            "#03900F#6PHm, it makes three with this one, right?\x02\x03",
            "#03903F──You took a lot of time from me.\x01",
            "Could you retire now?\x02",
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
        "#10108F#11PM-Mr. Lloyd...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00006F#5P──That was our agreement.\x01",
            "We'll leave here, this time.\x02\x03",
            "#00000FDo you mind if, having the chance,\x01",
            "we come to ask you something again?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#03903F#6PWell, if I feel inclined.\x02\x03",
            "#03901FBut first of all, you shouldn't\x01",
            "concern yourselves only with us.\x02\x03",
            "Shouldn't you have a few other forces \x01",
            "you must watch out due to that \x01",
            ""state independence" or whatever?\x02",
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
            "#10302F#11PYou seem to know all those\x01",
            "forces' movements, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#03903F#6PUh uh, I wonder.\x02",
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
            "#03900F#6P──Now go, stick close to that\x01",
            "little one even when returning.\x02\x03",
            "If you stray from her, I can't\x01",
            "guarantee your safety, you know?\x02",
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

    def Function_3_3274(): pass

    label("Function_3_3274")

    OP_95(0xFE, 0, 0, 102000, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    StopSound(957, 300, 30)
    Sleep(1000)
    Sound(957, 2, 40, 0)
    OP_95(0xFE, -21450, 0, 102000, 2000, 0x0)
    Return()

    # Function_3_3274 end

    def Function_4_32B3(): pass

    label("Function_4_32B3")

    Sound(957, 2, 40, 0)

    def lambda_32BE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_32BE)
    OP_95(0xFE, 0, 0, 5000, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    StopSound(957, 300, 30)
    Sleep(1000)
    Sound(957, 2, 40, 0)
    OP_95(0xFE, -2750, 0, 6300, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    StopSound(957, 300, 30)
    Return()

    # Function_4_32B3 end

    def Function_5_3316(): pass

    label("Function_5_3316")

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

    # Function_5_3316 end

    def Function_6_33A3(): pass

    label("Function_6_33A3")

    OP_68(0, 600, 101000, 7000)
    SetCameraDistance(22000, 7000)
    OP_95(0xFE, 0, 0, 100000, 2000, 0x0)

    def lambda_33D6():

        label("loc_33D6")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_33D6")

    QueueWorkItem2(0xFE, 2, lambda_33D6)
    Sleep(2000)
    EndChrThread(0xFE, 0x2)
    OP_68(-10000, 600, 102000, 8000)
    MoveCamera(40, 20, 0, 8000)
    OP_95(0xFE, -2000, 0, 102000, 2000, 0x0)
    OP_95(0xFE, -21450, 0, 102000, 2000, 0x0)
    Return()

    # Function_6_33A3 end

    def Function_7_342F(): pass

    label("Function_7_342F")


    def lambda_3434():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3434)
    OP_95(0xFE, 0, 0, 2500, 2000, 0x0)

    label("loc_3454")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3478")
    OP_93(0xFE, 0x87, 0x1F4)
    Sleep(1500)
    OP_93(0xFE, 0xE1, 0x1F4)
    Sleep(1500)
    Jump("loc_3454")

    label("loc_3478")

    Return()

    # Function_7_342F end

    def Function_8_3479(): pass

    label("Function_8_3479")

    TurnDirection(0xFE, 0x9, 500)
    Sleep(100)
    OP_95(0xFE, -3450, 0, -500, 2000, 0x0)
    OP_95(0xFE, -6500, -250, -1500, 2000, 0x0)
    OP_93(0xFE, 0xD2, 0x1F4)
    Return()

    # Function_8_3479 end

    def Function_9_34B3(): pass

    label("Function_9_34B3")

    OP_95(0xFE, 500, 0, 99500, 2000, 0x0)
    Sleep(2000)
    OP_95(0xFE, -2000, 0, 102500, 2000, 0x0)
    OP_95(0xFE, -21450, 0, 102500, 2000, 0x0)
    Return()

    # Function_9_34B3 end

    def Function_10_34F3(): pass

    label("Function_10_34F3")


    def lambda_34F8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_34F8)
    OP_95(0xFE, 750, 0, 3500, 2000, 0x0)

    label("loc_3518")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_353C")
    OP_93(0xFE, 0x87, 0x1F4)
    Sleep(1500)
    OP_93(0xFE, 0x5A, 0x1F4)
    Sleep(1500)
    Jump("loc_3518")

    label("loc_353C")

    Return()

    # Function_10_34F3 end

    def Function_11_353D(): pass

    label("Function_11_353D")

    TurnDirection(0xFE, 0x9, 500)
    Sleep(200)
    OP_95(0xFE, -3450, 0, -1000, 2000, 0x0)
    OP_95(0xFE, -5500, -250, -1150, 2000, 0x0)
    OP_93(0xFE, 0xD2, 0x1F4)
    Return()

    # Function_11_353D end

    def Function_12_3577(): pass

    label("Function_12_3577")

    OP_95(0xFE, -750, 0, 99000, 2000, 0x0)
    Sleep(2100)
    OP_95(0xFE, -2000, 0, 101250, 2000, 0x0)
    OP_95(0xFE, -21450, 0, 101250, 2000, 0x0)
    Return()

    # Function_12_3577 end

    def Function_13_35B7(): pass

    label("Function_13_35B7")


    def lambda_35BC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_35BC)
    OP_95(0xFE, -1000, 0, 3000, 2000, 0x0)

    label("loc_35DC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3600")
    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(1500)
    OP_93(0xFE, 0xE1, 0x1F4)
    Sleep(1500)
    Jump("loc_35DC")

    label("loc_3600")

    Return()

    # Function_13_35B7 end

    def Function_14_3601(): pass

    label("Function_14_3601")

    TurnDirection(0xFE, 0x9, 500)
    Sleep(500)
    OP_95(0xFE, -3450, 0, 500, 2000, 0x0)
    OP_95(0xFE, -6650, -250, -300, 2000, 0x0)
    OP_93(0xFE, 0xD2, 0x1F4)
    Return()

    # Function_14_3601 end

    def Function_15_363B(): pass

    label("Function_15_363B")

    OP_95(0xFE, 0, 0, 98000, 2000, 0x0)
    Sleep(2000)
    OP_95(0xFE, -2000, 0, 102000, 2000, 0x0)
    OP_95(0xFE, -21450, 0, 102000, 2000, 0x0)
    Return()

    # Function_15_363B end

    def Function_16_367B(): pass

    label("Function_16_367B")


    def lambda_3680():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3680)
    OP_95(0xFE, -250, 0, 4000, 2000, 0x0)

    label("loc_36A0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_36C4")
    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(1500)
    OP_93(0xFE, 0x5A, 0x1F4)
    Sleep(1500)
    Jump("loc_36A0")

    label("loc_36C4")

    Return()

    # Function_16_367B end

    def Function_17_36C5(): pass

    label("Function_17_36C5")

    TurnDirection(0xFE, 0x9, 500)
    Sleep(400)
    OP_95(0xFE, -3450, 0, -500, 2000, 0x0)
    OP_95(0xFE, -5450, -250, 300, 2000, 0x0)
    OP_93(0xFE, 0xD2, 0x1F4)
    Return()

    # Function_17_36C5 end

    def Function_18_36FF(): pass

    label("Function_18_36FF")

    OP_95(0xFE, 750, 0, 97250, 2000, 0x0)
    Sleep(2100)
    OP_95(0xFE, -2000, 0, 102250, 2000, 0x0)
    OP_95(0xFE, -21450, 0, 102250, 2000, 0x0)
    Return()

    # Function_18_36FF end

    def Function_19_373F(): pass

    label("Function_19_373F")


    def lambda_3744():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3744)
    OP_95(0xFE, 500, 0, 5500, 2000, 0x0)

    label("loc_3764")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3788")
    OP_93(0xFE, 0x87, 0x1F4)
    Sleep(1500)
    OP_93(0xFE, 0xE1, 0x1F4)
    Sleep(1500)
    Jump("loc_3764")

    label("loc_3788")

    Return()

    # Function_19_373F end

    def Function_20_3789(): pass

    label("Function_20_3789")

    TurnDirection(0xFE, 0x9, 500)
    Sleep(500)
    OP_95(0xFE, -3450, 0, -1000, 2000, 0x0)
    OP_95(0xFE, -4250, 0, -850, 2000, 0x0)
    OP_93(0xFE, 0xD2, 0x1F4)
    Return()

    # Function_20_3789 end

    def Function_21_37C3(): pass

    label("Function_21_37C3")

    OP_95(0xFE, 1250, 0, 98500, 2000, 0x0)
    Sleep(2000)
    OP_95(0xFE, -2000, 0, 102750, 2000, 0x0)
    OP_95(0xFE, -21450, 0, 102750, 2000, 0x0)
    Return()

    # Function_21_37C3 end

    def Function_22_3803(): pass

    label("Function_22_3803")


    def lambda_3808():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3808)
    OP_95(0xFE, -1000, 0, 4500, 2000, 0x0)

    label("loc_3828")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_384C")
    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(1500)
    OP_93(0xFE, 0x13B, 0x1F4)
    Sleep(1500)
    Jump("loc_3828")

    label("loc_384C")

    Return()

    # Function_22_3803 end

    def Function_23_384D(): pass

    label("Function_23_384D")

    TurnDirection(0xFE, 0x9, 500)
    Sleep(1000)
    OP_95(0xFE, -3450, 0, 500, 2000, 0x0)
    OP_95(0xFE, -4300, 0, 500, 2000, 0x0)
    OP_93(0xFE, 0xD2, 0x1F4)
    Return()

    # Function_23_384D end

    def Function_24_3887(): pass

    label("Function_24_3887")

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
            "──Hm.\x01",
            "Rare guests show up too.\x02\x03",
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
            "#3CYes it's been, child of man.\x02\x03",
            "It looks that you too\x01",
            "have aged quite a lot.\x02\x03",
            "It appears you're involved with\x01",
            "the "Snake" folks as always.\x02",
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
            "#03903F#11PUh uh, ties are things that follow you\x01",
            "around even not in an earthly life.\x02\x03",
            "#03900FThe "oath" that binds you\x01",
            "is a similar thing, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#01201F#6P#3CHa ha, for certain.\x02",
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
            "#00211F#6P(Somehow it appears they are talking\x01",
            "about an extremely old story...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#6P(Yeah, I can't think it's a conversation\x01",
            "about our same society...)\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x9, 0xE1, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x9,
        (
            "#03903F#5PIn any case, a Gralsritter Dominion\x01",
            "and the Demon of the Eastern District\x01",
            "who tried to infiltrate in here...\x02\x03",
            "#03900FQuite the eccentric ensemble\x01",
            "of people we have here, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10402F#12PHu hu, indeed.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#10710F#6P...I apologise for before.\x02",
    )

    CloseMessageWindow()
    Sleep(150)

    ChrTalk(
        0x101,
        (
            "#00006F#6P──Meister Jｶrg.\x02\x03",
            "#00001FLike we told you, we're\x01",
            "currently moving to do\x01",
            "something about this situation.\x02\x03",
            "Don't you know anything...?\x01",
            "Especially about the "Society" actions...\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x9, 0x10E, 0x1F4)
    Sleep(150)

    ChrTalk(
        0x9,
        (
            "#03900F#11PHm...\x02\x03",
            "#03903F──You might already know it, but this time,\x01",
            "the "Society" position is nothing more than\x01",
            "to cooperate to the Crois clan goals.\x02\x03",
            "It appear that the "Society" plan── the "Phantasmal\x01",
            "Blaze Plan" has already moved to the next stage.\x02\x03",
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
            "#10406F#12PIn practice, the other Anguis and Enforcers\x01",
            "have already begun to move over there.\x02\x03",
            "#10401FThat's also the reason why\x01",
            "we Knights couldn't spare that\x01",
            "much war potential in Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008F#6PIs that so...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#6P...It seems that too many things\x01",
            "are happening all over Zemuria.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#03903F#11PHowever, three extremely troublesome\x01",
            "persons still remain in Crossbell.\x02\x03",
            "#03901FThey're also prominent figures\x01",
            "among the Society.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#6PCampanella "The Fool"...\x02\x03",
            "#00013FAnd the "Anguis": the\x01",
            "doctor called Novartis, and\x01",
            "the woman called Arianrhod.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10708F#6P............\x02\x03",
            "#10706FWho in the world is that woman?\x02\x03",
            "#10701FThose movements and reactions──\x01",
            "I can't think they're something human at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#03903F#11PI too don't know the details.\x02\x03",
            "However,  she's known in the "Society"\x01",
            "as a terrific lance wielder and as a\x01",
            "person with a strong moral code.\x02\x03",
            "#03900FIt is said that all the walkｸres who\x01",
            "follow her were not only discovered\x01",
            "by her, but she's also trained them.\x02\x03",
            "It seems that each of them has a strength\x01",
            "that can rival that of an "Enforcer".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00205F#6PJust like that Miss Renne...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10403F#12PWell, it appears that the strength of an\x01",
            ""Enforcer" is not only fighting related...\x02\x03",
            "#10408FNevertheless, even six troublesome\x01",
            "enemies are working together, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F#6P...However, they're only\x01",
            "cooperating together.\x02\x03",
            "#00001FDepending on the circumstances, isn't it \x01",
            "possible that they won't involve themselves\x01",
            "further with the situation in Crossbell?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#03900F#11PHm, it could be.\x02\x03",
            "#03903FAlthough that greenhorn of Novartis seems\x01",
            "to be extremely interested into the dolls\x01",
            "that received the "Sept-Terrion" power.\x02\x03",
            "#03901FIn any event, with the information I have\x01",
            "I don't know what their future plans are.\x02",
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
            "#00206F#6PIt seems we won't be able to deal\x01",
            "with them with ordinary means.\x02\x03",
            "#00200F...By the way, there is something that\x01",
            "has been on my mind since before...\x02",
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
            "#00200F#6PAre you currently repairing\x01",
            "the "Pater-Mater"?\x02",
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
            "#03903F#5PWell, it's just mere\x01",
            "maintenance.\x02\x03",
            "That greenhorn of Novartis was\x01",
            "quite fond of this machine.\x02\x03",
            "#03901FHe's currently focused on the new dolls,\x01",
            "so I think there's nothing to worry, but...\x02\x03",
            "In case he comes to steal it, I'm just\x01",
            "preparing it so it can run away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F#6PI-I understand.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10404F#12PSo in case of emergency he'll be able to go \x01",
            "to Liberl, where the "Angel of Slaughter" is.\x02\x03",
            "#10400FAnyway, based on what I'm hearing,\x01",
            "you don't get along at all with that doctor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#03903F#5PHmph, I won't deny it.\x02\x03",
            "Originally, this "Gordias-class" was an\x01",
            "invention I gave my all to develop.\x02\x03",
            "#03900FHe took it away in the middle of it and\x01",
            "gave it to a little kid like Renne and in the\x01",
            "end he even did inhuman connection tests...\x02\x03",
            "Although the connection was somehow a success, \x01",
            "the tests itselves are an unforgivable act.\x02",
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
            "#00206F#6P...Virtually the same of the\x01",
            "experiments the Cult did.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#03903F#5PEven more, he developed on his own its\x01",
            "successor unit that can't even operate\x01",
            "satisfactorily without a Sept-Terrion...\x02\x03",
            "And the shamelessness to\x01",
            "impudently call it the "final\x01",
            "model" of the "Gordias-class"...!\x02\x03",
            "#03901FWhen he was here I was about\x01",
            "to strangle that ewe-neck of his...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012F#6PI-Is that so...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#01203F#6P#3CNow, calm down.\x02\x03",
            "#01200FAs always, it appears that you can't stay\x01",
            "calm when it comes to your creations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#03903F#5P*cough*...\x01",
            "Well, be that as it may...\x02\x03",
            "#03900FAlthough he's really brazen and unscrupulous,\x01",
            "it's true that he has a prodigy-like brain for\x01",
            "practical use and strengthening technologies.\x02\x03",
            "I heard that above remodeling and\x01",
            "powering up the archaism I developed,\x01",
            "he even mass produced it.\x02\x03",
            "According to rumors, it seems\x01",
            "that those units have been deployed\x01",
            "at the "Tower", "Temple" and so on.\x02",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AF, 4)), scpexpr(EXPR_END)), "loc_529A")

    ChrTalk(
        0x105,
        "#10401F#12PThe one that was in front of the Tower...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#6P...It's true that it\x01",
            "looked very strong...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_52DE")

    label("loc_529A")


    ChrTalk(
        0x101,
        "#00001F#6PI see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10403F#12P...That's the first I hear.\x02",
    )

    CloseMessageWindow()

    label("loc_52DE")


    ChrTalk(
        0x103,
        (
            "#00208F#6PAnyway, about the places where\x01",
            "they have been deployed...\x02\x03",
            "#00201FAs suspected, they are protecting\x01",
            "those "big bells", am I right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#03903F#5PIt's very likely.\x02\x03",
            "#03900FI too have been researching\x01",
            "about those Artifacts-like \x01",
            ""big bells" privately.\x02\x03",
            "If I figure something out,\x01",
            "I'll let you know too.\x02",
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
            "#10402F#12PEeh...?\x01",
            "Don't you think you're too much generous?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#03903F#5PHmph... I too am a little angry\x01",
            "about the recent facts.\x02\x03",
            "#03901FThere's that greenhorn of Novartis too, but...\x02\x03",
            "There's also the fact that the "Arc-en-ciel" I was \x01",
            "collaborating with has been made a mess of.\x02",
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
            "It seems that the stage settings and\x01",
            "the automatas too were all broken.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#03903F#5PHm, I'll remake all of that.\x02\x03",
            "#03901FIn that sense, it's personally hard to forgive\x01",
            "the head of the Crois clan who employed the\x01",
            ""Red Constellation" or whatever it's called.\x02\x03",
            "#03903FIt seems that the daughter is a\x01",
            "passionate collector of my dolls, but...\x01",
            "This and that are two different matters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10404F#12PHu hu, I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#6P...I understand.\x01",
            "Honestly, you're really a big help.\x02\x03",
            "#00000FIf you figure out something about the\x01",
            ""big bells", by all means, contact us.\x02",
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

    # Function_24_3887 end

    SaveToFile()

Try(main)
