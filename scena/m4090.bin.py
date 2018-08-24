from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "Ernest",                 # 1
        "Former Chairman Hartmann",# 2
        "ダミーハルトマン",       # 3
        "Demon Ernest",           # 4
        "Young Man in Priest's Robe",# 5
        "ダミーエフェクト",       # 6
        "ダミーエフェクト",       # 7
        "ダミーエフェクト",       # 8
        "ダミーエフェクト",       # 9
        "SE制御",                 # 10
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
        "Function_4_1D6C",         # 04, 4
        "Function_5_1DA7",         # 05, 5
        "Function_6_1DBA",         # 06, 6
        "Function_7_3B97",         # 07, 7
        "Function_8_3BF7",         # 08, 8
        "Function_9_3C1B",         # 09, 9
        "Function_10_3C3F",        # 0A, 10
        "Function_11_3C69",        # 0B, 11
        "Function_12_3C8B",        # 0C, 12
        "Function_13_3CB0",        # 0D, 13
        "Function_14_3EA6",        # 0E, 14
        "Function_15_3F23",        # 0F, 15
        "Function_16_3F7F",        # 10, 16
        "Function_17_40E6",        # 11, 17
        "Function_18_433A",        # 12, 18
        "Function_19_4387",        # 13, 19
        "Function_20_6C9F",        # 14, 20
        "Function_21_6CCC",        # 15, 21
        "Function_22_6CF1",        # 16, 22
        "Function_23_6D16",        # 17, 23
        "Function_24_6D4E",        # 18, 24
        "Function_25_7128",        # 19, 25
        "Function_26_7291",        # 1A, 26
        "Function_27_73E2",        # 1B, 27
        "Function_28_7437",        # 1C, 28
        "Function_29_7451",        # 1D, 29
        "Function_30_74BD",        # 1E, 30
        "Function_31_74FD",        # 1F, 31
        "Function_32_753D",        # 20, 32
        "Function_33_7557",        # 21, 33
        "Function_34_7571",        # 22, 34
        "Function_35_758B",        # 23, 35
        "Function_36_75F9",        # 24, 36
        "Function_37_7667",        # 25, 37
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
        "#00007F(Ah!)\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x109, 0)

    ChrTalk(
        0x109,
        "#6P#10101F(There they are!)\x02",
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
            "#02613FHehe... It's just as\x01",
            "Master Joachim said.\x02\x03",
            "#02610FI should be able to\x01",
            "accomplish my goal without\x01",
            "any further delay here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6P#02703FUgh... Enough of this\x01",
            "madness!\x02\x03",
            "#02701FYou and Joachim are\x01",
            "completely and\x01",
            "absolutely insane!\x02\x03",
            "Don't drag me into your\x01",
            "crazy delusions!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 500)

    ChrTalk(
        0x8,
        (
            "#11P#02613FHmph. Look who's talking.\x02\x03",
            "#02610FI recall a certain... Paradise, was it?\x01",
            "That's rather arrogant for someone who\x01",
            "was using such a place, don't you think?\x02",
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
            "#6P#02705FT-That's only because I was\x01",
            "tricked and led there by a pawn\x01",
            "of the cult...\x02\x03",
            "#02703FIf I'd known it was such a\x01",
            "distasteful place, I never\x01",
            "would've gotten involved!\x02\x03",
            "#02701FAnd dosing me with that strange\x01",
            "medicine on top of it all... It's\x01",
            "me who's the victim here! Me!\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x9)

    ChrTalk(
        0x8,
        (
            "#11P#02613FOh please, do you really\x01",
            "think society would believe\x01",
            "that kind of story?\x02\x03",
            "#02610FI'm sure Crossbell Times\x01",
            "would love to run a full-\x01",
            "length feature story on that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#6P#02701FUgh...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(2090, 255, 100, 0)

    NpcTalk(
        0x101,
        "Lloyd's Voice",
        "#30W#12AFreeze!\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_BD1():
        OP_93(0x8, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_BD1)
    Sleep(50)

    def lambda_BE1():
        OP_93(0x9, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_BE1)
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

    def lambda_C62():
        OP_97(0x101, 0x0, 0x0, 0x2710, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_C62)
    Sleep(100)

    def lambda_C7F():
        OP_97(0x109, 0x0, 0x0, 0x2710, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_C7F)
    Sleep(500)

    def lambda_C9C():
        OP_95(0xFE, 0, 200, 28500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_C9C)
    OP_6F(0x79)

    ChrTalk(
        0x9,
        "#11P#02705FOh, it's the police!\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x8, 1)

    ChrTalk(
        0x8,
        (
            "#02605F#11POh my, you again?\x02\x03",
            "#02613FI had hoped I'd lost you\x01",
            "pests, but you two cockroaches\x01",
            "managed to slip through.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00013FThat giant altar... So\x01",
            "this is the innermost\x01",
            "chamber of the lodge.\x02\x03",
            "#00007FWhere are Arios and\x01",
            "Dudley!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02610F#11PAh. The Divine Blade of\x01",
            "Wind and the Ace of\x01",
            "Section One?\x02\x03",
            "#02613FThose two are bad news,\x01",
            "so I slowed them down a\x01",
            "bit.\x02\x03",
            "Those ten archaisms\x01",
            "should give them a great\x01",
            "workout.\x02",
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
        "#6P#00010FWha...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10110FT-Ten of those\x01",
            "monsters...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02613F#11PTo be sure, I used everything I\x01",
            "inherited from my master.\x02\x03",
            "#02610FThat said, they should be enough to\x01",
            "finish them off.\x02\x03",
            "That means I can go ahead and focus\x01",
            "myself on leisurely fulfilling my\x01",
            "goal in this holy place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00007FAs if we'd let you!\x02",
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
        (
            "#6P#10107FPut your hands up and\x01",
            "surrender!\x02",
        )
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
            "Now, now... You don't seem to\x01",
            "understand the situation you're in.\x02\x03",
            "Anyhow, I was wondering why I\x01",
            "didn't see Elie with you...\x02\x03",
            "Oh, I see. She temporarily left the\x01",
            "SSS to assist Chairman MacDowell,\x01",
            "right?\x02",
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
        "#6P#00010FGuh!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10101FN-No way... Did you just\x01",
            "read Lloyd's memories!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#06613F#11PFurthermore, a collaboration between\x01",
            "the new mayor and chairman to pass\x01",
            "laws...\x02\x03",
            "#06610FHow interesting. This would make it\x01",
            "easier for the SSS to make their moves.\x01",
            "Gaining new political foothold, I see.\x02\x03",
            "#06613FHeh. Seems like something the new mayor\x01",
            "would do. I must say, quite an\x01",
            "interesting experiment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00013F...............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#06606F#11PHowever, I must say it's foolish for\x01",
            "someone like Elie to waste her\x01",
            "potential with the likes of the police.\x02\x03",
            "#06600FHmm... Once I take office as mayor,\x01",
            "I'll have the SSS disbanded.\x02\x03",
            "Then I'll hire Elie as my personal\x01",
            "secretary and make the most of her\x01",
            "abilities.\x02\x03",
            "#06604FYes, yes, that sounds perfect. I'll do\x01",
            "just that!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15F8")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "◆Max bond with Elie in Zero\x01",       # 0
            "◆Zero achievement incomplete\x01",      # 1
            "◆No change\x01",                        # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_15E3"),
        (1, "loc_15EB"),
        (2, "loc_15F3"),
        (SWITCH_DEFAULT, "loc_15F3"),
    )


    label("loc_15E3")

    SetScenarioFlags(0x25, 3)
    Jump("loc_15F8")

    label("loc_15EB")

    ClearScenarioFlags(0x25, 3)
    Jump("loc_15F8")

    label("loc_15F3")

    Jump("loc_15F8")

    label("loc_15F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 3)), scpexpr(EXPR_END)), "loc_175E")
    Sleep(500)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x101,
        (
            "#6P#00007F#4SStop messing around!\x02\x03",
            "#3S#00010FLike hell I'd let you\x01",
            "drag Elie into your\x01",
            "messed up delusions!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10105F(Lloyd's furious...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#06603F#11PHmph... It's not like a brat\x01",
            "like you would be a good match\x01",
            "for her in the first place.\x02\x03",
            "#06611FI'll have to weed out these\x01",
            "rotten buds to open her eyes.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_183E")

    label("loc_175E")


    ChrTalk(
        0x101,
        "#6P#00013FYou...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10106FSaying that with a\x01",
            "straight face is just...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#06613F#11PHehe... You're also an\x01",
            "enemy of master Joachim.\x02\x03",
            "#06610FI'll have to weed out\x01",
            "the rotten buds to cut\x01",
            "her loose from you.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_183E")

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

    def lambda_190A():
        OP_A6(0xFE, 0x0, 0x1E, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_190A)
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

    def lambda_196C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x5DC)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_196C)

    def lambda_197D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_197D)
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
        "#6P#02705FEeeeek...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10110FI-Isn't that...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00010FYeah... "Demonization",\x01",
            "the effect of the red\x01",
            "Gnosis.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(60, 80, -1, -1)
    Sleep(300)

    AnonymousTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "How pleasant to have my\x01",
            "powers powers awakened\x01",
            "in this holy place.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Well then, how about a modest\x01",
            "sacrifice before I my greatest\x01",
            "desires are granted...\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "I'll have you struggle,\x01",
            "squirm and writhe before\x01",
            "me!\x07\x00\x02",
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
        "#6P#00007FI don't think so!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10107FOne target confirmed!\x01",
            "Commence operations!\x02",
        )
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

    def lambda_1D17():
        OP_9D(0xFE, 0x0, 0xC8, 0x53FC, 0x384, 0x5DC)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1D17)
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

    def Function_4_1D6C(): pass

    label("Function_4_1D6C")

    OP_63(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_93(0x9, 0x87, 0x1F4)
    Sleep(500)

    def lambda_1D8D():
        OP_96(0xFE, 0xFFFFF31C, 0xC8, 0x79E0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1D8D)
    WaitChrThread(0x9, 1)
    Return()

    # Function_4_1D6C end

    def Function_5_1DA7(): pass

    label("Function_5_1DA7")

    Sleep(2500)
    Sound(805, 0, 100, 0)
    Sleep(100)
    Sound(531, 0, 100, 0)
    Return()

    # Function_5_1DA7 end

    def Function_6_1DBA(): pass

    label("Function_6_1DBA")

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
            "#5P#N#15AHehehe...\x02",
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
            "#5P#N#5S#20AMuahahahaha!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(300)

    ChrTalk(
        0x101,
        "#6P#00010FUgh, w-what the...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10110FOur attacks have no\x01",
            "effect on him at all!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#6P#02705FE-Eeeeek!\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    BeginChrThread(0x9, 3, 0, 7)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x9,
        "#10A#5P#4S#10AWAAAAAAAAH...!!\x02",
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
            "#5P#NMy, my. Allowing you to\x01",
            "leave just wouldn't do.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#5P#NThis isn't state\x01",
            "congress, after all.\x07\x00\x02",
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

    def lambda_2448():
        OP_95(0xFE, 0, -1400, -5000, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2448)
    WaitChrThread(0x9, 1)
    OP_64(0x9)
    OP_52(0x9, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x9, 0x2F)
    SetChrSubChip(0x9, 0x0)
    OP_82(0xC8, 0xC8, 0xBB8, 0x3E8)
    Sound(204, 0, 100, 0)
    Sound(833, 0, 100, 0)

    def lambda_2499():
        OP_A6(0xFE, 0x32, 0x32, 0xBB8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_2499)

    def lambda_24B2():
        OP_9D(0xFE, 0x514, 0xFFFFFA88, 0xFFFFE4A8, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_24B2)

    ChrTalk(
        0x9,
        "#4S#11P#12AGah!\x02",
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

    def lambda_2527():
        OP_93(0x101, 0xB4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2527)
    Sleep(0)

    def lambda_2537():
        OP_93(0x109, 0xB4, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2537)
    Sleep(0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x109, 0)
    OP_0D()

    ChrTalk(
        0x109,
        "#5P#10107FAhh...!?\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x0, 0x1F4)

    ChrTalk(
        0x101,
        "#6P#00010FErnest! You...!\x02",
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

    def lambda_25E7():
        OP_93(0xFE, 0x0, 0x2BC)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_25E7)
    SetMessageWindowPos(60, 80, -1, -1)

    AnonymousTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#5P#NDon't worry. He's still\x01",
            "useful, so I just\x01",
            "knocked him out.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#5P#NStill... Are you really in\x01",
            "the position to be worrying\x01",
            "about others right now?\x07\x00\x02",
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
        "#6P#00010FGuh!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10107FT-This is...\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(60, 80, -1, -1)

    AnonymousTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#5P#NHehe. This cult lodge\x01",
            "was built atop a septium\x01",
            "vein...\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#5P#NBy awakening here, I may\x01",
            "be able to open the door\x01",
            "to "D"...\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#5P#NJust as my master told\x01",
            "me. Hahaha!\x07\x00\x02",
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
        "#N#10105FN-No way...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#N#00010FTch... This is just like\x01",
            "with Joachim!\x02",
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
            "#60WHAHA... THIS IS THE\x01",
            "STATE MY MASTER\x01",
            "ATTAINED...\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xB),
            "#60WWITH THIS, I'LL BE ABLE\x01",
            "TO FORESEE EVERYTHING...\x02",
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
            "#60W...?...\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xB),
            "#60W...WHY?... ...WHY DON'T\x01",
            "I SEE ANYTHING?...\x02",
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
        "#00005F#12P...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10101F#12PS-Something's wrong...\x02",
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
            "#60W...WHY?... WHY CAN'T I\x01",
            "SEE "D"...!?\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xB),
            "#60WWHY CAN I NOT FEEL THE\x01",
            "BREATH OF THE TRUE GOD!?\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xB),
            "#60WTHIS IS NOT WHAT I HAVE\x01",
            "BEEN TOLD!!\x02",
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
            "#12P#00010FTch... Hang in there!\x02\x03",
            "#00007FWhat if everything\x01",
            "Joachim told you were\x01",
            "lies!?\x02",
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
            "#60W#4SS-SILENCE! SILENCE!\x01",
            "SILEEEEEENCE...!!\x02",
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
            "#60WWHATEVER... FIRST, I'LL\x01",
            "JUST SACRIFICE YOU...\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xB),
            "#60WTHEN I'LL RETURN TO\x01",
            "CROSSBELL AND CLAIM ELIE\x01",
            "AND THE DIVINE CHILD!!\x02",
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
        "#12P#00010FY-you bastard!\x02",
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x109,
        "#10107FLloyd! Watch out!\x02",
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
        "#00010FGuh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10110FWhat a monster...\x02",
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
            "#60WHEHEHE, FAREWELL THEN.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xB),
            "#60WYOU PATHETIC LITTLE PILE\x01",
            "OF REGRETS!\x02",
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
        "#4S#8A#6PHaaaaaaa!\x02",
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
            "#4SWHA...!?\x02",
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
            "#4S#15AARGHHH...!?\x02",
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

    def lambda_37EF():
        OP_95(0xFE, 2100, 200, 23400, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_37EF)
    OP_0D()
    SetChrChipByIndex(0x108, 0x25)
    SetChrSubChip(0x108, 0x1)
    Sound(809, 0, 50, 0)

    def lambda_3818():
        OP_9D(0xFE, 0xFFFFFED4, 0xC8, 0x607C, 0x1F4, 0xFA0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_3818)
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
        "#5P#10102FAh!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002FDudley, Arios!\x02",
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
            "#6P#00604FGood grief... Just in\x01",
            "time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#01402FLloyd, Sergeant Major\x01",
            "Noｱl. Good work holding\x01",
            "out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#5PI could say the same\x01",
            "about you two. I'm really\x01",
            "glad you're alright!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#6P#00606FHmph. We had a hard time\x01",
            "with those 10 archaisms.\x02\x03",
            "#00601FWe'll talk later! We\x01",
            "need to disable him\x01",
            "first!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#01407FThis is no common enemy!\x01",
            "Give it everything\x01",
            "you've got!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3A38():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3A38)

    def lambda_3A51():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_3A51)
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
        "#00007F#5P#4SYes, sir!\x02",
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

    # Function_6_1DBA end

    def Function_7_3B97(): pass

    label("Function_7_3B97")

    ClearChrFlags(0x9, 0x4)

    def lambda_3BA1():
        OP_95(0xFE, -3300, 200, 18500, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3BA1)
    WaitChrThread(0x9, 1)

    def lambda_3BBF():
        OP_95(0xFE, 0, 200, 13500, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3BBF)
    WaitChrThread(0x9, 1)

    def lambda_3BDD():
        OP_95(0xFE, 0, -1400, -5500, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3BDD)
    WaitChrThread(0x9, 1)
    Return()

    # Function_7_3B97 end

    def Function_8_3BF7(): pass

    label("Function_8_3BF7")

    OP_74(0x0, 0xA)
    OP_71(0x0, 0x209, 0x230, 0x0, 0x0)
    OP_79(0x0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x231, 0x258, 0x0, 0x20)
    Return()

    # Function_8_3BF7 end

    def Function_9_3C1B(): pass

    label("Function_9_3C1B")

    OP_74(0x0, 0x14)
    OP_71(0x0, 0x4BA, 0x4CE, 0x0, 0x0)
    OP_79(0x0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0xA, 0x31, 0x0, 0x20)
    Return()

    # Function_9_3C1B end

    def Function_10_3C3F(): pass

    label("Function_10_3C3F")

    Sound(831, 0, 100, 0)
    OP_70(0x0, 0x44D)
    OP_71(0x0, 0x44D, 0x460, 0x0, 0x0)
    OP_79(0x0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x460, 0x488, 0x0, 0x20)
    Return()

    # Function_10_3C3F end

    def Function_11_3C69(): pass

    label("Function_11_3C69")

    OP_70(0x0, 0x438)
    OP_74(0x0, 0xA)
    ClearMapObjFlags(0x0, 0x20)
    OP_71(0x0, 0x42A, 0x441, 0x0, 0x0)
    OP_79(0x0)
    OP_70(0x0, 0x441)
    Return()

    # Function_11_3C69 end

    def Function_12_3C8B(): pass

    label("Function_12_3C8B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3CAF")
    OP_82(0x32, 0x32, 0xBB8, 0x2710)
    Sleep(10000)
    Jump("Function_12_3C8B")

    label("loc_3CAF")

    Return()

    # Function_12_3C8B end

    def Function_13_3CB0(): pass

    label("Function_13_3CB0")

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

    # Function_13_3CB0 end

    def Function_14_3EA6(): pass

    label("Function_14_3EA6")

    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(700)
    SetChrChipByIndex(0x101, 0x28)
    SetChrSubChip(0x101, 0x2)
    Sound(809, 0, 80, 0)

    def lambda_3ED4():
        OP_9D(0xFE, 0xFFFFFD44, 0xC8, 0x5DC0, 0x190, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3ED4)
    WaitChrThread(0x101, 1)
    Sound(326, 0, 40, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    Sleep(700)
    SetChrChipByIndex(0x101, 0x28)
    SetChrSubChip(0x101, 0x0)

    def lambda_3F0E():
        OP_A6(0xFE, 0x32, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3F0E)
    Return()

    # Function_14_3EA6 end

    def Function_15_3F23(): pass

    label("Function_15_3F23")

    SetChrChipByIndex(0x109, 0x29)
    SetChrSubChip(0x109, 0x0)
    SetChrFlags(0x109, 0x20)
    SetChrFlags(0x109, 0x1000)

    def lambda_3F3A():
        OP_96(0xFE, 0x2BC, 0xC8, 0x5BCC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3F3A)

    def lambda_3F54():
        OP_A6(0xFE, 0x32, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_3F54)
    WaitChrThread(0x109, 1)
    ClearChrFlags(0x109, 0x20)
    ClearChrFlags(0x109, 0x1000)
    SetChrChipByIndex(0x109, 0x30)
    SetChrSubChip(0x109, 0x0)
    Return()

    # Function_15_3F23 end

    def Function_16_3F7F(): pass

    label("Function_16_3F7F")

    SetChrPos(0x108, 0, 200, 8000, 0)
    SetChrFlags(0x108, 0x1000)
    SetChrChipByIndex(0x108, 0x25)
    SetChrSubChip(0x108, 0x0)
    SetChrChip(0x0, 0x108, 0x32, 0x12C)
    Sound(250, 0, 100, 0)

    def lambda_3FB0():
        OP_95(0xFE, 0, 200, 19500, 10000, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_3FB0)
    WaitChrThread(0x108, 1)
    Sound(251, 0, 100, 0)

    def lambda_3FD4():
        OP_9D(0xFE, 0xFA0, 0xC8, 0x6338, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_3FD4)
    WaitChrThread(0x108, 1)
    Sound(326, 0, 100, 0)
    SetChrChipByIndex(0x108, 0x2B)
    SetChrSubChip(0x108, 0x2)
    Sound(844, 0, 100, 0)

    def lambda_4009():
        OP_9D(0xFE, 0xFFFFFE0C, 0xC8, 0x68B0, 0x7D0, 0xFA0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_4009)
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

    # Function_16_3F7F end

    def Function_17_40E6(): pass

    label("Function_17_40E6")

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

    # Function_17_40E6 end

    def Function_18_433A(): pass

    label("Function_18_433A")

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

    # Function_18_433A end

    def Function_19_4387(): pass

    label("Function_19_4387")

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
            "#4S#20A#60WOOOOOOOOH...!\x07\x00\x02",
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
        "#01401F#5PMmm....!\x02",
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
            "#00007F#3314V#30W#5P#4S#16A...It's coming! Watch\x01",
            "out!\x02",
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
        "#10110F#5P#6A!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        "#00610F#5P#6ATch!\x02",
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
            "#4S#60W#20AAAAAAAAAAH...!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(800)

    ChrTalk(
        0x101,
        "#00010F#N#6PThat's...!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x109,
        "#10110F#N#6PIs he... m-melting!?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x10A,
        (
            "#00610F#N#6PIt's just like in\x01",
            "Joachim's death\x01",
            "report...!\x02",
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
            "#60W#20AAAAAAAAA....\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    AnonymousTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#60W#30A...NOOOOO....\x01",
            "#4SNOOOOOOOOO!!\x02",
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
            "#60W#35AI DON'T WANT TO DIE...\x01",
            "#4S...DON'T...WANT...TO...DIIIE...!\x07\x00\x02",
        )
    )

    Sleep(1000)
    OP_82(0xC8, 0x0, 0xBB8, 0x3E8)
    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    def lambda_5229():
        OP_93(0x101, 0x0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_5229)
    Sleep(0)

    def lambda_5239():
        OP_93(0x109, 0x0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_5239)
    Sleep(0)

    def lambda_5249():
        OP_93(0x10A, 0x0, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_5249)
    Sleep(0)

    def lambda_5259():
        OP_93(0x108, 0x0, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 0, lambda_5259)
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
        "#10108F......\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        "#01403F...How pitiful.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00010FGuh!\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)

    def lambda_52F5():
        OP_95(0xFE, 0, 200, 27500, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_52F5)
    OP_68(0, 2000, 32299, 2000)
    MoveCamera(0, 3, 0, 2000)
    SetCameraDistance(16500, 2000)
    OP_6F(0x79)
    SetCameraDistance(14890, 30000)

    ChrTalk(
        0x109,
        "#10105F#N#12PLloyd!?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x10A,
        "#00607F#N#12PHey, what're you...!?\x02",
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
            "#6P#00007FErnest! Pull yourself\x01",
            "together!\x02\x03",
            "You can't give up here!\x01",
            "You're still yourself,\x01",
            "right!?\x02",
        )
    )

    CloseMessageWindow()
    Sound(1005, 0, 100, 0)
    SetMessageWindowPos(-1, 70, -1, -1)

    AnonymousTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#60W#20A...ARGHHH...\x01",
            "...UGHHH...?\x07\x00\x02",
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
            "#6P#00010FYou didn't take the same\x01",
            "large dose of red Gnosis\x01",
            "Joachim did!\x02\x03",
            "#00007FThere's still hope for\x01",
            "you! Don't give up now!\x02",
        )
    )

    CloseMessageWindow()
    Sound(1005, 0, 100, 0)
    SetMessageWindowPos(-1, 70, -1, -1)

    AnonymousTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#60W#20AARGH... GEHUHU...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(300)

    ChrTalk(
        0x10A,
        "#00600F#N#12PBannings, you...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x109,
        "#10108F#N#12P...Lloyd...\x02",
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
            "#60WUUUH... AAH...\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#60W...W-WHY...\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#60WWHY GO S-SO FAR...\x01",
            "...FOR... SOMEONE LIKE\x01",
            "ME...\x07\x00\x02",
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
            "#00006F...That's irrelevant here.\x02\x03",
            "#00008FSure, you did commit\x01",
            "crimes.\x02\x03",
            "But still, even if you did,\x01",
            "that's no reason to just\x01",
            "let you die down here.\x02\x03",
            "#00013FAlso, I'm sure Elie and\x01",
            "Chairman MacDowell would be\x01",
            "saddened by your death.\x02",
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
            "#00007FSo please... Pull\x01",
            "yourself together!\x02",
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
            "#60W...ELIE... CHAIRMAN\x01",
            "MACDOWELL...\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#60W...I'M SORRY... HOW\x01",
            "COULD I...\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#60W#25A...URGH...\x01",
            "...AAAAAAAAAH!\x07\x00\x02",
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
        "#00010F#5P...Ugh! It didn't work!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10113F#5P#NI-Isn't there anything\x01",
            "we can do about this!?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x10A,
        (
            "#00610FTch. You know cases like\x01",
            "this are outside my areas\x01",
            "of expertise, right!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#01400F#5P#NNo...\x02\x03",
            "#01404FBut it seems like the\x01",
            "real expert has arrived\x01",
            "just in time...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopBGM(0x1388)
    TurnDirection(0x10A, 0x108, 500)

    ChrTalk(
        0x10A,
        "#00605F#6PWhat...\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xC, 0x80)
    Sleep(300)

    NpcTalk(
        0xC,
        "Youth's Voice",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#40W#25AO Aidios, who art high\x01",
            "in heaven.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xC,
        "Youth's Voice",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#40W#30AWith thine light, return\x01",
            "home this lost lamb who\x01",
            "was drawn to evil...\x02",
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

    def lambda_5C9C():
        OP_93(0x101, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_5C9C)
    Sleep(50)

    def lambda_5CAC():
        OP_93(0x109, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_5CAC)
    Sleep(50)

    def lambda_5CBC():
        OP_93(0x10A, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_5CBC)
    Sleep(50)

    def lambda_5CCC():
        OP_93(0x108, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x108, 0, lambda_5CCC)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x10A, 0)
    WaitChrThread(0x108, 0)

    ChrTalk(
        0x101,
        "#12P#00005FHuh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10105FA Testaments verse...?\x02",
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

    def lambda_5D74():
        OP_95(0xFE, 0, 200, 16000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_5D74)

    def lambda_5D8E():

        label("loc_5D8E")

        TurnDirection(0xFE, 0xC, 500)
        Yield()
        Jump("loc_5D8E")

    QueueWorkItem2(0x101, 2, lambda_5D8E)

    def lambda_5DA0():

        label("loc_5DA0")

        TurnDirection(0xFE, 0xC, 500)
        Yield()
        Jump("loc_5DA0")

    QueueWorkItem2(0x109, 2, lambda_5DA0)

    def lambda_5DB2():

        label("loc_5DB2")

        TurnDirection(0xFE, 0xC, 500)
        Yield()
        Jump("loc_5DB2")

    QueueWorkItem2(0x10A, 2, lambda_5DB2)

    def lambda_5DC4():

        label("loc_5DC4")

        TurnDirection(0xFE, 0xC, 500)
        Yield()
        Jump("loc_5DC4")

    QueueWorkItem2(0x108, 2, lambda_5DC4)
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
        "#00605FYou're...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#04303FAhh, sorry. We're kinda\x01",
            "running out of time. Treatment\x01",
            "first, introductions later.\x02\x03",
            "#04300FMind standing aside?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FEh, ah... Yes, please go\x01",
            "ahead!\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(15000, 1500)

    def lambda_5F29():
        OP_95(0xFE, 0, 200, 27600, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_5F29)
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

    def lambda_5FEE():
        OP_96(0xFE, 0x1F4, 0xC8, 0x5BCC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5FEE)
    Sleep(300)

    def lambda_600B():
        OP_96(0xFE, 0xFFFFFE0C, 0xC8, 0x61A8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_600B)
    WaitChrThread(0xC, 1)
    SetMessageWindowPos(250, 70, -1, -1)

    AnonymousTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "GGGGAAHHH...\x01",
            "...URGGGGGGH...!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0xC,
        (
            "#6P#04308FOne step short of gone,\x01",
            "huh.\x02\x03",
            "#04304F...It looks like you\x01",
            "held out somehow,\x01",
            "though.\x02\x03",
            "#04301FIn that case...\x02",
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
            "#5P#04303F#50W#25AAzure seal of mine\x01",
            "shining from the abyss.\x02",
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
            "#5P#04301F#50W#30ASweep away the miasma with\x01",
            "light, and guide this lost\x01",
            "lamb toward salvation!\x02",
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

    def lambda_6379():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_6379)
    Sleep(30)

    def lambda_6389():
        OP_93(0x10A, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_6389)
    Sleep(30)

    def lambda_6399():
        OP_93(0x109, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_6399)
    Sleep(30)

    def lambda_63A9():
        OP_93(0x108, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x108, 0, lambda_63A9)
    Sleep(30)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x10A, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x108, 0)
    OP_6F(0x79)
    Sleep(500)

    ChrTalk(
        0x101,
        "#00005F#30W#N#6P#12AT-That's...\x02",
    )

    Sleep(2000)

    ChrTalk(
        0x10A,
        (
            "#00605F#30W#N#6P#15AWhat in the world is\x01",
            "that light...\x02",
        )
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

    def lambda_64E6():
        TurnDirection(0x101, 0x8, 0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_64E6)
    Sleep(0)

    def lambda_64F6():
        TurnDirection(0x109, 0x8, 0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_64F6)
    Sleep(0)

    def lambda_6506():
        TurnDirection(0x10A, 0x8, 0)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_6506)
    Sleep(0)

    def lambda_6516():
        TurnDirection(0x108, 0x8, 0)
        ExitThread()

    QueueWorkItem(0x108, 0, lambda_6516)
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
        "#10102F#30W#N#6PAh...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        "#00002F#30W#N#6PH-He's back!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xC,
        "#04306F#30W#5PPhew...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    def lambda_65AA():
        OP_95(0xFE, 0, 200, 29300, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_65AA)
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

    def lambda_65F4():
        OP_96(0xFE, 0xFFFFFF38, 0xC8, 0x6A40, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_65F4)
    Sleep(200)

    def lambda_6611():
        OP_96(0xFE, 0xC8, 0xC8, 0x6464, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6611)
    Sleep(200)

    def lambda_662E():
        TurnDirection(0xFE, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_662E)

    def lambda_663B():
        OP_96(0xFE, 0x76C, 0xC8, 0x6720, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_663B)
    Sleep(200)

    def lambda_6658():
        TurnDirection(0xFE, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_6658)

    def lambda_6665():
        OP_96(0xFE, 0xFFFFF894, 0xC8, 0x6590, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_6665)
    WaitChrThread(0x101, 1)
    Sleep(800)

    ChrTalk(
        0x101,
        "#00013F#6PH-How is he?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#04304FOh, he just fainted.\x02\x03",
            "#04300FHe's not gonna wake up for a couple\x01",
            "of days, but it's not as if his\x01",
            "life's on the line or anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#6PT-Thank goodness...\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x109, 1)
    WaitChrThread(0x10A, 1)
    WaitChrThread(0x108, 1)

    ChrTalk(
        0x109,
        "#6P#10112FPhew... That's a relief.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#6P#00607FT-That aside, who the hell\x01",
            "are you!?\x02\x03",
            "You do seem like a priest\x01",
            "though... What are you doing\x01",
            "in a place like this!?\x02",
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
            "#11P#04305FEh? Arios...\x02\x03",
            "You didn't even tell\x01",
            "them about me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#01404FHeh. You told me you\x01",
            "weren't sure whether you\x01",
            "could make it in time.\x02\x03",
            "#01402FMy position being what\x01",
            "it is, I kept it from\x01",
            "them, just in case.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11P#04304FOhh, I see. Thanks!\x02\x03",
            "#04311FYou haven't changed one\x01",
            "bit, still as thoughtful\x01",
            "as ever!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#01404FThe same could be said\x01",
            "about you.\x02\x03",
            "#01402FThank you. You really\x01",
            "saved us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00011F#6PUhmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#6P#00606FHmph. So you're some kind of insurance.\x02\x03",
            "#00600FI assume you're a member of the\x01",
            "Gralsritter, part of the Congregation of\x01",
            "the Sacraments of the Septian Church.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#3P#10105FGralsritter?\x01",
            "Congregation for the\x01",
            "what...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F#6PYou mean the ones tasked\x01",
            "with the retrieval of\x01",
            "Artifacts?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 500)
    Sleep(150)

    ChrTalk(
        0xC,
        "#11P#04304FHaha, bingo!\x02",
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
            "Pleased to meetcha! The name's\x01",
            "Kevin Graham, member of the Septian\x01",
            "Church's Gralsritter.\x02\x03",
            "Arios here contacted me and asked\x01",
            "me to come down.\x02\x03",
            "Pleased to make your acquaintance.\x02",
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

    # Function_19_4387 end

    def Function_20_6C9F(): pass

    label("Function_20_6C9F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6CCB")
    SetChrSubChip(0xC, 0x0)
    Sleep(100)
    SetChrSubChip(0xC, 0x1)
    Sleep(100)
    SetChrSubChip(0xC, 0x2)
    Sleep(100)
    SetChrSubChip(0xC, 0x3)
    Sleep(100)
    Jump("Function_20_6C9F")

    label("loc_6CCB")

    Return()

    # Function_20_6C9F end

    def Function_21_6CCC(): pass

    label("Function_21_6CCC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6CF0")
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)
    Sleep(500)
    Jump("Function_21_6CCC")

    label("loc_6CF0")

    Return()

    # Function_21_6CCC end

    def Function_22_6CF1(): pass

    label("Function_22_6CF1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6D15")
    OP_82(0x32, 0x32, 0xBB8, 0x1F4)
    Sleep(500)
    Jump("Function_22_6CF1")

    label("loc_6D15")

    Return()

    # Function_22_6CF1 end

    def Function_23_6D16(): pass

    label("Function_23_6D16")

    SetChrChipByIndex(0x101, 0x29)
    SetChrSubChip(0x101, 0x2)
    Sound(844, 0, 100, 0)

    def lambda_6D29():
        OP_9D(0xFE, 0xFFFFFC18, 0xC8, 0x5014, 0x190, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6D29)
    WaitChrThread(0x101, 1)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    Return()

    # Function_23_6D16 end

    def Function_24_6D4E(): pass

    label("Function_24_6D4E")

    SetChrChipByIndex(0x109, 0x31)
    SetChrSubChip(0x109, 0x2)
    Sound(809, 0, 100, 0)

    def lambda_6D61():
        OP_9D(0xFE, 0x5DC, 0xC8, 0x4A38, 0x190, 0xBB8)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6D61)
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

    # Function_24_6D4E end

    def Function_25_7128(): pass

    label("Function_25_7128")

    SetChrFlags(0x10A, 0x20)

    def lambda_7132():
        OP_93(0xFE, 0x13B, 0x2BC)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_7132)
    SetChrChipByIndex(0x10A, 0x32)
    SetChrSubChip(0x10A, 0x0)

    def lambda_7147():
        OP_9D(0xFE, 0xDAC, 0xC8, 0x4F4C, 0x190, 0xBB8)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_7147)
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

    # Function_25_7128 end

    def Function_26_7291(): pass

    label("Function_26_7291")

    SetChrFlags(0x108, 0x20)

    def lambda_729B():
        OP_93(0xFE, 0x3C, 0x2BC)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_729B)
    SetChrChipByIndex(0x108, 0x25)
    SetChrSubChip(0x108, 0x3)

    def lambda_72B0():
        OP_9D(0xFE, 0xFFFFF060, 0xC8, 0x526C, 0x190, 0xBB8)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_72B0)
    WaitChrThread(0x108, 1)
    Sound(540, 0, 100, 0)
    SetChrChipByIndex(0x108, 0x24)
    SetChrSubChip(0x108, 0x0)
    Sleep(100)
    Sound(881, 0, 100, 0)
    PlayEffect(0x4, 0x1, 0x108, 0x5, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_731F():
        OP_A6(0xFE, 0x32, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_731F)
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

    # Function_26_7291 end

    def Function_27_73E2(): pass

    label("Function_27_73E2")


    def lambda_73E7():
        OP_96(0xFE, 0x0, 0xC8, 0x5B68, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_73E7)
    Sleep(100)

    def lambda_7404():
        OP_96(0xFE, 0x7D0, 0xC8, 0x5E88, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_7404)
    Sleep(100)

    def lambda_7421():
        OP_96(0xFE, 0xFFFFF830, 0xC8, 0x5E88, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_7421)
    Return()

    # Function_27_73E2 end

    def Function_28_7437(): pass

    label("Function_28_7437")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7450")
    Sound(892, 0, 50, 0)
    Sleep(1150)
    Jump("Function_28_7437")

    label("loc_7450")

    Return()

    # Function_28_7437 end

    def Function_29_7451(): pass

    label("Function_29_7451")

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

    # Function_29_7451 end

    def Function_30_74BD(): pass

    label("Function_30_74BD")

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

    # Function_30_74BD end

    def Function_31_74FD(): pass

    label("Function_31_74FD")

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

    # Function_31_74FD end

    def Function_32_753D(): pass

    label("Function_32_753D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7556")
    Sound(934, 0, 60, 0)
    Sleep(1500)
    Jump("Function_32_753D")

    label("loc_7556")

    Return()

    # Function_32_753D end

    def Function_33_7557(): pass

    label("Function_33_7557")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7570")
    Sound(1034, 0, 100, 0)
    Sleep(1000)
    Jump("Function_33_7557")

    label("loc_7570")

    Return()

    # Function_33_7557 end

    def Function_34_7571(): pass

    label("Function_34_7571")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_758A")
    Sound(1034, 0, 50, 0)
    Sleep(1000)
    Jump("Function_34_7571")

    label("loc_758A")

    Return()

    # Function_34_7571 end

    def Function_35_758B(): pass

    label("Function_35_758B")

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

    # Function_35_758B end

    def Function_36_75F9(): pass

    label("Function_36_75F9")

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

    # Function_36_75F9 end

    def Function_37_7667(): pass

    label("Function_37_7667")

    OP_71(0x1, 0x119, 0x136, 0x0, 0x0)
    OP_79(0x1)
    Sound(831, 0, 100, 0)
    Sound(830, 0, 50, 0)
    OP_71(0x1, 0x384, 0x38E, 0x0, 0x0)
    OP_79(0x1)
    OP_71(0x1, 0x38F, 0x3B6, 0x0, 0x20)
    Return()

    # Function_37_7667 end

    SaveToFile()

Try(main)
