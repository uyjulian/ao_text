from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "m9082.bin",                # FileName
        "m9082",                    # MapName
        "m9082",                    # Location
        0x00C3,                     # MapIndex
        "ed7356",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x2A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 195, 0, 0, 0, 1],
    )

    BuildStringList((
        "m9082",                  # 0
        "Arios",                  # 1
        "台詞表示用ダミーキャラ", # 2
        "Arios' Companion",       # 3
        "Arios' Companion",       # 4
        "エフェクト表示用ダミーキャラ",# 5
        "bm9069",                 # 6
    ))

    ATBonus("ATBonus_1D8", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_298", 8, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_29C", 3, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_2A0", 13, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_2A4", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2A8", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2AC", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2B0", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2B4", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_278", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_27C", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_280", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_284", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_288", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_28C", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_290", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_294", 5, 5, 45)

    # monster count: 0

    # event battle count: 1

    BattleInfo(
        "BattleInfo_2B8", 0x0042, 255, 6, 45, 3, 3, 30, 0, "bm9069", 0x00000000, 100, 0, 0, 0,
        (
            ("ms02401.dat", "ms85401.dat", "ms85501.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_298", "MonsterBattlePostion_278", "ed7527", "ed7453", "ATBonus_1D8"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "apl/ch51744.itc",                   # 00
    ))

    DeclNpc(0,       12000,   211500,  180,  389,  0x0, 0,   0,   0,   255, 255, 0,   2,   255,  0)
    DeclNpc(0,       0,       0,       0,    508,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       13100,   204699,  305,  508,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 9,   0.0,                   185.0,                 11.0,                  225.0,                 [0.20000000298023224,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.1666666716337204,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.0,                  -30.83333396911621,    -2.200000047683716,    1.0])

    DeclActor(3500,    0,       155000,  1200,    3500,    1000,    155000,  0x007C, 0,  3,  0x0000)

    ChipFrameInfo(940, 0)                                        # 0

    ScpFunction((
        "Function_0_3AC",          # 00, 0
        "Function_1_3F8",          # 01, 1
        "Function_2_517",          # 02, 2
        "Function_3_7BD",          # 03, 3
        "Function_4_8B1",          # 04, 4
        "Function_5_B35",          # 05, 5
        "Function_6_C88",          # 06, 6
        "Function_7_CE9",          # 07, 7
        "Function_8_D4A",          # 08, 8
        "Function_9_D5D",          # 09, 9
        "Function_10_5F82",        # 0A, 10
        "Function_11_5FAD",        # 0B, 11
        "Function_12_5FD8",        # 0C, 12
        "Function_13_6003",        # 0D, 13
        "Function_14_602E",        # 0E, 14
        "Function_15_6059",        # 0F, 15
        "Function_16_607D",        # 10, 16
        "Function_17_608F",        # 11, 17
        "Function_18_60A1",        # 12, 18
        "Function_19_60B3",        # 13, 19
        "Function_20_60BF",        # 14, 20
        "Function_21_610D",        # 15, 21
        "Function_22_615B",        # 16, 22
        "Function_23_6184",        # 17, 23
        "Function_24_61CE",        # 18, 24
        "Function_25_61FB",        # 19, 25
        "Function_26_6227",        # 1A, 26
        "Function_27_624A",        # 1B, 27
        "Function_28_6293",        # 1C, 28
        "Function_29_62DC",        # 1D, 29
        "Function_30_62F8",        # 1E, 30
        "Function_31_636C",        # 1F, 31
        "Function_32_7FC5",        # 20, 32
        "Function_33_800E",        # 21, 33
        "Function_34_8078",        # 22, 34
        "Function_35_88F0",        # 23, 35
        "Function_36_8900",        # 24, 36
        "Function_37_890F",        # 25, 37
        "Function_38_8921",        # 26, 38
        "Function_39_8933",        # 27, 39
        "Function_40_893F",        # 28, 40
        "Function_41_898D",        # 29, 41
        "Function_42_89DB",        # 2A, 42
        "Function_43_8A02",        # 2B, 43
    ))


    def Function_0_3AC(): pass

    label("Function_0_3AC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3BD")
    Event(0, 4)

    label("loc_3BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_3D1")
    ClearScenarioFlags(0x22, 0)
    Event(0, 31)
    Jump("loc_3F7")

    label("loc_3D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_3E5")
    ClearScenarioFlags(0x22, 1)
    Event(0, 34)
    Jump("loc_3F7")

    label("loc_3E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3F7")
    Event(0, 8)

    label("loc_3F7")

    Return()

    # Function_0_3AC end

    def Function_1_3F8(): pass

    label("Function_1_3F8")

    OP_F0(0x1, 0x320)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_414")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_414")

    OP_1B(0x1, 0x0, 0x5)
    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_431")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_431")

    OP_52(0x8, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapObjFlags(0x2, 0x1000)
    ClearMapObjFlags(0x2, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_4BE")
    SetMapObjFlags(0x2, 0x4)
    SetMapObjFrame(0xFF, "magi10_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "magi11_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "point_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "magi_04_add", 0x0, 0x1)
    OP_70(0x1, 0x96)
    Jump("loc_50A")

    label("loc_4BE")

    SetMapObjFrame(0xFF, "magi10_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "magi11_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "point_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "magi_04_add", 0x1, 0x1)
    OP_70(0x1, 0x3C)

    label("loc_50A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_516")
    Call(0, 42)

    label("loc_516")

    Return()

    # Function_1_3F8 end

    def Function_2_517(): pass

    label("Function_2_517")

    SetChrFlags(0x8, 0x10)
    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CF, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_77D")

    ChrTalk(
        0x8,
        "...............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001F...He's completely lost\x01",
            "consciousness. His life doesn't\x01",
            "seem to be in danger either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FAs expected, he was one hell of\x01",
            "an opponent... To think he did\x01",
            "that much against all of us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00208FAs expected of the\x01",
            "Divine Blade of Wind...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_673")

    ChrTalk(
        0x10A,
        "#00603FHmph... I'm glad we won.\x02",
    )

    CloseMessageWindow()

    label("loc_673")


    ChrTalk(
        0x101,
        (
            "#00003FShizuku is probably worried. I'd\x01",
            "like to take him back to the\x01",
            "Merkabah immediately, but...\x02\x03",
            "#00001F...Mariabell and Lawyer Ian are\x01",
            "waiting for us ahead.\x02\x03",
            "#00003FI feel sorry for him, but let's\x01",
            "carry him back later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FRight... Let's go.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1CF, 0)
    Jump("loc_7B9")

    label("loc_77D")


    ChrTalk(
        0x8,
        "...............\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "He seems to be out cold.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_7B9")

    TalkEnd(0x8)
    Return()

    # Function_2_517 end

    def Function_3_7BD(): pass

    label("Function_3_7BD")

    OP_F4(0x2)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's an orbment charging station.\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Rest Here\x01",      # 0
            "Cancel\x01",         # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8A2")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_74(0x0, 0x1E)
    Sound(7, 0, 100, 0)
    OP_70(0x0, 0x0)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    OP_79(0x0)
    OP_71(0x0, 0x1F, 0x186, 0x0, 0x20)
    Sleep(1000)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    Sound(13, 0, 100, 0)
    OP_0D()
    OP_32(0xFF, 0xFE, 0x0)
    OP_6A(0x0, 0x0)
    OP_31(0x1)
    Sleep(3500)
    OP_70(0x0, 0x0)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_8A2")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_3_7BD end

    def Function_4_8B1(): pass

    label("Function_4_8B1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    LoadEffect(0x1, "event/ev202_00.eff")
    OP_68(-340, 13500, 219060, 0)
    MoveCamera(29, 41, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(12970, 0)
    SetChrPos(0x0, 0, 12000, 222000, 180)
    SetChrPos(0x1, 0, 12000, 222000, 180)
    SetChrPos(0x2, 0, 12000, 222000, 180)
    SetChrPos(0x3, 0, 12000, 222000, 180)
    OP_A7(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    Sound(920, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x0, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_9C1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_9C1)

    def lambda_9D2():
        OP_95(0xFE, -240, 12000, 218120, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_9D2)
    Sleep(500)
    PlayEffect(0x1, 0xFF, 0x1, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_A29():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_A29)

    def lambda_A3A():
        OP_95(0xFE, -1420, 12000, 218280, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_A3A)
    Sleep(500)
    Sound(920, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x2, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_A97():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2, 2, lambda_A97)

    def lambda_AA8():
        OP_95(0xFE, 1060, 12000, 218310, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_AA8)
    Sleep(500)
    PlayEffect(0x1, 0xFF, 0x3, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_AFF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x3, 2, lambda_AFF)

    def lambda_B10():
        OP_95(0xFE, -2780, 12000, 218680, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_B10)
    WaitChrThread(0x3, 1)
    Sleep(500)
    OP_E2(0x2)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_4_8B1 end

    def Function_5_B35(): pass

    label("Function_5_B35")

    EventBegin(0x0)
    OP_E2(0x3)
    LoadEffect(0x1, "event/evwarp.eff")
    Sound(936, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x0, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_B8E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_B8E)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0x1, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_BD9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_BD9)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0x2, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_C24():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2, 2, lambda_C24)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0x3, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_C6F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x3, 2, lambda_C6F)
    Sleep(1000)
    NewScene("m9008", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_5_B35 end

    def Function_6_C88(): pass

    label("Function_6_C88")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CA0")
    LoadChrToIndex("chr/ch03150.itc", 0x23)

    label("loc_CA0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CB8")
    LoadChrToIndex("chr/ch03250.itc", 0x23)

    label("loc_CB8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CD0")
    LoadChrToIndex("chr/ch02950.itc", 0x23)

    label("loc_CD0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CE8")
    LoadChrToIndex("chr/ch00950.itc", 0x23)

    label("loc_CE8")

    Return()

    # Function_6_C88 end

    def Function_7_CE9(): pass

    label("Function_7_CE9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D01")
    LoadChrToIndex("chr/ch03150.itc", 0x24)

    label("loc_D01")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D19")
    LoadChrToIndex("chr/ch03250.itc", 0x24)

    label("loc_D19")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D31")
    LoadChrToIndex("chr/ch02950.itc", 0x24)

    label("loc_D31")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D49")
    LoadChrToIndex("chr/ch00950.itc", 0x24)

    label("loc_D49")

    Return()

    # Function_7_CE9 end

    def Function_8_D4A(): pass

    label("Function_8_D4A")

    EventBegin(0x0)
    StopBGM(0xFA0)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    EventEnd(0x5)
    Return()

    # Function_8_D4A end

    def Function_9_D5D(): pass

    label("Function_9_D5D")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu01400.itp")
    LoadChrToIndex("apl/ch51233.itc", 0x1E)
    LoadChrToIndex("chr/ch00050.itc", 0x1F)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00250.itc", 0x21)
    LoadChrToIndex("chr/ch00350.itc", 0x22)
    Call(0, 6)
    Call(0, 7)
    LoadChrToIndex("chr/ch02450.itc", 0x25)
    LoadChrToIndex("monster/ch85450.itc", 0x26)
    LoadChrToIndex("monster/ch60051.itc", 0x27)
    LoadChrToIndex("monster/ch85550.itc", 0x28)
    LoadChrToIndex("monster/ch60051.itc", 0x29)
    LoadChrToIndex("apl/ch51743.itc", 0x2A)
    LoadEffect(0x0, "event/ev602_01.eff")
    LoadEffect(0x1, "event/eva06_02.eff")
    LoadEffect(0x2, "event/eva06_01.eff")
    LoadEffect(0x3, "event/ev17013.eff")
    SoundLoad(128)
    SoundLoad(825)
    SoundLoad(832)
    SoundLoad(881)
    SoundLoad(833)
    SoundLoad(4064)
    SoundLoad(4077)
    SoundLoad(4065)
    SoundLoad(4066)
    SoundLoad(4067)
    SetChrPos(0x101, 0, 25000, 181800, 0)
    SetChrPos(0x102, 1100, 25000, 181100, 0)
    SetChrPos(0x103, 200, 25000, 180000, 0)
    SetChrPos(0x104, -1100, 25000, 180750, 0)
    SetChrPos(0xF4, -650, 25000, 179250, 0)
    SetChrPos(0xF5, 850, 25000, 179000, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 0, 12000, 210000, 180)
    OP_52(0x8, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x9, 0x80)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x9, 0, 12000, 198500, 0)
    SetChrChipByIndex(0xA, 0x26)
    SetChrSubChip(0xA, 0x0)
    SetChrFlags(0xA, 0x20)
    OP_52(0xA, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0xA, -2500, 12000, 211500, 180)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    SetChrChipByIndex(0xB, 0x28)
    SetChrSubChip(0xB, 0x0)
    SetChrFlags(0xB, 0x20)
    OP_52(0xB, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0xB, 2500, 12000, 211500, 180)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    BeginChrThread(0xA, 2, 0, 29)
    BeginChrThread(0xB, 2, 0, 29)
    ClearChrFlags(0xC, 0x80)
    OP_68(0, 13000, 180500, 0)
    MoveCamera(0, 38, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(21000, 0)
    Sleep(500)
    OP_68(0, 13000, 188000, 4500)
    MoveCamera(0, 38, 0, 4500)
    OP_6E(600, 4500)
    SetCameraDistance(24000, 4500)
    FadeToBright(1000, 0)

    def lambda_1050():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1050)
    Sleep(50)

    def lambda_1068():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1068)
    Sleep(50)

    def lambda_1080():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1080)
    Sleep(50)

    def lambda_1098():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1098)
    Sleep(50)

    def lambda_10B0():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_10B0)
    Sleep(50)

    def lambda_10C8():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_10C8)
    OP_0D()
    Sleep(2400)
    OP_C9(0x0, 0x80000000)

    NpcTalk(
        0x8,
        "Man's Voice",
        "#4064V#6P#30W#16A─So you've arrived.\x02",
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
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
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    WaitChrThread(0xF5, 1)
    OP_6F(0x79)
    PlayBGM("ed7356", 0)
    BeginChrThread(0x101, 0, 0, 10)
    Sleep(50)
    BeginChrThread(0x102, 0, 0, 11)
    Sleep(50)
    BeginChrThread(0x103, 0, 0, 12)
    Sleep(50)
    BeginChrThread(0x104, 0, 0, 13)
    Sleep(50)
    BeginChrThread(0xF4, 0, 0, 14)
    Sleep(50)
    BeginChrThread(0xF5, 0, 0, 15)
    OP_68(-410, 13300, 205280, 4000)
    MoveCamera(47, 16, 0, 4000)
    OP_6E(600, 4000)
    SetCameraDistance(16180, 4000)
    OP_6F(0x79)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)

    ChrTalk(
        0x101,
        "#00001F#12P...Arios.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301F#12PYou're not wearin' that\x01",
            "secretary outfit\x01",
            "anymore...?\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x8,
        (
            "Although Mr. Crois requested it, it\x01",
            "was unnatural to me from the start.\x02\x03",
            "With the state independence\x01",
            "declaration of invalidity, I have\x01",
            "no need to wear to it.\x02\x03",
            "Think of me standing here...\x02\x03",
            "Neither as the Secretary of\x01",
            "Defense, nor as a bracer, but as a\x01",
            "mere ruffian fencer.\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1475")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1450")
    OP_FC(0xFFF4)
    Jump("loc_1453")

    label("loc_1450")

    OP_FC(0xC)

    label("loc_1453")


    ChrTalk(
        0x10A,
        "#00600F#13PMacLaine...\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_14BC")

    label("loc_1475")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_14BC")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_149F")
    OP_FC(0xFFF4)
    Jump("loc_14A2")

    label("loc_149F")

    OP_FC(0xC)

    label("loc_14A2")


    ChrTalk(
        0x109,
        "#10113F#13PArios...\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_14BC")


    ChrTalk(
        0x102,
        "#00108F#12PWhy are you...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00206F#12P...You're too honest.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00004F#12P...Haha, damn...\x02\x03",
            "#00008FI have so many things I want\x01",
            "to ask you that I can't decide\x01",
            "which to ask first, but...\x02\x03",
            "#00000FFirstly, do you mind answering\x01",
            "some of my questions?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01404FNo#5P─ That was my\x01",
            "intention from the\x01",
            "start.\x02\x03",
            "#01400FAsk away... I'll answer\x01",
            "every question, one by\x01",
            "one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003F#12PIn that case...\x02",
    )

    CloseMessageWindow()
    ClearScenarioFlags(0x0, 3)
    ClearScenarioFlags(0x0, 0)
    ClearScenarioFlags(0x0, 1)
    ClearScenarioFlags(0x0, 2)

    label("loc_1678")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E73")
    FadeToDark(300, 0, 100)
    OP_0D()
    MenuCmd(0, 0)
    MenuCmd(1, 0, "About the "accident" five years ago")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_16ED")
    MenuCmd(1, 0, "About Arios' relationship with Lawyer Ian")

    label("loc_16ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1719")
    MenuCmd(1, 0, "About KeA and the Black Auction")

    label("loc_1719")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_173C")
    MenuCmd(1, 0, "About the day guy died")

    label("loc_173C")

    MenuCmd(2, 0, -1, -1, 0)
    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1776"),
        (1, "loc_2616"),
        (2, "loc_3169"),
        (3, "loc_3E66"),
        (SWITCH_DEFAULT, "loc_3E6E"),
    )


    label("loc_1776")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2485")

    ChrTalk(
        0x101,
        (
            "#00008F#12P...I'm sorry to ask\x01",
            "about something so\x01",
            "painful, but...\x02\x03",
            "#00001FCould you tell me about\x01",
            "the "accident" five\x01",
            "years ago?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01403F#5PYes... No need to hide it anymore.\x02\x03",
            "#01400FThe truck explosion on a major street\x01",
            "five years ago...\x02\x03",
            "As you all have already realized, it\x01",
            "happened as a result of the intelligence\x01",
            "war between the Empire and Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00106F#12PAs we thought...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1ABC")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1937")
    OP_FC(0xFFF4)
    Jump("loc_193A")

    label("loc_1937")

    OP_FC(0xC)

    label("loc_193A")


    ChrTalk(
        0x10A,
        "#00608F#13P............\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x8,
        (
            "#01402F#5PHehe. Naturally, Section One knew the\x01",
            "truth, right?\x02\x03",
            "#01403FAccording to the judgment of police\x01",
            "leadership concerned with the Imperial\x01",
            "and Republican factions, it was\x01",
            "abandoned as a matter of course, but...\x02\x03",
            "#01400FEven if I was disappointed in that fact\x01",
            "itself, I now bear no grudge for that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#00606F#13P...There's nothing I can\x01",
            "say.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_1ABC")


    ChrTalk(
        0x103,
        (
            "#00208F#12P...And so Arios' wife\x01",
            "and Shizuku...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01403F#5PYes... Saya lost her life, while Shizuku\x01",
            "lost her sight.\x02\x03",
            "#01408FFive years have passed since then... With\x01",
            "the consolidation of both countries'\x01",
            "intelligence agencies, pointless\x01",
            "subversive activities have ceased, but...\x02\x03",
            "#01401FAs a result of many long years of secret\x01",
            "feuding, victims like Saya, Shizuku and\x01",
            "others have appeared in no small numbers.\x02\x03",
            "#01403FThat includes your parents, Lloyd, and\x01",
            "Mr. Grimwood's family as well.\x02",
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
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x101,
        "#00005F#12P#4S!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00307F#12PWhat the...!?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17C, 6)), scpexpr(EXPR_END)), "loc_1EB6")

    ChrTalk(
        0x102,
        (
            "#00101F#12PI-I'm sure that Lloyd's\x01",
            "parents...!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00208F#12PFifteen years ago, in an\x01",
            "airship accident...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#12PYeah... Just like I told\x01",
            "you before.\x02\x03",
            "#00008FI was young then, so I\x01",
            "barely remember it,\x01",
            "but...\x02\x03",
            "#00013FSo, back then... Lawyer\x01",
            "Ian's family was killed\x01",
            "too?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FF7")

    label("loc_1EB6")


    ChrTalk(
        0x102,
        "#00105F#12PY-Your parents!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#12P...This is the first\x01",
            "I've heard of this...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#12PMy parents... They passed away\x01",
            "when a newly commissioned airship\x01",
            "crashed with them onboard...\x02\x03",
            "#00008FI was young then, so I barely\x01",
            "remember it, but...\x02\x03",
            "#00013FSo, back then... Lawyer Ian's\x01",
            "family was killed too?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FF7")


    ChrTalk(
        0x8,
        (
            "#01403F#5PYes, I heard his wife and child\x01",
            "were onboard as well.\x02\x03",
            "I was left with Shizuku, but... I\x01",
            "can't even imagine his grief and\x01",
            "sorrow after having lost everyone.\x02\x03",
            "#01400FAlso, Guy and Mr. Grimwood met\x01",
            "each other then as fellow\x01",
            "bereaved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F#12P...............\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2162")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2138")
    OP_FC(0xFFF4)
    Jump("loc_213B")

    label("loc_2138")

    OP_FC(0xC)

    label("loc_213B")


    ChrTalk(
        0x109,
        "#10106F#13P...A-All that, huh...\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_2162")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_21C7")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_218C")
    OP_FC(0xFFF4)
    Jump("loc_218F")

    label("loc_218C")

    OP_FC(0xC)

    label("loc_218F")


    ChrTalk(
        0x10A,
        (
            "#00606F#13PEven Section One never\x01",
            "learned this...\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_21C7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2237")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_21F1")
    OP_FC(0xFFF4)
    Jump("loc_21F4")

    label("loc_21F1")

    OP_FC(0xC)

    label("loc_21F4")


    ChrTalk(
        0x105,
        (
            "#10401F#13P...I see. To think there\x01",
            "was such a connection...\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_2237")


    ChrTalk(
        0x8,
        (
            "#01403F#5P...Then, after the incident five years ago,\x01",
            "I retired from the police and knocked on the\x01",
            "door of the Bracer Guild.\x02\x03",
            "Disappointment towards the police, working\x01",
            "out a solution for Shizuku's hospitalization\x01",
            "costs... I had many reasons, but...\x02\x03",
            "#01408FSimply put, perhaps I was merely running\x01",
            "from the sorrow of having lost Saya.\x02\x03",
            "#01400FAfter all, if one wants to, he can immerse\x01",
            "himself in bracer work all he likes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008F#12PArios...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_247D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2427")
    OP_FC(0xFFF4)
    Jump("loc_242A")

    label("loc_2427")

    OP_FC(0xC)

    label("loc_242A")


    ChrTalk(
        0x106,
        (
            "#10706F#13P(...Even the families of\x01",
            "the targets Yin has\x01",
            "killed up to now...)\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_247D")

    SetScenarioFlags(0x0, 0)
    Jump("loc_2611")

    label("loc_2485")


    ChrTalk(
        0x8,
        (
            "#01403F#5PA truck explosion on a major\x01",
            "street five years ago that took\x01",
            "Saya's life and Shizuku's sight...\x02\x03",
            "#01401FIt happened as a result of an\x01",
            "intelligence war between the\x01",
            "Empire and the Republic.\x02\x03",
            "And the airship accident fifteen\x01",
            "years ago happened for the same\x01",
            "reason.\x02\x03",
            "#01403FAs a result... The lives of your\x01",
            "parents and Mr. Grimwood's family\x01",
            "were taken.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008F#12P...............\x02",
    )

    CloseMessageWindow()

    label("loc_2611")

    Jump("loc_3E6E")

    label("loc_2616")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3073")

    ChrTalk(
        0x101,
        (
            "#00006F#12P...I've had my doubts\x01",
            "about this, but...\x02\x03",
            "#00001FWhy did someone like\x01",
            "yourself decide to join\x01",
            "Dieter and the others?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        "#01405F#5POh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#12P...It's true that "uncle" and Mariabell are\x01",
            "knowledgeable in business, finance, and the\x01",
            "cult connected with the Crois clan, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F#12PThe unseen feud between\x01",
            "the Empire and\x01",
            "Republic...\x02\x03",
            "#00301FIt seems a little\x01",
            "strange that they'd know\x01",
            "even that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F#12PYou have no points of\x01",
            "contact...\x02\x03",
            "#00201FAnd yet Dieter, who became\x01",
            "President, designated Arios as\x01",
            "the Secretary of Defense...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_292A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_289A")
    OP_FC(0xFFF4)
    Jump("loc_289D")

    label("loc_289A")

    OP_FC(0xC)

    label("loc_289D")


    ChrTalk(
        0x10A,
        (
            "#00606F#13P...I see, so that's it.\x02\x03",
            "#00601FThen what connects you\x01",
            "both is Lawyer Ian, huh.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x101,
        "#00001F#12PYes... ─Are we wrong?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2A99")

    label("loc_292A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_29E9")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2954")
    OP_FC(0xFFF4)
    Jump("loc_2957")

    label("loc_2954")

    OP_FC(0xC)

    label("loc_2957")


    ChrTalk(
        0x105,
        (
            "#10406F#13P...I see, so that's it.\x02\x03",
            "#10401FThen what connects you\x01",
            "both is Mr. Beardy Bear,\x01",
            "eh?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x101,
        "#00001F#12PYeah... ─Are we wrong?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2A99")

    label("loc_29E9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2A99")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2A13")
    OP_FC(0xFFF4)
    Jump("loc_2A16")

    label("loc_2A13")

    OP_FC(0xC)

    label("loc_2A16")


    ChrTalk(
        0x109,
        (
            "#10108F#13PCould it be that...\x02\x03",
            "#10101FWhat connects both of\x01",
            "you is Mr. Grimwood...?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x101,
        "#00001F#12PYeah... ─Are we wrong?\x02",
    )

    CloseMessageWindow()

    label("loc_2A99")


    ChrTalk(
        0x8,
        "#01404F#5PHehe... Exactly right.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    CreatePortrait(0, 224, 0, 480, 256, 10, 16, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu02200.itp")
    OP_CB(0x0, 0x3, 0xAAFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(500)
    SetMessageWindowPos(14, 280, -1, 3)

    AnonymousTalk(
        0x8,
        (
            "#01402FLike all of you, Guy and I were greatly\x01",
            "helped by Mr. Grimwood's information in\x01",
            "our days with the police.\x02\x03",
            "He's a well-informed man who\x01",
            "collaborated as a civil advisor even in\x01",
            "the cult lodges suppression operation.\x02\x03",
            "#01403FThen, even after I became a bracer... I\x01",
            "frequently exchanged intel with him.\x02",
        )
    )

    CloseMessageWindow()
    CreatePortrait(1, 224, 0, 480, 256, 65296, 16, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu02800.itp")
    OP_CB(0x1, 0x3, 0xAAFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(500)
    SetMessageWindowPos(14, 280, -1, 3)

    AnonymousTalk(
        0x8,
        (
            "#01403F#5POn the other hand, Mr. Grimwood became\x01",
            "acquainted with the Croises through IBC legal\x01",
            "matters.\x02\x03",
            "#01401FThen─ All information and elements were\x01",
            "collected and synthesised by him.\x02\x03",
            "Mr. Crois was guided by him and Crossbell's\x01",
            "independence was achieved with many political\x01",
            "maneuverings and the Sept-Terrion's power.\x02\x03",
            "#01403FBehind his back and unbeknownst to him, the\x01",
            "true plan was being advanced by Mr. Grimwood\x01",
            "and Miss Mariabell.\x02",
        )
    )

    CloseMessageWindow()
    FadeToBright(800, 0)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x1, 0xFF, 0x0)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x101,
        "#00013F#12PThe true plan...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#12PThe "Azure-Zero\x01",
            "Project"...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01403F#5PRight... Mr. Grimwood quickly realized\x01",
            "the truth about the incidents\x01",
            "involving Saya and the others.\x02\x03",
            "Then, he told me the honest truth...\x01",
            "That's when I decided to cooperate and\x01",
            "join their project.\x02\x03",
            "#01400FThat's the whole story.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008F#12P............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#12PEverything went how\x01",
            "Lawyer Ian and Mariabell\x01",
            "wanted...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301F#12P...It's an incredible\x01",
            "story.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3164")

    label("loc_3073")


    ChrTalk(
        0x8,
        (
            "#01403F#5PMr. Crois and I... What connected us,\x01",
            "who have nothing in common, was Mr.\x01",
            "Grimwood.\x02\x03",
            "He quickly realized the truth of the\x01",
            "accident of five years ago and invited\x01",
            "me to join the "Azure-Zero Project"...\x02\x03",
            "#01400FThen, I accepted.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3164")

    Jump("loc_3E6E")

    label("loc_3169")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CF8")

    ChrTalk(
        0x101,
        (
            "#00006F#12P...This is something I have my\x01",
            "doubts about as well, but...\x02\x03",
            "#00013FIt was you, Arios, who removed\x01",
            "KeA from the Fort of Sun's\x01",
            "basement, right?\x02\x03",
            "Then, you switched her with a\x01",
            "Rosenberg doll to be displayed\x01",
            "at the Black Auction.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105F#12PN-Now that you mention\x01",
            "it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#12PIndeed, that question\x01",
            "has never been\x01",
            "completely resolved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01404F#5PYes, precisely.\x02\x03",
            "#01402FRegarding that, it wasn't\x01",
            "Mr. Grimwood's initiative,\x01",
            "but Miss Mariabell's.\x02",
        )
    )

    CloseMessageWindow()
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis303.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis304.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(500)
    SetMessageWindowPos(14, 280, -1, 3)

    AnonymousTalk(
        0x8,
        (
            "#01403FIt seems she completely understood\x01",
            "Joachim's actions...\x02\x03",
            "#01401FWith her teleportation skill, we easily\x01",
            "reached the altar at the lowest stratum\x01",
            "and freed that child from the cradle.\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x1, 0x4, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    Sleep(500)
    SetMessageWindowPos(14, 280, -1, 3)

    AnonymousTalk(
        0x8,
        (
            "#01403FThen, I switched her with a Rosenberg\x01",
            "doll that was brought here from\x01",
            "Remiferia.\x02\x03",
            "#01400FEven the body of that Rosenberg doll\x01",
            "itself was prepared by Miss Mariabell\x01",
            "so Revache wouldn't notice.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, -1, 3)

    AnonymousTalk(
        0x102,
        "#00106F...She went that far...\x02",
    )

    CloseMessageWindow()
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x1, 0xFF, 0x0)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00006F#12PHowever... What reason did\x01",
            "Mariabell have to do\x01",
            "something like that?\x02\x03",
            "#00013FIf she needed KeA for the\x01",
            "project, she could've taken\x01",
            "her, just like that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01403F#5PFirst, it was to involve Heiyue and make\x01",
            "Revache lose face, the first step to their\x01",
            "ruin...\x02\x03",
            "#01400FIf she had woken up at the Black Auction,\x01",
            "Miss Mariabell would have acted.\x02\x03",
            "In front of the agitated guests and Marconi,\x01",
            "she was probably planning to volunteer to\x01",
            "keep custody of her in the name of IBC.\x02\x03",
            "#01404FIf Heiyue acted, things would have developed\x01",
            "differently...\x02\x03",
            "Anyhow, I was hiding at the venue myself.\x02\x03",
            "#01402FNo matter how things unfolded, we had a plan\x01",
            "to deal with it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#12PWhat can I say... That's\x01",
            "too amazin'.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00211F#12PYou were too well\x01",
            "prepared...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3973")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_391A")
    OP_FC(0xFFF4)
    Jump("loc_391D")

    label("loc_391A")

    OP_FC(0xC)

    label("loc_391D")


    ChrTalk(
        0x106,
        (
            "#10708F#13P...Indeed, back then, I\x01",
            "felt a presence like\x01",
            "someone was in hiding...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3973")


    ChrTalk(
        0x8,
        (
            "#01403F#5PAnd, there was a second\x01",
            "reason...\x02\x03",
            "#01401FIt was to evaluate the awakening\x01",
            "potential of the Sept-Terrion\x01",
            "through that unique situation.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xF4, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xF5, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x103,
        (
            "#00205F#12PTo evaluate KeA's\x01",
            "potential?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00101F#12PW-What do you mean...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01403F#5PWell─ That's what Miss Mariabell said.\x02\x03",
            "#01408FIt was most likely a condition to wake\x01",
            "that child from her long slumber...\x02\x03",
            "#01400FIn any case, be it due to the Goddess'\x01",
            "guidance or by mere coincidence, she\x01",
            "woke up before you all.\x02\x03",
            "It should've been completely\x01",
            "unexpected to Miss Mariabell, but...\x02\x03",
            "#01403FIt seems she welcomed you taking\x01",
            "custody of the child and living with\x01",
            "her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008F#12P............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#12P...It's no use. I don't\x01",
            "get it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#12P...Bell... What in the\x01",
            "world are you\x01",
            "planning...?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3E61")

    label("loc_3CF8")


    ChrTalk(
        0x8,
        (
            "#01403F#5PFreeing KeA from the Fort of Sun\x01",
            "and taking her to the Black Auction\x01",
            "venue was Miss Mariabell's idea.\x02\x03",
            "#01408FHer purpose seemed to be to lead\x01",
            "Revache to ruin and even to control\x01",
            "the situation, but...\x02\x03",
            "#01401FIt seems she also had a goal of\x01",
            "evaluating her awakening potential\x01",
            "through that unique situation.\x02\x03",
            "#01403FSadly, I know nothing further.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E61")

    Jump("loc_3E6E")

    label("loc_3E66")

    SetScenarioFlags(0x0, 3)
    Jump("loc_3E6E")

    label("loc_3E6E")

    Jump("loc_1678")

    label("loc_3E73")

    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00006F#12P#30W...Well then...\x02\x03",
            "#00008FAbout the day my big\x01",
            "brother died... ...Could\x01",
            "you tell me the truth?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3F41")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3F26")
    OP_FC(0xFFF4)
    Jump("loc_3F29")

    label("loc_3F26")

    OP_FC(0xC)

    label("loc_3F29")


    ChrTalk(
        0x10A,
        "#00601F#13P......\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_3F41")


    ChrTalk(
        0x103,
        "#00208F#12P...Ah...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#01403F#5P#30W............\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x8)

    ChrTalk(
        0x8,
        "#01400F#5P#30WVery well─\x02",
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    WaitBGM()
    Sound(883, 0, 60, 0)
    Sleep(2300)
    Sound(128, 2, 10, 0)
    Sleep(150)
    OP_25(0x80, 0x14)
    Sleep(150)
    OP_25(0x80, 0x1E)
    Sleep(150)
    OP_25(0x80, 0x28)
    Sleep(150)
    OP_25(0x80, 0x32)
    Sleep(500)
    SetMessageWindowPos(14, 280, -1, 3)

    AnonymousTalk(
        0x8,
        (
            "#3C#30W...It was two years after I had left\x01",
            "the police following Saya's\x01",
            "passing...\x02\x03",
            "I was cooperating with Mr. Grimwood\x01",
            "and the others, accomplishing many\x01",
            "things and advancing the project...\x02\x03",
            "Each and every one of them\x01",
            "underhanded... All of it\x01",
            "conspiratorial intrigue.\x02\x03",
            "However, starting with the fact that\x01",
            "I was connected to the guild, in the\x01",
            "end, no one caught wind of any of it.\x02\x03",
            "Except for Guy Bannings... my former\x01",
            "partner.\x02",
        )
    )

    CloseMessageWindow()
    PlayBGM("ed7560", 0)
    CreatePortrait(0, 224, 0, 480, 256, 0, 16, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu07800.itp")
    OP_CB(0x0, 0x3, 0xEEFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(500)
    SetMessageWindowPos(14, 280, -1, 3)

    AnonymousTalk(
        0x8,
        (
            "#3C#30WGuy... He faced many conspiracies\x01",
            "and secrets with tenacity and an\x01",
            "awfully keen nose.\x02\x03",
            "The secret feud between the Empire\x01",
            "and Republic...\x02\x03",
            "Chairman Hartmann and Revache, the\x01",
            "actions of the D∴G Cult remnants...\x02\x03",
            "Furthermore, even the hidden\x01",
            "project of the Crois clan...\x02\x03",
            "Then─\x02\x03",
            "On that rainy day, Guy called me to\x01",
            "the Orchis Tower construction site,\x01",
            "where work had just started...\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFF000000, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_25(0x80, 0x3C)
    Sleep(200)
    OP_25(0x80, 0x46)
    Sleep(200)
    OP_25(0x80, 0x50)
    Sleep(200)
    OP_25(0x80, 0x5A)
    Sleep(200)
    OP_25(0x80, 0x64)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFF000000, 0x0, "c_vis305.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(500)
    SetMessageWindowPos(14, 280, -1, 3)

    AnonymousTalk(
        0x8,
        (
            "#3C#30WNaturally, he hadn't learned the details of the\x01",
            "project, but...\x02\x03",
            "Guy's conjecture perceived the entire project\x01",
            "with shocking accuracy.\x02\x03",
            "Mr. Crois, who used the cult and the mafia,\x01",
            "stepped forward into the political world...\x02\x03",
            "Fanning the flames of the independence movement\x01",
            "by having Crossbell City attacked and making it\x01",
            "look like the work of a foreign power...\x02\x03",
            "Furthermore, the fact of intimidating and\x01",
            "taking control of the whole of Zemuria with\x01",
            ""something" from the Crois clan...\x02\x03",
            "It's hard to believe, but he pointed out even\x01",
            "that.\x02\x03",
            "Then─\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFF000000, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x1, 0xFF, 0x0)
    CreatePortrait(0, 0, 0, 512, 512, 0, 65296, 512, 512, 0, 0, 512, 512, 0xFF000000, 0x0, "c_vis330.itp")
    CreatePortrait(1, 0, 0, 512, 512, 0, 0, 512, 512, 0, 0, 512, 512, 0xFFFFFF, 0x0, "c_vis331.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x7D0, 0x0)
    OP_CC(0x0, 0x0, 0x0)
    OP_CB(0x1, 0x4, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0xFFFC5680, 0x7D0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x0)
    OP_CB(0x1, 0x3, 0xFF000000, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x1, 0xFF, 0x0)
    Sound(534, 0, 80, 0)
    Sleep(100)
    PlayEffect(0x3, 0x3, 0xC, 0x0, 0, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(372, 0, 40, 0)
    Sleep(200)
    Sound(540, 0, 100, 0)
    Sound(511, 0, 100, 0)
    Sleep(400)
    Sound(540, 0, 100, 0)
    Sound(372, 0, 40, 0)
    Sound(566, 0, 50, 0)
    Sleep(200)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFF000000, 0x0, "c_vis306.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    Sleep(50)
    BeginChrThread(0x8, 0, 0, 30)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(500)
    SetMessageWindowPos(14, 280, -1, 3)

    AnonymousTalk(
        0x8,
        (
            "#3C#30W...Guy didn't accept my request to back\x01",
            "down...\x02\x03",
            "We began a duel to the death amidst the rain.\x02\x03",
            "My skills were somewhat better than his...\x01",
            "However, Guy brimmed with strength coming from\x01",
            "a solid will.\x02\x03",
            "We exchanged blows several times and, while\x01",
            "each of us struggled to keep up with the\x01",
            "other, our death duel continued in the rain...\x02\x03",
            "Then─\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFF000000, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x1, 0xFF, 0x0)
    Sleep(800)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFF000000, 0x0, "c_vis307.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x3E8, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(800)
    SetMessageWindowPos(14, 280, -1, 3)

    AnonymousTalk(
        0x8,
        (
            "#3C#30WThen Guy... lost his life.\x02\x03",
            "Naturally, it was I who took his\x01",
            "tonfas from the scene.\x02\x03",
            "Because I didn't want to be identified\x01",
            "as the culprit from the countless\x01",
            "sword cuts carved into them.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x3E8, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x1, 0xFF, 0x0)
    StopSound(128, 1000, 100)
    FadeToBright(1500, 0)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4B47")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4AFA")
    OP_FC(0xFFF4)
    Jump("loc_4AFD")

    label("loc_4AFA")

    OP_FC(0xC)

    label("loc_4AFD")


    ChrTalk(
        0x109,
        "#10106F#13P#30WAll of that...\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x103,
        "#00208F#12P#30W............\x02",
    )

    CloseMessageWindow()
    Jump("loc_4B9A")

    label("loc_4B47")


    ChrTalk(
        0x101,
        "#00008F#12P#30W............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#12P#30W...So that's what\x01",
            "happened...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B9A")

    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x8)
    Sleep(500)

    ChrTalk(
        0x8,
        (
            "#01403F#5P#30W...That is the outline of what\x01",
            "happened on that rainy day.\x02\x03",
            "#01408FThe fact that afterwards, a mafia\x01",
            "underling appeared and left with Guy's\x01",
            "badge was beyond my expectations...\x02\x03",
            "#01400FIn any case, this should answer most\x01",
            "of your doubts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003F#12P─No.\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        "#01405F#5P............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#12PYou already know this, of\x01",
            "course, but my big brother's\x01",
            "cause of death was a gunshot.\x02\x03",
            "#00001FI don't think you've\x01",
            "explained that, but...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01403F#5P...When I was in the police\x01",
            "I learned how to use a gun.\x02\x03",
            "#01401FExasperated by a persistent,\x01",
            "obstinate and troublesome\x01",
            "opponent, I used one...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4F37")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4E5E")
    OP_FC(0xFFF4)
    Jump("loc_4E61")

    label("loc_4E5E")

    OP_FC(0xC)

    label("loc_4E61")


    ChrTalk(
        0x10A,
        (
            "#00606F#13PYou lie, MacLaine.\x02\x03",
            "#00601FAs if you would have time to\x01",
            "change weapons in a death duel\x01",
            "like that.\x02\x03",
            "To say nothing of it being\x01",
            "impossible to deliver the final\x01",
            "blow to your opponent from behind.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5014")

    label("loc_4F37")


    ChrTalk(
        0x101,
        (
            "#00013F#12P─That's a lie.\x02\x03",
            "#00006FThere's no way you could've had\x01",
            "time to change weapons in a\x01",
            "death duel like that.\x02\x03",
            "#00001FTo say nothing of it being\x01",
            "impossible to deliver the final\x01",
            "blow from behind your opponent.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5014")

    StopBGM(0xFA0)

    ChrTalk(
        0x8,
        "#01401F#5P............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00303F#12PWell, that's reasonable.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108F#12PJust "who" shot Guy...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00201F#12P...Please tell us.\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x8, 0, 0, 22)
    WaitChrThread(0x8, 0)
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x8)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7356", 0)
    MoveCamera(43, 13, 0, 20000)
    Sleep(500)

    ChrTalk(
        0x8,
        (
            "#01403F#5P#30W─Say what you like, but the one who\x01",
            "killed Guy was none other than\x01",
            "yours truly.\x02\x03",
            "#01400FThen, I... chose the path of\x01",
            "collaborating with the project that\x01",
            "made my former partner a victim.\x02\x03",
            "Then, and even now... I'm trying to\x01",
            "complete a project that makes use\x01",
            "of an innocent girl's feelings.\x02\x03",
            "#01403FAll of this is for Saya... and for\x01",
            "Shizuku's future as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F#12P...Arios...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#12PDo you think that Shizuku\x01",
            "would be happy that you're\x01",
            "doing these things...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01403F#5P#30WOf course not.\x02\x03",
            "#01401FHowever─ The curse of the land called\x01",
            "Crossbell stole that child's mother\x01",
            "away and the light from her eyes.\x02\x03",
            "As long as Crossbell holds this\x01",
            "position in the continent, that curse\x01",
            "will never vanish.\x02\x03",
            "#01403F─Unless a "miracle" transcending the\x01",
            "logic of the human world occurs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#12P...!?\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x8, 0, 0, 23)
    WaitChrThread(0x8, 0)
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
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#01400F#5P#30WThree years ago, Guy... Without\x01",
            "even blaming me, he lost his life\x01",
            "at the end of a duel to the death.\x02\x03",
            "Then, KeA, who became a Sept-\x01",
            "Terrion, healed Shizuku's eyes.\x02\x03",
            "#01403FFor the me of right now─ it's\x01",
            "impossible to go back.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetCameraDistance(15370, 800)
    BeginChrThread(0x8, 0, 0, 24)
    Sleep(500)
    PlayEffect(0x1, 0x1, 0x8, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(250)
    OP_82(0x64, 0x0, 0xBB8, 0x320)
    Sound(825, 2, 50, 0)
    Sound(832, 2, 100, 0)
    Sound(881, 0, 50, 0)
    Sound(833, 0, 50, 0)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#01403F#5P#30W...If you can't accept that, then\x01",
            "try stopping me with force...\x02\x03",
            "#01401FUsing those tonfas your brother\x01",
            "left you...\x02\x03",
            "#01407FShow me that you'll take revenge\x01",
            "for him and open the path to take\x01",
            "back what is precious to you!\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xBB8)

    ChrTalk(
        0x101,
        (
            "#00006F#12P...Understood.\x02\x03",
            "#00001FHowever─ I have no\x01",
            "intentions of avenging\x01",
            "my brother.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    BeginChrThread(0x101, 0, 0, 16)
    WaitChrThread(0x101, 0)
    PlayEffect(0x2, 0x0, 0x101, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(881, 0, 50, 0)
    Sound(833, 0, 50, 0)
    OP_25(0x339, 0x46)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7527", 0)
    SetCameraDistance(18370, 20000)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00003F#12PAs a modest duty post that was\x01",
            "started by inheriting Guy Banning's\x01",
            "will...\x02\x03",
            "#00001FAs the Special Support Section that\x01",
            "was entrusted with the feelings of\x01",
            "many people, starting with Shizuku...\x02\x03",
            "#00007FI'll get over the Barrier that is\x01",
            "you, take KeA back... and solve this\x01",
            "case in a real sense!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x8,
        "#01405F#5P...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302F#12PHaha... That's our\x01",
            "leader for ya!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101F#12PEven for Shizuku who's\x01",
            "waiting at Orchis\x01",
            "Tower...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00201F#12P...We'll never back\x01",
            "down!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5A54")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5A21")
    OP_FC(0xFFF4)
    Jump("loc_5A24")

    label("loc_5A21")

    OP_FC(0xC)

    label("loc_5A24")


    ChrTalk(
        0x10A,
        (
            "#00604F#13PHmph... You guys are\x01",
            "hopeless.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_5A54")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5ABF")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5A7E")
    OP_FC(0xFFF4)
    Jump("loc_5A81")

    label("loc_5A7E")

    OP_FC(0xC)

    label("loc_5A81")


    ChrTalk(
        0x105,
        (
            "#10402F#13PHehe... This is the\x01",
            "Support Section's style.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_5ABF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5B28")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5AE9")
    OP_FC(0xFFF4)
    Jump("loc_5AEC")

    label("loc_5AE9")

    OP_FC(0xC)

    label("loc_5AEC")


    ChrTalk(
        0x109,
        (
            "#10107F#13PI'll support you with\x01",
            "everything I've got!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_5B28")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5BD1")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5B52")
    OP_FC(0xFFF4)
    Jump("loc_5B55")

    label("loc_5B52")

    OP_FC(0xC)

    label("loc_5B55")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5B9F")

    ChrTalk(
        0x106,
        (
            "#10701F#13PMe too... I'll do as\x01",
            "much as I can!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_5BD1")

    label("loc_5B9F")


    ChrTalk(
        0x106,
        (
            "#10707F#13PI'll help you with all\x01",
            "my might!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_5BD1")

    BeginChrThread(0x102, 0, 0, 17)
    BeginChrThread(0x103, 0, 0, 18)
    BeginChrThread(0x104, 0, 0, 19)
    BeginChrThread(0xF4, 0, 0, 20)
    BeginChrThread(0xF5, 0, 0, 21)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)
    Sleep(500)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x8,
        "#01404F#4077V#5P#30W#25AHehe─ Very well.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x8, 0, 0, 25)
    WaitChrThread(0x8, 0)
    Sound(817, 0, 100, 0)
    BeginChrThread(0xA, 3, 0, 27)
    BeginChrThread(0xB, 3, 0, 28)
    WaitChrThread(0xA, 3)
    WaitChrThread(0xB, 3)
    OP_68(180, 13300, 207000, 20000)
    MoveCamera(43, 13, 0, 20000)
    SetCameraDistance(14120, 20000)
    CreatePortrait(0, 65514, 0, 490, 256, 0, 0, 512, 256, 0, 0, 512, 256, 0xFFFFFF, 0x0, "bu01402.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    BeginChrThread(0x8, 0, 0, 26)

    AnonymousTalk(
        0x8,
        (
            "#4065V#40W#55AEight Leaves One Blade... Master\x01",
            "of the second form, Arios\x01",
            "MacLaine...\x02\x03",
            "#4066V#60ADue to personal circumstances,\x01",
            "I'll infringe justice, stray from\x01",
            "the path and act as I please!\x02\x03",
            "#4067V#30ACome at me─ Special Support\x01",
            "Section!\x02",
        )
    )

    WaitChrThread(0x8, 0)
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
    SetMessageWindowPos(330, 100, -1, -1)
    SetChrName("Everyone")
    OP_82(0xC8, 0x0, 0xBB8, 0x1F4)

    AnonymousTalk(
        0xFF,
        "#4S#12AYeah!\x02",
    )

    Sound(2153, 255, 90, 0)
    Sound(2343, 255, 100, 1)
    Sound(2249, 255, 100, 2)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5EAE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5EA5")
    OP_FC(0x4)
    Sound(2478, 255, 100, 4)
    Jump("loc_5EAE")

    label("loc_5EA5")

    OP_FC(0x3)
    Sound(2478, 255, 100, 3)

    label("loc_5EAE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5EE1")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5EDB")
    Sound(2417, 255, 100, 4)
    Jump("loc_5EE1")

    label("loc_5EDB")

    Sound(2417, 255, 100, 3)

    label("loc_5EE1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5F14")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5F0E")
    Sound(2544, 255, 100, 4)
    Jump("loc_5F14")

    label("loc_5F0E")

    Sound(2544, 255, 100, 3)

    label("loc_5F14")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5F47")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5F41")
    Sound(3174, 255, 100, 4)
    Jump("loc_5F47")

    label("loc_5F41")

    Sound(3174, 255, 100, 3)

    label("loc_5F47")

    Sound(2055, 255, 100, 5)
    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Battle("BattleInfo_2B8", 0x0, 0x0, 0x100, 0x45, 0xFF)
    FadeToDark(0, 0, -1)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    Call(0, 31)
    Return()

    # Function_9_D5D end

    def Function_10_5F82(): pass

    label("Function_10_5F82")

    OP_9B(0x0, 0xFE, 0x0, 0x1770, 0xFA0, 0x1)
    OP_96(0xFE, 0x0, 0x2EE0, 0x318BC, 0xFA0, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_10_5F82 end

    def Function_11_5FAD(): pass

    label("Function_11_5FAD")

    OP_9B(0x0, 0xFE, 0x0, 0x157C, 0xFA0, 0x1)
    OP_96(0xFE, 0x460, 0x2EE0, 0x313E4, 0xFA0, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_11_5FAD end

    def Function_12_5FD8(): pass

    label("Function_12_5FD8")

    OP_9B(0x0, 0xFE, 0x0, 0x157C, 0xFA0, 0x1)
    OP_96(0xFE, 0x1A4, 0x2EE0, 0x30EB2, 0xFA0, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_12_5FD8 end

    def Function_13_6003(): pass

    label("Function_13_6003")

    OP_9B(0x0, 0xFE, 0x0, 0x157C, 0xFA0, 0x1)
    OP_96(0xFE, 0xFFFFFB0A, 0x2EE0, 0x3116E, 0xFA0, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_13_6003 end

    def Function_14_602E(): pass

    label("Function_14_602E")

    OP_9B(0x0, 0xFE, 0x0, 0x1996, 0xFA0, 0x1)
    OP_96(0xFE, 0xFFFFF614, 0x2EE0, 0x313DA, 0xFA0, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_14_602E end

    def Function_15_6059(): pass

    label("Function_15_6059")

    OP_9B(0x0, 0xFE, 0x0, 0x1AC2, 0xFA0, 0x1)
    OP_96(0xFE, 0x9EC, 0x2EE0, 0x31312, 0xFA0, 0x0)
    Return()

    # Function_15_6059 end

    def Function_16_607D(): pass

    label("Function_16_607D")

    Sleep(150)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_16_607D end

    def Function_17_608F(): pass

    label("Function_17_608F")

    Sleep(300)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_17_608F end

    def Function_18_60A1(): pass

    label("Function_18_60A1")

    Sleep(450)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_18_60A1 end

    def Function_19_60B3(): pass

    label("Function_19_60B3")

    Sleep(450)
    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_19_60B3 end

    def Function_20_60BF(): pass

    label("Function_20_60BF")

    Sleep(600)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_60DF")
    Sound(540, 0, 50, 0)
    Jump("loc_6104")

    label("loc_60DF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6104")
    Sound(531, 0, 100, 0)

    label("loc_6104")

    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_20_60BF end

    def Function_21_610D(): pass

    label("Function_21_610D")

    Sleep(750)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_612D")
    Sound(540, 0, 50, 0)
    Jump("loc_6152")

    label("loc_612D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6152")
    Sound(531, 0, 100, 0)

    label("loc_6152")

    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_21_610D end

    def Function_22_615B(): pass

    label("Function_22_615B")

    SetChrChipByIndex(0x8, 0x2A)
    SetChrFlags(0xFE, 0x1000)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x2)
    SetChrSubChip(0xFE, 0x0)
    Sleep(125)
    SetChrSubChip(0xFE, 0x1)
    Sleep(125)
    SetChrSubChip(0xFE, 0x2)
    Sleep(500)
    Return()

    # Function_22_615B end

    def Function_23_6184(): pass

    label("Function_23_6184")

    SetChrChipByIndex(0x8, 0x2A)
    SetChrFlags(0xFE, 0x1000)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x2)
    SetChrSubChip(0xFE, 0x2)
    Sleep(125)
    Sound(932, 0, 60, 0)
    SetChrSubChip(0xFE, 0x3)
    Sleep(125)
    SetChrSubChip(0xFE, 0x4)
    Sleep(375)
    SetChrSubChip(0xFE, 0x5)
    Sleep(125)
    Sound(859, 0, 100, 0)
    SetChrSubChip(0xFE, 0x6)
    Sleep(125)
    SetChrSubChip(0xFE, 0x7)
    Sleep(500)
    Return()

    # Function_23_6184 end

    def Function_24_61CE(): pass

    label("Function_24_61CE")

    SetChrSubChip(0xFE, 0x7)
    Sleep(125)
    SetChrSubChip(0xFE, 0x8)
    Sleep(125)
    SetChrSubChip(0xFE, 0x9)
    Sleep(125)
    SetChrSubChip(0xFE, 0xA)
    Sleep(125)
    Sound(812, 0, 100, 0)
    Sound(531, 0, 50, 0)
    SetChrSubChip(0xFE, 0xB)
    Return()

    # Function_24_61CE end

    def Function_25_61FB(): pass

    label("Function_25_61FB")

    SetChrSubChip(0xFE, 0xB)
    Sleep(125)
    SetChrSubChip(0xFE, 0xC)
    Sleep(125)
    SetChrSubChip(0xFE, 0xD)
    Sleep(125)
    Sound(531, 0, 50, 0)
    SetChrSubChip(0xFE, 0xE)
    Sleep(250)
    Sound(859, 0, 60, 0)
    Sleep(250)
    Return()

    # Function_25_61FB end

    def Function_26_6227(): pass

    label("Function_26_6227")

    SetChrSubChip(0xFE, 0xE)
    Sleep(91)
    Sound(540, 0, 40, 0)
    SetChrSubChip(0xFE, 0xF)
    Sleep(91)
    SetChrSubChip(0xFE, 0x10)
    Sleep(91)
    SetChrSubChip(0xFE, 0x11)
    Sleep(364)
    Return()

    # Function_26_6227 end

    def Function_27_624A(): pass

    label("Function_27_624A")

    PlayEffect(0x0, 0x5, 0xFE, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    StopEffect(0x5, 0x2)
    Return()

    # Function_27_624A end

    def Function_28_6293(): pass

    label("Function_28_6293")

    PlayEffect(0x0, 0x6, 0xFE, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    StopEffect(0x6, 0x2)
    Return()

    # Function_28_6293 end

    def Function_29_62DC(): pass

    label("Function_29_62DC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_62F7")
    OP_A1(0xFE, 0x4B0, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_29_62DC")

    label("loc_62F7")

    Return()

    # Function_29_62DC end

    def Function_30_62F8(): pass

    label("Function_30_62F8")

    OP_CB(0x0, 0x0, 0xFFFFE0C0, 0x0, 0x6E, 0x0)
    OP_CC(0x0, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x1770, 0x0, 0x5A, 0x0)
    OP_CC(0x0, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFF060, 0x0, 0x46, 0x0)
    OP_CC(0x0, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x7D0, 0x0, 0x32, 0x0)
    OP_CC(0x0, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1E, 0x0)
    OP_CC(0x0, 0x0, 0x0)
    Return()

    # Function_30_62F8 end

    def Function_31_636C(): pass

    label("Function_31_636C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    LoadChrToIndex("chr/ch00050.itc", 0x1F)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00250.itc", 0x21)
    LoadChrToIndex("chr/ch00350.itc", 0x22)
    Call(0, 6)
    Call(0, 7)
    LoadChrToIndex("apl/ch51744.itc", 0x26)
    LoadEffect(0x0, "event/ev17084.eff")
    LoadEffect(0x1, "event/ev17085.eff")
    SoundLoad(128)
    SoundLoad(4078)
    SoundLoad(4079)
    OP_68(-80, 13300, 209040, 0)
    MoveCamera(358, 19, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(19000, 0)
    SetCameraDistance(16500, 2500)
    SetChrPos(0x101, 0, 12000, 207440, 0)
    SetChrPos(0x102, 1120, 12000, 206200, 0)
    SetChrPos(0x103, 420, 12000, 204870, 0)
    SetChrPos(0x104, -1270, 12000, 205570, 0)
    SetChrPos(0xF4, -2540, 11990, 206190, 0)
    SetChrPos(0xF5, 2540, 12000, 205990, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x101, 0x1F)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x21)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x22)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0xF4, 0x23)
    SetChrSubChip(0xF4, 0x0)
    SetChrChipByIndex(0xF5, 0x24)
    SetChrSubChip(0xF5, 0x0)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x1000)
    SetChrFlags(0x8, 0x2)
    SetChrFlags(0x8, 0x800)
    SetChrPos(0x8, 0, 12000, 211500, 180)
    BeginChrThread(0x8, 0, 0, 32)
    OP_68(0, 13000, 210000, 0)
    MoveCamera(0, 15, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17500, 0)
    SetCameraDistance(15800, 12000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x8,
        (
            "#01404F#4078V#5P#80W#30A...Hehe...\x02\x03",
            "#4079V#45ALloyd... and the rest of\x01",
            "you as well... ...You've\x01",
            "really become strong.\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(0, 13100, 208700, 0)
    MoveCamera(46, 18, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14680, 0)
    EndChrThread(0x8, 0x0)
    SetChrSubChip(0x8, 0x1)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#00006F#12P#40W...*pant*... *pant*...\x02\x03",
            "#00008FIf that's true... it's\x01",
            "because you were our\x01",
            "goal, Arios...\x02",
        )
    )

    OP_6F(0x79)
    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#12P#40WIndeed... Without you,\x01",
            "we might not have come\x01",
            "this far...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00206F#12P#40W...I agree...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#12P#40WYou were always so far\x01",
            "ahead of us, a Barrier\x01",
            "to always aim for...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01402F#5P#40WHehe... Honestly...\x02\x03",
            "#01404FAlthough I haven't the\x01",
            "slightest right to be\x01",
            "told that...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#00003F#12P#30W...Arios.\x02\x03",
            "#00001FThe one who shot my\x01",
            "brother that day... It was\x01",
            "Lawyer Ian, wasn't it.\x02",
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
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_68E6")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_68C4")
    OP_FC(0xFFF4)
    Jump("loc_68C7")

    label("loc_68C4")

    OP_FC(0xC)

    label("loc_68C7")


    ChrTalk(
        0x10A,
        "#00605F#13P#30W...!\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_692F")

    label("loc_68E6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_692F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6910")
    OP_FC(0xFFF4)
    Jump("loc_6913")

    label("loc_6910")

    OP_FC(0xC)

    label("loc_6913")


    ChrTalk(
        0x109,
        "#10105F#13P#30W...Ah!\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_692F")


    ChrTalk(
        0x104,
        "#00301F#12P#30WWell...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01403F#5P#40W............\x02\x03",
            "#01400F...Why do you think so?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#12P#30WIt's a simple process of\x01",
            "elimination...\x02\x03",
            "#00008F...Thinking about the circumstances...\x01",
            "Other suspects aside from Lawyer Ian\x01",
            "would be Dieter and Mariabell...\x02\x03",
            "#00001FHowever, Dieter didn't know the entire\x01",
            "plan and Mariabell had no connection\x01",
            "with my brother...\x02\x03",
            "#00006FBut... it seems he and Lawyer Ian were\x01",
            "very close...\x02\x03",
            "Also... Due to his many trips abroad,\x01",
            "it wouldn't be strange for Lawyer Ian\x01",
            "to be familiar with pistols if\x01",
            "necessary for self-defense...\x02\x03",
            "#00013F...What do you think of that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01403F#5P#40W...60 points...\x02\x03",
            "#01402FBut... It seems I have\x01",
            "to give you a passing\x01",
            "mark...\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    Sound(128, 2, 30, 0)
    Sleep(150)
    OP_25(0x80, 0x28)
    Sleep(150)
    OP_25(0x80, 0x32)
    Sleep(150)
    OP_25(0x80, 0x3C)
    Sleep(150)
    OP_25(0x80, 0x46)
    Sleep(150)
    OP_25(0x80, 0x50)
    Sleep(150)
    OP_25(0x80, 0x5A)
    Sleep(150)
    OP_25(0x80, 0x64)
    Sleep(300)
    Sound(884, 0, 100, 0)
    Sleep(3000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7534", 0)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis308.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis317.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x3E8, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(500)
    SetMessageWindowPos(20, 160, -1, -1)
    SetChrName("Guy")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x14),
            "#40W*pant, pant*...\x02\x03",
            "...Say, Arios...\x02\x03",
            "We're both at our\x01",
            "limit... Why don't we\x01",
            "call a truce this time?\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(230, 140, -1, -1)
    SetChrName("Arios")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x14),
            "#40W...What nonsense...\x02\x03",
            "As I'm sure you already know, I\x01",
            "can't let you leave here alive...\x02\x03",
            "If you want to safely reach your\x01",
            "wedding day next month, come at\x01",
            "me like you're trying to kill me!\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(20, 160, -1, -1)
    SetChrName("Guy")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x14),
            "#40WAs if I could do\x01",
            "something like that...\x02\x03",
            "If I did, I couldn't\x01",
            "invite you and Shizuku,\x01",
            "right...?\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(330, 140, -1, -1)
    SetChrName("Arios")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x14),
            "...!\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(20, 160, -1, -1)
    SetChrName("Guy")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x14),
            "#40WDon't worry... I haven't\x01",
            "mentioned your project to\x01",
            "anyone...\x02\x03",
            "I thought to get Dudley's\x01",
            "cooperation, but... That\x01",
            "guy lacks flexibility.\x02\x03",
            "I didn't even consult\x01",
            "with Sergei, you know?\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(250, 140, -1, -1)
    SetChrName("Arios")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x14),
            "#40WYou...\x02\x03",
            "Did you think, when I\x01",
            "heard this, I'd think it\x01",
            "was convenient?\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(20, 160, -1, -1)
    SetChrName("Guy")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x14),
            "#30WNo...? After all, you're\x01",
            "awkward.\x02\x03",
            "If you weren't, you\x01",
            "wouldn't have brazenly come\x01",
            "to a place like this alone.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(330, 140, -1, -1)
    SetChrName("Arios")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x14),
            "#30WUgh...\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(20, 160, -1, -1)
    SetChrName("Guy")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x14),
            "#30WAnyway... Why don't we leave\x01",
            "it at this and have\x01",
            "something to drink?\x02\x03",
            "If we leave it at this, we\x01",
            "won't have had a decent\x01",
            "conversation in two years...\x02\x03",
            "At least let me brag about\x01",
            "my younger brother and\x01",
            "fiancｳe.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(240, 150, -1, -1)
    SetChrName("Arios")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x14),
            "#30WHmph... You never\x01",
            "change.\x02\x03",
            "Your younger brother...\x01",
            "He's already 15, right?\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(20, 160, -1, -1)
    SetChrName("Guy")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x14),
            "#30WYeah. Unlike me, he's\x01",
            "quite the prodigy.\x02\x03",
            "I'm thinking of sending\x01",
            "him to high school\x01",
            "somewhere...\x02\x03",
            "...Oh, well. It's\x01",
            "raining, so even Galante\x01",
            "would be─\x02",
        )
    )

    CloseMessageWindow()
    Sound(567, 0, 100, 0)
    Sleep(200)
    OP_CB(0x1, 0x4, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    Sleep(500)
    SetMessageWindowPos(80, 160, -1, -1)
    SetChrName("Guy")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x14),
            "#60WAh─\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(330, 140, -1, -1)
    SetChrName("Arios")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x14),
            "#30W!?\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x1, 0xFF, 0x0)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis309.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x2EE, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(300)
    SetMessageWindowPos(330, 160, -1, -1)
    SetChrName("Arios")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x14),
            "#30WMr. Grimwood!?\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(250, 180, -1, -1)
    SetChrName("Guy")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x14),
            "#50W......Haha......\x02\x03",
            "...I see... So you're\x01",
            "the mastermind...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x1, 0xFF, 0x0)
    Sound(885, 0, 80, 0)
    Sound(811, 0, 80, 0)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis310.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis318.itp")
    CreatePortrait(2, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis319.itp")
    CreatePortrait(3, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis320.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(1000)
    OP_CB(0x1, 0x4, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    Sleep(1000)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    OP_CB(0x2, 0x4, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    Sleep(1000)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    OP_CB(0x3, 0x4, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x3, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    SetMessageWindowPos(30, 160, -1, -1)
    SetChrName("Lawyer Ian")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x14),
            "#30W...I'm sorry, Guy.\x02\x03",
            "When I thought about your\x01",
            "parents, I thought about\x01",
            "inviting you too, but...\x02\x03",
            "In the end, I was able to\x01",
            "confirm that you would've\x01",
            "never approved.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(350, 140, -1, -1)
    SetChrName("Arios")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x14),
            "#30W...Mr. Grimwood...\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(200, 200, -1, -1)
    SetChrName("Guy")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x14),
            "#50WHaha... Naturally...\x02\x03",
            "...With you there,\x01",
            "Lawyer Ian... maybe that\x01",
            "project will go well...\x02\x03",
            "But... I'm sure... a\x01",
            "substitute for me will\x01",
            "appear...\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(40, 160, -1, -1)
    SetChrName("Lawyer Ian")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x14),
            "#30WYes... Probably so.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(350, 140, -1, -1)
    SetChrName("Arios")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x14),
            "#30WGuy! Stay with me!\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(210, 200, -1, -1)
    SetChrName("Guy")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x14),
            "#60W*cough*... Aaah...\x01",
            "...Damn it all...\x02\x03",
            "#80WWith this... Lloyd\x01",
            "and... Cecil...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x3, 0x3, 0xFFFFFF, 0x3E8, 0x0, 0x0)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    OP_CC(0x0, 0x3, 0x3)
    OP_CC(0x1, 0xFF, 0x0)
    Sound(885, 0, 90, 0)
    Sleep(100)
    Sound(811, 0, 90, 0)
    Sound(862, 0, 40, 0)
    StopBGM(0x1770)
    Sleep(2000)
    StopSound(128, 2000, 100)
    WaitBGM()
    SetCameraDistance(16180, 3000)
    FadeToBright(1500, 0)
    OP_0D()
    OP_6F(0x79)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_789D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7878")
    OP_FC(0xFFF4)
    Jump("loc_787B")

    label("loc_7878")

    OP_FC(0xC)

    label("loc_787B")


    ChrTalk(
        0x10A,
        "#00608F#13P#30W............\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_789D")


    ChrTalk(
        0x103,
        "#00213F#12P#30W...Guy...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#12P#30W...So that's what\x01",
            "happened...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00308F#12P#30WHow unfortunate...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#12P#30W...Thank you for telling\x01",
            "me about my big\x01",
            "brother's final moments.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01404F#5P#40W...Don't thank me...\x02\x03",
            "#01400FLawyer Ian... You\x01",
            "probably can't convince\x01",
            "him...\x02\x03",
            "And... It seems KeA's\x01",
            "determination is firm as\x01",
            "well...\x02\x03",
            "#01404F#50WWill you beat those two\x01",
            "or not...? You'll need\x01",
            "everything you have to...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    Sound(898, 0, 100, 0)

    def lambda_7A66():
        OP_A6(0xFE, 0x0, 0x23, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_7A66)
    WaitChrThread(0x8, 2)
    BeginChrThread(0x8, 0, 0, 33)
    WaitChrThread(0x8, 0)
    Sleep(250)
    PlayBGM("ed7356", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x164), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(700)
    Sound(202, 0, 100, 0)
    Sound(181, 0, 80, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 0, 12050, 208000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    SetMapObjFrame(0xFF, "magi_04_add", 0x0, 0x1)
    Sleep(2000)
    OP_68(0, 13400, 208000, 0)
    MoveCamera(30, 20, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(42000, 0)
    Fade(500)
    SetCameraDistance(44000, 5000)
    OP_0D()
    Sound(223, 0, 50, 0)
    Sound(293, 0, 60, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -8810, 11000, 195890, 250, -40, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -18740, 11000, 207720, 240, -40, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -8810, 11000, 219990, 277, -40, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 2340, 11000, 226130, 26, -40, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 14640, 11000, 216150, 34, -40, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 14650, 11000, 200000, 64, -40, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    OP_75(0x2, 0x1, 0x7D0)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -14190, 4900, 215730, 314, -33, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 3670, 8000, 223960, 85, -33, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 16510, 5300, 208790, 89, -33, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -14840, 11000, 200070, 295, -40, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -14870, 11000, 216410, 326, -40, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -2400, 11000, 226170, 334, -40, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 8990, 11000, 220020, 80, -40, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 18340, 11000, 208220, 120, -40, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 8860, 11000, 195800, 110, -40, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -1580, 4700, 224260, 271, -33, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 16370, 8500, 219180, 44, -33, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 6440, 1300, 196290, 113, -13, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 23440, -900, 210080, 119, -13, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    Sleep(100)
    Sleep(100)
    Sleep(100)
    Sleep(100)
    Sleep(100)
    Sleep(100)
    FadeToDark(1500, 0, -1)
    OP_24(0x80)
    OP_0D()
    SetScenarioFlags(0x22, 0)
    SetScenarioFlags(0x22, 2)
    NewScene("m9008", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_31_636C end

    def Function_32_7FC5(): pass

    label("Function_32_7FC5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_800D")
    SetChrSubChip(0xFE, 0x8)
    Sleep(150)
    SetChrSubChip(0xFE, 0x9)
    Sleep(150)
    SetChrSubChip(0xFE, 0xA)
    Sleep(150)
    SetChrSubChip(0xFE, 0xB)
    Sleep(150)
    SetChrSubChip(0xFE, 0xC)
    Sleep(150)
    SetChrSubChip(0xFE, 0xB)
    Sleep(150)
    SetChrSubChip(0xFE, 0xA)
    Sleep(150)
    SetChrSubChip(0xFE, 0x9)
    Sleep(150)
    Jump("Function_32_7FC5")

    label("loc_800D")

    Return()

    # Function_32_7FC5 end

    def Function_33_800E(): pass

    label("Function_33_800E")

    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    SetChrSubChip(0xFE, 0x3)
    Sleep(100)
    SetChrSubChip(0xFE, 0x4)
    Sleep(100)
    SetChrSubChip(0xFE, 0x5)
    Sleep(100)
    SetChrSubChip(0xFE, 0x6)
    Sleep(100)
    SetChrSubChip(0xFE, 0x7)
    Sound(811, 0, 40, 0)
    Sleep(100)
    SetChrSubChip(0xFE, 0x7)
    Sleep(300)
    SetChrSubChip(0xFE, 0x7)
    Sleep(100)
    SetChrSubChip(0xFE, 0xD)
    Sleep(100)
    SetChrSubChip(0xFE, 0xE)
    Sleep(100)
    Sound(811, 0, 80, 0)
    SetChrSubChip(0xFE, 0xF)
    Sleep(100)
    Sound(862, 0, 30, 0)
    Sleep(300)
    Return()

    # Function_33_800E end

    def Function_34_8078(): pass

    label("Function_34_8078")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    Call(0, 43)
    LoadChrToIndex("chr/ch00050.itc", 0x1F)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00250.itc", 0x21)
    LoadChrToIndex("chr/ch00350.itc", 0x22)
    Call(0, 6)
    Call(0, 7)
    LoadChrToIndex("chr/ch00056.itc", 0x25)
    LoadEffect(0x0, "event/ev17012.eff")
    SetChrPos(0x101, -430, 12000, 207440, 0)
    SetChrPos(0x102, 470, 12000, 206000, 0)
    SetChrPos(0x103, -1370, 12000, 204870, 0)
    SetChrPos(0x104, 1370, 12000, 204570, 0)
    SetChrPos(0xF4, -2540, 12000, 205690, 0)
    SetChrPos(0xF5, 2400, 12000, 205790, 315)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x101, 0x1F)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x21)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x22)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0xF4, 0x23)
    SetChrSubChip(0xF4, 0x0)
    SetChrChipByIndex(0xF5, 0x24)
    SetChrSubChip(0xF5, 0x0)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0xF)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x1000)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x2)
    SetChrFlags(0x8, 0x800)
    SetChrPos(0x8, 0, 12000, 211500, 180)
    SetMapObjFrame(0xFF, "magi_04_add", 0x0, 0x1)
    SetMapObjFlags(0x2, 0x4)
    OP_68(0, 13050, 222000, 0)
    MoveCamera(16, 28, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(31500, 0)
    SetCameraDistance(29500, 2600)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(300)
    PlayEffect(0x0, 0x0, 0xFF, 0x0, 0, 12000, 222000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(935, 0, 80, 0)
    SetMapObjFrame(0xFF, "magi10_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "magi11_add", 0x1, 0x1)
    Sleep(200)
    SetMapObjFrame(0xFF, "point_add", 0x1, 0x1)
    Sleep(600)
    StopEffect(0x0, 0x2)
    OP_6F(0x79)
    OP_68(0, 12800, 208700, 0)
    MoveCamera(46, 18, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18410, 0)
    Fade(500)
    OP_0D()
    Sleep(300)
    BeginChrThread(0x101, 0, 0, 36)
    BeginChrThread(0x102, 0, 0, 37)
    BeginChrThread(0x103, 0, 0, 38)
    BeginChrThread(0x104, 0, 0, 39)
    BeginChrThread(0xF4, 0, 0, 40)
    BeginChrThread(0xF5, 0, 0, 41)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)
    Sleep(100)
    OP_68(160, 12800, 209170, 2000)
    MoveCamera(44, 18, 0, 2000)
    OP_6E(600, 2000)
    SetCameraDistance(17490, 2000)
    BeginChrThread(0x101, 0, 0, 35)
    WaitChrThread(0x101, 0)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    Sleep(500)
    OP_6F(0x79)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8377")

    ChrTalk(
        0x102,
        "#00108F#12PLloyd...\x02",
    )

    CloseMessageWindow()
    Jump("loc_845A")

    label("loc_8377")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_83A7")

    ChrTalk(
        0x103,
        "#00208F#12P...Lloyd...\x02",
    )

    CloseMessageWindow()
    Jump("loc_845A")

    label("loc_83A7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_83D4")

    ChrTalk(
        0x104,
        "#00308F#12PLloyd...\x02",
    )

    CloseMessageWindow()
    Jump("loc_845A")

    label("loc_83D4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8404")

    ChrTalk(
        0x105,
        "#10408F#12P...Lloyd...\x02",
    )

    CloseMessageWindow()
    Jump("loc_845A")

    label("loc_8404")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8431")

    ChrTalk(
        0x109,
        "#10108F#12PLloyd...\x02",
    )

    CloseMessageWindow()
    Jump("loc_845A")

    label("loc_8431")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_845A")

    ChrTalk(
        0x106,
        "#10708F#12P...Lloyd.\x02",
    )

    CloseMessageWindow()

    label("loc_845A")


    ChrTalk(
        0x101,
        (
            "#00004F#11P#30WHaha...\x02\x03",
            "#00008F...Now, at last... I\x01",
            "think I've reached my\x01",
            "big brother.\x02\x03",
            "#00002FThank you... It was\x01",
            "thanks to you all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00304F#12PHaha... The heck are you\x01",
            "sayin'?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00204F#12P...I think your will has\x01",
            "broken through the\x01",
            "Barrier called Arios.\x02\x03",
            "#00208FAnd also, it dispelled\x01",
            "the darkness of the\x01",
            "story of Guy's death...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104F#12PYes... We only helped you\x01",
            "to do it.\x02\x03",
            "#00108FAlthough I can't say\x01",
            "you'll need just some\x01",
            "help with what's ahead...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_866C")

    ChrTalk(
        0x106,
        "#10703F#12P...You're right...\x02",
    )

    CloseMessageWindow()
    Jump("loc_86D5")

    label("loc_866C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_86A4")

    ChrTalk(
        0x109,
        "#10106F#12P...You're right...\x02",
    )

    CloseMessageWindow()
    Jump("loc_86D5")

    label("loc_86A4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_86D5")

    ChrTalk(
        0x105,
        "#10406F#12P...That's right.\x02",
    )

    CloseMessageWindow()

    label("loc_86D5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_871B")

    ChrTalk(
        0x104,
        (
            "#00308F#12PBell, Lawyer Ian and\x01",
            "Keddo too?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_87B9")

    label("loc_871B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_876E")

    ChrTalk(
        0x105,
        (
            "#10408F#12PMariabell, Mr. Beardy-\x01",
            "Bear and also KeA, eh?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_87B9")

    label("loc_876E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_87B9")

    ChrTalk(
        0x109,
        (
            "#10108F#12PMariabell, Mr. Grimwood\x01",
            "and also KeA, huh?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_87B9")


    ChrTalk(
        0x101,
        "#00006F#11P#30W...Yeah...\x02",
    )

    CloseMessageWindow()
    OP_68(350, 12800, 208640, 1000)
    MoveCamera(37, 17, 0, 1000)

    def lambda_87F9():
        OP_93(0xFE, 0xB4, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_87F9)
    Sleep(300)

    def lambda_8809():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_8809)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#00003F#5PThe last Territory has\x01",
            "been released.\x02\x03",
            "#00000FAnyhow... Let's return\x01",
            "to the Sanctuary\x01",
            "terminus.\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(17740, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0x8, 0x8000)
    SetChrPos(0x0, 0, 12000, 202500, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    OP_37()
    SetScenarioFlags(0x1A9, 4)
    OP_29(0xB2, 0x1, 0x8)
    ModifyEventFlags(0, 0, 0x80)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x164), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x22, 2)
    OP_E2(0x2)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_34_8078 end

    def Function_35_88F0(): pass

    label("Function_35_88F0")

    OP_9B(0x0, 0xFE, 0x162, 0x320, 0x3E8, 0x0)
    Return()

    # Function_35_88F0 end

    def Function_36_8900(): pass

    label("Function_36_8900")

    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_36_8900 end

    def Function_37_890F(): pass

    label("Function_37_890F")

    Sleep(200)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_37_890F end

    def Function_38_8921(): pass

    label("Function_38_8921")

    Sleep(300)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_38_8921 end

    def Function_39_8933(): pass

    label("Function_39_8933")

    Sleep(100)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_39_8933 end

    def Function_40_893F(): pass

    label("Function_40_893F")

    Sleep(400)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_895F")
    Sound(540, 0, 50, 0)
    Jump("loc_8984")

    label("loc_895F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8984")
    Sound(531, 0, 100, 0)

    label("loc_8984")

    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_40_893F end

    def Function_41_898D(): pass

    label("Function_41_898D")

    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_89AD")
    Sound(540, 0, 50, 0)
    Jump("loc_89D2")

    label("loc_89AD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_89D2")
    Sound(531, 0, 100, 0)

    label("loc_89D2")

    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_41_898D end

    def Function_42_89DB(): pass

    label("Function_42_89DB")

    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x10)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x800)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x2)
    SetChrFlags(0x8, 0x1000)
    SetChrFlags(0x8, 0x800)
    Return()

    # Function_42_89DB end

    def Function_43_8A02(): pass

    label("Function_43_8A02")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 1)), scpexpr(EXPR_END)), "loc_8A24")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8B8D")

    label("loc_8A24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 2)), scpexpr(EXPR_END)), "loc_8A3C")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8B8D")

    label("loc_8A3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 3)), scpexpr(EXPR_END)), "loc_8A54")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8B8D")

    label("loc_8A54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 4)), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8A77")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8B8D")

    label("loc_8A77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 5)), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8A9A")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8B8D")

    label("loc_8A9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 6)), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8ABD")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8B8D")

    label("loc_8ABD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_DC(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8ADB")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8B8D")

    label("loc_8ADB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_DC(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8AF9")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8B8D")

    label("loc_8AF9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_DC(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8B17")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8B8D")

    label("loc_8B17")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_DC(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8B40")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8B8D")

    label("loc_8B40")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_DC(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8B69")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8B8D")

    label("loc_8B69")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_DC(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8B8D")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8B8D")

    Return()

    # Function_43_8A02 end

    SaveToFile()

Try(main)
