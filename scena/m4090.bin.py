from ScenarioHelper import *

def main():
    CreateScenaFile(
        "m4090.bin",                # FileName
        "m4090",                    # MapName
        "m4090",                    # Location
        0x007E,                     # MapIndex
        "ed7350",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x27,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 126, 0, 0, 0, 1],
    )

    BuildStringList((
        "m4090",                  # 0
        "Ernest",             # 1
        "Hartmann former chairman",       # 2
        "Dummy Hartmann",       # 3
        "魔人Ernest",         # 4
        "Young man in clothing appearance",           # 5
        "Dummy effect",       # 6
        "Dummy effect",       # 7
        "Dummy effect",       # 8
        "Dummy effect",       # 9
        "SE control",                 # 10
        "bm4030",                 # 11
        "bm4040",                 # 12
    ))

    ATBonus("ATBonus_1DC", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_29C", 8, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_2A0", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2A4", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2A8", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2AC", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2B0", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2B4", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2B8", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_27C", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_280", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_284", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_288", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_28C", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_290", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_294", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_298", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_2BC", 8, 16, 180)
    MonsterBattlePostion("MonsterBattlePostion_2C0", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2C4", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2C8", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2CC", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2D0", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2D4", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2D8", 0, 0, 180)

    # monster count: 0

    # event battle count: 2

    BattleInfo(
        "BattleInfo_2DC", 0x0042, 3, 6, 45, 3, 3, 30, 0, "bm4030", 0x00000000, 100, 0, 0, 0,
        (
            ("ms67400.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_29C", "MonsterBattlePostion_27C", "ed7451", "ed7000", "ATBonus_1DC"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_320", 0x004A, 3, 6, 45, 3, 3, 30, 0, "bm4040", 0x00000000, 100, 0, 0, 0,
        (
            ("ms88000.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_2BC", "MonsterBattlePostion_27C", "ed7454", "ed7000", "ATBonus_1DC"),
            (),
            (),
            (),
        )
    )

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    228,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    254,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    254,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    254,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    254,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(1020, 0)                                       # 0

    ScpFunction((
        "Function_0_3FC",          # 00, 0
        "Function_1_437",          # 01, 1
        "Function_2_474",          # 02, 2
        "Function_3_493",          # 03, 3
        "Function_4_1BB5",         # 04, 4
        "Function_5_1BF0",         # 05, 5
        "Function_6_1C03",         # 06, 6
        "Function_7_3A06",         # 07, 7
        "Function_8_3A66",         # 08, 8
        "Function_9_3A8A",         # 09, 9
        "Function_10_3AAE",        # 0A, 10
        "Function_11_3AD8",        # 0B, 11
        "Function_12_3AFA",        # 0C, 12
        "Function_13_3B1F",        # 0D, 13
        "Function_14_3D15",        # 0E, 14
        "Function_15_3D92",        # 0F, 15
        "Function_16_3DEE",        # 10, 16
        "Function_17_3F55",        # 11, 17
        "Function_18_41A9",        # 12, 18
        "Function_19_41F6",        # 13, 19
        "Function_20_6A4C",        # 14, 20
        "Function_21_6A79",        # 15, 21
        "Function_22_6A9E",        # 16, 22
        "Function_23_6AC3",        # 17, 23
        "Function_24_6AFB",        # 18, 24
        "Function_25_6ED5",        # 19, 25
        "Function_26_703E",        # 1A, 26
        "Function_27_718F",        # 1B, 27
        "Function_28_71E4",        # 1C, 28
        "Function_29_71FE",        # 1D, 29
        "Function_30_726A",        # 1E, 30
        "Function_31_72AA",        # 1F, 31
        "Function_32_72EA",        # 20, 32
        "Function_33_7304",        # 21, 33
        "Function_34_731E",        # 22, 34
        "Function_35_7338",        # 23, 35
        "Function_36_73A6",        # 24, 36
        "Function_37_7414",        # 25, 37
    ))


    def Function_0_3FC(): pass

    label("Function_0_3FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x121, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_40D")
    Event(0, 3)

    label("loc_40D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_424")
    ClearScenarioFlags(0x22, 0)
    SetScenarioFlags(0x0, 0)
    Event(0, 6)
    Jump("loc_436")

    label("loc_424")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_436")
    ClearScenarioFlags(0x22, 1)
    SetScenarioFlags(0x0, 1)
    Event(0, 19)

    label("loc_436")

    Return()

    # Function_0_3FC end

    def Function_1_437(): pass

    label("Function_1_437")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_44C")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1FE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 0)

    label("loc_44C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_461")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1C6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 1)

    label("loc_461")

    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x4)
    Sound(129, 1, 100, 0)
    Return()

    # Function_1_437 end

    def Function_2_474(): pass

    label("Function_2_474")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_492")
    OP_A1(0xFE, 0x708, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_2_474")

    label("loc_492")

    Return()

    # Function_2_474 end

    def Function_3_493(): pass

    label("Function_3_493")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00051.itc", 0x1F)
    LoadChrToIndex("chr/ch02950.itc", 0x20)
    LoadChrToIndex("chr/ch02951.itc", 0x21)
    LoadChrToIndex("chr/ch02300.itc", 0x22)
    LoadChrToIndex("chr/ch06500.itc", 0x23)
    LoadChrToIndex("monster/ch67450.itc", 0x24)
    LoadChrToIndex("chr/ch02952.itc", 0x25)
    LoadChrToIndex("chr/ch02350.itc", 0x26)
    LoadChrToIndex("monster/ch67452.itc", 0x27)
    LoadChrToIndex("chr/ch02357.itc", 0x28)
    LoadEffect(0x0, "event\\ev602_01.eff")
    LoadEffect(0x1, "event\\ev602_02.eff")
    LoadEffect(0x2, "event\\ev602_00.eff")
    SoundLoad(832)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu06600.itp")
    OP_68(0, -400, -20400, 0)
    MoveCamera(0, 23, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x101, 50, -1400, -24400, 0)
    SetChrPos(0x109, -100, -1400, -26400, 0)
    SetChrChipByIndex(0x8, 0x22)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 0, 200, 30500, 0)
    SetChrChipByIndex(0x9, 0x23)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, -1500, 200, 29800, 45)
    SetChrChipByIndex(0xB, 0x24)
    SetChrSubChip(0xB, 0x0)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, 0, 200, 28500, 180)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_52(0xB, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapObjFlags(0x0, 0x1000)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x1000)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFrame(0xFF, "bl_ato00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "bl_ato01", 0x0, 0x1)
    OP_68(0, -400, -17400, 3000)
    SetCameraDistance(18500, 3000)

    def lambda_685():
        OP_97(0x101, 0x0, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_685)
    Sleep(30)

    def lambda_6A2():
        OP_97(0x109, 0x0, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_6A2)
    FadeToBright(2000, 0)
    OP_0D()
    StopBGM(0xBB8)
    WaitChrThread(0x101, 0)

    ChrTalk(
        0x101,
        "#00007F(Ah……!)\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x109, 0)

    ChrTalk(
        0x109,
        "#6P#10101F(There was …!\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7510", 0)
    OP_68(0, 6000, 37500, 5000)
    MoveCamera(0, -3, 0, 5000)
    OP_6E(800, 5000)
    SetCameraDistance(29500, 5000)
    OP_6F(0x79)
    Sleep(1000)
    Fade(500)
    OP_68(0, 1300, 32000, 0)
    MoveCamera(329, 15, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18500, 0)
    SetCameraDistance(17500, 1500)
    OP_0D()
    OP_95(0x8, 0, 200, 32000, 1500, 0x0)
    OP_6F(0x79)

    ChrTalk(
        0x8,
        (
            "#02613FPowered by Translate\x01",
            "As I heard from Mr. Joachim.\x02\x03",
            "#02610FIn this place my purpose also\x01",
            "Everything will be delivered without delay.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6P#02703FCut … Do not do it!\x02\x03",
            "#02701FWith Joachim and nice you,\x01",
            "Do something you touched … …!\x02\x03",
            "Kimi to your delusions\x01",
            "Do not involve me!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 500)

    ChrTalk(
        0x8,
        (
            "#11P#02613FHaha, you are the only person\x01",
            "Is it in such a position as to say it confusingly?\x02\x03",
            "#02610FWas it \"paradise\" …?\x01",
            "In spite of using such a place\x01",
            "It is quite a great saying, is not it?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_63(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(300)

    ChrTalk(
        0x9,
        (
            "#6P#02705FOh, that in the hands of the cult\x01",
            "Just being taken over by being deceived … …\x02\x03",
            "#02703FIf you know that such a bad taste\x01",
            "Are you surely thrusting your neck!\x02\x03",
            "#02701FBesides, even a strange medicine is served ……\x01",
            "Wow, I am the perfect victim!\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x9)

    ChrTalk(
        0x8,
        (
            "#11P#02613FWell, such an explanation\x01",
            "Do you think that you can pass the world?\x02\x03",
            "#02610FIf you cross-exclusive coverage of the Crossbell Times\x01",
            "It will rise excitingly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#6P#02701FDamn\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(2090, 255, 100, 0)

    NpcTalk(
        0x101,
        "Voice of Lloyd",
        "#30W#12AThat's it …!\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_B6D():
        OP_93(0x8, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_B6D)
    Sleep(50)

    def lambda_B7D():
        OP_93(0x9, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_B7D)
    Sleep(50)
    WaitChrThread(0x8, 0)
    WaitChrThread(0x9, 0)
    SetChrPos(0x101, -600, 200, 12600, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrPos(0x109, 800, 200, 11900, 0)
    SetChrChipByIndex(0x109, 0x20)
    SetChrSubChip(0x109, 0x0)
    OP_68(-500, 1200, 25870, 3000)
    MoveCamera(329, 14, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(18000, 3000)
    Sleep(1000)
    BeginChrThread(0x11, 1, 0, 5)

    def lambda_BFE():
        OP_97(0x101, 0x0, 0x0, 0x2710, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_BFE)
    Sleep(100)

    def lambda_C1B():
        OP_97(0x109, 0x0, 0x0, 0x2710, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_C1B)
    Sleep(500)

    def lambda_C38():
        OP_95(0xFE, 0, 200, 28500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_C38)
    OP_6F(0x79)

    ChrTalk(
        0x9,
        "#11P#02705FOh, you guys …!\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x8, 1)

    ChrTalk(
        0x8,
        (
            "#02605F#11PAw, you guys.\x02\x03",
            "#02613FIf you thought you did spread the troublesome people\x01",
            "Terada Zako got into it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00013FThat huge altar ……\x01",
            "Is this the innermost of the lodge?\x02\x03",
            "#00007FWhat happened to Arios! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02610F#11POh, \"The sword of the wind\" and\x01",
            "Which one of the investigation division ace?\x02\x03",
            "#02613FBecause it was troublesome as expected\x01",
            "I was stopped.\x02\x03",
            "About this time, 10 magical dolls to partner\x01",
            "It will be around the moment.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x32, 0x0, 0x7D0, 0xC8)

    ChrTalk(
        0x101,
        "#6P#00010FBecome\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10110FTen of that thing … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02613F#11PThanks to you I inherited from my teacher.\x01",
            "I used up all the frames.\x02\x03",
            "#02610FBut with those people\x01",
            "You can surely clean up.\x02\x03",
            "I slowly, in this holy place\x01",
            "Let's say the purpose is to be fulfilled.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00007FLet's do it … …!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0x109, 0x25)
    SetChrSubChip(0x109, 0x4)
    OP_0D()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x109,
        "#6P#10107FRaise your hand and throw it down!\x02",
    )

    CloseMessageWindow()
    OP_68(-340, 1200, 26670, 1500)
    OP_6F(0x79)
    Sound(832, 2, 70, 0)
    Sound(934, 0, 50, 0)
    Sound(829, 0, 50, 0)
    PlayEffect(0x2, 0x1, 0x8, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetCameraDistance(16000, 30000)
    SetMessageWindowPos(14, 280, -1, 3)

    AnonymousTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Whew ……\x01",
            "It seems that the situation is not known.\x02\x03",
            "Even so, the appearance of Ellie\x01",
            "I thought why I could not see it … …\x02\x03",
            "Indeed, temporarily leaving the support department\x01",
            "Are you helping Mr. MacDael?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#6P#00010FCut …!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10101Fま だ か\x01",
            "Lloyd's memory …! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#06613F#11PIn addition, new mayor and new chairman\x01",
            "Cooperation to create a new system · bill …\x02\x03",
            "#06610FIndeed, by doing so\x01",
            "The support department is easier to move than ever\x01",
            "Are you planning to make a political foothold?\x02\x03",
            "#06613FHun, it seems to be a proposal of the new Mayor\x01",
            "It is quite an interesting attempt.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00013F……………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#06606F#11PHowever, talented people like Ellie\x01",
            "It's not like I'll be buried like a police\x01",
            "I can only say foolishly.\x02\x03",
            "#06600FHmm, when I became mayor\x01",
            "I will let the Special Affairs Support Division be dismantled.\x02\x03",
            "And as she is my exclusive secretary\x01",
            "Have the talent demonstrated to the fullest … …\x02\x03",
            "#06604FYeah yeah, that is nice.\x01",
            "Let's do so!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_148E")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "◆ Partially Achievements Achievement of a bond with Eli\x01",      # 0
            "◆ Partial achievement Achievement of bondage with Eli\x01",      # 1
            "◆ Do not change\x01",                      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1479"),
        (1, "loc_1481"),
        (2, "loc_1489"),
        (SWITCH_DEFAULT, "loc_1489"),
    )


    label("loc_1479")

    SetScenarioFlags(0x25, 3)
    Jump("loc_148E")

    label("loc_1481")

    ClearScenarioFlags(0x25, 3)
    Jump("loc_148E")

    label("loc_1489")

    Jump("loc_148E")

    label("loc_148E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 3)), scpexpr(EXPR_END)), "loc_15D4")
    Sleep(500)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x101,
        (
            "#6P#00007F#4SDo not be silly……!\x02\x03",
            "#3S#00010FTo your foolish delusion\x01",
            "Does it involve Ellie?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10105F(Mr. Lloyd, terrible power … …)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#06603F#11PHun …\x01",
            "In the first place, like a boy like you\x01",
            "Is it balanced with Ellie?\x02\x03",
            "#06611FTo make her awake\x01",
            "Let's pick out bad buds.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_16B4")

    label("loc_15D4")


    ChrTalk(
        0x101,
        "#6P#00013Fthis guy……!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10106FIf you are seriously saying\x01",
            "It is quite a feeling ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#06613F#11PPowered by Translate\x01",
            "You have the enemy of Master Joachim.\x02\x03",
            "#06610FTo break Elie's rethink\x01",
            "Let's pick out bad buds.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_16B4")

    StopBGM(0x7D0)
    Fade(250)
    OP_68(0, 1200, 28500, 0)
    MoveCamera(0, 21, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15000, 0)
    SetCameraDistance(14000, 3000)
    Sound(540, 0, 50, 0)
    Sound(531, 0, 20, 0)
    SetChrChipByIndex(0x8, 0x26)
    SetChrSubChip(0x8, 0x0)
    Sleep(500)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7451", 0)
    OP_82(0x32, 0x32, 0xBB8, 0xDAC)
    OP_25(0x340, 0x64)
    Sound(357, 0, 100, 0)
    StopEffect(0x1, 0x2)
    PlayEffect(0x0, 0x0, 0x8, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 0x28)
    SetChrSubChip(0x8, 0x2)

    def lambda_1780():
        OP_A6(0xFE, 0x0, 0x1E, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1780)
    Sleep(100)
    SetChrSubChip(0x8, 0x3)
    Sleep(2000)
    BeginChrThread(0x9, 3, 0, 4)
    Sound(831, 0, 100, 0)
    SetChrChipByIndex(0xB, 0x27)
    SetChrSubChip(0xB, 0x3)
    SetChrFlags(0xB, 0x800)
    OP_52(0xB, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xB, 0x80)

    def lambda_17E2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x5DC)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_17E2)

    def lambda_17F3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_17F3)
    Sleep(500)
    Sound(817, 0, 100, 0)
    Sleep(500)
    StopEffect(0x0, 0x2)
    Sound(202, 0, 100, 0)
    StopSound(832, 1000, 100)
    PlayEffect(0x1, 0xFF, 0xB, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_68(0, 1300, 28500, 1000)
    MoveCamera(0, 21, 10, 1000)
    SetCameraDistance(17000, 1000)
    OP_82(0x12C, 0x12C, 0xBB8, 0x5DC)
    SetChrSubChip(0xB, 0x4)
    Sleep(150)
    SetChrSubChip(0xB, 0x5)
    WaitChrThread(0x8, 2)
    WaitChrThread(0xB, 2)
    SetChrFlags(0x8, 0x80)
    Sleep(500)
    CancelBlur(500)
    Sleep(500)
    OP_6F(0x79)
    EndChrThread(0x8, 0xFF)
    ClearChrFlags(0xB, 0x800)
    Fade(250)
    SetChrChipByIndex(0xB, 0x24)
    SetChrSubChip(0xB, 0x0)
    OP_52(0xB, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xB, 3, 0, 2)
    OP_0D()
    OP_68(330, 1300, 26300, 1500)
    MoveCamera(36, 13, 0, 1500)
    OP_6E(600, 1500)
    SetCameraDistance(18000, 1500)
    OP_6F(0x79)
    WaitChrThread(0x9, 3)

    ChrTalk(
        0x9,
        "#6P#02705FHui Daii! …! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10110FHere, this …!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00010FOh, due to the red gnostic\x01",
            "Demonicization#6RDemonize#It is!\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(60, 80, -1, -1)
    Sleep(300)

    AnonymousTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "In this holy place,\x01",
            "Always awakening always#4RSolely#Comfortable ……\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Before realizing great hope\x01",
            "Small offerings ……\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "At best he scratches, struggling,\x01",
            "I will have you strike!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x101,
        "#6P#00007FIs that so …!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10107FOne target, we will start suppressing!\x02",
    )

    CloseMessageWindow()
    EndChrThread(0xB, 0x3)
    BlurSwitch(0x190, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetCameraDistance(16000, 400)
    SetChrChipByIndex(0xB, 0x27)
    SetChrSubChip(0xB, 0x6)
    OP_52(0xB, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChip(0x0, 0xB, 0x32, 0xC8)
    Sound(251, 0, 100, 0)

    def lambda_1B60():
        OP_9D(0xFE, 0x0, 0xC8, 0x53FC, 0x384, 0x5DC)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1B60)
    Sleep(250)
    SetChrSubChip(0xB, 0x7)
    Sleep(150)
    EndChrThread(0xB, 0x1)
    SetScenarioFlags(0x0, 0)
    Battle("BattleInfo_2DC", 0x0, 0x0, 0x100, 0x27, 0xFF)
    FadeToDark(0, 0, -1)
    OP_CC(0x1, 0xFF, 0x0)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0xB, 0x80)
    Call(0, 6)
    Return()

    # Function_3_493 end

    def Function_4_1BB5(): pass

    label("Function_4_1BB5")

    OP_63(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_93(0x9, 0x87, 0x1F4)
    Sleep(500)

    def lambda_1BD6():
        OP_96(0xFE, 0xFFFFF31C, 0xC8, 0x79E0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1BD6)
    WaitChrThread(0x9, 1)
    Return()

    # Function_4_1BB5 end

    def Function_5_1BF0(): pass

    label("Function_5_1BF0")

    Sleep(2500)
    Sound(805, 0, 100, 0)
    Sleep(100)
    Sound(531, 0, 100, 0)
    Return()

    # Function_5_1BF0 end

    def Function_6_1C03(): pass

    label("Function_6_1C03")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    AddParty(0x9, 0xFF, 0xFF)
    AddParty(0x7, 0xFF, 0xFF)
    OP_32(0x9, 0xFF, 0x0)
    OP_32(0x7, 0xFF, 0x0)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00051.itc", 0x1F)
    LoadChrToIndex("chr/ch02950.itc", 0x20)
    LoadChrToIndex("chr/ch02951.itc", 0x21)
    LoadChrToIndex("chr/ch00950.itc", 0x22)
    LoadChrToIndex("chr/ch00951.itc", 0x23)
    LoadChrToIndex("chr/ch02450.itc", 0x24)
    LoadChrToIndex("chr/ch02451.itc", 0x25)
    LoadChrToIndex("chr/ch06500.itc", 0x26)
    LoadChrToIndex("monster/ch67450.itc", 0x27)
    LoadChrToIndex("chr/ch00056.itc", 0x28)
    LoadChrToIndex("chr/ch02953.itc", 0x29)
    LoadChrToIndex("chr/ch00952.itc", 0x2A)
    LoadChrToIndex("chr/ch02452.itc", 0x2B)
    LoadChrToIndex("monster/ch67453.itc", 0x2C)
    LoadChrToIndex("monster/ch67456.itc", 0x2D)
    LoadChrToIndex("monster/ch67457.itc", 0x2E)
    LoadChrToIndex("apl/ch51022.itc", 0x2F)
    LoadChrToIndex("chr/ch0295F.itc", 0x30)
    LoadEffect(0x0, "event\\ev602_01.eff")
    LoadEffect(0x1, "event\\ev10020.eff")
    LoadEffect(0x2, "event\\ev10022.eff")
    LoadEffect(0x3, "battle\\cr313000.eff")
    LoadEffect(0x4, "event\\ev10018.eff")
    LoadEffect(0x5, "event/ev17034.eff")
    LoadEffect(0x6, "battle\\ms00001.eff")
    LoadEffect(0x7, "event/eva01_01.eff")
    LoadEffect(0x8, "event/ev10023.eff")
    LoadEffect(0x9, "event/eva04_00.eff")
    SoundLoad(832)
    SoundLoad(825)
    SoundLoad(889)
    OP_68(50, 1400, 25050, 0)
    MoveCamera(27, 12, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15500, 0)
    SetChrPos(0x101, -600, 200, 22600, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrPos(0x109, 800, 200, 21900, 0)
    SetChrChipByIndex(0x109, 0x20)
    SetChrSubChip(0x109, 0x0)
    SetChrPos(0x10A, 0, -1400, -33000, 0)
    SetChrChipByIndex(0x10A, 0x22)
    SetChrSubChip(0x10A, 0x0)
    SetChrPos(0x108, 0, -1400, -34000, 0)
    SetChrChipByIndex(0x108, 0x24)
    SetChrSubChip(0x108, 0x0)
    SetChrChipByIndex(0x9, 0x26)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, -3300, 200, 31200, 135)
    SetChrChipByIndex(0xB, 0x2C)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, 0, 200, 29500, 180)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_52(0xB, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapObjFlags(0x0, 0x1000)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x1000)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFrame(0xFF, "bl_ato00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "bl_ato01", 0x0, 0x1)
    PlayEffect(0x0, 0x0, 0xB, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(832, 2, 100, 0)
    OP_68(50, 1400, 25050, 30000)
    MoveCamera(38, 11, 0, 30000)
    OP_6E(600, 30000)
    SetCameraDistance(15500, 30000)
    FadeToBright(1000, 0)
    OP_0D()
    SetMessageWindowPos(60, 80, -1, -1)
    Sleep(300)

    AnonymousTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#5P#N#15AKukuku\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    Fade(100)
    SetChrSubChip(0xB, 0x1)
    OP_0D()
    Sleep(500)
    OP_82(0xC8, 0xC8, 0xBB8, 0x2BC)
    SetMessageWindowPos(60, 80, -1, -1)

    AnonymousTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#5P#N#5S#20AHa ha ha ha ha ha!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(300)

    ChrTalk(
        0x101,
        "#6P#00010FCut, this is …!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10110FIt does not work at all …! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#6P#02705FHie, huh …!\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    BeginChrThread(0x9, 3, 0, 7)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x9,
        "#10A#5P#4S#10AWow ah ah ah ……!\x02",
    )

    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(0, 1000, 14000, 0)
    MoveCamera(131, 22, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16000, 0)
    SetChrChipByIndex(0xB, 0x27)
    SetChrSubChip(0xB, 0x0)
    OP_52(0xB, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(3000)
    OP_68(0, 1400, 26500, 2000)
    OP_6F(0x79)
    SetMessageWindowPos(40, 130, -1, -1)

    AnonymousTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#5P#NAw……\x01",
            "Selfish exit is not a problem.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#5P#NYou were on your own\x01",
            "Because it is not an autonomous state legislature.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    Sound(802, 0, 100, 0)
    SetCameraDistance(15500, 800)
    SetChrChipByIndex(0xB, 0x2D)
    SetChrSubChip(0xB, 0x0)
    OP_52(0xB, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_0D()
    SetChrPos(0xA, 0, -1400, -3000, 0)
    Sound(258, 0, 100, 0)
    PlayEffect(0x2, 0x2, 0xB, 0x5, 0, 2000, 1500, 0, 0, 0, 1000, 1000, 1000, 0xA, 0, 0, 0, 0)
    Sleep(1000)
    Sound(321, 0, 100, 0)
    OP_68(0, -400, -5000, 2000)
    MoveCamera(143, 29, 0, 2000)
    SetCameraDistance(17000, 2000)
    WaitChrThread(0x9, 3)
    OP_90(0x9, 0, 200, 2500, 180)

    def lambda_22A8():
        OP_95(0xFE, 0, -1400, -5000, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_22A8)
    WaitChrThread(0x9, 1)
    OP_64(0x9)
    OP_52(0x9, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x9, 0x2F)
    SetChrSubChip(0x9, 0x0)
    OP_82(0xC8, 0xC8, 0xBB8, 0x3E8)
    Sound(204, 0, 100, 0)
    Sound(833, 0, 100, 0)

    def lambda_22F9():
        OP_A6(0xFE, 0x32, 0x32, 0xBB8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_22F9)

    def lambda_2312():
        OP_9D(0xFE, 0x514, 0xFFFFFA88, 0xFFFFE4A8, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2312)

    ChrTalk(
        0x9,
        "#4S#11P#12AGogaka …!\x02",
    )

    WaitChrThread(0x9, 1)
    Sound(514, 0, 100, 0)
    SetChrSubChip(0x9, 0x1)
    Sleep(2000)
    Fade(500)
    OP_68(50, 1400, 25050, 0)
    MoveCamera(27, 12, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15500, 0)

    def lambda_2391():
        OP_93(0x101, 0xB4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2391)
    Sleep(0)

    def lambda_23A1():
        OP_93(0x109, 0xB4, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_23A1)
    Sleep(0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x109, 0)
    OP_0D()

    ChrTalk(
        0x109,
        "#5P#10107FAhh ……! Is it?\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x0, 0x1F4)

    ChrTalk(
        0x101,
        "#6P#00010FErnest、貴様……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    Sound(802, 0, 50, 0)
    SetChrChipByIndex(0xB, 0x27)
    SetChrSubChip(0xB, 0x0)
    OP_52(0xB, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_0D()

    def lambda_245E():
        OP_93(0xFE, 0x0, 0x2BC)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_245E)
    SetMessageWindowPos(60, 80, -1, -1)

    AnonymousTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#5P#NHuff, I still have value for use\x01",
            "I just fainted lightly.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#5P#NMore than that, I will tell you about other people\x01",
            "Is there room to worry about?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    BeginChrThread(0x101, 3, 0, 12)
    BeginChrThread(0x11, 1, 0, 18)
    Sound(195, 0, 100, 0)
    Sound(212, 0, 100, 0)
    PlayEffect(0x1, 0x0, 0xB, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    ChrTalk(
        0x101,
        "#6P#00010FCut …!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10107FTh-This is……\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(60, 80, -1, -1)

    AnonymousTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#5P#NKuku, all the cult's lodge\x01",
            "It is made just above the seven anger … …\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#5P#NBy waking up just above that\x01",
            "The door leading to \"D\"\x01",
            "It will be possible to open …\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#5P#NHuhaha, you heard from the teacher!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    StopBGM(0x7D0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7454", 0)
    SetScenarioFlags(0x0, 1)
    EndChrThread(0x101, 0x3)
    OP_82(0x32, 0x32, 0xBB8, 0x157C)
    Fade(500)
    OP_68(0, 1700, 29500, 0)
    MoveCamera(0, 27, 0, 0)
    OP_6E(750, 0)
    SetCameraDistance(14500, 0)
    MoveCamera(0, 27, -25, 7000)
    SetCameraDistance(11500, 7000)
    SetChrFlags(0xB, 0x2)
    SetChrFlags(0xB, 0x10)
    SetChrChipByIndex(0xB, 0x2E)
    SetChrSubChip(0xB, 0x0)
    OP_52(0xB, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(620)
    SetChrSubChip(0xB, 0x1)
    Sleep(120)
    SetChrSubChip(0xB, 0x5)
    Sleep(120)
    SetChrSubChip(0xB, 0x6)
    Sleep(120)
    SetChrSubChip(0xB, 0x7)
    Sleep(120)
    SetChrSubChip(0xB, 0xA)
    Sound(308, 0, 50, 0)
    Sound(531, 0, 50, 0)
    Sound(540, 0, 50, 0)
    Sleep(1400)
    Sound(534, 0, 60, 0)
    SetChrSubChip(0xB, 0xB)
    Sleep(100)
    SetChrSubChip(0xB, 0xC)
    Sleep(100)
    SetChrSubChip(0xB, 0xD)
    Sleep(100)
    SetChrSubChip(0xB, 0xE)
    Sleep(2500)
    Sound(532, 0, 100, 0)
    Sleep(200)
    Sound(288, 0, 100, 0)
    Sound(308, 0, 100, 0)
    Sound(833, 0, 50, 0)
    Sound(889, 0, 100, 0)
    SetChrSubChip(0xB, 0x16)
    BeginChrThread(0xB, 3, 0, 13)
    OP_82(0x12C, 0x12C, 0xBB8, 0x5DC)
    StopSound(832, 2000, 90)
    StopSound(825, 2000, 90)
    FadeToDark(1500, 16777215, -1)
    OP_0D()
    Sound(817, 0, 100, 0)
    StopEffect(0x0, 0x2)
    SetMapObjFrame(0xFF, "hasiraR", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hasiraL", 0x0, 0x1)
    SetMapObjFrame(0xFF, "bl_mae00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "bl_mae01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "bl_mae02", 0x0, 0x1)
    SetMapObjFrame(0xFF, "bl_ato00", 0x1, 0x1)
    SetMapObjFrame(0xFF, "bl_ato01", 0x1, 0x1)
    ClearMapObjFlags(0x0, 0x4)
    SetChrChipByIndex(0xB, 0x27)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x2)
    ClearChrFlags(0xB, 0x10)
    SetChrFlags(0xB, 0x8)
    OP_78(0x0, 0xB)
    OP_49()
    SetChrPos(0xB, 0, 0, 33000, 180)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_D5(0xB, 0x0, 0x41EB0, 0x0, 0x0)
    OP_74(0x0, 0x1E)
    OP_70(0x0, 0x334)
    SetChrPos(0x101, -700, 200, 25200, 0)
    SetChrFlags(0x101, 0x8)
    SetChrPos(0x109, 700, 200, 24500, 0)
    SetChrFlags(0x109, 0x8)
    Sound(829, 0, 100, 0)
    Sleep(1000)
    StopSound(889, 2000, 100)
    OP_68(0, 4000, 32000, 0)
    MoveCamera(0, 25, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(8500, 0)
    PlayEffect(0x1, 0x0, 0xB, 0x0, 0, 0, 0, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    OP_68(0, 1500, 32000, 5000)
    FadeToBright(2000, 16777215)
    Sleep(500)
    StopEffect(0x0, 0x2)
    OP_6F(0x79)
    Fade(500)
    OP_68(0, 2800, 32000, 0)
    MoveCamera(330, -20, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(8500, 0)
    OP_68(0, 3000, 32000, 6000)
    MoveCamera(30, -13, 0, 6000)
    SetCameraDistance(11500, 6000)
    BlurSwitch(0xBB8, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    Sound(1005, 0, 100, 0)
    Sound(889, 0, 50, 0)
    OP_74(0x0, 0x14)
    OP_71(0x0, 0x334, 0x38E, 0x0, 0x0)
    OP_79(0x0)
    OP_74(0x0, 0xA)
    OP_71(0x0, 0x38F, 0x3B6, 0x0, 0x20)
    OP_6F(0x79)
    Sleep(500)
    Fade(250)
    Sound(833, 0, 100, 0)
    OP_68(0, 4500, 33500, 0)
    MoveCamera(0, 45, 0, 0)
    OP_6E(900, 0)
    SetCameraDistance(7500, 0)
    OP_68(0, 3000, 33500, 1500)
    MoveCamera(0, 50, 0, 1500)
    SetCameraDistance(12500, 1500)
    OP_6F(0x79)
    Sleep(500)

    ChrTalk(
        0x109,
        "#N#10105FSounds like that … ….\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#N#00010FDamn\x01",
            "It is the same as Joachim at that time!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    CancelBlur(0)
    OP_68(0, 1700, 29200, 0)
    MoveCamera(33, 9, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(14000, 0)
    ClearChrFlags(0x101, 0x8)
    ClearChrFlags(0x109, 0x8)
    MoveCamera(33, 9, 5, 20000)
    SetCameraDistance(15500, 20000)
    OP_74(0x0, 0xF)
    OP_71(0x0, 0x3B7, 0x3C0, 0x0, 0x0)
    OP_79(0x0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x1E1, 0x208, 0x0, 0x20)
    Sleep(500)
    FadeToDark(300, 0, 100)
    OP_0D()
    Sound(1005, 0, 100, 0)
    OP_C9(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xB),
            "#60WKuku …… Corsoziano teaching point ……\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xB),
            "#60WCollect total Teno truth Hai Nomononi ……\x02",
        )
    )

    CloseMessageWindow()
    OP_74(0x0, 0xF)
    OP_71(0x0, 0x28B, 0x294, 0x0, 0x0)
    OP_79(0x0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x294, 0x2BC, 0x0, 0x20)

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xB),
            "#60W… ……………? ………………\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xB),
            "#60W………… Nazeda …………\x01",
            "…… Naze What am I looking at …?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    OP_0D()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x800)

    ChrTalk(
        0x101,
        "#00005F#12P……?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10101F#12PSomething is strange … …\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()
    Sound(1005, 0, 100, 0)
    OP_C9(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xB),
            "#60W… …. Nazeda ……!\x01",
            "Naze \"D\" Gaze Enai ……! Is it?\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xB),
            "#60WTrue Naru nobu ga Gora\x01",
            "Douchet feeling jirarena nada Na! Is it?\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xB),
            "#60WCoredeja story ghost udhanaika! It is!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    OP_0D()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x800)
    OP_95(0x101, -700, 200, 26200, 4000, 0x0)
    Sound(30, 0, 100, 0)

    ChrTalk(
        0x101,
        (
            "#12P#00010FCool … … firmly!\x02\x03",
            "#00007FJoachim tells the truth\x01",
            "It will not be limited! Is it?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()
    Sound(1005, 0, 100, 0)
    OP_C9(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_82(0xC8, 0x0, 0xBB8, 0x3E8)

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xB),
            "#60W#4SDa, damaire!\x01",
            "Damare Damare Damareyeet!\x02",
        )
    )

    CloseMessageWindow()
    OP_74(0x0, 0xF)
    OP_71(0x0, 0x2BC, 0x2C6, 0x0, 0x0)
    OP_79(0x0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x1E1, 0x208, 0x0, 0x20)

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xB),
            "#60WMariai …… Masuha starting hook\x01",
            "You sir La Touche cerebre ……\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xB),
            "#60WSono de Kurobetsuru return letter,\x01",
            "Otoko Eri Robotte Kureruwa!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    OP_0D()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x800)

    ChrTalk(
        0x101,
        "#12P#00010FHere, this …!\x02",
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x109,
        "#10107FMr. Lloyd is dangerous!\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x101, 3, 0, 14)
    Sleep(1000)
    Sound(834, 0, 100, 0)
    OP_68(0, 10000, 27900, 0)
    MoveCamera(330, 50, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(14500, 0)
    OP_68(0, 1000, 27900, 650)
    MoveCamera(0, 35, 0, 650)
    BeginChrThread(0xB, 3, 0, 8)
    OP_6F(0x79)
    Sound(833, 0, 100, 0)
    Sound(288, 0, 100, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 0, 200, 28000, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0xFF, 0xFF, 0x0, 0, 200, 28000, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x8, 0x7, 0xFF, 0x0, 0, 200, 28000, 0, 0, 0, 400, 400, 400, 0xFF, 0, 0, 0, 0)
    OP_82(0x0, 0x1F4, 0xBB8, 0x5DC)
    BeginChrThread(0x109, 3, 0, 15)
    SetCameraDistance(19500, 1500)
    WaitChrThread(0x109, 3)
    WaitChrThread(0x101, 3)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#00010FCut …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10110FWhat a god … …\x02",
    )

    CloseMessageWindow()
    OP_68(0, 2600, 29000, 3000)
    MoveCamera(0, -3, 0, 3000)
    SetCameraDistance(14000, 3000)
    Sound(892, 0, 100, 0)
    OP_74(0x0, 0xA)
    OP_71(0x0, 0x259, 0x280, 0x0, 0x0)
    Sleep(800)
    PlayEffect(0x9, 0xFF, 0xFF, 0x0, 500, 0, 28000, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x9, 0xFF, 0xFF, 0x0, -500, 0, 28000, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x9, 0xFF, 0xFF, 0x0, 500, 0, 28000, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x9, 0xFF, 0xFF, 0x0, -500, 0, 28000, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x9, 0xFF, 0xFF, 0x0, 500, 0, 28000, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x9, 0xFF, 0xFF, 0x0, -500, 0, 28000, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x9, 0xFF, 0xFF, 0x0, 500, 0, 28000, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x9, 0xFF, 0xFF, 0x0, -500, 0, 28000, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x9, 0xFF, 0xFF, 0x0, 500, 0, 28000, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x9, 0xFF, 0xFF, 0x0, -500, 0, 28000, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    Sleep(400)
    Sound(288, 0, 70, 0)
    Sound(210, 0, 40, 0)
    OP_79(0x0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0xA, 0x32, 0x0, 0x20)
    OP_6F(0x79)
    SetCameraDistance(15500, 10000)
    FadeToDark(300, 0, 100)
    OP_0D()
    Sound(1005, 0, 100, 0)
    OP_C9(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xB),
            "#60WKukku, Soredehasarabada …\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xB),
            "#60WDwarf null selflessness\x01",
            "Dusty ugly!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    OP_0D()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x800)
    Sound(892, 0, 100, 0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_71(0x0, 0x411, 0x438, 0x0, 0x0)
    OP_79(0x0)
    Sound(833, 0, 100, 0)
    Sound(892, 0, 100, 0)
    OP_74(0x0, 0xA)
    OP_71(0x0, 0x438, 0x441, 0x0, 0x0)
    Sleep(200)
    Sound(893, 0, 100, 0)
    OP_79(0x0)
    OP_68(0, 700, 16000, 0)
    MoveCamera(315, 25, -5, 0)
    OP_6E(700, 0)
    SetCameraDistance(15000, 0)
    CancelBlur(0)
    BeginChrThread(0xB, 3, 0, 11)
    OP_68(0, 1100, 18500, 1600)
    MoveCamera(323, 15, -5, 1600)
    SetCameraDistance(13500, 1600)
    BeginChrThread(0x108, 3, 0, 16)
    OP_6F(0x79)
    OP_68(1000, 1100, 27000, 0)
    MoveCamera(300, 13, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(16000, 0)
    OP_68(1000, 2100, 27000, 1000)
    MoveCamera(313, 5, 0, 1000)
    SetCameraDistance(13000, 1000)
    OP_0D()
    Sound(3997, 255, 100, 0)

    ChrTalk(
        0x108,
        "#4S#8A#6PHa ha ha!\x02",
    )

    Sleep(600)
    OP_57(0x0)
    OP_5A()
    WaitChrThread(0x108, 3)
    SetMessageWindowPos(300, 70, -1, -1)

    AnonymousTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xB),
            "#4SNa\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    WaitChrThread(0xB, 3)
    Sound(2514, 255, 100, 0)
    Sleep(300)
    OP_68(0, 3100, 32000, 1500)
    MoveCamera(327, -1, 0, 1500)
    SetCameraDistance(13500, 1500)
    Sleep(300)
    BeginChrThread(0x10A, 3, 0, 17)
    Sleep(300)
    Sound(1005, 0, 100, 0)
    SetMessageWindowPos(-1, 120, -1, -1)

    AnonymousTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xB),
            "#4S#15AGoo … oh! Is it?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    WaitChrThread(0x10A, 3)
    Fade(500)
    OP_68(0, 2100, 27400, 0)
    MoveCamera(323, 9, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(17500, 0)
    SetCameraDistance(16500, 2000)
    BeginChrThread(0xB, 3, 0, 9)
    SetChrPos(0x101, -700, 200, 23000, 0)
    SetChrPos(0x109, 700, 200, 22500, 0)
    SetChrPos(0x108, -300, 200, 26700, 0)
    SetChrPos(0x10A, 2100, 200, 16400, 0)

    def lambda_367E():
        OP_95(0xFE, 2100, 200, 23400, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_367E)
    OP_0D()
    SetChrChipByIndex(0x108, 0x25)
    SetChrSubChip(0x108, 0x1)
    Sound(809, 0, 50, 0)

    def lambda_36A7():
        OP_9D(0xFE, 0xFFFFFED4, 0xC8, 0x607C, 0x1F4, 0xFA0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_36A7)
    WaitChrThread(0x108, 1)
    Sound(540, 0, 50, 0)
    SetChrChipByIndex(0x108, 0x2B)
    SetChrSubChip(0x108, 0x1)
    WaitChrThread(0x10A, 1)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0x10A, 0x2A)
    SetChrSubChip(0x10A, 0x0)

    ChrTalk(
        0x109,
        "#5P#10102FAh……!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002FMr. Dudley, Arios!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    OP_68(0, 1300, 24700, 0)
    MoveCamera(230, 23, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(14000, 0)
    OP_0D()

    ChrTalk(
        0x10A,
        (
            "#6P#00604FWhew ……\x01",
            "Have you managed to make it in time?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#01402FLloyd, Noel chief.\x01",
            "It endured well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#5PTwo people are the one\x01",
            "Well well … OK!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#6P#00606FHun, as expected 10 body\x01",
            "I wish you were drunk.\x02\x03",
            "#00601FThe story is back!\x01",
            "First of all, I will neutralize the guy!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#01407FIt is not an ordinary opponent!\x01",
            "We will hit our best!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_38A5():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_38A5)

    def lambda_38BE():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_38BE)
    Sleep(150)
    Fade(250)
    Sound(802, 0, 100, 0)
    Sound(805, 0, 100, 0)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x109, 0x20)
    SetChrSubChip(0x109, 0x0)
    OP_0D()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x101,
        "#00007F#5P#4SYes!\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x109,
        "#10107F#5P#4SYes, sir!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BlurSwitch(0x3E8, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_68(0, 2100, 27400, 2000)
    MoveCamera(323, 9, 0, 2000)
    SetCameraDistance(16500, 2000)
    OP_6F(0x79)
    Sound(892, 0, 100, 0)
    OP_71(0x0, 0x410, 0x438, 0x0, 0x0)
    OP_79(0x0)
    MoveCamera(323, 9, -10, 500)
    SetCameraDistance(14500, 500)
    Sound(893, 0, 100, 0)
    Sound(833, 0, 60, 0)
    OP_74(0x0, 0x14)
    OP_71(0x0, 0x438, 0x442, 0x0, 0x0)
    OP_79(0x0)
    SetScenarioFlags(0x0, 0)
    Battle("BattleInfo_320", 0x30200011, 0x0, 0x100, 0x23, 0xFF)
    FadeToDark(0, 0, -1)
    SetChrFlags(0xB, 0x80)
    StopEffect(0x7, 0x0)
    Call(0, 19)
    Return()

    # Function_6_1C03 end

    def Function_7_3A06(): pass

    label("Function_7_3A06")

    ClearChrFlags(0x9, 0x4)

    def lambda_3A10():
        OP_95(0xFE, -3300, 200, 18500, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3A10)
    WaitChrThread(0x9, 1)

    def lambda_3A2E():
        OP_95(0xFE, 0, 200, 13500, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3A2E)
    WaitChrThread(0x9, 1)

    def lambda_3A4C():
        OP_95(0xFE, 0, -1400, -5500, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3A4C)
    WaitChrThread(0x9, 1)
    Return()

    # Function_7_3A06 end

    def Function_8_3A66(): pass

    label("Function_8_3A66")

    OP_74(0x0, 0xA)
    OP_71(0x0, 0x209, 0x230, 0x0, 0x0)
    OP_79(0x0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x231, 0x258, 0x0, 0x20)
    Return()

    # Function_8_3A66 end

    def Function_9_3A8A(): pass

    label("Function_9_3A8A")

    OP_74(0x0, 0x14)
    OP_71(0x0, 0x4BA, 0x4CE, 0x0, 0x0)
    OP_79(0x0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0xA, 0x31, 0x0, 0x20)
    Return()

    # Function_9_3A8A end

    def Function_10_3AAE(): pass

    label("Function_10_3AAE")

    Sound(831, 0, 100, 0)
    OP_70(0x0, 0x44D)
    OP_71(0x0, 0x44D, 0x460, 0x0, 0x0)
    OP_79(0x0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x460, 0x488, 0x0, 0x20)
    Return()

    # Function_10_3AAE end

    def Function_11_3AD8(): pass

    label("Function_11_3AD8")

    OP_70(0x0, 0x438)
    OP_74(0x0, 0xA)
    ClearMapObjFlags(0x0, 0x20)
    OP_71(0x0, 0x42A, 0x441, 0x0, 0x0)
    OP_79(0x0)
    OP_70(0x0, 0x441)
    Return()

    # Function_11_3AD8 end

    def Function_12_3AFA(): pass

    label("Function_12_3AFA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3B1E")
    OP_82(0x32, 0x32, 0xBB8, 0x2710)
    Sleep(10000)
    Jump("Function_12_3AFA")

    label("loc_3B1E")

    Return()

    # Function_12_3AFA end

    def Function_13_3B1F(): pass

    label("Function_13_3B1F")

    OP_52(0xB, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x4CE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x4CE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x4CE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_52(0xB, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x4EC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x4EC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x4EC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_52(0xB, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x50A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x50A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x50A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_52(0xB, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x528), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x528), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x528), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_52(0xB, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x546), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x546), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x546), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_52(0xB, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x564), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x564), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x564), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_52(0xB, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x582), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x582), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x582), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_52(0xB, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x5A0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x5A0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x5A0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_52(0xB, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x5BE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x5BE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x5BE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_52(0xB, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_52(0xB, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x5FA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x5FA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x5FA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_52(0xB, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x618), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x618), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x618), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_52(0xB, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x636), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x636), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x636), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_52(0xB, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x654), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x654), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x654), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_13_3B1F end

    def Function_14_3D15(): pass

    label("Function_14_3D15")

    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(700)
    SetChrChipByIndex(0x101, 0x28)
    SetChrSubChip(0x101, 0x2)
    Sound(809, 0, 80, 0)

    def lambda_3D43():
        OP_9D(0xFE, 0xFFFFFD44, 0xC8, 0x5DC0, 0x190, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3D43)
    WaitChrThread(0x101, 1)
    Sound(326, 0, 40, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    Sleep(700)
    SetChrChipByIndex(0x101, 0x28)
    SetChrSubChip(0x101, 0x0)

    def lambda_3D7D():
        OP_A6(0xFE, 0x32, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3D7D)
    Return()

    # Function_14_3D15 end

    def Function_15_3D92(): pass

    label("Function_15_3D92")

    SetChrChipByIndex(0x109, 0x29)
    SetChrSubChip(0x109, 0x0)
    SetChrFlags(0x109, 0x20)
    SetChrFlags(0x109, 0x1000)

    def lambda_3DA9():
        OP_96(0xFE, 0x2BC, 0xC8, 0x5BCC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3DA9)

    def lambda_3DC3():
        OP_A6(0xFE, 0x32, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_3DC3)
    WaitChrThread(0x109, 1)
    ClearChrFlags(0x109, 0x20)
    ClearChrFlags(0x109, 0x1000)
    SetChrChipByIndex(0x109, 0x30)
    SetChrSubChip(0x109, 0x0)
    Return()

    # Function_15_3D92 end

    def Function_16_3DEE(): pass

    label("Function_16_3DEE")

    SetChrPos(0x108, 0, 200, 8000, 0)
    SetChrFlags(0x108, 0x1000)
    SetChrChipByIndex(0x108, 0x25)
    SetChrSubChip(0x108, 0x0)
    SetChrChip(0x0, 0x108, 0x32, 0x12C)
    Sound(250, 0, 100, 0)

    def lambda_3E1F():
        OP_95(0xFE, 0, 200, 19500, 10000, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_3E1F)
    WaitChrThread(0x108, 1)
    Sound(251, 0, 100, 0)

    def lambda_3E43():
        OP_9D(0xFE, 0xFA0, 0xC8, 0x6338, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_3E43)
    WaitChrThread(0x108, 1)
    Sound(326, 0, 100, 0)
    SetChrChipByIndex(0x108, 0x2B)
    SetChrSubChip(0x108, 0x2)
    Sound(844, 0, 100, 0)

    def lambda_3E78():
        OP_9D(0xFE, 0xFFFFFE0C, 0xC8, 0x68B0, 0x7D0, 0xFA0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_3E78)
    Sleep(300)
    Sound(534, 0, 100, 0)
    Sound(540, 0, 100, 0)
    Sleep(200)
    Sound(288, 0, 100, 0)
    Sound(859, 0, 100, 0)
    Sound(196, 0, 100, 0)
    PlayEffect(0x6, 0xFF, 0x108, 0x0, 0, 1000, 1200, 0, 0, 0, 1100, 1100, 1100, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0xFF, 0x108, 0x0, 0, 1000, 1200, 0, 0, 0, 1100, 1100, 1100, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0x108, 0x3)
    OP_82(0x12C, 0x12C, 0xBB8, 0x1F4)
    BeginChrThread(0xB, 3, 0, 10)
    WaitChrThread(0x108, 1)
    Sound(326, 0, 100, 0)
    ClearChrFlags(0x108, 0x1000)
    SetChrChip(0x1, 0x108, 0x0, 0x0)
    Return()

    # Function_16_3DEE end

    def Function_17_3F55(): pass

    label("Function_17_3F55")

    Sound(567, 0, 100, 0)
    PlayEffect(0x5, 0xFF, 0xFF, 0x0, -2000, 3500, 18000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    Sound(196, 0, 70, 0)
    PlayEffect(0x6, 0xFF, 0xFF, 0x0, -2000, 3500, 32000, 0, 0, 0, 1100, 1100, 1100, 0xFF, 0, 0, 0, 0)
    OP_71(0x0, 0x489, 0x4BA, 0x0, 0x0)
    OP_82(0x12C, 0x12C, 0xBB8, 0xC8)
    Sleep(300)
    Sound(567, 0, 100, 0)
    PlayEffect(0x5, 0xFF, 0xFF, 0x0, 2000, 3000, 18000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    Sound(196, 0, 70, 0)
    PlayEffect(0x6, 0xFF, 0xFF, 0x0, 2000, 3000, 32000, 0, 0, 0, 1100, 1100, 1100, 0xFF, 0, 0, 0, 0)
    OP_82(0x12C, 0x12C, 0xBB8, 0xC8)
    Sleep(300)
    Sound(567, 0, 100, 0)
    PlayEffect(0x5, 0xFF, 0xFF, 0x0, 0, 1500, 17500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    Sound(196, 0, 70, 0)
    PlayEffect(0x6, 0xFF, 0xFF, 0x0, 0, 1500, 31500, 0, 0, 0, 1100, 1100, 1100, 0xFF, 0, 0, 0, 0)
    OP_82(0x12C, 0x12C, 0xBB8, 0xC8)
    Sleep(300)
    Sound(567, 0, 100, 0)
    PlayEffect(0x5, 0xFF, 0xFF, 0x0, 0, 4000, 18500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    Sound(196, 0, 70, 0)
    Sound(353, 0, 100, 0)
    PlayEffect(0x6, 0xFF, 0xFF, 0x0, 0, 4000, 32500, 0, 0, 0, 1100, 1100, 1100, 0xFF, 0, 0, 0, 0)
    OP_82(0x12C, 0x12C, 0xBB8, 0xC8)
    Return()

    # Function_17_3F55 end

    def Function_18_41A9(): pass

    label("Function_18_41A9")

    Sound(825, 2, 0, 0)
    Sleep(200)
    OP_25(0x339, 0xA)
    Sleep(200)
    OP_25(0x339, 0x14)
    Sleep(200)
    OP_25(0x339, 0x1E)
    Sleep(200)
    OP_25(0x339, 0x28)
    Sleep(200)
    OP_25(0x339, 0x32)
    Sleep(200)
    OP_25(0x339, 0x3C)
    Sleep(200)
    OP_25(0x339, 0x46)
    Sleep(200)
    OP_25(0x339, 0x50)
    Sleep(200)
    OP_25(0x339, 0x5A)
    Sleep(200)
    OP_25(0x339, 0x64)
    Return()

    # Function_18_41A9 end

    def Function_19_41F6(): pass

    label("Function_19_41F6")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_32(0xFF, 0xFE, 0x0)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00051.itc", 0x1F)
    LoadChrToIndex("chr/ch02950.itc", 0x20)
    LoadChrToIndex("chr/ch02951.itc", 0x21)
    LoadChrToIndex("chr/ch00950.itc", 0x22)
    LoadChrToIndex("chr/ch00951.itc", 0x23)
    LoadChrToIndex("chr/ch02450.itc", 0x24)
    LoadChrToIndex("chr/ch02451.itc", 0x25)
    LoadChrToIndex("apl/ch51022.itc", 0x26)
    LoadChrToIndex("apl/ch50523.itc", 0x27)
    LoadChrToIndex("chr/ch11400.itc", 0x28)
    LoadChrToIndex("chr/ch00056.itc", 0x29)
    LoadChrToIndex("chr/ch02452.itc", 0x2A)
    LoadChrToIndex("chr/ch02456.itc", 0x2B)
    LoadChrToIndex("chr/ch02952.itc", 0x2C)
    LoadChrToIndex("chr/ch00952.itc", 0x2D)
    LoadChrToIndex("apl/ch51024.itc", 0x2E)
    LoadChrToIndex("apl/ch51025.itc", 0x2F)
    LoadChrToIndex("apl/ch51028.itc", 0x30)
    LoadChrToIndex("chr/ch0295F.itc", 0x31)
    LoadChrToIndex("apl/ch51021.itc", 0x32)
    SoundLoad(3314)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis223.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu04300.itp")
    LoadEffect(0x9, "event\\ev620_00.eff")
    LoadEffect(0x0, "event\\ev614_01.eff")
    LoadEffect(0x1, "event\\ev614_02.eff")
    LoadEffect(0x2, "battle\\cr024200.eff")
    LoadEffect(0x3, "battle\\cr024201.eff")
    LoadEffect(0x4, "battle\\cr024102.eff")
    LoadEffect(0x5, "battle\\btgun00.eff")
    LoadEffect(0x6, "battle\\ms00001.eff")
    LoadEffect(0x7, "event\\ev10032.eff")
    LoadEffect(0x8, "event\\ev10033.eff")
    SoundLoad(825)
    SoundLoad(1004)
    SetChrPos(0x101, -200, 200, 24000, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrPos(0x109, 200, 200, 22400, 0)
    SetChrChipByIndex(0x109, 0x20)
    SetChrSubChip(0x109, 0x0)
    SetChrPos(0x10A, 1600, 200, 22800, 0)
    SetChrChipByIndex(0x10A, 0x22)
    SetChrSubChip(0x10A, 0x0)
    SetChrPos(0x108, -1600, 200, 23100, 0)
    SetChrChipByIndex(0x108, 0x24)
    SetChrSubChip(0x108, 0x0)
    SetChrPos(0xD, -200, 200, 24000, 0)
    SetChrPos(0xE, 200, 200, 22400, 0)
    SetChrPos(0xF, 1600, 200, 22800, 0)
    SetChrPos(0x10, -1600, 200, 23100, 0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrChipByIndex(0x9, 0x26)
    SetChrSubChip(0x9, 0x1)
    SetChrPos(0x9, -1000, -1400, -4000, 180)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrChipByIndex(0x8, 0x27)
    SetChrSubChip(0x8, 0x0)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrPos(0x8, 0, 200, 30000, 270)
    OP_52(0x8, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xAA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x640), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x640), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_78(0x1, 0xB)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8)
    OP_49()
    SetChrPos(0xB, 0, 0, 33000, 180)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_D5(0xB, 0x0, 0x41EB0, 0x0, 0x0)
    OP_74(0x1, 0x1E)
    OP_70(0x1, 0x65)
    OP_71(0x1, 0x65, 0x78, 0x0, 0x20)
    SetChrFlags(0xC, 0x8000)
    ClearChrFlags(0xC, 0x4)
    SetChrChipByIndex(0xC, 0x28)
    SetChrSubChip(0xC, 0x0)
    SetChrPos(0xC, 0, -1400, -3000, 0)
    SetMapObjFlags(0x0, 0x1000)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x1000)
    ClearMapObjFlags(0x1, 0x4)
    SetMapObjFrame(0xFF, "hasiraR", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hasiraL", 0x0, 0x1)
    SetMapObjFrame(0xFF, "bl_mae00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "bl_mae01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "bl_mae02", 0x0, 0x1)
    SetMapObjFrame(0xFF, "bl_ato00", 0x1, 0x1)
    SetMapObjFrame(0xFF, "bl_ato01", 0x1, 0x1)
    OP_7D(0xFF, 0xC8, 0xBE, 0x0, 0x1770)
    OP_11(0xA0, 0x0, 0x2D, 0xF, 0x64, 0x1770)
    OP_68(0, 2700, 34000, 0)
    MoveCamera(319, 35, 0, 0)
    OP_6E(750, 0)
    SetCameraDistance(12500, 0)
    MoveCamera(329, 25, 0, 6000)
    SetCameraDistance(15500, 6000)
    Sound(825, 2, 100, 0)
    BeginChrThread(0x11, 1, 0, 28)
    BeginChrThread(0xB, 3, 0, 21)
    FadeToBright(1000, 0)
    Sound(1005, 0, 100, 0)
    Sound(1031, 0, 100, 0)
    Sound(833, 0, 100, 0)
    BlurSwitch(0x3E8, 0xBBFFFFFF, 0x0, 0x1, 0xF)
    SetMessageWindowPos(-1, 120, -1, -1)

    AnonymousTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#4S#20A#60WOh oh oh!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(2000)
    OP_6F(0x79)
    Fade(500)
    OP_68(0, 1900, 28300, 0)
    MoveCamera(329, 13, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(17000, 0)
    CancelBlur(0)
    OP_0D()

    ChrTalk(
        0x108,
        "#01401F#5PMuu! …!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(800)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x101,
        (
            "#00007F#3314V#30W#5P#4S#16A── I will come!\x01",
            "Please be careful!\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    OP_63(0x108, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x32, 0x0, 0x7D0, 0xC8)

    ChrTalk(
        0x109,
        "#10110F#5P#6Aっ!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        "#00610F#5P#6AChi!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_71(0x1, 0xC8, 0xF0, 0x0, 0x0)
    Sleep(1100)
    Sound(1033, 0, 100, 0)
    Sound(833, 0, 100, 0)
    OP_82(0x0, 0xC8, 0xBB8, 0x1F4)
    PlayEffect(0x9, 0x6, 0xB, 0x0, 3000, 200, -2400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x9, 0x7, 0xB, 0x0, -3000, 200, -2400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_79(0x1)
    OP_71(0x1, 0xF1, 0x118, 0x0, 0x20)
    Sleep(100)
    OP_68(0, 1000, 21700, 1000)
    MoveCamera(300, 25, 0, 1000)
    OP_6F(0x79)
    MoveCamera(285, 23, 0, 4500)
    SetCameraDistance(13500, 4500)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    Sound(1006, 0, 100, 0)
    Sound(607, 0, 100, 0)
    BeginChrThread(0x101, 3, 0, 23)
    Sleep(100)
    PlayEffect(0x0, 0x0, 0xD, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    BeginChrThread(0x109, 3, 0, 24)
    Sleep(100)
    PlayEffect(0x0, 0x1, 0xE, 0x0, 0, 0, 0, 30, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    BeginChrThread(0x10A, 3, 0, 25)
    Sleep(100)
    PlayEffect(0x0, 0x2, 0xF, 0x0, 0, 0, 0, 70, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    BeginChrThread(0x108, 3, 0, 26)
    Sleep(100)
    PlayEffect(0x0, 0x3, 0x10, 0x0, 0, 0, 0, 130, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(2000)
    PlayEffect(0x6, 0xFF, 0xD, 0x5, 0, 900, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x6, 0xFF, 0xE, 0x5, 0, 900, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x6, 0xFF, 0xF, 0x5, 0, 900, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x6, 0xFF, 0x10, 0x5, 0, 900, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x6, 0xFF, 0xD, 0x5, 0, 900, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x6, 0xFF, 0xE, 0x5, 0, 900, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x6, 0xFF, 0xF, 0x5, 0, 900, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x6, 0xFF, 0x10, 0x5, 0, 900, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x6, 0xFF, 0xD, 0x5, 0, 900, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x6, 0xFF, 0xE, 0x5, 0, 900, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x6, 0xFF, 0xF, 0x5, 0, 900, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x6, 0xFF, 0x10, 0x5, 0, 900, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    Sound(514, 0, 100, 0)
    Sound(253, 0, 100, 0)
    Sound(248, 0, 100, 0)
    StopEffect(0x0, 0x0)
    StopEffect(0x1, 0x0)
    StopEffect(0x2, 0x0)
    StopEffect(0x3, 0x0)
    PlayEffect(0x1, 0xFF, 0xD, 0x0, 0, -1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xE, 0x0, 0, -1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xF, 0x0, 0, -1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x10, 0x0, 0, -1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    StopEffect(0x6, 0x2)
    StopEffect(0x7, 0x2)
    BeginChrThread(0xB, 3, 0, 37)
    Sleep(1000)
    OP_6F(0x79)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    LoadEffect(0x2, "event\\ev10030.eff")
    LoadEffect(0x3, "event\\ev10031.eff")
    LoadEffect(0x4, "event\\ev10034.eff")
    LoadEffect(0x5, "event\\ev10035.eff")
    LoadEffect(0x6, "event\\ev10036.eff")
    OP_68(0, 2700, 33000, 2000)
    MoveCamera(321, 4, 0, 2000)
    SetCameraDistance(15500, 2000)
    OP_6F(0x79)
    Sound(1004, 2, 100, 0)
    PlayEffect(0x7, 0x0, 0xB, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(1005, 0, 100, 0)
    SetMessageWindowPos(-1, 120, -1, -1)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)

    AnonymousTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#4S#60W#20AOooo on … …!!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(800)

    ChrTalk(
        0x101,
        "#00010F#N#6Pthis is……!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x109,
        "#10110F#N#6PAnd it melts …! Is it?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x10A,
        (
            "#00610F#N#6PTo report on Joachim's death\x01",
            "There was a man …!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(500)
    Sound(1005, 0, 100, 0)
    SetMessageWindowPos(-1, 120, -1, -1)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)

    AnonymousTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#60W#20AAaaaaa ……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    AnonymousTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#60W#30A…. Iyada …\x01",
            "#4SIyada AREA SAE! It is!\x02",
        )
    )

    Sleep(1000)
    OP_82(0xC8, 0x0, 0xBB8, 0x320)
    CloseMessageWindow()
    Sleep(300)

    AnonymousTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#60W#35ADeath Nitaku Nai …\x01",
            "#4S… … Death Nitaka Naiyo Ooh! …!\x07\x00\x02",
        )
    )

    Sleep(1000)
    OP_82(0xC8, 0x0, 0xBB8, 0x3E8)
    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    def lambda_50BC():
        OP_93(0x101, 0x0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_50BC)
    Sleep(0)

    def lambda_50CC():
        OP_93(0x109, 0x0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_50CC)
    Sleep(0)

    def lambda_50DC():
        OP_93(0x10A, 0x0, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_50DC)
    Sleep(0)

    def lambda_50EC():
        OP_93(0x108, 0x0, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 0, lambda_50EC)
    Sleep(0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x10A, 0)
    WaitChrThread(0x108, 0)
    Fade(500)
    OP_68(0, 1900, 25300, 0)
    MoveCamera(330, 7, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(17000, 0)
    OP_0D()

    ChrTalk(
        0x109,
        "#10108F…… Well ………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        "#01403F……Pathetic.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00010FCut …!\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)

    def lambda_5191():
        OP_95(0xFE, 0, 200, 27500, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5191)
    OP_68(0, 2000, 32299, 2000)
    MoveCamera(0, 3, 0, 2000)
    SetCameraDistance(16500, 2000)
    OP_6F(0x79)
    SetCameraDistance(14890, 30000)

    ChrTalk(
        0x109,
        "#10105F#N#12PMr. Lloyd! Is it?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x10A,
        "#00607F#N#12PHey, what … …! Is it?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    WaitChrThread(0x101, 1)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0x101, 0x2E)
    SetChrSubChip(0x101, 0x0)
    SetChrFlags(0x101, 0x10)
    SetChrFlags(0x101, 0x2)
    SetChrFlags(0x101, 0x20)
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x101,
        (
            "#6P#00007FErnest！\x01",
            "Hold in!\x02\x03",
            "Do not lose sight of yourself!\x01",
            "You are, you!\x02",
        )
    )

    CloseMessageWindow()
    Sound(1005, 0, 100, 0)
    SetMessageWindowPos(-1, 70, -1, -1)

    AnonymousTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#60W#20A…… Gugg … … Giggi gig … …?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#6P#00010FUnlike Joachim you are\x01",
            "Red Gnostic\x01",
            "I did not drink in large quantities!\x02\x03",
            "#00007FI will be saved!\x01",
            "Absolutely do not give up!\x02",
        )
    )

    CloseMessageWindow()
    Sound(1005, 0, 100, 0)
    SetMessageWindowPos(-1, 70, -1, -1)

    AnonymousTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#60W#20AKugu …… Gagaga ……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(300)

    ChrTalk(
        0x10A,
        "#00600F#N#12PBannings, you …\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x109,
        "#10108F#N#12P…… Mr. Lloyd ………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopSound(1004, 1000, 100)
    OP_25(0x339, 0x28)
    Fade(500)
    OP_68(0, 2300, 31000, 0)
    MoveCamera(213, 29, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14000, 0)
    SetChrSubChip(0x101, 0x1)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x10A, 0xFF)
    SetChrSubChip(0x10A, 0x0)
    SetChrChipByIndex(0x108, 0xFF)
    SetChrSubChip(0x108, 0x0)
    SetChrPos(0x109, 0, 200, 20400, 0)
    SetChrPos(0x10A, 2500, 200, 21200, 0)
    SetChrPos(0x108, -2500, 200, 21200, 0)
    BeginChrThread(0x109, 3, 0, 27)
    BeginChrThread(0xB, 2, 0, 35)
    StopEffect(0x0, 0x2)
    PlayEffect(0x8, 0x1, 0xB, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    MoveCamera(223, 29, 0, 15000)
    SetCameraDistance(15500, 15000)
    OP_0D()
    EndChrThread(0xB, 0x3)
    StopEffect(0x0, 0x2)
    Sleep(300)
    Sound(1005, 0, 100, 0)
    SetMessageWindowPos(250, 140, -1, -1)

    AnonymousTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#60WUuu … … Ah … …\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#60W…… Do … Doshite ……\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#60WKokomadecita me …\x01",
            "……… Doshishi you … ha ………\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00006F… and that is a different story from this one.\x02\x03",
            "#00008FYou surely sinned.\x02\x03",
            "But that does not matter\x01",
            "Dead in a place like this\x01",
            "I do not think he was sinful.\x02\x03",
            "#00013FBesides, if you die\x01",
            "Eli and McDaill's chairman\x01",
            "It will surely be sad.\x02",
        )
    )

    CloseMessageWindow()
    Sound(802, 0, 100, 0)
    SetChrSubChip(0x101, 0x4)
    Sleep(90)
    SetChrSubChip(0x101, 0x5)
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x101,
        (
            "#00007FSo ….\x01",
            "Absolutely regain yourself!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Sound(1005, 0, 100, 0)
    SetMessageWindowPos(250, 140, -1, -1)

    AnonymousTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#60WErice …… Movement teacher ……\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#60W…… Smanai …… Doshite I … Ha …\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#60W#25A… ….!\x01",
            "…… ARE ARE ARE UP!\x07\x00\x02",
        )
    )

    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x320)
    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sound(1004, 2, 100, 0)
    OP_25(0x339, 0x64)
    BeginChrThread(0xB, 3, 0, 21)
    BeginChrThread(0xB, 2, 0, 36)
    StopEffect(0x1, 0x2)
    PlayEffect(0x7, 0x0, 0xB, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x108, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Sound(802, 0, 100, 0)
    SetChrSubChip(0x101, 0x6)

    ChrTalk(
        0x101,
        "#00010F#5PIs not it OK? Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10113F#5P#NSomething\x01",
            "Why not! Is it?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x10A,
        (
            "#00610FCut, this case,\x01",
            "As expected it is out of the field! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#01400F#5P#NDisagreeable……\x02\x03",
            "#01404FApparently it is \"expert\"\x01",
            "It seems they made it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopBGM(0x1388)
    TurnDirection(0x10A, 0x108, 500)

    ChrTalk(
        0x10A,
        "#00605F#6Pwhat……\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xC, 0x80)
    Sleep(300)

    NpcTalk(
        0xC,
        "Voice of a young man",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#40W#25A\"Sit in the sky#2RNow#We are the Lord. \"\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xC,
        "Voice of a young man",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#40W#30A\"Drawn by the devil and pitiful lost child\x01",
            "Things to call back with your light … \"\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EndChrThread(0xB, 0x3)
    BeginChrThread(0xB, 2, 0, 35)
    StopEffect(0x0, 0x2)
    Sound(1002, 0, 100, 0)
    BeginChrThread(0x11, 2, 0, 33)
    PlayEffect(0x8, 0x1, 0xB, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0x7, 0xB, 0x1, 0, 2000, 0, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(300)
    Sound(692, 0, 80, 0)
    Sleep(700)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x101, 0x10)
    ClearChrFlags(0x101, 0x2)
    ClearChrFlags(0x101, 0x20)

    def lambda_5B1B():
        OP_93(0x101, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_5B1B)
    Sleep(50)

    def lambda_5B2B():
        OP_93(0x109, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_5B2B)
    Sleep(50)

    def lambda_5B3B():
        OP_93(0x10A, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_5B3B)
    Sleep(50)

    def lambda_5B4B():
        OP_93(0x108, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x108, 0, lambda_5B4B)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x10A, 0)
    WaitChrThread(0x108, 0)

    ChrTalk(
        0x101,
        "#12P#00005FHuh……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10105FChurch's verse … ….?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x11, 1, 0, 29)
    EndChrThread(0x11, 0x2)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7573", 0)
    BeginChrThread(0x11, 2, 0, 34)
    Fade(500)
    OP_68(0, 1000, 0, 0)
    MoveCamera(0, 25, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(10500, 0)

    def lambda_5BED():
        OP_95(0xFE, 0, 200, 16000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_5BED)

    def lambda_5C07():

        label("loc_5C07")

        TurnDirection(0xFE, 0xC, 500)
        Yield()
        Jump("loc_5C07")

    QueueWorkItem2(0x101, 2, lambda_5C07)

    def lambda_5C19():

        label("loc_5C19")

        TurnDirection(0xFE, 0xC, 500)
        Yield()
        Jump("loc_5C19")

    QueueWorkItem2(0x109, 2, lambda_5C19)

    def lambda_5C2B():

        label("loc_5C2B")

        TurnDirection(0xFE, 0xC, 500)
        Yield()
        Jump("loc_5C2B")

    QueueWorkItem2(0x10A, 2, lambda_5C2B)

    def lambda_5C3D():

        label("loc_5C3D")

        TurnDirection(0xFE, 0xC, 500)
        Yield()
        Jump("loc_5C3D")

    QueueWorkItem2(0x108, 2, lambda_5C3D)
    OP_68(0, 1000, 2000, 3500)
    MoveCamera(0, 17, 0, 3500)
    SetCameraDistance(15500, 3500)
    OP_6F(0x79)
    Sleep(1000)
    Fade(500)
    OP_68(0, 1300, 16000, 0)
    MoveCamera(221, 21, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17500, 0)
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0x109, 0x8)
    SetChrFlags(0x10A, 0x8)
    SetChrFlags(0x108, 0x8)
    MoveCamera(213, 21, 0, 3000)
    SetCameraDistance(14500, 3000)
    OP_0D()
    OP_6F(0x79)
    WaitChrThread(0xC, 1)

    ChrTalk(
        0x10A,
        "#00605FYou are …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#04303FSorry, I do not have the time\x01",
            "I will treat you right away.\x02\x03",
            "#04300FYou retired for a while#2RWhen#Can you have it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FEr, Oh … yes!\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(15000, 1500)

    def lambda_5D8D():
        OP_95(0xFE, 0, 200, 27600, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_5D8D)
    Sleep(1500)
    EndChrThread(0x11, 0x2)
    BeginChrThread(0x11, 1, 0, 30)
    BeginChrThread(0x11, 2, 0, 33)
    Fade(500)
    OP_68(0, 1500, 29500, 0)
    MoveCamera(310, 15, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(17500, 0)
    SetCameraDistance(16000, 2500)
    ClearChrFlags(0x101, 0x8)
    ClearChrFlags(0x109, 0x8)
    ClearChrFlags(0x10A, 0x8)
    ClearChrFlags(0x108, 0x8)
    SetChrPos(0x101, -1300, 200, 25500, 180)
    SetChrPos(0x109, 1300, 200, 23000, 180)
    SetChrPos(0x10A, 2200, 200, 24000, 180)
    SetChrPos(0x108, -2200, 200, 24000, 180)
    OP_0D()
    Sleep(1500)

    def lambda_5E52():
        OP_96(0xFE, 0x1F4, 0xC8, 0x5BCC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5E52)
    Sleep(300)

    def lambda_5E6F():
        OP_96(0xFE, 0xFFFFFE0C, 0xC8, 0x61A8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5E6F)
    WaitChrThread(0xC, 1)
    SetMessageWindowPos(250, 70, -1, -1)

    AnonymousTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Googgu …\x01",
            "…… AREA ___ ___ 0\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0xC,
        (
            "#6P#04308FHmm, it's a step before the collapse.\x02\x03",
            "#04304F… but … somehow\x01",
            "Did you stay with us?\x02\x03",
            "#04301FIf this is the case\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(0, 2300, 27600, 0)
    MoveCamera(0, 21, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(14000, 0)
    OP_68(0, 1300, 27600, 2000)
    Sleep(1000)
    BeginChrThread(0x11, 1, 0, 31)
    Sound(531, 0, 100, 0)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0xC, 0x2F)
    SetChrSubChip(0xC, 0x0)
    BeginChrThread(0xC, 3, 0, 20)
    Sound(357, 0, 100, 0)
    PlayEffect(0x2, 0x2, 0xFF, 0x0, 0, 250, 27600, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_6F(0x79)
    Sleep(300)

    ChrTalk(
        0xC,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#5P#04303F#50W#25A\"A sparkling blue stamp at my abyss\"\x02",
        )
    )

    CloseMessageWindow()
    MoveCamera(315, 17, 0, 1500)
    OP_6F(0x79)
    SetCameraDistance(13500, 500)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x1, 0x5)
    Sound(895, 0, 100, 0)
    Sound(222, 0, 100, 0)
    PlayEffect(0x3, 0x3, 0xFF, 0x0, 0, 500, 27600, 0, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)
    OP_7D(0xFF, 0xC8, 0xDC, 0x0, 0x5DC)
    Sleep(1500)
    CancelBlur(0)
    Sleep(500)

    ChrTalk(
        0xC,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#5P#04301F#50W#30A\"I will talk a tragedy as light,\x01",
            "Point the way of a lost child ─ ─! \"\x02",
        )
    )

    CloseMessageWindow()
    Sound(1002, 0, 100, 0)
    PlayEffect(0x6, 0xFF, 0xFF, 0x0, 0, 500, 27600, 0, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)
    EndChrThread(0xC, 0x3)
    SetChrSubChip(0xC, 0x4)
    Sleep(90)
    SetChrSubChip(0xC, 0x5)
    BeginChrThread(0xB, 3, 0, 22)
    OP_68(0, 2300, 31600, 1500)
    MoveCamera(327, 3, 0, 1500)
    SetCameraDistance(16500, 1500)
    BeginChrThread(0x11, 3, 0, 32)
    Sound(222, 0, 100, 0)
    PlayEffect(0x5, 0x6, 0xB, 0x1, 0, 2000, 0, 0, 0, 0, 1100, 1100, 1100, 0xFF, 0, 0, 0, 0)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x109, 0x2)
    EndChrThread(0x10A, 0x2)
    EndChrThread(0x108, 0x2)

    def lambda_61BC():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_61BC)
    Sleep(30)

    def lambda_61CC():
        OP_93(0x10A, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_61CC)
    Sleep(30)

    def lambda_61DC():
        OP_93(0x109, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_61DC)
    Sleep(30)

    def lambda_61EC():
        OP_93(0x108, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x108, 0, lambda_61EC)
    Sleep(30)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x10A, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x108, 0)
    OP_6F(0x79)
    Sleep(500)

    ChrTalk(
        0x101,
        "#00005F#30W#N#6P#12ATh-This is……\x02",
    )

    Sleep(2000)

    ChrTalk(
        0x10A,
        "#00605F#30W#N#6P#15AThat light is united ……\x02",
    )

    Sleep(1500)
    SetCameraDistance(19500, 2000)
    Sound(829, 0, 100, 0)
    Sound(1002, 0, 100, 0)
    Sound(833, 0, 80, 0)
    StopSound(825, 2000, 30)
    StopSound(1004, 2000, 30)
    EndChrThread(0x11, 0x1)
    EndChrThread(0x11, 0x2)
    EndChrThread(0x11, 0x3)
    FadeToDark(2000, 16777215, -1)
    OP_0D()
    Sleep(1000)
    OP_68(0, 1100, 28800, 0)
    MoveCamera(310, 21, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(19500, 0)
    SetMapObjFlags(0x1, 0x4)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0xB, 0x80)
    EndChrThread(0xB, 0xFF)
    SetChrChipByIndex(0xC, 0x28)
    SetChrSubChip(0xC, 0x0)
    StopEffect(0x1, 0x0)
    StopEffect(0x2, 0x0)
    StopEffect(0x3, 0x0)
    StopEffect(0x6, 0x0)
    StopEffect(0x7, 0x0)
    OP_7D(0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_11(0xB3, 0x35, 0x5E, 0xA, 0xC8, 0x0)

    def lambda_631A():
        TurnDirection(0x101, 0x8, 0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_631A)
    Sleep(0)

    def lambda_632A():
        TurnDirection(0x109, 0x8, 0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_632A)
    Sleep(0)

    def lambda_633A():
        TurnDirection(0x10A, 0x8, 0)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_633A)
    Sleep(0)

    def lambda_634A():
        TurnDirection(0x108, 0x8, 0)
        ExitThread()

    QueueWorkItem(0x108, 0, lambda_634A)
    Sleep(0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x10A, 0)
    WaitChrThread(0x108, 0)
    SetCameraDistance(17000, 2000)
    FadeToBright(2000, 16777215)
    OP_0D()

    ChrTalk(
        0x109,
        "#10102F#30W#N#6PAh……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        "#00002F#30W#N#6PWell, back … ….!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xC,
        "#04306F#30W#5PWhew … … did something happen.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    def lambda_63F4():
        OP_95(0xFE, 0, 200, 29300, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_63F4)
    WaitChrThread(0xC, 1)
    Fade(250)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0xC, 0x30)
    SetChrSubChip(0xC, 0x0)
    SetChrFlags(0xC, 0x10)
    SetChrFlags(0xC, 0x2)
    SetChrFlags(0xC, 0x20)
    OP_0D()
    SetCameraDistance(16500, 1500)

    def lambda_643E():
        OP_96(0xFE, 0xFFFFFF38, 0xC8, 0x6A40, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_643E)
    Sleep(200)

    def lambda_645B():
        OP_96(0xFE, 0xC8, 0xC8, 0x6464, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_645B)
    Sleep(200)

    def lambda_6478():
        TurnDirection(0xFE, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_6478)

    def lambda_6485():
        OP_96(0xFE, 0x76C, 0xC8, 0x6720, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_6485)
    Sleep(200)

    def lambda_64A2():
        TurnDirection(0xFE, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_64A2)

    def lambda_64AF():
        OP_96(0xFE, 0xFFFFF894, 0xC8, 0x6590, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_64AF)
    WaitChrThread(0x101, 1)
    Sleep(800)

    ChrTalk(
        0x101,
        "#00013F#6PHow are you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#04304FYeah, I just fainted.\x02\x03",
            "#04300FA few days can not get up.\x01",
            "There is no different in life.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#6PI'm glad.\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x109, 1)
    WaitChrThread(0x10A, 1)
    WaitChrThread(0x108, 1)

    ChrTalk(
        0x109,
        "#6P#10112FHaa … It is a safe one.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#6P#00607FWell, anyway\x01",
            "Who the hell are you! Is it?\x02\x03",
            "It seems to be the Father of the Church … …\x01",
            "How come this place! Is it?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0xC8, 1900, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Fade(250)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0xC, 0x28)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x10)
    ClearChrFlags(0xC, 0x2)
    ClearChrFlags(0xC, 0x20)
    OP_0D()
    TurnDirection(0xC, 0x108, 500)

    ChrTalk(
        0xC,
        (
            "#11P#04305FWell, Arios.\x02\x03",
            "To me, to all of you here\x01",
            "Are you talking?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#01404FHuh, whether you will make it in time\x01",
            "I was told that I do not know.\x02\x03",
            "#01402FThe standpoint would be the position,\x01",
            "I had him lie down just in case.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11P#04304FIndeed, I will be saved.\x02\x03",
            "#04311FNo, as usual\x01",
            "He is a nice guy with a nice feeling.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#01404FHuh, you better.\x02\x03",
            "#01402FThank you.\x01",
            "I was really saved for coming.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00011F#6PEr …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#6P#00606FHun, apparently without permission\x01",
            "You seem to have insured.\x02\x03",
            "#00600FThe Yaoi Association belongs to the Ministry of Seaport\x01",
            "\"Star cup knight\" Which do you think?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#3P#10105FSeaport Province, Star Cup Knight ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F#6PSurely \"ancient artifacts#8RArtifact#The\x01",
            "It is collecting … …?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 500)
    Sleep(150)

    ChrTalk(
        0xC,
        "#11P#04304FHaha, was your prospects?\x02",
    )

    CloseMessageWindow()
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0xC,
        (
            "Nice to meet you ──\x01",
            "Seven Yi Church, belongs to the Star Cup Order\x01",
            "It's Kevin Graham.\x02\x03",
            "In response to Arios' contact\x01",
            "I was invited to the party.\x02\x03",
            "Please let me know your favorite ──\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    SetCameraDistance(17000, 2000)
    StopSound(129, 2000, 90)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    OP_CC(0x1, 0xFF, 0x0)
    StopBGM(0xFA0)
    WaitBGM()
    SetScenarioFlags(0x22, 0)
    NewScene("t5000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_19_41F6 end

    def Function_20_6A4C(): pass

    label("Function_20_6A4C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6A78")
    SetChrSubChip(0xC, 0x0)
    Sleep(100)
    SetChrSubChip(0xC, 0x1)
    Sleep(100)
    SetChrSubChip(0xC, 0x2)
    Sleep(100)
    SetChrSubChip(0xC, 0x3)
    Sleep(100)
    Jump("Function_20_6A4C")

    label("loc_6A78")

    Return()

    # Function_20_6A4C end

    def Function_21_6A79(): pass

    label("Function_21_6A79")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6A9D")
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)
    Sleep(500)
    Jump("Function_21_6A79")

    label("loc_6A9D")

    Return()

    # Function_21_6A79 end

    def Function_22_6A9E(): pass

    label("Function_22_6A9E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6AC2")
    OP_82(0x32, 0x32, 0xBB8, 0x1F4)
    Sleep(500)
    Jump("Function_22_6A9E")

    label("loc_6AC2")

    Return()

    # Function_22_6A9E end

    def Function_23_6AC3(): pass

    label("Function_23_6AC3")

    SetChrChipByIndex(0x101, 0x29)
    SetChrSubChip(0x101, 0x2)
    Sound(844, 0, 100, 0)

    def lambda_6AD6():
        OP_9D(0xFE, 0xFFFFFC18, 0xC8, 0x5014, 0x190, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6AD6)
    WaitChrThread(0x101, 1)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    Return()

    # Function_23_6AC3 end

    def Function_24_6AFB(): pass

    label("Function_24_6AFB")

    SetChrChipByIndex(0x109, 0x31)
    SetChrSubChip(0x109, 0x2)
    Sound(809, 0, 100, 0)

    def lambda_6B0E():
        OP_9D(0xFE, 0x5DC, 0xC8, 0x4A38, 0x190, 0xBB8)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6B0E)
    WaitChrThread(0x109, 1)
    SetChrChipByIndex(0x109, 0x20)
    SetChrSubChip(0x109, 0x0)
    Sleep(1500)
    SetChrChipByIndex(0x109, 0x2C)
    SetChrSubChip(0x109, 0x0)
    Sound(531, 0, 100, 0)
    Sleep(50)
    SetChrSubChip(0x109, 0x1)
    Sleep(50)
    SetChrSubChip(0x109, 0x2)
    Sleep(50)
    SetChrSubChip(0x109, 0x3)
    Sleep(50)
    Sound(2450, 255, 100, 0)
    Sound(539, 0, 100, 0)
    SetChrSubChip(0x109, 0x4)
    PlayEffect(0x5, 0xFF, 0xFE, 0x5, 0, 1200, 1100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(30)
    SetChrSubChip(0x109, 0x5)
    Sleep(30)
    SetChrSubChip(0x109, 0x4)
    PlayEffect(0x5, 0xFF, 0xFE, 0x5, 0, 1200, 1100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(30)
    SetChrSubChip(0x109, 0x5)
    Sleep(30)
    SetChrSubChip(0x109, 0x4)
    PlayEffect(0x5, 0xFF, 0xFE, 0x5, 0, 1200, 1100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(30)
    SetChrSubChip(0x109, 0x5)
    Sleep(30)
    SetChrSubChip(0x109, 0x4)
    PlayEffect(0x5, 0xFF, 0xFE, 0x5, 0, 1200, 1100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(30)
    SetChrSubChip(0x109, 0x5)
    Sleep(30)
    Sound(539, 0, 100, 0)
    SetChrSubChip(0x109, 0x4)
    PlayEffect(0x5, 0xFF, 0xFE, 0x5, 0, 1200, 1100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(30)
    SetChrSubChip(0x109, 0x5)
    Sleep(30)
    SetChrSubChip(0x109, 0x4)
    PlayEffect(0x5, 0xFF, 0xFE, 0x5, 0, 1200, 1100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(30)
    SetChrSubChip(0x109, 0x5)
    Sleep(30)
    SetChrSubChip(0x109, 0x4)
    PlayEffect(0x5, 0xFF, 0xFE, 0x5, 0, 1200, 1100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(30)
    SetChrSubChip(0x109, 0x5)
    Sleep(30)
    SetChrSubChip(0x109, 0x4)
    PlayEffect(0x5, 0xFF, 0xFE, 0x5, 0, 1200, 1100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(30)
    SetChrSubChip(0x109, 0x5)
    Sleep(30)
    SetChrSubChip(0x109, 0x4)
    PlayEffect(0x5, 0xFF, 0xFE, 0x5, 0, 1200, 1100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(30)
    SetChrSubChip(0x109, 0x5)
    Sleep(30)
    SetChrSubChip(0x109, 0x4)
    PlayEffect(0x5, 0xFF, 0xFE, 0x5, 0, 1200, 1100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(30)
    SetChrSubChip(0x109, 0x5)
    Sleep(30)
    SetChrSubChip(0x109, 0x4)
    PlayEffect(0x5, 0xFF, 0xFE, 0x5, 0, 1200, 1100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(30)
    SetChrSubChip(0x109, 0x5)
    Sleep(30)
    SetChrSubChip(0x109, 0x4)
    PlayEffect(0x5, 0xFF, 0xFE, 0x5, 0, 1200, 1100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(30)
    SetChrSubChip(0x109, 0x5)
    Sleep(30)
    SetChrSubChip(0x109, 0x4)
    Sleep(50)
    SetChrSubChip(0x109, 0x3)
    Sleep(50)
    SetChrSubChip(0x109, 0x2)
    Sleep(50)
    SetChrSubChip(0x109, 0x1)
    Sleep(50)
    SetChrSubChip(0x109, 0x0)
    Sleep(50)
    SetChrChipByIndex(0x109, 0x20)
    SetChrSubChip(0x109, 0x0)
    Return()

    # Function_24_6AFB end

    def Function_25_6ED5(): pass

    label("Function_25_6ED5")

    SetChrFlags(0x10A, 0x20)

    def lambda_6EDF():
        OP_93(0xFE, 0x13B, 0x2BC)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_6EDF)
    SetChrChipByIndex(0x10A, 0x32)
    SetChrSubChip(0x10A, 0x0)

    def lambda_6EF4():
        OP_9D(0xFE, 0xDAC, 0xC8, 0x4F4C, 0x190, 0xBB8)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_6EF4)
    WaitChrThread(0x10A, 1)
    SetChrChipByIndex(0x10A, 0x22)
    SetChrSubChip(0x10A, 0x0)
    Sleep(1500)
    SetChrChipByIndex(0x10A, 0x2D)
    SetChrSubChip(0x10A, 0x0)
    Sleep(100)
    Sound(567, 0, 100, 0)
    PlayEffect(0x5, 0xFF, 0xFE, 0x5, 0, 1100, 1200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0x10A, 0x1)
    Sleep(300)
    SetChrSubChip(0x10A, 0x2)
    Sleep(50)
    SetChrSubChip(0x10A, 0x3)
    Sleep(50)
    SetChrSubChip(0x10A, 0x4)
    Sleep(50)
    SetChrSubChip(0x10A, 0x0)
    Sleep(100)
    Sound(2512, 255, 100, 0)
    Sound(567, 0, 100, 0)
    PlayEffect(0x5, 0xFF, 0xFE, 0x5, 0, 1100, 1200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0x10A, 0x1)
    Sleep(300)
    SetChrSubChip(0x10A, 0x2)
    Sleep(50)
    SetChrSubChip(0x10A, 0x3)
    Sleep(50)
    SetChrSubChip(0x10A, 0x4)
    Sleep(50)
    SetChrSubChip(0x10A, 0x0)
    Sleep(100)
    Sound(567, 0, 100, 0)
    PlayEffect(0x5, 0xFF, 0xFE, 0x5, 0, 1100, 1200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0x10A, 0x1)
    Sleep(300)
    SetChrChipByIndex(0x10A, 0x22)
    SetChrSubChip(0x10A, 0x0)
    ClearChrFlags(0x10A, 0x20)
    Return()

    # Function_25_6ED5 end

    def Function_26_703E(): pass

    label("Function_26_703E")

    SetChrFlags(0x108, 0x20)

    def lambda_7048():
        OP_93(0xFE, 0x3C, 0x2BC)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_7048)
    SetChrChipByIndex(0x108, 0x25)
    SetChrSubChip(0x108, 0x3)

    def lambda_705D():
        OP_9D(0xFE, 0xFFFFF060, 0xC8, 0x526C, 0x190, 0xBB8)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_705D)
    WaitChrThread(0x108, 1)
    Sound(540, 0, 100, 0)
    SetChrChipByIndex(0x108, 0x24)
    SetChrSubChip(0x108, 0x0)
    Sleep(100)
    Sound(881, 0, 100, 0)
    PlayEffect(0x4, 0x1, 0x108, 0x5, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_70CC():
        OP_A6(0xFE, 0x32, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_70CC)
    SetChrChipByIndex(0x108, 0x2A)
    SetChrSubChip(0x108, 0x3)
    Sleep(1000)
    StopEffect(0x1, 0x2)
    Sound(259, 0, 100, 0)
    Sound(3988, 255, 100, 0)
    PlayEffect(0x2, 0xFF, 0x108, 0x5, 0, 0, 0, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0x108, 0x5, 0, 0, 0, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0x108, 0x2B)
    SetChrSubChip(0x108, 0x0)
    Sleep(100)
    SetChrSubChip(0x108, 0x1)
    Sleep(2500)
    SetChrSubChip(0x108, 0x2)
    Sleep(100)
    SetChrChipByIndex(0x108, 0x24)
    SetChrSubChip(0x108, 0x0)
    ClearChrFlags(0x108, 0x20)
    Return()

    # Function_26_703E end

    def Function_27_718F(): pass

    label("Function_27_718F")


    def lambda_7194():
        OP_96(0xFE, 0x0, 0xC8, 0x5B68, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_7194)
    Sleep(100)

    def lambda_71B1():
        OP_96(0xFE, 0x7D0, 0xC8, 0x5E88, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_71B1)
    Sleep(100)

    def lambda_71CE():
        OP_96(0xFE, 0xFFFFF830, 0xC8, 0x5E88, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_71CE)
    Return()

    # Function_27_718F end

    def Function_28_71E4(): pass

    label("Function_28_71E4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_71FD")
    Sound(892, 0, 50, 0)
    Sleep(1150)
    Jump("Function_28_71E4")

    label("loc_71FD")

    Return()

    # Function_28_71E4 end

    def Function_29_71FE(): pass

    label("Function_29_71FE")

    OP_25(0x339, 0x5F)
    OP_25(0x3EC, 0x5F)
    Sleep(100)
    OP_25(0x339, 0x5A)
    OP_25(0x3EC, 0x5A)
    Sleep(100)
    OP_25(0x339, 0x55)
    OP_25(0x3EC, 0x55)
    Sleep(100)
    OP_25(0x339, 0x50)
    OP_25(0x3EC, 0x50)
    Sleep(100)
    OP_25(0x339, 0x4B)
    OP_25(0x3EC, 0x4B)
    Sleep(100)
    OP_25(0x339, 0x46)
    OP_25(0x3EC, 0x46)
    Sleep(100)
    OP_25(0x339, 0x41)
    OP_25(0x3EC, 0x41)
    Sleep(100)
    OP_25(0x339, 0x3C)
    OP_25(0x3EC, 0x3C)
    Sleep(100)
    OP_25(0x339, 0x32)
    OP_25(0x3EC, 0x32)
    Sleep(100)
    OP_25(0x339, 0x28)
    OP_25(0x3EC, 0x28)
    Return()

    # Function_29_71FE end

    def Function_30_726A(): pass

    label("Function_30_726A")

    OP_25(0x339, 0x32)
    OP_25(0x3EC, 0x32)
    Sleep(100)
    OP_25(0x339, 0x3C)
    OP_25(0x3EC, 0x3C)
    Sleep(100)
    OP_25(0x339, 0x41)
    OP_25(0x3EC, 0x41)
    Sleep(100)
    OP_25(0x339, 0x46)
    OP_25(0x3EC, 0x46)
    Sleep(100)
    OP_25(0x339, 0x4B)
    OP_25(0x3EC, 0x4B)
    Sleep(100)
    OP_25(0x339, 0x50)
    OP_25(0x3EC, 0x50)
    Return()

    # Function_30_726A end

    def Function_31_72AA(): pass

    label("Function_31_72AA")

    OP_25(0x339, 0x4B)
    OP_25(0x3EC, 0x4B)
    Sleep(100)
    OP_25(0x339, 0x46)
    OP_25(0x3EC, 0x46)
    Sleep(100)
    OP_25(0x339, 0x41)
    OP_25(0x3EC, 0x41)
    Sleep(100)
    OP_25(0x339, 0x3C)
    OP_25(0x3EC, 0x3C)
    Sleep(100)
    OP_25(0x339, 0x32)
    OP_25(0x3EC, 0x32)
    Sleep(100)
    OP_25(0x339, 0x28)
    OP_25(0x3EC, 0x28)
    Return()

    # Function_31_72AA end

    def Function_32_72EA(): pass

    label("Function_32_72EA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7303")
    Sound(934, 0, 60, 0)
    Sleep(1500)
    Jump("Function_32_72EA")

    label("loc_7303")

    Return()

    # Function_32_72EA end

    def Function_33_7304(): pass

    label("Function_33_7304")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_731D")
    Sound(1034, 0, 100, 0)
    Sleep(1000)
    Jump("Function_33_7304")

    label("loc_731D")

    Return()

    # Function_33_7304 end

    def Function_34_731E(): pass

    label("Function_34_731E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7337")
    Sound(1034, 0, 50, 0)
    Sleep(1000)
    Jump("Function_34_731E")

    label("loc_7337")

    Return()

    # Function_34_731E end

    def Function_35_7338(): pass

    label("Function_35_7338")

    OP_74(0x1, 0x1E)
    Sleep(300)
    OP_74(0x1, 0x1D)
    Sleep(300)
    OP_74(0x1, 0x1C)
    Sleep(300)
    OP_74(0x1, 0x1B)
    Sleep(300)
    OP_74(0x1, 0x1A)
    Sleep(300)
    OP_74(0x1, 0x19)
    Sleep(300)
    OP_74(0x1, 0x18)
    Sleep(300)
    OP_74(0x1, 0x17)
    Sleep(300)
    OP_74(0x1, 0x16)
    Sleep(300)
    OP_74(0x1, 0x15)
    Sleep(300)
    OP_74(0x1, 0x14)
    Sleep(300)
    OP_74(0x1, 0x13)
    Sleep(300)
    OP_74(0x1, 0x12)
    Sleep(300)
    OP_74(0x1, 0x11)
    Sleep(300)
    OP_74(0x1, 0x10)
    Sleep(300)
    OP_74(0x1, 0xF)
    Return()

    # Function_35_7338 end

    def Function_36_73A6(): pass

    label("Function_36_73A6")

    OP_74(0x1, 0xF)
    Sleep(300)
    OP_74(0x1, 0x10)
    Sleep(300)
    OP_74(0x1, 0x11)
    Sleep(300)
    OP_74(0x1, 0x12)
    Sleep(300)
    OP_74(0x1, 0x13)
    Sleep(300)
    OP_74(0x1, 0x14)
    Sleep(300)
    OP_74(0x1, 0x15)
    Sleep(300)
    OP_74(0x1, 0x16)
    Sleep(300)
    OP_74(0x1, 0x17)
    Sleep(300)
    OP_74(0x1, 0x18)
    Sleep(300)
    OP_74(0x1, 0x19)
    Sleep(300)
    OP_74(0x1, 0x1A)
    Sleep(300)
    OP_74(0x1, 0x1B)
    Sleep(300)
    OP_74(0x1, 0x1C)
    Sleep(300)
    OP_74(0x1, 0x1D)
    Sleep(300)
    OP_74(0x1, 0x1E)
    Return()

    # Function_36_73A6 end

    def Function_37_7414(): pass

    label("Function_37_7414")

    OP_71(0x1, 0x119, 0x136, 0x0, 0x0)
    OP_79(0x1)
    Sound(831, 0, 100, 0)
    Sound(830, 0, 50, 0)
    OP_71(0x1, 0x384, 0x38E, 0x0, 0x0)
    OP_79(0x1)
    OP_71(0x1, 0x38F, 0x3B6, 0x0, 0x20)
    Return()

    # Function_37_7414 end

    SaveToFile()

Try(main)
