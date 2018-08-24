from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "m9072.bin",                # FileName
        "m9072",                    # MapName
        "m9072",                    # Location
        0x00C2,                     # MapIndex
        "ed7354",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x2A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 1500, 0, 0, 1, 194, 0, 0, 0, 1],
    )

    BuildStringList((
        "m9072",                  # 0
        "Ogre Sigmund",           # 1
        "台詞表示用ダミーキャラ", # 2
        "Sigmund's Companion",    # 3
        "Sigmund's Companion",    # 4
        "SE制御",                 # 5
        "bm9059",                 # 6
    ))

    ATBonus("ATBonus_1D8", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_298", 8, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_29C", 3, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_2A0", 13, 9, 180)
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
        "BattleInfo_2B8", 0x0042, 255, 6, 45, 3, 3, 30, 0, "bm9059", 0x00000000, 100, 0, 0, 0,
        (
            ("ms03301.dat", "ms81200.dat", "ms81200.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_298", "MonsterBattlePostion_278", "ed7458", "ed7453", "ATBonus_1D8"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "apl/ch51742.itc",                   # 00
    ))

    DeclNpc(0,       4000,    63500,   180,  389,  0x0, 0,   0,   0,   255, 255, 0,   2,   255,  0)
    DeclNpc(0,       0,       0,       0,    508,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 10,  0.0,                   35.0,                  3.0,                   625.0,                 [0.10000000149011612,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.0,                  -7.0,                  -0.6000000238418579,   1.0])

    DeclActor(3750,    0,       10000,   1200,    3750,    1000,    10000,   0x007C, 0,  3,  0x0000)

    ChipFrameInfo(932, 0)                                        # 0

    ScpFunction((
        "Function_0_3A4",          # 00, 0
        "Function_1_3E2",          # 01, 1
        "Function_2_5BE",          # 02, 2
        "Function_3_86C",          # 03, 3
        "Function_4_960",          # 04, 4
        "Function_5_BE8",          # 05, 5
        "Function_6_D41",          # 06, 6
        "Function_7_DA2",          # 07, 7
        "Function_8_E03",          # 08, 8
        "Function_9_E64",          # 09, 9
        "Function_10_EC5",         # 0A, 10
        "Function_11_30CC",        # 0B, 11
        "Function_12_30F7",        # 0C, 12
        "Function_13_3122",        # 0D, 13
        "Function_14_314D",        # 0E, 14
        "Function_15_3178",        # 0F, 15
        "Function_16_31A3",        # 10, 16
        "Function_17_31CE",        # 11, 17
        "Function_18_31EB",        # 12, 18
        "Function_19_321A",        # 13, 19
        "Function_20_323D",        # 14, 20
        "Function_21_324F",        # 15, 21
        "Function_22_3261",        # 16, 22
        "Function_23_326D",        # 17, 23
        "Function_24_32BB",        # 18, 24
        "Function_25_3309",        # 19, 25
        "Function_26_3352",        # 1A, 26
        "Function_27_339B",        # 1B, 27
        "Function_28_33F2",        # 1C, 28
        "Function_29_340C",        # 1D, 29
        "Function_30_343B",        # 1E, 30
        "Function_31_3ABA",        # 1F, 31
        "Function_32_3AFD",        # 20, 32
        "Function_33_441A",        # 21, 33
        "Function_34_446F",        # 22, 34
        "Function_35_4495",        # 23, 35
        "Function_36_44A4",        # 24, 36
        "Function_37_44B3",        # 25, 37
        "Function_38_44BF",        # 26, 38
        "Function_39_44D1",        # 27, 39
        "Function_40_450B",        # 28, 40
        "Function_41_453F",        # 29, 41
    ))


    def Function_0_3A4(): pass

    label("Function_0_3A4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B5")
    Event(0, 4)

    label("loc_3B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_3CF")
    ClearScenarioFlags(0x22, 0)
    SetScenarioFlags(0x0, 0)
    SetScenarioFlags(0x0, 1)
    Event(0, 30)
    Jump("loc_3E1")

    label("loc_3CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_3E1")
    ClearScenarioFlags(0x22, 1)
    SetScenarioFlags(0x0, 2)
    Event(0, 32)

    label("loc_3E1")

    Return()

    # Function_0_3A4 end

    def Function_1_3E2(): pass

    label("Function_1_3E2")

    OP_F0(0x1, 0x320)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_3FB")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 0)

    label("loc_3FB")

    OP_52(0x8, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_1B(0x1, 0x0, 0x5)
    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A8, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_439")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_439")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 0)), scpexpr(EXPR_END)), "loc_4D9")
    SetMapObjFrame(0xFF, "magi10_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "magi11_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "point_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "magi_04_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "point16_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "yuka_15_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "fire00_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "fire02_add", 0x0, 0x1)
    Jump("loc_56B")

    label("loc_4D9")

    SetMapObjFrame(0xFF, "magi10_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "magi11_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "point_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "magi_04_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "point16_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "yuka_15_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "fire00_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "fire02_add", 0x1, 0x1)

    label("loc_56B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_57C")
    Call(0, 41)

    label("loc_57C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_597")
    OP_24(0x82)
    Sound(825, 1, 40, 0)
    Jump("loc_5BD")

    label("loc_597")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_5B1")
    OP_24(0x82)
    Sound(825, 1, 60, 0)
    ClearScenarioFlags(0x0, 1)
    Jump("loc_5BD")

    label("loc_5B1")

    Sound(130, 1, 60, 0)
    Sound(825, 1, 60, 0)

    label("loc_5BD")

    Return()

    # Function_1_3E2 end

    def Function_2_5BE(): pass

    label("Function_2_5BE")

    SetChrFlags(0x8, 0x10)
    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CE, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_82C")

    ChrTalk(
        0x8,
        "...............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301FLooks like he's out cold, but...\x02\x03",
            "#00306FHe doesn't seem to have suffered\x01",
            "any fatal wounds. ...Man, you're\x01",
            "just way too tough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104F...Should we take him\x01",
            "back to the Merkabah?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001FWell... He's the perpetrator of the\x01",
            "attack on Crossbell City and if we\x01",
            "could arrest him, I'd like to do so.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F...That would be\x01",
            "dangerous.\x02\x03",
            "#00200FSince his life is not in\x01",
            "danger, I think it's\x01",
            "best to leave him here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303FWell, I don't think he'll wake up\x01",
            "for a while, so there's no need\x01",
            "to worry about him pursuin' us.\x02\x03",
            "#00300FFor now, let's move on.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1CE, 7)
    Jump("loc_868")

    label("loc_82C")


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

    label("loc_868")

    TalkEnd(0x8)
    Return()

    # Function_2_5BE end

    def Function_3_86C(): pass

    label("Function_3_86C")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_951")
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

    label("loc_951")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_3_86C end

    def Function_4_960(): pass

    label("Function_4_960")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    LoadEffect(0x1, "event/ev202_00.eff")
    OP_69(0x1, 0x0)
    OP_68(-830, 5000, 70360, 0)
    MoveCamera(47, 43, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14220, 0)
    SetChrPos(0x0, 0, 4000, 72000, 180)
    SetChrPos(0x1, 0, 4000, 72000, 180)
    SetChrPos(0x2, 0, 4000, 72000, 180)
    SetChrPos(0x3, 0, 4000, 72000, 180)
    OP_A7(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    Sound(920, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x0, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_A74():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_A74)

    def lambda_A85():
        OP_95(0xFE, -230, 4000, 68330, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_A85)
    Sleep(500)
    PlayEffect(0x1, 0xFF, 0x1, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_ADC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_ADC)

    def lambda_AED():
        OP_95(0xFE, -1240, 4000, 68690, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_AED)
    Sleep(500)
    Sound(920, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x2, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_B4A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2, 2, lambda_B4A)

    def lambda_B5B():
        OP_95(0xFE, 1150, 4000, 68650, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_B5B)
    Sleep(500)
    PlayEffect(0x1, 0xFF, 0x3, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_BB2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x3, 2, lambda_BB2)

    def lambda_BC3():
        OP_95(0xFE, -2400, 4000, 69350, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_BC3)
    WaitChrThread(0x3, 1)
    Sleep(500)
    OP_E2(0x2)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_4_960 end

    def Function_5_BE8(): pass

    label("Function_5_BE8")

    EventBegin(0x0)
    OP_E2(0x3)
    LoadEffect(0x1, "event/evwarp.eff")
    Sound(936, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x0, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_C41():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_C41)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0x1, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_C8C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_C8C)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0x2, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_CD7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2, 2, lambda_CD7)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0x3, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_D22():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x3, 2, lambda_D22)
    StopSound(825, 1000, 40)
    Sleep(1000)
    NewScene("m9005", 105, 0, 0)
    IdleLoop()
    Return()

    # Function_5_BE8 end

    def Function_6_D41(): pass

    label("Function_6_D41")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D59")
    LoadChrToIndex("chr/ch03150.itc", 0x23)

    label("loc_D59")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D71")
    LoadChrToIndex("chr/ch03250.itc", 0x23)

    label("loc_D71")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D89")
    LoadChrToIndex("chr/ch02950.itc", 0x23)

    label("loc_D89")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DA1")
    LoadChrToIndex("chr/ch00950.itc", 0x23)

    label("loc_DA1")

    Return()

    # Function_6_D41 end

    def Function_7_DA2(): pass

    label("Function_7_DA2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DBA")
    LoadChrToIndex("chr/ch03150.itc", 0x24)

    label("loc_DBA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DD2")
    LoadChrToIndex("chr/ch03250.itc", 0x24)

    label("loc_DD2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DEA")
    LoadChrToIndex("chr/ch02950.itc", 0x24)

    label("loc_DEA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E02")
    LoadChrToIndex("chr/ch00950.itc", 0x24)

    label("loc_E02")

    Return()

    # Function_7_DA2 end

    def Function_8_E03(): pass

    label("Function_8_E03")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E1B")
    LoadChrToIndex("chr/ch03056.itc", 0x29)

    label("loc_E1B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E33")
    LoadChrToIndex("chr/ch03253.itc", 0x29)

    label("loc_E33")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E4B")
    LoadChrToIndex("chr/ch0295F.itc", 0x29)

    label("loc_E4B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E63")
    LoadChrToIndex("chr/ch00953.itc", 0x29)

    label("loc_E63")

    Return()

    # Function_8_E03 end

    def Function_9_E64(): pass

    label("Function_9_E64")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E7C")
    LoadChrToIndex("chr/ch03056.itc", 0x2A)

    label("loc_E7C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E94")
    LoadChrToIndex("chr/ch03253.itc", 0x2A)

    label("loc_E94")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_EAC")
    LoadChrToIndex("chr/ch0295F.itc", 0x2A)

    label("loc_EAC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_EC4")
    LoadChrToIndex("chr/ch00953.itc", 0x2A)

    label("loc_EC4")

    Return()

    # Function_9_E64 end

    def Function_10_EC5(): pass

    label("Function_10_EC5")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu04500.itp")
    CreatePortrait(1, 65514, 0, 490, 256, 0, 0, 512, 256, 0, 0, 512, 256, 0xFFFFFF, 0x0, "bu04501.itp")
    LoadChrToIndex("chr/ch03300.itc", 0x1E)
    LoadChrToIndex("chr/ch00050.itc", 0x1F)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00250.itc", 0x21)
    LoadChrToIndex("chr/ch00350.itc", 0x22)
    Call(0, 6)
    Call(0, 7)
    LoadChrToIndex("chr/ch03350.itc", 0x25)
    LoadChrToIndex("chr/ch03354.itc", 0x26)
    LoadChrToIndex("monster/ch81250.itc", 0x27)
    LoadChrToIndex("apl/ch51778.itc", 0x28)
    LoadEffect(0x0, "event/ev602_01.eff")
    LoadEffect(0x1, "event/ev17001.eff")
    LoadEffect(0x2, "event/ev305_00.eff")
    SoundLoad(825)
    SoundLoad(832)
    SoundLoad(2771)
    SoundLoad(2772)
    SoundLoad(2773)
    SoundLoad(3847)
    SoundLoad(3850)
    SoundLoad(3851)
    SoundLoad(3852)
    SoundLoad(3848)
    SoundLoad(3849)
    SetChrPos(0x101, 1100, 5000, 38100, 0)
    SetChrPos(0x102, -1100, 5000, 37750, 0)
    SetChrPos(0x103, 200, 5000, 37000, 0)
    SetChrPos(0x104, 0, 5000, 38800, 0)
    SetChrPos(0xF4, -650, 5000, 36250, 0)
    SetChrPos(0xF5, 850, 5000, 36000, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x8, 0x25)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x800)
    SetChrPos(0x8, 0, 4000, 62000, 180)
    OP_52(0x8, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x9, 0x80)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x9, 5000, 4000, 56500, 0)
    SetChrChipByIndex(0xA, 0x27)
    SetChrSubChip(0xA, 0x0)
    SetChrFlags(0xA, 0x20)
    OP_52(0xA, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0xA, -3500, 4400, 63500, 180)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    SetChrChipByIndex(0xB, 0x27)
    SetChrSubChip(0xB, 0x0)
    SetChrFlags(0xB, 0x20)
    OP_52(0xB, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0xB, 3500, 4400, 63500, 180)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    BeginChrThread(0xA, 2, 0, 27)
    BeginChrThread(0xB, 2, 0, 27)
    OP_68(0, 3000, 42800, 0)
    MoveCamera(55, 33, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(25000, 0)
    OP_68(0, 5000, 44800, 2500)
    MoveCamera(63, 29, 0, 2500)
    OP_6E(600, 2500)
    SetCameraDistance(15680, 2500)
    FadeToBright(1000, 0)

    def lambda_11C2():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_11C2)
    Sleep(50)

    def lambda_11DA():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_11DA)
    Sleep(50)

    def lambda_11F2():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_11F2)
    Sleep(50)

    def lambda_120A():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_120A)
    Sleep(50)

    def lambda_1222():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_1222)
    Sleep(50)

    def lambda_123A():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_123A)
    OP_0D()
    Sleep(1600)
    StopBGM(0x7D0)
    OP_C9(0x0, 0x80000000)

    NpcTalk(
        0x9,
        "Bold Voice",
        (
            "#3847V#11P#N#33A#30WHeh─ You got through the\x01",
            "preliminary matches,\x01",
            "huh?\x02",
        )
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
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7582", 0)
    OP_68(-140, 5300, 57850, 4000)
    MoveCamera(43, 12, 0, 4000)
    OP_6E(600, 4000)
    SetCameraDistance(16860, 4000)
    BeginChrThread(0x104, 0, 0, 11)
    Sleep(50)
    BeginChrThread(0x101, 0, 0, 12)
    Sleep(50)
    BeginChrThread(0x103, 0, 0, 13)
    Sleep(50)
    BeginChrThread(0x102, 0, 0, 14)
    Sleep(50)
    BeginChrThread(0xF4, 0, 0, 15)
    Sleep(50)
    BeginChrThread(0xF5, 0, 0, 16)
    OP_6F(0x79)
    BeginChrThread(0xC, 1, 0, 29)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)
    Sleep(300)

    ChrTalk(
        0x104,
        "#00311F#12PUncle...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00013F#12PSigmund Orlando...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_148C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1448")
    OP_FC(0xFFF4)
    Jump("loc_144B")

    label("loc_1448")

    OP_FC(0xC)

    label("loc_144B")


    ChrTalk(
        0x10A,
        (
            "#00601F#13PRed Constellation's vice\x01",
            "commander, huh...\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_152B")

    label("loc_148C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_14F5")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_14B6")
    OP_FC(0xFFF4)
    Jump("loc_14B9")

    label("loc_14B6")

    OP_FC(0xC)

    label("loc_14B9")


    ChrTalk(
        0x109,
        (
            "#10101F#13PRed Constellation's vice\x01",
            "commander...\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_152B")

    label("loc_14F5")


    ChrTalk(
        0x102,
        (
            "#00101F#12PRed Constellation's vice\x01",
            "commander...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_152B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1592")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1555")
    OP_FC(0xFFF4)
    Jump("loc_1558")

    label("loc_1555")

    OP_FC(0xC)

    label("loc_1558")


    ChrTalk(
        0x106,
        (
            "#10708F#13POgre Rosso... The\x01",
            "strongest jaeger.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_1638")

    label("loc_1592")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_15FD")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_15BC")
    OP_FC(0xFFF4)
    Jump("loc_15BF")

    label("loc_15BC")

    OP_FC(0xC)

    label("loc_15BF")


    ChrTalk(
        0x105,
        (
            "#10408F#13POgre Rosso... The\x01",
            "strongest jaeger, eh?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_1638")

    label("loc_15FD")


    ChrTalk(
        0x103,
        (
            "#00208F#12POgre Rosso... The\x01",
            "strongest jaeger, right?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1638")

    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x8,
        (
            "Heh... That's right.\x02\x03",
            "I was almost as strong as the War\x01",
            "God and the Jaeger King, but...\x02\x03",
            "After those two killed each other,\x01",
            "I can say I'm the strongest.\x02\x03",
            "─"Up until now", that is.\x02",
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
        0x104,
        "#00305F#12P...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04503F#5PRandolph... You should've noticed already.\x02\x03",
            "With this situation in Crossbell and the\x01",
            "unrest in the Erebonian Empire, Zemuria is\x01",
            "headed for turbulent times.\x02\x03",
            "#04501FThe places we jaegers can conduct our\x01",
            "activities will expand more than ever.\x02\x03",
            "Terrorists will be emboldened, the secret\x01",
            "feud between the Snake and Church will\x01",
            "intensify, the bracers will get desperate.\x02\x03",
            "#04504FYou should be able to tell that from\x01",
            "experience...\x02\x03",
            "#04502F─That they're bound to be truly over. The\x01",
            "peaceful times... are over.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00311F#12P............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00010F#12P...Say what you like...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#12PBut... It's not necessarily a mistake.\x02\x03",
            "#00106FWith the Crossbell incident... And the civil war\x01",
            "in the Empire and the unrest in the Republic,\x01",
            "Zemuria is greatly shaken right now...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00201F#12PCould it be that... Even if\x01",
            "nothing happened in Crossbell, it\x01",
            "would have been inevitable...?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1BBC")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1B23")
    OP_FC(0xFFF4)
    Jump("loc_1B26")

    label("loc_1B23")

    OP_FC(0xC)

    label("loc_1B26")


    ChrTalk(
        0x106,
        (
            "#10703F#13P...It's true that sparks\x01",
            "were smouldering\x01",
            "everywhere in Zemuria.\x02\x03",
            "#10701FIn the end, the\x01",
            "Crossbell incident was\x01",
            "just an excuse.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_1D58")

    label("loc_1BBC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1C8D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1BE6")
    OP_FC(0xFFF4)
    Jump("loc_1BE9")

    label("loc_1BE6")

    OP_FC(0xC)

    label("loc_1BE9")


    ChrTalk(
        0x10A,
        (
            "#00606F#13P...It is true that sparks\x01",
            "were smouldering\x01",
            "everywhere in Zemuria.\x02\x03",
            "#00601FIn the end, the Crossbell\x01",
            "incident was nothing more\x01",
            "than a pretext.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_1D58")

    label("loc_1C8D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1D58")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1CB7")
    OP_FC(0xFFF4)
    Jump("loc_1CBA")

    label("loc_1CB7")

    OP_FC(0xC)

    label("loc_1CBA")


    ChrTalk(
        0x105,
        (
            "#10406F#13P...It's true that sparks\x01",
            "were smouldering\x01",
            "everywhere in Zemuria.\x02\x03",
            "#10401FIn the end, the Crossbell\x01",
            "incident was nothing more\x01",
            "than an excuse.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_1D58")


    ChrTalk(
        0x104,
        (
            "#00306FYeah#12P... You're\x01",
            "right.\x02\x03",
            "#00311FBut it is true... I can\x01",
            "tell.\x02\x03",
            "Omens of a storm... The\x01",
            "smell of a battlefield\x01",
            "enveloping us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008F#12P...Randy...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04502F#5PHeh, that's proof that\x01",
            "you're a jaeger to the\x01",
            "core...\x02\x03",
            "And of the "fate" of the\x01",
            "warrior blood that runs\x01",
            "in the Orlando family.\x02\x03",
            "#04503FAnd yet, Randolph... Why\x01",
            "don't you open your eyes?\x02\x03",
            "#04501FHow can you live a\x01",
            "tranquil life while lying\x01",
            "to yourself like this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00311F#12P#30W...............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04501F#5P─This is the last time,\x01",
            "Randolph. Succeed the War\x01",
            "God.\x02\x03",
            "I'll teach you what you\x01",
            "lack in brother's place.\x02\x03",
            "#04504FThen you'll become the\x01",
            "boss of Red Constellation\x01",
            "in name and reality...\x02\x03",
            "#04502FWe'll support you however\x01",
            "you desire.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_82(0x32, 0x0, 0x7D0, 0xC8)

    ChrTalk(
        0x104,
        "#00305F#12P...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04504F#5PHehe. Even supporting Crossbell\x01",
            "would be all right with us, you\x01",
            "know.\x02\x03",
            "#04502FNo matter how this incident turns\x01",
            "out, there's no doubt that great\x01",
            "difficulties are in store for you.\x02\x03",
            "You could even do it for your\x01",
            ""friends"...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00010F#12P...Guh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00107F#12PYou...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00211F#12P...You're talking down\x01",
            "to us too much...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(150)
    BeginChrThread(0x104, 3, 0, 17)
    WaitChrThread(0x104, 3)
    Sleep(200)

    def lambda_21C9():
        OP_A6(0xFE, 0x0, 0x14, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_21C9)
    WaitChrThread(0x104, 2)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#00304F#12P#30WHehe, I see...\x02\x03",
            "#00312FYou're cooling your\x01",
            "fierce impulses with\x01",
            "calm rationality...\x02\x03",
            "You're the Ogre Rosso\x01",
            "indeed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04504F#5PThat's why a jaeger is a\x01",
            "jaeger... You should\x01",
            "understand that too.\x02\x03",
            "#04502FAfter the peaceful times have\x01",
            "passed, you won't have a\x01",
            ""foothold" to resist anywhere.\x02\x03",
            "That being the case, how could\x01",
            "there be room for hesitation?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F#12PYou might be right about\x01",
            "that...\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x104, 3, 0, 18)
    WaitChrThread(0x104, 3)
    Sleep(350)

    ChrTalk(
        0x104,
        "#00301F#12P─But my answer is NO.\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x8,
        "#04505F#5P...Ohh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00315F#12PLooks like your failure of a nephew\x01",
            "strayed from the path, huh?\x02\x03",
            "#00304FSeekin' peace in turbulent times,\x01",
            "seekin' justice in a world of\x01",
            "deceit...\x02\x03",
            "Even more, neither as a fantasy nor an\x01",
            "illusion, but by steadily doin' what\x01",
            "we can, one thing after the next...\x02\x03",
            "#00302F─That's the kind of "foothold" I've\x01",
            "found.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00214F#12PRandy...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2618")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_25FB")
    OP_FC(0xFFF4)
    Jump("loc_25FE")

    label("loc_25FB")

    OP_FC(0xC)

    label("loc_25FE")


    ChrTalk(
        0x109,
        "#10100F#13PRandy...\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_2618")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_266F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2642")
    OP_FC(0xFFF4)
    Jump("loc_2645")

    label("loc_2642")

    OP_FC(0xC)

    label("loc_2645")


    ChrTalk(
        0x10A,
        "#00604F#13PHmph, how impertinent...\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_266F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_26E1")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2699")
    OP_FC(0xFFF4)
    Jump("loc_269C")

    label("loc_2699")

    OP_FC(0xC)

    label("loc_269C")


    ChrTalk(
        0x105,
        (
            "#10402F#13PHehe, I wonder if he\x01",
            "takes after a certain\x01",
            "someone?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_26E1")


    ChrTalk(
        0x8,
        "#04501F#5P............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F#12PI'll go up against my own "fate" by\x01",
            "means of this "foothold".\x02\x03",
            "#00308FI said my complete farewells to\x01",
            "those battlefield days where I could\x01",
            "only live in a veritable hell.\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x104, 3, 0, 19)
    WaitChrThread(0x104, 3)
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x104,
        (
            "#00301F#12P#30WThis is my way of\x01",
            "settling things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002F#12PRandy...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104F#12P...We'll watch over you\x01",
            "too.\x02",
        )
    )

    CloseMessageWindow()
    StopSound(130, 3000, 30)
    StopSound(825, 3000, 60)
    Sleep(300)

    def lambda_2866():
        OP_A6(0xFE, 0x1E, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_2866)
    WaitChrThread(0x8, 2)
    Sleep(800)

    def lambda_2886():
        OP_A6(0xFE, 0x28, 0x28, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_2886)
    WaitChrThread(0x8, 2)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#04502F#5P#30W...Hehe...\x02\x03",
            "#04504F......Hahahaha......\x02\x03",
            "#04501F─Done with the saucy\x01",
            "speech?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    BeginChrThread(0x8, 0, 0, 28)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xF)
    CancelBlur(1000)
    PlayEffect(0x1, 0x1, 0x8, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_82(0x0, 0x258, 0x1770, 0x1F4)
    ClearChrFlags(0x104, 0x2)
    ClearChrFlags(0x104, 0x1000)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    Sound(256, 0, 80, 0)
    Sound(881, 0, 70, 0)
    OP_24(0x339)
    Sleep(1)
    Sound(825, 2, 80, 0)
    Sound(832, 2, 100, 0)
    Sleep(800)
    SetCameraDistance(17860, 20000)

    ChrTalk(
        0x101,
        "#00010F#12PGuh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00210F#12P#N...Uwaah...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2A31")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2A02")
    OP_FC(0xFFF4)
    Jump("loc_2A05")

    label("loc_2A02")

    OP_FC(0xC)

    label("loc_2A05")


    ChrTalk(
        0x106,
        "#10707F#13PWhat fighting spirit!\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_2AE5")

    label("loc_2A31")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2A8A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2A5B")
    OP_FC(0xFFF4)
    Jump("loc_2A5E")

    label("loc_2A5B")

    OP_FC(0xC)

    label("loc_2A5E")


    ChrTalk(
        0x105,
        "#10410F#13PWhat fighting spirit!\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_2AE5")

    label("loc_2A8A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2AE5")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2AB4")
    OP_FC(0xFFF4)
    Jump("loc_2AB7")

    label("loc_2AB4")

    OP_FC(0xC)

    label("loc_2AB7")


    ChrTalk(
        0x10A,
        (
            "#00610F#13PWhat fighting spirit he\x01",
            "has!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_2AE5")


    ChrTalk(
        0x8,
        (
            "#04504F#5PHehe... Very well.\x02\x03",
            "I'll acknowledge your\x01",
            ""stand" by means of that\x01",
            "unreliable "foothold"...\x02\x03",
            "#04501FHowever... You get it,\x01",
            "right?\x02\x03",
            "Since you've said that\x01",
            "much, I won't go easy on\x01",
            "you anymore, you know?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopBGM(0xBB8)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x104,
        (
            "#00303F#2771V#12P#30W#20AYeah─ That's exactly\x01",
            "what I want.\x02",
        )
    )

    CloseMessageWindow()
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0x104, 0x22)
    SetChrSubChip(0x104, 0x0)
    ClearChrFlags(0x104, 0x2)
    ClearChrFlags(0x104, 0x1000)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xF)
    CancelBlur(1000)
    PlayEffect(0x2, 0x0, 0x104, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_82(0x1F4, 0x0, 0xBB8, 0x1F4)
    Sound(256, 0, 80, 0)
    Sound(881, 0, 70, 0)
    WaitChrThread(0x104, 0)
    Sleep(500)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7458", 0)
    MoveCamera(48, 14, 0, 20000)
    Sleep(800)

    ChrTalk(
        0x104,
        (
            "#00301F#2772V#12P#30W#46AI'll use the crafts I learned\x01",
            "from the ol' man and you and\x01",
            "all the power I have...\x02\x03",
            "#00307F#2773V#35ATo beat you, the strongest\x01",
            "jaeger!!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#04504F#3850V#5P#30W#35AHeh... Interesting.\x02\x03",
            "#04512F#3851V#30W#50AThen, I'll devour you\x01",
            "and succeed the War God!\x02\x03",
            "#3852V#30W#50AYou'll be a minimal\x01",
            "offering for big bro's\x01",
            "failure of a son!!\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    Fade(500)
    OP_68(-140, 5300, 57850, 0)
    MoveCamera(359, 10, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17860, 0)
    SetCameraDistance(14860, 20000)
    OP_52(0x8, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    EndChrThread(0x8, 0x0)
    SetChrChipByIndex(0x8, 0x26)
    SetChrSubChip(0x8, 0x0)
    Sound(802, 0, 100, 0)
    Sound(531, 0, 50, 0)
    Sound(358, 0, 80, 0)
    Sleep(300)
    Sound(817, 0, 100, 0)
    BeginChrThread(0xA, 3, 0, 25)
    BeginChrThread(0xB, 3, 0, 26)
    WaitChrThread(0xA, 3)
    WaitChrThread(0xB, 3)
    Sleep(100)
    BeginChrThread(0x101, 0, 0, 20)
    BeginChrThread(0x102, 0, 0, 21)
    BeginChrThread(0x103, 0, 0, 22)
    BeginChrThread(0xF4, 0, 0, 23)
    BeginChrThread(0xF5, 0, 0, 24)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)
    OP_A0(0x8, 1800, 0x0, 0x4)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    OP_C9(0x0, 0x80000000)

    AnonymousTalk(
        0x8,
        (
            "#3848V#5P#40W#30ANow, here they come...\x02\x03",
            "#3849V#30W#52AThe twin battle-axes of Ogre Rosso,\x01",
            "who devours and tramples across the\x01",
            "battlefield!!\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    Sleep(300)

    ChrTalk(
        0x102,
        "#00107F#6P#N#10A...He's coming!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00007F#12P#15ALet's face him! Support\x01",
            "Randy with all you've\x01",
            "got!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    SetScenarioFlags(0x0, 1)
    Battle("BattleInfo_2B8", 0x0, 0x0, 0x100, 0x47, 0xFF)
    FadeToDark(0, 0, -1)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    EndChrThread(0x8, 0x0)
    OP_CC(0x1, 0xFF, 0x0)
    OP_52(0x8, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 30)
    Return()

    # Function_10_EC5 end

    def Function_11_30CC(): pass

    label("Function_11_30CC")

    OP_9B(0x0, 0xFE, 0x0, 0x1770, 0xFA0, 0x1)
    OP_96(0xFE, 0x0, 0xFA0, 0xD69C, 0xFA0, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_11_30CC end

    def Function_12_30F7(): pass

    label("Function_12_30F7")

    OP_9B(0x0, 0xFE, 0x0, 0x157C, 0xFA0, 0x1)
    OP_96(0xFE, 0x460, 0xFA0, 0xD1C4, 0xFA0, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_12_30F7 end

    def Function_13_3122(): pass

    label("Function_13_3122")

    OP_9B(0x0, 0xFE, 0x0, 0x157C, 0xFA0, 0x1)
    OP_96(0xFE, 0x1A4, 0xFA0, 0xCC92, 0xFA0, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_13_3122 end

    def Function_14_314D(): pass

    label("Function_14_314D")

    OP_9B(0x0, 0xFE, 0x0, 0x157C, 0xFA0, 0x1)
    OP_96(0xFE, 0xFFFFFB0A, 0xFA0, 0xCF4E, 0xFA0, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_14_314D end

    def Function_15_3178(): pass

    label("Function_15_3178")

    OP_9B(0x0, 0xFE, 0x0, 0x1996, 0xFA0, 0x1)
    OP_96(0xFE, 0xFFFFF614, 0xFA0, 0xD1BA, 0xFA0, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_15_3178 end

    def Function_16_31A3(): pass

    label("Function_16_31A3")

    OP_9B(0x0, 0xFE, 0x0, 0x1AC2, 0xFA0, 0x1)
    OP_96(0xFE, 0x9EC, 0xFA0, 0xD0F2, 0xFA0, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_16_31A3 end

    def Function_17_31CE(): pass

    label("Function_17_31CE")

    SetChrChipByIndex(0x104, 0x28)
    SetChrFlags(0x104, 0x2)
    SetChrFlags(0x104, 0x1000)
    SetChrSubChip(0xFE, 0x1)
    Sleep(143)
    SetChrSubChip(0xFE, 0x2)
    Sleep(429)
    Return()

    # Function_17_31CE end

    def Function_18_31EB(): pass

    label("Function_18_31EB")

    SetChrChipByIndex(0x104, 0x28)
    SetChrFlags(0x104, 0x2)
    SetChrFlags(0x104, 0x1000)
    SetChrSubChip(0xFE, 0x2)
    Sleep(110)
    SetChrSubChip(0xFE, 0x1)
    Sleep(130)
    SetChrChipByIndex(0x104, 0xFF)
    ClearChrFlags(0x104, 0x2)
    ClearChrFlags(0x104, 0x1000)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_18_31EB end

    def Function_19_321A(): pass

    label("Function_19_321A")

    SetChrChipByIndex(0x104, 0x28)
    SetChrFlags(0x104, 0x2)
    SetChrFlags(0x104, 0x1000)
    Sound(802, 0, 100, 0)
    SetChrSubChip(0xFE, 0x4)
    Sleep(143)
    SetChrSubChip(0xFE, 0x5)
    Sleep(429)
    Return()

    # Function_19_321A end

    def Function_20_323D(): pass

    label("Function_20_323D")

    Sleep(150)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_20_323D end

    def Function_21_324F(): pass

    label("Function_21_324F")

    Sleep(300)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_21_324F end

    def Function_22_3261(): pass

    label("Function_22_3261")

    Sleep(450)
    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_22_3261 end

    def Function_23_326D(): pass

    label("Function_23_326D")

    Sleep(600)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_328D")
    Sound(540, 0, 50, 0)
    Jump("loc_32B2")

    label("loc_328D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_32B2")
    Sound(531, 0, 100, 0)

    label("loc_32B2")

    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_23_326D end

    def Function_24_32BB(): pass

    label("Function_24_32BB")

    Sleep(750)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_32DB")
    Sound(540, 0, 50, 0)
    Jump("loc_3300")

    label("loc_32DB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3300")
    Sound(531, 0, 100, 0)

    label("loc_3300")

    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_24_32BB end

    def Function_25_3309(): pass

    label("Function_25_3309")

    PlayEffect(0x0, 0x5, 0xFE, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    StopEffect(0x5, 0x2)
    Return()

    # Function_25_3309 end

    def Function_26_3352(): pass

    label("Function_26_3352")

    PlayEffect(0x0, 0x6, 0xFE, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    StopEffect(0x6, 0x2)
    Return()

    # Function_26_3352 end

    def Function_27_339B(): pass

    label("Function_27_339B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_33F1")
    SetChrSubChip(0xFE, 0x0)
    Sleep(100)
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
    SetChrSubChip(0xFE, 0x4)
    Sleep(100)
    SetChrSubChip(0xFE, 0x3)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    Jump("Function_27_339B")

    label("loc_33F1")

    Return()

    # Function_27_339B end

    def Function_28_33F2(): pass

    label("Function_28_33F2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_340B")
    OP_A1(0xFE, 0x5DC, 0x3, 0x0, 0x1, 0x2)
    Jump("Function_28_33F2")

    label("loc_340B")

    Return()

    # Function_28_33F2 end

    def Function_29_340C(): pass

    label("Function_29_340C")

    OP_25(0x82, 0x3C)
    Sleep(200)
    OP_25(0x82, 0x37)
    Sleep(200)
    OP_25(0x82, 0x32)
    Sleep(200)
    OP_25(0x82, 0x2D)
    Sleep(200)
    OP_25(0x82, 0x28)
    Sleep(200)
    OP_25(0x82, 0x23)
    Sleep(200)
    OP_25(0x82, 0x1E)
    Return()

    # Function_29_340C end

    def Function_30_343B(): pass

    label("Function_30_343B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch51742.itc", 0x1E)
    LoadChrToIndex("chr/ch00050.itc", 0x1F)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00250.itc", 0x21)
    LoadChrToIndex("chr/ch00350.itc", 0x22)
    Call(0, 6)
    Call(0, 7)
    LoadEffect(0x0, "event/ev17083.eff")
    SetChrPos(0x101, 1120, 4000, 58200, 0)
    SetChrPos(0x102, -1270, 4000, 57570, 0)
    SetChrPos(0x103, 420, 4000, 56870, 0)
    SetChrPos(0x104, 0, 4000, 59440, 0)
    SetChrPos(0xF4, -2540, 4000, 58190, 0)
    SetChrPos(0xF5, 2540, 4000, 57990, 0)
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
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x1000)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x2)
    SetChrFlags(0x8, 0x800)
    SetChrPos(0x8, 0, 4000, 63500, 180)
    OP_68(0, 4800, 62000, 0)
    MoveCamera(180, 29, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16300, 0)
    SetCameraDistance(14300, 2500)
    PlayBGM("ed7543", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x21F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1500)
    OP_6F(0x79)

    ChrTalk(
        0x8,
        (
            "#04510F#6P#40W...Hehe...\x02\x03",
            "#04511FWho would've thought with\x01",
            "such a "foothold"... you'd\x01",
            "be able to do this much...\x02\x03",
            "However... That's another\x01",
            "of your strengths now...\x02",
        )
    )

    OP_6F(0x79)
    CloseMessageWindow()
    Fade(500)
    SetChrSubChip(0x8, 0x1)
    OP_68(-150, 5400, 60750, 0)
    MoveCamera(39, 13, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14680, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#00306F#12P#30W...Yeah... Sorry but,\x01",
            "I'll have you respect my\x01",
            "will...\x02\x03",
            "#00301FAlthough it might be\x01",
            "disrespectful to you and\x01",
            "my ol' man...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04510F#5P#40WHehe... What's that, at this\x01",
            "late hour?\x02\x03",
            "#04511F...Also, the greatest\x01",
            "disrespect was when you walked\x01",
            "away without settling things...\x02\x03",
            "He never said a single word,\x01",
            "but... ...Big bro was worried\x01",
            "about you too, you know...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00308F#12P#30W...I see... My ol' man\x01",
            "was...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)

    def lambda_3852():
        OP_A6(0xFE, 0x0, 0x23, 0x12C, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_3852)
    Sleep(800)

    ChrTalk(
        0x8,
        (
            "#04510F#5P#50WHehe... However... It seems\x01",
            "you've grown a face I wouldn't\x01",
            "be ashamed to show him...\x02\x03",
            "#60W...Show me how far that\x01",
            "courage... can go...\x02\x03",
            "Prove it to me... with your...\x01",
            "future way of life...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)

    def lambda_3941():
        OP_A6(0xFE, 0x0, 0x23, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_3941)
    WaitChrThread(0x8, 2)
    Fade(500)
    BeginChrThread(0x8, 0, 0, 31)
    Sleep(300)
    OP_68(-40, 5400, 62080, 1000)
    WaitChrThread(0x8, 0)
    Sleep(200)
    Sound(202, 0, 100, 0)
    Sound(181, 0, 80, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 0, 4050, 60140, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    SetMapObjFrame(0xFF, "magi_04_add", 0x0, 0x1)
    Sleep(2300)
    Sleep(500)
    MoveCamera(38, 20, 0, 4500)
    SetCameraDistance(20600, 4500)
    Sleep(3000)
    StopSound(825, 1000, 60)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(0, -900, 58000, 0)
    MoveCamera(24, 17, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(46500, 0)
    SetCameraDistance(50000, 1500)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    Sound(202, 0, 70, 0)
    SetMapObjFrame(0xFF, "magi_04_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "yuka_15_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "fire00_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "fire02_add", 0x0, 0x1)
    Fade(500)
    Sleep(2500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 0)
    NewScene("m9005", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_30_343B end

    def Function_31_3ABA(): pass

    label("Function_31_3ABA")

    SetChrSubChip(0xFE, 0x2)
    Sleep(143)
    SetChrSubChip(0xFE, 0x3)
    Sleep(143)
    SetChrSubChip(0xFE, 0x4)
    Sleep(143)
    SetChrSubChip(0xFE, 0x5)
    Sleep(429)
    SetChrSubChip(0xFE, 0x6)
    Sound(811, 0, 100, 0)
    Sound(898, 0, 100, 0)
    Sleep(143)
    SetChrSubChip(0xFE, 0x7)
    Sound(862, 0, 50, 0)
    Sound(833, 0, 50, 0)
    Sleep(429)
    Return()

    # Function_31_3ABA end

    def Function_32_3AFD(): pass

    label("Function_32_3AFD")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch51742.itc", 0x1E)
    LoadChrToIndex("chr/ch00050.itc", 0x1F)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00250.itc", 0x21)
    LoadChrToIndex("chr/ch00350.itc", 0x22)
    Call(0, 6)
    Call(0, 7)
    LoadChrToIndex("chr/ch00056.itc", 0x25)
    LoadChrToIndex("chr/ch00156.itc", 0x26)
    LoadChrToIndex("chr/ch00256.itc", 0x27)
    LoadChrToIndex("chr/ch00356.itc", 0x28)
    Call(0, 8)
    Call(0, 9)
    LoadEffect(0x0, "event/ev17012.eff")
    SetChrPos(0x101, 1120, 4000, 58200, 0)
    SetChrPos(0x102, -1270, 4000, 57570, 0)
    SetChrPos(0x103, 420, 4000, 56870, 0)
    SetChrPos(0x104, 0, 4000, 59440, 0)
    SetChrPos(0xF4, -2540, 4000, 58190, 0)
    SetChrPos(0xF5, 2540, 4000, 57990, 0)
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
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x7)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x1000)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x2)
    SetChrFlags(0x8, 0x800)
    SetChrPos(0x8, 0, 4000, 63500, 180)
    SetMapObjFrame(0xFF, "magi_04_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "yuka_15_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "fire00_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "fire02_add", 0x0, 0x1)
    OP_68(0, 4500, 72000, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(31500, 0)
    SetCameraDistance(29500, 2600)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(300)
    PlayEffect(0x0, 0x0, 0xFF, 0x0, 0, 4000, 72000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(935, 0, 80, 0)
    SetMapObjFrame(0xFF, "magi10_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "magi11_add", 0x1, 0x1)
    Sleep(200)
    SetMapObjFrame(0xFF, "point_add", 0x1, 0x1)
    Sleep(600)
    StopEffect(0x0, 0x2)
    OP_6F(0x79)
    Fade(500)
    OP_68(-280, 5100, 60700, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15710, 0)
    Fade(500)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x101,
        "#00005F#11P#30WAh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00102F#12P#30W...Did we... win...?\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    BeginChrThread(0x101, 0, 0, 36)
    BeginChrThread(0x102, 0, 0, 37)
    BeginChrThread(0x103, 0, 0, 38)
    BeginChrThread(0xF4, 0, 0, 39)
    BeginChrThread(0xF5, 0, 0, 40)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)
    Sleep(300)

    ChrTalk(
        0x103,
        "#00206F#12P#40W...*pant, pant*...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3E9D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3E57")
    OP_FC(0xFFF4)
    Jump("loc_3E5A")

    label("loc_3E57")

    OP_FC(0xB)

    label("loc_3E5A")


    ChrTalk(
        0x109,
        (
            "#10106F#13P#40WIt's unbelievable...\x01",
            "...We really won...\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_3F53")

    label("loc_3E9D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3EFC")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3EC7")
    OP_FC(0xFFF4)
    Jump("loc_3ECA")

    label("loc_3EC7")

    OP_FC(0xB)

    label("loc_3ECA")


    ChrTalk(
        0x10A,
        "#00606F#13P#40WIncredible... We won...\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_3F53")

    label("loc_3EFC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3F53")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3F26")
    OP_FC(0xFFF4)
    Jump("loc_3F29")

    label("loc_3F26")

    OP_FC(0xB)

    label("loc_3F29")


    ChrTalk(
        0x106,
        "#10706F#13P#40W...It's a miracle...\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_3F53")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3FD2")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3F7D")
    OP_FC(0xFFF4)
    Jump("loc_3F80")

    label("loc_3F7D")

    OP_FC(0xB)

    label("loc_3F80")


    ChrTalk(
        0x105,
        (
            "#10402F#13P#40WJust this time...\x01",
            "...I'll be grateful to\x01",
            "the Goddess...\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_4085")

    label("loc_3FD2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_402E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3FFC")
    OP_FC(0xFFF4)
    Jump("loc_3FFF")

    label("loc_3FFC")

    OP_FC(0xB)

    label("loc_3FFF")


    ChrTalk(
        0x106,
        "#10702F#13P#40W...It's a miracle...\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_4085")

    label("loc_402E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4085")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4058")
    OP_FC(0xFFF4)
    Jump("loc_405B")

    label("loc_4058")

    OP_FC(0xB)

    label("loc_405B")


    ChrTalk(
        0x10A,
        "#00602F#13P#40W...It's a miracle...\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_4085")


    ChrTalk(
        0x104,
        "#00306F#11P#30W...Yeah...\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    BeginChrThread(0x104, 0, 0, 35)
    WaitChrThread(0x104, 0)
    Sleep(500)
    OP_68(-350, 5100, 61510, 1200)
    MoveCamera(38, 15, 0, 1200)
    OP_6E(600, 1200)
    SetCameraDistance(15710, 1200)
    OP_99(0x104, 0x8, 0x9C4, 0x4B0, 0x0)
    Sleep(300)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x104)

    ChrTalk(
        0x104,
        "#00308F#11P#30W............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#12P#30W...No matter what anyone\x01",
            "says... he's your\x01",
            ""family", right...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00202F#12P#30WIt seems he was\x01",
            "worried... ...about you,\x01",
            "Randy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#11P#30WYeah... I know.\x02\x03",
            "#00303FBein' rough seems to be\x01",
            "my family's style...\x02\x03",
            "#00300F...However... With this,\x01",
            "I've settled things,\x01",
            "somehow.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_68(-300, 5100, 60840, 1100)
    OP_93(0x104, 0xB4, 0x190)
    OP_6F(0x79)

    ChrTalk(
        0x104,
        (
            "#00304F#5PIt appears the Territory\x01",
            "was released too.\x02\x03",
            "#00302FFor the time bein'...\x01",
            "Let's head back to the\x01",
            "gate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00104F#12PRight...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002F#12P...Nice job, Randy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00204F#12PThat was good job...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00309F#5PHaha, right back at'cha.\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(17000, 2000)
    FadeToDark(1500, 0, -1)
    OP_0D()
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0xF4, 0xFF)
    SetChrSubChip(0xF4, 0x0)
    SetChrChipByIndex(0xF5, 0xFF)
    SetChrSubChip(0xF5, 0x0)
    SetChrPos(0x0, 0, 4000, 57300, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    OP_37()
    SetScenarioFlags(0x1A9, 0)
    OP_29(0xB2, 0x1, 0x6)
    ModifyEventFlags(0, 0, 0x80)
    StopBGM(0xFA0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7354", 0)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x162), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_E2(0x2)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_32_3AFD end

    def Function_33_441A(): pass

    label("Function_33_441A")


    def lambda_441F():
        OP_A6(0xFE, 0x0, 0x19, 0x12C, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_441F)
    Sleep(700)
    OP_9B(0x0, 0xFE, 0x162, 0x320, 0x3E8, 0x0)
    OP_95(0xFE, -1200, 4100, 63800, 1000, 0x0)
    TurnDirection(0xFE, 0x8, 500)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_33_441A end

    def Function_34_446F(): pass

    label("Function_34_446F")

    OP_93(0xFE, 0xB4, 0x1F4)
    OP_95(0xFE, 650, 4100, 59850, 1500, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(700)
    Return()

    # Function_34_446F end

    def Function_35_4495(): pass

    label("Function_35_4495")

    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_35_4495 end

    def Function_36_44A4(): pass

    label("Function_36_44A4")

    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_36_44A4 end

    def Function_37_44B3(): pass

    label("Function_37_44B3")

    Sleep(100)
    SetChrChipByIndex(0xFE, 0x26)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_37_44B3 end

    def Function_38_44BF(): pass

    label("Function_38_44BF")

    Sleep(200)
    Sound(811, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_38_44BF end

    def Function_39_44D1(): pass

    label("Function_39_44D1")

    Sleep(300)
    Sound(514, 0, 50, 0)
    SetChrChipByIndex(0xFE, 0x29)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4506")
    SetChrSubChip(0xFE, 0x2)
    Jump("loc_450A")

    label("loc_4506")

    SetChrSubChip(0xFE, 0x0)

    label("loc_450A")

    Return()

    # Function_39_44D1 end

    def Function_40_450B(): pass

    label("Function_40_450B")

    Sleep(400)
    SetChrChipByIndex(0xFE, 0x2A)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_453A")
    SetChrSubChip(0xFE, 0x2)
    Jump("loc_453E")

    label("loc_453A")

    SetChrSubChip(0xFE, 0x0)

    label("loc_453E")

    Return()

    # Function_40_450B end

    def Function_41_453F(): pass

    label("Function_41_453F")

    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x7)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x1000)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x2)
    SetChrFlags(0x8, 0x800)
    Return()

    # Function_41_453F end

    SaveToFile()

Try(main)
