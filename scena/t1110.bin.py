from ScenarioHelper import *

def main():
    CreateScenaFile(
        "t1110.bin",                # FileName
        "t1110",                    # MapName
        "t1110",                    # Location
        0x0000,                     # MapIndex
        "ed7000",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x1A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    )

    BuildStringList((
        "t1110",                  # 0
        "voice",                   # 1
        "voice",                   # 2
        "voice",                   # 3
        "Erie",                 # 4
        "McDowell",         # 5
        "Yona",                   # 6
        "SE control",                 # 7
        "bt1110",                 # 8
    ))

    ATBonus("ATBonus_188", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_248", 8, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_24C", 3, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_250", 13, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_254", 3, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_258", 13, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_25C", 6, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_260", 10, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_264", 8, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_228", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_22C", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_230", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_234", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_238", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_23C", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_240", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_244", 5, 5, 45)

    # monster count: 0

    # event battle count: 1

    BattleInfo(
        "BattleInfo_268", 0x0052, 255, 6, 45, 3, 3, 30, 0, "bt1110", 0x00000000, 100, 0, 0, 0,
        (
            ("ms84000.dat", "ms84500.dat", "ms84500.dat", 0, 0, 0, "ms84500.dat", 0, "MonsterBattlePostion_248", "MonsterBattlePostion_228", "ed7451", "ed7453", "ATBonus_188"),
            (),
            (),
            (),
        )
    )

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(852, 0)                                        # 0

    ScpFunction((
        "Function_0_354",          # 00, 0
        "Function_1_375",          # 01, 1
        "Function_2_38E",          # 02, 2
        "Function_3_D24",          # 03, 3
        "Function_4_D49",          # 04, 4
        "Function_5_DAA",          # 05, 5
        "Function_6_E91",          # 06, 6
        "Function_7_EEC",          # 07, 7
        "Function_8_F3B",          # 08, 8
        "Function_9_F5A",          # 09, 9
        "Function_10_F76",         # 0A, 10
        "Function_11_F92",         # 0B, 11
        "Function_12_2FBA",        # 0C, 12
        "Function_13_3022",        # 0D, 13
        "Function_14_3067",        # 0E, 14
        "Function_15_30A5",        # 0F, 15
        "Function_16_30CF",        # 10, 16
        "Function_17_30EB",        # 11, 17
        "Function_18_30FD",        # 12, 18
        "Function_19_310F",        # 13, 19
        "Function_20_3207",        # 14, 20
        "Function_21_326D",        # 15, 21
        "Function_22_3291",        # 16, 22
        "Function_23_32DC",        # 17, 23
        "Function_24_3812",        # 18, 24
        "Function_25_3858",        # 19, 25
        "Function_26_3880",        # 1A, 26
        "Function_27_38A8",        # 1B, 27
        "Function_28_38E8",        # 1C, 28
        "Function_29_3910",        # 1D, 29
        "Function_30_3971",        # 1E, 30
        "Function_31_39D2",        # 1F, 31
        "Function_32_3A33",        # 20, 32
        "Function_33_3A94",        # 21, 33
        "Function_34_3AF5",        # 22, 34
        "Function_35_3DBA",        # 23, 35
        "Function_36_3E76",        # 24, 36
        "Function_37_3EEF",        # 25, 37
        "Function_38_4159",        # 26, 38
        "Function_39_4188",        # 27, 39
        "Function_40_41B7",        # 28, 40
        "Function_41_41D0",        # 29, 41
    ))


    def Function_0_354(): pass

    label("Function_0_354")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_365")
    Event(0, 2)

    label("loc_365")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_374")
    ClearScenarioFlags(0x22, 0)
    Event(0, 11)

    label("loc_374")

    Return()

    # Function_0_354 end

    def Function_1_375(): pass

    label("Function_1_375")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_387")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0xFB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_387")

    Sound(124, 1, 50, 0)
    Return()

    # Function_1_375 end

    def Function_2_38E(): pass

    label("Function_2_38E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00250.itc", 0x1F)
    LoadChrToIndex("chr/ch00350.itc", 0x20)
    LoadChrToIndex("chr/ch02950.itc", 0x21)
    LoadChrToIndex("chr/ch03150.itc", 0x22)
    LoadChrToIndex("chr/ch03250.itc", 0x23)
    LoadChrToIndex("monster/ch84050.itc", 0x24)
    LoadChrToIndex("monster/ch84051.itc", 0x25)
    LoadChrToIndex("monster/ch84052.itc", 0x26)
    LoadChrToIndex("monster/ch84550.itc", 0x27)
    LoadEffect(0x0, "event\\ev502_00.eff")
    SoundLoad(950)
    SoundLoad(825)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, -500, 500, 13500, 0)
    SetChrPos(0x104, 500, 500, 13500, 0)
    SetChrPos(0x103, -500, 500, 12000, 0)
    SetChrPos(0x105, 500, 500, 12000, 0)
    SetChrPos(0x106, -1500, 500, 12750, 0)
    SetChrPos(0x109, 1500, 500, 13050, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 0x24)
    SetChrSubChip(0x8, 0x0)
    OP_52(0x8, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xE4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 0, 1500, 23000, 180)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x8, 0x1)
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0xAF0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x9, 0x80)
    SetChrChipByIndex(0x9, 0x27)
    SetChrSubChip(0x9, 0x0)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, -4000, 500, 21000, 135)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xA, 0x27)
    SetChrSubChip(0xA, 0x0)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 4000, 500, 21000, 225)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(320, 2500, 18250, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(21500, 0)
    FadeToBright(1000, 0)
    OP_68(320, 1500, 18250, 4000)

    def lambda_55D():
        OP_9B(0x0, 0x101, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_55D)
    Sleep(30)

    def lambda_575():
        OP_9B(0x0, 0x103, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_575)
    Sleep(30)

    def lambda_58D():
        OP_9B(0x0, 0x104, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_58D)
    Sleep(30)

    def lambda_5A5():
        OP_9B(0x0, 0x105, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_5A5)
    Sleep(30)

    def lambda_5BD():
        OP_9B(0x0, 0x109, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_5BD)
    Sleep(30)

    def lambda_5D5():
        OP_9B(0x0, 0x106, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_5D5)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x106, 0)
    OP_6F(0x79)
    OP_0D()
    Fade(1000)
    OP_68(320, 1500, 18250, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#00008F#11PThere's no one here?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10708F#12PHouse……\x01",
            "I feel a sign of something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10401F#12PHmm, it is a kind of devil\x01",
            "I do not think so.\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0x1388)
    ReplaceBGM("ed7251", -1)
    ReplaceBGM("ed7565", -1)
    OP_68(0, 3300, 21000, 1500)
    MoveCamera(45, 15, 0, 1500)
    OP_6E(600, 1500)
    SetCameraDistance(15000, 1500)
    OP_6F(0x79)
    Sound(903, 0, 100, 0)
    SetMessageWindowPos(70, 60, -1, -1)

    AnonymousTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "P---Confirmed intruders\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
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
    Sleep(50)
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(500)
    BeginChrThread(0x8, 0, 0, 3)
    Sound(825, 2, 30, 0)
    Sleep(500)

    ChrTalk(
        0x103,
        "#00207F#11PReaction straight ahead!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00310F#11PChit\x01",
            "The people#4R噵 噵#What is it!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7451", 0)
    Fade(500)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    SetCameraDistance(14000, 500)
    BeginChrThread(0x8, 3, 0, 4)
    Sound(950, 2, 100, 0)
    OP_6F(0x79)
    CancelBlur(500)
    OP_0D()
    EndChrThread(0x8, 0x3)
    StopEffect(0x0, 0x2)
    BeginChrThread(0x8, 3, 0, 5)
    WaitChrThread(0x8, 3)
    OP_6F(0x79)
    CancelBlur(500)
    OP_0D()
    Sleep(1500)
    Fade(500)
    OP_68(390, 2600, 19220, 0)
    MoveCamera(331, 20, 0, 0)
    MoveCamera(0, 15, 0, 10000)
    OP_6E(600, 0)
    SetCameraDistance(12220, 0)
    OP_0D()
    Sleep(500)
    Fade(250)
    Sound(805, 0, 100, 0)
    Sound(531, 0, 100, 0)
    Sound(541, 0, 30, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x103, 0x1F)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x20)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x21)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x22)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x106, 0x23)
    SetChrSubChip(0x106, 0x0)
    OP_0D()
    Sound(903, 0, 100, 0)
    SetMessageWindowPos(270, 90, -1, -1)

    AnonymousTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "6 Intruders\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "3 persons in charge of special affairs support section,\x01",
            "Confirm the Defense Force Seeker lieutenant.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Two are unknown ─ ─ however, the combat strength is\x01",
            "I guess that it is over A rank.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x105,
        "#10407F#12P#NTch…\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x106,
        "#10707F#6P#NA machine could learn that much?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-590, 2300, 19970, 0)
    MoveCamera(41, 15, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(13440, 0)
    OP_68(-590, 2300, 19970, 0)
    MoveCamera(41, 15, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(13000, 0)
    SetCameraDistance(14000, 1500)
    BeginChrThread(0x8, 3, 0, 3)
    BeginChrThread(0x9, 3, 0, 6)
    BeginChrThread(0xA, 3, 0, 7)
    Sound(825, 2, 30, 0)
    OP_6F(0x79)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
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
    Sleep(50)
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    WaitChrThread(0x9, 3)
    WaitChrThread(0xA, 3)
    EndChrThread(0x8, 0x3)
    Sound(903, 0, 100, 0)
    SetMessageWindowPos(50, 100, -1, -1)

    AnonymousTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Izayoi is here\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Legenenkov type,\x01",
            "\"Muramasa\" ──\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Activating combat mode\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        "#00010F#12P#NIt's coming!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x109,
        "#10107F#12P#NPrepare for battle!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EndChrThread(0x8, 0x0)
    Sound(905, 0, 100, 0)
    StopSound(825, 1000, 30)
    SetChrChipByIndex(0x8, 0x26)
    SetChrSubChip(0x8, 0x0)
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0xAF0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A1(0x8, 0x3E8, 0x2, 0x0, 0x1)
    Sleep(750)
    Sound(951, 0, 100, 0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_68(-610, 2300, 19190, 500)
    SetCameraDistance(9500, 500)
    SetChrSubChip(0x8, 0x2)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x9, 0x20)
    SetChrFlags(0xA, 0x20)
    SetChrFlags(0x8, 0x1000)
    SetChrFlags(0x9, 0x1000)
    SetChrFlags(0xA, 0x1000)
    SetChrChip(0x0, 0x8, 0x64, 0x1F4)
    SetChrChip(0x0, 0x9, 0x64, 0x1F4)
    SetChrChip(0x0, 0xA, 0x64, 0x1F4)

    def lambda_C97():
        OP_9B(0x1, 0xFE, 0x0, 0xBB8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_C97)

    def lambda_CAC():
        OP_9B(0x1, 0xFE, 0x0, 0xBB8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_CAC)

    def lambda_CC1():
        OP_9B(0x1, 0xFE, 0x0, 0xBB8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_CC1)
    Sleep(500)
    EndChrThread(0x8, 0x1)
    EndChrThread(0x9, 0x1)
    EndChrThread(0xA, 0x1)
    EndChrThread(0x9, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrChip(0x1, 0x8, 0x0, 0x0)
    SetChrChip(0x1, 0x9, 0x0, 0x0)
    SetChrChip(0x1, 0xA, 0x0, 0x0)
    OP_24(0x3B6)
    OP_24(0x339)
    Battle("BattleInfo_268", 0x0, 0x0, 0x100, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    Call(0, 11)
    Return()

    # Function_2_38E end

    def Function_3_D24(): pass

    label("Function_3_D24")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D48")
    OP_82(0x0, 0x1E, 0x1388, 0x3E8)
    Sleep(1000)
    Jump("Function_3_D24")

    label("loc_D48")

    Return()

    # Function_3_D24 end

    def Function_4_D49(): pass

    label("Function_4_D49")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_DA9")
    PlayEffect(0x0, 0x0, 0xFE, 0x1, 0, 1500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x96, 0x2EE)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xC8, 0x2EE)
    StopEffect(0x0, 0x2)
    Jump("Function_4_D49")

    label("loc_DA9")

    Return()

    # Function_4_D49 end

    def Function_5_DAA(): pass

    label("Function_5_DAA")

    SetCameraDistance(15000, 4000)
    PlayEffect(0x0, 0x0, 0xFE, 0x1, 0, 1500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x96, 0x0)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x9C4)
    Sleep(500)
    EndChrThread(0x8, 0x0)
    StopSound(825, 1000, 30)
    Fade(700)
    OP_68(0, 2300, 21500, 300)
    SetChrFlags(0xFE, 0x1)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0xDAC, 0x0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 0, 0, 8)
    StopSound(950, 1000, 100)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_82(0x12C, 0x1F4, 0x1388, 0x3E8)
    Sound(902, 0, 100, 0)
    Sound(833, 0, 50, 0)
    Sleep(1000)
    CancelBlur(500)
    OP_0D()
    Return()

    # Function_5_DAA end

    def Function_6_E91(): pass

    label("Function_6_E91")

    Sound(950, 2, 100, 0)
    PlayEffect(0x0, 0x1, 0xFE, 0x1, 0, 1000, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0xBB8)
    StopEffect(0x1, 0x2)
    StopSound(950, 1000, 100)
    BeginChrThread(0xFE, 0, 0, 10)
    Sleep(1000)
    Return()

    # Function_6_E91 end

    def Function_7_EEC(): pass

    label("Function_7_EEC")

    PlayEffect(0x0, 0x2, 0xFE, 0x1, 0, 1000, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0xBB8)
    StopEffect(0x2, 0x2)
    BeginChrThread(0xFE, 0, 0, 10)
    Sleep(1000)
    Return()

    # Function_7_EEC end

    def Function_8_F3B(): pass

    label("Function_8_F3B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_F59")
    OP_A1(0xFE, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_8_F3B")

    label("loc_F59")

    Return()

    # Function_8_F3B end

    def Function_9_F5A(): pass

    label("Function_9_F5A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_F75")
    OP_A1(0xFE, 0x3E8, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_9_F5A")

    label("loc_F75")

    Return()

    # Function_9_F5A end

    def Function_10_F76(): pass

    label("Function_10_F76")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_F91")
    OP_A1(0xFE, 0x5DC, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_10_F76")

    label("loc_F91")

    Return()

    # Function_10_F76 end

    def Function_11_F92(): pass

    label("Function_11_F92")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00100.itc", 0x1E)
    LoadChrToIndex("chr/ch05800.itc", 0x1F)
    LoadChrToIndex("chr/ch06100.itc", 0x20)
    LoadChrToIndex("chr/ch00050.itc", 0x21)
    LoadChrToIndex("chr/ch00051.itc", 0x22)
    LoadChrToIndex("chr/ch00250.itc", 0x23)
    LoadChrToIndex("chr/ch00251.itc", 0x24)
    LoadChrToIndex("chr/ch00350.itc", 0x25)
    LoadChrToIndex("chr/ch00351.itc", 0x26)
    LoadChrToIndex("chr/ch02950.itc", 0x27)
    LoadChrToIndex("chr/ch02951.itc", 0x28)
    LoadChrToIndex("chr/ch03150.itc", 0x29)
    LoadChrToIndex("chr/ch03151.itc", 0x2A)
    LoadChrToIndex("chr/ch03250.itc", 0x2B)
    LoadChrToIndex("chr/ch03251.itc", 0x2C)
    LoadChrToIndex("chr/ch00056.itc", 0x2D)
    LoadChrToIndex("chr/ch00256.itc", 0x2E)
    LoadChrToIndex("chr/ch00356.itc", 0x2F)
    LoadChrToIndex("chr/ch0295F.itc", 0x30)
    LoadChrToIndex("chr/ch0315F.itc", 0x31)
    LoadChrToIndex("chr/ch0325A.itc", 0x32)
    LoadChrToIndex("chr/ch00053.itc", 0x33)
    LoadChrToIndex("chr/ch00352.itc", 0x34)
    LoadChrToIndex("chr/ch03252.itc", 0x35)
    LoadChrToIndex("chr/ch00150.itc", 0x36)
    LoadChrToIndex("monster/ch84050.itc", 0x37)
    LoadChrToIndex("monster/ch84051.itc", 0x38)
    LoadChrToIndex("monster/ch84052.itc", 0x39)
    LoadChrToIndex("apl/ch51767.itc", 0x3A)
    LoadChrToIndex("chr/ch02952.itc", 0x3B)
    LoadChrToIndex("chr/ch00101.itc", 0x3C)
    LoadChrToIndex("apl/ch51713.itc", 0x3D)
    LoadEffect(0x0, "battle/ms00001.eff")
    LoadEffect(0x1, "event\\ev10008.eff")
    LoadEffect(0x3, "battle/cr001000.eff")
    LoadEffect(0x4, "event/ev17029.eff")
    LoadEffect(0x5, "event\\ev15010.eff")
    LoadEffect(0x6, "event\\ev14002.eff")
    LoadEffect(0x7, "event\\ev17030.eff")
    LoadEffect(0x8, "event\\\\eva04_00.eff")
    LoadEffect(0x9, "event\\\\ev17034.eff")
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu00102.itp")
    SoundLoad(3403)
    SoundLoad(3404)
    SoundLoad(3405)
    SoundLoad(3406)
    SoundLoad(904)
    SoundLoad(579)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, 0, 500, 20500, 0)
    SetChrPos(0x104, -900, 500, 19200, 0)
    SetChrPos(0x109, 850, 500, 19650, 0)
    SetChrPos(0x105, 150, 500, 18550, 0)
    SetChrPos(0x103, 950, 500, 18000, 0)
    SetChrPos(0x106, -1200, 500, 17900, 0)
    SetChrChipByIndex(0x101, 0x21)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x103, 0x23)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x25)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x27)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x29)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x106, 0x2B)
    SetChrSubChip(0x106, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 0x3A)
    SetChrSubChip(0x8, 0x3)
    OP_52(0x8, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xE4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 0, 500, 24000, 180)
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0xAF0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xB, 0x80)
    SetChrChipByIndex(0xB, 0x36)
    SetChrSubChip(0xB, 0x0)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, 11000, 500, 20000, 270)
    SetChrFlags(0xB, 0x8)
    ClearChrFlags(0xC, 0x80)
    SetChrChipByIndex(0xC, 0x1F)
    SetChrSubChip(0xC, 0x0)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, 16500, 1000, 20500, 270)
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xD, 0x80)
    SetChrChipByIndex(0xD, 0x20)
    SetChrSubChip(0xD, 0x0)
    SetChrFlags(0xD, 0x8000)
    SetChrPos(0xD, 16500, 1000, 19500, 270)
    OP_A7(0xD, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    OP_68(0, 1500, 24000, 0)
    MoveCamera(50, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16000, 0)
    PlayEffect(0x4, 0x0, 0x8, 0x5, 0, 1500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    BeginChrThread(0xE, 1, 0, 40)
    FadeToBright(1000, 0)
    SetCameraDistance(15000, 4000)
    BeginChrThread(0x8, 3, 0, 12)
    WaitChrThread(0x8, 3)
    StopEffect(0x0, 0x2)
    EndChrThread(0xE, 0x1)
    OP_6F(0x79)
    OP_0D()
    OP_68(0, 1500, 21000, 2500)
    OP_6F(0x79)
    Fade(500)

    def lambda_1374():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1374)
    Sleep(50)

    def lambda_1390():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1390)
    Sleep(50)

    def lambda_13AC():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_13AC)
    Sleep(50)

    def lambda_13C8():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_13C8)
    Sleep(50)

    def lambda_13E4():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_13E4)
    Sleep(50)

    def lambda_1400():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_1400)
    Sound(898, 0, 100, 0)
    SetChrChipByIndex(0x101, 0x2D)
    SetChrSubChip(0x101, 0x0)
    Sleep(50)
    SetChrChipByIndex(0x103, 0x2E)
    SetChrSubChip(0x103, 0x0)
    Sleep(50)
    Sound(514, 0, 40, 0)
    SetChrChipByIndex(0x104, 0x2F)
    SetChrSubChip(0x104, 0x0)
    Sleep(50)
    SetChrChipByIndex(0x109, 0x30)
    SetChrSubChip(0x109, 0x0)
    Sleep(50)
    SetChrChipByIndex(0x105, 0x31)
    SetChrSubChip(0x105, 0x0)
    Sleep(50)
    SetChrChipByIndex(0x106, 0x32)
    SetChrSubChip(0x106, 0x0)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x104, 2)
    WaitChrThread(0x109, 2)
    WaitChrThread(0x105, 2)
    WaitChrThread(0x106, 2)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00015F#12PDamn\x01",
            "That's a terrible guy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10708F#12P#N\"Society\" is\x01",
            "It is a terrible group, is not it?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#00306F#12POh, that red Mushier doll\x01",
            "What is strengthened so far …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00211F#12P…… That Dr.\x01",
            "Did they remodel … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10406F#12PIt seems likely\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(1000)
    OP_68(0, 1500, 19500, 0)
    MoveCamera(135, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14000, 0)
    SetCameraDistance(14500, 1500)
    OP_6F(0x79)
    OP_0D()
    Fade(250)

    def lambda_15E0():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_15E0)
    SetChrChipByIndex(0x101, 0x21)
    SetChrSubChip(0x101, 0x0)
    Sound(812, 0, 100, 0)
    WaitChrThread(0x101, 2)
    OP_0D()
    Fade(500)

    def lambda_1611():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1611)
    Sleep(50)

    def lambda_162D():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_162D)
    Sleep(50)

    def lambda_1649():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1649)
    Sleep(50)

    def lambda_1665():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_1665)
    Sleep(50)

    def lambda_1681():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_1681)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0x103, 0x23)
    SetChrSubChip(0x103, 0x0)
    Sleep(50)
    SetChrChipByIndex(0x104, 0x25)
    SetChrSubChip(0x104, 0x0)
    Sleep(50)
    SetChrChipByIndex(0x109, 0x27)
    SetChrSubChip(0x109, 0x0)
    Sleep(50)
    SetChrChipByIndex(0x105, 0x29)
    SetChrSubChip(0x105, 0x0)
    Sleep(50)
    SetChrChipByIndex(0x106, 0x2B)
    SetChrSubChip(0x106, 0x2)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x104, 2)
    WaitChrThread(0x109, 2)
    WaitChrThread(0x105, 2)
    WaitChrThread(0x106, 2)
    OP_0D()
    SetCameraDistance(17000, 5000)
    MoveCamera(120, 25, 0, 5000)
    BeginChrThread(0x101, 3, 0, 13)
    Sleep(150)
    BeginChrThread(0x103, 3, 0, 14)
    Sleep(150)
    BeginChrThread(0x104, 3, 0, 15)
    Sleep(150)
    BeginChrThread(0x109, 3, 0, 16)
    Sleep(150)
    BeginChrThread(0x105, 3, 0, 17)
    Sleep(150)
    BeginChrThread(0x106, 3, 0, 18)
    OP_6F(0x79)
    Fade(1000)
    OP_68(0, 1500, 21500, 0)
    MoveCamera(0, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15500, 0)
    SetCameraDistance(15000, 2000)
    OP_6F(0x79)
    OP_0D()
    Fade(250)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    OP_0D()
    OP_93(0x101, 0xB4, 0x1F4)

    def lambda_178C():
        OP_93(0x103, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_178C)
    Sleep(50)

    def lambda_179C():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_179C)
    Sleep(50)

    def lambda_17AC():
        OP_93(0x109, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_17AC)
    Sleep(50)

    def lambda_17BC():
        OP_93(0x105, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_17BC)
    Sleep(50)

    def lambda_17CC():
        OP_93(0x106, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_17CC)
    Sleep(50)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x106, 0)

    ChrTalk(
        0x101,
        (
            "#00004F#5POK, this is the obstacle\x01",
            "You should have eliminated them all.\x02\x03",
            "#00000FSearch the mansion\x01",
            "Eli and the Chairpersons\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0x7D0)
    OP_68(0, 2000, 23000, 1000)
    MoveCamera(0, 33, 0, 1000)
    OP_6F(0x79)
    Sound(140, 0, 100, 0)
    PlayEffect(0x7, 0x0, 0x8, 0x5, 50, 1700, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    Sound(655, 0, 50, 0)
    Sleep(950)
    Fade(500)

    def lambda_18CA():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_18CA)
    OP_A1(0x8, 0x3E8, 0x3, 0x1, 0x2, 0x3)
    SetChrChipByIndex(0x8, 0x37)
    SetChrSubChip(0x8, 0x0)
    Sound(951, 0, 100, 0)
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0xAF0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xE, 1, 0, 41)
    PlayEffect(0x4, 0x7, 0x8, 0x5, 0, 1500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    BeginChrThread(0x8, 0, 0, 8)
    WaitChrThread(0x8, 2)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_93(0x101, 0x0, 0x1F4)

    ChrTalk(
        0x101,
        "#00011F#6PWhat?!\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7455", 0)
    EndChrThread(0x8, 0x0)
    BeginChrThread(0x8, 0, 0, 21)
    BeginChrThread(0x8, 3, 0, 19)
    WaitChrThread(0x8, 3)
    OP_68(750, 2000, 20800, 750)
    MoveCamera(0, 20, 0, 750)
    OP_6E(600, 750)
    SetCameraDistance(15000, 750)
    OP_6F(0x79)
    Fade(250)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0x109, 0x3B)
    SetChrSubChip(0x109, 0x0)
    OP_A1(0x109, 0x5DC, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    OP_0D()

    ChrTalk(
        0x109,
        "#10110F#12PYou…\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x8, 3, 0, 23)
    WaitChrThread(0x8, 3)

    def lambda_1A1D():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1A1D)
    Sleep(50)

    def lambda_1A2D():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1A2D)
    Sleep(50)

    def lambda_1A3D():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_1A3D)
    Sleep(50)

    def lambda_1A4D():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1A4D)
    Sleep(50)

    def lambda_1A5D():
        TurnDirection(0x106, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_1A5D)
    Sleep(50)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x106, 0)
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00010F#6P#NCrap!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)

    def lambda_1AC2():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1AC2)
    Sleep(50)

    def lambda_1ADE():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1ADE)
    Sleep(50)

    def lambda_1AFA():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1AFA)
    Sleep(50)

    def lambda_1B16():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_1B16)
    Sleep(50)

    def lambda_1B32():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_1B32)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0x103, 0x23)
    SetChrSubChip(0x103, 0x0)
    Sleep(50)
    SetChrChipByIndex(0x104, 0x25)
    SetChrSubChip(0x104, 0x0)
    Sleep(50)
    SetChrChipByIndex(0x109, 0x27)
    SetChrSubChip(0x109, 0x0)
    Sleep(50)
    SetChrChipByIndex(0x105, 0x29)
    SetChrSubChip(0x105, 0x0)
    Sleep(50)
    SetChrChipByIndex(0x106, 0x2B)
    SetChrSubChip(0x106, 0x2)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x104, 2)
    WaitChrThread(0x109, 2)
    WaitChrThread(0x105, 2)
    WaitChrThread(0x106, 2)
    OP_0D()

    ChrTalk(
        0x109,
        "#10107F#5PLloyd!\x02",
    )

    CloseMessageWindow()
    OP_68(3550, 2300, 21350, 1000)
    MoveCamera(315, 26, 0, 1000)
    OP_6E(600, 1000)
    SetCameraDistance(13700, 1000)
    OP_6F(0x79)
    Fade(350)
    Sound(951, 0, 100, 0)
    SetChrChipByIndex(0x8, 0x39)
    SetChrSubChip(0x8, 0x0)
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0xAF0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_0D()
    StopBGM(0xBB8)
    OP_C9(0x0, 0x80000000)

    NpcTalk(
        0xB,
        "Daughter's voice",
        "#3403V#1P#10AI won't let you!\x02",
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    BeginChrThread(0x8, 3, 0, 34)
    WaitChrThread(0x8, 3)

    ChrTalk(
        0x101,
        "#00005F#5P#N#8AHuh\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    OP_68(-2850, 1700, 21800, 0)
    OP_68(-4350, 1700, 21800, 500)
    MoveCamera(23, 18, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15500, 0)
    TurnDirection(0x103, 0x8, 0)
    TurnDirection(0x104, 0x8, 0)
    TurnDirection(0x105, 0x8, 0)
    TurnDirection(0x109, 0x8, 0)
    TurnDirection(0x106, 0x8, 0)
    OP_6F(0x79)
    OP_0D()
    BeginChrThread(0x106, 3, 0, 36)
    Sleep(150)
    BeginChrThread(0x104, 3, 0, 35)
    WaitChrThread(0x104, 3)
    WaitChrThread(0x106, 3)
    CloseMessageWindow()
    OP_5A()
    SetChrFlags(0x8, 0x80)
    Sleep(1000)
    Fade(500)
    OP_82(0x7D, 0x7D, 0x1388, 0x3E8)
    OP_68(-1000, 1500, 21000, 0)
    OP_68(-1500, 1500, 20000, 2000)
    MoveCamera(35, 26, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16000, 0)
    OP_6F(0x79)
    Fade(250)
    Sound(805, 0, 80, 0)
    Sound(531, 0, 80, 0)
    Sound(540, 0, 40, 0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x106, 0xFF)
    SetChrSubChip(0x106, 0x0)
    OP_0D()

    def lambda_1D8E():
        OP_93(0x103, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1D8E)
    Sleep(50)

    def lambda_1D9E():
        OP_93(0x104, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1D9E)
    Sleep(50)

    def lambda_1DAE():
        OP_93(0x109, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1DAE)
    Sleep(50)

    def lambda_1DBE():
        OP_93(0x105, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_1DBE)
    Sleep(50)

    def lambda_1DCE():
        OP_93(0x106, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_1DCE)
    Sleep(50)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x106, 0)
    OP_68(1000, 1500, 20000, 1500)
    SetCameraDistance(13500, 1500)

    def lambda_1E0C():
        OP_9B(0x1, 0xFE, 0x1E, 0xBB8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_1E0C)
    Sleep(50)

    def lambda_1E24():
        OP_9B(0x1, 0xFE, 0xFFE7, 0xFA0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1E24)
    Sleep(50)

    def lambda_1E3C():
        OP_9B(0x1, 0xFE, 0xFFDA, 0xBB8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1E3C)
    Sleep(50)

    def lambda_1E54():
        OP_9B(0x1, 0xFE, 0x21, 0xBB8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1E54)
    Sleep(50)

    def lambda_1E6C():
        OP_9B(0x1, 0xFE, 0xFFE2, 0xFA0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1E6C)
    Sleep(50)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x109, 1)
    WaitChrThread(0x105, 1)
    WaitChrThread(0x106, 1)
    OP_6F(0x79)

    ChrTalk(
        0x103,
        "#00206F#6P#6PAhh\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10406F#6POh brother\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xB, 0x8)
    OP_68(11000, 1500, 20000, 2200)
    MoveCamera(60, 25, 0, 2200)
    OP_6E(600, 2200)
    SetCameraDistance(14500, 2200)
    OP_6F(0x79)
    SetChrPos(0x101, 700, 500, 20000, 90)

    ChrTalk(
        0x101,
        "#00002F#6P#NElie…\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x101, 4700, 500, 20000, 90)

    ChrTalk(
        0x103,
        "#00202F#6P#NElie!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        "#00309F#6P#NAhah, you were alright!\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    Sound(531, 0, 50, 0)
    SetChrChipByIndex(0xB, 0x1E)
    SetChrSubChip(0xB, 0x0)
    OP_0D()
    OP_68(9000, 1500, 20000, 1500)
    MoveCamera(60, 18, 0, 1500)
    SetCameraDistance(15500, 1500)
    OP_6F(0x79)

    ChrTalk(
        0xB,
        "#00106F#40W#11P….\x02",
    )

    CloseMessageWindow()

    def lambda_2003():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2003)
    Sleep(250)
    Fade(250)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    WaitChrThread(0x101, 2)
    OP_0D()
    Sleep(800)
    OP_9B(0x0, 0x101, 0x0, 0x1F4, 0x3E8, 0x0)

    ChrTalk(
        0x101,
        (
            "#00012F#6PThat……\x01",
            "What should I say?\x02\x03",
            "#00004FTentatively,\x01",
            "Thank you, Erie.\x02\x03",
            "#00002FYou saved me\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#00101F#11P…!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7523", 0)
    Fade(250)
    SetChrChipByIndex(0xB, 0x1E)
    SetChrSubChip(0xB, 0x0)
    OP_0D()
    OP_68(5300, 1500, 20000, 1400)
    MoveCamera(45, 18, 0, 1400)
    SetCameraDistance(12000, 1400)
    SetChrChipByIndex(0xB, 0x3C)
    SetChrSubChip(0xB, 0x0)
    OP_95(0xB, 5800, 500, 20000, 5000, 0x0)
    Fade(250)
    Sound(898, 0, 100, 0)
    Sound(811, 0, 20, 0)

    def lambda_2149():
        OP_A6(0xFE, 0x0, 0x1E, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2149)
    SetChrFlags(0xB, 0x2)
    SetChrChipByIndex(0xB, 0x3D)
    SetChrSubChip(0xB, 0x0)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x3D)
    SetChrSubChip(0x101, 0x8)
    WaitChrThread(0x101, 2)
    OP_6F(0x79)
    SetCameraDistance(11000, 20000)
    OP_0D()
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x106, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00011F#6P#10AWaa\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    OP_C9(0x0, 0x80000000)

    AnonymousTalk(
        0xB,
        (
            "#3404V#40W#40AWas good……\x01",
            "……It is very nice……\x02\x03",
            "#3405V#40AFor being safe … ….\x01",
            "…… I can see you again ……\x02\x03",
            "#3406V#40Anever again……\x01",
            "I thought I could meet him … ….\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Sleep(300)

    ChrTalk(
        0x101,
        "#00002F#6PElie…\x02",
    )

    CloseMessageWindow()
    OP_68(3000, 1500, 20000, 2000)
    SetCameraDistance(14000, 2000)
    Sleep(1500)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x106, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x104,
        "#00309F#6P(Uhhh…. Sooo)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10114F#6P(Well, even if you call out to me\x01",
            "Is not it okay …? )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#10706F#6P(I-It's hard to say)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10402F#6P(But it was good with you,\x01",
            "His subjugation is also very useful. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00211F#6P(I don't know what you mean…)\x02",
    )

    CloseMessageWindow()
    OP_68(3700, 1500, 20000, 1500)
    Sleep(1000)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Sound(2185, 255, 100, 0)

    ChrTalk(
        0xB,
        "#00105F#11PHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#6PAhah…\x02\x03",
            "… … I'm happy,\x01",
            "As expected\x01",
            "I wonder if my eyes hurt ……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Fade(250)
    Sound(802, 0, 50, 0)
    SetChrSubChip(0xB, 0x1)
    SetChrSubChip(0x101, 0x9)
    SetChrPos(0xB, 6000, 500, 20000, 270)
    OP_0D()
    SetChrChipByIndex(0xB, 0x1E)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x101, 0x2)
    OP_68(3840, 1500, 19790, 2000)
    Sound(2177, 255, 80, 0)
    OP_96(0xB, 0x1770, 0x1F4, 0x4B00, 0x7D0, 0x0)
    OP_93(0x101, 0x10E, 0x1F4)
    OP_63(0xB, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    SetChrFlags(0xB, 0x2)
    SetChrChipByIndex(0xB, 0x3D)
    OP_A1(0xB, 0x514, 0x8, 0x2, 0x3, 0x4, 0x3, 0x2, 0x3, 0x4, 0x3)
    OP_A1(0xB, 0x514, 0x4, 0x2, 0x3, 0x4, 0x3)

    ChrTalk(
        0xB,
        (
            "#00112F#11PW-wait a minute, that's not…\x02\x03",
            "Lloyd is now\x01",
            "Because it was a dangerous place\x01",
            "You are just going crazy!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10402F#6POh-\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00309F#6PIs that right- (Grin)\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(2183, 255, 100, 0)
    Fade(250)
    SetChrChipByIndex(0xB, 0x1E)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x2)
    OP_0D()
    Sleep(800)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0xB,
        (
            "#00115F#11P#4SOH COME ON IT'S NOT LIKE THAT!\x02\x03",
            "#00112F#3STio, noel!\x01",
            "Do not get me wrong! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10112F#6PEh, uh, right\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00204F#6P#NI'm trying my best \x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xB,
        (
            "#00113F#11PUh, well then\x01",
            "Mr. Lisha\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xB,
        (
            "#00105F#11P#30WHuh?\x02\x03",
            "Why\x01",
            "Mr. Lisha together?\x02\x03",
            "#00108FBesides, there is also Noel,\x01",
            "Waji is doing such a dress … …\x02\x03",
            "#00105F?????\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012F#11PAhah…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#10710F#6PUh, it's a long story\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0xC,
        "Voice of an old man",
        (
            "#3P#2SGiggle\x01",
            "Apparently it seems like that.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x106, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Fade(500)
    OP_68(16500, 1500, 20000, 0)
    OP_68(3500, 1500, 20000, 6000)

    def lambda_29E4():

        label("loc_29E4")

        TurnDirection(0xFE, 0xC, 500)
        Yield()
        Jump("loc_29E4")

    QueueWorkItem2(0x101, 2, lambda_29E4)

    def lambda_29F6():

        label("loc_29F6")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_29F6")

    QueueWorkItem2(0xB, 2, lambda_29F6)
    BeginChrThread(0xC, 3, 0, 38)
    Sleep(300)
    BeginChrThread(0xD, 3, 0, 39)
    Sleep(3000)

    def lambda_2A1A():
        OP_98(0xFE, 0xFFFFFED4, 0x0, 0x6A4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2A1A)

    def lambda_2A34():
        OP_98(0xFE, 0xFFFFFE0C, 0x0, 0xFFFFFE0C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2A34)
    WaitChrThread(0xC, 3)
    WaitChrThread(0xD, 3)
    WaitChrThread(0x101, 1)
    WaitChrThread(0xB, 1)
    EndChrThread(0x101, 0x2)
    EndChrThread(0xB, 0x2)
    OP_93(0x101, 0xE1, 0x1F4)
    OP_93(0xB, 0x10E, 0x1F4)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#00002F#5PChairman, you were ok\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00205F#6P#NAnd Jona!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#02309F#11POkay.\x01",
            "It has been quite a long time.\x02\x03",
            "#02302FNo, I really was saved!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#00100F#11PUm, he is after us\x01",
            "I was brought to the bell.\x02\x03",
            "#00106FEverything to the center of Orkis Tower\x01",
            "It seems I repeated hacking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#02310F#11PThat one's a real bitch\x02\x03",
            "More than\x01",
            "On a mansion with no conducting net\x01",
            "Keep this confinement!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012F#5PI-I see\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00204F#6P#NCertainly for you\x01",
            "It is probably the best moxa.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#02503F#11PWell, we should exchange stories after\x02\x03",
            "#02500FApparently we\x01",
            "You seem to have come to help?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00013F#5PYes……!\x01",
            "I got to pick you up!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10400F#6PIf there is no particular problem\x01",
            "Can you escape as it is?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#02503F#11POf course\x02\x03",
            "#02501FPeace#4RAnan#The situation that can be said\x01",
            "It's gone by now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#00106F#11PRight…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301F#6POK, reinforcement of your uncle\x01",
            "Will escape before coming!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10101F#6PWhile securing withdrawal,\x01",
            "Let's return to Mercapa!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    StopSound(124, 1000, 40)
    SetCameraDistance(14300, 1000)
    OP_6F(0x79)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "After that, Lloyd's\x01",
            "Joined with Zeit who was standing in the sun\x01",
            "Return to Mercapa ……\x02\x03",
            "Before reinforcement of \"Red constellation\" comes\x01",
            "I succeeded in departing from Michelam.\x02\x03",
            "And then-\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_24(0x388)
    OP_24(0x243)
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x22, 7)
    NewScene("e4300", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_11_F92 end

    def Function_12_2FBA(): pass

    label("Function_12_2FBA")


    def lambda_2FBF():
        OP_A6(0xFE, 0x0, 0x14, 0x7D0, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2FBF)
    WaitChrThread(0xFE, 2)
    Sound(905, 0, 70, 0)
    Sound(954, 0, 100, 0)

    def lambda_2FE8():
        OP_A6(0xFE, 0x0, 0x1E, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2FE8)
    OP_A1(0xFE, 0x3E8, 0x4, 0x3, 0x2, 0x1, 0x0)
    OP_82(0x64, 0x64, 0x1388, 0x1F4)
    Sound(902, 0, 50, 0)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_12_2FBA end

    def Function_13_3022(): pass

    label("Function_13_3022")

    OP_93(0xFE, 0x2D, 0x1F4)
    Sleep(500)
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(500)
    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x3E8, 0x0)
    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    Sleep(200)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x2D)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_13_3022 end

    def Function_14_3067(): pass

    label("Function_14_3067")

    OP_93(0xFE, 0x2D, 0x1F4)
    Sleep(500)
    OP_93(0xFE, 0x5A, 0x1F4)
    Sleep(500)
    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0x3E8, 0x0)
    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x0)
    Sleep(300)
    OP_93(0xFE, 0x87, 0x1F4)
    Return()

    # Function_14_3067 end

    def Function_15_30A5(): pass

    label("Function_15_30A5")

    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(500)
    SetChrChipByIndex(0xFE, 0x26)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x3E8, 0x0)
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_15_30A5 end

    def Function_16_30CF(): pass

    label("Function_16_30CF")

    OP_93(0xFE, 0x5A, 0x1F4)
    Sleep(750)
    OP_93(0xFE, 0x87, 0x1F4)
    Sleep(750)
    OP_93(0xFE, 0x2D, 0x1F4)
    Return()

    # Function_16_30CF end

    def Function_17_30EB(): pass

    label("Function_17_30EB")

    OP_93(0xFE, 0x2D, 0x1F4)
    Sleep(1000)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_17_30EB end

    def Function_18_30FD(): pass

    label("Function_18_30FD")

    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(500)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_18_30FD end

    def Function_19_310F(): pass

    label("Function_19_310F")

    Sound(905, 0, 100, 0)
    Fade(500)
    SetCameraDistance(14000, 500)
    Sound(904, 2, 100, 0)
    SetChrChipByIndex(0xFE, 0x39)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0xAF0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6F(0x79)
    OP_0D()
    Sleep(300)
    Sound(951, 0, 100, 0)
    SetChrSubChip(0xFE, 0x1)
    Sleep(50)
    SetChrSubChip(0xFE, 0x2)
    Sleep(50)
    SetChrSubChip(0xFE, 0x3)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_68(2000, 2000, 21000, 500)
    MoveCamera(345, 21, 0, 500)
    OP_6E(600, 500)
    SetCameraDistance(15000, 500)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 0, 2000, 22000, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    OP_82(0x1F4, 0x1F4, 0x1388, 0x12C)
    Sound(833, 0, 100, 0)
    Sound(902, 0, 100, 0)
    Sound(2030, 255, 100, 0)
    BeginChrThread(0x101, 3, 0, 20)
    Sleep(50)
    SetChrSubChip(0xFE, 0x4)
    WaitChrThread(0x101, 3)
    OP_6F(0x79)
    CancelBlur(500)
    Return()

    # Function_19_310F end

    def Function_20_3207(): pass

    label("Function_20_3207")

    OP_93(0xFE, 0x13B, 0x0)
    SetChrChipByIndex(0xFE, 0x33)
    SetChrSubChip(0xFE, 0x0)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x1000)
    SetChrChip(0x0, 0xFE, 0x1E, 0x12C)

    def lambda_322D():
        OP_9D(0xFE, 0x125C, 0x1F4, 0x4E20, 0x3E8, 0x1194)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_322D)
    WaitChrThread(0xFE, 1)
    ClearChrFlags(0xFE, 0x20)
    ClearChrFlags(0xFE, 0x1000)
    OP_A1(0xFE, 0x5DC, 0x2, 0x2, 0x3)
    Sound(514, 0, 100, 0)
    Sleep(500)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_20_3207 end

    def Function_21_326D(): pass

    label("Function_21_326D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3290")
    OP_A6(0x8, 0x1E, 0x1E, 0x1F4, 0x1388)
    Jump("Function_21_326D")

    label("loc_3290")

    Return()

    # Function_21_326D end

    def Function_22_3291(): pass

    label("Function_22_3291")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_32DB")
    PlayEffect(0x8, 0xFF, 0x8, 0x0, 0, -300, -500, 0, 0, 0, 4000, 4000, 4000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    Jump("Function_22_3291")

    label("loc_32DB")

    Return()

    # Function_22_3291 end

    def Function_23_32DC(): pass

    label("Function_23_32DC")

    OP_68(0, 2000, 22500, 500)
    Sound(905, 0, 100, 0)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    BeginChrThread(0x8, 2, 0, 22)
    SetChrChipByIndex(0xFE, 0x3A)
    SetChrSubChip(0xFE, 0x4)
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0xAF0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6F(0x79)
    OP_68(1000, 2000, 14450, 1000)
    MoveCamera(330, 20, 0, 1000)
    OP_6E(600, 1000)
    SetCameraDistance(15000, 1000)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x1000)
    SetChrChip(0x0, 0xFE, 0x96, 0x2BC)
    Sound(579, 2, 100, 0)

    def lambda_3360():
        OP_9B(0x0, 0xFE, 0xFFEC, 0x2CEC, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3360)

    def lambda_3375():

        label("loc_3375")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_3375")

    QueueWorkItem2(0x103, 2, lambda_3375)

    def lambda_3387():

        label("loc_3387")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_3387")

    QueueWorkItem2(0x104, 2, lambda_3387)

    def lambda_3399():

        label("loc_3399")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_3399")

    QueueWorkItem2(0x109, 2, lambda_3399)

    def lambda_33AB():

        label("loc_33AB")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_33AB")

    QueueWorkItem2(0x105, 2, lambda_33AB)

    def lambda_33BD():

        label("loc_33BD")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_33BD")

    QueueWorkItem2(0x106, 2, lambda_33BD)
    Sleep(100)
    Sound(844, 0, 100, 0)
    BeginChrThread(0x109, 3, 0, 26)
    Sleep(50)
    BeginChrThread(0x103, 3, 0, 24)
    Sleep(50)
    BeginChrThread(0x105, 3, 0, 27)
    Sleep(50)
    BeginChrThread(0x104, 3, 0, 25)
    Sleep(50)
    BeginChrThread(0x106, 3, 0, 28)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    WaitChrThread(0x109, 3)
    WaitChrThread(0x105, 3)
    WaitChrThread(0x106, 3)
    WaitChrThread(0xFE, 1)
    OP_24(0x243)
    PlayEffect(0x1, 0xFF, 0xFE, 0x5, 0, 0, 0, 0, 0, 0, 1250, 1250, 1250, 0xFF, 0, 0, 0, 0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_82(0x1F4, 0x1F4, 0x1388, 0x12C)
    Sound(833, 0, 70, 0)
    Sound(902, 0, 100, 0)
    Sleep(500)
    CancelBlur(500)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0x109, 0x2)
    EndChrThread(0x105, 0x2)
    EndChrThread(0x106, 0x2)
    OP_6F(0x79)
    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#00310F#5P#NChit\x01",
            "Does it runaway! Is it?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_93(0xFE, 0x13E, 0x1F4)
    OP_68(-5550, 2000, 23200, 1200)
    MoveCamera(315, 26, 0, 1200)
    OP_6E(600, 1200)
    SetCameraDistance(19000, 1200)
    SetChrChip(0x0, 0xFE, 0x96, 0x2BC)
    Sound(579, 2, 100, 0)

    def lambda_3518():
        OP_9B(0x0, 0xFE, 0x0, 0x36B0, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3518)

    def lambda_352D():

        label("loc_352D")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_352D")

    QueueWorkItem2(0x103, 2, lambda_352D)

    def lambda_353F():

        label("loc_353F")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_353F")

    QueueWorkItem2(0x104, 2, lambda_353F)

    def lambda_3551():

        label("loc_3551")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_3551")

    QueueWorkItem2(0x109, 2, lambda_3551)

    def lambda_3563():

        label("loc_3563")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_3563")

    QueueWorkItem2(0x105, 2, lambda_3563)

    def lambda_3575():

        label("loc_3575")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_3575")

    QueueWorkItem2(0x106, 2, lambda_3575)
    Sleep(350)
    BeginChrThread(0x103, 3, 0, 29)
    Sleep(50)
    BeginChrThread(0x105, 3, 0, 32)
    Sleep(50)
    BeginChrThread(0x109, 3, 0, 31)
    Sleep(50)
    BeginChrThread(0x104, 3, 0, 30)
    Sleep(50)
    BeginChrThread(0x106, 3, 0, 33)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    WaitChrThread(0x109, 3)
    WaitChrThread(0x105, 3)
    WaitChrThread(0x106, 3)
    WaitChrThread(0xFE, 1)
    OP_24(0x243)
    PlayEffect(0x1, 0xFF, 0xFE, 0x5, 0, 0, 0, 0, 0, 0, 1250, 1250, 1250, 0xFF, 0, 0, 0, 0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_82(0x1F4, 0x1F4, 0x1388, 0x12C)
    Sound(833, 0, 70, 0)
    Sound(902, 0, 100, 0)
    Sleep(500)
    CancelBlur(500)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0x109, 0x2)
    EndChrThread(0x105, 0x2)
    EndChrThread(0x106, 0x2)
    OP_6F(0x79)
    OP_93(0xFE, 0x78, 0x1F4)
    OP_68(3150, 2300, 19400, 1000)
    MoveCamera(300, 20, 0, 1000)
    OP_6E(600, 1000)
    SetCameraDistance(14700, 1000)
    SetChrChip(0x0, 0xFE, 0x96, 0x2BC)
    Sound(844, 0, 100, 0)
    ClearChrFlags(0xFE, 0x1)

    def lambda_369D():
        OP_9D(0xFE, 0xA8C, 0x1F4, 0x56B8, 0xBB8, 0x1194)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_369D)

    def lambda_36BA():

        label("loc_36BA")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_36BA")

    QueueWorkItem2(0x103, 2, lambda_36BA)

    def lambda_36CC():

        label("loc_36CC")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_36CC")

    QueueWorkItem2(0x104, 2, lambda_36CC)

    def lambda_36DE():

        label("loc_36DE")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_36DE")

    QueueWorkItem2(0x109, 2, lambda_36DE)

    def lambda_36F0():

        label("loc_36F0")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_36F0")

    QueueWorkItem2(0x105, 2, lambda_36F0)

    def lambda_3702():

        label("loc_3702")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_3702")

    QueueWorkItem2(0x106, 2, lambda_3702)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x1)
    SetChrSubChip(0xFE, 0x2)
    EndChrThread(0x8, 0x2)
    PlayEffect(0x1, 0xFF, 0xFE, 0x5, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_82(0x1F4, 0x1F4, 0x1388, 0x12C)
    Sound(833, 0, 70, 0)
    Sound(902, 0, 100, 0)
    Sleep(500)
    CancelBlur(500)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    TurnDirection(0xFE, 0x101, 500)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0x109, 0x2)
    EndChrThread(0x105, 0x2)
    EndChrThread(0x106, 0x2)

    def lambda_37B0():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_37B0)
    Sleep(50)

    def lambda_37C0():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_37C0)
    Sleep(50)

    def lambda_37D0():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_37D0)
    Sleep(50)

    def lambda_37E0():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_37E0)
    Sleep(50)

    def lambda_37F0():
        TurnDirection(0x106, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_37F0)
    Sleep(50)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x106, 0)
    OP_6F(0x79)
    Return()

    # Function_23_32DC end

    def Function_24_3812(): pass

    label("Function_24_3812")


    ChrTalk(
        0x103,
        "#00210F#6PWell then …! Is it?\x05\x02",
    )

    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x2)
    OP_9D(0xFE, 0xFFFFFF9C, 0x1F4, 0x40A6, 0x3E8, 0x1388)
    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_24_3812 end

    def Function_25_3858(): pass

    label("Function_25_3858")

    SetChrChipByIndex(0xFE, 0x2F)
    SetChrSubChip(0xFE, 0x2)
    OP_9D(0xFE, 0xFFFFF22C, 0x1F4, 0x49B6, 0x3E8, 0x1388)
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_25_3858 end

    def Function_26_3880(): pass

    label("Function_26_3880")

    SetChrChipByIndex(0xFE, 0x30)
    SetChrSubChip(0xFE, 0x2)
    OP_9D(0xFE, 0xFFFFFB5A, 0x1F4, 0x4998, 0x3E8, 0x1388)
    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_26_3880 end

    def Function_27_38A8(): pass

    label("Function_27_38A8")

    SetChrChipByIndex(0xFE, 0x31)
    SetChrSubChip(0xFE, 0x2)
    OP_9D(0xFE, 0xFFFFFBBE, 0x1F4, 0x4376, 0x3E8, 0x1388)
    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x0)

    ChrTalk(
        0x105,
        "#10410F#5PDamn\x05\x02",
    )

    Return()

    # Function_27_38A8 end

    def Function_28_38E8(): pass

    label("Function_28_38E8")

    SetChrChipByIndex(0xFE, 0x32)
    SetChrSubChip(0xFE, 0x2)
    OP_9D(0xFE, 0xFFFFF5D8, 0x1F4, 0x42AE, 0x3E8, 0x1388)
    SetChrChipByIndex(0xFE, 0x2B)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_28_38E8 end

    def Function_29_3910(): pass

    label("Function_29_3910")

    Sound(501, 0, 70, 0)
    PlayEffect(0x0, 0xFF, 0xFE, 0x0, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x2)
    OP_9D(0xFE, 0xFFFFFBC8, 0x1F4, 0x3DB8, 0x3E8, 0x1388)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_29_3910 end

    def Function_30_3971(): pass

    label("Function_30_3971")

    Sound(501, 0, 70, 0)
    PlayEffect(0x0, 0xFF, 0xFE, 0x0, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0xFE, 0x2F)
    SetChrSubChip(0xFE, 0x2)
    OP_9D(0xFE, 0xFFFFE93A, 0x1F4, 0x5014, 0x3E8, 0x1388)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_30_3971 end

    def Function_31_39D2(): pass

    label("Function_31_39D2")

    Sound(501, 0, 70, 0)
    PlayEffect(0x0, 0xFF, 0xFE, 0x0, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0xFE, 0x30)
    SetChrSubChip(0xFE, 0x2)
    OP_9D(0xFE, 0xFFFFF4A2, 0x1F4, 0x45D8, 0x3E8, 0x1388)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_31_39D2 end

    def Function_32_3A33(): pass

    label("Function_32_3A33")

    Sound(501, 0, 70, 0)
    PlayEffect(0x0, 0xFF, 0xFE, 0x0, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0xFE, 0x31)
    SetChrSubChip(0xFE, 0x2)
    OP_9D(0xFE, 0xFFFFF47A, 0x1F4, 0x3FDE, 0x3E8, 0x1388)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_32_3A33 end

    def Function_33_3A94(): pass

    label("Function_33_3A94")

    Sound(501, 0, 70, 0)
    PlayEffect(0x0, 0xFF, 0xFE, 0x0, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0xFE, 0x32)
    SetChrSubChip(0xFE, 0x2)
    OP_9D(0xFE, 0xFFFFEAD4, 0x1F4, 0x4902, 0x3E8, 0x1388)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_33_3A94 end

    def Function_34_3AF5(): pass

    label("Function_34_3AF5")

    Sound(530, 0, 100, 0)
    Sound(566, 0, 50, 0)
    PlayEffect(0x9, 0xFF, 0xFF, 0x0, 15000, 2500, 20000, 282, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    Sound(902, 0, 100, 0)
    PlayEffect(0x3, 0xFF, 0xFE, 0x1, 0, 2000, 0, 270, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)

    def lambda_3B7D():
        OP_A6(0xFE, 0x0, 0x4B, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3B7D)
    SetChrChipByIndex(0xFE, 0x3A)
    SetChrSubChip(0xFE, 0x3)
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0xAF0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(2600, 2300, 22500, 150)
    OP_82(0x12C, 0x12C, 0x1388, 0x12C)

    def lambda_3BCB():
        OP_96(0xFE, 0x79E, 0x1F4, 0x5A6E, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3BCB)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    OP_6F(0x79)
    Sleep(800)
    Sound(530, 0, 100, 0)
    Sound(566, 0, 50, 0)
    PlayEffect(0x9, 0xFF, 0xFF, 0x0, 15000, 2500, 20000, 283, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    Sound(902, 0, 100, 0)
    PlayEffect(0x3, 0xFF, 0xFE, 0x1, 0, 2000, 0, 270, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)

    def lambda_3C75():
        OP_A6(0xFE, 0x0, 0x4B, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3C75)
    SetChrSubChip(0xFE, 0x2)
    OP_68(1150, 2300, 22050, 150)
    OP_82(0x12C, 0x12C, 0x1388, 0x12C)

    def lambda_3CB4():
        OP_96(0xFE, 0x258, 0x1F4, 0x5816, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3CB4)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    OP_6F(0x79)
    Sound(530, 0, 100, 0)
    Sound(566, 0, 50, 0)
    PlayEffect(0x9, 0xFF, 0xFF, 0x0, 15000, 2500, 20000, 278, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    Sound(902, 0, 100, 0)
    PlayEffect(0x3, 0xFF, 0xFE, 0x1, 0, 2000, 0, 270, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)

    def lambda_3D5B():
        OP_A6(0xFE, 0x0, 0x4B, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3D5B)
    SetChrSubChip(0xFE, 0x1)
    OP_68(850, 2300, 23100, 150)
    OP_82(0x12C, 0x12C, 0x1388, 0x12C)

    def lambda_3D9A():
        OP_96(0xFE, 0x0, 0x1F4, 0x5DC0, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3D9A)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    OP_6F(0x79)
    Return()

    # Function_34_3AF5 end

    def Function_35_3DBA(): pass

    label("Function_35_3DBA")

    OP_68(-1500, 2300, 22700, 500)
    MoveCamera(45, 27, 0, 500)
    OP_6E(600, 500)
    SetCameraDistance(11000, 500)
    SetChrChipByIndex(0xFE, 0x2F)
    SetChrSubChip(0xFE, 0x1)
    SetChrChip(0x0, 0xFE, 0x1E, 0x12C)
    Sound(844, 0, 100, 0)
    OP_9D(0xFE, 0xFFFFF9F2, 0x1F4, 0x5C30, 0x3E8, 0x1388)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    OP_6F(0x79)
    Sound(2315, 255, 100, 0)

    ChrTalk(
        0x104,
        "#00307F#3POh there ah!\x05\x02",
    )

    Sound(532, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x34)
    OP_A1(0xFE, 0x5DC, 0x3, 0x0, 0x1, 0x2)
    BeginChrThread(0x8, 3, 0, 37)
    OP_A1(0xFE, 0x5DC, 0x3, 0x3, 0x4, 0x5)
    WaitChrThread(0x8, 3)
    EndChrThread(0x8, 0x0)
    Return()

    # Function_35_3DBA end

    def Function_36_3E76(): pass

    label("Function_36_3E76")

    SetChrChipByIndex(0xFE, 0x32)
    SetChrSubChip(0xFE, 0x1)
    SetChrChip(0x0, 0xFE, 0x1E, 0x12C)
    OP_9D(0xFE, 0xFFFFFB82, 0x1F4, 0x57BC, 0x3E8, 0x1388)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    SetChrChipByIndex(0xFE, 0x2B)
    SetChrSubChip(0xFE, 0x0)
    Sleep(250)
    Sound(3183, 255, 100, 1)

    ChrTalk(
        0x106,
        "#10707F#4PWhat……!\x05\x02",
    )

    Sound(538, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x35)
    OP_A1(0xFE, 0x5DC, 0x3, 0x0, 0x1, 0x2)
    OP_A1(0xFE, 0x5DC, 0x3, 0x3, 0x4, 0x5)
    Return()

    # Function_36_3E76 end

    def Function_37_3EEF(): pass

    label("Function_37_3EEF")

    OP_93(0xFE, 0xE1, 0x0)
    SetChrSubChip(0xFE, 0x0)
    Sound(196, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, -670, 2000, 23530, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    OP_82(0x1F4, 0x1F4, 0xBB8, 0x3E8)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    Sleep(50)
    OP_68(2170, 2400, 26370, 500)
    OP_96(0xFE, 0xA14, 0x1F4, 0x689C, 0x3A98, 0x0)
    PlayEffect(0x5, 0xFF, 0xFE, 0x5, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    CancelBlur(500)
    Sleep(500)
    OP_6F(0x79)
    Sound(546, 0, 100, 0)
    StopEffect(0x7, 0x2)
    PlayEffect(0x4, 0x0, 0xFF, 0x0, 2020, 2500, 26630, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0x1, 0xFF, 0x0, 2820, 1750, 25760, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0x2, 0xFF, 0x0, 1260, 2000, 27380, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0x3, 0xFF, 0x0, 2410, 3000, 26190, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    SetCameraDistance(10000, 2500)
    Sleep(1500)
    Sound(546, 0, 100, 0)
    OP_6F(0x79)
    Fade(250)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetCameraDistance(8000, 250)
    OP_6F(0x79)
    OP_0D()
    OP_82(0x12C, 0x12C, 0x1388, 0x7D0)
    SetCameraDistance(23500, 500)
    Sound(200, 0, 100, 0)
    Sound(833, 0, 100, 0)
    PlayEffect(0x6, 0xFF, 0xFF, 0x0, 2580, 500, 26780, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    StopEffect(0x0, 0x2)
    StopEffect(0x1, 0x2)
    StopEffect(0x2, 0x2)
    StopEffect(0x3, 0x2)
    EndChrThread(0xE, 0x1)
    StopSound(904, 500, 100)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
    OP_6F(0x79)
    CancelBlur(2000)
    Return()

    # Function_37_3EEF end

    def Function_38_4159(): pass

    label("Function_38_4159")

    ClearChrFlags(0xFE, 0x4)

    def lambda_4163():
        OP_9B(0x0, 0xFE, 0x0, 0x2EE0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4163)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_38_4159 end

    def Function_39_4188(): pass

    label("Function_39_4188")

    ClearChrFlags(0xFE, 0x4)

    def lambda_4192():
        OP_9B(0x0, 0xFE, 0x0, 0x2EE0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4192)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_39_4188 end

    def Function_40_41B7(): pass

    label("Function_40_41B7")

    Sound(203, 0, 60, 0)
    Sleep(900)
    Sound(203, 0, 70, 0)
    Sleep(1100)
    Sound(203, 0, 60, 0)
    Return()

    # Function_40_41B7 end

    def Function_41_41D0(): pass

    label("Function_41_41D0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4204")
    Sound(203, 0, 60, 0)
    Sleep(900)
    Sound(203, 0, 70, 0)
    Sleep(1100)
    Sound(203, 0, 60, 0)
    Sleep(800)
    Sound(203, 0, 50, 0)
    Sleep(1000)
    Jump("Function_41_41D0")

    label("loc_4204")

    Return()

    # Function_41_41D0 end

    SaveToFile()

Try(main)
