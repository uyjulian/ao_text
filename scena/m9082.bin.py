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
        "Function_3_7D6",          # 03, 3
        "Function_4_8CC",          # 04, 4
        "Function_5_B50",          # 05, 5
        "Function_6_CA3",          # 06, 6
        "Function_7_D04",          # 07, 7
        "Function_8_D65",          # 08, 8
        "Function_9_D78",          # 09, 9
        "Function_10_613A",        # 0A, 10
        "Function_11_6165",        # 0B, 11
        "Function_12_6190",        # 0C, 12
        "Function_13_61BB",        # 0D, 13
        "Function_14_61E6",        # 0E, 14
        "Function_15_6211",        # 0F, 15
        "Function_16_6235",        # 10, 16
        "Function_17_6247",        # 11, 17
        "Function_18_6259",        # 12, 18
        "Function_19_626B",        # 13, 19
        "Function_20_6277",        # 14, 20
        "Function_21_62C5",        # 15, 21
        "Function_22_6313",        # 16, 22
        "Function_23_633C",        # 17, 23
        "Function_24_6386",        # 18, 24
        "Function_25_63B3",        # 19, 25
        "Function_26_63DF",        # 1A, 26
        "Function_27_6402",        # 1B, 27
        "Function_28_644B",        # 1C, 28
        "Function_29_6494",        # 1D, 29
        "Function_30_64B0",        # 1E, 30
        "Function_31_6524",        # 1F, 31
        "Function_32_8225",        # 20, 32
        "Function_33_826E",        # 21, 33
        "Function_34_82D8",        # 22, 34
        "Function_35_8BA1",        # 23, 35
        "Function_36_8BB1",        # 24, 36
        "Function_37_8BC0",        # 25, 37
        "Function_38_8BD2",        # 26, 38
        "Function_39_8BE4",        # 27, 39
        "Function_40_8BF0",        # 28, 40
        "Function_41_8C3E",        # 29, 41
        "Function_42_8C8C",        # 2A, 42
        "Function_43_8CB3",        # 2B, 43
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CF, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_783")

    ChrTalk(
        0x8,
        "............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001F...He's lost consciousness completely.\x01",
            "His life doesn't seem to be in danger too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FAs expected, he was one hell of an opponent...\x01",
            "To think he did that much against all of us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00208FNothing less from the "Divine Blade of Wind"...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_671")

    ChrTalk(
        0x10A,
        "#00603FHmph...I'm glad we won.\x02",
    )

    CloseMessageWindow()

    label("loc_671")


    ChrTalk(
        0x101,
        (
            "#00003FShizuku is probably worried. I'd like to carry\x01",
            "him back to the Merkabah immediately, but...\x02\x03",
            "#00001F...Miss Mariabell and Lawyer Ian\x01",
            "are lying in wait for us ahead.\x02\x03",
            "#00003FI'm sorry for him, but\x01",
            "let's carry him back later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FRight...let's go.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1CF, 0)
    Jump("loc_7D2")

    label("loc_783")


    ChrTalk(
        0x8,
        "............\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It seems he has lost consciousness completely.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_7D2")

    TalkEnd(0x8)
    Return()

    # Function_2_517 end

    def Function_3_7D6(): pass

    label("Function_3_7D6")

    OP_F4(0x2)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is an orbment charging station.\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Rest Here\x01",      # 0
            "Quit\x01",           # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8BD")
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

    label("loc_8BD")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_3_7D6 end

    def Function_4_8CC(): pass

    label("Function_4_8CC")

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

    def lambda_9DC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_9DC)

    def lambda_9ED():
        OP_95(0xFE, -240, 12000, 218120, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_9ED)
    Sleep(500)
    PlayEffect(0x1, 0xFF, 0x1, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_A44():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_A44)

    def lambda_A55():
        OP_95(0xFE, -1420, 12000, 218280, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_A55)
    Sleep(500)
    Sound(920, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x2, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_AB2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2, 2, lambda_AB2)

    def lambda_AC3():
        OP_95(0xFE, 1060, 12000, 218310, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_AC3)
    Sleep(500)
    PlayEffect(0x1, 0xFF, 0x3, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_B1A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x3, 2, lambda_B1A)

    def lambda_B2B():
        OP_95(0xFE, -2780, 12000, 218680, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_B2B)
    WaitChrThread(0x3, 1)
    Sleep(500)
    OP_E2(0x2)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_4_8CC end

    def Function_5_B50(): pass

    label("Function_5_B50")

    EventBegin(0x0)
    OP_E2(0x3)
    LoadEffect(0x1, "event/evwarp.eff")
    Sound(936, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x0, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_BA9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_BA9)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0x1, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_BF4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_BF4)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0x2, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_C3F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2, 2, lambda_C3F)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0x3, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_C8A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x3, 2, lambda_C8A)
    Sleep(1000)
    NewScene("m9008", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_5_B50 end

    def Function_6_CA3(): pass

    label("Function_6_CA3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CBB")
    LoadChrToIndex("chr/ch03150.itc", 0x23)

    label("loc_CBB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CD3")
    LoadChrToIndex("chr/ch03250.itc", 0x23)

    label("loc_CD3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CEB")
    LoadChrToIndex("chr/ch02950.itc", 0x23)

    label("loc_CEB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D03")
    LoadChrToIndex("chr/ch00950.itc", 0x23)

    label("loc_D03")

    Return()

    # Function_6_CA3 end

    def Function_7_D04(): pass

    label("Function_7_D04")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D1C")
    LoadChrToIndex("chr/ch03150.itc", 0x24)

    label("loc_D1C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D34")
    LoadChrToIndex("chr/ch03250.itc", 0x24)

    label("loc_D34")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D4C")
    LoadChrToIndex("chr/ch02950.itc", 0x24)

    label("loc_D4C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D64")
    LoadChrToIndex("chr/ch00950.itc", 0x24)

    label("loc_D64")

    Return()

    # Function_7_D04 end

    def Function_8_D65(): pass

    label("Function_8_D65")

    EventBegin(0x0)
    StopBGM(0xFA0)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    EventEnd(0x5)
    Return()

    # Function_8_D65 end

    def Function_9_D78(): pass

    label("Function_9_D78")

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

    def lambda_106B():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_106B)
    Sleep(50)

    def lambda_1083():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1083)
    Sleep(50)

    def lambda_109B():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_109B)
    Sleep(50)

    def lambda_10B3():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_10B3)
    Sleep(50)

    def lambda_10CB():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_10CB)
    Sleep(50)

    def lambda_10E3():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_10E3)
    OP_0D()
    Sleep(2400)
    OP_C9(0x0, 0x80000000)

    NpcTalk(
        0x8,
        "Man's Voice",
        "#4064V#6P#30W#16A──So you have arrived.\x02",
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
        "#00001F#12P...Mr. Arios.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301F#12PYou aren't wearin' that\x01",
            "secretary outfit anymore...?\x02",
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
            "Although it was requested by\x01",
            "Mr. Crois, it was unnatural\x01",
            "to me since the beginning.\x02\x03",
            "After the state independence\x01",
            "declaration of invalidity, I\x01",
            "have no right to wear that.\x02\x03",
            "Just think about me \x01",
            "standing here...\x02\x03",
            "Neither as the Secretary of\x01",
            "Defense, nor as a Bracer, but\x01",
            "as a mere ruffian fencer.\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_14AE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1489")
    OP_FC(0xFFF4)
    Jump("loc_148C")

    label("loc_1489")

    OP_FC(0xC)

    label("loc_148C")


    ChrTalk(
        0x10A,
        "#00600F#13PMacLaine...\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_14F9")

    label("loc_14AE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_14F9")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_14D8")
    OP_FC(0xFFF4)
    Jump("loc_14DB")

    label("loc_14D8")

    OP_FC(0xC)

    label("loc_14DB")


    ChrTalk(
        0x109,
        "#10113F#13PMr. Arios...\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_14F9")


    ChrTalk(
        0x102,
        "#00108F#12PWhy are you...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00206F#12P...Too honest.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00004F#12P...Ha ha, damn...\x02\x03",
            "#00008FI have so many things I want to ask you\x01",
            "that I can't sort them out, but...\x02\x03",
            "#00000FFirst of all, do you mind\x01",
            "replying to some of my questions...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01404FNo#5P──that was my intention.\x02\x03",
            "#01400FAsk away...\x01",
            "I'll answer every question,\x01",
            "one by one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003F#12PThen...\x02",
    )

    CloseMessageWindow()
    ClearScenarioFlags(0x0, 3)
    ClearScenarioFlags(0x0, 0)
    ClearScenarioFlags(0x0, 1)
    ClearScenarioFlags(0x0, 2)

    label("loc_1697")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4036")
    FadeToDark(300, 0, 100)
    OP_0D()
    MenuCmd(0, 0)
    MenuCmd(1, 0, "About the "Accident" Five Years Ago")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1709")
    MenuCmd(1, 0, "About the Relationship with Lawyer Ian")

    label("loc_1709")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1735")
    MenuCmd(1, 0, "About KeA and the Black Auction")

    label("loc_1735")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1758")
    MenuCmd(1, 0, "About the Day Guy Died")

    label("loc_1758")

    MenuCmd(2, 0, -1, -1, 0)
    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1792"),
        (1, "loc_26D9"),
        (2, "loc_32A3"),
        (3, "loc_4029"),
        (SWITCH_DEFAULT, "loc_4031"),
    )


    label("loc_1792")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_250E")

    ChrTalk(
        0x101,
        (
            "#00008F#12P...I'm very sorry for asking\x01",
            "about a painful thing, but...\x02\x03",
            "#00001FCould you tell me about the\x01",
            ""accident" five years ago...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01403F#5PYes...\x01",
            "No need to hide it anymore.\x02\x03",
            "#01400FThe explosion accident of the truck that\x01",
            "happened on the main street five years ago...\x02\x03",
            "Like you all have already realized, it\x01",
            "happened as a result of the intelligence\x01",
            "war between the Empire and the Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00106F#12PAs we thought...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1AF7")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_197F")
    OP_FC(0xFFF4)
    Jump("loc_1982")

    label("loc_197F")

    OP_FC(0xC)

    label("loc_1982")


    ChrTalk(
        0x10A,
        "#00608F#13P............\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x8,
        (
            "#01402F#5PHu hu, naturally Section\x01",
            "One knew the truth, right?\x02\x03",
            "#01403FAccording to the top brass judgment concerned\x01",
            "with the Imperial and Republican factions, \x01",
            "it was abandoned as a matter of course, but...\x02\x03",
            "#01400FEven if I was disappointed in the fact itself,\x01",
            "now I don't have any resentments.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        "#00606F#13P...I can't say anything.\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_1AF7")


    ChrTalk(
        0x103,
        (
            "#00208F#12P...And so Mr. Arios'\x01",
            "wife and Shizuku...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01403F#5PYes... Saya lost her life,\x01",
            "while Shizuku lost her sight.\x02\x03",
            "#01408FFive years have passed since then...\x01",
            "With the consolidation of both countries'\x01",
            "intelligence agencies, insignificant\x01",
            "sabotage activities have ceased, but...\x02\x03",
            "#01401FAs a result of many years of a secret feud,\x01",
            "victims like Saya, Shizuku and others\x01",
            "appeared in no small numbers.\x02\x03",
            "#01403FLloyd── that includes your parents,\x01",
            "and Mr. Grimwood's family too.\x02",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17C, 6)), scpexpr(EXPR_END)), "loc_1F09")

    ChrTalk(
        0x102,
        (
            "#00101F#12PI-I'm sure that \x01",
            "Lloyd's parents...!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00208F#12PFifteen years ago, in an airship accident...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#12PYeah...exactly like I told you before.\x02\x03",
            "#00008FI had just started noticing things around me,\x01",
            "so I almost don't remember about it...\x02\x03",
            "#00013FSo, at that time...\x01",
            "Lawyer Ian's family too?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2060")

    label("loc_1F09")


    ChrTalk(
        0x102,
        "#00105F#12PL-Loyd parents!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00206F#12P...It is the first time I hear about this...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#12PMy parents...\x01",
            "Passed away in an airship accident\x01",
            "that had just gone into commission...\x02\x03",
            "#00008FI had just started noticing things around me,\x01",
            "so I almost don't remember about it...\x02\x03",
            "#00013FSo, at that time...\x01",
            "Lawyer Ian's family too?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2060")


    ChrTalk(
        0x8,
        (
            "#01403F#5PYes, I've heard his wife and child\x01",
            "were riding on that too.\x02\x03",
            "I was left with Shizuku, but...\x01",
            "I can't even imagine his grief and\x01",
            "sorrow for having lost everything.\x02\x03",
            "#01400FAlso, at that time Guy and Mr. Grimwood\x01",
            "knew each other as bereaved families.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F#12P............\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_21D8")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_21AF")
    OP_FC(0xFFF4)
    Jump("loc_21B2")

    label("loc_21AF")

    OP_FC(0xC)

    label("loc_21B2")


    ChrTalk(
        0x109,
        "#10106F#13P...S-Such a thing...\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_21D8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_223F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2202")
    OP_FC(0xFFF4)
    Jump("loc_2205")

    label("loc_2202")

    OP_FC(0xC)

    label("loc_2205")


    ChrTalk(
        0x10A,
        (
            "#00606F#13PNot even Section One\x01",
            "got hold of this...\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_223F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_22AF")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2269")
    OP_FC(0xFFF4)
    Jump("loc_226C")

    label("loc_2269")

    OP_FC(0xC)

    label("loc_226C")


    ChrTalk(
        0x105,
        (
            "#10401F#13P...I see. To think there\x01",
            "was such a connection...\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_22AF")


    ChrTalk(
        0x8,
        (
            "#01403F#5P...Then, after the incident of five\x01",
            "years ago, I retired from the police\x01",
            "and knocked at the Bracer Guild door.\x02\x03",
            "Disappointment towards the police, working\x01",
            "out a solution for Shizuku's hospitalization\x01",
            "costs... I had many reasons, but...\x02\x03",
            "#01408FPut it simply, maybe I was only running\x01",
            "away from the sorrow of having lost Saya.\x02\x03",
            "#01400FAfter all, if someone wants to, he can immerse\x01",
            "himself in Bracer jobs as much as he likes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008F#12PMr. Arios...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2506")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_24AE")
    OP_FC(0xFFF4)
    Jump("loc_24B1")

    label("loc_24AE")

    OP_FC(0xC)

    label("loc_24B1")


    ChrTalk(
        0x106,
        (
            "#10706F#13P(...Even the families of the targets\x01",
            ""Yin" has killed until now...)\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_2506")

    SetScenarioFlags(0x0, 0)
    Jump("loc_26D4")

    label("loc_250E")


    ChrTalk(
        0x8,
        (
            "#01403F#5PThe explosion accident of the truck that\x01",
            "took away Saya's life and Shizuku's sight that\x01",
            "happened on the main street five years ago...\x02\x03",
            "#01401FThat happened as a result of the intelligence\x01",
            "war between the Empire and the Republic.\x02\x03",
            "Also, even the airship incident of fifteen\x01",
            "years ago happened for the same motive.\x02\x03",
            "#01403FAs a result... Yours and Guy's parents, and\x01",
            "Mr. Grimwood's family lives were taken away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008F#12P............\x02",
    )

    CloseMessageWindow()

    label("loc_26D4")

    Jump("loc_4031")

    label("loc_26D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3197")

    ChrTalk(
        0x101,
        (
            "#00006F#12P...I've always had some\x01",
            "doubts about this, but...\x02\x03",
            "#00001FWhy did, someone like yourself, decide\x01",
            "to join with Mr. Dieter and the others?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        "#01405F#5POoh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#12P...It's true that "uncle" and Mariabell are\x01",
            "knowledgeable about finance, monetary\x01",
            "circulation and information about the Cult\x01",
            "they were related to as the Crois clan, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F#12PThe behind the scenes feud\x01",
            "between the Empire and Republic...\x02\x03",
            "#00301FIt seems a little strange they'd\x01",
            "have known even about that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F#12PYou do not have points of contact...\x02\x03",
            "#00201FAnd yet, Mr. Dieter, who became President,\x01",
            "designated Mr. Arios as the Secretary of Defense...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2A57")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_29BD")
    OP_FC(0xFFF4)
    Jump("loc_29C0")

    label("loc_29BD")

    OP_FC(0xC)

    label("loc_29C0")


    ChrTalk(
        0x10A,
        (
            "#00606F#13P...I see, so that's it.\x02\x03",
            "#00601FIt means that what connects\x01",
            "you both is Lawyer Ian, eh?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00001F#12PYes...\x01",
            "──Are we wrong?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BD0")

    label("loc_2A57")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2B21")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2A81")
    OP_FC(0xFFF4)
    Jump("loc_2A84")

    label("loc_2A81")

    OP_FC(0xC)

    label("loc_2A84")


    ChrTalk(
        0x105,
        (
            "#10406F#13P...I see, so that's it.\x02\x03",
            "#10401FIt means that what connects\x01",
            "you both is Mr. Beardy-Bear, eh?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00001F#12PYeah...\x01",
            "──Are we wrong?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BD0")

    label("loc_2B21")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2BD0")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2B4B")
    OP_FC(0xFFF4)
    Jump("loc_2B4E")

    label("loc_2B4B")

    OP_FC(0xC)

    label("loc_2B4E")


    ChrTalk(
        0x109,
        (
            "#10108F#13PCould it be that...\x02\x03",
            "#10101FWhat connects you\x01",
            "both is Mr. Grimwood...?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00001F#12PYeah...\x01",
            "──Are we wrong?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BD0")


    ChrTalk(
        0x8,
        "#01404F#5PHu hu...it's like you say.\x02",
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
            "#01402FLike you all, in our police days,\x01",
            "Guy and I were helped a lot by\x01",
            "Mr. Grimwood's information.\x02\x03",
            "He's a well-informed person who\x01",
            "collaborated as a civil advisor even \x01",
            "in the Cult lodges suppress operation.\x02\x03",
            "#01403FThen, even after I became a Bracer...\x01",
            "I frequently exchanged intel with him.\x02",
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
            "#01403F#5POn the other hand, Mr. Grimwood was acquainted\x01",
            "with the Croises through IBC judicial affairs.\x02\x03",
            "#01401FThen── all information and elements were\x01",
            "collected and synthesised by him.\x02\x03",
            "Mr. Crois was guided by him and Crossbell\x01",
            "independence was achieved with many political \x01",
            "maneuverings and the "Sept-Terrion"'s power.\x02\x03",
            "#01403FWithout knowing that, behind his back, \x01",
            "the true plan was being advanced by \x01",
            "him and Miss Mariabell.\x02",
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
        "#00108F#12PThe "Azure-Zero Project"...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01403F#5PRight... Mr. Grimwood had quickly realized \x01",
            "the truth about Saya and the others' incident.\x02\x03",
            "Then, he frankly told me the circumstances...\x01",
            "And I decided to cooperate to the project too.\x02\x03",
            "#01400FThis is the whole story.\x02",
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
            "#00206F#12PEverything went how Lawyer Ian\x01",
            "and Miss Mariabell wanted...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00301F#12P...It's an incredible story.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_329E")

    label("loc_3197")


    ChrTalk(
        0x8,
        (
            "#01403F#5PMr. Crois and I...\x01",
            "What connected us, who don't have anything\x01",
            "in common was none other than Mr. Grimwood.\x02\x03",
            "He quickly noticed the truth about\x01",
            "the accident of five years before and\x01",
            "invited me to the "Azure-Zero Project"...\x02\x03",
            "#01400FThen, I accepted.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_329E")

    Jump("loc_4031")

    label("loc_32A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3EAB")

    ChrTalk(
        0x101,
        (
            "#00006F#12P...Likewise, this too is something\x01",
            "I had my doubts about, but...\x02\x03",
            "#00013FIt was you, Mr. Arios, who took out KeA\x01",
            "from the "Fort of Sun" underground, right?\x02\x03",
            "And then, you switched a Rosenberg doll to be\x01",
            "displayed at the "Black Auction" with her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105F#12PN-Now that you mention it...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#12PIndeed, that question had never\x01",
            "been completely solved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01404F#5PYes, precisely.\x02\x03",
            "#01402FRegarding that, it wasn't Mr. Grimwood's\x01",
            "initiative, but Miss Mariabell's.\x02",
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
            "#01403FIt seems that she had completely\x01",
            "understood Joachim's moves...\x02\x03",
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
            "#01403FThen, I switched a Rosenberg doll I was\x01",
            "carrying from Remiferia with that child.\x01\x02\x03",
            "#01400FEven the body of that Rosenberg doll\x01",
            "itself was prepared by Miss Mariabell\x01",
            "so the Revache party wouldn't notice.\x02",
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
            "#00006F#12PHowever...\x01",
            "What sense had for Miss Mariabell\x01",
            "to do such a thing?\x02\x03",
            "#00013FIf she needed KeA for the project, she could've\x01",
            "taken custody of her just like that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01403F#5PFirst, it was to involve the "Heiyue"\x01",
            "and make the Revache party lose their face,\x01",
            "the first step to their ruin...\x02\x03",
            "#01400FIf she had woken up at the\x01",
            "Black Auction, Miss Mariabell\x01",
            "would have acted.\x02\x03",
            "In front of the agitated guests and Marconi,\x01",
            "she was probably planning to volunteer to\x01",
            "keep custody of her using the IBC name.\x02\x03",
            "#01404FIf the "Heiyue" had acted, there\x01",
            "would've been a different development...\x02\x03",
            "At any rate, at that time,\x01",
            "I was hiding in the venue too.\x02\x03",
            "#01402FNo matter the development, we had\x01",
            "prepared to cope with the situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#12PWhat can I say...\x01",
            "That's too amazin'.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00211F#12PToo thoroughly prepared...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3B15")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3AB7")
    OP_FC(0xFFF4)
    Jump("loc_3ABA")

    label("loc_3AB7")

    OP_FC(0xC)

    label("loc_3ABA")


    ChrTalk(
        0x106,
        (
            "#10708F#13P...Indeed, at that time, \x01",
            "I felt a presence like \x01",
            "someone was in hiding...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B15")


    ChrTalk(
        0x8,
        (
            "#01403F#5PAlso, second...\x02\x03",
            "#01401FIt was to probe the potential by\x01",
            "making the "Sept-Terrion" awaken\x01",
            "in such a unique situation.\x02",
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
        "#00205F#12PTo probe KeA's potential?\x02",
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
            "#01403F#5PWell── It was just Miss\x01",
            "Mariabell who said that.\x02\x03",
            "#01408FProbably a condition to\x01",
            "awake that child from\x01",
            "her long slumber...\x02\x03",
            "#01400FIn any case, was it for the Goddess \x01",
            "guidance or for a mere coincidence,\x01",
            "she woke up in front of you all.\x02\x03",
            "It should've been completely\x01",
            "unexpected to Miss Mariabell, but...\x02\x03",
            "#01403FIncluding that you took in that child\x01",
            "and even started living together,\x01",
            "it seems she well accepted that.\x02",
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
            "#00306F#12P...It's no use.\x01",
            "I don't get it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#12P...Bell...\x01",
            "What in the world are you planning...?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4024")

    label("loc_3EAB")


    ChrTalk(
        0x8,
        (
            "#01403F#5PFreeing KeA from the "Fort of Sun"\x01",
            "and taking her at the Black Auction\x01",
            "place was Miss Mariabell's initiative.\x02\x03",
            "#01408FHer purpose seemed to be to lead\x01",
            "Revache to ruin and even to\x01",
            "control the situation, but...\x02\x03",
            "#01401FIt seems she also had the goal to\x01",
            "awaken her in a unique situation\x01",
            "and probe her potential.\x02\x03",
            "#01403FSadly, even I don't know\x01",
            "any more than that.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4024")

    Jump("loc_4031")

    label("loc_4029")

    SetScenarioFlags(0x0, 3)
    Jump("loc_4031")

    label("loc_4031")

    Jump("loc_1697")

    label("loc_4036")

    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00006F#12P#30W...Well then...\x02\x03",
            "#00008FAbout the day my big brother died...\x01",
            "...Could you tell me the truth?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_410A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_40E9")
    OP_FC(0xFFF4)
    Jump("loc_40EC")

    label("loc_40E9")

    OP_FC(0xC)

    label("loc_40EC")


    ChrTalk(
        0x10A,
        "#00601F#13P............\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_410A")


    ChrTalk(
        0x103,
        "#00208F#12P......Ah......\x02",
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
        "#01400F#5P#30WVery well──\x02",
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
            "#3C#30W...Two years after I left the police\x01",
            "following Saya's passing away...\x02\x03",
            "I was cooperating to the project with Mr. Grimwood\x01",
            "and the others, accomplishing many things...\x02\x03",
            "All shady...\x01",
            "Nothing but plot intrigues.\x02\x03",
            "However, starting with the fact that\x01",
            "I was connected to the Guild, in the end,\x01",
            "no one had an inkling about those.\x02\x03",
            "Except for Guy Bannings...\x01",
            "My former partner.\x02",
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
            "and secrets with an absurdly keen\x01",
            "nose and tenaciousness.\x02\x03",
            "The Empire and Republic secret feud...\x02\x03",
            "Chairman Hartmann and Revache,\x01",
            "the actions of the D∴G Cult remnants...\x02\x03",
            "Furthermore, even the hidden\x01",
            "project of the Crois clan...\x02\x03",
            "Then──\x02\x03",
            "On that rainy day, Guy called me\x01",
            "at the Orchis Tower, of which works\x01",
            "had just started, construction site...\x02",
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
            "#3C#30WNaturally, he didn't catch even\x01",
            "the project details, but...\x02\x03",
            "Guy's conjecture perceived the project\x01",
            "whole picture with a shocking accuracy.\x02\x03",
            "Mr. Crois, who used the Cult and the mafia,\x01",
            "stepping forward into the political world...\x02\x03",
            "Stirring the opportunity for independence\x01",
            "by having Crossbell City attacked feigning\x01",
            "it was the act of a foreign power...\x02\x03",
            "Furthermore, the fact of intimidating and\x01",
            "taking control over the whole Zemuria with\x01",
            ""something" from the Crois clan...\x02\x03",
            "Unbelievably, he unexpectedly\x01",
            "pointed out even that.\x02\x03",
            "Then──\x02",
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
            "#3C#30W...Guy didn't accept my\x01",
            "words to back out of that...\x02\x03",
            "We began a duel to the death amidst the rain.\x02\x03",
            "My skills were quite better...\x01",
            "However, Guy was brimming with a\x01",
            "strength coming from a solid will.\x02\x03",
            "We exchanged blows several times and\x01",
            "while scrambling for each other's physical \x01",
            "strength, the death duel went on in the rain...\x02\x03",
            "Then──\x02",
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
            "#3C#30WThen Guy...\x01",
            "Lost his life.\x02\x03",
            "Naturally, it was I who took away\x01",
            "his tonfas from the scene.\x02\x03",
            "Because I didn't want to be identified as the culprit\x01",
            "from the countless sword cuts carved on them.\x07\x00\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4CE2")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4C94")
    OP_FC(0xFFF4)
    Jump("loc_4C97")

    label("loc_4C94")

    OP_FC(0xC)

    label("loc_4C97")


    ChrTalk(
        0x109,
        "#10106F#13P#30WSuch a thing...\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x103,
        "#00208F#12P#30W............\x02",
    )

    CloseMessageWindow()
    Jump("loc_4D32")

    label("loc_4CE2")


    ChrTalk(
        0x101,
        "#00008F#12P#30W............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00206F#12P#30W...That's what happened...\x02",
    )

    CloseMessageWindow()

    label("loc_4D32")

    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x8)
    Sleep(500)

    ChrTalk(
        0x8,
        (
            "#01403F#5P#30W...This is the outline of the incident\x01",
            "that happened on that rainy day.\x02\x03",
            "#01408FThat afterwards a mafia underling\x01",
            "appeared and went away with Guy's\x01",
            "badge was beyond my expectations...\x02\x03",
            "#01400FIn any case, with this, your doubts\x01",
            "should've gotten substantially an answer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003F#12P──No.\x02",
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
            "#00006F#12PI'm sure you know this, but my big\x01",
            "brother's cause of death was a shoot-out.\x02\x03",
            "#00001FIt seems you didn't explain\x01",
            "about that...?\x02",
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
            "opponent, I used even that...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_50F3")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5015")
    OP_FC(0xFFF4)
    Jump("loc_5018")

    label("loc_5015")

    OP_FC(0xC)

    label("loc_5018")


    ChrTalk(
        0x10A,
        (
            "#00606F#13PLies── MacLaine.\x02\x03",
            "#00601FAs if you could've had the\x01",
            "room to use a different weapon\x01",
            "in such a death duel.\x02\x03",
            "To say nothing of being impossible to give the\x01",
            "final blow to your opponent from his back.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_51D3")

    label("loc_50F3")


    ChrTalk(
        0x101,
        (
            "#00013F#12P──That's a lie.\x02\x03",
            "#00006FThere's no way you could've had the\x01",
            "room to use a different weapon in\x01",
            "such a death duel.\x02\x03",
            "#00001FMuch less of being impossible to give the\x01",
            "final blow to your opponent from his back.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_51D3")

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
        (
            "#00108F#12PJust "who" shot\x01",
            "Mr. Guy...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00201F#12P...Please talk.\x02",
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
            "#01403F#5P#30W──Say what you want,\x01",
            "but who killed Guy was \x01",
            "none other than me.\x02\x03",
            "#01400FThen, I...\x01",
            "Chose the path to collaborate with the project\x01",
            "that even made my former partner a victim.\x02\x03",
            "Then, even now...\x01",
            "I'm trying to make complete a project\x01",
            "that uses an innocent girl's feelings.\x02\x03",
            "#01403FEverything because of Saya...\x01",
            "And also, for Shizuku's future.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F#12P...Mr. Arios...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#12PDo you think that Shizuku would be\x01",
            "happy that you're doing such things...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01403F#5P#30WOf course not.\x02\x03",
            "#01401FHowever──\x01",
            "The curse of the land called Crossbell stole\x01",
            "away from that child her mother and the light.\x02\x03",
            "Then, as long as Crossbell holds\x01",
            "this position in the continent,\x01",
            "the curse will never vanish.\x02\x03",
            "#01403F──Unless a "miracle" transcending\x01",
            "the logic of the human world happens.\x02",
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
            "#01400F#5P#30WThree years ago, Guy...\x01",
            "Without even blaming me, lost his life\x01",
            "at the end of a duel to the death.\x02\x03",
            "Then, KeA, who became a "Sept-Terrion",\x01",
            "healed Shizuku's eyes.\x02\x03",
            "#01403FNow for me──\x01",
            "It's impossible to go back.\x02",
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
            "#01403F#5P#30W...If you can't comply,\x01",
            "try stopping me with force...\x02\x03",
            "#01401FUsing those tonfas your brother left you...\x02\x03",
            "#01407FShow me that you'll admirably take\x01",
            "revenge for him and open the path to\x01",
            "take back what is precious to you...!\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xBB8)

    ChrTalk(
        0x101,
        (
            "#00006F#12P...Understood.\x02\x03",
            "#00001FHowever── I've got no intention\x01",
            "to avenge my big brother.\x02",
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
            "#00003F#12PAs a modest duty post that\x01",
            "was started by inheriting\x01",
            "Guy Banning's will...\x02\x03",
            "#00001FStarting from Shizuku, as the\x01",
            ""Special Support Section" that was\x01",
            "entrusted with the feelings of many people...\x02\x03",
            "#00007FI'll get over the "barrier" that is you,\x01",
            "take KeA back...\x01",
            "And solve this case in its real sense!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x8,
        "#01405F#5P...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302F#12PHa ha...\x01",
            "That's our leader!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101F#12PEven for Shizuku who's waiting\x01",
            "at Orchis Tower...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00201F#12P...We'll never back down...!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5C00")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5BD5")
    OP_FC(0xFFF4)
    Jump("loc_5BD8")

    label("loc_5BD5")

    OP_FC(0xC)

    label("loc_5BD8")


    ChrTalk(
        0x10A,
        (
            "#00604F#13PHmph...\x01",
            "Hopeless guys.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_5C00")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5C6C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5C2A")
    OP_FC(0xFFF4)
    Jump("loc_5C2D")

    label("loc_5C2A")

    OP_FC(0xC)

    label("loc_5C2D")


    ChrTalk(
        0x105,
        (
            "#10402F#13PHu hu...\x01",
            "This is the Support Section's style.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_5C6C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5CD5")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5C96")
    OP_FC(0xFFF4)
    Jump("loc_5C99")

    label("loc_5C96")

    OP_FC(0xC)

    label("loc_5C99")


    ChrTalk(
        0x109,
        "#10107F#13PI'll support you with everything I've got!\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_5CD5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5D75")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5CFF")
    OP_FC(0xFFF4)
    Jump("loc_5D02")

    label("loc_5CFF")

    OP_FC(0xC)

    label("loc_5D02")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5D43")

    ChrTalk(
        0x106,
        "#10701F#13PMe too...as much as I can!\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_5D75")

    label("loc_5D43")


    ChrTalk(
        0x106,
        "#10707F#13PI'll help you with all my might!\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_5D75")

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
        "#01404F#4077V#5P#30W#25AHu hu── very well.\x02",
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
            "#4065V#40W#55AEight Leaves One Blade...\x01",
            "certified fencer of the Second\x01",
            "Form secrets, Arios MacLaine...\x02\x03",
            "#4066V#60ADue to personal circumstances,\x01",
            "I'll infringe justice, stray from\x01",
            "the path and act up as I please!\x02\x03",
            "#4067V#30ACome── Special Support Section!\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6066")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_605D")
    OP_FC(0x4)
    Sound(2478, 255, 100, 4)
    Jump("loc_6066")

    label("loc_605D")

    OP_FC(0x3)
    Sound(2478, 255, 100, 3)

    label("loc_6066")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6099")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6093")
    Sound(2417, 255, 100, 4)
    Jump("loc_6099")

    label("loc_6093")

    Sound(2417, 255, 100, 3)

    label("loc_6099")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_60CC")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_60C6")
    Sound(2544, 255, 100, 4)
    Jump("loc_60CC")

    label("loc_60C6")

    Sound(2544, 255, 100, 3)

    label("loc_60CC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_60FF")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_60F9")
    Sound(3174, 255, 100, 4)
    Jump("loc_60FF")

    label("loc_60F9")

    Sound(3174, 255, 100, 3)

    label("loc_60FF")

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

    # Function_9_D78 end

    def Function_10_613A(): pass

    label("Function_10_613A")

    OP_9B(0x0, 0xFE, 0x0, 0x1770, 0xFA0, 0x1)
    OP_96(0xFE, 0x0, 0x2EE0, 0x318BC, 0xFA0, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_10_613A end

    def Function_11_6165(): pass

    label("Function_11_6165")

    OP_9B(0x0, 0xFE, 0x0, 0x157C, 0xFA0, 0x1)
    OP_96(0xFE, 0x460, 0x2EE0, 0x313E4, 0xFA0, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_11_6165 end

    def Function_12_6190(): pass

    label("Function_12_6190")

    OP_9B(0x0, 0xFE, 0x0, 0x157C, 0xFA0, 0x1)
    OP_96(0xFE, 0x1A4, 0x2EE0, 0x30EB2, 0xFA0, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_12_6190 end

    def Function_13_61BB(): pass

    label("Function_13_61BB")

    OP_9B(0x0, 0xFE, 0x0, 0x157C, 0xFA0, 0x1)
    OP_96(0xFE, 0xFFFFFB0A, 0x2EE0, 0x3116E, 0xFA0, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_13_61BB end

    def Function_14_61E6(): pass

    label("Function_14_61E6")

    OP_9B(0x0, 0xFE, 0x0, 0x1996, 0xFA0, 0x1)
    OP_96(0xFE, 0xFFFFF614, 0x2EE0, 0x313DA, 0xFA0, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_14_61E6 end

    def Function_15_6211(): pass

    label("Function_15_6211")

    OP_9B(0x0, 0xFE, 0x0, 0x1AC2, 0xFA0, 0x1)
    OP_96(0xFE, 0x9EC, 0x2EE0, 0x31312, 0xFA0, 0x0)
    Return()

    # Function_15_6211 end

    def Function_16_6235(): pass

    label("Function_16_6235")

    Sleep(150)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_16_6235 end

    def Function_17_6247(): pass

    label("Function_17_6247")

    Sleep(300)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_17_6247 end

    def Function_18_6259(): pass

    label("Function_18_6259")

    Sleep(450)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_18_6259 end

    def Function_19_626B(): pass

    label("Function_19_626B")

    Sleep(450)
    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_19_626B end

    def Function_20_6277(): pass

    label("Function_20_6277")

    Sleep(600)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6297")
    Sound(540, 0, 50, 0)
    Jump("loc_62BC")

    label("loc_6297")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_62BC")
    Sound(531, 0, 100, 0)

    label("loc_62BC")

    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_20_6277 end

    def Function_21_62C5(): pass

    label("Function_21_62C5")

    Sleep(750)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_62E5")
    Sound(540, 0, 50, 0)
    Jump("loc_630A")

    label("loc_62E5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_630A")
    Sound(531, 0, 100, 0)

    label("loc_630A")

    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_21_62C5 end

    def Function_22_6313(): pass

    label("Function_22_6313")

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

    # Function_22_6313 end

    def Function_23_633C(): pass

    label("Function_23_633C")

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

    # Function_23_633C end

    def Function_24_6386(): pass

    label("Function_24_6386")

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

    # Function_24_6386 end

    def Function_25_63B3(): pass

    label("Function_25_63B3")

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

    # Function_25_63B3 end

    def Function_26_63DF(): pass

    label("Function_26_63DF")

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

    # Function_26_63DF end

    def Function_27_6402(): pass

    label("Function_27_6402")

    PlayEffect(0x0, 0x5, 0xFE, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    StopEffect(0x5, 0x2)
    Return()

    # Function_27_6402 end

    def Function_28_644B(): pass

    label("Function_28_644B")

    PlayEffect(0x0, 0x6, 0xFE, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    StopEffect(0x6, 0x2)
    Return()

    # Function_28_644B end

    def Function_29_6494(): pass

    label("Function_29_6494")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_64AF")
    OP_A1(0xFE, 0x4B0, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_29_6494")

    label("loc_64AF")

    Return()

    # Function_29_6494 end

    def Function_30_64B0(): pass

    label("Function_30_64B0")

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

    # Function_30_64B0 end

    def Function_31_6524(): pass

    label("Function_31_6524")

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
            "#01404F#4078V#5P#80W#30A......Hu hu......\x02\x03",
            "#4079V#45ALloyd...and you all too...\x01",
            "...You've really become strong.\x02",
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
            "#00006F#12P#40W......*pant*...*pant*......\x02\x03",
            "#00008FIf it's so...it's because\x01",
            "Mr. Arios was our goal...\x02",
        )
    )

    OP_6F(0x79)
    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#12P#40WIndeed... Without you, maybe\x01",
            "we wouldn't have come this far...\x02",
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
            "#00108F#12P#40WYou were always way further ahead\x01",
            "as a "barrier" to always aim at...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01402F#5P#40WHu hu...honestly...\x02\x03",
            "#01404FAlthough I haven't the slightest\x01",
            "right to be told that...\x02",
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
            "#00003F#12P#30W...Mr. Arios.\x02\x03",
            "#00001FWho shot my big brother on\x01",
            "that day...was Lawyer Ian, right...?\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6A9E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6A79")
    OP_FC(0xFFF4)
    Jump("loc_6A7C")

    label("loc_6A79")

    OP_FC(0xC)

    label("loc_6A7C")


    ChrTalk(
        0x10A,
        "#00605F#13P#30W......!\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_6AF0")

    label("loc_6A9E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6AF0")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6AC8")
    OP_FC(0xFFF4)
    Jump("loc_6ACB")

    label("loc_6AC8")

    OP_FC(0xC)

    label("loc_6ACB")


    ChrTalk(
        0x109,
        "#10105F#13P#30W......Ah......!\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_6AF0")


    ChrTalk(
        0x104,
        "#00301F#12P#30WWell...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01403F#5P#40W............\x02\x03",
            "#01400F...Why do you think so...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#12P#30WIt's a simple elimination process...\x02\x03",
            "#00008F...Thinking about the incident circumstances...\x01",
            "Other suspects aside from Lawyer Ian\x01",
            "would be Mr. Dieter and Miss Mariabell...\x02\x03",
            "#00001FHowever, it appears that the entire plan hadn't \x01",
            "been conveyed to Mr. Dieter and Miss Mariabell\x01",
            "had no connection with my big brother...\x02\x03",
            "#00006FBut...it seems that Lawyer Ian\x01",
            "was very close with him...\x02\x03",
            "Also... Due to his many business trips abroad,\x01",
            "it wouldn't be strange for Lawyer Ian to be\x01",
            "familiar with pistols if needed for self-defense...\x02\x03",
            "#00013F...What do you say?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01403F#5P#40W...60 points...\x02\x03",
            "#01402FBut...it seems I have to\x01",
            "give you a passing mark...\x02",
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
            "It seems we're both at our limit...\x01",
            "Why don't we have a truce for this time?\x02",
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
            "Like you know well, I can't\x01",
            "let you go back from here...\x02\x03",
            "If you want to safely reach your next month's ceremony,\x01",
            "come at me with the intention of killing me...!\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(20, 160, -1, -1)
    SetChrName("Guy")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x14),
            "#40WAs if I could do something like that...\x02\x03",
            "If I did it, I couldn't invite you and\x01",
            "Shizuku to the ceremony, right...?\x02",
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
            "#40WDon't worry... I didn't talk about\x01",
            "your project to anyone...\x02\x03",
            "I had thought to get Dudley's\x01",
            "cooperation, but...\x01",
            "That guy lacks adaptability.\x02\x03",
            "I didn't even consult with\x01",
            "Mr. Sergei, you know...?\x02",
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
            "...Don't you think that, by\x01",
            "hearing this, I would judge it\x01",
            "to be convenient for me...?\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(20, 160, -1, -1)
    SetChrName("Guy")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x14),
            "#30WNo...?\x01",
            "After all, you're awkward.\x02\x03",
            "If you weren't, you wouldn't have come\x01",
            "to such a place alone unconcerned.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(330, 140, -1, -1)
    SetChrName("Arios")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x14),
            "#30WKh...\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(20, 160, -1, -1)
    SetChrName("Guy")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x14),
            "#30WAnyway...why don't we leave it at this\x01",
            "and go have something to drink now?\x02\x03",
            "If we don't do like this, we wouldn't even\x01",
            "had a decent talk in two years...\x02\x03",
            "Let me at least brag about my\x01",
            "younger brother and my fiancｳ.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(240, 150, -1, -1)
    SetChrName("Arios")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x14),
            "#30WHmph...you're always the same.\x02\x03",
            "Your younger brother...\x01",
            "He already turned 15, right?\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(20, 160, -1, -1)
    SetChrName("Guy")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x14),
            "#30WYeah, unlike me, he's quite the prodigy.\x02\x03",
            "I'm thinking of sending him\x01",
            "to high-school somewhere...\x02\x03",
            "...Oh, well. It's raining, so\x01",
            "even "Garante" would be──\x02",
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
            "#60WAh──\x02",
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
            "#30WMr. Grimwood...!?\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(250, 180, -1, -1)
    SetChrName("Guy")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x14),
            "#50W......Ha ha......\x02\x03",
            "...I see...\x01",
            "You were the wirepuller...\x02",
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
            "When I thought about your parents,\x01",
            "I considered to invite you too, but...\x02\x03",
            "In the end, I was able to confirm\x01",
            "that you would've never approved.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(350, 140, -1, -1)
    SetChrName("Arios")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x14),
            "#30W......Mr. Grimwood......\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(200, 200, -1, -1)
    SetChrName("Guy")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x14),
            "#50WHa ha...naturally...\x02\x03",
            "...With you there, Lawyer Ian,\x01",
            "maybe...that project\x01",
            "will go well...\x02\x03",
            "But...I'm sure that...\x01",
            "A substitute for me will appear...\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(40, 160, -1, -1)
    SetChrName("Lawyer Ian")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x14),
            "#30WYes...probably so.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(350, 140, -1, -1)
    SetChrName("Arios")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x14),
            "#30WGuy......!\x01",
            "...Stay with me......!\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(210, 200, -1, -1)
    SetChrName("Guy")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x14),
            "#60W*cough*...*haah*...\x01",
            "...Oh damn...\x02\x03",
            "#80WWith this happening...\x01",
            "Lloyd and...Cecil...\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7B0B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7AE6")
    OP_FC(0xFFF4)
    Jump("loc_7AE9")

    label("loc_7AE6")

    OP_FC(0xC)

    label("loc_7AE9")


    ChrTalk(
        0x10A,
        "#00608F#13P#30W............\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_7B0B")


    ChrTalk(
        0x103,
        "#00213F#12P#30W...Mr. Guy...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108F#12P#30W...So that's what...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00308F#12P#30WWhat an unfortunate story...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#12P#30W...Thank you for telling me\x01",
            "my big brother's final moments.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01404F#5P#40W...Don't thank me...\x02\x03",
            "#01400FLawyer Ian...\x01",
            "Probably won't sway...\x02\x03",
            "And... It seems that KeA's\x01",
            "determination too is firm...\x02\x03",
            "#01404F#50WWill you beat those two or not...?\x01",
            "You'll have to try everything to...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    Sound(898, 0, 100, 0)

    def lambda_7CC6():
        OP_A6(0xFE, 0x0, 0x23, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_7CC6)
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

    # Function_31_6524 end

    def Function_32_8225(): pass

    label("Function_32_8225")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_826D")
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
    Jump("Function_32_8225")

    label("loc_826D")

    Return()

    # Function_32_8225 end

    def Function_33_826E(): pass

    label("Function_33_826E")

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

    # Function_33_826E end

    def Function_34_82D8(): pass

    label("Function_34_82D8")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_85D7")

    ChrTalk(
        0x102,
        "#00108F#12PLloyd...\x02",
    )

    CloseMessageWindow()
    Jump("loc_86C7")

    label("loc_85D7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_860B")

    ChrTalk(
        0x103,
        "#00208F#12P...Mr. Lloyd...\x02",
    )

    CloseMessageWindow()
    Jump("loc_86C7")

    label("loc_860B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8638")

    ChrTalk(
        0x104,
        "#00308F#12PLloyd...\x02",
    )

    CloseMessageWindow()
    Jump("loc_86C7")

    label("loc_8638")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8668")

    ChrTalk(
        0x105,
        "#10408F#12P...Lloyd...\x02",
    )

    CloseMessageWindow()
    Jump("loc_86C7")

    label("loc_8668")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8699")

    ChrTalk(
        0x109,
        "#10108F#12PMr. Lloyd...\x02",
    )

    CloseMessageWindow()
    Jump("loc_86C7")

    label("loc_8699")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_86C7")

    ChrTalk(
        0x106,
        "#10708F#12P...Mr. Lloyd. \x02",
    )

    CloseMessageWindow()

    label("loc_86C7")


    ChrTalk(
        0x101,
        (
            "#00004F#11P#30WHa ha...\x02\x03",
            "#00008F...Now, at last...\x01",
            "I think I've reached my big brother.\x02\x03",
            "#00002FThank you...\x01",
            "It was thanks to you all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00304F#12PHa ha...\x01",
            "The heck are you sayin'?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00204F#12P...I think that Mr. Lloyd's\x01",
            "will has broken through the\x01",
            ""barrier" called Mr. Arios.\x02\x03",
            "#00208FAnd also it dispelled the darkness\x01",
            "of the past of Mr. Guy's death...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104F#12PYes...we have only\x01",
            "helped you doing that.\x02\x03",
            "#00108FAlthough I can't say we'll just need\x01",
            "some help with what awaits us...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_88F6")

    ChrTalk(
        0x106,
        "#10703F#12P...You're right...\x02",
    )

    CloseMessageWindow()
    Jump("loc_895F")

    label("loc_88F6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_892E")

    ChrTalk(
        0x109,
        "#10106F#12P...You're right...\x02",
    )

    CloseMessageWindow()
    Jump("loc_895F")

    label("loc_892E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_895F")

    ChrTalk(
        0x105,
        "#10406F#12P...You're right.\x02",
    )

    CloseMessageWindow()

    label("loc_895F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_89B4")

    ChrTalk(
        0x104,
        (
            "#00308F#12PMilady Bell, Lawyer Ian\x01",
            "and Keddo too, huh...?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_8A60")

    label("loc_89B4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8A0E")

    ChrTalk(
        0x105,
        (
            "#10408F#12PMiss Mariabell, Mr. Beardy-Bear\x01",
            "and also KeA, eh...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8A60")

    label("loc_8A0E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8A60")

    ChrTalk(
        0x109,
        (
            "#10108F#12PMiss Mariabell, Mr. Grimwood\x01",
            "and also KeA, eh...?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8A60")


    ChrTalk(
        0x101,
        "#00006F#11P#30W...Yeah...\x02",
    )

    CloseMessageWindow()
    OP_68(350, 12800, 208640, 1000)
    MoveCamera(37, 17, 0, 1000)

    def lambda_8AA0():
        OP_93(0xFE, 0xB4, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8AA0)
    Sleep(300)

    def lambda_8AB0():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_8AB0)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#00003F#5PThe last "territory" has been released.\x02\x03",
            "#00000FAt any rate...\x01",
            "Let's go back to the "Sanctuary" terminus.\x02",
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

    # Function_34_82D8 end

    def Function_35_8BA1(): pass

    label("Function_35_8BA1")

    OP_9B(0x0, 0xFE, 0x162, 0x320, 0x3E8, 0x0)
    Return()

    # Function_35_8BA1 end

    def Function_36_8BB1(): pass

    label("Function_36_8BB1")

    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_36_8BB1 end

    def Function_37_8BC0(): pass

    label("Function_37_8BC0")

    Sleep(200)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_37_8BC0 end

    def Function_38_8BD2(): pass

    label("Function_38_8BD2")

    Sleep(300)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_38_8BD2 end

    def Function_39_8BE4(): pass

    label("Function_39_8BE4")

    Sleep(100)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_39_8BE4 end

    def Function_40_8BF0(): pass

    label("Function_40_8BF0")

    Sleep(400)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8C10")
    Sound(540, 0, 50, 0)
    Jump("loc_8C35")

    label("loc_8C10")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8C35")
    Sound(531, 0, 100, 0)

    label("loc_8C35")

    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_40_8BF0 end

    def Function_41_8C3E(): pass

    label("Function_41_8C3E")

    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8C5E")
    Sound(540, 0, 50, 0)
    Jump("loc_8C83")

    label("loc_8C5E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8C83")
    Sound(531, 0, 100, 0)

    label("loc_8C83")

    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_41_8C3E end

    def Function_42_8C8C(): pass

    label("Function_42_8C8C")

    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x10)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x800)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x2)
    SetChrFlags(0x8, 0x1000)
    SetChrFlags(0x8, 0x800)
    Return()

    # Function_42_8C8C end

    def Function_43_8CB3(): pass

    label("Function_43_8CB3")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 1)), scpexpr(EXPR_END)), "loc_8CD5")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8E3E")

    label("loc_8CD5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 2)), scpexpr(EXPR_END)), "loc_8CED")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8E3E")

    label("loc_8CED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 3)), scpexpr(EXPR_END)), "loc_8D05")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8E3E")

    label("loc_8D05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 4)), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8D28")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8E3E")

    label("loc_8D28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 5)), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8D4B")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8E3E")

    label("loc_8D4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 6)), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8D6E")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8E3E")

    label("loc_8D6E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_DC(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8D8C")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8E3E")

    label("loc_8D8C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_DC(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8DAA")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8E3E")

    label("loc_8DAA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_DC(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8DC8")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8E3E")

    label("loc_8DC8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_DC(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8DF1")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8E3E")

    label("loc_8DF1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_DC(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8E1A")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8E3E")

    label("loc_8E1A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_DC(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8E3E")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8E3E")

    Return()

    # Function_43_8CB3 end

    SaveToFile()

Try(main)
