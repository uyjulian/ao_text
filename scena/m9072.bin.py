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
        "Function_3_87E",          # 03, 3
        "Function_4_974",          # 04, 4
        "Function_5_BFC",          # 05, 5
        "Function_6_D55",          # 06, 6
        "Function_7_DB6",          # 07, 7
        "Function_8_E17",          # 08, 8
        "Function_9_E78",          # 09, 9
        "Function_10_ED9",         # 0A, 10
        "Function_11_311F",        # 0B, 11
        "Function_12_314A",        # 0C, 12
        "Function_13_3175",        # 0D, 13
        "Function_14_31A0",        # 0E, 14
        "Function_15_31CB",        # 0F, 15
        "Function_16_31F6",        # 10, 16
        "Function_17_3221",        # 11, 17
        "Function_18_323E",        # 12, 18
        "Function_19_326D",        # 13, 19
        "Function_20_3290",        # 14, 20
        "Function_21_32A2",        # 15, 21
        "Function_22_32B4",        # 16, 22
        "Function_23_32C0",        # 17, 23
        "Function_24_330E",        # 18, 24
        "Function_25_335C",        # 19, 25
        "Function_26_33A5",        # 1A, 26
        "Function_27_33EE",        # 1B, 27
        "Function_28_3445",        # 1C, 28
        "Function_29_345F",        # 1D, 29
        "Function_30_348E",        # 1E, 30
        "Function_31_3B4A",        # 1F, 31
        "Function_32_3B8D",        # 20, 32
        "Function_33_44AD",        # 21, 33
        "Function_34_4502",        # 22, 34
        "Function_35_4528",        # 23, 35
        "Function_36_4537",        # 24, 36
        "Function_37_4546",        # 25, 37
        "Function_38_4552",        # 26, 38
        "Function_39_4564",        # 27, 39
        "Function_40_459E",        # 28, 40
        "Function_41_45D2",        # 29, 41
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CE, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_82B")

    ChrTalk(
        0x8,
        "............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301FSeems he's totally out cold, but...\x02\x03",
            "#00306FIt doesn't seem he suffered any fatal wounds.\x01",
            "...Oh man, you're too tough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104F...Would it be better to carry \x01",
            "him to the Merkabah?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001FWell...\x01",
            "He's the perpetrator of the Crossbell City raid\x01",
            "and if he could be arrested, I'd like he'd be.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F...It would be dangerous.\x02\x03",
            "#00200FSince his life is not in peril, I think\x01",
            "it would be wiser to leave him here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303FWell, I guess he won't wake up for awhile, so we \x01",
            "shouldn't even be worried 'bout him to pursue us.\x02\x03",
            "#00300FLet's move on for now.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1CE, 7)
    Jump("loc_87A")

    label("loc_82B")


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

    label("loc_87A")

    TalkEnd(0x8)
    Return()

    # Function_2_5BE end

    def Function_3_87E(): pass

    label("Function_3_87E")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_965")
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

    label("loc_965")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_3_87E end

    def Function_4_974(): pass

    label("Function_4_974")

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

    def lambda_A88():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_A88)

    def lambda_A99():
        OP_95(0xFE, -230, 4000, 68330, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_A99)
    Sleep(500)
    PlayEffect(0x1, 0xFF, 0x1, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_AF0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_AF0)

    def lambda_B01():
        OP_95(0xFE, -1240, 4000, 68690, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_B01)
    Sleep(500)
    Sound(920, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x2, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_B5E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2, 2, lambda_B5E)

    def lambda_B6F():
        OP_95(0xFE, 1150, 4000, 68650, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_B6F)
    Sleep(500)
    PlayEffect(0x1, 0xFF, 0x3, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_BC6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x3, 2, lambda_BC6)

    def lambda_BD7():
        OP_95(0xFE, -2400, 4000, 69350, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_BD7)
    WaitChrThread(0x3, 1)
    Sleep(500)
    OP_E2(0x2)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_4_974 end

    def Function_5_BFC(): pass

    label("Function_5_BFC")

    EventBegin(0x0)
    OP_E2(0x3)
    LoadEffect(0x1, "event/evwarp.eff")
    Sound(936, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x0, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_C55():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_C55)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0x1, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_CA0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_CA0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0x2, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_CEB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2, 2, lambda_CEB)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0x3, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_D36():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x3, 2, lambda_D36)
    StopSound(825, 1000, 40)
    Sleep(1000)
    NewScene("m9005", 105, 0, 0)
    IdleLoop()
    Return()

    # Function_5_BFC end

    def Function_6_D55(): pass

    label("Function_6_D55")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D6D")
    LoadChrToIndex("chr/ch03150.itc", 0x23)

    label("loc_D6D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D85")
    LoadChrToIndex("chr/ch03250.itc", 0x23)

    label("loc_D85")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D9D")
    LoadChrToIndex("chr/ch02950.itc", 0x23)

    label("loc_D9D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DB5")
    LoadChrToIndex("chr/ch00950.itc", 0x23)

    label("loc_DB5")

    Return()

    # Function_6_D55 end

    def Function_7_DB6(): pass

    label("Function_7_DB6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DCE")
    LoadChrToIndex("chr/ch03150.itc", 0x24)

    label("loc_DCE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DE6")
    LoadChrToIndex("chr/ch03250.itc", 0x24)

    label("loc_DE6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DFE")
    LoadChrToIndex("chr/ch02950.itc", 0x24)

    label("loc_DFE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E16")
    LoadChrToIndex("chr/ch00950.itc", 0x24)

    label("loc_E16")

    Return()

    # Function_7_DB6 end

    def Function_8_E17(): pass

    label("Function_8_E17")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E2F")
    LoadChrToIndex("chr/ch03056.itc", 0x29)

    label("loc_E2F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E47")
    LoadChrToIndex("chr/ch03253.itc", 0x29)

    label("loc_E47")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E5F")
    LoadChrToIndex("chr/ch0295F.itc", 0x29)

    label("loc_E5F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E77")
    LoadChrToIndex("chr/ch00953.itc", 0x29)

    label("loc_E77")

    Return()

    # Function_8_E17 end

    def Function_9_E78(): pass

    label("Function_9_E78")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E90")
    LoadChrToIndex("chr/ch03056.itc", 0x2A)

    label("loc_E90")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_EA8")
    LoadChrToIndex("chr/ch03253.itc", 0x2A)

    label("loc_EA8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_EC0")
    LoadChrToIndex("chr/ch0295F.itc", 0x2A)

    label("loc_EC0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_ED8")
    LoadChrToIndex("chr/ch00953.itc", 0x2A)

    label("loc_ED8")

    Return()

    # Function_9_E78 end

    def Function_10_ED9(): pass

    label("Function_10_ED9")

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

    def lambda_11D6():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_11D6)
    Sleep(50)

    def lambda_11EE():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_11EE)
    Sleep(50)

    def lambda_1206():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1206)
    Sleep(50)

    def lambda_121E():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_121E)
    Sleep(50)

    def lambda_1236():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_1236)
    Sleep(50)

    def lambda_124E():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_124E)
    OP_0D()
    Sleep(1600)
    StopBGM(0x7D0)
    OP_C9(0x0, 0x80000000)

    NpcTalk(
        0x9,
        "Bold Voice",
        (
            "#3847V#11P#N#33A#30WEh eh──\x01",
            "You got through the preliminary matches, huh?\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_14A5")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1460")
    OP_FC(0xFFF4)
    Jump("loc_1463")

    label("loc_1460")

    OP_FC(0xC)

    label("loc_1463")


    ChrTalk(
        0x10A,
        "#00601F#13PThe "Red Constellation" vice leader, eh...?\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_1546")

    label("loc_14A5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_150F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_14CF")
    OP_FC(0xFFF4)
    Jump("loc_14D2")

    label("loc_14CF")

    OP_FC(0xC)

    label("loc_14D2")


    ChrTalk(
        0x109,
        "#10101F#13PThe "Red Constellation" vice leader...\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_1546")

    label("loc_150F")


    ChrTalk(
        0x102,
        "#00101F#12PThe "Red Constellation" vice leader...\x02",
    )

    CloseMessageWindow()

    label("loc_1546")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_15B1")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1570")
    OP_FC(0xFFF4)
    Jump("loc_1573")

    label("loc_1570")

    OP_FC(0xC)

    label("loc_1573")


    ChrTalk(
        0x106,
        (
            "#10708F#13PThe "Red Ogre"...\x01",
            "The strongest jaeger.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_165F")

    label("loc_15B1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1620")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_15DB")
    OP_FC(0xFFF4)
    Jump("loc_15DE")

    label("loc_15DB")

    OP_FC(0xC)

    label("loc_15DE")


    ChrTalk(
        0x105,
        (
            "#10408F#13PThe "Red Ogre"...\x01",
            "The strongest jaeger, eh?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_165F")

    label("loc_1620")


    ChrTalk(
        0x103,
        (
            "#00208F#12PThe "Red Ogre"...\x01",
            "The strongest jaeger, right?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_165F")

    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x8,
        (
            "Eh eh...that's right.\x02\x03",
            "I was almost as strong\x01",
            "as the "War God" and\x01",
            "the "Jaeger King", but...\x02\x03",
            "After those two killed each other,\x01",
            "I can say that I'm the strongest.\x02\x03",
            "──"Up to now", that is.\x02",
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
            "#04503F#5PRandolph...\x01",
            "You too should've noticed already.\x02\x03",
            "With this situation in Crossbell and\x01",
            "the disorders in the Erebonian Empire,\x01",
            "Zemuria is headed for turbulent times.\x02\x03",
            "#04501FThe places for our jaegers' activities\x01",
            "will increase more than ever.\x02\x03",
            "Terrorists will be in high spirits, the "Snake" \x01",
            "and the "Church" secret feud will broaden,\x01",
            "the Bracers will become desperate.\x02\x03",
            "#04504FYou too should tell by experience...\x02\x03",
            "#04502F──That they're bound to be truly over;\x01",
            "the peaceful times...are over.\x02",
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
        "#00010F#12P...Saying whatever you want...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#12PBut...\x01",
            "He's not necessarily mistaking.\x02\x03",
            "#00106FWith the Crossbell incident...\x01",
            "The civil war in the Empire and the disorders\x01",
            "in the Republic, Zemuria is greatly swaying...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00201F#12PCould it be that...\x01",
            "Even if no incident happened in Crossbell, \x01",
            "it would have been inevitable...?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1BE7")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1B4A")
    OP_FC(0xFFF4)
    Jump("loc_1B4D")

    label("loc_1B4A")

    OP_FC(0xC)

    label("loc_1B4D")


    ChrTalk(
        0x106,
        (
            "#10703F#13P...It's true that sparkles were \x01",
            "smouldering everywhere in Zemuria.\x02\x03",
            "#10701FThe Crossbell incident was,\x01",
            "after all, just the excuse.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_1D86")

    label("loc_1BE7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1CB9")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1C11")
    OP_FC(0xFFF4)
    Jump("loc_1C14")

    label("loc_1C11")

    OP_FC(0xC)

    label("loc_1C14")


    ChrTalk(
        0x10A,
        (
            "#00606F#13P...It's true that sparkles were\x01",
            "smouldering everywhere in Zemuria.\x02\x03",
            "#00601FThe Crossbell incident was, after all,\x01",
            "nothing more than a pretext.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_1D86")

    label("loc_1CB9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1D86")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1CE3")
    OP_FC(0xFFF4)
    Jump("loc_1CE6")

    label("loc_1CE3")

    OP_FC(0xC)

    label("loc_1CE6")


    ChrTalk(
        0x105,
        (
            "#10406F#13P...It's true that sparkles were\x01",
            "smouldering everywhere in Zemuria.\x02\x03",
            "#10401FThe Crossbell incident was, after all,\x01",
            "nothing more than an excuse.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_1D86")


    ChrTalk(
        0x104,
        (
            "#00306FYeah#12P...you're right.\x02\x03",
            "#00311FBut it's true that...\x01",
            "I could tell about it.\x02\x03",
            "About the presentiment of a storm...\x01",
            "The smell of a battlefield hangin' over.\x02",
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
            "#04502F#5PEh eh, that's the very proof of\x01",
            "you being a jaeger to the bone...\x02\x03",
            "And the "karma" of the warrior\x01",
            "blood running in the Orlando family.\x02\x03",
            "#04503FAnd yet, Randolph...\x01",
            "Why don't you open your eyes?\x02\x03",
            "#04501FHow can you live a tranquil\x01",
            "life while lying to yourself?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00311F#12P#30W............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04501F#5P──This is the last time.\x01",
            "Randolph, succeed the "War God".\x02\x03",
            "I'll teach you what you\x01",
            "lack instead of big bro.\x02\x03",
            "#04504FThen, the day you'll become the boss of the\x01",
            ""Red Constellation" in name and substance...\x02\x03",
            "#04502FWe'll support whoever you want as you wish.\x02",
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
            "#04504F#5PEh eh, of course Crossbell\x01",
            "too would be all right.\x02\x03",
            "#04502FNo matter how this incident turns out,\x01",
            "no doubt that heavy hardships will await.\x01\x02\x03",
            "You could do it even\x01",
            "for you "comrades"...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00010F#12P...Kh...\x02",
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
            "#00211F#12P...You are taking advantage\x01",
            "of the situation too much...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(150)
    BeginChrThread(0x104, 3, 0, 17)
    WaitChrThread(0x104, 3)
    Sleep(200)

    def lambda_2213():
        OP_A6(0xFE, 0x0, 0x14, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_2213)
    WaitChrThread(0x104, 2)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#00304F#12P#30WEh eh, I see...\x02\x03",
            "#00312FCool-headed and tames fierce\x01",
            "impulses rationally...\x02\x03",
            "The "Ogre Rosso", indeed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04504F#5PThat's why a jaeger is a jaeger...\x01",
            "You should get it too.\x02\x03",
            "#04502FAfter the peaceful times have passed,\x01",
            "you won't have a "foothold" where to\x01",
            "resist anywhere.\x02\x03",
            "Then, could there be any room for hesitations?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00303F#12PThat could be true...\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x104, 3, 0, 18)
    WaitChrThread(0x104, 3)
    Sleep(350)

    ChrTalk(
        0x104,
        "#00301F#12P──But my answer is NO.\x02",
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
        "#04505F#5P...Ooh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00315F#12PIt appears your poor work of a nephew\x01",
            "has stranded from the path, huh...?\x02\x03",
            "#00304FSeekin' peace in turbulent times,\x01",
            "seekin' justice in a world of deceit...\x02\x03",
            "Even more, neither as a fantasy\x01",
            "nor as an illusion, but by steadily\x01",
            "accumulatin' what we can do...\x02\x03",
            "#00302F──That's the kind of\x01",
            ""foothold" I've found out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00214F#12PMr. Randy...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2644")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2626")
    OP_FC(0xFFF4)
    Jump("loc_2629")

    label("loc_2626")

    OP_FC(0xC)

    label("loc_2629")


    ChrTalk(
        0x109,
        "#10100F#13PSenior...\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_2644")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2695")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_266E")
    OP_FC(0xFFF4)
    Jump("loc_2671")

    label("loc_266E")

    OP_FC(0xC)

    label("loc_2671")


    ChrTalk(
        0x10A,
        "#00604F#13PHmph, conceited...\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_2695")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2709")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_26BF")
    OP_FC(0xFFF4)
    Jump("loc_26C2")

    label("loc_26BF")

    OP_FC(0xC)

    label("loc_26C2")


    ChrTalk(
        0x105,
        (
            "#10402F#13PHu hu, I wonder if he took\x01",
            "a certain someone's trait?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_2709")


    ChrTalk(
        0x8,
        "#04501F#5P............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F#12PI'll stand up against my own "karma"\x01",
            "by means of this "foothold".\x02\x03",
            "#00308FThose nostalgic battlefields days...\x01",
            "I totally said farewell to those where\x01",
            "I could only live in a veritable hell.\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x104, 3, 0, 19)
    WaitChrThread(0x104, 3)
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x104,
        "#00301F#12P#30WThis is──my way to settle things.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002F#12PRandy...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00104F#12P...We'll watch over you too.\x02",
    )

    CloseMessageWindow()
    StopSound(130, 3000, 30)
    StopSound(825, 3000, 60)
    Sleep(300)

    def lambda_28A2():
        OP_A6(0xFE, 0x1E, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_28A2)
    WaitChrThread(0x8, 2)
    Sleep(800)

    def lambda_28C2():
        OP_A6(0xFE, 0x28, 0x28, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_28C2)
    WaitChrThread(0x8, 2)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#04502F#5P#30W...Eh eh...\x02\x03",
            "#04504F......Ha ha ha ha......\x02\x03",
            "#04501F──Done with the saucy speech?\x02",
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
        "#00010F#12PKh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00210F#12P#N...Uwaah...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2A77")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2A43")
    OP_FC(0xFFF4)
    Jump("loc_2A46")

    label("loc_2A43")

    OP_FC(0xC)

    label("loc_2A46")


    ChrTalk(
        0x106,
        "#10707F#13PWhat a fighting spirit...!\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_2B36")

    label("loc_2A77")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2AD8")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2AA1")
    OP_FC(0xFFF4)
    Jump("loc_2AA4")

    label("loc_2AA1")

    OP_FC(0xC)

    label("loc_2AA4")


    ChrTalk(
        0x105,
        "#10410F#13PWhat a fighting spirit......!\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_2B36")

    label("loc_2AD8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2B36")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2B02")
    OP_FC(0xFFF4)
    Jump("loc_2B05")

    label("loc_2B02")

    OP_FC(0xC)

    label("loc_2B05")


    ChrTalk(
        0x10A,
        "#00610F#13PWhat fighting spirit he has...!\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_2B36")


    ChrTalk(
        0x8,
        (
            "#04504F#5PHu hu...very well.\x02\x03",
            "I'll ascertain your "stand" by the\x01",
            "means of that unreliable "foothold"...\x02\x03",
            "#04501FHowever...you get it, right?\x02\x03",
            "After stating that much, I\x01",
            "can't go easy anymore, hm...?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopBGM(0xBB8)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x104,
        "#00303F#2771V#12P#30W#20AYeah──that's what I want.\x02",
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
            "#00301F#2772V#12P#30W#46AI'll use the Crafts I learned from the ol'\x01",
            "man and you and all the power I have...\x02\x03",
            "#00307F#2773V#35ATo beat you, who're the\x01",
            "strongest jaeger!!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#04504F#3850V#5P#30W#35AEh eh...interesting.\x02\x03",
            "#04512F#3851V#30W#50AThen, I'll devour you and\x01",
            "succeed the "War God"!\x02\x03",
            "#3852V#30W#50AYou'll be a minimal offering to big\x01",
            "bro who had a poor job of a son!!\x02",
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
            "#3849V#30W#52AThe twin battle-axes of the\x01",
            ""Ogre Rosso", who devour and\x01",
            "tramples on battlefields!!\x02",
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
        "#00107F#6P#N#10A...He's coming...!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00007F#12P#15ALet's face him...!\x01",
            "Support Randy with all you've got!\x02",
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

    # Function_10_ED9 end

    def Function_11_311F(): pass

    label("Function_11_311F")

    OP_9B(0x0, 0xFE, 0x0, 0x1770, 0xFA0, 0x1)
    OP_96(0xFE, 0x0, 0xFA0, 0xD69C, 0xFA0, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_11_311F end

    def Function_12_314A(): pass

    label("Function_12_314A")

    OP_9B(0x0, 0xFE, 0x0, 0x157C, 0xFA0, 0x1)
    OP_96(0xFE, 0x460, 0xFA0, 0xD1C4, 0xFA0, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_12_314A end

    def Function_13_3175(): pass

    label("Function_13_3175")

    OP_9B(0x0, 0xFE, 0x0, 0x157C, 0xFA0, 0x1)
    OP_96(0xFE, 0x1A4, 0xFA0, 0xCC92, 0xFA0, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_13_3175 end

    def Function_14_31A0(): pass

    label("Function_14_31A0")

    OP_9B(0x0, 0xFE, 0x0, 0x157C, 0xFA0, 0x1)
    OP_96(0xFE, 0xFFFFFB0A, 0xFA0, 0xCF4E, 0xFA0, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_14_31A0 end

    def Function_15_31CB(): pass

    label("Function_15_31CB")

    OP_9B(0x0, 0xFE, 0x0, 0x1996, 0xFA0, 0x1)
    OP_96(0xFE, 0xFFFFF614, 0xFA0, 0xD1BA, 0xFA0, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_15_31CB end

    def Function_16_31F6(): pass

    label("Function_16_31F6")

    OP_9B(0x0, 0xFE, 0x0, 0x1AC2, 0xFA0, 0x1)
    OP_96(0xFE, 0x9EC, 0xFA0, 0xD0F2, 0xFA0, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_16_31F6 end

    def Function_17_3221(): pass

    label("Function_17_3221")

    SetChrChipByIndex(0x104, 0x28)
    SetChrFlags(0x104, 0x2)
    SetChrFlags(0x104, 0x1000)
    SetChrSubChip(0xFE, 0x1)
    Sleep(143)
    SetChrSubChip(0xFE, 0x2)
    Sleep(429)
    Return()

    # Function_17_3221 end

    def Function_18_323E(): pass

    label("Function_18_323E")

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

    # Function_18_323E end

    def Function_19_326D(): pass

    label("Function_19_326D")

    SetChrChipByIndex(0x104, 0x28)
    SetChrFlags(0x104, 0x2)
    SetChrFlags(0x104, 0x1000)
    Sound(802, 0, 100, 0)
    SetChrSubChip(0xFE, 0x4)
    Sleep(143)
    SetChrSubChip(0xFE, 0x5)
    Sleep(429)
    Return()

    # Function_19_326D end

    def Function_20_3290(): pass

    label("Function_20_3290")

    Sleep(150)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_20_3290 end

    def Function_21_32A2(): pass

    label("Function_21_32A2")

    Sleep(300)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_21_32A2 end

    def Function_22_32B4(): pass

    label("Function_22_32B4")

    Sleep(450)
    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_22_32B4 end

    def Function_23_32C0(): pass

    label("Function_23_32C0")

    Sleep(600)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_32E0")
    Sound(540, 0, 50, 0)
    Jump("loc_3305")

    label("loc_32E0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3305")
    Sound(531, 0, 100, 0)

    label("loc_3305")

    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_23_32C0 end

    def Function_24_330E(): pass

    label("Function_24_330E")

    Sleep(750)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_332E")
    Sound(540, 0, 50, 0)
    Jump("loc_3353")

    label("loc_332E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3353")
    Sound(531, 0, 100, 0)

    label("loc_3353")

    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_24_330E end

    def Function_25_335C(): pass

    label("Function_25_335C")

    PlayEffect(0x0, 0x5, 0xFE, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    StopEffect(0x5, 0x2)
    Return()

    # Function_25_335C end

    def Function_26_33A5(): pass

    label("Function_26_33A5")

    PlayEffect(0x0, 0x6, 0xFE, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    StopEffect(0x6, 0x2)
    Return()

    # Function_26_33A5 end

    def Function_27_33EE(): pass

    label("Function_27_33EE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3444")
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
    Jump("Function_27_33EE")

    label("loc_3444")

    Return()

    # Function_27_33EE end

    def Function_28_3445(): pass

    label("Function_28_3445")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_345E")
    OP_A1(0xFE, 0x5DC, 0x3, 0x0, 0x1, 0x2)
    Jump("Function_28_3445")

    label("loc_345E")

    Return()

    # Function_28_3445 end

    def Function_29_345F(): pass

    label("Function_29_345F")

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

    # Function_29_345F end

    def Function_30_348E(): pass

    label("Function_30_348E")

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
            "#04510F#6P#40W...Eh eh...\x02\x03",
            "#04511FWho could've thought that with such a "foothold"...\x01",
            "...You'd have done this much...\x02\x03",
            "However...\x01",
            "That too is another of your strengths now...\x02",
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
            "#00306F#12P#30W...Yeah...\x01",
            "Sorry but, I'll have you respect my will...\x02\x03",
            "#00301FAlthough it'll be ingratitude...\x01",
            "...Towards you and the ol' man...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04510F#5P#40WEh eh...what about that now, of all times...?\x02\x03",
            "#04511F...Also, you did the greatest \x01",
            "ingratitude by freely walking\x01",
            "away without settling things...\x02\x03",
            "He never said a single word, but...\x01",
            "...Big bro too was worried about you, you know...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00308F#12P#30W...I see...my ol' man was...\x02",
    )

    CloseMessageWindow()
    Sleep(200)

    def lambda_38C3():
        OP_A6(0xFE, 0x0, 0x23, 0x12C, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_38C3)
    Sleep(800)

    ChrTalk(
        0x8,
        (
            "#04510F#5P#50WEh eh...however...\x01",
            "Seems you've grown a little face that\x01",
            "wouldn't be a shame to show to him...\x02\x03",
            "#60W...Show me how far that courage...\x01",
            "Can enforce...your will...\x02\x03",
            "Prove it to me...with your...\x01",
            "...future way of living...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)

    def lambda_39D1():
        OP_A6(0xFE, 0x0, 0x23, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_39D1)
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

    # Function_30_348E end

    def Function_31_3B4A(): pass

    label("Function_31_3B4A")

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

    # Function_31_3B4A end

    def Function_32_3B8D(): pass

    label("Function_32_3B8D")

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
        "#00102F#12P#30W...Did we...win...?\x02",
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
        "#00206F#12P#40W...*pant pant*...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3F36")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3EE5")
    OP_FC(0xFFF4)
    Jump("loc_3EE8")

    label("loc_3EE5")

    OP_FC(0xB)

    label("loc_3EE8")


    ChrTalk(
        0x109,
        (
            "#10106F#13P#40WIt's unbelievable...\x01",
            "...That we could really win...\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_3FEC")

    label("loc_3F36")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3F95")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3F60")
    OP_FC(0xFFF4)
    Jump("loc_3F63")

    label("loc_3F60")

    OP_FC(0xB)

    label("loc_3F63")


    ChrTalk(
        0x10A,
        (
            "#00606F#13P#40WIncredible...\x01",
            "We won...\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_3FEC")

    label("loc_3F95")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3FEC")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3FBF")
    OP_FC(0xFFF4)
    Jump("loc_3FC2")

    label("loc_3FBF")

    OP_FC(0xB)

    label("loc_3FC2")


    ChrTalk(
        0x106,
        "#10706F#13P#40W...It's a miracle...\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_3FEC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_406B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4016")
    OP_FC(0xFFF4)
    Jump("loc_4019")

    label("loc_4016")

    OP_FC(0xB)

    label("loc_4019")


    ChrTalk(
        0x105,
        (
            "#10402F#13P#40WJust this time...\x01",
            "...I'll be grateful to the Goddess...\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_411E")

    label("loc_406B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_40C7")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4095")
    OP_FC(0xFFF4)
    Jump("loc_4098")

    label("loc_4095")

    OP_FC(0xB)

    label("loc_4098")


    ChrTalk(
        0x106,
        "#10702F#13P#40W...It's a miracle...\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_411E")

    label("loc_40C7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_411E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_40F1")
    OP_FC(0xFFF4)
    Jump("loc_40F4")

    label("loc_40F1")

    OP_FC(0xB)

    label("loc_40F4")


    ChrTalk(
        0x10A,
        "#00602F#13P#40W...It's a miracle...\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_411E")


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
            "#00000F#12P#30W...No matter what one can say...\x01",
            "He's your "family", right...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00202F#12P#30WIt seems he was worried...\x01",
            "...About Mr. Randy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#11P#30WYeah...I know.\x02\x03",
            "#00303FBein' rough seems to\x01",
            "be my family style...\x02\x03",
            "#00300F...However...\x01",
            "With this, I've settled things, somehow.\x02",
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
            "#00304F#5PIt appears the "territory" was unsealed too.\x02\x03",
            "#00302FFor the time bein'...\x01",
            "Let's go back to the gate.\x02",
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
        "#00204F#12PYou did a very nice job...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00309F#5PHa ha, likewise.\x02",
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

    # Function_32_3B8D end

    def Function_33_44AD(): pass

    label("Function_33_44AD")


    def lambda_44B2():
        OP_A6(0xFE, 0x0, 0x19, 0x12C, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_44B2)
    Sleep(700)
    OP_9B(0x0, 0xFE, 0x162, 0x320, 0x3E8, 0x0)
    OP_95(0xFE, -1200, 4100, 63800, 1000, 0x0)
    TurnDirection(0xFE, 0x8, 500)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_33_44AD end

    def Function_34_4502(): pass

    label("Function_34_4502")

    OP_93(0xFE, 0xB4, 0x1F4)
    OP_95(0xFE, 650, 4100, 59850, 1500, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(700)
    Return()

    # Function_34_4502 end

    def Function_35_4528(): pass

    label("Function_35_4528")

    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_35_4528 end

    def Function_36_4537(): pass

    label("Function_36_4537")

    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_36_4537 end

    def Function_37_4546(): pass

    label("Function_37_4546")

    Sleep(100)
    SetChrChipByIndex(0xFE, 0x26)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_37_4546 end

    def Function_38_4552(): pass

    label("Function_38_4552")

    Sleep(200)
    Sound(811, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_38_4552 end

    def Function_39_4564(): pass

    label("Function_39_4564")

    Sleep(300)
    Sound(514, 0, 50, 0)
    SetChrChipByIndex(0xFE, 0x29)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4599")
    SetChrSubChip(0xFE, 0x2)
    Jump("loc_459D")

    label("loc_4599")

    SetChrSubChip(0xFE, 0x0)

    label("loc_459D")

    Return()

    # Function_39_4564 end

    def Function_40_459E(): pass

    label("Function_40_459E")

    Sleep(400)
    SetChrChipByIndex(0xFE, 0x2A)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_45CD")
    SetChrSubChip(0xFE, 0x2)
    Jump("loc_45D1")

    label("loc_45CD")

    SetChrSubChip(0xFE, 0x0)

    label("loc_45D1")

    Return()

    # Function_40_459E end

    def Function_41_45D2(): pass

    label("Function_41_45D2")

    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x7)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x1000)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x2)
    SetChrFlags(0x8, 0x800)
    Return()

    # Function_41_45D2 end

    SaveToFile()

Try(main)
