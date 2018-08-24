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
        "Function_3_26BD",         # 03, 3
        "Function_4_26F9",         # 04, 4
        "Function_5_2735",         # 05, 5
        "Function_6_2771",         # 06, 6
        "Function_7_27AD",         # 07, 7
        "Function_8_27E9",         # 08, 8
        "Function_9_281B",         # 09, 9
        "Function_10_2B22",        # 0A, 10
        "Function_11_2BA9",        # 0B, 11
        "Function_12_2C72",        # 0C, 12
        "Function_13_2C7B",        # 0D, 13
        "Function_14_2C84",        # 0E, 14
        "Function_15_2C8D",        # 0F, 15
        "Function_16_2C96",        # 10, 16
        "Function_17_2C9F",        # 11, 17
        "Function_18_2CA8",        # 12, 18
        "Function_19_6E0C",        # 13, 19
        "Function_20_6E2E",        # 14, 20
        "Function_21_6F7A",        # 15, 21
        "Function_22_6F8D",        # 16, 22
        "Function_23_7082",        # 17, 23
        "Function_24_70EC",        # 18, 24
        "Function_25_710B",        # 19, 25
        "Function_26_721C",        # 1A, 26
        "Function_27_7288",        # 1B, 27
        "Function_28_7334",        # 1C, 28
        "Function_29_73D4",        # 1D, 29
        "Function_30_7474",        # 1E, 30
        "Function_31_751A",        # 1F, 31
        "Function_32_75BA",        # 20, 32
        "Function_33_7653",        # 21, 33
        "Function_34_778B",        # 22, 34
        "Function_35_78AE",        # 23, 35
        "Function_36_78C1",        # 24, 36
        "Function_37_78F6",        # 25, 37
        "Function_38_79E8",        # 26, 38
        "Function_39_7A03",        # 27, 39
        "Function_40_7A43",        # 28, 40
        "Function_41_7A81",        # 29, 41
        "Function_42_7A9A",        # 2A, 42
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
        "#00011F#6P(T-This place is...!)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00205F#12P#N(Amazing... It looks like\x01",
            "a vast quantity of energy\x01",
            "is gathering here...)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#00311F#12P(And... I thought they\x01",
            "might be here.)\x02",
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
            "#04809F#6PUhuhu... This is place\x01",
            "is amazing.\x02\x03",
            "#04800FSince you've stimulated\x01",
            "it this much, I guess\x01",
            "we're just about ready?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "White-Robed Man",
        (
            "#04704F#11PHehe, I wonder about\x01",
            "that.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x86, 0x1F4)
    Sleep(200)

    NpcTalk(
        0x8,
        "White-Robed Man",
        (
            "#04702F#5PYes, yes, it's sure to\x01",
            "be a fascinating show.\x02\x03",
            "If The Faceless were\x01",
            "alive, I'm sure he'd\x01",
            "enjoy it.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x9, 0xE1, 0x1F4)
    Sleep(100)

    ChrTalk(
        0x9,
        (
            "#04809F#11PAhaha, no doubt.\x02\x03",
            "#04805FHowever, if the Professor had come to\x01",
            "Crossbell in addition to you, Doctor,\x01",
            "things might have gotten out of hand.\x02\x03",
            "#04802FHe'd have even brought out the\x01",
            "Glorious and picked a fight with the\x01",
            "major powers.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "White-Robed Man",
        (
            "#04709F#5PHaha. Wouldn't have that\x01",
            "been quite interesting\x01",
            "in its own way?\x02",
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

    def lambda_C31():
        OP_9B(0x0, 0xFE, 0x166, 0x1F40, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C31)

    def lambda_C46():
        OP_9B(0x0, 0xFE, 0x166, 0x1F40, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C46)

    def lambda_C5B():
        OP_9B(0x0, 0xFE, 0x166, 0x1F40, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_C5B)

    def lambda_C70():
        OP_9B(0x0, 0xFE, 0x166, 0x1F40, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_C70)

    def lambda_C85():
        OP_9B(0x0, 0xFE, 0x166, 0x1F40, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_C85)

    def lambda_C9A():
        OP_9B(0x0, 0xFE, 0x166, 0x1F40, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_C9A)
    OP_63(0x9, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x9, 0x87, 0x1F4)

    ChrTalk(
        0x9,
        (
            "#04805F#5POh, what's wrong?\x02\x03",
            "#04800FMay I assume missions of\x01",
            "this level are too simple\x01",
            "and boring for you?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xA,
        "Armored Character",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5P─Everything is as that\x01",
            "person wills. I have no\x01",
            "objections.\x02\x03",
            "More importantly Doctor,\x01",
            "Campanella. That's enough\x01",
            "with your chatting.\x02\x03",
            "It appears we have\x01",
            "guests.\x07\x00\x02",
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

    def lambda_E4F():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_E4F)
    Sleep(50)

    def lambda_E5F():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_E5F)
    WaitChrThread(0x101, 1)

    def lambda_E70():
        OP_9B(0x0, 0xFE, 0x166, 0x2710, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E70)
    Sleep(50)

    def lambda_E88():
        OP_9B(0x0, 0xFE, 0x166, 0x2710, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_E88)
    Sleep(50)

    def lambda_EA0():
        OP_9B(0x0, 0xFE, 0x166, 0x2710, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_EA0)
    Sleep(50)

    def lambda_EB8():
        OP_9B(0x0, 0xFE, 0x166, 0x2710, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_EB8)
    Sleep(50)

    def lambda_ED0():
        OP_9B(0x0, 0xFE, 0x166, 0x2710, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_ED0)
    Sleep(50)

    def lambda_EE8():
        OP_9B(0x0, 0xFE, 0x166, 0x2710, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_EE8)
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
            "#00702F#12P#N...It seems more\x01",
            "monsters than I imagined\x01",
            "are gathered here.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x9,
        (
            "#04805F#5PAh, it's you guys, huh.\x02\x03",
            "#04804FThose bracer ladies\x01",
            "should be tied up around\x01",
            "now, but...\x02\x03",
            "#04802FUhuhu, I wonder how were\x01",
            "you able to locate this\x01",
            "place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F...#12P#NWell, it's a\x01",
            "trade secret.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#00301F#12P#NBut, you guys were\x01",
            "talkin' about some\x01",
            "interesting stuff, huh...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1159")

    ChrTalk(
        0x109,
        (
            "#10107F#12P#NYour plan... We can't\x01",
            "overlook it!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1197")

    label("loc_1159")


    ChrTalk(
        0x105,
        (
            "#10302F#12P#NWe can't very well\x01",
            "overlook it, now can we.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1197")

    OP_57(0x0)
    OP_5A()

    NpcTalk(
        0x8,
        "White-Robed Man",
        (
            "#04703F#5PHmm...\x02\x03",
            "#04701FYou're those Crossbell\x01",
            "Police recruits, I\x01",
            "presume?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F...#12PCrossbell Police,\x01",
            "Special Support Section.\x02\x03",
            "#00008FI suppose you're\x01",
            "officers of the society\x01",
            "of Ouroboros...\x02\x03",
            "#00001FFirst, could you\x01",
            "identify yourselves for\x01",
            "us?\x02",
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
            "#04705F#5PIdentify ourselves? What\x01",
            "is he saying?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#04806F#5PHmm, could he be going\x01",
            "through the formalities as a\x01",
            "policeman?\x02\x03",
            "#04802FUhuhu. We can only think of\x01",
            "revealing our identities to\x01",
            "our opponents as a bad joke.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xA,
        "Armored Character",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5PYou're certainly a\x01",
            "straightforward young\x01",
            "man, aren't you.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xA,
        "Armored Character",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5PI am sorry I cannot\x01",
            "comply with your\x01",
            "request, however...\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F...#11PIt's no use,\x01",
            "Lloyd.\x02\x03",
            "#00301FLooks like common sense\x01",
            "won't work with these\x01",
            "guys.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#00700F#12P#NIn that way, we should\x01",
            "think of them the same\x01",
            "as the Cult.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    NpcTalk(
        0x8,
        "White-Robed Man",
        (
            "#04703F#5PHmph, being lumped\x01",
            "together with them isn't\x01",
            "amusing in the slightest.\x02\x03",
            "#04702FHehe... very well. I'll\x01",
            "at least introduce\x01",
            "myself.\x02",
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
            "6th Anguis of Ouroboros and\x01",
            "supervisor of the Thirteen\x01",
            "Workshops.\x02\x03",
            "Hehe. Please, feel free to call me\x01",
            ""Doctor".\x02",
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
            "#00203F#12P#N...I see. It was your doing,\x01",
            "then.\x02\x03",
            "#00201FYou're the one who developed\x01",
            "the mysterious code used to\x01",
            "hack the orbal net.\x02",
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
            "#04705F#1POhhh!? You can\x01",
            "understand that code!?\x02\x03",
            "#04709FThat's my Astral Code!\x01",
            "Using the society's\x01",
            "network, it─\x02",
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
            "#04703F#5PNow that you mention it, I heard there\x01",
            "was a girl among the cult test subjects\x01",
            "those Epstein folks picked up...\x02\x03",
            "#04702F─How 'bout it, you!? Don't you want to\x01",
            "make use of that talent for Ouroboros!?\x02",
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
        "#04705F#5P#4SAck!\x02",
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
            "#04806F#5PHonestly... Just because\x01",
            "Renne has run away, aren't\x01",
            "you a little too desperate?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04701F#5PR-Renne really doesn't\x01",
            "have anything to do with\x01",
            "this, you know?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xA,
        "Armored Character",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5P─Then, I suppose it is\x01",
            "my turn.\x07\x00\x02",
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
            "#3888V7th Anguis of Ouroboros and crowned\x01",
            "with the name of Steel.\x02\x03",
            "#3889VIt is a pleasure to make your\x01",
            "acquaintance.\x07\x00\x02",
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
        "#00108F#12P#NWhat a clear voice...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#00301F#12P#NShe's wearing bulky\x01",
            "armor, but she seems\x01",
            "like a woman...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D02")

    ChrTalk(
        0x109,
        (
            "#10108F#12P#NShe's unbelievably\x01",
            "intimidating...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D44")

    label("loc_1D02")


    ChrTalk(
        0x105,
        (
            "#10301F#12P#NShe's intimidating like\x01",
            "you wouldn't believe...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D44")

    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#00700F#12P#N...So you're Ouroboros'\x01",
            "strongest warrior, huh.\x02\x03",
            "Indeed, you seem to\x01",
            "possess an awesome\x01",
            "fighting spirit, but─\x07\x00\x02",
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
            "#00702F#6P─I wonder how much of\x01",
            "that composure you can\x01",
            "maintain before I, Yin.\x07\x00\x02",
        )
    )

    OP_6F(0x79)
    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#04900F#11P#N............\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        "#00011F#5PH-Hey, Yin...\x02",
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
            "#04804F#5P#NUhuhu. I do think you've\x01",
            "got a pretty interesting\x01",
            "lineup here, but...\x02\x03",
            "#04800FBefore that, it appears\x01",
            "that the guardian of\x01",
            "this place has returned.\x02",
        )
    )

    OP_6F(0x79)
    CloseMessageWindow()

    def lambda_2036():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2036)
    Sleep(50)

    def lambda_2046():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2046)
    Sleep(50)

    def lambda_2056():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2056)
    Sleep(50)

    def lambda_2066():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2066)
    Sleep(50)

    def lambda_2076():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_2076)
    Sleep(100)

    ChrTalk(
        0x101,
        "#00005F#6PWhat...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_20C9")

    ChrTalk(
        0x109,
        "#10105F#12P"Guardian"?\x02",
    )

    CloseMessageWindow()
    Jump("loc_20E5")

    label("loc_20C9")


    ChrTalk(
        0x105,
        "#10305F#12P"Guardian"?\x02",
    )

    CloseMessageWindow()

    label("loc_20E5")

    Sleep(100)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    StopBGM(0xFA0)

    ChrTalk(
        0x103,
        (
            "#00208F#6PApproach of gigantic\x01",
            "aura confirmed...\x02\x03",
            "#00207FA large cryptid is\x01",
            "coming!\x02",
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

    def lambda_21F0():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_21F0)
    Sleep(50)

    def lambda_2200():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2200)
    Sleep(50)

    def lambda_2210():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2210)
    Sleep(50)

    def lambda_2220():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2220)
    Sleep(50)

    def lambda_2230():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_2230)
    Sleep(50)

    def lambda_2240():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_2240)
    Sleep(150)

    ChrTalk(
        0x104,
        "#00307F#5PWhat!?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_228F")

    ChrTalk(
        0x109,
        "#10101F#5PW-Where!?\x02",
    )

    CloseMessageWindow()
    Jump("loc_22C1")

    label("loc_228F")


    ChrTalk(
        0x105,
        (
            "#10308F#5PWhere the heck is it\x01",
            "coming from!?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22C1")

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

    def lambda_2358():
        OP_93(0x101, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2358)
    Sleep(50)

    def lambda_2368():
        OP_93(0x102, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_2368)
    Sleep(50)

    def lambda_2378():
        OP_93(0x103, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_2378)
    Sleep(50)

    def lambda_2388():
        OP_93(0x104, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_2388)
    Sleep(50)

    def lambda_2398():
        OP_93(0x106, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_2398)
    Sleep(50)

    def lambda_23A8():
        OP_93(0xF4, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_23A8)
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
            "#04804F#6P#NThe Sphinximera Cryptid...\x02\x03",
            "#04802FThe guardian of the divine\x01",
            "flower garden made of\x01",
            "ancient illusions, was it?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x8,
        (
            "#04704F#6P#NDear me, to think even\x01",
            "something like this is\x01",
            "materializing...\x02\x03",
            "#04702FHehe. Then we can expect\x01",
            "things to go as planned\x01",
            "as well.\x02",
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
        "#00010F#6P#NUgh!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#00310F#6P#NTch! If you're targetin'\x01",
            "someone, target those\x01",
            "guys!!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#00707F#6P#N─We'll talk later! Let's\x01",
            "exorcise it quickly!\x07\x00\x02",
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

    def Function_3_26BD(): pass

    label("Function_3_26BD")


    def lambda_26C2():
        OP_9B(0x1, 0xFE, 0x66, 0xFFFFFD12, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_26C2)

    def lambda_26D7():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_26D7)
    WaitChrThread(0xFE, 2)

    def lambda_26E8():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_26E8)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_3_26BD end

    def Function_4_26F9(): pass

    label("Function_4_26F9")


    def lambda_26FE():
        OP_9B(0x1, 0xFE, 0x126, 0xFFFFFD12, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_26FE)

    def lambda_2713():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2713)
    WaitChrThread(0xFE, 2)

    def lambda_2724():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2724)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_4_26F9 end

    def Function_5_2735(): pass

    label("Function_5_2735")


    def lambda_273A():
        OP_9B(0x1, 0xFE, 0x66, 0xFFFFFEA2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_273A)

    def lambda_274F():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_274F)
    WaitChrThread(0xFE, 2)

    def lambda_2760():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2760)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_5_2735 end

    def Function_6_2771(): pass

    label("Function_6_2771")


    def lambda_2776():
        OP_9B(0x1, 0xFE, 0x126, 0xFFFFFEA2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2776)

    def lambda_278B():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_278B)
    WaitChrThread(0xFE, 2)

    def lambda_279C():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_279C)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_6_2771 end

    def Function_7_27AD(): pass

    label("Function_7_27AD")


    def lambda_27B2():
        OP_9B(0x1, 0xFE, 0x126, 0xFFFFFF6A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_27B2)

    def lambda_27C7():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_27C7)
    WaitChrThread(0xFE, 2)

    def lambda_27D8():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_27D8)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0x13, 2)
    Return()

    # Function_7_27AD end

    def Function_8_27E9(): pass

    label("Function_8_27E9")

    OP_68(-4000, 1950, -6700, 800)
    MoveCamera(21, 12, -1, 800)
    OP_6F(0x79)
    OP_68(-4650, 1950, -8700, 800)
    OP_6F(0x79)
    Return()

    # Function_8_27E9 end

    def Function_9_281B(): pass

    label("Function_9_281B")

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

    def lambda_296B():
        OP_9D(0xFE, 0x29F4, 0xFFFFFE0C, 0xFFFFF8B2, 0x96, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_296B)
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

    def lambda_2A93():
        OP_9C(0xFE, 0x32, 0x0, 0x0, 0x546, 0x1194)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2A93)
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

    # Function_9_281B end

    def Function_10_2B22(): pass

    label("Function_10_2B22")

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

    # Function_10_2B22 end

    def Function_11_2BA9(): pass

    label("Function_11_2BA9")

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

    # Function_11_2BA9 end

    def Function_12_2C72(): pass

    label("Function_12_2C72")

    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_12_2C72 end

    def Function_13_2C7B(): pass

    label("Function_13_2C7B")

    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_13_2C7B end

    def Function_14_2C84(): pass

    label("Function_14_2C84")

    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_14_2C84 end

    def Function_15_2C8D(): pass

    label("Function_15_2C8D")

    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_15_2C8D end

    def Function_16_2C96(): pass

    label("Function_16_2C96")

    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_16_2C96 end

    def Function_17_2C9F(): pass

    label("Function_17_2C9F")

    SetChrChipByIndex(0xFE, 0x26)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_17_2C9F end

    def Function_18_2CA8(): pass

    label("Function_18_2CA8")

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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F44")
    LoadChrToIndex("chr/ch02950.itc", 0x2F)
    LoadChrToIndex("chr/ch02953.itc", 0x38)
    LoadChrToIndex("chr/ch0295F.itc", 0x3E)
    SetScenarioFlags(0x0, 0)
    AddParty(0x4, 0xFF, 0xFF)
    Jump("loc_2F5D")

    label("loc_2F44")

    LoadChrToIndex("chr/ch03050.itc", 0x2F)
    LoadChrToIndex("chr/ch03053.itc", 0x38)
    LoadChrToIndex("chr/ch0305F.itc", 0x3E)
    ClearScenarioFlags(0x0, 0)
    AddParty(0x8, 0xFF, 0xFF)

    label("loc_2F5D")

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

    def lambda_32D0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_32D0)
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
        "#00006F#6PUgh... *pant pant*...\x02",
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
        (
            "#04809F#5PUhuhu, you're quite\x01",
            "good㈱\x02",
        )
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

    def lambda_33E6():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_33E6)
    Sleep(50)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)

    def lambda_33FE():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_33FE)
    Sleep(50)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)

    def lambda_3416():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_3416)
    Sleep(50)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)

    def lambda_342E():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_342E)
    Sleep(50)
    SetChrChipByIndex(0xF4, 0xFF)
    SetChrSubChip(0xF4, 0x0)

    def lambda_3446():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_3446)
    Sleep(50)
    SetChrChipByIndex(0xB, 0x21)
    SetChrSubChip(0xB, 0x0)

    def lambda_345E():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_345E)
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
            "#04704F#5PHmm, I guess they're pretty\x01",
            "good for amateurs.\x02\x03",
            "#04700FAlso, it seems that orbal\x01",
            "staff those Foundation folks\x01",
            "made is pretty far along.\x02",
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
            "#00003F#12POuroboros─ Answer us\x01",
            "already!\x02\x03",
            "#00013FWhat are you trying to do\x01",
            "in the land of Crossbell!?\x02\x03",
            "#00007FI hope I'm wrong, but... It\x01",
            "was you who remanufactured\x01",
            "Gnosis, wasn't it!?\x02",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_375F")

    ChrTalk(
        0x109,
        "#10110F#11PN-No way...\x02",
    )

    CloseMessageWindow()

    label("loc_375F")


    ChrTalk(
        0x9,
        (
            "#04809F#5PHaha, the delinquent leader who\x01",
            "demonized, huh.\x02\x03",
            "I watched it too. It was quite the\x01",
            "show, wasn't it.\x02\x03",
            "#04802FUhuhu. If he had just gone a\x01",
            "little further, I could've invited\x01",
            "him into Ouroboros, though.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_385E")

    ChrTalk(
        0x105,
        "#10301F#11P............\x02",
    )

    CloseMessageWindow()

    label("loc_385E")


    ChrTalk(
        0x101,
        (
            "#00007F#12PDon't dodge the\x01",
            "question! Answer me!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04709F#1PHaha. I can understand why\x01",
            "you all think that, but...\x02\x03",
            "#04702FIn the end, we came only to\x01",
            "see how the "plan" is\x01",
            "progressing.\x02\x03",
            "The degree of stimulation of\x01",
            "the septium vein... and the\x01",
            "timing of the "promised day".\x02",
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
            "#00301F#12P#NTch, how vague can you\x01",
            "get?\x02",
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

    def lambda_3A05():
        OP_9B(0x1, 0xFE, 0x0, 0x190, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_3A05)
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
            "#00702F#12P─That's all they're\x01",
            "going to tell us.\x02\x03",
            "Starting now, we'll use\x01",
            "force to loosen their\x01",
            "tongues.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xBB8)

    ChrTalk(
        0x101,
        "#00008F#6PYin...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_3AFD")

    ChrTalk(
        0x109,
        (
            "#10107F#12P...It seems there's no\x01",
            "other way!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B31")

    label("loc_3AFD")


    ChrTalk(
        0x105,
        (
            "#10303F#12P...There's no other\x01",
            "path, is there.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B31")

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
        "#04704F#6POh my.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#04804F#6PHehe. I guess taking on\x01",
            "all of you would be too\x01",
            "much, even for me.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x9, 0x5A, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x9,
        "#04802F#12PCan I leave this to you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#04900F#5PI suppose there is no\x01",
            "choice.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3C82():
        OP_9B(0x1, 0xFE, 0x0, 0x4B0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_3C82)
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
            "#00105F#12P#NIt looks like a "lance"\x01",
            "used by middle age\x01",
            "knights...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#00306F#6P#NWhoa... What are you\x01",
            "doin' bringin' out an\x01",
            "antique like that?\x02",
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
            "#3890V#5P#30W─Do not waste your breath.\x02\x03",
            "#3891VCome at me full force using the\x01",
            "weapons each of you is specialized\x01",
            "in.\x02\x03",
            "#3892VOr else you will die.\x07\x00\x02",
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
        "#00005F#6P#N...!?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#00707F#12P#NIncoming─!\x07\x00\x02",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_41CE")
    Sound(2464, 255, 100, 4)
    Jump("loc_41D4")

    label("loc_41CE")

    Sound(2404, 255, 100, 4)

    label("loc_41D4")

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
            "#04900F#5P............\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_42B5")

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
            "#00310F#12P#30W#NS-She unleashed tens of\x01",
            "super-high speed thrusts\x01",
            "in an instant?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_433F")

    label("loc_42B5")


    ChrTalk(
        0x104,
        "#00310F#12P#30W#NGuh... No way...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x105,
        (
            "#10310F#12P#30W#N...She unleashed tens of\x01",
            "super-high speed thrusts\x01",
            "that quickly, huh...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_433F")


    ChrTalk(
        0x103,
        (
            "#00206F#12P#30W#N...Unbelievable... That\x01",
            "isn't something a human\x01",
            "can do...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#00710F#11P#30W......Ugh......\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04702F#5POhhh, to think there's\x01",
            "someone who can resist\x01",
            "the Steel Maiden's lance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#04809F#5PUhuhu. Looks like you aren't\x01",
            "called the demon of Eastern\x01",
            "Quarter for nothing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#04900F#5PVery good reflexes.\x02\x03",
            "However, compared to your\x01",
            ""predecessor", it appears\x01",
            "you still have some doubts.\x07\x00\x02",
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
        "#00011F#12P...!\x02",
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
        "#00205F#11PRixia...?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_47BA")

    ChrTalk(
        0x109,
        "#10111F#5PH-Huuuh...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_47FA")

    label("loc_47BA")


    ChrTalk(
        0x105,
        (
            "#10301F#5PAmazing... So you were\x01",
            "altering your\x01",
            "presence...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_47FA")

    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x9,
        (
            "#04809F#5PAhaha, this is hilarious!\x02\x03",
            "To think Yin's true identity\x01",
            "is that of Rixia Mao, the\x01",
            "Arc-en-Ciel co-star!!\x02\x03",
            "#04802FUhuhu, isn't this quite the\x01",
            "amusing drama?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#00711F#5P......Ugh......\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    OP_A7(0x5, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrPos(0x5, -900, -750, -23000, 0)
    Sleep(300)
    OP_C9(0x0, 0x80000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_4985")

    NpcTalk(
        0x105,
        "Young Man's Voice",
        (
            "#2915V#6P#25A─Dear me. it seems we\x01",
            "arrived during an\x01",
            "amazing scene.\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    Jump("loc_49C1")

    label("loc_4985")


    NpcTalk(
        0x109,
        "Girl's Voice",
        "#3519V#6P#20AEveryone, are you ok!?\x02",
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)

    label("loc_49C1")

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

    def lambda_4A99():
        OP_9B(0x0, 0xFE, 0x0, 0x1F40, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x5, 1, lambda_4A99)
    Sleep(100)

    def lambda_4AB1():
        OP_9B(0x0, 0xFE, 0x0, 0x1F40, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_4AB1)
    Sleep(50)

    def lambda_4AC9():
        OP_9B(0x0, 0xFE, 0x0, 0x1F40, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_4AC9)
    Sleep(50)

    def lambda_4AE1():
        OP_9B(0x0, 0xFE, 0x0, 0x1F40, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_4AE1)

    def lambda_4AF6():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_4AF6)
    Sleep(50)

    def lambda_4B06():
        OP_93(0xFE, 0xB5, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_4B06)
    Sleep(50)

    def lambda_4B16():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_4B16)
    Sleep(50)

    def lambda_4B26():
        OP_93(0xFE, 0xB5, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_4B26)
    Sleep(50)

    def lambda_4B36():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4B36)
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_4BB6")

    ChrTalk(
        0x101,
        (
            "#00008F#6P#NWazy... And Arios and\x01",
            "everyone else, too...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4BF3")

    label("loc_4BB6")


    ChrTalk(
        0x101,
        (
            "#00008F#6P#NNoｱl... And Arios and\x01",
            "everyone else, too...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4BF3")

    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        "#00106F#6PYou came for us...\x02",
    )

    CloseMessageWindow()
    Sleep(50)

    def lambda_4C20():
        OP_9B(0x0, 0xFE, 0x163, 0x1A90, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x5, 1, lambda_4C20)
    Sleep(100)

    def lambda_4C38():
        OP_9B(0x0, 0xFE, 0x0, 0x1964, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_4C38)
    Sleep(150)

    def lambda_4C50():
        OP_9B(0x0, 0xFE, 0x0, 0x1964, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_4C50)
    Sleep(50)

    def lambda_4C68():
        OP_9B(0x0, 0xFE, 0x0, 0x1964, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_4C68)
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
        "#12PThose Snake guys, huh!?\x02",
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
            "#4053V#11P#40WCampanella The Fool...\x02\x03",
            "#4054VAnd the Thirteen Workshops\x01",
            "supervisor and the Steel Maiden...\x02",
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
            "#04705F#5P#NHoho... And is that one\x01",
            "the Divine Blade of\x01",
            "Wind, perhaps?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x9,
        (
            "#04802F#5P#NUhuhu. It seems his\x01",
            "skills are a match for\x01",
            "Loewe's...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#04900F#5P#N─Divine Blade of Wind. I\x01",
            "suppose this is the first\x01",
            "time we've faced one another.\x02\x03",
            "I see. Your skills are as\x01",
            "magnificent as the rumors\x01",
            "say.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xF,
        (
            "#01403F#11P...Enough with the\x01",
            "flattery.\x02\x03",
            "I can't accept it until I\x01",
            "surpass "human limits" as\x01",
            "you have.\x02\x03",
            "#01401FBefore that lance of yours,\x01",
            "even an army would have no\x01",
            "choice but to retreat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#04900F#5P#NHehe. You are quite\x01",
            "something even just for\x01",
            "having seen through that.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xD,
        "#6PArios...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#12PYou don't mean... We're\x01",
            "letting them go!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#01403F#11PNo... However, we're at\x01",
            "a disadvantage here.\x02",
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

    def lambda_5263():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x2EE)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_5263)
    Sleep(400)
    PlayEffect(0x5, 0xFF, 0x11, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_52AE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x2EE)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_52AE)
    Sleep(400)
    PlayEffect(0x5, 0xFF, 0x12, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_52F9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x2EE)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_52F9)
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

    def lambda_53D9():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x5, 1, lambda_53D9)
    Sleep(150)

    def lambda_53E9():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_53E9)
    Sleep(150)

    def lambda_53F9():
        OP_93(0xFE, 0xB5, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_53F9)
    Sleep(250)

    ChrTalk(
        0x10,
        "#11P............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#5PUgh... The ones Ling and\x01",
            "Eolia fought?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_54A3")

    ChrTalk(
        0x105,
        (
            "#10301F#11PLooks like these ladies\x01",
            "aren't your ordinary\x01",
            "foes either...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_54DB")

    label("loc_54A3")


    ChrTalk(
        0x109,
        (
            "#10108F#11PUgh... (They have no\x01",
            "openings at all!?)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_54DB")

    OP_68(240, 1000, -7460, 1500)
    MoveCamera(25, 10, -1, 1500)
    OP_6E(530, 1500)
    SetCameraDistance(20910, 1500)
    OP_6F(0x79)

    ChrTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#04900F#5P#N─Enough. There is no\x01",
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
        "#5PHehe, understood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#11PAs the Master wishes.\x02",
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

    def lambda_55C6():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFD12, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_55C6)
    Sleep(100)

    def lambda_55DE():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFD12, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_55DE)
    Sleep(100)

    def lambda_55F6():
        OP_9B(0x1, 0xFE, 0x13B, 0xFFFFFD44, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_55F6)
    Sleep(500)

    ChrTalk(
        0x101,
        "#00010F#1PGuh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#00712F#11P............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#04804F#5P#NUhuhu. Looks like it's\x01",
            "about time.\x02",
        )
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

    def lambda_56B6():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_56B6)

    def lambda_56C3():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_56C3)

    def lambda_56D0():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_56D0)

    def lambda_56DD():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_56DD)

    def lambda_56EA():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_56EA)

    def lambda_56F7():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_56F7)

    def lambda_5704():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x5, 2, lambda_5704)

    def lambda_5711():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_5711)

    def lambda_571E():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_571E)

    ChrTalk(
        0x8,
        (
            "#04704F#5PI was able to confirm the\x01",
            ""plan"'s progression and\x01",
            "the septium vein status.\x02\x03",
            "#04702FHehe. It's about time I\x01",
            "got back to the "finishing\x01",
            "touches" as well.\x02",
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
        "#00007F#12P#NW-Wait!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xF,
        (
            "#01407F#12P#N...As you might imagine,\x01",
            "we can't let you get\x01",
            "away like this!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#04900F#5PI will give you one\x01",
            "warning.\x02\x03",
            "In regard to this "plan",\x01",
            "we have nothing more than\x01",
            "a mere supporting role.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#12P#NHuh...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xF,
        "#01405FWhat#12P#N...?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#04900F#5PIn time, the beasts will be\x01",
            "released and chaos will\x01",
            "visit this land.\x02\x03",
            "Even so, take care not to be\x01",
            "swallowed up by the tragedy\x01",
            "that unfolds before you.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#04802F#5PUhuhu... Then, have a\x01",
            "nice day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04709F#5PHaha. Please look\x01",
            "forward to our next\x01",
            "encounter.\x02",
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

    def lambda_5B51():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_5B51)
    Sound(1035, 0, 100, 0)
    Sound(977, 0, 100, 0)
    Sleep(400)
    StopEffect(0x1, 0x2)

    def lambda_5B74():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_5B74)
    Sound(1035, 0, 100, 0)
    Sleep(400)
    StopEffect(0x2, 0x2)

    def lambda_5B91():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_5B91)
    Sound(1035, 0, 100, 0)
    Sleep(400)
    StopSound(959, 1000, 100)
    Sleep(600)

    def lambda_5BB4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_5BB4)
    Sleep(400)

    def lambda_5BC8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_5BC8)
    Sleep(400)

    def lambda_5BDC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_5BDC)
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
        "#11PUgh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11POuroboros... They're one\x01",
            "a hell of a bunch.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#00713F#11P#40W...............\x02",
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
        "#00108F#11PRixia...\x02",
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
            "#00713F#3249V...Excuse me...\x02",
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
            "#00108F#6PUnbelievable things have been\x01",
            "happening, one after the next. It\x01",
            "feels like this can't be real...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00306F#12P...Yeah...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00208F#6PIt almost feels like I'm\x01",
            "dreaming...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10106F#6PMaybe we really are...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10308F#12PThere's Wald too... I\x01",
            "think this is some kind\x01",
            "of nightmare, though.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0xF,
        (
            "#01403F#4068V#5P#40WHowever─ This is\x01",
            "unmistakable reality.\x02",
        )
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

    def lambda_628A():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_628A)
    Sleep(50)

    def lambda_629A():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_629A)

    def lambda_62A7():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_62A7)
    Sleep(50)

    def lambda_62B7():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_62B7)

    def lambda_62C4():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_62C4)

    def lambda_62D1():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_62D1)
    Sleep(50)

    def lambda_62E1():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_62E1)

    def lambda_62EE():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_62EE)
    Sleep(300)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7561", 0)

    ChrTalk(
        0x101,
        "#00001F#6PArios...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0x101, 500)

    ChrTalk(
        0xF,
        (
            "#01401F#5POuroboros left us more\x01",
            "clues than I thought they\x01",
            "would.\x02\x03",
            "The meaning of this place\x01",
            "and also "In time, beasts\x01",
            "will be released"...\x02\x03",
            "#01403FIt seems we have no time\x01",
            "to stay dumbfounded.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00013F#6PR-Right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00311F#12P("Beasts"... It can't\x01",
            "be...)\x02",
        )
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

    def lambda_64D3():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_64D3)

    def lambda_64E0():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_64E0)
    Sleep(50)

    def lambda_64F0():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_64F0)

    def lambda_64FD():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_64FD)
    Sleep(50)

    def lambda_650D():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_650D)

    def lambda_651A():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_651A)
    Sleep(50)

    def lambda_652A():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_652A)

    def lambda_6537():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_6537)
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
            "#00011F#6PT-That's right. I guess\x01",
            "orbal waves do reach\x01",
            "here, don't they.\x02",
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
            "#00007F─Yes! Special Support\x01",
            "Section, Bannings\x01",
            "speaking.\x02",
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
            "#3459V#30WIt's Dudley.\x02\x03",
            "#3460VI heard you headed to\x01",
            "the lake's south bank.\x01",
            "Are you there now?\x02",
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
            "#00001FUmm... Many things\x01",
            "happened and we're with\x01",
            "Arios and the others.\x02",
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
            "Perfect timing, then. Tell\x01",
            "them all too, since\x01",
            "they're there.\x02\x03",
            "─All members of Red\x01",
            "Constellation have\x01",
            "disappeared from the city.\x02",
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
            "Can you come back\x01",
            "immediately?\x02",
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
        "#00101F#5PW-What's wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10113F#5PYou were quite\x01",
            "flustered...\x02",
        )
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
            "Lloyd briefly explained\x01",
            "the intel from Dudley.\x07\x00\x02",
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
        "#00205F#11PThat's...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#11PRed Constellation has...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5PUgh... We were keeping\x01",
            "tabs on them too.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xF)

    ChrTalk(
        0xF,
        (
            "#01403F#5P─Lloyd. You all hurry\x01",
            "and return to the city.\x02\x03",
            "#01400FWe'll return after\x01",
            "investigating this\x01",
            "place.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)

    def lambda_6BCB():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6BCB)
    Sleep(50)

    def lambda_6BDB():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6BDB)

    def lambda_6BE8():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6BE8)
    Sleep(50)

    def lambda_6BF8():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6BF8)

    def lambda_6C05():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6C05)

    def lambda_6C12():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6C12)
    Sleep(250)

    ChrTalk(
        0x101,
        (
            "#00011F#6PAh...\x02\x03",
            "#00003FSorry. Thanks for doing\x01",
            "that for us.\x02",
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
        (
            "#11PWe're all the same in\x01",
            "times like these.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5PAnd it'll probably take us\x01",
            "a little longer because of\x01",
            "Ling and Eolia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#01403F#5PIf Red Constellation has\x01",
            "acted, Heiyue should\x01",
            "have acted as well...\x02\x03",
            "#01401FWe'll be back as soon as\x01",
            "we can. You all should\x01",
            "be careful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00007F#6PRight!\x02",
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

    # Function_18_2CA8 end

    def Function_19_6E0C(): pass

    label("Function_19_6E0C")

    OP_71(0x0, 0x157, 0x16C, 0x0, 0x0)
    OP_79(0x0)
    Sound(913, 0, 100, 0)
    OP_71(0x0, 0x16D, 0x17E, 0x0, 0x20)
    Return()

    # Function_19_6E0C end

    def Function_20_6E2E(): pass

    label("Function_20_6E2E")

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

    label("loc_6EC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6F1A")
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
    Jump("loc_6EC8")

    label("loc_6F1A")

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

    # Function_20_6E2E end

    def Function_21_6F7A(): pass

    label("Function_21_6F7A")

    Sleep(2000)
    OP_9B(0x1, 0xFE, 0x0, 0xFFFFFD12, 0x1F4, 0x1)
    Return()

    # Function_21_6F7A end

    def Function_22_6F8D(): pass

    label("Function_22_6F8D")

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

    def lambda_702C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_702C)
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

    # Function_22_6F8D end

    def Function_23_7082(): pass

    label("Function_23_7082")

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

    # Function_23_7082 end

    def Function_24_70EC(): pass

    label("Function_24_70EC")

    SetChrChipByIndex(0xFE, 0x31)
    Sound(531, 0, 100, 0)
    Sound(358, 0, 70, 0)
    SetChrSubChip(0xFE, 0x0)
    Sleep(100)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    Return()

    # Function_24_70EC end

    def Function_25_710B(): pass

    label("Function_25_710B")

    SetChrChipByIndex(0xFE, 0x31)
    SetChrSubChip(0xFE, 0x1)
    Sleep(200)
    SetChrChip(0x0, 0xFE, 0x1E, 0x12C)

    def lambda_7123():
        OP_9D(0xFE, 0xFFFFFF06, 0xFFFFFD12, 0x726, 0x96, 0x1B58)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_7123)
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

    # Function_25_710B end

    def Function_26_721C(): pass

    label("Function_26_721C")

    SetChrSubChip(0xFE, 0x5)
    Sleep(200)
    SetChrChip(0x0, 0xFE, 0x1E, 0x12C)
    Sound(844, 0, 60, 0)
    Sound(250, 0, 80, 0)

    def lambda_723C():
        OP_9D(0xFE, 0x258, 0xFA, 0x1900, 0x60E, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_723C)
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

    # Function_26_721C end

    def Function_27_7288(): pass

    label("Function_27_7288")

    SetChrChipByIndex(0xFE, 0x33)
    SetChrSubChip(0xFE, 0x0)

    label("loc_7290")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_72B7")
    OP_A6(0xFE, 0x1E, 0x1E, 0xFA, 0xBB8)
    Jump("loc_7290")

    label("loc_72B7")

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

    # Function_27_7288 end

    def Function_28_7334(): pass

    label("Function_28_7334")

    SetChrChipByIndex(0xFE, 0x34)
    SetChrSubChip(0xFE, 0x0)

    label("loc_733C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7363")
    OP_A6(0xFE, 0x1E, 0x1E, 0xFA, 0xBB8)
    Jump("loc_733C")

    label("loc_7363")

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

    # Function_28_7334 end

    def Function_29_73D4(): pass

    label("Function_29_73D4")

    SetChrChipByIndex(0xFE, 0x35)
    SetChrSubChip(0xFE, 0x0)

    label("loc_73DC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7403")
    OP_A6(0xFE, 0x1E, 0x1E, 0xFA, 0xBB8)
    Jump("loc_73DC")

    label("loc_7403")

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

    # Function_29_73D4 end

    def Function_30_7474(): pass

    label("Function_30_7474")

    SetChrChipByIndex(0xFE, 0x36)
    SetChrSubChip(0xFE, 0x0)

    label("loc_747C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_74A3")
    OP_A6(0xFE, 0x1E, 0x1E, 0xFA, 0xBB8)
    Jump("loc_747C")

    label("loc_74A3")

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

    # Function_30_7474 end

    def Function_31_751A(): pass

    label("Function_31_751A")

    SetChrChipByIndex(0xFE, 0x38)
    SetChrSubChip(0xFE, 0x0)

    label("loc_7522")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7549")
    OP_A6(0xFE, 0x1E, 0x1E, 0xFA, 0xBB8)
    Jump("loc_7522")

    label("loc_7549")

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

    # Function_31_751A end

    def Function_32_75BA(): pass

    label("Function_32_75BA")

    SetChrChip(0x0, 0xFE, 0x32, 0x12C)
    Sound(844, 0, 100, 0)
    OP_9C(0xFE, 0xDAC, 0x0, 0xFFFFFE0C, 0x3E8, 0xBB8)
    Sound(844, 0, 100, 0)
    OP_9C(0xFE, 0xFFFFF060, 0x0, 0x0, 0x5DC, 0xBB8)
    Sound(844, 0, 100, 0)
    OP_9C(0xFE, 0x1F4, 0x0, 0x0, 0xC8, 0xBB8)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)

    label("loc_7621")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7638")
    Sleep(1)
    Jump("loc_7621")

    label("loc_7638")

    Sleep(200)
    OP_9D(0xFE, 0xC8, 0xFFFFFD12, 0xFFFFF3E4, 0x2EE, 0x5DC)
    Return()

    # Function_32_75BA end

    def Function_33_7653(): pass

    label("Function_33_7653")

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

    # Function_33_7653 end

    def Function_34_778B(): pass

    label("Function_34_778B")

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

    # Function_34_778B end

    def Function_35_78AE(): pass

    label("Function_35_78AE")

    ClearChrFlags(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_35_78AE end

    def Function_36_78C1(): pass

    label("Function_36_78C1")

    OP_93(0xFE, 0xB3, 0x1F4)
    Sleep(300)
    OP_9B(0x0, 0xFE, 0x0, 0x514, 0x4B0, 0x0)
    OP_95(0xFE, 470, -750, -5220, 1200, 0x0)
    OP_93(0xFE, 0x87, 0x0)
    Return()

    # Function_36_78C1 end

    def Function_37_78F6(): pass

    label("Function_37_78F6")

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

    # Function_37_78F6 end

    def Function_38_79E8(): pass

    label("Function_38_79E8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7A02")
    TurnDirection(0xFE, 0xC, 500)
    Sleep(300)
    Jump("Function_38_79E8")

    label("loc_7A02")

    Return()

    # Function_38_79E8 end

    def Function_39_7A03(): pass

    label("Function_39_7A03")

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

    # Function_39_7A03 end

    def Function_40_7A43(): pass

    label("Function_40_7A43")

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

    # Function_40_7A43 end

    def Function_41_7A81(): pass

    label("Function_41_7A81")

    SetChrChipByIndex(0xFE, 0x37)
    SetChrSubChip(0xFE, 0x0)
    Sleep(700)
    Sound(325, 0, 100, 0)
    SetChrSubChip(0xFE, 0x1)
    Sleep(300)
    Return()

    # Function_41_7A81 end

    def Function_42_7A9A(): pass

    label("Function_42_7A9A")

    Sleep(1500)
    Sound(936, 0, 100, 0)
    Sleep(400)
    Sound(936, 0, 80, 0)
    Sleep(400)
    Sound(936, 0, 80, 0)
    Return()

    # Function_42_7A9A end

    SaveToFile()

Try(main)
