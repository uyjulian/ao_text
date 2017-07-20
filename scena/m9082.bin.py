from ScenarioHelper import *

def main():
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
        "Arios",               # 1
        "Dummy characters for speech display", # 2
        "Supplied with Arios",           # 3
        "Supplied with Arios",           # 4
        "Dummy characters for effect display",# 5
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
        "Function_3_78F",          # 03, 3
        "Function_4_88B",          # 04, 4
        "Function_5_B0F",          # 05, 5
        "Function_6_C62",          # 06, 6
        "Function_7_CC3",          # 07, 7
        "Function_8_D24",          # 08, 8
        "Function_9_D37",          # 09, 9
        "Function_10_575F",        # 0A, 10
        "Function_11_578A",        # 0B, 11
        "Function_12_57B5",        # 0C, 12
        "Function_13_57E0",        # 0D, 13
        "Function_14_580B",        # 0E, 14
        "Function_15_5836",        # 0F, 15
        "Function_16_585A",        # 10, 16
        "Function_17_586C",        # 11, 17
        "Function_18_587E",        # 12, 18
        "Function_19_5890",        # 13, 19
        "Function_20_589C",        # 14, 20
        "Function_21_58EA",        # 15, 21
        "Function_22_5938",        # 16, 22
        "Function_23_5961",        # 17, 23
        "Function_24_59AB",        # 18, 24
        "Function_25_59D8",        # 19, 25
        "Function_26_5A04",        # 1A, 26
        "Function_27_5A27",        # 1B, 27
        "Function_28_5A70",        # 1C, 28
        "Function_29_5AB9",        # 1D, 29
        "Function_30_5AD5",        # 1E, 30
        "Function_31_5B49",        # 1F, 31
        "Function_32_76AE",        # 20, 32
        "Function_33_76F7",        # 21, 33
        "Function_34_7761",        # 22, 34
        "Function_35_7FDC",        # 23, 35
        "Function_36_7FEC",        # 24, 36
        "Function_37_7FFB",        # 25, 37
        "Function_38_800D",        # 26, 38
        "Function_39_801F",        # 27, 39
        "Function_40_802B",        # 28, 40
        "Function_41_8079",        # 29, 41
        "Function_42_80C7",        # 2A, 42
        "Function_43_80EE",        # 2B, 43
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CF, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_73E")

    ChrTalk(
        0x8,
        "…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001F…… I am entirely distracted.\x01",
            "It seems that there is no alternative to life.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FIt was truly a terrible partner …\x01",
            "Every one of us to doing so far.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00208FIt is truly \"a sword of the wind\" … ….\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_641")

    ChrTalk(
        0x10A,
        "#00603FHuh … … I could win well.\x02",
    )

    CloseMessageWindow()

    label("loc_641")


    ChrTalk(
        0x101,
        (
            "#00003FShizuku will also be worried,\x01",
            "I want to carry it to Mercapa soon ….\x02\x03",
            "#00001F…… Ahead this time with Mr. Marybele\x01",
            "Mr. Ian is waiting.\x02\x03",
            "#00003FI am sorry,\x01",
            "I will let you postpone now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FWell … let's go.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1CF, 0)
    Jump("loc_78B")

    label("loc_73E")


    ChrTalk(
        0x8,
        "…\x02",
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

    label("loc_78B")

    TalkEnd(0x8)
    Return()

    # Function_2_517 end

    def Function_3_78F(): pass

    label("Function_3_78F")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_87C")
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

    label("loc_87C")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_3_78F end

    def Function_4_88B(): pass

    label("Function_4_88B")

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

    def lambda_99B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_99B)

    def lambda_9AC():
        OP_95(0xFE, -240, 12000, 218120, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_9AC)
    Sleep(500)
    PlayEffect(0x1, 0xFF, 0x1, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_A03():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_A03)

    def lambda_A14():
        OP_95(0xFE, -1420, 12000, 218280, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_A14)
    Sleep(500)
    Sound(920, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x2, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_A71():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2, 2, lambda_A71)

    def lambda_A82():
        OP_95(0xFE, 1060, 12000, 218310, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_A82)
    Sleep(500)
    PlayEffect(0x1, 0xFF, 0x3, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_AD9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x3, 2, lambda_AD9)

    def lambda_AEA():
        OP_95(0xFE, -2780, 12000, 218680, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_AEA)
    WaitChrThread(0x3, 1)
    Sleep(500)
    OP_E2(0x2)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_4_88B end

    def Function_5_B0F(): pass

    label("Function_5_B0F")

    EventBegin(0x0)
    OP_E2(0x3)
    LoadEffect(0x1, "event/evwarp.eff")
    Sound(936, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x0, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_B68():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_B68)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0x1, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_BB3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_BB3)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0x2, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_BFE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2, 2, lambda_BFE)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0x3, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_C49():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x3, 2, lambda_C49)
    Sleep(1000)
    NewScene("m9008", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_5_B0F end

    def Function_6_C62(): pass

    label("Function_6_C62")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C7A")
    LoadChrToIndex("chr/ch03150.itc", 0x23)

    label("loc_C7A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C92")
    LoadChrToIndex("chr/ch03250.itc", 0x23)

    label("loc_C92")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CAA")
    LoadChrToIndex("chr/ch02950.itc", 0x23)

    label("loc_CAA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CC2")
    LoadChrToIndex("chr/ch00950.itc", 0x23)

    label("loc_CC2")

    Return()

    # Function_6_C62 end

    def Function_7_CC3(): pass

    label("Function_7_CC3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CDB")
    LoadChrToIndex("chr/ch03150.itc", 0x24)

    label("loc_CDB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CF3")
    LoadChrToIndex("chr/ch03250.itc", 0x24)

    label("loc_CF3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D0B")
    LoadChrToIndex("chr/ch02950.itc", 0x24)

    label("loc_D0B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D23")
    LoadChrToIndex("chr/ch00950.itc", 0x24)

    label("loc_D23")

    Return()

    # Function_7_CC3 end

    def Function_8_D24(): pass

    label("Function_8_D24")

    EventBegin(0x0)
    StopBGM(0xFA0)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    EventEnd(0x5)
    Return()

    # Function_8_D24 end

    def Function_9_D37(): pass

    label("Function_9_D37")

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

    def lambda_102A():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_102A)
    Sleep(50)

    def lambda_1042():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1042)
    Sleep(50)

    def lambda_105A():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_105A)
    Sleep(50)

    def lambda_1072():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1072)
    Sleep(50)

    def lambda_108A():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_108A)
    Sleep(50)

    def lambda_10A2():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_10A2)
    OP_0D()
    Sleep(2400)
    OP_C9(0x0, 0x80000000)

    NpcTalk(
        0x8,
        "Male voice",
        "#4064V#6P#30W#16AYou made it.\x02",
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
        "#00001F#12PArios…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301F#12PThe dress of that secretary is already\x01",
            "You did not do that …?\x02",
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
            "Despite Mr. Crois' request,\x01",
            "Originally, it is impossible personnel affair.\x02\x03",
            "As there was an invalid declaration of an independent country,\x01",
            "I can not qualify to wear that one.\x02\x03",
            "I am not a government head of state nor a bracer\x02\x03",
            "As just a blunt swordsman\x01",
            "Think of being standing here.\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1406")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_13DE")
    OP_FC(0xFFF4)
    Jump("loc_13E1")

    label("loc_13DE")

    OP_FC(0xC)

    label("loc_13E1")


    ChrTalk(
        0x10A,
        "#00600F#13PMcRae …\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_1455")

    label("loc_1406")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1455")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1430")
    OP_FC(0xFFF4)
    Jump("loc_1433")

    label("loc_1430")

    OP_FC(0xC)

    label("loc_1433")


    ChrTalk(
        0x109,
        "#10113F#13PArios…\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_1455")


    ChrTalk(
        0x102,
        "#00108F#12PWhy would you\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00206F#12PToo honest…\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00004F#12PAhah, well crap\x02\x03",
            "#00008FThere are various things I want to hear\x01",
            "I can not organize it ….\x02\x03",
            "#00000FEven if you first \"answer\"\x01",
            "Do you mind……?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01404FAh#5P─ ─ We plan on doing so.\x02\x03",
            "#01400FYou better listen …\x01",
            "Except for only one thing\x01",
            "Let's answer everything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003F#12PWell then\x02",
    )

    CloseMessageWindow()
    ClearScenarioFlags(0x0, 3)
    ClearScenarioFlags(0x0, 0)
    ClearScenarioFlags(0x0, 1)
    ClearScenarioFlags(0x0, 2)

    label("loc_15EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A20")
    FadeToDark(300, 0, 100)
    OP_0D()
    MenuCmd(0, 0)
    MenuCmd(1, 0, "About \"accident\" five years ago")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1647")
    MenuCmd(1, 0, "About relationship with Ian lawyer")

    label("loc_1647")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1670")
    MenuCmd(1, 0, "About Ka'aa at a black auctioneer")

    label("loc_1670")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1697")
    MenuCmd(1, 0, "About the day when Guy died")

    label("loc_1697")

    MenuCmd(2, 0, -1, -1, 0)
    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_16D1"),
        (1, "loc_234B"),
        (2, "loc_2D7F"),
        (3, "loc_3A13"),
        (SWITCH_DEFAULT, "loc_3A1B"),
    )


    label("loc_16D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2208")

    ChrTalk(
        0x101,
        (
            "#00008F#12P…… Seems to hear what is difficult\x01",
            "I'm sorry but……\x02\x03",
            "#00001FAbout \"accident\" five years ago\x01",
            "Can you tell me …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01403F#5PAh……\x01",
            "There is no need to hide it anymore.\x02\x03",
            "#01400FFive years ago, I got up at the main street\x01",
            "Truck explosion accident ……\x02\x03",
            "As you are aware,\x01",
            "That is because of the intelligent warfare of the Empire and the Republic\x01",
            "It was what happened as a result.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00106F#12PAs we thought…\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1982")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_185D")
    OP_FC(0xFFF4)
    Jump("loc_1860")

    label("loc_185D")

    OP_FC(0xC)

    label("loc_1860")


    ChrTalk(
        0x10A,
        "#00608F#13PSo then that's when your wife and Shizuku…\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x8,
        (
            "#01402F#5PHuhu, obviously in one department\x01",
            "You ought to have grasped the facts?\x02\x03",
            "#01403FAnd consideration to the Empire and Republicism\x01",
            "In the judgment of the upper part, as a matter of course\x01",
            "It was squashed, but …\x02\x03",
            "#01400FEven though there is disappointment in itself\x01",
            "There is no grudge at the moment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        "#00606F#13P…… There is no word.\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_1982")


    ChrTalk(
        0x103,
        (
            "#00208F#12P…… So Arios' s\x01",
            "My wife and Shizuku … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01403F#5POh …… Saya's life is lost,\x01",
            "The light of Shizuku was robbed.\x02\x03",
            "#01408FFive years from then … …\x01",
            "As the intelligence agencies of both countries were improved\x01",
            "There is no mission destruction work … …\x02\x03",
            "#01401FAs a result of the battle over decades,\x01",
            "Victims like Saya are\x01",
            "Not a little out.\x02\x03",
            "#01403FLloyd - your parents and\x01",
            "Including Mr. Ian's family.\x02",
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
        "#00307F#12PWhat!?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17C, 6)), scpexpr(EXPR_END)), "loc_1CE2")

    ChrTalk(
        0x102,
        (
            "#00101F#12PB, Parents of Lloyd\x01",
            "Surely …! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00208F#12PIn an airship accident 15 years ago ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#12PAh … … as I said before.\x02\x03",
            "#00008FI just got something real\x01",
            "I do not remember most of it … ….\x02\x03",
            "#00013FWell then, then ……\x01",
            "Mr. Ian's family as well?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DFD")

    label("loc_1CE2")


    ChrTalk(
        0x102,
        "#00105F#12PB, Lloyd's parents! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00206F#12PI never heard that\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#12PMy parents ……\x01",
            "Fifteen years ago, I just got in service\x01",
            "He died of an airship accident ……\x02\x03",
            "#00008FI just got something real\x01",
            "I do not remember most of it … ….\x02\x03",
            "#00013FWell then, then ……\x01",
            "Mr. Ian's family as well?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DFD")


    ChrTalk(
        0x8,
        (
            "#01403F#5POh, my wife and my two children\x01",
            "I heard that it was on that.\x02\x03",
            "I was left with Shizuku … …\x01",
            "His mourning and sorrow that lost everything\x01",
            "It will not be imagined.\x02\x03",
            "#01400FAnd then Guy and Ian also\x01",
            "I should have known of the same bereaved family.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F#12P…\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1F70")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1F45")
    OP_FC(0xFFF4)
    Jump("loc_1F48")

    label("loc_1F45")

    OP_FC(0xC)

    label("loc_1F48")


    ChrTalk(
        0x109,
        "#10106F#13P…… That's … such a thing ….\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_1F70")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1FDA")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1F9A")
    OP_FC(0xFFF4)
    Jump("loc_1F9D")

    label("loc_1F9A")

    OP_FC(0xC)

    label("loc_1F9D")


    ChrTalk(
        0x10A,
        (
            "#00606F#13PEven in one lesson\x01",
            "I was not grasping … ….\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_1FDA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2044")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2004")
    OP_FC(0xFFF4)
    Jump("loc_2007")

    label("loc_2004")

    OP_FC(0xC)

    label("loc_2007")


    ChrTalk(
        0x105,
        (
            "#10401F#13P……I see.\x01",
            "It is said that there was such a fate … …\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_2044")


    ChrTalk(
        0x8,
        (
            "#01403F#5P… …. And after the incident five years ago,\x01",
            "I quit the police,\x01",
            "I hit the door of the Association of Association.\x02\x03",
            "Disappointment to the police, the hospitalization expenses of Suzuku,\x01",
            "Although there were various reasons … …\x02\x03",
            "#01408FSimply, from the sorrow that lost Saya\x01",
            "I might just want to escape.\x02\x03",
            "#01400FThere are many if it comes to that\x01",
            "It is to immerse yourself in the work of the hypocrite.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008F#12PArios…\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2200")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_21B0")
    OP_FC(0xFFF4)
    Jump("loc_21B3")

    label("loc_21B0")

    OP_FC(0xC)

    label("loc_21B3")


    ChrTalk(
        0x106,
        (
            "#10706F#13P(… until now \"Silver#2RIn#\"Killed.\x01",
            "Families of targets … …)\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_2200")

    SetScenarioFlags(0x0, 0)
    Jump("loc_2346")

    label("loc_2208")


    ChrTalk(
        0x8,
        (
            "#01403F#5PFive years ago, I got up at the main street\x01",
            "I took Saya's life and Shizuku's light\x01",
            "Truck explosion accident ……\x02\x03",
            "#01401FThat's the Empire and the Republic\x01",
            "It was the result of intelligence fight.\x02\x03",
            "And also the 15-year-old airship accident\x01",
            "I am awake for the same reason.\x02\x03",
            "#01403FAs a result … … Guy and your parents\x01",
            "Ian's family's life was robbed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008F#12P…\x02",
    )

    CloseMessageWindow()

    label("loc_2346")

    Jump("loc_3A1B")

    label("loc_234B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C91")

    ChrTalk(
        0x101,
        (
            "#00006F#12P…… I have always wondered\x01",
            "There was a thing.\x02\x03",
            "#00001FHow come with Dieter\x01",
            "I wonder if your existence is connected.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        "#01405F#5POh…?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#12P…… Indeed the uncle and the bell are\x01",
            "Economy and finance, related to the Clois family\x01",
            "It seems to be detailed to the cult's information, but …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F#12PBehind closed doors from the Empire and the Republic\x02\x03",
            "#00301FTo the circumstances around that\x01",
            "I feel a sense of incongruity that I can communicate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F#12PThere is some common ground\x02\x03",
            "#00201FNevertheless, Mr. Dieter who became president\x01",
            "I nominated Arios as Secretary of Defense ……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2623")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2585")
    OP_FC(0xFFF4)
    Jump("loc_2588")

    label("loc_2585")

    OP_FC(0xC)

    label("loc_2588")


    ChrTalk(
        0x10A,
        (
            "#00606F#13PI see… so that's it\x02\x03",
            "#00601FIt is the one that brought them together\x01",
            "Did I mean Mr. Ian?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00001F#12PYeah ….\x01",
            "─ ─ Does it differ?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2796")

    label("loc_2623")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_26EB")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_264D")
    OP_FC(0xFFF4)
    Jump("loc_2650")

    label("loc_264D")

    OP_FC(0xC)

    label("loc_2650")


    ChrTalk(
        0x105,
        (
            "#10406F#13PI see… so that's it\x02\x03",
            "#10401FIt is the one that brought them together\x01",
            "That translation was that bear beard teacher?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00001F#12PAh……\x01",
            "─ ─ Does it differ?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2796")

    label("loc_26EB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2796")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2715")
    OP_FC(0xFFF4)
    Jump("loc_2718")

    label("loc_2715")

    OP_FC(0xC)

    label("loc_2718")


    ChrTalk(
        0x109,
        (
            "#10108F#13PPossibly …\x02\x03",
            "#10101FIt is the one that brought them together\x01",
            "Mr. Ian … …?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00001F#12PAh……\x01",
            "─ ─ Does it differ?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2796")


    ChrTalk(
        0x8,
        "#01404F#5PHaha, exactly\x02",
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
            "#01402FDuring the police era, like you guys,\x01",
            "I and Guy are also information on Professor Ian\x01",
            "It was saved a lot.\x02\x03",
            "Even in the cult's lodge control strategy\x01",
            "As a private advisor\x01",
            "It is information communication that I cooperated with.\x02\x03",
            "#01403FAnd even after becoming a hypocrite ……\x01",
            "I exchanged information frequently with him.\x02",
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
            "#01403F#5PMeanwhile the teacher, through IBC's legal affairs\x01",
            "I have had friends with Clois father and daughter from long ago.\x02\x03",
            "#01401FAnd all information and elements\x01",
            "It is consolidated and integrated at the teacher … …\x02\x03",
            "Mr. Croix remains guided by him,\x01",
            "Due to various political work and the power of \"treasure\"\x01",
            "Crossbell achieved independence.\x02\x03",
            "#01403FBehind them, by Mr. Mary Bell and Mr.\x01",
            "Without knowing that the real plan is being advanced.\x02",
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
        "#00013F#12PTrue plan?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108F#12PThe Azure Zero Plan… \x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01403F#5PYes … about the accidents of the pears\x01",
            "The teacher was aware of the truth first.\x02\x03",
            "And tell the situation to me ……\x01",
            "I also cooperated with the plan.\x02\x03",
            "#01400FThis is the background#4RProminence#That's all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008F#12PSo then that's when your wife and Shizuku…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#12PAll with Mr. Ian\x01",
            "Maria Bell's palm#2RPalm trees#upon……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00301F#12PThis is an insane story\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2D7A")

    label("loc_2C91")


    ChrTalk(
        0x8,
        (
            "#01403F#5PMr. Croix and I … ….\x01",
            "I joined the two without contacts\x01",
            "I was Mr. Ian, the other teacher.\x02\x03",
            "He also said about the accident five years ago\x01",
            "Be aware of the truth first\x01",
            "I '#2RBlue#Ice#2Rzero#Invite to the plan of … \"\x02\x03",
            "#01400FAnd I also responded to it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D7A")

    Jump("loc_3A1B")

    label("loc_2D7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38B0")

    ChrTalk(
        0x101,
        (
            "#00006F#12P…… Again this,\x01",
            "I was wondering, but …\x02\x03",
            "#00013FFrom the underground of \"Sun Fort\"\x01",
            "It was Arios who took out?\x02\x03",
            "And it is sent to \"Black Auction Society\"\x01",
            "It was also replaced with the Rosenberg doll.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105F#12PY-yeah, that's right\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#12PCertainly that problem is completely\x01",
            "It is not clear.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01404F#5PYes, that's right\x02\x03",
            "#01402FIn that regard is not a teacher,\x01",
            "He was led by Mr. Mariavell.\x02",
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
            "#01403FApparently she said Joachim's move\x01",
            "It seems that you have perfectly grasped … …\x02\x03",
            "#01401FWe make it easy for her transposition\x01",
            "I arrive at the altar of the bottom layer,\x01",
            "Creatures that child#4RCradle#Liberated from.\x02",
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
            "#01403FAnd then, from the direction towards Remiferia\x01",
            "With the Rosenberg doll carried\x01",
            "I replaced her.\x02\x03",
            "#01400FThat Rosenberg doll itself is also\x01",
            "Not to be noticed by the Rubatie side\x01",
            "It is what Miss Mary Bell prepared.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, -1, 3)

    AnonymousTalk(
        0x102,
        "#00106FEven to that level…\x02",
    )

    CloseMessageWindow()
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x1, 0xFF, 0x0)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00006F#12PHowever……\x01",
            "Doing something like that to Mr. Mary Bell\x01",
            "What meaning did you have?\x02\x03",
            "#00013FIf you need a keyer in the plan\x01",
            "I wish I had protected ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01403F#5POne is \"black moon#4RHayuue#\"Also involved\x01",
            "I lost face on Rubatie's side,\x01",
            "To be the first step of self-destruction … …\x02\x03",
            "#01400FIf at an auction house\x01",
            "If she wakes up\x01",
            "Miss Maria Bell should have moved.\x02\x03",
            "Upsetting customers and Marconi in front\x01",
            "Give the name of IBC to protect that child\x01",
            "I guess it was meant to buy it.\x02\x03",
            "#01404FIf \"black moon\" moves\x01",
            "I guess there was another development … …\x02\x03",
            "Either way, at that time\x01",
            "This I was also latent in the hall#28R噵 噵 噵 噵 噵 噵 噵 噵 噵 噵 噵 噵 噵 噵#.\x02\x03",
            "#01402FNo matter what kind of deployment\x01",
            "The system was ready to be settled.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#12PWhat is it?\x01",
            "It's Ultra C too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00211F#12PIt's hard to imagine all of that…\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3540")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_34E2")
    OP_FC(0xFFF4)
    Jump("loc_34E5")

    label("loc_34E2")

    OP_FC(0xC)

    label("loc_34E5")


    ChrTalk(
        0x106,
        (
            "#10708F#13P…… Indeed, at that time,\x01",
            "It seems like some other people are still lurking\x01",
            "I felt a sign … ….\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3540")


    ChrTalk(
        0x8,
        (
            "#01403F#5PThere was one other thing\x02\x03",
            "#01401FIn such a unique situation\x01",
            "By awaking \"treasure\"\x01",
            "It is to figure out the potential ability.\x02",
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
        "#00205F#12PSee through to KeA's latent power?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00101F#12PW-what do you mean\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01403F#5PWell - __ - Mr. Mariavell\x01",
            "It is only saying that.\x02\x03",
            "#01408FProbably, I had to sleep that boy for a long time\x01",
            "It may be one of the conditions to wake me up.\x01",
            "Maybe …\x02\x03",
            "#01400FIn any case, the guidance of the goddess,\x01",
            "Or is it just a coincidence?\x01",
            "She awoke in front of you.\x02\x03",
            "If you make Mary Bell\x01",
            "It should have been completely unexpected … …\x02\x03",
            "#01403FThat girl was taken over by you,\x01",
            "Including including having to live together\x01",
            "It was as if welcoming.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008F#12PSo then that's when your wife and Shizuku…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#12P… … It is useless.\x01",
            "I do not understand Wake …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#12P…… Bell ……\x01",
            "What on earth are you … ….?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3A0E")

    label("loc_38B0")


    ChrTalk(
        0x8,
        (
            "#01403F#5PRelease Keya from the \"Fort of the Sun\"\x01",
            "I brought it to the auction house\x01",
            "It is led by Ms. Mariavell.\x02\x03",
            "#01408FIts aim is to lead the Rubache to the collapse,\x01",
            "Even for controlling the situation\x01",
            "It seems there was … …\x02\x03",
            "#01401FMake her awake in a unique situation,\x01",
            "The purpose of identifying the potential ability is also\x01",
            "It seems there was one.\x02\x03",
            "#01403FMore than that\x01",
            "Unfortunately I do not know.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A0E")

    Jump("loc_3A1B")

    label("loc_3A13")

    SetScenarioFlags(0x0, 3)
    Jump("loc_3A1B")

    label("loc_3A1B")

    Jump("loc_15EA")

    label("loc_3A20")

    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00006F#12P#30WOK then…\x02\x03",
            "#00008FThe thing about the day my brother passed away …\x01",
            "… … Can you tell me the truth?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3AEE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3ACD")
    OP_FC(0xFFF4)
    Jump("loc_3AD0")

    label("loc_3ACD")

    OP_FC(0xC)

    label("loc_3AD0")


    ChrTalk(
        0x10A,
        "#00601F#13P…… Well ………\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_3AEE")


    ChrTalk(
        0x103,
        "#00208F#12PAh….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#01403F#5P#30WSo then that's when your wife and Shizuku…\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x8)

    ChrTalk(
        0x8,
        "#01400F#5P#30WVery well\x02",
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
            "#3C#30W… … losing Saya\x01",
            "Two years since I left the police ……\x02\x03",
            "I cooperated with Ian's plan,\x01",
            "He had accomplished several works … …\x02\x03",
            "Both are dark behind …\x01",
            "It is just a conspiracy work.\x02\x03",
            "But, including guild officials,\x01",
            "It is not possible for someone to feel it\x01",
            "It was not finally.\x02\x03",
            "Guy · Bannings …\x01",
            "Except my former partner.\x02",
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
            "#3C#30WGuy is … … That guy\x01",
            "With a tremendous sense of smell and tenacity\x01",
            "I was close to various conspiracy and secrets.\x02\x03",
            "The secret feud between the Empire and the Republic\x02\x03",
            "Mr. Hartmann and Rubache,\x01",
            "And the movement of the remnants of the D∴ G group ……\x02\x03",
            "Beyond that,\x01",
            "To the plan of the Clois family ……\x02\x03",
            "And then-\x02\x03",
            "On that rainy day, Guy made me\x01",
            "The newly constructed Orkis Tower\x01",
            "Called to the construction site ……\x02",
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
            "#3C#30WOf course, until the details of the plan\x01",
            "I did not grab it … …\x02\x03",
            "Guy's guess is surprisingly precise\x01",
            "It captured the whole picture of the plan.\x02\x03",
            "I used a cult and mafia\x01",
            "Mr. Crois advances into the political world … …\x02\x03",
            "Mimicking the work of foreign forces\x01",
            "By causing Crossbell City to attack\x01",
            "Feeding independence mind …\x02\x03",
            "Furthermore, in the \"something\" of the Clois family\x01",
            "To intimidate and lead the whole continent … …\x02\x03",
            "Unbelievably\x01",
            "I could point out such a thing.\x02\x03",
            "And then-\x02",
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
            "#3C#30W…… It's called hand-pulling.\x01",
            "Guy will not accept my words ……\x02\x03",
            "And we began a fight to the death in the rain\x02\x03",
            "My martial arts arm is slightly above me ……\x01",
            "But it's unwavering to Guy\x01",
            "Power by the will was full.\x02\x03",
            "I met with dozens,\x01",
            "While struggling with each other's physical strength\x01",
            "Suicide battle in the rain continues ……\x02\x03",
            "And then-\x02",
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
            "#3C#30WAnd Guy ……\x01",
            "I decided to lose my life.\x02\x03",
            "Of course, his daughter\x01",
            "It is me who took away from the scene.\x02\x03",
            "From sword innumerable carvings on toffers\x01",
            "Because he did not want to identify the criminal.\x07\x00\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4514")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_44BD")
    OP_FC(0xFFF4)
    Jump("loc_44C0")

    label("loc_44BD")

    OP_FC(0xC)

    label("loc_44C0")


    ChrTalk(
        0x109,
        "#10106F#13P#30WSuch a thing ……\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x103,
        "#00208F#12P#30W….\x02",
    )

    CloseMessageWindow()
    Jump("loc_456A")

    label("loc_4514")


    ChrTalk(
        0x101,
        "#00008F#12P#30W….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00206F#12P#30WThat's what…\x02",
    )

    CloseMessageWindow()

    label("loc_456A")

    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x8)
    Sleep(500)

    ChrTalk(
        0x8,
        (
            "#01403F#5P#30W…… This is that rainy day,\x01",
            "It is an overview of what happened.\x02\x03",
            "#01408FAfter that, the mafia subordinate appeared,\x01",
            "Having brought Guy's badge\x01",
            "As expected it was unexpected … …\x02\x03",
            "#01400FEither way, this is almost the case\x01",
            "I could have answered the question.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003F#12PNo….\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        "#01405F#5PSo then that's when your wife and Shizuku…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#12POf course you probably know,\x01",
            "The cause of death of my brother is shooting#4R噵 噵#It is due to.\x02\x03",
            "#00001FAn explanation about that\x01",
            "It looks like it was not … ….?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01403F#5P… when I was in the police\x01",
            "Handling of handguns is acquired.\x02\x03",
            "#01401FI crawl steadily and come down\x01",
            "Boil the business to a troublesome partner\x01",
            "Even though I used it … ….?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_48B0")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_480D")
    OP_FC(0xFFF4)
    Jump("loc_4810")

    label("loc_480D")

    OP_FC(0xC)

    label("loc_4810")


    ChrTalk(
        0x10A,
        (
            "#00606F#13PIt's a lie - McLaughn.\x02\x03",
            "#00601FIn such a death battle\x01",
            "We can afford another gift etc.\x01",
            "Is it something?\x02\x03",
            "Not much from the other's back\x01",
            "It is impossible to stab a stop.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4956")

    label("loc_48B0")


    ChrTalk(
        0x101,
        (
            "#00013F#12PThat's a lie.\x02\x03",
            "#00006FIn such a death battle\x01",
            "We can afford another gift etc.\x01",
            "There will not be a certain translation.\x02\x03",
            "#00001FNot much from the other's back\x01",
            "It is impossible to stab a stop.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4956")

    StopBGM(0xFA0)

    ChrTalk(
        0x8,
        "#01401F#5PSo then that's when your wife and Shizuku…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00303F#12PWell, the truth\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#12PEveryone \"who\"\x01",
            "Did you shoot Guy ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00201F#12PPlease tell us who\x02",
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
            "#01403F#5P#30WWhatever may be said\x01",
            "It was that I forced Guy to die\x01",
            "It is nothing except me.\x02\x03",
            "#01400FAnd I …\x01",
            "Until at the expense of former buddies\x01",
            "I chose the road to cooperate with the plan.\x02\x03",
            "And still ….\x01",
            "Using the feeling of a girl who is dubious\x01",
            "I am about to complete the plan.\x02\x03",
            "#01403FEverything is for Saya ……\x01",
            "And for the future of Shizuku.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F#12PArios…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#12PShizuoka is doing this\x01",
            "Even if you rejoice ……?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01403F#5P#30WOf course she is not\x02\x03",
            "#01401FBut\x01",
            "The curse of the place called Cross Bell\x01",
            "He robbed my mother and light from that girl.\x02\x03",
            "And the crossbell\x01",
            "Beyond this position on the continent,\x01",
            "The curse never goes out.\x02\x03",
            "#01403F── It transcended the logic of human beings\x01",
            "As long as it does not happen even in \"miracle\".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#12P!?\x02",
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
            "#01400F#5P#30WThree years ago Guy … …\x01",
            "I did not blame you for a single word,\x01",
            "I lost my life at the end of the death battle.\x02\x03",
            "And she became \"treasure\"#4RKeya#Is\x01",
            "He cured the eye of Suzuku.\x02\x03",
            "#01403FNo longer ──\x01",
            "There is no reason to be able to go back.\x02",
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
            "#01403F#5P#30W…… If you can not accept yourself\x01",
            "Try stopping with power.\x02\x03",
            "#01401FMy brother's remains#2RHere#With that tofu you did ……\x02\x03",
            "#01407FBrilliantly, hurting his brother's enemy\x01",
            "A way to regain important things\x01",
            "Shoot it up, let's see … …!\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xBB8)

    ChrTalk(
        0x101,
        (
            "#00006F#12PUnderstood…\x02\x03",
            "#00001FBut ─ ─ brother's enemy\x01",
            "I do not have hair as I intend to take it.\x02",
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
            "#00003F#12PGuy Bannings'\x01",
            "It was launched with the will\x01",
            "As a small department ……\x02\x03",
            "#00001FStarting with Shizuku,\x01",
            "I was committed to the thought of many people\x01",
            "As a \"Special Affairs Support Division\" ……\x02\x03",
            "#00007FOvercoming the \"wall\" you say,\x01",
            "Take back Ka'a … …\x01",
            "I will settle the case in the real sense!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x8,
        "#01405F#5P…!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302F#12PHa ha …\x01",
            "Truly our leader!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101F#12PI'm waiting at the Orkis Tower\x01",
            "Even for Shizuoka … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00201F#12P… … absolutely withdraw#2RFacial#I can not do it!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_52A2")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5270")
    OP_FC(0xFFF4)
    Jump("loc_5273")

    label("loc_5270")

    OP_FC(0xC)

    label("loc_5273")


    ChrTalk(
        0x10A,
        (
            "#00604F#13PHydrofluoric acid\x01",
            "It is a useless guy.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_52A2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5302")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_52CC")
    OP_FC(0xFFF4)
    Jump("loc_52CF")

    label("loc_52CC")

    OP_FC(0xC)

    label("loc_52CF")


    ChrTalk(
        0x105,
        (
            "#10402F#13PGiggle\x01",
            "This nori is the support department.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_5302")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5353")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_532C")
    OP_FC(0xFFF4)
    Jump("loc_532F")

    label("loc_532C")

    OP_FC(0xC)

    label("loc_532F")


    ChrTalk(
        0x109,
        "#10107F#13PI will cooperate fully!\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_5353")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_53E1")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_537D")
    OP_FC(0xFFF4)
    Jump("loc_5380")

    label("loc_537D")

    OP_FC(0xC)

    label("loc_5380")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_53B9")

    ChrTalk(
        0x106,
        "#10701F#13PI, too … … as long as I can!\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_53E1")

    label("loc_53B9")


    ChrTalk(
        0x106,
        "#10707F#13PI'll help you with all my strength!\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_53E1")

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
        "#01404F#4077V#5P#30W#25AHaha, good\x02",
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
            "#4065V#40W#55AHachiba Tadasu style, type of dai Mysterious Shinsengumi,\x01",
            "Arios McRae …\x02\x03",
            "#4066V#60ADepending on personal circumstances, to turn righteousness,\x01",
            "Get out of the way, let your selfishness go!\x02\x03",
            "#4067V#30ACome, SSS\x02",
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
    SetChrName("Lloyd's")
    OP_82(0xC8, 0x0, 0xBB8, 0x1F4)

    AnonymousTalk(
        0xFF,
        "#4S#12ARight!\x02",
    )

    Sound(2153, 255, 90, 0)
    Sound(2343, 255, 100, 1)
    Sound(2249, 255, 100, 2)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_568B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5682")
    OP_FC(0x4)
    Sound(2478, 255, 100, 4)
    Jump("loc_568B")

    label("loc_5682")

    OP_FC(0x3)
    Sound(2478, 255, 100, 3)

    label("loc_568B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_56BE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_56B8")
    Sound(2417, 255, 100, 4)
    Jump("loc_56BE")

    label("loc_56B8")

    Sound(2417, 255, 100, 3)

    label("loc_56BE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_56F1")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_56EB")
    Sound(2544, 255, 100, 4)
    Jump("loc_56F1")

    label("loc_56EB")

    Sound(2544, 255, 100, 3)

    label("loc_56F1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5724")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_571E")
    Sound(3174, 255, 100, 4)
    Jump("loc_5724")

    label("loc_571E")

    Sound(3174, 255, 100, 3)

    label("loc_5724")

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

    # Function_9_D37 end

    def Function_10_575F(): pass

    label("Function_10_575F")

    OP_9B(0x0, 0xFE, 0x0, 0x1770, 0xFA0, 0x1)
    OP_96(0xFE, 0x0, 0x2EE0, 0x318BC, 0xFA0, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_10_575F end

    def Function_11_578A(): pass

    label("Function_11_578A")

    OP_9B(0x0, 0xFE, 0x0, 0x157C, 0xFA0, 0x1)
    OP_96(0xFE, 0x460, 0x2EE0, 0x313E4, 0xFA0, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_11_578A end

    def Function_12_57B5(): pass

    label("Function_12_57B5")

    OP_9B(0x0, 0xFE, 0x0, 0x157C, 0xFA0, 0x1)
    OP_96(0xFE, 0x1A4, 0x2EE0, 0x30EB2, 0xFA0, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_12_57B5 end

    def Function_13_57E0(): pass

    label("Function_13_57E0")

    OP_9B(0x0, 0xFE, 0x0, 0x157C, 0xFA0, 0x1)
    OP_96(0xFE, 0xFFFFFB0A, 0x2EE0, 0x3116E, 0xFA0, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_13_57E0 end

    def Function_14_580B(): pass

    label("Function_14_580B")

    OP_9B(0x0, 0xFE, 0x0, 0x1996, 0xFA0, 0x1)
    OP_96(0xFE, 0xFFFFF614, 0x2EE0, 0x313DA, 0xFA0, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_14_580B end

    def Function_15_5836(): pass

    label("Function_15_5836")

    OP_9B(0x0, 0xFE, 0x0, 0x1AC2, 0xFA0, 0x1)
    OP_96(0xFE, 0x9EC, 0x2EE0, 0x31312, 0xFA0, 0x0)
    Return()

    # Function_15_5836 end

    def Function_16_585A(): pass

    label("Function_16_585A")

    Sleep(150)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_16_585A end

    def Function_17_586C(): pass

    label("Function_17_586C")

    Sleep(300)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_17_586C end

    def Function_18_587E(): pass

    label("Function_18_587E")

    Sleep(450)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_18_587E end

    def Function_19_5890(): pass

    label("Function_19_5890")

    Sleep(450)
    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_19_5890 end

    def Function_20_589C(): pass

    label("Function_20_589C")

    Sleep(600)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_58BC")
    Sound(540, 0, 50, 0)
    Jump("loc_58E1")

    label("loc_58BC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_58E1")
    Sound(531, 0, 100, 0)

    label("loc_58E1")

    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_20_589C end

    def Function_21_58EA(): pass

    label("Function_21_58EA")

    Sleep(750)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_590A")
    Sound(540, 0, 50, 0)
    Jump("loc_592F")

    label("loc_590A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_592F")
    Sound(531, 0, 100, 0)

    label("loc_592F")

    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_21_58EA end

    def Function_22_5938(): pass

    label("Function_22_5938")

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

    # Function_22_5938 end

    def Function_23_5961(): pass

    label("Function_23_5961")

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

    # Function_23_5961 end

    def Function_24_59AB(): pass

    label("Function_24_59AB")

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

    # Function_24_59AB end

    def Function_25_59D8(): pass

    label("Function_25_59D8")

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

    # Function_25_59D8 end

    def Function_26_5A04(): pass

    label("Function_26_5A04")

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

    # Function_26_5A04 end

    def Function_27_5A27(): pass

    label("Function_27_5A27")

    PlayEffect(0x0, 0x5, 0xFE, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    StopEffect(0x5, 0x2)
    Return()

    # Function_27_5A27 end

    def Function_28_5A70(): pass

    label("Function_28_5A70")

    PlayEffect(0x0, 0x6, 0xFE, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    StopEffect(0x6, 0x2)
    Return()

    # Function_28_5A70 end

    def Function_29_5AB9(): pass

    label("Function_29_5AB9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5AD4")
    OP_A1(0xFE, 0x4B0, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_29_5AB9")

    label("loc_5AD4")

    Return()

    # Function_29_5AB9 end

    def Function_30_5AD5(): pass

    label("Function_30_5AD5")

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

    # Function_30_5AD5 end

    def Function_31_5B49(): pass

    label("Function_31_5B49")

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
            "#01404F#4078V#5P#80W#30AHaha\x02\x03",
            "#4079V#45ALloyd … … others also …\x01",
            "…… It really got stronger.\x02",
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
            "#00006F#12P#40WHaaa Haa\x02\x03",
            "#00008FIf so … … Arios\x01",
            "It is because it became a goal ……\x02",
        )
    )

    OP_6F(0x79)
    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#12P#40WSurely … if you do not have any\x01",
            "I guess he could not go so far …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00206F#12P#40WAgreed…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#12P#40WAs always \"a wall\" to aim for\x01",
            "Because it stayed far away … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01402F#5P#40WAhaha, seriously\x02\x03",
            "#01404FCertification etc. to be said as such\x01",
            "Even though it is not in the first place ……\x02",
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
            "#00003F#12P#30WArios…\x02\x03",
            "#00001FThat day, I shot my brother\x01",
            "Ian is a teacher, is not it?\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_60AC")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6088")
    OP_FC(0xFFF4)
    Jump("loc_608B")

    label("loc_6088")

    OP_FC(0xC)

    label("loc_608B")


    ChrTalk(
        0x10A,
        "#00605F#13P#30W…!\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_60FB")

    label("loc_60AC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_60FB")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_60D6")
    OP_FC(0xFFF4)
    Jump("loc_60D9")

    label("loc_60D6")

    OP_FC(0xC)

    label("loc_60D9")


    ChrTalk(
        0x109,
        "#10105F#13P#30W…… Ah …!\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_60FB")


    ChrTalk(
        0x104,
        "#00301F#12P#30WThat is…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01403F#5P#40WSo then that's when your wife and Shizuku…\x02\x03",
            "#01400FWhy do you think that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#12P#30WJust my intuition\x02\x03",
            "#00008F…… Given the background of the incident ……\x01",
            "If there are suspects other than the teacher\x01",
            "Mr. Dieter or Mary Bell …\x02\x03",
            "#00001FHowever, to Dieter\x01",
            "Everything about the plan seems to have been told,\x01",
            "Maria Bell also has no point of contact with his brother … …\x02\x03",
            "#00006FBut … Ian is a\x01",
            "I seemed pretty close to my brother … …\x02\x03",
            "And … … many business trips abroad,\x01",
            "As a teacher who needs self-defense\x01",
            "It is not amusing to be accustomed to a handgun …\x02\x03",
            "#00013FSo then?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01403F#5P#40WYou get 60 points\x02\x03",
            "#01402FBut …\x01",
            "It seems I can not help attaching ……\x02",
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
    SetChrName("A guy")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x14),
            "#40WHaa Haa\x02\x03",
            "Hey Arios…\x02\x03",
            "It seems like each other's limits ……\x01",
            "Do not you decide to celebrate today?\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(230, 140, -1, -1)
    SetChrName("Arios")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x14),
            "#40W… What stupidity\x02\x03",
            "Since you were known, you from here\x01",
            "It can not be attributed ……\x02\x03",
            "I want to have the ceremony of next month safely\x01",
            "Come with me with killing … good!\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(20, 160, -1, -1)
    SetChrName("A guy")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x14),
            "#40WThere's no way I can \x02\x03",
            "Then you and Shizuku-chan\x01",
            "I guess we can call it an expression … ….?\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(330, 140, -1, -1)
    SetChrName("Arios")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x14),
            "…!\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(20, 160, -1, -1)
    SetChrName("A guy")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x14),
            "#40WDo not worry … your plan is\x01",
            "I do not talk to anyone …\x02\x03",
            "Per Dudley\x01",
            "I thought I might cooperate … …\x01",
            "You can not adapt himself well.\x02\x03",
            "Sergei's even\x01",
            "I have not consulted yet … ….?\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(250, 140, -1, -1)
    SetChrName("Arios")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x14),
            "#40WYou…\x02\x03",
            "…… Listen to it\x01",
            "To judge it as convenient\x01",
            "Do not you think …?\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(20, 160, -1, -1)
    SetChrName("A guy")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x14),
            "#30WDisagreeable……?\x01",
            "Because you are clumsy.\x02\x03",
            "If not, this is where\x01",
            "You can not come by alone.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(330, 140, -1, -1)
    SetChrName("Arios")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x14),
            "#30WUgh…\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(20, 160, -1, -1)
    SetChrName("A guy")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x14),
            "#30WAnyway … in the vicinity of this\x01",
            "Let 's go for a drink now.\x02\x03",
            "Even if it is not the last two years,\x01",
            "I could not talk to Roku ….\x02\x03",
            "About my brother and her boastful talk,\x01",
            "Let's do it.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(240, 150, -1, -1)
    SetChrName("Arios")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x14),
            "#30WHah, same as always\x02\x03",
            "My brother is certain … ….\x01",
            "Was it already 15?\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(20, 160, -1, -1)
    SetChrName("A guy")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x14),
            "#30WYeah.. He's quite a genius, unlike me\x02\x03",
            "About somewhere high school\x01",
            "I'd like to let you go ……\x02\x03",
            "……whatever.\x01",
            "It's raining and even \"Galante\" - ─\x02",
        )
    )

    CloseMessageWindow()
    Sound(567, 0, 100, 0)
    Sleep(200)
    OP_CB(0x1, 0x4, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    Sleep(500)
    SetMessageWindowPos(80, 160, -1, -1)
    SetChrName("A guy")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x14),
            "#60WAh--\x02",
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
            "#30WSensei!?\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(250, 180, -1, -1)
    SetChrName("A guy")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x14),
            "#50WHaha….\x02\x03",
            "……I see……\x01",
            "Was the black curtain anta …?\x02",
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
    SetChrName("Ian lawyer")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x14),
            "#30WI apologize, Guy\x02\x03",
            "After considering your parents\x01",
            "I thought you should invite me … …\x02\x03",
            "Perhaps you are absolute#4R噵 噵#We must agree with\x01",
            "I was convinced.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(350, 140, -1, -1)
    SetChrName("Arios")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x14),
            "#30WSensei…\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(200, 200, -1, -1)
    SetChrName("A guy")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x14),
            "#50WHaha… of course not\x02\x03",
            "…… If your teacher is on\x01",
            "Probably … that plan is also\x01",
            "I will carry it well ……\x02\x03",
            "But … … surely ……\x01",
            "I will appear instead of me … ….?\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(40, 160, -1, -1)
    SetChrName("Ian lawyer")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x14),
            "#30WYes… Of course\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(350, 140, -1, -1)
    SetChrName("Arios")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x14),
            "#30WGuy …!\x01",
            "……come on……!\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(210, 200, -1, -1)
    SetChrName("A guy")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x14),
            "#60WGeorge: … Ah … ….\x01",
            "… …. I should have … …\x02\x03",
            "#80WIf such a thing ……\x01",
            "Lloyd and … … to Cecil ……\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6FC3")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6F94")
    OP_FC(0xFFF4)
    Jump("loc_6F97")

    label("loc_6F94")

    OP_FC(0xC)

    label("loc_6F97")


    ChrTalk(
        0x10A,
        "#00608F#13P#30W….\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_6FC3")


    ChrTalk(
        0x103,
        "#00213F#12P#30WGuy…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108F#12P#30WSo that's what…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00308F#12P#30WCause and effect…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#12P#30W……Thank you.\x01",
            "Tell me the end of my brother.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01404F#5P#40WDon't thank me\x02\x03",
            "#01400FMr. Ian is … …\x01",
            "Perhaps, it will not be shaken …\x02\x03",
            "And …\x01",
            "Kaoru's determination seems to be hard …\x02\x03",
            "#01404F#50WWhether we can break two people ……\x01",
            "Try bumping all of you … …\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    Sound(898, 0, 100, 0)

    def lambda_714F():
        OP_A6(0xFE, 0x0, 0x23, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_714F)
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

    # Function_31_5B49 end

    def Function_32_76AE(): pass

    label("Function_32_76AE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_76F6")
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
    Jump("Function_32_76AE")

    label("loc_76F6")

    Return()

    # Function_32_76AE end

    def Function_33_76F7(): pass

    label("Function_33_76F7")

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

    # Function_33_76F7 end

    def Function_34_7761(): pass

    label("Function_34_7761")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7A62")

    ChrTalk(
        0x102,
        "#00108F#12PLloyd …\x02",
    )

    CloseMessageWindow()
    Jump("loc_7B5E")

    label("loc_7A62")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7A99")

    ChrTalk(
        0x103,
        "#00208F#12PLloyd…\x02",
    )

    CloseMessageWindow()
    Jump("loc_7B5E")

    label("loc_7A99")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7AC8")

    ChrTalk(
        0x104,
        "#00308F#12PLloyd …\x02",
    )

    CloseMessageWindow()
    Jump("loc_7B5E")

    label("loc_7AC8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7AFB")

    ChrTalk(
        0x105,
        "#10408F#12P…… Lloyd ……\x02",
    )

    CloseMessageWindow()
    Jump("loc_7B5E")

    label("loc_7AFB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7B2E")

    ChrTalk(
        0x109,
        "#10108F#12PMr. Lloyd ……\x02",
    )

    CloseMessageWindow()
    Jump("loc_7B5E")

    label("loc_7B2E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7B5E")

    ChrTalk(
        0x106,
        "#10708F#12P…… Lloyd.\x02",
    )

    CloseMessageWindow()

    label("loc_7B5E")


    ChrTalk(
        0x101,
        (
            "#00004F#11P#30WHaha\x02\x03",
            "#00008F…… Finally finished ……\x01",
            "I feel I delivered it to my brother.\x02\x03",
            "#00002FThank you……\x01",
            "I owe it to everyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00304F#12PHaha\x01",
            "What are you talking about?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00204F#12P…… Lloyd's will\x01",
            "I call Arios \"wall\"\x01",
            "I think that it broke down.\x02\x03",
            "#00208FAnd the death of Guy\x01",
            "I hit the light of the past … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104F#12PYeah …. We\x01",
            "I just helped with it.\x02\x03",
            "#00108FI can not help out next time\x01",
            "I can not say that … but …\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7D50")

    ChrTalk(
        0x106,
        "#10703F#12PThat's right\x02",
    )

    CloseMessageWindow()
    Jump("loc_7DB7")

    label("loc_7D50")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7D88")

    ChrTalk(
        0x109,
        "#10106F#12PThat's right\x02",
    )

    CloseMessageWindow()
    Jump("loc_7DB7")

    label("loc_7D88")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7DB7")

    ChrTalk(
        0x105,
        "#10406F#12P……Yeah.\x02",
    )

    CloseMessageWindow()

    label("loc_7DB7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7E0B")

    ChrTalk(
        0x104,
        (
            "#00308F#12PDr. Ian to Mr. Bell,\x01",
            "Besides, it's a key …\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_7EB8")

    label("loc_7E0B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7E5E")

    ChrTalk(
        0x105,
        (
            "#10408F#12PMr. Bear Beard to Mr. Mary Bell,\x01",
            "And Kaoru … …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7EB8")

    label("loc_7E5E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7EB8")

    ChrTalk(
        0x109,
        (
            "#10108F#12PMr. Ian, Mr. Maria Bell,\x01",
            "And Ka'a-chan ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7EB8")


    ChrTalk(
        0x101,
        "#00006F#11P#30WYeah…\x02",
    )

    CloseMessageWindow()
    OP_68(350, 12800, 208640, 1000)
    MoveCamera(37, 17, 0, 1000)

    def lambda_7EFA():
        OP_93(0xFE, 0xB4, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7EFA)
    Sleep(300)

    def lambda_7F0A():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_7F0A)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#00003F#5PWe cleared the Final Territory\x02\x03",
            "#00000FTentatively …\x01",
            "Let's go back to the end of the \"shinto area\".\x02",
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

    # Function_34_7761 end

    def Function_35_7FDC(): pass

    label("Function_35_7FDC")

    OP_9B(0x0, 0xFE, 0x162, 0x320, 0x3E8, 0x0)
    Return()

    # Function_35_7FDC end

    def Function_36_7FEC(): pass

    label("Function_36_7FEC")

    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_36_7FEC end

    def Function_37_7FFB(): pass

    label("Function_37_7FFB")

    Sleep(200)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_37_7FFB end

    def Function_38_800D(): pass

    label("Function_38_800D")

    Sleep(300)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_38_800D end

    def Function_39_801F(): pass

    label("Function_39_801F")

    Sleep(100)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_39_801F end

    def Function_40_802B(): pass

    label("Function_40_802B")

    Sleep(400)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_804B")
    Sound(540, 0, 50, 0)
    Jump("loc_8070")

    label("loc_804B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8070")
    Sound(531, 0, 100, 0)

    label("loc_8070")

    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_40_802B end

    def Function_41_8079(): pass

    label("Function_41_8079")

    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8099")
    Sound(540, 0, 50, 0)
    Jump("loc_80BE")

    label("loc_8099")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_80BE")
    Sound(531, 0, 100, 0)

    label("loc_80BE")

    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_41_8079 end

    def Function_42_80C7(): pass

    label("Function_42_80C7")

    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x10)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x800)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x2)
    SetChrFlags(0x8, 0x1000)
    SetChrFlags(0x8, 0x800)
    Return()

    # Function_42_80C7 end

    def Function_43_80EE(): pass

    label("Function_43_80EE")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 1)), scpexpr(EXPR_END)), "loc_8110")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8279")

    label("loc_8110")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 2)), scpexpr(EXPR_END)), "loc_8128")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8279")

    label("loc_8128")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 3)), scpexpr(EXPR_END)), "loc_8140")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8279")

    label("loc_8140")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 4)), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8163")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8279")

    label("loc_8163")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 5)), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8186")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8279")

    label("loc_8186")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 6)), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_81A9")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8279")

    label("loc_81A9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_DC(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_81C7")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8279")

    label("loc_81C7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_DC(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_81E5")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8279")

    label("loc_81E5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_DC(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8203")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8279")

    label("loc_8203")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_DC(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_822C")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8279")

    label("loc_822C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_DC(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8255")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8279")

    label("loc_8255")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_DC(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8279")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8279")

    Return()

    # Function_43_80EE end

    SaveToFile()

Try(main)
