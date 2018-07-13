from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "m4290.bin",                # FileName
        "m4290",                    # MapName
        "m4290",                    # Location
        0x007F,                     # MapIndex
        "ed7573",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x29,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 127, 0, 0, 0, 1],
    )

    BuildStringList((
        "m4290",                  # 0
        "Dr. Novartis",           # 1
        "Campanella The Fool",    # 2
        "Arianrhod",              # 3
        "Yin",                    # 4
        "Rixia",                  # 5
        "Bracer Scott",           # 6
        "Bracer Wenzel",          # 7
        "Arios",                  # 8
        "Knight Dressed Girl",    # 9
        "Knight Dressed Girl",    # 10
        "Knight Dressed Girl",    # 11
        "スフィンキマイラ",       # 12
        "SE制御",                 # 13
        "APL表示用",              # 14
        "bm4210",                 # 15
    ))

    ATBonus("ATBonus_24C", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_30C", 8, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_310", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_314", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_318", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_31C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_320", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_324", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_328", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2EC", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_2F0", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_2F4", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_2F8", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_2FC", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_300", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_304", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_308", 5, 5, 45)

    # monster count: 0

    # event battle count: 1

    BattleInfo(
        "BattleInfo_32C", 0x0042, 72, 6, 45, 3, 3, 30, 0, "bm4210", 0x00000000, 100, 0, 0, 0,
        (
            ("ms88400.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_30C", "MonsterBattlePostion_2EC", "ed7454", "ed7453", "ATBonus_24C"),
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
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(1052, 0)                                       # 0

    ScpFunction((
        "Function_0_41C",          # 00, 0
        "Function_1_43D",          # 01, 1
        "Function_2_480",          # 02, 2
        "Function_3_2788",         # 03, 3
        "Function_4_27C4",         # 04, 4
        "Function_5_2800",         # 05, 5
        "Function_6_283C",         # 06, 6
        "Function_7_2878",         # 07, 7
        "Function_8_28B4",         # 08, 8
        "Function_9_28E6",         # 09, 9
        "Function_10_2BED",        # 0A, 10
        "Function_11_2C74",        # 0B, 11
        "Function_12_2D3D",        # 0C, 12
        "Function_13_2D46",        # 0D, 13
        "Function_14_2D4F",        # 0E, 14
        "Function_15_2D58",        # 0F, 15
        "Function_16_2D61",        # 10, 16
        "Function_17_2D6A",        # 11, 17
        "Function_18_2D73",        # 12, 18
        "Function_19_7020",        # 13, 19
        "Function_20_7042",        # 14, 20
        "Function_21_718E",        # 15, 21
        "Function_22_71A1",        # 16, 22
        "Function_23_7296",        # 17, 23
        "Function_24_7300",        # 18, 24
        "Function_25_731F",        # 19, 25
        "Function_26_7430",        # 1A, 26
        "Function_27_749C",        # 1B, 27
        "Function_28_7548",        # 1C, 28
        "Function_29_75E8",        # 1D, 29
        "Function_30_7688",        # 1E, 30
        "Function_31_772E",        # 1F, 31
        "Function_32_77CE",        # 20, 32
        "Function_33_7867",        # 21, 33
        "Function_34_799F",        # 22, 34
        "Function_35_7AC2",        # 23, 35
        "Function_36_7AD5",        # 24, 36
        "Function_37_7B0A",        # 25, 37
        "Function_38_7BFC",        # 26, 38
        "Function_39_7C17",        # 27, 39
        "Function_40_7C57",        # 28, 40
        "Function_41_7C95",        # 29, 41
        "Function_42_7CAE",        # 2A, 42
    ))


    def Function_0_41C(): pass

    label("Function_0_41C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_42D")
    Event(0, 2)

    label("loc_42D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_43C")
    ClearScenarioFlags(0x22, 0)
    Event(0, 18)

    label("loc_43C")

    Return()

    # Function_0_41C end

    def Function_1_43D(): pass

    label("Function_1_43D")

    SoundDistance(0x7A, 0xFFFFB06E, 0xBC2, 0xFFFFD008, 0x4E20, 0x186A0, 0x64, 0x0)
    OP_E3(0x24E, 0xFFFFFD12, 0x6004)
    OP_E3(0x7DBD, 0xFFFFFD12, 0x14DC)
    Sound(123, 1, 80, 0)
    SetMapObjFlags(0x0, 0x4)
    Return()

    # Function_1_43D end

    def Function_2_480(): pass

    label("Function_2_480")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch13400.itc", 0x1E)
    LoadChrToIndex("chr/ch03600.itc", 0x1F)
    LoadChrToIndex("chr/ch03500.itc", 0x20)
    LoadChrToIndex("chr/ch00050.itc", 0x21)
    LoadChrToIndex("chr/ch00150.itc", 0x22)
    LoadChrToIndex("chr/ch00250.itc", 0x23)
    LoadChrToIndex("chr/ch00350.itc", 0x24)
    LoadChrToIndex("chr/ch00550.itc", 0x26)
    SoundLoad(3887)
    SoundLoad(3888)
    SoundLoad(3889)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4E0")
    LoadChrToIndex("chr/ch02950.itc", 0x25)
    Jump("loc_4E6")

    label("loc_4E0")

    LoadChrToIndex("chr/ch03050.itc", 0x25)

    label("loc_4E6")

    LoadEffect(0x7, "event/ev10008.eff")
    LoadEffect(0x0, "event/ev10017.eff")
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu04700.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu04900.itp")
    SetChrPos(0x101, -800, -750, -26000, 0)
    SetChrPos(0x102, 600, -750, -26000, 0)
    SetChrPos(0x103, -1100, -750, -27400, 0)
    SetChrPos(0x104, 900, -750, -27400, 0)
    SetChrPos(0x106, -800, -750, -28800, 0)
    SetChrPos(0xF4, 600, -750, -28800, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrPos(0x8, -2300, 250, 7600, 315)
    SetChrFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrPos(0x9, -900, 250, 7400, 0)
    SetChrFlags(0x9, 0x8000)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrChipByIndex(0xA, 0x20)
    SetChrPos(0xA, 600, 250, 7600, 45)
    SetChrFlags(0xA, 0x8000)
    OP_52(0xA, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapObjFlags(0x0, 0x1000)
    OP_78(0x0, 0x13)
    OP_68(-290, 750, -25000, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(750, 0)
    SetCameraDistance(17000, 0)
    FadeToBright(1000, 0)
    OP_68(-720, 2250, -20050, 3000)
    MoveCamera(52, 18, 0, 3000)
    OP_6E(750, 3000)
    SetCameraDistance(17000, 3000)

    def lambda_6DF():
        OP_9B(0x0, 0xFE, 0x0, 0x1F40, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6DF)
    Sleep(100)

    def lambda_6F7():
        OP_9B(0x0, 0x102, 0x0, 0x1F40, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_6F7)
    Sleep(50)

    def lambda_70F():
        OP_9B(0x0, 0x103, 0x0, 0x1F40, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_70F)
    Sleep(50)

    def lambda_727():
        OP_9B(0x0, 0x104, 0x0, 0x1F40, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_727)
    Sleep(50)

    def lambda_73F():
        OP_9B(0x0, 0xF4, 0x0, 0x1F40, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_73F)
    Sleep(50)

    def lambda_757():
        OP_9B(0x0, 0x106, 0x0, 0x1F40, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_757)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0x106, 0)
    WaitChrThread(0x101, 2)
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
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00011F#6P(W-What is this place...!)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00205F#12P#N(Amazing... It looks like enormous\x01",
            "energy is gathering here...)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#00311F#12P(Also...\x01",
            "As expected, there they're.)\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    SetCameraDistance(12000, 4000)
    OP_68(-800, 2250, 1500, 4000)
    MoveCamera(0, 14, 0, 4000)
    OP_6E(810, 4000)
    OP_6F(0x79)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7580", 0)
    Fade(500)
    OP_68(-800, 12550, 2650, 0)
    MoveCamera(0, 14, 0, 0)
    OP_6E(810, 0)
    SetCameraDistance(5000, 0)
    OP_68(-800, 2750, 1500, 5000)
    OP_6F(0x79)
    Sleep(500)

    ChrTalk(
        0x9,
        (
            "#04809F#6PUhuhu...\x01",
            "This is a staggering place.\x02\x03",
            "#04800FSince you enlivened it this much, I\x01",
            "guess that preparations are complete?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "White-Robed Man",
        "#04704F#11PHu hu, I wonder.\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0x86, 0x1F4)
    Sleep(200)

    NpcTalk(
        0x8,
        "White-Robed Man",
        (
            "#04702F#5PYes, yes, it seems it's become\x01",
            "surely an interesting spectacle.\x02\x03",
            "If "The Faceless" was alive,\x01",
            "I'm sure he'd be enjoying it.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x9, 0xE1, 0x1F4)
    Sleep(100)

    ChrTalk(
        0x9,
        (
            "#04809F#11PAhaha, no doubt.\x02\x03",
            "#04805FHowever, if even the Professor had come\x01",
            "to Crossbell in addition to you, Doctor, \x01",
            "maybe things would've gone out of hand.\x02\x03",
            "#04802FHe'd have even brought out the "Glorious" and\x01",
            "picked up a fight with the two major powers.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "White-Robed Man",
        (
            "#04709F#5PHa ha, wouldn't have that been\x01",
            "quite interesting in its own way?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xA,
        "Armored Character",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5P............\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    def lambda_C52():
        OP_9B(0x0, 0xFE, 0x166, 0x1F40, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C52)

    def lambda_C67():
        OP_9B(0x0, 0xFE, 0x166, 0x1F40, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C67)

    def lambda_C7C():
        OP_9B(0x0, 0xFE, 0x166, 0x1F40, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_C7C)

    def lambda_C91():
        OP_9B(0x0, 0xFE, 0x166, 0x1F40, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_C91)

    def lambda_CA6():
        OP_9B(0x0, 0xFE, 0x166, 0x1F40, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_CA6)

    def lambda_CBB():
        OP_9B(0x0, 0xFE, 0x166, 0x1F40, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_CBB)
    OP_63(0x9, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x9, 0x87, 0x1F4)

    ChrTalk(
        0x9,
        (
            "#04805F#5POh, what's wrong?\x02\x03",
            "#04800FLike I thought, these kind of missions are\x01",
            "too simple and don't have any appeal to you?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xA,
        "Armored Character",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5P──Everything is as per that person's will.\x01",
            "I have nothing to object.\x02\x03",
            "More importantly, Doctor, Campanella.\x01",
            "Leave the chitchat to that.\x02\x03",
            "It appears we have guests.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x9, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(-800, 2250, -4500, 2500)
    MoveCamera(0, 25, 0, 2500)
    SetCameraDistance(16000, 2500)
    OP_93(0xA, 0xB4, 0x1F4)
    Sleep(50)

    def lambda_E87():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_E87)
    Sleep(50)

    def lambda_E97():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_E97)
    WaitChrThread(0x101, 1)

    def lambda_EA8():
        OP_9B(0x0, 0xFE, 0x166, 0x2710, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_EA8)
    Sleep(50)

    def lambda_EC0():
        OP_9B(0x0, 0xFE, 0x166, 0x2710, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_EC0)
    Sleep(50)

    def lambda_ED8():
        OP_9B(0x0, 0xFE, 0x166, 0x2710, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_ED8)
    Sleep(50)

    def lambda_EF0():
        OP_9B(0x0, 0xFE, 0x166, 0x2710, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_EF0)
    Sleep(50)

    def lambda_F08():
        OP_9B(0x0, 0xFE, 0x166, 0x2710, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_F08)
    Sleep(50)

    def lambda_F20():
        OP_9B(0x0, 0xFE, 0x166, 0x2710, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_F20)
    OP_6F(0x79)
    Fade(500)
    OP_68(-6700, 2150, -2690, 0)
    MoveCamera(47, 8, -1, 0)
    OP_6E(630, 0)
    SetCameraDistance(10290, 0)
    SetCameraDistance(9290, 2000)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0xF4, 1)
    WaitChrThread(0x106, 1)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#00013F#12P............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00107F#12P...Y-You...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#00702F#12P#N...It looks like more monsters than\x01",
            "I could imagine are gathered here.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x9,
        (
            "#04805F#5PAah, it's you guys.\x02\x03",
            "#04804FThe Bracers women couldn't take\x01",
            "things into their own hands, but...\x02\x03",
            "#04802FUhuhu, how were you able\x01",
            "to locate this place?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00203F......#12P#NWell, it is a trade secret.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#00301F#12P#NAt any rate, weren't you sayin'\x01",
            "a lot of interesting things...?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_119D")

    ChrTalk(
        0x109,
        (
            "#10107F#12P#NYour plan...\x01",
            "We can't overlook it!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11DF")

    label("loc_119D")


    ChrTalk(
        0x105,
        (
            "#10302F#12P#NI guess we really can't\x01",
            "overlook what you said.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11DF")

    OP_57(0x0)
    OP_5A()

    NpcTalk(
        0x8,
        "White-Robed Man",
        (
            "#04703F#5PHm...\x02\x03",
            "#04701FYou're the Crossbell police\x01",
            "newcomers, I presume?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F......#12PCrossbell Police,\x01",
            ""Special Support Section".\x02\x03",
            "#00008FI suppose you're related to\x01",
            "the Society of "Ouroboros"...\x02\x03",
            "#00001FFirst of all, could you\x01",
            "reveal your identities?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x9, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    NpcTalk(
        0x8,
        "White-Robed Man",
        (
            "#04705F#5PReveal our identities...?\x01",
            "What is he saying?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#04806F#5PHmm, could he be going through the\x01",
            "due formalities as a policeman?\x02\x03",
            "#04802FUhuhu, we can only think as a bad joke\x01",
            "revealing our identities to our opponents.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xA,
        "Armored Character",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5PYou are an upright young man.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xA,
        "Armored Character",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5PI feel sorry to not be able\x01",
            "to answer your question...\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F...#11PNo use, Lloyd.\x02\x03",
            "#00301FIt seems that common sense\x01",
            "doesn't work with these guys.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#00700F#12P#NYou should probably consider them\x01",
            "the same like the "Cult" ones.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    NpcTalk(
        0x8,
        "White-Robed Man",
        (
            "#04703F#5PHmph, being put in the same league\x01",
            "with them isn't really funny, you know.\x02\x03",
            "#04702FHu hu...very well.\x01",
            "I will at least introduce myself.\x02",
        )
    )

    CloseMessageWindow()
    OP_9B(0x1, 0x8, 0x0, 0x190, 0x320, 0x0)
    Sleep(300)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("White-Robed Man")

    AnonymousTalk(
        0xFF,
        (
            "I'm F. Novartis.\x02\x03",
            "I'm "Ouroboros" 6th Anguis,\x01",
            "also in charge of the \x01",
            ""Thirteen Workshops".\x02\x03",
            "Uh uh, please call\x01",
            "me "Doctor" freely.\x02",
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
        0x103,
        (
            "#00203F#12P#N...I see.\x01",
            "It was your doing, then.\x02\x03",
            "#00201FThe development of the mysterious code\x01",
            "used to hack the orbal net, I mean.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#04705F#1PHoo...!?\x01",
            "You can understand that code!?\x02\x03",
            "#04709FThat's called "Astral Code", you know!\x01",
            "It's used in the Society network and──\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#04801F#5PDoctor, Doctor.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04703F#5PNow that I think about it, there was\x01",
            "a girl among the Cult test subjects who \x01",
            "the Epstein folks had taken with them...\x02\x03",
            "#04702F──What do you say!?\x01",
            "Don't you want to make use of\x01",
            "that talent for the "Society"!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00211F#12P#NI refuse.\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    OP_82(0x64, 0x0, 0xBB8, 0x190)

    ChrTalk(
        0x8,
        "#04705F#5P#4S*ack!*\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0xF4, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1200)

    ChrTalk(
        0x9,
        (
            "#04806F#5PHonestly...\x01",
            "Just because Renne has run away,\x01",
            "aren't you really too desperate?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04701F#5PW-What happened with Renne has\x01",
            "nothing to do with this, you know?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xA,
        "Armored Character",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5P──Well, it is my turn then.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_9B(0x1, 0xA, 0x0, 0x190, 0x320, 0x0)
    Fade(500)
    OP_68(-3520, 2450, 2610, 0)
    MoveCamera(53, 7, -1, 0)
    OP_6E(630, 0)
    SetCameraDistance(7100, 0)
    OP_0D()
    Sleep(300)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    OP_C9(0x0, 0x80000000)
    SetChrName("Armored Character")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#3887V#40WMy name is Arianrhod.\x02\x03",
            "#3888VI am "Ouroboros"\x01",
            "7th Anguis, designated\x01",
            "with the name of "Steel".\x02\x03",
            "#3889VIt is a pleasure to make\x01",
            "your acquaintance.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xF31)
    OP_C9(0x1, 0x80000000)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)

    ChrTalk(
        0x101,
        "#00011F#12P#N......\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        "#00108F#12P#NWhat a limpid voice...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#00301F#12P#NIt's wearing a bulky armor,\x01",
            "but it seems she's a woman...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D79")

    ChrTalk(
        0x109,
        (
            "#10108F#12P#NW-What an unbelievable\x01",
            "intimidating air...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DB7")

    label("loc_1D79")


    ChrTalk(
        0x105,
        (
            "#10301F#12P#N...What an unbelievable\x01",
            "intimidating air...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DB7")

    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#00700F#12P#N...So you're the "Society"\x01",
            "strongest warrior, eh?\x02\x03",
            "It really seems you possess a\x01",
            "shuddering fighting spirit, but──\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-2330, 1950, -5470, 2000)
    MoveCamera(14, 13, -1, 2000)
    OP_6E(630, 2000)
    SetCameraDistance(9290, 2000)
    Sound(540, 0, 70, 0)
    SetChrChipByIndex(0x106, 0x26)
    SetChrSubChip(0x106, 0x0)
    Sleep(1500)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    BeginChrThread(0xF4, 3, 0, 7)
    BeginChrThread(0x103, 3, 0, 5)
    BeginChrThread(0x104, 3, 0, 6)
    BeginChrThread(0x101, 3, 0, 3)
    BeginChrThread(0x102, 3, 0, 4)
    WaitChrThread(0xF4, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x106, 3)
    Sleep(150)

    ChrTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#00702F#6P──I wonder, how much of that composure\x01",
            "could you maintain in front of me, "Yin"?\x07\x00\x02",
        )
    )

    OP_6F(0x79)
    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#04900F#11P#N.......................................\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        "#00011F#5PH-Hey, "Yin"...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108F#11PWhy did you...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#04804F#5P#NUhuhu, I think you have quite the\x01",
            "very interesting fighting card, but...\x02\x03",
            "#04800FBefore that, it appears that the\x01",
            "guardian of this place has come back.\x02",
        )
    )

    OP_6F(0x79)
    CloseMessageWindow()

    def lambda_20DD():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_20DD)
    Sleep(50)

    def lambda_20ED():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_20ED)
    Sleep(50)

    def lambda_20FD():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_20FD)
    Sleep(50)

    def lambda_210D():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_210D)
    Sleep(50)

    def lambda_211D():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_211D)
    Sleep(100)

    ChrTalk(
        0x101,
        "#00005F#6PWhat...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2173")

    ChrTalk(
        0x109,
        "#10105F#12P"Guardian"...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2192")

    label("loc_2173")


    ChrTalk(
        0x105,
        "#10305F#12P"Guardian"...?\x02",
    )

    CloseMessageWindow()

    label("loc_2192")

    Sleep(100)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    StopBGM(0xFA0)

    ChrTalk(
        0x103,
        (
            "#00208F#6PGigantic aura approaching, confirmed...\x02\x03",
            "#00207FA large-scale Cryptid is coming!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetCameraDistance(11290, 5000)

    def lambda_22A4():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_22A4)
    Sleep(50)

    def lambda_22B4():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_22B4)
    Sleep(50)

    def lambda_22C4():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_22C4)
    Sleep(50)

    def lambda_22D4():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_22D4)
    Sleep(50)

    def lambda_22E4():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_22E4)
    Sleep(50)

    def lambda_22F4():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_22F4)
    Sleep(150)

    ChrTalk(
        0x104,
        "#00307F#5PWhat...!?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_234E")

    ChrTalk(
        0x109,
        "#10101F#5PF-From where...!?\x02",
    )

    CloseMessageWindow()
    Jump("loc_237A")

    label("loc_234E")


    ChrTalk(
        0x105,
        "#10308F#5PWhere is it coming from...!?\x02",
    )

    CloseMessageWindow()

    label("loc_237A")

    WaitBGM()
    Sleep(10)
    PlayBGM("ed7454", 0)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 35000, 7000, -1870, 270)
    OP_93(0x13, 0x10E, 0x0)
    OP_A7(0x13, 0xFF, 0xFF, 0xFF, 0x0, 0x5A)
    SetChrFlags(0x13, 0x1)
    OP_52(0x13, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1B58), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapObjFlags(0x0, 0x4)
    OP_70(0x0, 0xE5)
    OP_68(8260, 2850, -1360, 0)
    MoveCamera(72, 16, 0, 0)
    OP_6E(810, 0)
    SetCameraDistance(11450, 0)
    Fade(500)
    BeginChrThread(0x13, 0, 0, 9)
    WaitChrThread(0x13, 0)

    def lambda_2411():
        OP_93(0x101, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2411)
    Sleep(50)

    def lambda_2421():
        OP_93(0x102, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_2421)
    Sleep(50)

    def lambda_2431():
        OP_93(0x103, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_2431)
    Sleep(50)

    def lambda_2441():
        OP_93(0x104, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_2441)
    Sleep(50)

    def lambda_2451():
        OP_93(0x106, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_2451)
    Sleep(50)

    def lambda_2461():
        OP_93(0xF4, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_2461)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x106, 0)
    WaitChrThread(0xF4, 0)
    OP_6F(0x79)
    WaitChrThread(0x13, 0)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x106, 2)
    WaitChrThread(0x104, 2)
    WaitChrThread(0x102, 2)
    WaitChrThread(0xF4, 2)
    BeginChrThread(0x103, 3, 0, 14)
    Sleep(50)
    BeginChrThread(0x106, 3, 0, 17)
    Sleep(50)
    BeginChrThread(0x101, 3, 0, 12)
    Sleep(50)
    BeginChrThread(0x104, 3, 0, 15)
    Sleep(50)
    BeginChrThread(0xF4, 3, 0, 16)
    Sleep(50)
    BeginChrThread(0x102, 3, 0, 13)
    Sleep(50)
    OP_6F(0x79)
    WaitChrThread(0x101, 3)
    Sleep(500)
    SetChrPos(0x101, -1040, -750, -890, 90)
    SetChrPos(0x102, -2590, -750, 20, 90)

    ChrTalk(
        0x101,
        "#00007F#6P#NWha...!?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        "#00110F#6P#NT-This monster is...!?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x9,
        (
            "#04804F#6P#NThe "Sphinximera" Cryptid...\x02\x03",
            "#04802FThe divine flower garden guardian\x01",
            "made with ancient illusions, was it?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x8,
        (
            "#04704F#6P#NDear me, to think that even such\x01",
            "a thing is materializing...\x02\x03",
            "#04702FHu hu, well, I can have expectations\x01",
            "for the plan's accuracy too.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(300)
    BeginChrThread(0x13, 0, 0, 10)
    WaitChrThread(0x13, 0)
    OP_68(-830, 2050, -5110, 2000)
    MoveCamera(52, 7, -1, 2000)
    OP_6E(530, 2000)
    SetCameraDistance(14680, 2000)
    OP_6F(0x79)
    Sleep(500)

    ChrTalk(
        0x101,
        "#00010F#6P#NKh...!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#00310F#6P#NTch...!\x01",
            "If you're targetin' someone, target those guys!!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#00707F#6P#N──Save the talks for later!\x01",
            "Let's exorcise it quickly!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x13, 0, 0, 11)
    WaitChrThread(0x13, 0)
    Battle("BattleInfo_32C", 0x0, 0x0, 0x0, 0x28, 0xFF)
    FadeToDark(0, 0, -1)
    OP_CC(0x1, 0xFF, 0x0)
    Call(0, 18)
    Return()

    # Function_2_480 end

    def Function_3_2788(): pass

    label("Function_3_2788")


    def lambda_278D():
        OP_9B(0x1, 0xFE, 0x66, 0xFFFFFD12, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_278D)

    def lambda_27A2():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_27A2)
    WaitChrThread(0xFE, 2)

    def lambda_27B3():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_27B3)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_3_2788 end

    def Function_4_27C4(): pass

    label("Function_4_27C4")


    def lambda_27C9():
        OP_9B(0x1, 0xFE, 0x126, 0xFFFFFD12, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_27C9)

    def lambda_27DE():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_27DE)
    WaitChrThread(0xFE, 2)

    def lambda_27EF():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_27EF)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_4_27C4 end

    def Function_5_2800(): pass

    label("Function_5_2800")


    def lambda_2805():
        OP_9B(0x1, 0xFE, 0x66, 0xFFFFFEA2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2805)

    def lambda_281A():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_281A)
    WaitChrThread(0xFE, 2)

    def lambda_282B():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_282B)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_5_2800 end

    def Function_6_283C(): pass

    label("Function_6_283C")


    def lambda_2841():
        OP_9B(0x1, 0xFE, 0x126, 0xFFFFFEA2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2841)

    def lambda_2856():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2856)
    WaitChrThread(0xFE, 2)

    def lambda_2867():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2867)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_6_283C end

    def Function_7_2878(): pass

    label("Function_7_2878")


    def lambda_287D():
        OP_9B(0x1, 0xFE, 0x126, 0xFFFFFF6A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_287D)

    def lambda_2892():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2892)
    WaitChrThread(0xFE, 2)

    def lambda_28A3():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_28A3)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0x13, 2)
    Return()

    # Function_7_2878 end

    def Function_8_28B4(): pass

    label("Function_8_28B4")

    OP_68(-4000, 1950, -6700, 800)
    MoveCamera(21, 12, -1, 800)
    OP_6F(0x79)
    OP_68(-4650, 1950, -8700, 800)
    OP_6F(0x79)
    Return()

    # Function_8_28B4 end

    def Function_9_28E6(): pass

    label("Function_9_28E6")

    OP_68(17070, 10650, -6540, 0)
    MoveCamera(48, 5, 0, 0)
    OP_6E(810, 0)
    SetCameraDistance(7630, 0)
    Fade(500)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    CancelBlur(1300)
    OP_68(17070, 10650, -6540, 1650)
    MoveCamera(312, 24, 0, 1650)
    OP_6E(810, 1650)
    SetCameraDistance(7630, 1650)
    Sound(914, 0, 100, 0)
    Sound(251, 0, 100, 0)
    Sound(834, 0, 100, 0)
    OP_74(0x0, 0xA)
    OP_71(0x0, 0xE5, 0xEF, 0x0, 0x0)
    CloseMessageWindow()
    OP_96(0xFE, 0x3A98, 0x1B58, 0xFFFFF8B2, 0x4268, 0x0)
    OP_74(0x0, 0x1E)
    OP_68(9820, 9950, -1820, 0)
    MoveCamera(82, 49, 0, 0)
    OP_6E(810, 0)
    SetCameraDistance(12750, 0)
    Fade(500)
    PlayEffect(0x0, 0x0, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(990, 0, 100, 0)
    OP_68(9820, 1350, -1820, 1500)
    MoveCamera(67, 7, 0, 1500)
    OP_6E(810, 1500)
    SetCameraDistance(10570, 1500)

    def lambda_2A36():
        OP_9D(0xFE, 0x29F4, 0xFFFFFE0C, 0xFFFFF8B2, 0x96, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2A36)
    Sleep(1100)
    BlurSwitch(0x12C, 0xBBFFFFFF, 0x0, 0x1, 0x5)
    WaitChrThread(0xFE, 2)
    OP_0D()
    Sound(833, 0, 100, 0)
    StopEffect(0x0, 0x2)
    PlayEffect(0x7, 0xFF, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 1250, 1250, 1250, 0xFF, 0, 0, 0, 0)
    OP_82(0x96, 0x12C, 0x1388, 0x320)
    OP_71(0x0, 0xF0, 0xF8, 0x0, 0x0)
    Sleep(300)
    CancelBlur(900)
    OP_79(0x0)
    Sleep(900)
    OP_68(9820, 2750, -1820, 600)
    MoveCamera(67, -3, 0, 600)
    OP_6E(810, 600)
    SetCameraDistance(10570, 600)
    OP_74(0x0, 0xF)
    Sound(251, 0, 100, 0)
    PlayEffect(0x7, 0xFF, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 750, 750, 750, 0xFF, 0, 0, 0, 0)
    OP_82(0x0, 0xC8, 0xBB8, 0x1F4)
    OP_71(0x0, 0xF9, 0x104, 0x0, 0x0)

    def lambda_2B5E():
        OP_9C(0xFE, 0x32, 0x0, 0x0, 0x546, 0x1194)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2B5E)
    WaitChrThread(0xFE, 2)
    Sound(893, 0, 50, 0)
    OP_68(8900, 2000, -1790, 700)
    MoveCamera(61, -2, 0, 700)
    OP_6E(810, 700)
    SetCameraDistance(10360, 700)
    OP_79(0x0)
    OP_71(0x0, 0x105, 0x118, 0x0, 0x0)
    Sleep(200)
    Sound(833, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0x1F4)
    OP_79(0x0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0xA, 0x2B, 0x0, 0x20)
    OP_6F(0x79)
    Return()

    # Function_9_28E6 end

    def Function_10_2BED(): pass

    label("Function_10_2BED")

    Fade(100)
    OP_74(0x0, 0xF)
    OP_71(0x0, 0x40, 0x4C, 0x0, 0x0)
    OP_79(0x0)
    OP_0D()
    BlurSwitch(0x12C, 0xBBFFFFFF, 0x0, 0x1, 0x5)
    SetCameraDistance(11950, 500)
    Sound(913, 0, 100, 0)
    OP_71(0x0, 0x4D, 0x55, 0x0, 0x20)
    Sleep(300)
    OP_82(0xC8, 0xC8, 0xBB8, 0x5DC)
    Sleep(1800)
    ClearMapObjFlags(0x0, 0x20)
    OP_79(0x0)
    OP_6F(0x79)
    CancelBlur(0)
    OP_71(0x0, 0x56, 0x63, 0x0, 0x0)
    OP_79(0x0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0xA, 0x2B, 0x0, 0x20)
    Return()

    # Function_10_2BED end

    def Function_11_2C74(): pass

    label("Function_11_2C74")

    OP_74(0x0, 0xF)
    OP_71(0x0, 0xD4, 0xE4, 0x0, 0x0)
    Sleep(300)
    BlurSwitch(0x12C, 0xBBFFFFFF, 0x0, 0x1, 0x5)
    Sleep(400)
    CancelBlur(300)
    OP_79(0x0)
    SetChrFlags(0xFE, 0x4)
    OP_71(0x0, 0xE5, 0xED, 0x0, 0x20)
    PlayEffect(0x7, 0xFF, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 750, 750, 750, 0xFF, 0, 0, 0, 0)
    OP_82(0x32, 0x64, 0xBB8, 0x1F4)
    Sound(251, 0, 100, 0)
    Sound(833, 0, 100, 0)
    OP_68(-2700, 2550, -4100, 700)
    BlurSwitch(0x12C, 0xBBFFFFFF, 0x0, 0x1, 0x5)
    OP_9C(0xFE, 0xFFFFE890, 0x1F4, 0x0, 0x226, 0x640)
    CancelBlur(0)
    Return()

    # Function_11_2C74 end

    def Function_12_2D3D(): pass

    label("Function_12_2D3D")

    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_12_2D3D end

    def Function_13_2D46(): pass

    label("Function_13_2D46")

    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_13_2D46 end

    def Function_14_2D4F(): pass

    label("Function_14_2D4F")

    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_14_2D4F end

    def Function_15_2D58(): pass

    label("Function_15_2D58")

    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_15_2D58 end

    def Function_16_2D61(): pass

    label("Function_16_2D61")

    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_16_2D61 end

    def Function_17_2D6A(): pass

    label("Function_17_2D6A")

    SetChrChipByIndex(0xFE, 0x26)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_17_2D6A end

    def Function_18_2D73(): pass

    label("Function_18_2D73")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch13400.itc", 0x1E)
    LoadChrToIndex("chr/ch03600.itc", 0x1F)
    LoadChrToIndex("chr/ch03500.itc", 0x20)
    LoadChrToIndex("chr/ch00500.itc", 0x21)
    LoadChrToIndex("chr/ch13700.itc", 0x22)
    LoadChrToIndex("chr/ch27200.itc", 0x23)
    LoadChrToIndex("chr/ch27300.itc", 0x24)
    LoadChrToIndex("chr/ch02400.itc", 0x25)
    LoadChrToIndex("chr/ch43150.itc", 0x26)
    LoadChrToIndex("chr/ch43250.itc", 0x27)
    LoadChrToIndex("chr/ch43350.itc", 0x28)
    LoadChrToIndex("apl/ch50011.itc", 0x29)
    LoadChrToIndex("chr/ch00050.itc", 0x2A)
    LoadChrToIndex("chr/ch00150.itc", 0x2B)
    LoadChrToIndex("chr/ch00250.itc", 0x2C)
    LoadChrToIndex("chr/ch00350.itc", 0x2D)
    LoadChrToIndex("chr/ch00550.itc", 0x2E)
    LoadChrToIndex("chr/ch03550.itc", 0x30)
    LoadChrToIndex("chr/ch03552.itc", 0x31)
    LoadChrToIndex("apl/ch51408.itc", 0x32)
    LoadChrToIndex("chr/ch00053.itc", 0x33)
    LoadChrToIndex("chr/ch00153.itc", 0x34)
    LoadChrToIndex("chr/ch00253.itc", 0x35)
    LoadChrToIndex("chr/ch00353.itc", 0x36)
    LoadChrToIndex("chr/ch00056.itc", 0x39)
    LoadChrToIndex("chr/ch00156.itc", 0x3A)
    LoadChrToIndex("chr/ch00256.itc", 0x3B)
    LoadChrToIndex("chr/ch00356.itc", 0x3C)
    LoadChrToIndex("chr/ch00556.itc", 0x3D)
    LoadChrToIndex("chr/ch43100.itc", 0x3F)
    LoadChrToIndex("chr/ch43200.itc", 0x40)
    LoadChrToIndex("chr/ch43300.itc", 0x41)
    LoadChrToIndex("apl/ch51415.itc", 0x42)
    LoadChrToIndex("apl/ch51416.itc", 0x37)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis007.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu00701.itp")
    CreatePortrait(2, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu04900.itp")
    CreatePortrait(3, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu01400.itp")
    LoadEffect(0x1, "battle/bs000001.eff")
    LoadEffect(0x2, "eff/cutin35.eff")
    LoadEffect(0x3, "event/eva01_01.eff")
    LoadEffect(0x4, "event/ev14016.eff")
    LoadEffect(0x5, "event/ev10007.eff")
    LoadEffect(0x6, "event/ev10002.eff")
    LoadEffect(0x7, "battle/ms00001.eff")
    LoadEffect(0x8, "event/ev10006.eff")
    LoadEffect(0x9, "event/ev14015.eff")
    SoundLoad(3890)
    SoundLoad(3891)
    SoundLoad(3892)
    SoundLoad(4053)
    SoundLoad(4054)
    SoundLoad(4068)
    SoundLoad(3459)
    SoundLoad(3460)
    SoundLoad(2915)
    SoundLoad(3519)
    SoundLoad(3248)
    SoundLoad(3249)
    SoundLoad(4135)
    SoundLoad(959)
    SoundLoad(803)
    SoundLoad(825)
    RemoveParty(0x5, 0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_300F")
    LoadChrToIndex("chr/ch02950.itc", 0x2F)
    LoadChrToIndex("chr/ch02953.itc", 0x38)
    LoadChrToIndex("chr/ch0295F.itc", 0x3E)
    SetScenarioFlags(0x0, 0)
    AddParty(0x4, 0xFF, 0xFF)
    Jump("loc_3028")

    label("loc_300F")

    LoadChrToIndex("chr/ch03050.itc", 0x2F)
    LoadChrToIndex("chr/ch03053.itc", 0x38)
    LoadChrToIndex("chr/ch0305F.itc", 0x3E)
    ClearScenarioFlags(0x0, 0)
    AddParty(0x8, 0xFF, 0xFF)

    label("loc_3028")

    OP_68(-1820, 1450, 3350, 0)
    MoveCamera(153, 15, -1, 0)
    OP_6E(530, 0)
    SetCameraDistance(17390, 0)
    SetChrPos(0x101, -2190, -750, -670, 270)
    SetChrChipByIndex(0x101, 0x2A)
    SetChrSubChip(0x101, 0x0)
    SetChrPos(0x102, -210, -750, -3260, 270)
    SetChrChipByIndex(0x102, 0x2B)
    SetChrSubChip(0x102, 0x0)
    SetChrPos(0x103, -1200, -750, -2190, 270)
    SetChrChipByIndex(0x103, 0x2C)
    SetChrSubChip(0x103, 0x0)
    SetChrPos(0x104, -2960, -750, -2640, 270)
    SetChrChipByIndex(0x104, 0x2D)
    SetChrSubChip(0x104, 0x0)
    SetChrPos(0xF4, 960, -750, -1430, 270)
    SetChrChipByIndex(0xF4, 0x2F)
    SetChrSubChip(0xF4, 0x0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x5, 10000, 12000, -7000, 0)
    OP_A7(0x5, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrChipByIndex(0xB, 0x2E)
    SetChrPos(0xB, 200, -750, 0, 270)
    SetChrFlags(0xC, 0x8000)
    SetChrChipByIndex(0xC, 0x22)
    SetChrSubChip(0xC, 0x0)
    SetChrPos(0xC, 200, -750, -3000, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrPos(0x8, -2300, 250, 7600, 180)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrPos(0x9, -900, 250, 7400, 180)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrChipByIndex(0xA, 0x20)
    SetChrPos(0xA, 600, 250, 7600, 180)
    OP_52(0xA, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xF, 0x8000)
    SetChrChipByIndex(0xF, 0x25)
    SetChrPos(0xF, 900, -750, -23000, 0)
    SetChrFlags(0xD, 0x8000)
    SetChrChipByIndex(0xD, 0x23)
    SetChrPos(0xD, -900, -750, -25000, 0)
    SetChrFlags(0xE, 0x8000)
    SetChrChipByIndex(0xE, 0x24)
    SetChrPos(0xE, 900, -750, -25000, 0)
    SetChrFlags(0x10, 0x8000)
    SetChrChipByIndex(0x10, 0x26)
    SetChrPos(0x10, 0, -750, -13600, 0)
    SetChrFlags(0x11, 0x8000)
    SetChrChipByIndex(0x11, 0x27)
    SetChrPos(0x11, 3850, -750, -7000, 250)
    SetChrFlags(0x12, 0x8000)
    SetChrChipByIndex(0x12, 0x28)
    SetChrPos(0x12, -4180, -750, -8370, 117)
    SetMapObjFlags(0x0, 0x1000)
    ClearMapObjFlags(0x0, 0x4)
    OP_78(0x0, 0x13)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, -9950, -750, 880, 0)
    OP_93(0x13, 0x64, 0x0)
    OP_74(0x0, 0x1E)
    SetChrFlags(0x13, 0x1)
    OP_52(0x13, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1B58), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x15, 0x32)
    SetChrSubChip(0x15, 0x8)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, 600, 750, 5200, 180)
    SetChrFlags(0x15, 0x8000)
    SetChrFlags(0x15, 0x2)
    SetChrFlags(0x15, 0x20)
    SetChrFlags(0x15, 0x1000)
    SetChrFlags(0x15, 0x4)
    ClearChrFlags(0x15, 0x1)
    OP_A7(0x15, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetScenarioFlags(0x0, 1)
    OP_68(-5390, 2150, 1420, 0)
    MoveCamera(246, 16, -1, 0)
    OP_6E(530, 0)
    SetCameraDistance(14170, 0)
    SetCameraDistance(19170, 3000)
    FadeToBright(1000, 0)
    OP_82(0x0, 0x32, 0x5DC, 0x1388)
    BeginChrThread(0x13, 3, 0, 19)
    OP_0D()
    Sleep(500)
    Sound(843, 0, 100, 0)
    BlurSwitch(0x12C, 0xBBFFFFFF, 0x0, 0x1, 0x5)
    PlayEffect(0x1, 0x0, 0x13, 0x1, 500, -750, 500, 0, 0, 0, 1350, 1350, 1350, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    OP_6F(0x79)
    OP_75(0x0, 0x1, 0x5DC)

    def lambda_339B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_339B)
    Sleep(1000)
    StopEffect(0x0, 0x2)
    CancelBlur(2000)
    OP_6F(0x79)
    Sleep(500)
    OP_68(1240, 2150, 1060, 2000)
    MoveCamera(246, 16, -1, 2000)
    OP_6E(530, 2000)
    SetCameraDistance(15170, 2000)
    OP_6F(0x79)
    Sleep(300)

    ChrTalk(
        0x101,
        "#00006F#6PKh... *pant pant*...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108F#6PW-We beat it, somehow...\x02",
    )

    CloseMessageWindow()
    Sound(971, 0, 100, 0)
    Sleep(1000)
    Sound(4124, 255, 100, 0)
    Sleep(500)

    ChrTalk(
        0x9,
        "#04809F#5PUhuhu, you're quite good㈱\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(1140, 2150, 4290, 2000)
    MoveCamera(313, 15, -1, 2000)
    OP_6E(630, 2000)
    SetCameraDistance(9710, 2000)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)

    def lambda_34B0():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_34B0)
    Sleep(50)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)

    def lambda_34C8():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_34C8)
    Sleep(50)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)

    def lambda_34E0():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_34E0)
    Sleep(50)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)

    def lambda_34F8():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_34F8)
    Sleep(50)
    SetChrChipByIndex(0xF4, 0xFF)
    SetChrSubChip(0xF4, 0x0)

    def lambda_3510():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_3510)
    Sleep(50)
    SetChrChipByIndex(0xB, 0x21)
    SetChrSubChip(0xB, 0x0)

    def lambda_3528():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_3528)
    Sleep(50)
    OP_6F(0x79)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x104, 2)
    WaitChrThread(0xF4, 2)
    WaitChrThread(0xB, 2)

    ChrTalk(
        0x8,
        (
            "#04704F#5PHm, I suppose they're quite\x01",
            "good for some amateurs.\x02\x03",
            "#04700FAlso, it seems that the degree of\x01",
            "perfection of that "orbal staff" the\x01",
            "Foundation folks made, is not bad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00201F#6P#N............\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        "#00311F#6P#NDamn you...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-6700, 2150, -2690, 0)
    MoveCamera(47, 8, -1, 0)
    OP_6E(630, 0)
    SetCameraDistance(9290, 0)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    Sleep(300)
    OP_9B(0x1, 0x101, 0x0, 0x190, 0x3E8, 0x0)
    Fade(250)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0x101, 0x2A)
    SetChrSubChip(0x101, 0x0)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#00003F#12P"Ouroboros"──\x01",
            "Answer us already!\x02\x03",
            "#00013FWhat're you trying to do\x01",
            "in the land of Crossbell!?\x02\x03",
            "#00007FI dare not hope I'm right on this, but...\x01",
            "Don't tell me that you're the ones who\x01",
            "manufactured "Gnosis" again!?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#00105F#11PEh!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00208F#11PAh...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_386E")

    ChrTalk(
        0x109,
        "#10110F#11PN-No way...\x02",
    )

    CloseMessageWindow()

    label("loc_386E")


    ChrTalk(
        0x9,
        (
            "#04809F#5PHa ha, it's about the delinquents'\x01",
            "leader who demonized, eh?\x02\x03",
            "I was watching that too and\x01",
            "it was quite the show.\x02\x03",
            "#04802FUhuhu, if he had gone through with it a bit\x01",
            "more, I could've invited him in the "Society".\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3978")

    ChrTalk(
        0x105,
        "#10301F#11P............\x02",
    )

    CloseMessageWindow()

    label("loc_3978")


    ChrTalk(
        0x101,
        (
            "#00007F#12PDon't dodge the question!\x01",
            "Answer me!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04709F#1PHa ha, I can't blame you for\x01",
            "thinking that about us, but...\x02\x03",
            "#04702FWe only came to ascertain the\x01",
            "level of progress of the "plan".\x02\x03",
            "The degree of stimulation of the Septium vein...\x01",
            "For the "promised day" timing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00205F#12P#NThe "promised day"...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#00301F#12P#NTch, how much\x01",
            "vague can you be?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#00700F#12P............\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    SetCameraDistance(8000, 1500)

    def lambda_3B22():
        OP_9B(0x1, 0xFE, 0x0, 0x190, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_3B22)
    WaitChrThread(0xB, 1)
    Sleep(300)
    Sound(540, 0, 70, 0)
    SetChrChipByIndex(0xB, 0x2E)
    SetChrSubChip(0xB, 0x0)
    OP_6F(0x79)
    Sleep(300)

    ChrTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#00702F#12P──Enough with the talks already.\x02\x03",
            "From now on, we'll loosen their\x01",
            "mouths with the use of force.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xBB8)

    ChrTalk(
        0x101,
        "#00008F#6PYin...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_3C28")

    ChrTalk(
        0x109,
        (
            "#10107F#12P...It appears it's the\x01",
            "only thing we can do.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C66")

    label("loc_3C28")


    ChrTalk(
        0x105,
        (
            "#10303F#12P...It appears it's the\x01",
            "only path we can take.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C66")

    Sound(531, 0, 100, 0)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0xF4, 0x2F)
    SetChrSubChip(0xF4, 0x0)
    Sleep(50)
    SetChrChipByIndex(0x104, 0x2D)
    SetChrSubChip(0x104, 0x0)
    Sleep(50)
    SetChrChipByIndex(0x102, 0x2B)
    SetChrSubChip(0x102, 0x0)
    Sleep(50)
    SetChrChipByIndex(0x103, 0x2C)
    SetChrSubChip(0x103, 0x0)
    Sleep(500)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7584", 0)
    Fade(500)
    OP_68(-970, 1050, 4590, 0)
    MoveCamera(150, 17, -1, 0)
    OP_6E(530, 0)
    SetCameraDistance(18630, 0)
    SetCameraDistance(18130, 1000)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x8,
        "#04704F#6POh boy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#04804F#6PUh uh, even for me taking on all\x01",
            "of you would really be unreasonable.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x9, 0x5A, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x9,
        (
            "#04802F#12PCan we leave\x01",
            "this to you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#04900F#5PIt can not be helped.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3DB4():
        OP_9B(0x1, 0xFE, 0x0, 0x4B0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_3DB4)
    Sleep(50)
    OP_93(0x9, 0xB4, 0x1F4)
    OP_9B(0x1, 0x9, 0x0, 0xFFFFFCE0, 0x3E8, 0x0)
    Sleep(300)
    Fade(500)
    OP_68(130, 1950, 4130, 0)
    MoveCamera(11, 10, -1, 0)
    OP_6E(530, 0)
    SetCameraDistance(15000, 0)
    SetCameraDistance(14000, 1000)
    OP_6F(0x79)
    BeginChrThread(0xA, 0, 0, 22)
    Sleep(300)
    SetCameraDistance(13000, 500)
    BlurSwitch(0xA, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    Sleep(400)
    CancelBlur(0)
    WaitChrThread(0xA, 0)
    OP_6F(0x79)
    OP_68(-740, 2050, -670, 1200)
    SetCameraDistance(16550, 1200)
    OP_6F(0x79)
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
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00011F#6P#NA-A spear...?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        (
            "#00105F#12P#NIt looks like a "lance" that was used\x01",
            "by the knights in the Middle Ages...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#00306F#6P#NHey now...\x01",
            "What's the meaning of bringin'\x01",
            "out such an oddity?\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)
    OP_C9(0x0, 0x80000000)

    AnonymousTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#3890V#5P#30W──Do not waste your breath.\x02\x03",
            "#3891VYou can all come at me at\x01",
            "full force using the weapons\x01",
            "you are specialized in.\x02\x03",
            "#3892VIf you do not, you will\x01",
            "lose your lives.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xF34)
    OP_C9(0x1, 0x80000000)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)

    ChrTalk(
        0x101,
        "#00005F#6P#N......!?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#00707F#12P#NIncoming──!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    Sleep(800)
    BeginChrThread(0xA, 3, 0, 24)
    Sleep(700)
    EndChrThread(0xA, 0x3)
    BeginChrThread(0xA, 3, 0, 25)
    BeginChrThread(0x14, 1, 0, 39)
    Fade(500)
    OP_68(-4770, 1950, -2610, 0)
    OP_68(-5000, 1850, -2610, 3000)
    MoveCamera(51, 8, -1, 0)
    OP_6E(530, 0)
    SetCameraDistance(9500, 0)
    SetCameraDistance(11000, 3000)
    Fade(500)
    CancelBlur(0)
    OP_0D()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_82(0x0, 0x32, 0x5DC, 0x7D0)
    SetCameraDistance(12000, 3000)
    BeginChrThread(0xB, 3, 0, 32)
    BeginChrThread(0xB, 2, 0, 33)
    Sound(815, 0, 100, 0)
    BeginChrThread(0x101, 3, 0, 27)
    BeginChrThread(0x101, 2, 0, 34)
    BeginChrThread(0x102, 3, 0, 28)
    BeginChrThread(0x103, 3, 0, 29)
    BeginChrThread(0x104, 3, 0, 30)
    BeginChrThread(0xF4, 3, 0, 31)

    ChrTalk(
        0x102,
        "#00105F#11P#7AEeek──\x02",
    )

    Sleep(800)

    ChrTalk(
        0x101,
        "#00010F#4P#N#7A...Wha...\x02",
    )

    CloseMessageWindow()
    OP_6F(0x79)
    WaitChrThread(0xA, 3)
    Sleep(300)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_68(-3210, 1650, -4260, 1000)
    MoveCamera(36, 5, -1, 1000)
    OP_6E(530, 1000)
    SetCameraDistance(17220, 1000)
    OP_82(0x1F4, 0x0, 0xBB8, 0x3E8)
    Sound(369, 0, 100, 0)
    Sound(196, 0, 80, 0)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(2031, 255, 100, 0)
    Sound(2129, 255, 70, 1)
    Sound(2223, 255, 100, 2)
    Sound(2318, 255, 100, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_4337")
    Sound(2464, 255, 100, 4)
    Jump("loc_433D")

    label("loc_4337")

    Sound(2404, 255, 100, 4)

    label("loc_433D")

    WaitChrThread(0xB, 2)
    WaitChrThread(0xB, 3)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    WaitChrThread(0xF4, 3)
    CancelBlur(0)
    Sleep(500)
    BeginChrThread(0xA, 3, 0, 26)
    WaitChrThread(0xA, 3)

    ChrTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#04900F#5P....................................\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_4438")

    ChrTalk(
        0x109,
        "#10108F#12P#30W#NN-No way...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#00310F#12P#30W#NS-She released several super-high\x01",
            "speed thrusts in an instant...?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_44BF")

    label("loc_4438")


    ChrTalk(
        0x104,
        "#00310F#12P#30W#NGh...no way...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x105,
        (
            "#10310F#12P#30W#N...Did she released several super-\x01",
            "high speed thrusts in a moment...?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_44BF")


    ChrTalk(
        0x103,
        (
            "#00206F#12P#30W#N...Unbelievable...\x01",
            "That is not something a human could do...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#00710F#11P#30W......Kh......\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04702F#5PHoo, to think there's someone who can\x01",
            "resist against the "Steel Maiden"'s lance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#04809F#5PUhuhu, it looks like you aren't called\x01",
            "the Eastern District demon for nothing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#04900F#5PVery good reflexes.\x02\x03",
            "However, compared to your "family predecessor",\x01",
            "it appears you still have some hesitations.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(150)
    Sound(2617, 255, 100, 0)

    ChrTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#00705F#11P#30W#10A......What......\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(972, 0, 100, 0)
    Sleep(800)
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Fade(500)
    OP_68(-90, 550, -3200, 0)
    MoveCamera(168, 27, -1, 0)
    MoveCamera(168, 23, -1, 0)
    OP_6E(530, 0)
    SetCameraDistance(16000, 0)
    SetCameraDistance(15000, 1000)
    ClearChrFlags(0x101, 0x20)
    SetChrChipByIndex(0x101, 0x39)
    SetChrSubChip(0x101, 0x0)
    OP_93(0x101, 0x2D, 0x0)
    ClearChrFlags(0x102, 0x20)
    SetChrChipByIndex(0x102, 0x3A)
    SetChrSubChip(0x102, 0x0)
    ClearChrFlags(0x104, 0x20)
    SetChrChipByIndex(0x104, 0x3C)
    SetChrSubChip(0x104, 0x0)
    OP_93(0x104, 0x2D, 0x0)
    ClearChrFlags(0x103, 0x20)
    SetChrChipByIndex(0x103, 0x3B)
    SetChrSubChip(0x103, 0x0)
    ClearChrFlags(0xF4, 0x20)
    SetChrChipByIndex(0xF4, 0x3E)
    SetChrSubChip(0xF4, 0x0)
    Sleep(300)
    OP_6F(0x79)
    OP_FD(0xC, 0xB)
    BeginChrThread(0xB, 0, 0, 40)
    WaitChrThread(0xB, 0)
    SetChrChipByIndex(0xC, 0x42)
    SetChrSubChip(0xC, 0x1)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xB, 0x80)
    OP_0D()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF4, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0xC,
        "#30W────────────\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x101,
        "#00011F#12P......!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105F#5PHuh...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00307F#11PWhaaat...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00205F#11PMiss...Rixia...?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_495B")

    ChrTalk(
        0x109,
        "#10111F#5PE-Eeeh...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_4999")

    label("loc_495B")


    ChrTalk(
        0x105,
        (
            "#10301F#5PAmazing...\x01",
            "Were you altering your presence...?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4999")

    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x9,
        (
            "#04809F#5PAhaha, this is hilarious!\x02\x03",
            "To think that "Yin"'s true identity\x01",
            "is Rixia Mao, the Arc-en-ciel\x01",
            "quasi-heroine!!\x02\x03",
            "#04802FUhuhu, doesn't it look like\x01",
            "quite the amusing drama?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#00711F#5P......Kh...... \x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    OP_A7(0x5, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrPos(0x5, -900, -750, -23000, 0)
    Sleep(300)
    OP_C9(0x0, 0x80000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_4B35")

    NpcTalk(
        0x105,
        "Young Man's Voice",
        (
            "#2915V#6P#25A──Dear me. it seems we arrived\x01",
            "during an amazing scene.\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    Jump("loc_4B71")

    label("loc_4B35")


    NpcTalk(
        0x109,
        "Girl's Voice",
        "#3519V#6P#20AEveryone, are you ok!?\x02",
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)

    label("loc_4B71")

    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF4, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetChrFlags(0xC, 0x2)
    SetChrSubChip(0xC, 0x5)
    OP_68(-2330, 1950, -1820, 1500)
    MoveCamera(158, 16, -1, 1500)
    OP_6E(530, 1500)
    SetCameraDistance(14070, 1500)
    Sleep(500)

    def lambda_4C49():
        OP_9B(0x0, 0xFE, 0x0, 0x1F40, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x5, 1, lambda_4C49)
    Sleep(100)

    def lambda_4C61():
        OP_9B(0x0, 0xFE, 0x0, 0x1F40, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_4C61)
    Sleep(50)

    def lambda_4C79():
        OP_9B(0x0, 0xFE, 0x0, 0x1F40, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_4C79)
    Sleep(50)

    def lambda_4C91():
        OP_9B(0x0, 0xFE, 0x0, 0x1F40, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_4C91)

    def lambda_4CA6():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_4CA6)
    Sleep(50)

    def lambda_4CB6():
        OP_93(0xFE, 0xB5, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_4CB6)
    Sleep(50)

    def lambda_4CC6():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_4CC6)
    Sleep(50)

    def lambda_4CD6():
        OP_93(0xFE, 0xB5, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_4CD6)
    Sleep(50)

    def lambda_4CE6():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4CE6)
    Sleep(150)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x104, 2)
    WaitChrThread(0xF4, 2)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x101, 2)
    WaitChrThread(0xC, 2)
    WaitChrThread(0x5, 1)
    WaitChrThread(0xF, 1)
    WaitChrThread(0xD, 1)
    WaitChrThread(0xE, 1)
    OP_6F(0x79)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_4D5B")

    ChrTalk(
        0x101,
        (
            "#00008F#6P#NWazy...\x01",
            "Mr. Arios and you all...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D8D")

    label("loc_4D5B")


    ChrTalk(
        0x101,
        (
            "#00008F#6P#NNoｱl...\x01",
            "Mr. Arios and you all...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D8D")

    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        "#00106F#6PYou are here...\x02",
    )

    CloseMessageWindow()
    Sleep(50)

    def lambda_4DB7():
        OP_9B(0x0, 0xFE, 0x163, 0x1A90, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x5, 1, lambda_4DB7)
    Sleep(100)

    def lambda_4DCF():
        OP_9B(0x0, 0xFE, 0x0, 0x1964, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_4DCF)
    Sleep(150)

    def lambda_4DE7():
        OP_9B(0x0, 0xFE, 0x0, 0x1964, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_4DE7)
    Sleep(50)

    def lambda_4DFF():
        OP_9B(0x0, 0xFE, 0x0, 0x1964, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_4DFF)
    Sleep(400)
    Fade(500)
    SetChrChipByIndex(0xC, 0x42)
    SetChrFlags(0xC, 0x1000)
    ClearChrFlags(0xC, 0x2)
    SetChrSubChip(0xC, 0x1)
    OP_68(-3310, 1950, -11270, 0)
    MoveCamera(24, 9, -1, 0)
    OP_6E(530, 0)
    SetCameraDistance(13150, 0)
    WaitChrThread(0x5, 1)
    WaitChrThread(0xF, 1)
    WaitChrThread(0xD, 1)
    WaitChrThread(0xE, 1)
    OP_63(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xE,
        "#12PThose guys are...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#12P"Ouroboros" members, eh...!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x3, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x3, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x3, 0x3)
    OP_CC(0x0, 0x3, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)
    OP_C9(0x0, 0x80000000)

    AnonymousTalk(
        0xF,
        (
            "#4053V#11P#40WCampanella "The Fool"...\x02\x03",
            "#4054VAnd also the "Thirteen Workshops"\x01",
            "manager and the "Steel Maiden"...\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xFD6)
    OP_57(0x0)
    OP_5A()
    OP_C9(0x1, 0x80000000)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x3, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x3, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x3, 0x3)
    OP_CC(0x0, 0x3, 0x0)

    ChrTalk(
        0x8,
        (
            "#04705F#5P#NOh oooh...\x01",
            "Is that one the "Divine Blade of Wind", perhaps?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x9,
        (
            "#04802F#5P#NUhuhu, they say that his\x01",
            "ability rivals Loewe's...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#04900F#5P#N──"Divine Blade of Wind".\x01",
            "It is the first time we meet, correct?\x02\x03",
            "Indeed, it looks like you are \x01",
            "wonderfully skilled as rumored.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xF,
        (
            "#01403F#11P...Enough with the flattery.\x02\x03",
            "I can't accept it until I surpass\x01",
            "the "human limits" like you.\x02\x03",
            "#01401FEspecially in front of "that lance",\x01",
            "even an army would have to retreat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#04900F#5P#NUh uh, you are really something even\x01",
            "just for having seen through that.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xD,
        "#6PMr. Arios...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#12PThere's no way that...\x01",
            "We're letting them go!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#01403F#11PNonsense... However, the\x01",
            "situation doesn't fare well for us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#12P!?\x02",
    )

    CloseMessageWindow()
    OP_68(30, 150, -9540, 1500)
    MoveCamera(24, 25, -1, 1500)
    OP_6E(530, 1500)
    SetCameraDistance(21930, 1500)
    OP_6F(0x79)
    Fade(500)
    OP_68(30, 150, -9540, 0)
    MoveCamera(345, 34, -1, 0)
    OP_6E(530, 0)
    SetCameraDistance(21930, 0)
    OP_68(970, 150, -9750, 3000)
    MoveCamera(64, 29, -1, 3000)
    OP_6E(530, 3000)
    SetCameraDistance(21930, 3000)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    OP_A7(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x12, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Sound(977, 0, 100, 0)
    BeginChrThread(0x14, 1, 0, 42)
    PlayEffect(0x5, 0xFF, 0x10, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_5412():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x2EE)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_5412)
    Sleep(400)
    PlayEffect(0x5, 0xFF, 0x11, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_545D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x2EE)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_545D)
    Sleep(400)
    PlayEffect(0x5, 0xFF, 0x12, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_54A8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x2EE)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_54A8)
    Sleep(800)
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
    Sleep(50)
    OP_63(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_5588():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x5, 1, lambda_5588)
    Sleep(150)

    def lambda_5598():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_5598)
    Sleep(150)

    def lambda_55A8():
        OP_93(0xFE, 0xB5, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_55A8)
    Sleep(250)

    ChrTalk(
        0x10,
        "#11P............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#5PKh...  \x01",
            "The ones Ling and Eolia fought against?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_5657")

    ChrTalk(
        0x105,
        (
            "#10301F#11PIt looks like these ladies\x01",
            "aren't common persons too...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5691")

    label("loc_5657")


    ChrTalk(
        0x109,
        (
            "#10108F#11PKh...\x01",
            "(They have no openings at all...!?)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5691")

    OP_68(240, 1000, -7460, 1500)
    MoveCamera(25, 10, -1, 1500)
    OP_6E(530, 1500)
    SetCameraDistance(20910, 1500)
    OP_6F(0x79)

    ChrTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#04900F#5P#N──Enough. There is no\x01",
            "need to taunt them here.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x11,
        "#11PSir.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "#5PUh uh, understood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#11PLike Master wishes.\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(250)
    Sound(805, 0, 70, 0)
    Sound(540, 0, 50, 0)
    Sound(531, 0, 70, 0)
    SetChrChipByIndex(0x10, 0x3F)
    SetChrChipByIndex(0x11, 0x40)
    SetChrChipByIndex(0x12, 0x41)
    OP_0D()
    Sleep(300)

    def lambda_577D():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFD12, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_577D)
    Sleep(100)

    def lambda_5795():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFD12, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_5795)
    Sleep(100)

    def lambda_57AD():
        OP_9B(0x1, 0xFE, 0x13B, 0xFFFFFD44, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_57AD)
    Sleep(500)

    ChrTalk(
        0x101,
        "#00010F#1PKh......\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#00712F#11P............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#04804F#5P#NUhuhu, it looks like a favorable opportunity.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(440, 1150, 7910, 0)
    MoveCamera(30, 11, -1, 0)
    OP_6E(530, 0)
    SetCameraDistance(19660, 0)
    SetCameraDistance(18660, 1000)
    OP_6F(0x79)

    def lambda_587A():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_587A)

    def lambda_5887():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5887)

    def lambda_5894():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_5894)

    def lambda_58A1():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_58A1)

    def lambda_58AE():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_58AE)

    def lambda_58BB():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_58BB)

    def lambda_58C8():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x5, 2, lambda_58C8)

    def lambda_58D5():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_58D5)

    def lambda_58E2():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_58E2)

    ChrTalk(
        0x8,
        (
            "#04704F#5PI was able to confirm the level of advancement\x01",
            "of the "plan" and the Septium vein state.\x02\x03",
            "#04702FHu hu, it is time for me too to go\x01",
            "back to the "finishing touches."\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    BeginChrThread(0x9, 0, 0, 41)
    WaitChrThread(0x9, 0)
    Sound(959, 2, 100, 0)
    PlayEffect(0x6, 0x0, 0x9, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x6, 0x1, 0x8, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x6, 0x2, 0xA, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    Sleep(500)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)
    Sleep(100)
    OP_93(0x101, 0x0, 0x1F4)

    ChrTalk(
        0x101,
        "#00007F#12P#NW-Wait...!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xF,
        (
            "#01407F#12P#N...As you can Imagine, we\x01",
            "can't let you go away like that...!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#04900F#5PI will give you one warning.\x02\x03",
            "In regards to this "plan", we have\x01",
            "nothing more than a mere support role.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#12P#NHuh... \x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xF,
        "#01405FWhat#12P#N......?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#04900F#5PThe beasts will be immediately released\x01",
            "and chaos will be brought to this land.\x02\x03",
            "Be that as it may, know it so to not be too\x01",
            "much swayed by the tragedies that will occur\x01",
            "in front of your eyes.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#04802F#5PUhuhu...\x01",
            "Then, have a good day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04709F#5PHa ha, I'll look forward\x01",
            "to our next encounter.\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x101, 1, 0, 35)
    BeginChrThread(0x102, 1, 0, 35)
    BeginChrThread(0x103, 1, 0, 35)
    BeginChrThread(0x104, 1, 0, 35)
    BeginChrThread(0xF4, 1, 0, 35)
    ClearChrFlags(0xC, 0x1000)
    ClearChrFlags(0xC, 0x20)
    SetChrChipByIndex(0xC, 0x22)
    SetChrSubChip(0xC, 0x0)
    Sound(4135, 255, 100, 0)
    OP_68(-160, 750, 1070, 8000)
    MoveCamera(31, 15, -1, 8000)
    OP_6E(530, 8000)
    SetCameraDistance(25510, 8000)
    StopEffect(0x0, 0x2)

    def lambda_5D4E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_5D4E)
    Sound(1035, 0, 100, 0)
    Sound(977, 0, 100, 0)
    Sleep(400)
    StopEffect(0x1, 0x2)

    def lambda_5D71():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_5D71)
    Sound(1035, 0, 100, 0)
    Sleep(400)
    StopEffect(0x2, 0x2)

    def lambda_5D8E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_5D8E)
    Sound(1035, 0, 100, 0)
    Sleep(400)
    StopSound(959, 1000, 100)
    Sleep(600)

    def lambda_5DB1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_5DB1)
    Sleep(400)

    def lambda_5DC5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_5DC5)
    Sleep(400)

    def lambda_5DD9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_5DD9)
    Sleep(400)
    StopBGM(0x1F40)
    WaitChrThread(0x9, 2)
    WaitChrThread(0x8, 2)
    WaitChrThread(0xA, 2)
    WaitChrThread(0x10, 2)
    WaitChrThread(0x11, 2)
    WaitChrThread(0x12, 2)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    Sleep(1500)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xC, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xD, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xF, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0xC)
    OP_64(0x109)
    OP_64(0x105)
    OP_64(0xD)
    OP_64(0xE)
    OP_64(0xF)
    OP_6F(0x79)
    Fade(500)
    OP_68(-860, 750, -6060, 0)
    MoveCamera(137, 16, -1, 0)
    OP_6E(530, 0)
    SetCameraDistance(17680, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0xE,
        "#11PKh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11P"Ouroboros"...\x01",
            "What a hell of a bunch.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#00713F#11P#40W............\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0xC, 3, 0, 36)
    Sleep(500)
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
    BeginChrThread(0x101, 3, 0, 38)
    BeginChrThread(0x102, 3, 0, 38)
    Sleep(50)
    BeginChrThread(0x103, 3, 0, 38)
    BeginChrThread(0x104, 3, 0, 38)
    BeginChrThread(0x109, 3, 0, 38)
    BeginChrThread(0x105, 3, 0, 38)
    Sleep(50)
    BeginChrThread(0xF, 3, 0, 38)
    Sleep(50)
    BeginChrThread(0xD, 3, 0, 38)
    BeginChrThread(0xE, 3, 0, 38)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x104, 2)
    WaitChrThread(0x109, 2)
    WaitChrThread(0x105, 2)
    WaitChrThread(0xF, 2)
    WaitChrThread(0xD, 2)
    WaitChrThread(0xE, 2)
    Sleep(100)

    ChrTalk(
        0x101,
        "#00011F#12PRixia...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108F#11PMiss Rixia...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0xC,
        (
            "#00714F#3248V#5P#30W...It's time for me to\x01",
            "go back to practice.\x02\x03",
            "#00713F#3249V......Excuse me......\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xCB1)
    OP_57(0x0)
    OP_5A()
    OP_C9(0x1, 0x80000000)
    BeginChrThread(0xC, 3, 0, 37)
    Sleep(500)
    OP_68(2660, 750, -9640, 2000)
    MoveCamera(140, 15, -1, 2000)
    OP_6E(530, 2000)
    SetCameraDistance(23490, 2000)
    WaitChrThread(0xC, 3)
    SetChrFlags(0xC, 0x80)
    OP_6F(0x79)
    EndChrThread(0x101, 0x3)
    EndChrThread(0x102, 0x3)
    EndChrThread(0x103, 0x3)
    EndChrThread(0x104, 0x3)
    EndChrThread(0x109, 0x3)
    EndChrThread(0x105, 0x3)
    EndChrThread(0xF, 0x3)
    EndChrThread(0xD, 0x3)
    EndChrThread(0xE, 0x3)
    Sleep(1000)
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
    OP_68(-960, 750, -5650, 1500)
    MoveCamera(140, 17, -1, 1500)
    OP_6E(530, 1500)
    SetCameraDistance(18220, 1500)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#00008F#6P............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#6PUnbelievable things have been happening\x01",
            "one after the other that it doesn't\x01",
            "feel this is reality anymore...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00306F#12P......Yeah......\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00208F#6PI just feel like\x01",
            "I am dreaming...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10106F#6PI-It could be really so...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10308F#12PIn the case of Wald, though...\x01",
            "I think that's a kind of nightmare.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0xF,
        "#01403F#4068V#5P#40WHowever── This is, unmistakably, reality.\x02",
    )

    CloseMessageWindow()
    OP_24(0xFE4)
    OP_C9(0x1, 0x80000000)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_649E():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_649E)
    Sleep(50)

    def lambda_64AE():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_64AE)

    def lambda_64BB():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_64BB)
    Sleep(50)

    def lambda_64CB():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_64CB)

    def lambda_64D8():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_64D8)

    def lambda_64E5():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_64E5)
    Sleep(50)

    def lambda_64F5():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_64F5)

    def lambda_6502():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6502)
    Sleep(300)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7561", 0)

    ChrTalk(
        0x101,
        "#00001F#6PMr. Arios... \x02",
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0x101, 500)

    ChrTalk(
        0xF,
        (
            "#01401F#5PThe "Society" guys left us with\x01",
            "more clues than expected.\x02\x03",
            "The meaning of this place and also\x01",
            ""beasts that will be immediately released"...\x02\x03",
            "#01403FIt seems we have no time to stay dumbfounded.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00013F#6PY-Yes.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00311F#12P("Beasts"...don't tell me that...)\x02",
    )

    CloseMessageWindow()
    Sound(803, 2, 100, 0)
    Sleep(300)
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

    def lambda_66FA():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_66FA)

    def lambda_6707():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6707)
    Sleep(50)

    def lambda_6717():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6717)

    def lambda_6724():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6724)
    Sleep(50)

    def lambda_6734():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_6734)

    def lambda_6741():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6741)
    Sleep(50)

    def lambda_6751():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_6751)

    def lambda_675E():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_675E)
    Sleep(700)
    Fade(250)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x29)
    SetChrSubChip(0x101, 0x4)
    Sound(802, 0, 100, 0)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#00011F#6PB-By the way.\x01",
            "Orbal waves reach here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00200F#11PYes, barely I think.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x5)
    OP_24(0x323)
    Sound(804, 0, 100, 0)
    Sleep(300)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CC(0x0, 0x0, 0x3)
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00007F──Yes! Special Support Section,\x01",
            "Bannings speaking.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Dudley's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#3459V#30W...It's Dudley.\x02\x03",
            "#3460VI heard you headed to the lake\x01",
            "south bank, are you there now?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xD84)
    OP_C9(0x1, 0x80000000)
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00005FAh, yes.\x02\x03",
            "#00001FUhhm...many things happened and\x01",
            "we're with Mr. Arios and the others.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Dudley's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Then it's perfect.\x01",
            "Tell them all too, since they're there.\x02\x03",
            "──All of the "Red Constellation"\x01",
            "members have disappeared from the city.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00005F#4SWhat...!?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Dudley's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "I'd like to talk with\x01",
            "Orlando, if possible.\x02\x03",
            "Can you come back immediately?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00010FU-Understood!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sound(813, 0, 60, 0)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    OP_CC(0x0, 0x0, 0x3)
    SetChrSubChip(0x101, 0x4)
    Sound(804, 0, 100, 0)
    Sleep(300)

    ChrTalk(
        0x102,
        "#00101F#5PD-Did something happen?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10113F#5PYou were quite flustered...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Sound(802, 0, 100, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x101,
        "#00003F#6PYeah...\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Briefly explained the intel from Dudley.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0xC8)

    ChrTalk(
        0x104,
        "#00310F#4S#11P!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00205F#11PWhat...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#11PThe "Red Constellation" has...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5PKh...\x01",
            "We were keeping tabs on them too.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xF)

    ChrTalk(
        0xF,
        (
            "#01403F#5P──Lloyd.\x01",
            "Return to the city at once.\x02\x03",
            "#01400FWe'll return after having\x01",
            "searched this place.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)

    def lambda_6DE4():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6DE4)
    Sleep(50)

    def lambda_6DF4():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6DF4)

    def lambda_6E01():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6E01)
    Sleep(50)

    def lambda_6E11():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6E11)

    def lambda_6E1E():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6E1E)

    def lambda_6E2B():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6E2B)
    Sleep(250)

    ChrTalk(
        0x101,
        (
            "#00011F#6PAh...\x02\x03",
            "#00003F...Thank you.\x01",
            "Doing that would help us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00306F#12P...Thanks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#11PWe're all the same in such situations.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5PAlso, even Ling and Eolia\x01",
            "can't move at once.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#01403F#5PIf the "Red Constellation" has moved, there\x01",
            "should also be movements in the "Heiyue"...\x02\x03",
            "#01401FWe'll return immediately too, \x01",
            "so be extremely careful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00007F#6PYes...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10107F#6PThen, excuse us!\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(20180, 2000)
    StopSound(122, 2000, 50)
    StopSound(123, 2000, 70)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_CC(0x1, 0xFF, 0x0)
    OP_C9(0x0, 0x10000)
    OP_24(0x323)
    SoundLoad(959)
    SoundLoad(825)
    SetScenarioFlags(0x22, 1)
    NewScene("e4500", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_18_2D73 end

    def Function_19_7020(): pass

    label("Function_19_7020")

    OP_71(0x0, 0x157, 0x16C, 0x0, 0x0)
    OP_79(0x0)
    Sound(913, 0, 100, 0)
    OP_71(0x0, 0x16D, 0x17E, 0x0, 0x20)
    Return()

    # Function_19_7020 end

    def Function_20_7042(): pass

    label("Function_20_7042")

    Sound(970, 0, 100, 0)
    Sound(920, 0, 100, 0)
    Sound(202, 0, 100, 0)
    PlayEffect(0x9, 0xFF, 0xFE, 0x1, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    SetChrChip(0x0, 0xFE, 0x32, 0x12C)
    Sound(893, 0, 70, 0)
    SetChrSubChip(0xFE, 0x8)
    Sleep(156)
    SetChrSubChip(0xFE, 0x9)
    Sleep(144)
    SetChrSubChip(0xFE, 0xA)
    Sleep(132)
    SetChrSubChip(0xFE, 0xB)
    Sleep(120)
    SetChrSubChip(0xFE, 0xC)
    Sleep(108)
    SetChrSubChip(0xFE, 0xD)
    Sleep(96)
    SetChrSubChip(0xFE, 0xE)
    Sleep(84)
    SetChrSubChip(0xFE, 0xF)
    Sleep(72)

    label("loc_70DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_712E")
    Sound(893, 0, 50, 0)
    SetChrSubChip(0xFE, 0x8)
    Sleep(60)
    SetChrSubChip(0xFE, 0x9)
    Sleep(60)
    SetChrSubChip(0xFE, 0xA)
    Sleep(60)
    SetChrSubChip(0xFE, 0xB)
    Sleep(60)
    SetChrSubChip(0xFE, 0xC)
    Sleep(60)
    SetChrSubChip(0xFE, 0xD)
    Sleep(60)
    SetChrSubChip(0xFE, 0xE)
    Sleep(60)
    SetChrSubChip(0xFE, 0xF)
    Sleep(60)
    Jump("loc_70DC")

    label("loc_712E")

    Sound(893, 0, 60, 0)
    SetChrSubChip(0xFE, 0x8)
    Sleep(72)
    SetChrSubChip(0xFE, 0x9)
    Sleep(84)
    SetChrSubChip(0xFE, 0xA)
    Sleep(96)
    SetChrSubChip(0xFE, 0xB)
    Sleep(108)
    SetChrSubChip(0xFE, 0xC)
    Sleep(120)
    SetChrSubChip(0xFE, 0xD)
    Sleep(132)
    SetChrSubChip(0xFE, 0xE)
    Sleep(144)
    SetChrSubChip(0xFE, 0xF)
    Sleep(156)
    Sound(531, 0, 80, 0)
    Sound(358, 0, 50, 0)
    Sound(308, 0, 100, 0)
    SetChrSubChip(0xFE, 0x8)
    Sleep(400)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_20_7042 end

    def Function_21_718E(): pass

    label("Function_21_718E")

    Sleep(2000)
    OP_9B(0x1, 0xFE, 0x0, 0xFFFFFD12, 0x1F4, 0x1)
    Return()

    # Function_21_718E end

    def Function_22_71A1(): pass

    label("Function_22_71A1")

    SetChrChipByIndex(0xFE, 0x32)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x2)
    SetChrSubChip(0xFE, 0x0)
    Sleep(300)
    Sound(531, 0, 80, 0)
    Sound(358, 0, 60, 0)
    SetChrSubChip(0xFE, 0x0)
    Sleep(100)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(300)
    SetChrSubChip(0xFE, 0x3)
    Sleep(100)
    Sound(308, 0, 100, 0)
    Sound(531, 0, 50, 0)
    SetChrSubChip(0xFE, 0x4)
    Sleep(500)
    BeginChrThread(0x15, 3, 0, 20)
    BeginChrThread(0x15, 2, 0, 21)
    Sleep(2500)
    ClearScenarioFlags(0x0, 1)
    WaitChrThread(0x15, 2)
    WaitChrThread(0x15, 3)
    Fade(500)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    CancelBlur(3000)
    OP_82(0x0, 0x64, 0x1388, 0x320)
    SetCameraDistance(11000, 250)

    def lambda_7240():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_7240)
    SetChrSubChip(0xFE, 0x4)
    Sleep(100)
    SetChrSubChip(0xFE, 0x5)
    Sleep(100)
    SetChrSubChip(0xFE, 0x6)
    Sleep(100)
    SetChrSubChip(0xFE, 0x7)
    Sleep(300)
    Sound(288, 0, 70, 0)
    Sound(308, 0, 100, 0)
    Sound(358, 0, 60, 0)
    SetChrChipByIndex(0xFE, 0x30)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x20)
    ClearChrFlags(0xFE, 0x2)
    Sleep(100)
    OP_6F(0x79)
    OP_0D()
    Sleep(1000)
    Return()

    # Function_22_71A1 end

    def Function_23_7296(): pass

    label("Function_23_7296")

    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x2)
    SetChrChipByIndex(0xFE, 0x32)
    SetChrSubChip(0xFE, 0x0)
    Sleep(100)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x5)
    Sleep(150)
    SetChrSubChip(0xFE, 0x6)
    Sleep(100)
    SetChrSubChip(0xFE, 0x7)
    Sleep(100)
    SetChrSubChip(0xFE, 0x8)
    Sleep(800)
    SetChrSubChip(0xFE, 0x5)
    Sleep(100)
    SetChrSubChip(0xFE, 0x4)
    Sleep(100)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x0)
    Sleep(100)
    SetChrChipByIndex(0xFE, 0x30)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x20)
    ClearChrFlags(0xFE, 0x2)
    Sleep(100)
    Return()

    # Function_23_7296 end

    def Function_24_7300(): pass

    label("Function_24_7300")

    SetChrChipByIndex(0xFE, 0x31)
    Sound(531, 0, 100, 0)
    Sound(358, 0, 70, 0)
    SetChrSubChip(0xFE, 0x0)
    Sleep(100)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    Return()

    # Function_24_7300 end

    def Function_25_731F(): pass

    label("Function_25_731F")

    SetChrChipByIndex(0xFE, 0x31)
    SetChrSubChip(0xFE, 0x1)
    Sleep(200)
    SetChrChip(0x0, 0xFE, 0x1E, 0x12C)

    def lambda_7337():
        OP_9D(0xFE, 0xFFFFFF06, 0xFFFFFD12, 0x726, 0x96, 0x1B58)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_7337)
    WaitChrThread(0xFE, 2)
    PlayEffect(0x4, 0x0, 0xFE, 0x4, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    SetChrSubChip(0xFE, 0x2)
    Sleep(50)
    SetChrSubChip(0xFE, 0x3)
    Sleep(50)
    SetChrSubChip(0xFE, 0x4)
    Sleep(50)
    SetChrSubChip(0xFE, 0x2)
    Sleep(50)
    SetChrSubChip(0xFE, 0x3)
    Sleep(50)
    SetChrSubChip(0xFE, 0x4)
    Sleep(50)
    SetChrSubChip(0xFE, 0x2)
    Sleep(50)
    SetChrSubChip(0xFE, 0x3)
    Sleep(50)
    SetChrSubChip(0xFE, 0x4)
    Sleep(50)
    SetChrSubChip(0xFE, 0x2)
    Sleep(50)
    SetChrSubChip(0xFE, 0x3)
    Sleep(50)
    SetChrSubChip(0xFE, 0x4)
    Sleep(50)
    SetChrSubChip(0xFE, 0x2)
    Sleep(50)
    SetChrSubChip(0xFE, 0x3)
    Sleep(50)
    SetChrSubChip(0xFE, 0x4)
    Sleep(50)
    SetChrSubChip(0xFE, 0x2)
    Sleep(50)
    SetChrSubChip(0xFE, 0x3)
    Sleep(50)
    SetChrSubChip(0xFE, 0x4)
    Sleep(50)
    SetChrSubChip(0xFE, 0x2)
    Sleep(50)
    SetChrSubChip(0xFE, 0x3)
    Sleep(50)
    SetChrSubChip(0xFE, 0x4)
    Sleep(50)
    SetChrSubChip(0xFE, 0x1)
    StopEffect(0x0, 0x2)
    Return()

    # Function_25_731F end

    def Function_26_7430(): pass

    label("Function_26_7430")

    SetChrSubChip(0xFE, 0x5)
    Sleep(200)
    SetChrChip(0x0, 0xFE, 0x1E, 0x12C)
    Sound(844, 0, 60, 0)
    Sound(250, 0, 80, 0)

    def lambda_7450():
        OP_9D(0xFE, 0x258, 0xFA, 0x1900, 0x60E, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_7450)
    WaitChrThread(0xFE, 2)
    Sound(326, 0, 50, 0)
    Sleep(300)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Sound(531, 0, 60, 0)
    Sound(358, 0, 60, 0)
    SetChrChipByIndex(0xA, 0x30)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x20)
    ClearChrFlags(0xA, 0x2)
    Return()

    # Function_26_7430 end

    def Function_27_749C(): pass

    label("Function_27_749C")

    SetChrChipByIndex(0xFE, 0x33)
    SetChrSubChip(0xFE, 0x0)

    label("loc_74A4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_74CB")
    OP_A6(0xFE, 0x1E, 0x1E, 0xFA, 0xBB8)
    Jump("loc_74A4")

    label("loc_74CB")

    PlayEffect(0x7, 0xFF, 0xFE, 0x0, 0, 800, 0, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x33)
    SetChrSubChip(0xFE, 0x0)
    Sound(251, 0, 100, 0)
    OP_9C(0xFE, 0x0, 0xFFFFFE70, 0xFFFFF34E, 0x2EE, 0x3AB6)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    SetChrSubChip(0xFE, 0x3)
    Sound(514, 0, 100, 0)
    Sleep(150)
    Return()

    # Function_27_749C end

    def Function_28_7548(): pass

    label("Function_28_7548")

    SetChrChipByIndex(0xFE, 0x34)
    SetChrSubChip(0xFE, 0x0)

    label("loc_7550")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7577")
    OP_A6(0xFE, 0x1E, 0x1E, 0xFA, 0xBB8)
    Jump("loc_7550")

    label("loc_7577")

    PlayEffect(0x7, 0xFF, 0xFE, 0x0, 0, 800, 0, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x34)
    SetChrSubChip(0xFE, 0x0)
    OP_9C(0xFE, 0xFA, 0x0, 0xFFFFF34E, 0x2EE, 0x5DC)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    SetChrSubChip(0xFE, 0x3)
    Sleep(150)
    Return()

    # Function_28_7548 end

    def Function_29_75E8(): pass

    label("Function_29_75E8")

    SetChrChipByIndex(0xFE, 0x35)
    SetChrSubChip(0xFE, 0x0)

    label("loc_75F0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7617")
    OP_A6(0xFE, 0x1E, 0x1E, 0xFA, 0xBB8)
    Jump("loc_75F0")

    label("loc_7617")

    PlayEffect(0x7, 0xFF, 0xFE, 0x0, 0, 800, 0, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x35)
    SetChrSubChip(0xFE, 0x0)
    OP_9C(0xFE, 0x0, 0x0, 0xFFFFEF66, 0x2EE, 0x5DC)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    SetChrSubChip(0xFE, 0x3)
    Sleep(150)
    Return()

    # Function_29_75E8 end

    def Function_30_7688(): pass

    label("Function_30_7688")

    SetChrChipByIndex(0xFE, 0x36)
    SetChrSubChip(0xFE, 0x0)

    label("loc_7690")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_76B7")
    OP_A6(0xFE, 0x1E, 0x1E, 0xFA, 0xBB8)
    Jump("loc_7690")

    label("loc_76B7")

    PlayEffect(0x7, 0xFF, 0xFE, 0x0, 0, 800, 0, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x36)
    SetChrSubChip(0xFE, 0x0)
    OP_9C(0xFE, 0xFFFFFF06, 0x0, 0xFFFFF15A, 0x2EE, 0x5DC)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    SetChrSubChip(0xFE, 0x3)
    Sound(514, 0, 100, 0)
    Sleep(150)
    Return()

    # Function_30_7688 end

    def Function_31_772E(): pass

    label("Function_31_772E")

    SetChrChipByIndex(0xFE, 0x38)
    SetChrSubChip(0xFE, 0x0)

    label("loc_7736")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_775D")
    OP_A6(0xFE, 0x1E, 0x1E, 0xFA, 0xBB8)
    Jump("loc_7736")

    label("loc_775D")

    PlayEffect(0x7, 0xFF, 0xFE, 0x0, 0, 800, 0, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x38)
    SetChrSubChip(0xFE, 0x0)
    OP_9C(0xFE, 0x190, 0x0, 0xFFFFF34E, 0x2EE, 0x5DC)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    SetChrSubChip(0xFE, 0x3)
    Sleep(150)
    Return()

    # Function_31_772E end

    def Function_32_77CE(): pass

    label("Function_32_77CE")

    SetChrChip(0x0, 0xFE, 0x32, 0x12C)
    Sound(844, 0, 100, 0)
    OP_9C(0xFE, 0xDAC, 0x0, 0xFFFFFE0C, 0x3E8, 0xBB8)
    Sound(844, 0, 100, 0)
    OP_9C(0xFE, 0xFFFFF060, 0x0, 0x0, 0x5DC, 0xBB8)
    Sound(844, 0, 100, 0)
    OP_9C(0xFE, 0x1F4, 0x0, 0x0, 0xC8, 0xBB8)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)

    label("loc_7835")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_784C")
    Sleep(1)
    Jump("loc_7835")

    label("loc_784C")

    Sleep(200)
    OP_9D(0xFE, 0xC8, 0xFFFFFD12, 0xFFFFF3E4, 0x2EE, 0x5DC)
    Return()

    # Function_32_77CE end

    def Function_33_7867(): pass

    label("Function_33_7867")

    Sleep(50)
    PlayEffect(0x3, 0xFF, 0xFE, 0x0, 0, 1200, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    Sound(540, 0, 100, 0)
    PlayEffect(0x3, 0xFF, 0xFE, 0x0, 0, 1200, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(400)
    Sleep(50)
    PlayEffect(0x3, 0xFF, 0xFE, 0x0, 0, 1200, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(250)
    Sound(540, 0, 100, 0)
    PlayEffect(0x3, 0xFF, 0xFE, 0x0, 0, 1200, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(350)
    Sound(540, 0, 100, 0)
    PlayEffect(0x3, 0xFF, 0xFE, 0x0, 0, 1200, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_33_7867 end

    def Function_34_799F(): pass

    label("Function_34_799F")

    Sleep(50)
    PlayEffect(0x7, 0xFF, 0x101, 0x0, 0, 800, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x7, 0xFF, 0x102, 0x0, 0, 800, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(400)
    PlayEffect(0x7, 0xFF, 0x103, 0x0, 0, 800, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(250)
    PlayEffect(0x7, 0xFF, 0x104, 0x0, 0, 800, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(350)
    PlayEffect(0x7, 0xFF, 0xF4, 0x0, 0, 800, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_34_799F end

    def Function_35_7AC2(): pass

    label("Function_35_7AC2")

    ClearChrFlags(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_35_7AC2 end

    def Function_36_7AD5(): pass

    label("Function_36_7AD5")

    OP_93(0xFE, 0xB3, 0x1F4)
    Sleep(300)
    OP_9B(0x0, 0xFE, 0x0, 0x514, 0x4B0, 0x0)
    OP_95(0xFE, 470, -750, -5220, 1200, 0x0)
    OP_93(0xFE, 0x87, 0x0)
    Return()

    # Function_36_7AD5 end

    def Function_37_7B0A(): pass

    label("Function_37_7B0A")

    SetChrFlags(0xFE, 0x40)
    OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0x3E8, 0x1)
    OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0xFA0, 0x1)
    OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x1388, 0x1)
    OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x1770, 0x1)
    OP_9B(0x0, 0xFE, 0x5, 0x3E8, 0x1B58, 0x1)
    OP_9B(0x0, 0xFE, 0xA, 0x3E8, 0x1B58, 0x1)
    OP_9B(0x0, 0xFE, 0xA, 0x3E8, 0x1B58, 0x1)
    SetChrChip(0x0, 0xFE, 0x32, 0x12C)
    OP_9B(0x0, 0xFE, 0x5, 0x9C4, 0x1B58, 0x1)
    SetChrFlags(0xFE, 0x20)
    Sound(844, 0, 50, 0)
    OP_9C(0xFE, 0xDAC, 0x6D6, 0xFFFFDECC, 0x7D0, 0xDAC)
    ClearChrFlags(0xFE, 0x20)
    OP_9B(0x0, 0xFE, 0x0, 0xFA, 0x1B58, 0x1)
    SetChrFlags(0xFE, 0x20)
    Sound(844, 0, 50, 0)
    OP_9C(0xFE, 0x3E8, 0xFA0, 0xFFFFF768, 0x1388, 0x9C4)
    ClearChrFlags(0xFE, 0x20)
    Return()

    # Function_37_7B0A end

    def Function_38_7BFC(): pass

    label("Function_38_7BFC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7C16")
    TurnDirection(0xFE, 0xC, 500)
    Sleep(300)
    Jump("Function_38_7BFC")

    label("loc_7C16")

    Return()

    # Function_38_7BFC end

    def Function_39_7C17(): pass

    label("Function_39_7C17")

    Sleep(200)
    Sound(287, 0, 100, 0)
    Sound(270, 0, 80, 0)
    Sound(225, 0, 70, 0)
    Sound(833, 0, 70, 0)
    Sound(825, 2, 100, 0)
    Sleep(1000)
    Sound(271, 0, 80, 0)
    Sound(287, 0, 60, 0)
    Sleep(1000)
    StopSound(225, 1000, 40)
    StopSound(825, 1000, 90)
    Return()

    # Function_39_7C17 end

    def Function_40_7C57(): pass

    label("Function_40_7C57")

    SetChrChipByIndex(0xFE, 0x42)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x2)
    Sound(1037, 0, 100, 0)
    SetChrSubChip(0xFE, 0x0)
    Sleep(400)
    SetChrSubChip(0xFE, 0x1)
    Sleep(400)
    SetChrSubChip(0xFE, 0x2)
    Sleep(400)
    Sound(1037, 0, 70, 0)
    SetChrSubChip(0xFE, 0x3)
    Sleep(400)
    SetChrSubChip(0xFE, 0x4)
    Sleep(400)
    Return()

    # Function_40_7C57 end

    def Function_41_7C95(): pass

    label("Function_41_7C95")

    SetChrChipByIndex(0xFE, 0x37)
    SetChrSubChip(0xFE, 0x0)
    Sleep(700)
    Sound(325, 0, 100, 0)
    SetChrSubChip(0xFE, 0x1)
    Sleep(300)
    Return()

    # Function_41_7C95 end

    def Function_42_7CAE(): pass

    label("Function_42_7CAE")

    Sleep(1500)
    Sound(936, 0, 100, 0)
    Sleep(400)
    Sound(936, 0, 80, 0)
    Sleep(400)
    Sound(936, 0, 80, 0)
    Return()

    # Function_42_7CAE end

    SaveToFile()

Try(main)
