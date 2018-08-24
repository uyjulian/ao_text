﻿from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "Voice",                  # 1
        "Voice",                  # 2
        "Voice",                  # 3
        "Elie",                   # 4
        "Chairman MacDowell",     # 5
        "Jona",                   # 6
        "SE制御",                 # 7
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
        "Function_3_D62",          # 03, 3
        "Function_4_D87",          # 04, 4
        "Function_5_DE8",          # 05, 5
        "Function_6_ECF",          # 06, 6
        "Function_7_F2A",          # 07, 7
        "Function_8_F79",          # 08, 8
        "Function_9_F98",          # 09, 9
        "Function_10_FB4",         # 0A, 10
        "Function_11_FD0",         # 0B, 11
        "Function_12_30A0",        # 0C, 12
        "Function_13_3108",        # 0D, 13
        "Function_14_314D",        # 0E, 14
        "Function_15_318B",        # 0F, 15
        "Function_16_31B5",        # 10, 16
        "Function_17_31D1",        # 11, 17
        "Function_18_31E3",        # 12, 18
        "Function_19_31F5",        # 13, 19
        "Function_20_32ED",        # 14, 20
        "Function_21_3353",        # 15, 21
        "Function_22_3377",        # 16, 22
        "Function_23_33C2",        # 17, 23
        "Function_24_38F9",        # 18, 24
        "Function_25_3939",        # 19, 25
        "Function_26_3961",        # 1A, 26
        "Function_27_3989",        # 1B, 27
        "Function_28_39C8",        # 1C, 28
        "Function_29_39F0",        # 1D, 29
        "Function_30_3A51",        # 1E, 30
        "Function_31_3AB2",        # 1F, 31
        "Function_32_3B13",        # 20, 32
        "Function_33_3B74",        # 21, 33
        "Function_34_3BD5",        # 22, 34
        "Function_35_3E9A",        # 23, 35
        "Function_36_3F4F",        # 24, 36
        "Function_37_3FC4",        # 25, 37
        "Function_38_422E",        # 26, 38
        "Function_39_425D",        # 27, 39
        "Function_40_428C",        # 28, 40
        "Function_41_42A5",        # 29, 41
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
        "#00008F#11PNo one's here...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10708F#12PNo... I feel some kind\x01",
            "of presence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10401F#12PHmm. It doesn't seem to\x01",
            "be a monster, though.\x02",
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
            "Beep─ Intruders found.\x07\x00\x02",
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
        (
            "#00207F#11PA reaction from the\x01",
            "front!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00310F#11PTch... So "those\x01",
            "guys"... were him, huh?\x02",
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
            "6 targets─\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Confirmed 3 from the SSS\x01",
            "and State Guard 2nd Lt.\x01",
            "Seeker.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "2 unknowns─ However, I\x01",
            "estimate their fighting\x01",
            "power above A-rank.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x105,
        "#10407F#12P#NKh...?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x106,
        (
            "#10707F#6P#NA machine can tell that\x01",
            "much...!?\x02",
        )
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
            "Deploying the Izayoi.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Regenenkopf Mark II,\x01",
            "Muramasa─\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Entering extermination\x01",
            "mode.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        "#00010F#12P#NHere they come!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x109,
        "#10107F#12P#NCommencing attack!\x02",
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

    def lambda_CD5():
        OP_9B(0x1, 0xFE, 0x0, 0xBB8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_CD5)

    def lambda_CEA():
        OP_9B(0x1, 0xFE, 0x0, 0xBB8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_CEA)

    def lambda_CFF():
        OP_9B(0x1, 0xFE, 0x0, 0xBB8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_CFF)
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

    def Function_3_D62(): pass

    label("Function_3_D62")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D86")
    OP_82(0x0, 0x1E, 0x1388, 0x3E8)
    Sleep(1000)
    Jump("Function_3_D62")

    label("loc_D86")

    Return()

    # Function_3_D62 end

    def Function_4_D87(): pass

    label("Function_4_D87")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_DE7")
    PlayEffect(0x0, 0x0, 0xFE, 0x1, 0, 1500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x96, 0x2EE)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xC8, 0x2EE)
    StopEffect(0x0, 0x2)
    Jump("Function_4_D87")

    label("loc_DE7")

    Return()

    # Function_4_D87 end

    def Function_5_DE8(): pass

    label("Function_5_DE8")

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

    # Function_5_DE8 end

    def Function_6_ECF(): pass

    label("Function_6_ECF")

    Sound(950, 2, 100, 0)
    PlayEffect(0x0, 0x1, 0xFE, 0x1, 0, 1000, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0xBB8)
    StopEffect(0x1, 0x2)
    StopSound(950, 1000, 100)
    BeginChrThread(0xFE, 0, 0, 10)
    Sleep(1000)
    Return()

    # Function_6_ECF end

    def Function_7_F2A(): pass

    label("Function_7_F2A")

    PlayEffect(0x0, 0x2, 0xFE, 0x1, 0, 1000, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0xBB8)
    StopEffect(0x2, 0x2)
    BeginChrThread(0xFE, 0, 0, 10)
    Sleep(1000)
    Return()

    # Function_7_F2A end

    def Function_8_F79(): pass

    label("Function_8_F79")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_F97")
    OP_A1(0xFE, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_8_F79")

    label("loc_F97")

    Return()

    # Function_8_F79 end

    def Function_9_F98(): pass

    label("Function_9_F98")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_FB3")
    OP_A1(0xFE, 0x3E8, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_9_F98")

    label("loc_FB3")

    Return()

    # Function_9_F98 end

    def Function_10_FB4(): pass

    label("Function_10_FB4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_FCF")
    OP_A1(0xFE, 0x5DC, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_10_FB4")

    label("loc_FCF")

    Return()

    # Function_10_FB4 end

    def Function_11_FD0(): pass

    label("Function_11_FD0")

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

    def lambda_13B2():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_13B2)
    Sleep(50)

    def lambda_13CE():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_13CE)
    Sleep(50)

    def lambda_13EA():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_13EA)
    Sleep(50)

    def lambda_1406():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1406)
    Sleep(50)

    def lambda_1422():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_1422)
    Sleep(50)

    def lambda_143E():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_143E)
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
            "#00015F#12PKh... What a hell of a\x01",
            "machine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10708F#12P#NOuroboros is truly a\x01",
            "formidable group...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#00306F#12PYeah, to think that\x01",
            "crimson warrior doll could\x01",
            "be enhanced that much...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00211F#12P...I wonder if that\x01",
            "Doctor modded him...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10406F#12PThat seems likely...\x02",
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

    def lambda_1626():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1626)
    SetChrChipByIndex(0x101, 0x21)
    SetChrSubChip(0x101, 0x0)
    Sound(812, 0, 100, 0)
    WaitChrThread(0x101, 2)
    OP_0D()
    Fade(500)

    def lambda_1657():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1657)
    Sleep(50)

    def lambda_1673():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1673)
    Sleep(50)

    def lambda_168F():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_168F)
    Sleep(50)

    def lambda_16AB():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_16AB)
    Sleep(50)

    def lambda_16C7():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_16C7)
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

    def lambda_17D2():
        OP_93(0x103, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_17D2)
    Sleep(50)

    def lambda_17E2():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_17E2)
    Sleep(50)

    def lambda_17F2():
        OP_93(0x109, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_17F2)
    Sleep(50)

    def lambda_1802():
        OP_93(0x105, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_1802)
    Sleep(50)

    def lambda_1812():
        OP_93(0x106, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_1812)
    Sleep(50)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x106, 0)

    ChrTalk(
        0x101,
        (
            "#00004F#5PAlright, with this, the\x01",
            "obstacles should be\x01",
            "removed.\x02\x03",
            "#00000FLet's search the mansion\x01",
            "to find Elie, the\x01",
            "Chairman and─\x02",
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

    def lambda_192D():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_192D)
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
        "#00011F#6PWhat!?\x02",
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
        "#10110F#12PHow...!\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x8, 3, 0, 23)
    WaitChrThread(0x8, 3)

    def lambda_1A75():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1A75)
    Sleep(50)

    def lambda_1A85():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1A85)
    Sleep(50)

    def lambda_1A95():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_1A95)
    Sleep(50)

    def lambda_1AA5():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1AA5)
    Sleep(50)

    def lambda_1AB5():
        TurnDirection(0x106, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_1AB5)
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

    def lambda_1B13():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1B13)
    Sleep(50)

    def lambda_1B2F():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1B2F)
    Sleep(50)

    def lambda_1B4B():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1B4B)
    Sleep(50)

    def lambda_1B67():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_1B67)
    Sleep(50)

    def lambda_1B83():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_1B83)
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
        "#10107F#5PLloyd...!\x02",
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
        "Girl's Voice",
        "#3403V#1P#10AI won't let you─!\x02",
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    BeginChrThread(0x8, 3, 0, 34)
    WaitChrThread(0x8, 3)

    ChrTalk(
        0x101,
        "#00005F#5P#N#8AHuh─\x02",
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

    def lambda_1DDF():
        OP_93(0x103, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1DDF)
    Sleep(50)

    def lambda_1DEF():
        OP_93(0x104, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1DEF)
    Sleep(50)

    def lambda_1DFF():
        OP_93(0x109, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1DFF)
    Sleep(50)

    def lambda_1E0F():
        OP_93(0x105, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_1E0F)
    Sleep(50)

    def lambda_1E1F():
        OP_93(0x106, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_1E1F)
    Sleep(50)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x106, 0)
    OP_68(1000, 1500, 20000, 1500)
    SetCameraDistance(13500, 1500)

    def lambda_1E5D():
        OP_9B(0x1, 0xFE, 0x1E, 0xBB8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_1E5D)
    Sleep(50)

    def lambda_1E75():
        OP_9B(0x1, 0xFE, 0xFFE7, 0xFA0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1E75)
    Sleep(50)

    def lambda_1E8D():
        OP_9B(0x1, 0xFE, 0xFFDA, 0xBB8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1E8D)
    Sleep(50)

    def lambda_1EA5():
        OP_9B(0x1, 0xFE, 0x21, 0xBB8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1EA5)
    Sleep(50)

    def lambda_1EBD():
        OP_9B(0x1, 0xFE, 0xFFE2, 0xFA0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1EBD)
    Sleep(50)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x109, 1)
    WaitChrThread(0x105, 1)
    WaitChrThread(0x106, 1)
    OP_6F(0x79)

    ChrTalk(
        0x103,
        "#00206F#6P#6P*sigh*...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10406F#6P...Oh man.\x02",
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
        "#00002F#6P#NElie...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x101, 4700, 500, 20000, 90)

    ChrTalk(
        0x103,
        "#00202F#6P#N...Elie.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        "#00309F#6P#NHaha, so you were safe.\x02",
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
        "#00106F#40W#11P............\x02",
    )

    CloseMessageWindow()

    def lambda_2039():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2039)
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
            "#00012F#6PUhhm... What can I\x01",
            "say...\x02\x03",
            "#00004F─In any case, thank you,\x01",
            "Elie.\x02\x03",
            "#00002FI'm safe, thanks to you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#00101F#11P......!\x02",
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

    def lambda_2174():
        OP_A6(0xFE, 0x0, 0x1E, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2174)
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
        "#00011F#6P#10AW-What...!?\x02",
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
            "#3404V#40W#40AThank goodness... ...Really, thank\x01",
            "goodness...\x02\x03",
            "#3405V#40AYou're safe... ...Seeing you like\x01",
            "this...\x02\x03",
            "#3406V#40AI thought we'd... never see each\x01",
            "other again...\x02",
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
        "#00002F#6PElie...\x02",
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
        "#00309F#6P(Aah, well...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10114F#6P(Uhhm, I wonder if I\x01",
            "should call out to\x01",
            "them...?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#10706F#6P(W-What a problem...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10402F#6P(In any case, like with you\x01",
            "back then, he's got all\x01",
            "those side benefits, eh?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00211F#6P(...I don't recall that\x01",
            "happening.)\x02",
        )
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
        "#00105F#11POh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#6PHaha...\x02\x03",
            "...I'm happy, but their\x01",
            "glances are painful to\x01",
            "bear...\x02",
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
            "#00112F#11PI-It's not how it looks!\x02\x03",
            "Lloyd just got out of a\x01",
            "tough predicament and I, for\x01",
            "some reason, felt happy!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10402F#6PEeh.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00309F#6PSo that's how it is...\x02",
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
            "#00115F#11P#4SOh, enough, it's not\x01",
            "like that!\x02\x03",
            "#00112F#3STio... You too, Noｱl!\x01",
            "Don't misunderstand,\x01",
            "ok!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10112F#6PEh, um, sure...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00204F#6P#NI'll do my best.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xB,
        "#00113F#11PUuh, then, Rixia─\x02",
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xB,
        (
            "#00105F#11P#30W......Oh......\x02\x03",
            "W-Why is Rixia with you?\x02\x03",
            "#00108FNoｱl is here too, and\x01",
            "Wazy is dressed so\x01",
            "differently...\x02\x03",
            "#00105F?????\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012F#11PHaha...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10710F#6PWell... It's a long\x01",
            "story.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xC,
        "Elderly Voice",
        (
            "#3P#2SHahaha... It sure seems\x01",
            "that way, doesn't it?\x02",
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

    def lambda_2A19():

        label("loc_2A19")

        TurnDirection(0xFE, 0xC, 500)
        Yield()
        Jump("loc_2A19")

    QueueWorkItem2(0x101, 2, lambda_2A19)

    def lambda_2A2B():

        label("loc_2A2B")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_2A2B")

    QueueWorkItem2(0xB, 2, lambda_2A2B)
    BeginChrThread(0xC, 3, 0, 38)
    Sleep(300)
    BeginChrThread(0xD, 3, 0, 39)
    Sleep(3000)

    def lambda_2A4F():
        OP_98(0xFE, 0xFFFFFED4, 0x0, 0x6A4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2A4F)

    def lambda_2A69():
        OP_98(0xFE, 0xFFFFFE0C, 0x0, 0xFFFFFE0C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2A69)
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
        (
            "#00002F#5PChairman, are you all\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00205F#6P#NAnd... Jona!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#02309F#11PHi guys. Didja miss me?\x02\x03",
            "#02302FMaaan, you really are\x01",
            "lifesavers!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#00100F#11PUhhm, Bell brought him\x01",
            "here after us.\x02\x03",
            "#00106FIt seems he repeatedly\x01",
            "hacked the central part\x01",
            "of Orchis Tower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#02310F#11PThat woman, she's truly a\x01",
            "witch!\x02\x03",
            "Daring to lock me up in a\x01",
            "mansion where there's no\x01",
            "orbal net of all things!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012F#5PI-I see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00204F#6P#NIt is true that, to someone\x01",
            "like you, it could be the\x01",
            "worst punishment imaginable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#02503F#11PWell, let's leave our\x01",
            "circumstances for later.\x02\x03",
            "#02500FSo you're here to save\x01",
            "us?\x02",
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
        "#00013F#5PYes! We came to get you!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10400F#6PIf you don't have anything you\x01",
            "need in particular, would you\x01",
            "like us to get you out of here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#02503F#11PBut of course.\x02\x03",
            "#02501FAfter all, the situation\x01",
            "where I can stay quiet\x01",
            "has long since passed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#00106F#11PRight...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301F#6PAlright, let's get out of\x01",
            "here before uncle's damn\x01",
            "reinforcements come!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10101F#6PLet's take a safe path\x01",
            "back to the Merkabah!\x02",
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
            "Afterwards, Lloyd and the others met up\x01",
            "with with Zeit, who had been distracting\x01",
            "the enemy, and returned to the Merkabah...\x02\x03",
            "They succeeded in breaking away from\x01",
            "Michelam before Red Constellation's\x01",
            "reinforcements arrived.\x02\x03",
            "And then─\x07\x00\x02",
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

    # Function_11_FD0 end

    def Function_12_30A0(): pass

    label("Function_12_30A0")


    def lambda_30A5():
        OP_A6(0xFE, 0x0, 0x14, 0x7D0, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_30A5)
    WaitChrThread(0xFE, 2)
    Sound(905, 0, 70, 0)
    Sound(954, 0, 100, 0)

    def lambda_30CE():
        OP_A6(0xFE, 0x0, 0x1E, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_30CE)
    OP_A1(0xFE, 0x3E8, 0x4, 0x3, 0x2, 0x1, 0x0)
    OP_82(0x64, 0x64, 0x1388, 0x1F4)
    Sound(902, 0, 50, 0)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_12_30A0 end

    def Function_13_3108(): pass

    label("Function_13_3108")

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

    # Function_13_3108 end

    def Function_14_314D(): pass

    label("Function_14_314D")

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

    # Function_14_314D end

    def Function_15_318B(): pass

    label("Function_15_318B")

    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(500)
    SetChrChipByIndex(0xFE, 0x26)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x3E8, 0x0)
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_15_318B end

    def Function_16_31B5(): pass

    label("Function_16_31B5")

    OP_93(0xFE, 0x5A, 0x1F4)
    Sleep(750)
    OP_93(0xFE, 0x87, 0x1F4)
    Sleep(750)
    OP_93(0xFE, 0x2D, 0x1F4)
    Return()

    # Function_16_31B5 end

    def Function_17_31D1(): pass

    label("Function_17_31D1")

    OP_93(0xFE, 0x2D, 0x1F4)
    Sleep(1000)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_17_31D1 end

    def Function_18_31E3(): pass

    label("Function_18_31E3")

    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(500)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_18_31E3 end

    def Function_19_31F5(): pass

    label("Function_19_31F5")

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

    # Function_19_31F5 end

    def Function_20_32ED(): pass

    label("Function_20_32ED")

    OP_93(0xFE, 0x13B, 0x0)
    SetChrChipByIndex(0xFE, 0x33)
    SetChrSubChip(0xFE, 0x0)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x1000)
    SetChrChip(0x0, 0xFE, 0x1E, 0x12C)

    def lambda_3313():
        OP_9D(0xFE, 0x125C, 0x1F4, 0x4E20, 0x3E8, 0x1194)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3313)
    WaitChrThread(0xFE, 1)
    ClearChrFlags(0xFE, 0x20)
    ClearChrFlags(0xFE, 0x1000)
    OP_A1(0xFE, 0x5DC, 0x2, 0x2, 0x3)
    Sound(514, 0, 100, 0)
    Sleep(500)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_20_32ED end

    def Function_21_3353(): pass

    label("Function_21_3353")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3376")
    OP_A6(0x8, 0x1E, 0x1E, 0x1F4, 0x1388)
    Jump("Function_21_3353")

    label("loc_3376")

    Return()

    # Function_21_3353 end

    def Function_22_3377(): pass

    label("Function_22_3377")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_33C1")
    PlayEffect(0x8, 0xFF, 0x8, 0x0, 0, -300, -500, 0, 0, 0, 4000, 4000, 4000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    Jump("Function_22_3377")

    label("loc_33C1")

    Return()

    # Function_22_3377 end

    def Function_23_33C2(): pass

    label("Function_23_33C2")

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

    def lambda_3446():
        OP_9B(0x0, 0xFE, 0xFFEC, 0x2CEC, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3446)

    def lambda_345B():

        label("loc_345B")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_345B")

    QueueWorkItem2(0x103, 2, lambda_345B)

    def lambda_346D():

        label("loc_346D")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_346D")

    QueueWorkItem2(0x104, 2, lambda_346D)

    def lambda_347F():

        label("loc_347F")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_347F")

    QueueWorkItem2(0x109, 2, lambda_347F)

    def lambda_3491():

        label("loc_3491")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_3491")

    QueueWorkItem2(0x105, 2, lambda_3491)

    def lambda_34A3():

        label("loc_34A3")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_34A3")

    QueueWorkItem2(0x106, 2, lambda_34A3)
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
            "#00310F#5P#NTch... Is it going\x01",
            "berserk!?\x02",
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

    def lambda_35FF():
        OP_9B(0x0, 0xFE, 0x0, 0x36B0, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_35FF)

    def lambda_3614():

        label("loc_3614")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_3614")

    QueueWorkItem2(0x103, 2, lambda_3614)

    def lambda_3626():

        label("loc_3626")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_3626")

    QueueWorkItem2(0x104, 2, lambda_3626)

    def lambda_3638():

        label("loc_3638")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_3638")

    QueueWorkItem2(0x109, 2, lambda_3638)

    def lambda_364A():

        label("loc_364A")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_364A")

    QueueWorkItem2(0x105, 2, lambda_364A)

    def lambda_365C():

        label("loc_365C")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_365C")

    QueueWorkItem2(0x106, 2, lambda_365C)
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

    def lambda_3784():
        OP_9D(0xFE, 0xA8C, 0x1F4, 0x56B8, 0xBB8, 0x1194)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3784)

    def lambda_37A1():

        label("loc_37A1")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_37A1")

    QueueWorkItem2(0x103, 2, lambda_37A1)

    def lambda_37B3():

        label("loc_37B3")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_37B3")

    QueueWorkItem2(0x104, 2, lambda_37B3)

    def lambda_37C5():

        label("loc_37C5")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_37C5")

    QueueWorkItem2(0x109, 2, lambda_37C5)

    def lambda_37D7():

        label("loc_37D7")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_37D7")

    QueueWorkItem2(0x105, 2, lambda_37D7)

    def lambda_37E9():

        label("loc_37E9")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_37E9")

    QueueWorkItem2(0x106, 2, lambda_37E9)
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

    def lambda_3897():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_3897)
    Sleep(50)

    def lambda_38A7():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_38A7)
    Sleep(50)

    def lambda_38B7():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_38B7)
    Sleep(50)

    def lambda_38C7():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_38C7)
    Sleep(50)

    def lambda_38D7():
        TurnDirection(0x106, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_38D7)
    Sleep(50)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x106, 0)
    OP_6F(0x79)
    Return()

    # Function_23_33C2 end

    def Function_24_38F9(): pass

    label("Function_24_38F9")


    ChrTalk(
        0x103,
        "#00210F#6PEek...!?\x05\x02",
    )

    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x2)
    OP_9D(0xFE, 0xFFFFFF9C, 0x1F4, 0x40A6, 0x3E8, 0x1388)
    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_24_38F9 end

    def Function_25_3939(): pass

    label("Function_25_3939")

    SetChrChipByIndex(0xFE, 0x2F)
    SetChrSubChip(0xFE, 0x2)
    OP_9D(0xFE, 0xFFFFF22C, 0x1F4, 0x49B6, 0x3E8, 0x1388)
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_25_3939 end

    def Function_26_3961(): pass

    label("Function_26_3961")

    SetChrChipByIndex(0xFE, 0x30)
    SetChrSubChip(0xFE, 0x2)
    OP_9D(0xFE, 0xFFFFFB5A, 0x1F4, 0x4998, 0x3E8, 0x1388)
    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_26_3961 end

    def Function_27_3989(): pass

    label("Function_27_3989")

    SetChrChipByIndex(0xFE, 0x31)
    SetChrSubChip(0xFE, 0x2)
    OP_9D(0xFE, 0xFFFFFBBE, 0x1F4, 0x4376, 0x3E8, 0x1388)
    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x0)

    ChrTalk(
        0x105,
        "#10410F#5PDamn...\x05\x02",
    )

    Return()

    # Function_27_3989 end

    def Function_28_39C8(): pass

    label("Function_28_39C8")

    SetChrChipByIndex(0xFE, 0x32)
    SetChrSubChip(0xFE, 0x2)
    OP_9D(0xFE, 0xFFFFF5D8, 0x1F4, 0x42AE, 0x3E8, 0x1388)
    SetChrChipByIndex(0xFE, 0x2B)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_28_39C8 end

    def Function_29_39F0(): pass

    label("Function_29_39F0")

    Sound(501, 0, 70, 0)
    PlayEffect(0x0, 0xFF, 0xFE, 0x0, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x2)
    OP_9D(0xFE, 0xFFFFFBC8, 0x1F4, 0x3DB8, 0x3E8, 0x1388)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_29_39F0 end

    def Function_30_3A51(): pass

    label("Function_30_3A51")

    Sound(501, 0, 70, 0)
    PlayEffect(0x0, 0xFF, 0xFE, 0x0, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0xFE, 0x2F)
    SetChrSubChip(0xFE, 0x2)
    OP_9D(0xFE, 0xFFFFE93A, 0x1F4, 0x5014, 0x3E8, 0x1388)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_30_3A51 end

    def Function_31_3AB2(): pass

    label("Function_31_3AB2")

    Sound(501, 0, 70, 0)
    PlayEffect(0x0, 0xFF, 0xFE, 0x0, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0xFE, 0x30)
    SetChrSubChip(0xFE, 0x2)
    OP_9D(0xFE, 0xFFFFF4A2, 0x1F4, 0x45D8, 0x3E8, 0x1388)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_31_3AB2 end

    def Function_32_3B13(): pass

    label("Function_32_3B13")

    Sound(501, 0, 70, 0)
    PlayEffect(0x0, 0xFF, 0xFE, 0x0, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0xFE, 0x31)
    SetChrSubChip(0xFE, 0x2)
    OP_9D(0xFE, 0xFFFFF47A, 0x1F4, 0x3FDE, 0x3E8, 0x1388)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_32_3B13 end

    def Function_33_3B74(): pass

    label("Function_33_3B74")

    Sound(501, 0, 70, 0)
    PlayEffect(0x0, 0xFF, 0xFE, 0x0, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0xFE, 0x32)
    SetChrSubChip(0xFE, 0x2)
    OP_9D(0xFE, 0xFFFFEAD4, 0x1F4, 0x4902, 0x3E8, 0x1388)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_33_3B74 end

    def Function_34_3BD5(): pass

    label("Function_34_3BD5")

    Sound(530, 0, 100, 0)
    Sound(566, 0, 50, 0)
    PlayEffect(0x9, 0xFF, 0xFF, 0x0, 15000, 2500, 20000, 282, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    Sound(902, 0, 100, 0)
    PlayEffect(0x3, 0xFF, 0xFE, 0x1, 0, 2000, 0, 270, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)

    def lambda_3C5D():
        OP_A6(0xFE, 0x0, 0x4B, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3C5D)
    SetChrChipByIndex(0xFE, 0x3A)
    SetChrSubChip(0xFE, 0x3)
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0xAF0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(2600, 2300, 22500, 150)
    OP_82(0x12C, 0x12C, 0x1388, 0x12C)

    def lambda_3CAB():
        OP_96(0xFE, 0x79E, 0x1F4, 0x5A6E, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3CAB)
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

    def lambda_3D55():
        OP_A6(0xFE, 0x0, 0x4B, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3D55)
    SetChrSubChip(0xFE, 0x2)
    OP_68(1150, 2300, 22050, 150)
    OP_82(0x12C, 0x12C, 0x1388, 0x12C)

    def lambda_3D94():
        OP_96(0xFE, 0x258, 0x1F4, 0x5816, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3D94)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    OP_6F(0x79)
    Sound(530, 0, 100, 0)
    Sound(566, 0, 50, 0)
    PlayEffect(0x9, 0xFF, 0xFF, 0x0, 15000, 2500, 20000, 278, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    Sound(902, 0, 100, 0)
    PlayEffect(0x3, 0xFF, 0xFE, 0x1, 0, 2000, 0, 270, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)

    def lambda_3E3B():
        OP_A6(0xFE, 0x0, 0x4B, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3E3B)
    SetChrSubChip(0xFE, 0x1)
    OP_68(850, 2300, 23100, 150)
    OP_82(0x12C, 0x12C, 0x1388, 0x12C)

    def lambda_3E7A():
        OP_96(0xFE, 0x0, 0x1F4, 0x5DC0, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3E7A)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    OP_6F(0x79)
    Return()

    # Function_34_3BD5 end

    def Function_35_3E9A(): pass

    label("Function_35_3E9A")

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
        "#00307F#3POraaah!\x05\x02",
    )

    Sound(532, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x34)
    OP_A1(0xFE, 0x5DC, 0x3, 0x0, 0x1, 0x2)
    BeginChrThread(0x8, 3, 0, 37)
    OP_A1(0xFE, 0x5DC, 0x3, 0x3, 0x4, 0x5)
    WaitChrThread(0x8, 3)
    EndChrThread(0x8, 0x0)
    Return()

    # Function_35_3E9A end

    def Function_36_3F4F(): pass

    label("Function_36_3F4F")

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
        "#10707F#4PHaah...!\x05\x02",
    )

    Sound(538, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x35)
    OP_A1(0xFE, 0x5DC, 0x3, 0x0, 0x1, 0x2)
    OP_A1(0xFE, 0x5DC, 0x3, 0x3, 0x4, 0x5)
    Return()

    # Function_36_3F4F end

    def Function_37_3FC4(): pass

    label("Function_37_3FC4")

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

    # Function_37_3FC4 end

    def Function_38_422E(): pass

    label("Function_38_422E")

    ClearChrFlags(0xFE, 0x4)

    def lambda_4238():
        OP_9B(0x0, 0xFE, 0x0, 0x2EE0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4238)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_38_422E end

    def Function_39_425D(): pass

    label("Function_39_425D")

    ClearChrFlags(0xFE, 0x4)

    def lambda_4267():
        OP_9B(0x0, 0xFE, 0x0, 0x2EE0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4267)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_39_425D end

    def Function_40_428C(): pass

    label("Function_40_428C")

    Sound(203, 0, 60, 0)
    Sleep(900)
    Sound(203, 0, 70, 0)
    Sleep(1100)
    Sound(203, 0, 60, 0)
    Return()

    # Function_40_428C end

    def Function_41_42A5(): pass

    label("Function_41_42A5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_42D9")
    Sound(203, 0, 60, 0)
    Sleep(900)
    Sound(203, 0, 70, 0)
    Sleep(1100)
    Sound(203, 0, 60, 0)
    Sleep(800)
    Sound(203, 0, 50, 0)
    Sleep(1000)
    Jump("Function_41_42A5")

    label("loc_42D9")

    Return()

    # Function_41_42A5 end

    SaveToFile()

Try(main)
