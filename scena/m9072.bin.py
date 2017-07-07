from ScenarioHelper import *

def main():
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
        "Kibun Sigmund",         # 1
        "Dummy characters for speech display", # 2
        "Sigmund attendant",         # 3
        "Sigmund attendant",         # 4
        "SE control",                 # 5
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
        "Function_3_830",          # 03, 3
        "Function_4_92C",          # 04, 4
        "Function_5_BB4",          # 05, 5
        "Function_6_D0D",          # 06, 6
        "Function_7_D6E",          # 07, 7
        "Function_8_DCF",          # 08, 8
        "Function_9_E30",          # 09, 9
        "Function_10_E91",         # 0A, 10
        "Function_11_2E4E",        # 0B, 11
        "Function_12_2E79",        # 0C, 12
        "Function_13_2EA4",        # 0D, 13
        "Function_14_2ECF",        # 0E, 14
        "Function_15_2EFA",        # 0F, 15
        "Function_16_2F25",        # 10, 16
        "Function_17_2F50",        # 11, 17
        "Function_18_2F6D",        # 12, 18
        "Function_19_2F9C",        # 13, 19
        "Function_20_2FBF",        # 14, 20
        "Function_21_2FD1",        # 15, 21
        "Function_22_2FE3",        # 16, 22
        "Function_23_2FEF",        # 17, 23
        "Function_24_303D",        # 18, 24
        "Function_25_308B",        # 19, 25
        "Function_26_30D4",        # 1A, 26
        "Function_27_311D",        # 1B, 27
        "Function_28_3174",        # 1C, 28
        "Function_29_318E",        # 1D, 29
        "Function_30_31BD",        # 1E, 30
        "Function_31_37B8",        # 1F, 31
        "Function_32_37FB",        # 20, 32
        "Function_33_410A",        # 21, 33
        "Function_34_415F",        # 22, 34
        "Function_35_4185",        # 23, 35
        "Function_36_4194",        # 24, 36
        "Function_37_41A3",        # 25, 37
        "Function_38_41AF",        # 26, 38
        "Function_39_41C1",        # 27, 39
        "Function_40_41FB",        # 28, 40
        "Function_41_422F",        # 29, 41
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CE, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7DF")

    ChrTalk(
        0x8,
        "……………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301FAlthough it seems to be completely falling … …\x02\x03",
            "#00306FApparently you must bear deadly wounds.\x01",
            "…… Well, it's too tough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00104FShould I bring it to Mercapa?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001FThat's right.\x01",
            "It was a criminal offense of the Crossbell City raid incident,\x01",
            "I would like to do so if I can arrest him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F…… It is dangerous as expected.\x02\x03",
            "#00200FIf there is no alternative to life, in this place\x01",
            "I think that it is wise to leave it alone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303FWell, it will not wake up for a while\x01",
            "I do not have to worry about pursuing it.\x02\x03",
            "#00300FLet's move on now.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1CE, 7)
    Jump("loc_82C")

    label("loc_7DF")


    ChrTalk(
        0x8,
        "……………………………………\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It seems that you are completely obsessed.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_82C")

    TalkEnd(0x8)
    Return()

    # Function_2_5BE end

    def Function_3_830(): pass

    label("Function_3_830")

    OP_F4(0x2)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There are devices that can recover the orbment.\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "To take a break here\x01",      # 0
            "quit\x01",              # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_91D")
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

    label("loc_91D")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_3_830 end

    def Function_4_92C(): pass

    label("Function_4_92C")

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

    def lambda_A40():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_A40)

    def lambda_A51():
        OP_95(0xFE, -230, 4000, 68330, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_A51)
    Sleep(500)
    PlayEffect(0x1, 0xFF, 0x1, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_AA8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_AA8)

    def lambda_AB9():
        OP_95(0xFE, -1240, 4000, 68690, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_AB9)
    Sleep(500)
    Sound(920, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x2, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_B16():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2, 2, lambda_B16)

    def lambda_B27():
        OP_95(0xFE, 1150, 4000, 68650, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_B27)
    Sleep(500)
    PlayEffect(0x1, 0xFF, 0x3, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_B7E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x3, 2, lambda_B7E)

    def lambda_B8F():
        OP_95(0xFE, -2400, 4000, 69350, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_B8F)
    WaitChrThread(0x3, 1)
    Sleep(500)
    OP_E2(0x2)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_4_92C end

    def Function_5_BB4(): pass

    label("Function_5_BB4")

    EventBegin(0x0)
    OP_E2(0x3)
    LoadEffect(0x1, "event/evwarp.eff")
    Sound(936, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x0, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_C0D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_C0D)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0x1, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_C58():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_C58)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0x2, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_CA3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2, 2, lambda_CA3)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0x3, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_CEE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x3, 2, lambda_CEE)
    StopSound(825, 1000, 40)
    Sleep(1000)
    NewScene("m9005", 105, 0, 0)
    IdleLoop()
    Return()

    # Function_5_BB4 end

    def Function_6_D0D(): pass

    label("Function_6_D0D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D25")
    LoadChrToIndex("chr/ch03150.itc", 0x23)

    label("loc_D25")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D3D")
    LoadChrToIndex("chr/ch03250.itc", 0x23)

    label("loc_D3D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D55")
    LoadChrToIndex("chr/ch02950.itc", 0x23)

    label("loc_D55")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D6D")
    LoadChrToIndex("chr/ch00950.itc", 0x23)

    label("loc_D6D")

    Return()

    # Function_6_D0D end

    def Function_7_D6E(): pass

    label("Function_7_D6E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D86")
    LoadChrToIndex("chr/ch03150.itc", 0x24)

    label("loc_D86")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D9E")
    LoadChrToIndex("chr/ch03250.itc", 0x24)

    label("loc_D9E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DB6")
    LoadChrToIndex("chr/ch02950.itc", 0x24)

    label("loc_DB6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DCE")
    LoadChrToIndex("chr/ch00950.itc", 0x24)

    label("loc_DCE")

    Return()

    # Function_7_D6E end

    def Function_8_DCF(): pass

    label("Function_8_DCF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DE7")
    LoadChrToIndex("chr/ch03056.itc", 0x29)

    label("loc_DE7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DFF")
    LoadChrToIndex("chr/ch03253.itc", 0x29)

    label("loc_DFF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E17")
    LoadChrToIndex("chr/ch0295F.itc", 0x29)

    label("loc_E17")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E2F")
    LoadChrToIndex("chr/ch00953.itc", 0x29)

    label("loc_E2F")

    Return()

    # Function_8_DCF end

    def Function_9_E30(): pass

    label("Function_9_E30")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E48")
    LoadChrToIndex("chr/ch03056.itc", 0x2A)

    label("loc_E48")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E60")
    LoadChrToIndex("chr/ch03253.itc", 0x2A)

    label("loc_E60")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E78")
    LoadChrToIndex("chr/ch0295F.itc", 0x2A)

    label("loc_E78")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E90")
    LoadChrToIndex("chr/ch00953.itc", 0x2A)

    label("loc_E90")

    Return()

    # Function_9_E30 end

    def Function_10_E91(): pass

    label("Function_10_E91")

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

    def lambda_118E():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_118E)
    Sleep(50)

    def lambda_11A6():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_11A6)
    Sleep(50)

    def lambda_11BE():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_11BE)
    Sleep(50)

    def lambda_11D6():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_11D6)
    Sleep(50)

    def lambda_11EE():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_11EE)
    Sleep(50)

    def lambda_1206():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_1206)
    OP_0D()
    Sleep(1600)
    StopBGM(0x7D0)
    OP_C9(0x0, 0x80000000)

    NpcTalk(
        0x9,
        "A bold voice",
        (
            "#3847V#11P#N#33A#30WUgly\x01",
            "Did you get through the battlefield?\x02",
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
        "#00311F#12PUncle Takashi ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00013F#12PSigmund Orlando …\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_143C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1408")
    OP_FC(0xFFF4)
    Jump("loc_140B")

    label("loc_1408")

    OP_FC(0xC)

    label("loc_140B")


    ChrTalk(
        0x10A,
        "#00601F#13PDeputy head of the \"red constellation\" ……\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_14C1")

    label("loc_143C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1498")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1466")
    OP_FC(0xFFF4)
    Jump("loc_1469")

    label("loc_1466")

    OP_FC(0xC)

    label("loc_1469")


    ChrTalk(
        0x109,
        "#10101F#13PDeputy head of the \"red constellation\" ……\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_14C1")

    label("loc_1498")


    ChrTalk(
        0x102,
        "#00101F#12PDeputy head of the \"red constellation\" ……\x02",
    )

    CloseMessageWindow()

    label("loc_14C1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_152E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_14EB")
    OP_FC(0xFFF4)
    Jump("loc_14EE")

    label("loc_14EB")

    OP_FC(0xC)

    label("loc_14EE")


    ChrTalk(
        0x106,
        (
            "#10708F#13P\"Red war demon\" ……\x01",
            "It is one of the strongest hunters.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_15D3")

    label("loc_152E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1599")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1558")
    OP_FC(0xFFF4)
    Jump("loc_155B")

    label("loc_1558")

    OP_FC(0xC)

    label("loc_155B")


    ChrTalk(
        0x105,
        (
            "#10408F#13P\"Red war demon\" ……\x01",
            "It is one of the strongest hunters.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_15D3")

    label("loc_1599")


    ChrTalk(
        0x103,
        (
            "#00208F#12P\"Red war demon\" ……\x01",
            "Is it one of the strongest hunters?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15D3")

    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x8,
        (
            "Kuku … That's right.\x02\x03",
            "If you say that you want to stretch me \"fighting spirit\" and\x01",
            "It was about \"King of Hunters\" ……\x02\x03",
            "After the two people have disagreed,\x01",
            "Maybe I am the strongest.\x02\x03",
            "─ ─ It is \"current point\" to the last.\x02",
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
        "#00305F#12P……!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04503F#5PRandolph ……\x01",
            "You should be aware of it.\x02\x03",
            "The situation of this crossbell and\x01",
            "By the turbulence of Eleven Empire\x01",
            "The continent has reached a turbulent era.\x02\x03",
            "#04501FMore than ever, we are a hunter\x01",
            "The place of active activity will increase.\x02\x03",
            "The terrorists raised their minds,\x01",
            "The battle of \"snake\" and \"church\" spread,\x01",
            "The strikers will be amazed.\x02\x03",
            "#04504FYou should feel it with your skin.\x02\x03",
            "#04502F─ ─ to end exactly\x01",
            "The peaceful era has ended.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00311F#12P…………………………………….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00010F#12P… … selfish … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#12PBut …\x01",
            "You are not wrong.\x02\x03",
            "#00106FCrossbell incident ……\x01",
            "And in the civil war of the Empire and the mess of the Republic\x01",
            "The continent is now shaking greatly …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00201F#12PDid you mean ……\x01",
            "Even if the Crossbell incident does not occur\x01",
            "It was inevitable ……?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1A8F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_19FE")
    OP_FC(0xFFF4)
    Jump("loc_1A01")

    label("loc_19FE")

    OP_FC(0xC)

    label("loc_1A01")


    ChrTalk(
        0x106,
        (
            "#10703F#13P…… Ground fuse throughout the continent\x01",
            "It is true that he was smoldering.\x02\x03",
            "#10701FCrossbell incidents to the last\x01",
            "It will only be a chance.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_1BFA")

    label("loc_1A8F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1B46")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1AB9")
    OP_FC(0xFFF4)
    Jump("loc_1ABC")

    label("loc_1AB9")

    OP_FC(0xC)

    label("loc_1ABC")


    ChrTalk(
        0x10A,
        (
            "#00606F#13P…… Ground fuse throughout the continent\x01",
            "It is true that he was smoldering.\x02\x03",
            "#00601FCrossbell incidents to the last\x01",
            "It was just a chance.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_1BFA")

    label("loc_1B46")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1BFA")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1B70")
    OP_FC(0xFFF4)
    Jump("loc_1B73")

    label("loc_1B70")

    OP_FC(0xC)

    label("loc_1B73")


    ChrTalk(
        0x105,
        (
            "#10406F#13P…… Ground fuse throughout the continent\x01",
            "It is true that he was smoldering.\x02\x03",
            "#10401FCrossbell incidents to the last\x01",
            "It was only a chance.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_1BFA")


    ChrTalk(
        0x104,
        (
            "#00306FAh#12P… … I guess so.\x02\x03",
            "#00311FAnd surely …\x01",
            "I felt it with my skin.\x02\x03",
            "Premonition of Arashi ……\x01",
            "I can smell the battlefield.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008F#12P… …. Randy …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04502F#5PKuku, that is what you\x01",
            "Evidence that it is a hunter to the marrow ……\x02\x03",
            "And flowing to the family of Orlando,\x01",
            "Blood 's work as a warrior#2RKarma#\".\x02\x03",
            "#04503FYet Randolph ……\x01",
            "Why will not you wake up yet?\x02\x03",
            "#04501FWhy do you lie yourself\x01",
            "Can you send a restful life?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00311F#12P#30W……………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04501F#5PThis is the last.\x01",
            "Randolph, \"the fighting spirit\" is seized.\x02\x03",
            "Instead of your brother instead of missing parts\x01",
            "I'll do it for you.\x02\x03",
            "#04504FAnd with the name \"Red constellation\"\x01",
            "To the Akatsuki who became the head coach ……\x02\x03",
            "#04502FWherever you shoulder it is as you wish.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_82(0x32, 0x0, 0x7D0, 0xC8)

    ChrTalk(
        0x104,
        "#00305F#12P……!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04504F#5PKuku, of course this crossbell\x01",
            "It would be nice to shoulder.\x02\x03",
            "#04502FWhatever happens to this matter,\x01",
            "There is no doubt a considerable hardship\x01",
            "I guess they will be waiting.\x02\x03",
            "For \"friends\" as well\x01",
            "Maybe it will be … ….?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00010F#12P…… Ku … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00107F#12PYou……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00211F#12P…… I am watching too much … …\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(150)
    BeginChrThread(0x104, 3, 0, 17)
    WaitChrThread(0x104, 3)
    Sleep(200)

    def lambda_201C():
        OP_A6(0xFE, 0x0, 0x14, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_201C)
    WaitChrThread(0x104, 2)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#00304F#12P#30WI wonder, …\x02\x03",
            "#00312FCold and rational,\x01",
            "Tame of the ferocious impulse …\x02\x03",
            "As expected is \"Red war demon#8ROgre Rosso#\".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04504F#5PThat is the reason why he is a hunter hunter … …\x01",
            "I wonder what you know.\x02\x03",
            "#04502FSince the peaceful era has passed,\x01",
            "You are anti#2RArka#\"Scaffolding\"\x01",
            "There should not be anywhere.\x02\x03",
            "Then if there is room for lost?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00303F#12PMaybe so …\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x104, 3, 0, 18)
    WaitChrThread(0x104, 3)
    Sleep(350)

    ChrTalk(
        0x104,
        "#00301F#12P─ ─ But the answer is NO.\x02",
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
        "#04505F#5P……… ho ………?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00315F#12PApparently you are the unlucky nephew of you\x01",
            "You seem to have gone off the road … ….?\x02\x03",
            "#00304FIn peacetime era demanded peace,\x01",
            "deception#4RGinka#Seeking justice for the world … …\x02\x03",
            "Moreover, without romance and illusion,\x01",
            "What we can do\x01",
            "By accumulating on a steady … ….\x02\x03",
            "#00302F── Such a \"foothold\"\x01",
            "Because the headlines are dirty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00214F#12PRandy san ……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_241A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_23FD")
    OP_FC(0xFFF4)
    Jump("loc_2400")

    label("loc_23FD")

    OP_FC(0xC)

    label("loc_2400")


    ChrTalk(
        0x109,
        "#10100F#13PSenior……\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_241A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_246B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2444")
    OP_FC(0xFFF4)
    Jump("loc_2447")

    label("loc_2444")

    OP_FC(0xC)

    label("loc_2447")


    ChrTalk(
        0x10A,
        "#00604F#13PHye, cheeky ……\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_246B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_24D3")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2495")
    OP_FC(0xFFF4)
    Jump("loc_2498")

    label("loc_2495")

    OP_FC(0xC)

    label("loc_2498")


    ChrTalk(
        0x105,
        (
            "#10402F#13PHuh, from someone\x01",
            "I wonder if it has moved.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_24D3")


    ChrTalk(
        0x8,
        "#04501F#5P………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F#12PWith this \"foothold\"\x01",
            "I will have you resist my \"work\".\x02\x03",
            "#00308FThe days of that old battlefield ……\x01",
            "I had no choice but to live as a Shura\x01",
            "I completely break out with myself.\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x104, 3, 0, 19)
    WaitChrThread(0x104, 3)
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x104,
        "#00301F#12P#30WThis is ─ ─ I am getting along.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002F#12PRandy …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00104F#12P…… We can also see.\x02",
    )

    CloseMessageWindow()
    StopSound(130, 3000, 30)
    StopSound(825, 3000, 60)
    Sleep(300)

    def lambda_2643():
        OP_A6(0xFE, 0x1E, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_2643)
    WaitChrThread(0x8, 2)
    Sleep(800)

    def lambda_2663():
        OP_A6(0xFE, 0x28, 0x28, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_2663)
    WaitChrThread(0x8, 2)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#04502F#5P#30W…………………\x02\x03",
            "#04504F………… ha ha ha …………\x02\x03",
            "#04501F── Is that just for yourself?\x02",
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
        "#00010F#12PDamn\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00210F#12P#N… … Wow …\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_280F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_27E5")
    OP_FC(0xFFF4)
    Jump("loc_27E8")

    label("loc_27E5")

    OP_FC(0xC)

    label("loc_27E8")


    ChrTalk(
        0x106,
        "#10707F#13PWhat a battle …!\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_28B4")

    label("loc_280F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2865")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2839")
    OP_FC(0xFFF4)
    Jump("loc_283C")

    label("loc_2839")

    OP_FC(0xC)

    label("loc_283C")


    ChrTalk(
        0x105,
        "#10410F#13PHow blunt … …!\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_28B4")

    label("loc_2865")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_28B4")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_288F")
    OP_FC(0xFFF4)
    Jump("loc_2892")

    label("loc_288F")

    OP_FC(0xC)

    label("loc_2892")


    ChrTalk(
        0x10A,
        "#00610F#13PThis battle is … !.!\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_28B4")


    ChrTalk(
        0x8,
        (
            "#04504F#5PHuh … I think it would be nice.\x02\x03",
            "With that unreliable \"foothold\"\x01",
            "Your anti#2RArka#Let's admit ……\x02\x03",
            "#04501FBut … you know what?\x02\x03",
            "Because it has been said so far\x01",
            "I can not withhold it anymore … ….?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopBGM(0xBB8)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x104,
        "#00303F#2771V#12P#30W#20AOh ─ ─ Where you want.\x02",
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
            "#00301F#2772V#12P#30W#46AThe fighting skills learned from my father and you\x01",
            "Multiply all of the power you can have … …\x02\x03",
            "#00307F#2773V#35AYou are the strongest hunter\x01",
            "Have the tongue let me down!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#04504F#3850V#5P#30W#35AKuku …… It is funny.\x02\x03",
            "#04512F#3851V#30W#50ASo then I gotta eat you\x01",
            "Let 's succeed the \"fighting spirit\"!\x02\x03",
            "#3852V#30W#50ATo the older brother with a bad son\x01",
            "As aiming at least!\x02",
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
            "#3848V#5P#40W#30ACome on, accept it … ….\x02\x03",
            "#3849V#30W#52AEat battlefield, end up violating,\x01",
            "\"Red war demon#8ROgre Rosso#\"Double War ax!\x02",
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
        "#00107F#6P#N#10A… … I'm coming …!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00007F#12P#15AInterception start … …!\x01",
            "We will cover Randy with full power!\x02",
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

    # Function_10_E91 end

    def Function_11_2E4E(): pass

    label("Function_11_2E4E")

    OP_9B(0x0, 0xFE, 0x0, 0x1770, 0xFA0, 0x1)
    OP_96(0xFE, 0x0, 0xFA0, 0xD69C, 0xFA0, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_11_2E4E end

    def Function_12_2E79(): pass

    label("Function_12_2E79")

    OP_9B(0x0, 0xFE, 0x0, 0x157C, 0xFA0, 0x1)
    OP_96(0xFE, 0x460, 0xFA0, 0xD1C4, 0xFA0, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_12_2E79 end

    def Function_13_2EA4(): pass

    label("Function_13_2EA4")

    OP_9B(0x0, 0xFE, 0x0, 0x157C, 0xFA0, 0x1)
    OP_96(0xFE, 0x1A4, 0xFA0, 0xCC92, 0xFA0, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_13_2EA4 end

    def Function_14_2ECF(): pass

    label("Function_14_2ECF")

    OP_9B(0x0, 0xFE, 0x0, 0x157C, 0xFA0, 0x1)
    OP_96(0xFE, 0xFFFFFB0A, 0xFA0, 0xCF4E, 0xFA0, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_14_2ECF end

    def Function_15_2EFA(): pass

    label("Function_15_2EFA")

    OP_9B(0x0, 0xFE, 0x0, 0x1996, 0xFA0, 0x1)
    OP_96(0xFE, 0xFFFFF614, 0xFA0, 0xD1BA, 0xFA0, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_15_2EFA end

    def Function_16_2F25(): pass

    label("Function_16_2F25")

    OP_9B(0x0, 0xFE, 0x0, 0x1AC2, 0xFA0, 0x1)
    OP_96(0xFE, 0x9EC, 0xFA0, 0xD0F2, 0xFA0, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_16_2F25 end

    def Function_17_2F50(): pass

    label("Function_17_2F50")

    SetChrChipByIndex(0x104, 0x28)
    SetChrFlags(0x104, 0x2)
    SetChrFlags(0x104, 0x1000)
    SetChrSubChip(0xFE, 0x1)
    Sleep(143)
    SetChrSubChip(0xFE, 0x2)
    Sleep(429)
    Return()

    # Function_17_2F50 end

    def Function_18_2F6D(): pass

    label("Function_18_2F6D")

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

    # Function_18_2F6D end

    def Function_19_2F9C(): pass

    label("Function_19_2F9C")

    SetChrChipByIndex(0x104, 0x28)
    SetChrFlags(0x104, 0x2)
    SetChrFlags(0x104, 0x1000)
    Sound(802, 0, 100, 0)
    SetChrSubChip(0xFE, 0x4)
    Sleep(143)
    SetChrSubChip(0xFE, 0x5)
    Sleep(429)
    Return()

    # Function_19_2F9C end

    def Function_20_2FBF(): pass

    label("Function_20_2FBF")

    Sleep(150)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_20_2FBF end

    def Function_21_2FD1(): pass

    label("Function_21_2FD1")

    Sleep(300)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_21_2FD1 end

    def Function_22_2FE3(): pass

    label("Function_22_2FE3")

    Sleep(450)
    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_22_2FE3 end

    def Function_23_2FEF(): pass

    label("Function_23_2FEF")

    Sleep(600)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_300F")
    Sound(540, 0, 50, 0)
    Jump("loc_3034")

    label("loc_300F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3034")
    Sound(531, 0, 100, 0)

    label("loc_3034")

    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_23_2FEF end

    def Function_24_303D(): pass

    label("Function_24_303D")

    Sleep(750)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_305D")
    Sound(540, 0, 50, 0)
    Jump("loc_3082")

    label("loc_305D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3082")
    Sound(531, 0, 100, 0)

    label("loc_3082")

    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_24_303D end

    def Function_25_308B(): pass

    label("Function_25_308B")

    PlayEffect(0x0, 0x5, 0xFE, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    StopEffect(0x5, 0x2)
    Return()

    # Function_25_308B end

    def Function_26_30D4(): pass

    label("Function_26_30D4")

    PlayEffect(0x0, 0x6, 0xFE, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    StopEffect(0x6, 0x2)
    Return()

    # Function_26_30D4 end

    def Function_27_311D(): pass

    label("Function_27_311D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3173")
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
    Jump("Function_27_311D")

    label("loc_3173")

    Return()

    # Function_27_311D end

    def Function_28_3174(): pass

    label("Function_28_3174")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_318D")
    OP_A1(0xFE, 0x5DC, 0x3, 0x0, 0x1, 0x2)
    Jump("Function_28_3174")

    label("loc_318D")

    Return()

    # Function_28_3174 end

    def Function_29_318E(): pass

    label("Function_29_318E")

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

    # Function_29_318E end

    def Function_30_31BD(): pass

    label("Function_30_31BD")

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
            "#04510F#6P#40W……… Kuku …………\x02\x03",
            "#04511FNo way in such a \"foothold\" ……\x01",
            "…… And to step on that … …\x02\x03",
            "But …\x01",
            "Is that your strength now … ….\x02",
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
            "#00306F#12P#30W……Ah……\x01",
            "To have bad penetrate … …\x02\x03",
            "#00301FTo you and your father ……\x01",
            "…… I will not oblige you … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04510F#5P#40WKuku …… nowadays … ….?\x02\x03",
            "#04511F…… And the first obligation is\x01",
            "Without taking a trip and getting to know\x01",
            "It probably was flowing … ….\x02\x03",
            "I did not say a word … …\x01",
            "… … My brother was also worried … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00308F#12P#30W…… I see … my dad … ….\x02",
    )

    CloseMessageWindow()
    Sleep(200)

    def lambda_3568():
        OP_A6(0xFE, 0x0, 0x23, 0x12C, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_3568)
    Sleep(800)

    ChrTalk(
        0x8,
        (
            "#04510F#5P#50Wクク……But …\x01",
            "A little can face the older brother\x01",
            "It looks like she became a face …\x02\x03",
            "#60W…… That strength is\x01",
            "Where can you penetrate … ….\x02\x03",
            "In the future of life ……\x01",
            "… … … Proof … … please do … …\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)

    def lambda_363F():
        OP_A6(0xFE, 0x0, 0x23, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_363F)
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

    # Function_30_31BD end

    def Function_31_37B8(): pass

    label("Function_31_37B8")

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

    # Function_31_37B8 end

    def Function_32_37FB(): pass

    label("Function_32_37FB")

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
        "#00005F#11P#30WAh……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00102F#12P#30W… … or … I won … ….?\x02",
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
        "#00206F#12P#40W……Ha Ha……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3B9F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3B56")
    OP_FC(0xFFF4)
    Jump("loc_3B59")

    label("loc_3B56")

    OP_FC(0xB)

    label("loc_3B59")


    ChrTalk(
        0x109,
        (
            "#10106F#13P#40WIncredible……\x01",
            "…… I really could win … …\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_3C5F")

    label("loc_3B9F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3C0A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3BC9")
    OP_FC(0xFFF4)
    Jump("loc_3BCC")

    label("loc_3BC9")

    OP_FC(0xB)

    label("loc_3BCC")


    ChrTalk(
        0x10A,
        (
            "#00606F#13P#40WI can not believe it ….\x01",
            "I was able to win well …\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_3C5F")

    label("loc_3C0A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3C5F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3C34")
    OP_FC(0xFFF4)
    Jump("loc_3C37")

    label("loc_3C34")

    OP_FC(0xB)

    label("loc_3C37")


    ChrTalk(
        0x106,
        "#10706F#13P#40W… … It's a miracle …\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_3C5F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3CCE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3C89")
    OP_FC(0xFFF4)
    Jump("loc_3C8C")

    label("loc_3C89")

    OP_FC(0xB)

    label("loc_3C8C")


    ChrTalk(
        0x105,
        (
            "#10402F#13P#40WOnly this time …\x01",
            "… … I thank the goddess … …\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_3D7B")

    label("loc_3CCE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3D28")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3CF8")
    OP_FC(0xFFF4)
    Jump("loc_3CFB")

    label("loc_3CF8")

    OP_FC(0xB)

    label("loc_3CFB")


    ChrTalk(
        0x106,
        "#10702F#13P#40W… … It's a miracle …\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_3D7B")

    label("loc_3D28")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3D7B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3D52")
    OP_FC(0xFFF4)
    Jump("loc_3D55")

    label("loc_3D52")

    OP_FC(0xB)

    label("loc_3D55")


    ChrTalk(
        0x10A,
        "#00602F#13P#40W… … It's a miracle ……\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_3D7B")


    ChrTalk(
        0x104,
        "#00306F#11P#30W……Ah………\x02",
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
        "#00308F#11P#30W………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#12P#30W…… Whatever ……\x01",
            "It was a \"family\" … ….?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00202F#12P#30WAbout Randy's … ….\x01",
            "… … It sounds like you were worried.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#11P#30WOh … I knew it.\x02\x03",
            "#00303FThe rough one is the family of our family\x01",
            "Because it is a monstrous monster ……\x02\x03",
            "#00300F……But …\x01",
            "I managed to get a rush on this.\x02",
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
            "#00304F#5P\"Area\" could also be released.\x02\x03",
            "#00302FTentatively …\x01",
            "Let's go back to the gate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00104F#12PI see …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002F#12P… …. Tired, Randy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00204F#12PCongratulations! …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00309F#5PHaha, that is it.\x02",
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

    # Function_32_37FB end

    def Function_33_410A(): pass

    label("Function_33_410A")


    def lambda_410F():
        OP_A6(0xFE, 0x0, 0x19, 0x12C, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_410F)
    Sleep(700)
    OP_9B(0x0, 0xFE, 0x162, 0x320, 0x3E8, 0x0)
    OP_95(0xFE, -1200, 4100, 63800, 1000, 0x0)
    TurnDirection(0xFE, 0x8, 500)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_33_410A end

    def Function_34_415F(): pass

    label("Function_34_415F")

    OP_93(0xFE, 0xB4, 0x1F4)
    OP_95(0xFE, 650, 4100, 59850, 1500, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(700)
    Return()

    # Function_34_415F end

    def Function_35_4185(): pass

    label("Function_35_4185")

    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_35_4185 end

    def Function_36_4194(): pass

    label("Function_36_4194")

    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_36_4194 end

    def Function_37_41A3(): pass

    label("Function_37_41A3")

    Sleep(100)
    SetChrChipByIndex(0xFE, 0x26)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_37_41A3 end

    def Function_38_41AF(): pass

    label("Function_38_41AF")

    Sleep(200)
    Sound(811, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_38_41AF end

    def Function_39_41C1(): pass

    label("Function_39_41C1")

    Sleep(300)
    Sound(514, 0, 50, 0)
    SetChrChipByIndex(0xFE, 0x29)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_41F6")
    SetChrSubChip(0xFE, 0x2)
    Jump("loc_41FA")

    label("loc_41F6")

    SetChrSubChip(0xFE, 0x0)

    label("loc_41FA")

    Return()

    # Function_39_41C1 end

    def Function_40_41FB(): pass

    label("Function_40_41FB")

    Sleep(400)
    SetChrChipByIndex(0xFE, 0x2A)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_422A")
    SetChrSubChip(0xFE, 0x2)
    Jump("loc_422E")

    label("loc_422A")

    SetChrSubChip(0xFE, 0x0)

    label("loc_422E")

    Return()

    # Function_40_41FB end

    def Function_41_422F(): pass

    label("Function_41_422F")

    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x7)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x1000)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x2)
    SetChrFlags(0x8, 0x800)
    Return()

    # Function_41_422F end

    SaveToFile()

Try(main)
