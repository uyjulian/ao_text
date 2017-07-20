from ScenarioHelper import *

def main():
    CreateScenaFile(
        "m9052.bin",                # FileName
        "m9052",                    # MapName
        "m9052",                    # Location
        0x00C0,                     # MapIndex
        "ed7351",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x2A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 192, 0, 0, 0, 1],
    )

    BuildStringList((
        "m9052",                  # 0
        "Charlie",             # 1
        "Dummy characters for speech display", # 2
        "Attendant Shirley",         # 3
        "Attendant Shirley",         # 4
        "bm9039",                 # 5
    ))

    ATBonus("ATBonus_1BC", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_27C", 8, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_280", 3, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_284", 13, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_288", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_28C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_290", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_294", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_298", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_25C", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_260", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_264", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_268", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_26C", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_270", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_274", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_278", 5, 5, 45)

    # monster count: 0

    # event battle count: 1

    BattleInfo(
        "BattleInfo_29C", 0x0042, 255, 6, 45, 3, 3, 30, 0, "bm9039", 0x00000000, 100, 0, 0, 0,
        (
            ("ms03401.dat", "ms81000.dat", "ms81000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_27C", "MonsterBattlePostion_25C", "ed7540", "ed7453", "ATBonus_1BC"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "apl/ch51739.itc",                   # 00
    ))

    DeclNpc(0,       35000,   26500,   180,  389,  0x0, 0,   1,   0,   255, 255, 0,   2,   255,  0)
    DeclNpc(0,       0,       0,       0,    508,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 8,   0.0,                   7.0,                   34.0,                  156.25,                [0.20000000298023224,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.0,                  -1.399999976158142,    -6.800000190734863,    1.0])

    DeclActor(5000,    33000,   4294960796, 1200,    5000,    34000,   4294960796, 0x007C, 0,  3,  0x0000)

    ChipFrameInfo(892, 0)                                        # 0

    ScpFunction((
        "Function_0_37C",          # 00, 0
        "Function_1_3B7",          # 01, 1
        "Function_2_59E",          # 02, 2
        "Function_3_8E3",          # 03, 3
        "Function_4_9DF",          # 04, 4
        "Function_5_C5F",          # 05, 5
        "Function_6_DB2",          # 06, 6
        "Function_7_DF3",          # 07, 7
        "Function_8_E30",          # 08, 8
        "Function_9_2B14",         # 09, 9
        "Function_10_2B3F",        # 0A, 10
        "Function_11_2B6A",        # 0B, 11
        "Function_12_2B95",        # 0C, 12
        "Function_13_2BC0",        # 0D, 13
        "Function_14_2BEB",        # 0E, 14
        "Function_15_2C16",        # 0F, 15
        "Function_16_2C28",        # 10, 16
        "Function_17_2C3A",        # 11, 17
        "Function_18_2C46",        # 12, 18
        "Function_19_2C58",        # 13, 19
        "Function_20_2C89",        # 14, 20
        "Function_21_2CD2",        # 15, 21
        "Function_22_2D1B",        # 16, 22
        "Function_23_2D3A",        # 17, 23
        "Function_24_2D5B",        # 18, 24
        "Function_25_36BF",        # 19, 25
        "Function_26_36E6",        # 1A, 26
        "Function_27_36FB",        # 1B, 27
        "Function_28_3EAA",        # 1C, 28
        "Function_29_3EBC",        # 1D, 29
        "Function_30_3ECE",        # 1E, 30
        "Function_31_3EE0",        # 1F, 31
        "Function_32_3EEC",        # 20, 32
        "Function_33_3F37",        # 21, 33
        "Function_34_3F85",        # 22, 34
        "Function_35_439F",        # 23, 35
        "Function_36_43FC",        # 24, 36
        "Function_37_441D",        # 25, 37
        "Function_38_4438",        # 26, 38
    ))


    def Function_0_37C(): pass

    label("Function_0_37C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_38D")
    Event(0, 4)

    label("loc_38D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_3A7")
    ClearScenarioFlags(0x22, 0)
    SetScenarioFlags(0x0, 0)
    SetScenarioFlags(0x0, 1)
    Event(0, 24)
    Jump("loc_3B6")

    label("loc_3A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_3B6")
    ClearScenarioFlags(0x22, 1)
    Event(0, 27)

    label("loc_3B6")

    Return()

    # Function_0_37C end

    def Function_1_3B7(): pass

    label("Function_1_3B7")

    OP_F0(0x1, 0x320)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_3D0")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 0)

    label("loc_3D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A8, 3)), scpexpr(EXPR_END)), "loc_48C")
    SetMapObjFrame(0xFF, "magi10_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "magi11_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "point_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "magi_04_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hasira_7s", 0x1, 0x1)
    SetMapObjFrame(0xFF, "hasira_0s", 0x1, 0x1)
    SetMapObjFrame(0xFF, "hasira_5d", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hasira_6n", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hasira_0d", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hasira_0n", 0x0, 0x1)
    Jump("loc_53A")

    label("loc_48C")

    SetMapObjFrame(0xFF, "magi10_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "magi11_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "point_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "magi_04_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "hasira_7s", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hasira_0s", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hasira_5d", 0x1, 0x1)
    SetMapObjFrame(0xFF, "hasira_6n", 0x1, 0x1)
    SetMapObjFrame(0xFF, "hasira_0d", 0x1, 0x1)
    SetMapObjFrame(0xFF, "hasira_0n", 0x1, 0x1)

    label("loc_53A")

    OP_1B(0x1, 0x0, 0x5)
    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A8, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A8, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_557")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_557")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A8, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A8, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A8, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_56F")
    OP_1B(0x1, 0x0, 0x22)

    label("loc_56F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A8, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_580")
    Call(0, 38)

    label("loc_580")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_597")
    Sound(124, 1, 60, 0)
    ClearScenarioFlags(0x0, 1)
    Jump("loc_59D")

    label("loc_597")

    Sound(124, 1, 80, 0)

    label("loc_59D")

    Return()

    # Function_1_3B7 end

    def Function_2_59E(): pass

    label("Function_2_59E")

    SetChrFlags(0x8, 0x10)
    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CE, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_892")

    ChrTalk(
        0x8,
        "……………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F… … It seems like I am out of your mind.\x01",
            "It does not seem to be a fatal injury … ….\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_674")

    ChrTalk(
        0x106,
        (
            "#10701F……what should I do?\x01",
            "Also carrying things to Mercapa\x01",
            "Is it possible to … …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6B1")

    label("loc_674")


    ChrTalk(
        0x102,
        (
            "#00101Fwhat will you do?\x01",
            "Also carrying things to Mercapa\x01",
            "It seems likely, but …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6B1")


    ChrTalk(
        0x104,
        (
            "#00301FNo, he is\x01",
            "It would be better to stop.\x02\x03",
            "#00306FIf you wake up on the ship\x01",
            "That seems to be awkward for it,\x01",
            "Let's leave it for now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FThat's right.\x01",
            "It does not change to an enemy for the time being.\x02\x03",
            "#00000FJust to be sure, even with minimal treatment alone\x01",
            "Although it may be better to do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FWell then, then … …\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd's to Charlie\x01",
            "I gave a temporary first aid.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x102,
        "#00104F… Well, this is fine.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FWell then, shall we go?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1CE, 6)
    Jump("loc_8DF")

    label("loc_892")


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

    label("loc_8DF")

    TalkEnd(0x8)
    Return()

    # Function_2_59E end

    def Function_3_8E3(): pass

    label("Function_3_8E3")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9D0")
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

    label("loc_9D0")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_3_8E3 end

    def Function_4_9DF(): pass

    label("Function_4_9DF")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    LoadEffect(0x1, "event\\ev202_00.eff")
    OP_68(-510, 35500, 34190, 0)
    MoveCamera(46, 51, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17100, 0)
    SetChrPos(0x0, 0, 35000, 36000, 180)
    SetChrPos(0x1, 0, 35000, 36000, 180)
    SetChrPos(0x2, 0, 35000, 36000, 180)
    SetChrPos(0x3, 0, 35000, 36000, 180)
    OP_A7(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    Sound(920, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x0, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_AEF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_AEF)

    def lambda_B00():
        OP_95(0xFE, -640, 35000, 32810, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_B00)
    Sleep(500)
    PlayEffect(0x1, 0xFF, 0x1, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_B57():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_B57)

    def lambda_B68():
        OP_95(0xFE, -1720, 35000, 33060, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_B68)
    Sleep(500)
    Sound(920, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x2, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_BC5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2, 2, lambda_BC5)

    def lambda_BD6():
        OP_95(0xFE, 930, 35000, 34060, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_BD6)
    Sleep(500)
    PlayEffect(0x1, 0xFF, 0x3, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_C2D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x3, 2, lambda_C2D)

    def lambda_C3E():
        OP_95(0xFE, -2850, 35000, 33620, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_C3E)
    WaitChrThread(0x3, 1)
    Sleep(1000)
    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_4_9DF end

    def Function_5_C5F(): pass

    label("Function_5_C5F")

    EventBegin(0x0)
    OP_E2(0x3)
    LoadEffect(0x1, "event\\evwarp.eff")
    Sound(936, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x0, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_CB8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_CB8)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0x1, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_D03():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_D03)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0x2, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_D4E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2, 2, lambda_D4E)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0x3, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_D99():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x3, 2, lambda_D99)
    Sleep(1000)
    NewScene("m9002", 108, 0, 0)
    IdleLoop()
    Return()

    # Function_5_C5F end

    def Function_6_DB2(): pass

    label("Function_6_DB2")

    OP_CF(0x1, 0xF4, 0x5)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DCA")
    OP_CF(0x1, 0xF5, 0x4)

    label("loc_DCA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DDE")
    OP_CF(0x1, 0xF5, 0x8)

    label("loc_DDE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DF2")
    OP_CF(0x1, 0xF5, 0x9)

    label("loc_DF2")

    Return()

    # Function_6_DB2 end

    def Function_7_DF3(): pass

    label("Function_7_DF3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E07")
    OP_CF(0x1, 0xF5, 0x4)

    label("loc_E07")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E1B")
    OP_CF(0x1, 0xF5, 0x8)

    label("loc_E1B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E2F")
    OP_CF(0x1, 0xF5, 0x9)

    label("loc_E2F")

    Return()

    # Function_7_DF3 end

    def Function_8_E30(): pass

    label("Function_8_E30")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu04600.itp")
    CreatePortrait(1, 224, 0, 480, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu04601.itp")
    CreatePortrait(2, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu04602.itp")
    LoadChrToIndex("chr/ch03450.itc", 0x1E)
    LoadChrToIndex("chr/ch00050.itc", 0x1F)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00250.itc", 0x21)
    LoadChrToIndex("chr/ch00350.itc", 0x22)
    LoadChrToIndex("chr/ch03250.itc", 0x23)
    SoundLoad(3260)
    SoundLoad(3261)
    SoundLoad(3262)
    SoundLoad(3263)
    SoundLoad(3964)
    SoundLoad(3965)
    SoundLoad(3966)
    SoundLoad(3967)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F6E")
    Call(0, 6)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F3A")
    OP_CF(0x1, 0xF5, 0x4)
    LoadChrToIndex("chr/ch03150.itc", 0x24)

    label("loc_F3A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F54")
    OP_CF(0x1, 0xF5, 0x8)
    LoadChrToIndex("chr/ch02950.itc", 0x24)

    label("loc_F54")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F6E")
    OP_CF(0x1, 0xF5, 0x9)
    LoadChrToIndex("chr/ch00950.itc", 0x24)

    label("loc_F6E")

    LoadChrToIndex("chr/ch03454.itc", 0x25)
    LoadChrToIndex("monster/ch81050.itc", 0x26)
    LoadChrToIndex("apl/ch51738.itc", 0x27)
    LoadEffect(0x0, "event\\ev602_01.eff")
    SetChrPos(0x102, -650, 35000, -750, 0)
    SetChrPos(0x101, -1100, 33000, 750, 0)
    SetChrPos(0x103, 200, 33000, 0, 0)
    SetChrPos(0x104, 1100, 33000, 1100, 0)
    SetChrPos(0xF4, 0, 33000, 1800, 0)
    SetChrPos(0xF5, 850, 33000, -1000, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x800)
    SetChrPos(0x8, 0, 35000, 25000, 180)
    ClearChrFlags(0x9, 0x80)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x9, 2300, 38000, 18000, 0)
    SetChrChipByIndex(0xA, 0x26)
    SetChrSubChip(0xA, 0x0)
    SetChrFlags(0xA, 0x20)
    OP_52(0xA, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0xA, -2100, 35000, 26000, 180)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    SetChrChipByIndex(0xB, 0x26)
    SetChrSubChip(0xB, 0x0)
    SetChrFlags(0xB, 0x20)
    OP_52(0xB, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0xB, 2100, 35000, 26000, 180)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    OP_52(0xA, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(0, 35400, -800, 0)
    MoveCamera(60, 19, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(25000, 0)
    OP_68(0, 36200, 6000, 3900)
    MoveCamera(55, 20, 0, 3900)
    OP_6E(600, 3900)
    SetCameraDistance(17280, 3900)
    FadeToBright(1000, 0)

    def lambda_1196():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_1196)
    Sleep(100)

    def lambda_11AE():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_11AE)
    Sleep(100)

    def lambda_11C6():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_11C6)
    Sleep(100)

    def lambda_11DE():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_11DE)
    Sleep(100)

    def lambda_11F6():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_11F6)
    Sleep(100)

    def lambda_120E():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_120E)
    OP_0D()
    Sleep(2100)
    StopBGM(0x9C4)
    StopSound(124, 3000, 80)
    OP_C9(0x0, 0x80000000)

    NpcTalk(
        0x9,
        "Voice of a girl",
        "#3964V#N#30W#20AAhah, you finally came!\x02",
    )

    CloseMessageWindow()
    OP_24(0xF7C)
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
    OP_C9(0x1, 0x80000000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7571", 0)
    BeginChrThread(0xF4, 0, 0, 9)
    Sleep(50)
    BeginChrThread(0x104, 0, 0, 10)
    Sleep(50)
    BeginChrThread(0x103, 0, 0, 11)
    Sleep(50)
    BeginChrThread(0x101, 0, 0, 13)
    Sleep(50)
    BeginChrThread(0x102, 0, 0, 12)
    Sleep(50)
    BeginChrThread(0xF5, 0, 0, 14)
    OP_68(-1300, 36600, 19180, 4000)
    MoveCamera(41, 14, 0, 4000)
    OP_6E(600, 4000)
    SetCameraDistance(14680, 4000)
    OP_6F(0x79)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0xF5, 0)

    ChrTalk(
        0x106,
        "#10701F#12PBlooded#8RBladder#Shirley \"……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#12PHappy\x01",
            "You waited behaving well?\x02\x03",
            "#00301FIf you were usual\x01",
            "I will not bear it and I will strike.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04606F#5PBoo - Bu.\x01",
            "It is awful, Randy elder brother.\x02\x03",
            "#04602FWell, indeed Randy's only brothers\x01",
            "I'm sortie and caught and it has annihilated but Sa.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00310F#12POi\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00211F#12P(She's too free with her words)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109F#12P(Oh, haha ….\x01",
            "You are not joking. )\x02",
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
            "Well then Rixia\x02\x03",
            "It seems you are prepared\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(150)
    SetMessageWindowPos(14, 280, -1, 3)

    AnonymousTalk(
        0x106,
        "#10708F….\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x1, 0x4, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x15E, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    Sleep(400)

    AnonymousTalk(
        0x8,
        (
            "To continue what we started at Arc En Ciel\x02\x03",
            "The best feeling \"killing\"\x01",
            "Shall I start?\x02\x03",
            "That's why Charlie\x01",
            "Was it waiting here?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(150)
    SetMessageWindowPos(14, 280, -1, 3)
    OP_C9(0x0, 0x80000000)

    AnonymousTalk(
        0x106,
        "#10703F#3260V#30W#15AI refuse.\x02",
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
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
    OP_63(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x8, 0x64, 1800, 0x2, 0x7, 0x50, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005F#6P#NEh\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1810")

    ChrTalk(
        0x10A,
        "#00605F#12POh?\x02",
    )

    CloseMessageWindow()
    Jump("loc_1873")

    label("loc_1810")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1840")

    ChrTalk(
        0x105,
        "#10402F#12POh ….?\x02",
    )

    CloseMessageWindow()
    Jump("loc_1873")

    label("loc_1840")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1873")

    ChrTalk(
        0x109,
        "#10105F#12PMr. Lisha …?\x02",
    )

    CloseMessageWindow()

    label("loc_1873")

    OP_63(0x8, 0x64, 1800, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#04601F#5PW-wait a minute\x02\x03",
            "Come here\x01",
            "Such an Ali! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10703F#12PCertainly you and I … …\x01",
            "It may be similar somewhere.\x02\x03",
            "#10708FAs a \"silver\" ……\x01",
            "When I arrived at my mind\x01",
            "so#4R噵 噵#I was brought up.\x02\x03",
            "#10701FProbably also when you notice it\x01",
            "You must have been in the world of battlefields.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04605F#5PAh, well, yeah\x02\x03",
            "#04604FThe actual battle from 9 years old\x01",
            "Was it the same as Randy's older brother?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00308F#12PHun …… Both my father and my uncle\x01",
            "Only Ika\x01",
            "Though I can not say it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04609F#5PBut, Charlie once again\x01",
            "I never thought of being unhappy?\x02\x03",
            "#04602FIt certainly hurts and it may be painful, but\x01",
            "The battle field is sparkling,\x01",
            "Because I'm excited more than anything else.\x02\x03",
            "That's not how you were, Rixia?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10706F#12PUnfortunately … I like it.\x01",
            "I did not dislike it either.\x02\x03",
            "#10708FThat's for me\x01",
            "Naturally like air ……\x02\x03",
            "Even robbing the target 's life,\x01",
            "There was no special emotion.\x02\x03",
            "#10710FIn that sense, than you\x01",
            "It probably was not like a person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F#6P#NRixia…\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x102,
        "#00108F#12PRixia…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04606F#5PHmm, I feel bad for ya\x02\x03",
            "#04602FBut was not it good?\x01",
            "It's called alkane shell\x01",
            "Other fun has been found.\x02\x03",
            "#04609FCharlie and Risha\x01",
            "\"Silver#2RIn#\"Whether or not it is\x01",
            "Separately it does not matter.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_82(0x28, 0x0, 0x7D0, 0xC8)

    ChrTalk(
        0x106,
        "#10708F#12P….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00206F#12PThat's cruel\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#12P……you……\x01",
            "It is seriously serious ……\x02\x03",
            "#00311FWhat did I do\x01",
            "Do you understand properly?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04605F#5PWhen I assaulted Arc En Ciel?\x02\x03",
            "#04606F'Cause I have to do it ah\x01",
            "Lisa seriously and Charlie\x01",
            "Do not you kill me?\x02\x03",
            "#04600FIt's too bad but what else could I do\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00310F#12P….tch\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1EF1")

    ChrTalk(
        0x10A,
        "#00606F#12PThis discussion is going nowhere\x02",
    )

    CloseMessageWindow()
    Jump("loc_1F60")

    label("loc_1EF1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1F2B")

    ChrTalk(
        0x105,
        "#10406F#12P…… I can not make myself understood.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1F60")

    label("loc_1F2B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1F60")

    ChrTalk(
        0x109,
        "#10108F#12PI can not make myself understood …\x02",
    )

    CloseMessageWindow()

    label("loc_1F60")


    ChrTalk(
        0x101,
        "#00008F#6P#NRixia…\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x106,
        (
            "#10704F#11P── All right.\x01",
            "I understand her.\x02\x03",
            "#10708FIf I am on the path of \"silver\"\x01",
            "If you find joy ……\x02\x03",
            "#10710FSurely the same as her#4RMono#Into\x01",
            "Because it would have been.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#04605F#5P???\x02",
    )

    CloseMessageWindow()
    OP_68(-1210, 36600, 19580, 750)
    MoveCamera(40, 14, 0, 750)

    def lambda_2069():
        OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_2069)
    OP_6F(0x79)
    Sleep(300)

    ChrTalk(
        0x106,
        (
            "#10703F#12P── Mr. Charlie.\x01",
            "I say it clearly.\x02\x03",
            "#10701FI don't want to die.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x64, 1800, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x8,
        "#04605F#5P…Huh\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10706F#12PUntil you come to the crossbell ……\x01",
            "I do not mind when I die\x01",
            "I thought.\x02\x03",
            "#10708FNo, I know that I die\x01",
            "I had not even consciousness.\x02\x03",
            "#10710FBut now I want to live.\x02\x03",
            "Live alive, newly grasped light\x01",
            "With important people\x01",
            "I want to pursue and go.\x02\x03",
            "#10704FSo ….\x01",
            "To \"killing\" with you\x01",
            "I can not respond.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002F#6P#NRixia…\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        "#00104F#12P#NRixia…\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#00302F#12P…… I said well,\x01",
            "Lisa-chan.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x64, 1800, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x8)

    ChrTalk(
        0x8,
        (
            "#04601F#5PSo then…\x02\x03",
            "#04606FThen why come bother.\x01",
            "I came to such a place … ….?\x02\x03",
            "#04602FLisha and Shirley\x01",
            "I did not want to fight … ….?\x02\x03",
            "The enemy of Iria who became irrecoverable\x01",
            "I did not want to take it! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10703F#12PIria absolutely ──\x01",
            "No matter what happens, I will resurrect.\x02\x03",
            "#10701FIn that sense, I will give you\x01",
            "There is no reason to take revenge.\x02\x03",
            "#10706FIf you want to be revenged\x01",
            "Even when Iria was resurrected\x01",
            "Please come and meet with her.\x02\x03",
            "#10710FPerhaps, one shot a bitter,\x01",
            "I will get it.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_82(0x32, 0x0, 0x7D0, 0xC8)

    ChrTalk(
        0x8,
        "#04601F#5P….!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012F#6P#NAhah\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x103,
        (
            "#00204F#12PCertainly if Iria\x01",
            "That seems to be done for that degree.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10704F#12PI bother to Mr. Lloyd\x01",
            "Reason for attaching … ….\x02\x03",
            "It is with you,\x01",
            "To prove to myself.\x02\x03",
            "#10702FAs I am now I'm stronger than you\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x64, 1800, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    StopBGM(0xBB8)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x8,
        "#04605F#5P#4S!?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(531, 0, 60, 0)
    Sound(540, 0, 60, 0)
    MoveCamera(38, 14, 0, 750)
    BeginChrThread(0x106, 0, 0, 23)
    WaitChrThread(0x106, 0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7540", 0)
    SetCameraDistance(13000, 30000)
    Sleep(500)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x106,
        (
            "#10703F#3261V#12P#40W#40A─ ─ At the end of the dark,\x01",
            "To me who found a new light ……\x02\x03",
            "#3262V#40AOnly the way of blood smeared with smoke\x01",
            "You do not know you do not know.\x02\x03",
            "#10701F#3263V#25AThat's what I'm here to prove\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    Sleep(500)

    def lambda_2739():
        OP_A6(0xFE, 0x0, 0x28, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_2739)
    WaitChrThread(0x8, 2)
    Sleep(500)

    def lambda_2759():
        OP_A6(0xFE, 0x0, 0x28, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_2759)
    WaitChrThread(0x8, 2)
    Sleep(300)
    Sleep(500)
    Sound(358, 0, 100, 0)
    SetChrChipByIndex(0x8, 0x25)
    SetChrSubChip(0x8, 0x0)
    Sleep(200)
    Sound(531, 0, 100, 0)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#04604F#5P#30W…… Haha … …\x01",
            "Really, Lisher is the best …\x02\x03",
            "More than mere killing … …\x01",
            "…… I am excited all the time ……\x02\x03",
            "#04611Ftruly……\x01",
            "I'm glad I came to the crossbell …!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-130, 36600, 19430, 0)
    MoveCamera(358, 11, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15180, 0)
    SetCameraDistance(14180, 1500)
    OP_0D()
    SetChrSubChip(0x106, 0x2)
    OP_A0(0x8, 1800, 0x0, 0x4)
    Sound(817, 0, 100, 0)
    BeginChrThread(0xA, 3, 0, 20)
    BeginChrThread(0xA, 2, 0, 22)
    Sleep(50)
    BeginChrThread(0xB, 3, 0, 21)
    BeginChrThread(0xB, 2, 0, 22)
    WaitChrThread(0xA, 3)
    WaitChrThread(0xB, 3)
    OP_6F(0x79)
    SetCameraDistance(11000, 24000)
    Sleep(800)
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    OP_C9(0x0, 0x80000000)

    AnonymousTalk(
        0x8,
        (
            "#3965V#5P#40W#35A── It's okay!\x01",
            "Then let's get started quickly!\x02\x03",
            "#3966V#30ARandy's brothers too\x01",
            "I will give him another opportunity!\x02\x03",
            "#3967V#35ATo the fight of Charlie\x01",
            "Do not come with me properly! Is it?\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)
    BeginChrThread(0x101, 0, 0, 15)
    BeginChrThread(0x102, 0, 0, 16)
    BeginChrThread(0x103, 0, 0, 17)
    BeginChrThread(0x104, 0, 0, 18)
    BeginChrThread(0xF5, 0, 0, 19)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF5, 0)
    Sleep(150)

    ChrTalk(
        0x104,
        "#00307F#12P#N#10AShe's coming!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00007F#6P#N#15A── Interception started!\x01",
            "We will cover Lisha with full power!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    SetMessageWindowPos(-1, 160, -1, -1)
    SetChrName("member")
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    AnonymousTalk(
        0xFF,
        "#4S#12AHuh!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x0, 0)
    SetScenarioFlags(0x0, 1)
    Battle("BattleInfo_29C", 0x0, 0x0, 0x100, 0x46, 0xFF)
    FadeToDark(0, 0, -1)
    ClearChrFlags(0x106, 0x2)
    ClearChrFlags(0x106, 0x1000)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    OP_CC(0x1, 0xFF, 0x0)
    Call(0, 24)
    Return()

    # Function_8_E30 end

    def Function_9_2B14(): pass

    label("Function_9_2B14")

    OP_9B(0x0, 0xFE, 0x0, 0x1770, 0xFA0, 0x1)
    OP_96(0xFE, 0x0, 0x88B8, 0x4614, 0xFA0, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_9_2B14 end

    def Function_10_2B3F(): pass

    label("Function_10_2B3F")

    OP_9B(0x0, 0xFE, 0x0, 0x157C, 0xFA0, 0x1)
    OP_96(0xFE, 0x460, 0x88B8, 0x413C, 0xFA0, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_10_2B3F end

    def Function_11_2B6A(): pass

    label("Function_11_2B6A")

    OP_9B(0x0, 0xFE, 0x0, 0x157C, 0xFA0, 0x1)
    OP_96(0xFE, 0x1A4, 0x88B8, 0x3C0A, 0xFA0, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_11_2B6A end

    def Function_12_2B95(): pass

    label("Function_12_2B95")

    OP_9B(0x0, 0xFE, 0x0, 0x157C, 0xFA0, 0x1)
    OP_96(0xFE, 0xFFFFFB0A, 0x88B8, 0x3EC6, 0xFA0, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_12_2B95 end

    def Function_13_2BC0(): pass

    label("Function_13_2BC0")

    OP_9B(0x0, 0xFE, 0x0, 0x1996, 0xFA0, 0x1)
    OP_96(0xFE, 0xFFFFF614, 0x88B8, 0x4132, 0xFA0, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_13_2BC0 end

    def Function_14_2BEB(): pass

    label("Function_14_2BEB")

    OP_9B(0x0, 0xFE, 0x0, 0x1AC2, 0xFA0, 0x1)
    OP_96(0xFE, 0x9EC, 0x88B8, 0x406A, 0xFA0, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_14_2BEB end

    def Function_15_2C16(): pass

    label("Function_15_2C16")

    Sleep(50)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_15_2C16 end

    def Function_16_2C28(): pass

    label("Function_16_2C28")

    Sleep(100)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_16_2C28 end

    def Function_17_2C3A(): pass

    label("Function_17_2C3A")

    Sleep(150)
    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_17_2C3A end

    def Function_18_2C46(): pass

    label("Function_18_2C46")

    Sleep(200)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_18_2C46 end

    def Function_19_2C58(): pass

    label("Function_19_2C58")

    Sleep(250)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2C80")
    Sound(531, 0, 100, 0)

    label("loc_2C80")

    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_19_2C58 end

    def Function_20_2C89(): pass

    label("Function_20_2C89")

    PlayEffect(0x0, 0x5, 0xFE, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    StopEffect(0x5, 0x2)
    Return()

    # Function_20_2C89 end

    def Function_21_2CD2(): pass

    label("Function_21_2CD2")

    PlayEffect(0x0, 0x6, 0xFE, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    StopEffect(0x6, 0x2)
    Return()

    # Function_21_2CD2 end

    def Function_22_2D1B(): pass

    label("Function_22_2D1B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2D39")
    OP_A1(0xFE, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_22_2D1B")

    label("loc_2D39")

    Return()

    # Function_22_2D1B end

    def Function_23_2D3A(): pass

    label("Function_23_2D3A")

    SetChrChipByIndex(0x106, 0x27)
    SetChrSubChip(0x106, 0x0)
    SetChrFlags(0x106, 0x2)
    SetChrFlags(0x106, 0x1000)
    SetChrSubChip(0x106, 0x0)
    Sleep(143)
    SetChrSubChip(0x106, 0x1)
    Sleep(429)
    Return()

    # Function_23_2D3A end

    def Function_24_2D5B(): pass

    label("Function_24_2D5B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    LoadChrToIndex("apl/ch51739.itc", 0x1E)
    LoadChrToIndex("chr/ch00050.itc", 0x1F)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00250.itc", 0x21)
    LoadChrToIndex("chr/ch00350.itc", 0x22)
    LoadChrToIndex("chr/ch03250.itc", 0x23)
    LoadEffect(0x0, "event/ev17082.eff")
    SoundLoad(3968)
    SoundLoad(3969)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2E08")
    Call(0, 6)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2DD4")
    OP_CF(0x1, 0xF5, 0x4)
    LoadChrToIndex("chr/ch03150.itc", 0x24)

    label("loc_2DD4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2DEE")
    OP_CF(0x1, 0xF5, 0x8)
    LoadChrToIndex("chr/ch02950.itc", 0x24)

    label("loc_2DEE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2E08")
    OP_CF(0x1, 0xF5, 0x9)
    LoadChrToIndex("chr/ch00950.itc", 0x24)

    label("loc_2E08")

    LoadChrToIndex("chr/ch00356.itc", 0x25)
    SetChrPos(0x101, -2540, 35000, 20690, 0)
    SetChrPos(0x102, -1270, 35000, 20070, 0)
    SetChrPos(0x103, 420, 35000, 19370, 0)
    SetChrPos(0x104, 1120, 35000, 20700, 0)
    SetChrPos(0xF4, 0, 35000, 22340, 0)
    SetChrPos(0xF5, 2540, 35000, 20490, 0)
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
    SetChrPos(0x8, 0, 35000, 26500, 90)
    OP_8E(0x8, "Charlie")
    OP_68(-120, 35300, 23440, 0)
    MoveCamera(160, 27, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(27500, 0)
    SetCameraDistance(22800, 4000)
    FadeToBright(1500, 0)
    PlayBGM("ed7568", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x238), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6F(0x79)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x8,
        (
            "#04606F#3968V#6P#80W#30AHa …… Ha …#1500W…\x01",
            "#04609F#40W#4S…… Hahahahahahahahah … ….!\x02\x03",
            "#04602F#3969V#40AIt was a long time ago ……\x01",
            "It really proved … …\x02",
        )
    )

    Sleep(3000)
    OP_82(0xC8, 0x0, 0xBB8, 0x3E8)
    OP_6F(0x79)
    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    SetChrSubChip(0x8, 0x1)
    OP_68(0, 36100, 23500, 0)
    MoveCamera(46, 20, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14680, 0)
    OP_0D()
    Sleep(300)
    Sound(2632, 255, 100, 0)

    ChrTalk(
        0x106,
        "#10706F#12P#40W#16AHaa.. Haaa\x02",
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#04604F#5P#40WBut it is ….\x01",
            "…… It's a bit offending … am I?\x02\x03",
            "#04600FRandy brothers anyway ……\x01",
            "It seems that it is not the power of only one person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10704F#12P#40W… That is it … …\x01",
            "Because I got it ……\x02\x03",
            "#10710FIf you have complaints ……\x01",
            "Why do not you get yours … ….?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04604F#5P#40WHehu … … now\x01",
            "It is impossible for Charlie ……\x02\x03",
            "#04602FOh well or … well then\x01",
            "Sakutto killed#2RYa#Take care! …\x02\x03",
            "#04604FRemembering it now … …\x01",
            "…… I do not have much ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10706F#12P#40W…… So kill#2RYa#I will not …\x02\x03",
            "#10701FYou should listen when people talk to you\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04606F#5P#40WTch… Ahhh\x02\x03",
            "I feel ashamed\x01",
            "I thought I'd be fine …\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0xF5, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1500)
    OP_82(0x32, 0x0, 0x7D0, 0xC8)

    ChrTalk(
        0x104,
        (
            "#00307F#11P── Kora!\x01",
            "The brat is not saying anything!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04604F#5P#40WHaha …!\x01",
            "Randy's older brother …… It's hidden ……\x02\x03",
            "#04601FFor your inquiry ……\x01",
            "Daddy is waiting for you ….?\x02\x03",
            "Preparedness ……\x01",
            "I think that it is better to decide … ….?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#11P…… Hun.\x01",
            "I understand it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04604F#5P#40WBig brothers ….\x01",
            "Well … at best let's do your best …\x02\x03",
            "That \"Sword Saint\" is also amazing … …\x01",
            "…… My daughter seems to be stupid ……\x02\x03",
            "#04606FBut well … that girl ……\x01",
            "Because it seemed to be very spicy … ….\x02\x03",
            "#04600FTo regain a smile ……\x01",
            "Alright … may well be Ali … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001F#12P#N……Ah.\x01",
            "Of course I do.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x8,
        (
            "#04606F#5P#50WNo good… falling\x02\x03",
            "#04604F#60WRixia…\x01",
            "In addition … Next time … Let's play …\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(20680, 4500)
    MoveCamera(46, 25, 0, 4500)
    BeginChrThread(0x8, 0, 0, 26)
    WaitChrThread(0x8, 0)
    Sleep(300)
    Sound(202, 0, 100, 0)
    Sound(181, 0, 80, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 0, 35050, 23440, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    SetMapObjFrame(0xFF, "magi_04_add", 0x0, 0x1)
    Sleep(1000)
    StopSound(124, 3000, 60)
    Sleep(2500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 0)
    NewScene("m9050", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_24_2D5B end

    def Function_25_36BF(): pass

    label("Function_25_36BF")

    OP_9B(0x0, 0xFE, 0x15E, 0xDAC, 0x7D0, 0x0)
    SetChrChipByIndex(0x104, 0x25)
    SetChrSubChip(0x104, 0x0)
    Sound(802, 0, 50, 0)
    Sound(805, 0, 20, 0)
    Sleep(150)
    Return()

    # Function_25_36BF end

    def Function_26_36E6(): pass

    label("Function_26_36E6")

    SetChrSubChip(0xFE, 0x2)
    Sleep(300)
    Sound(812, 0, 100, 0)
    SetChrSubChip(0xFE, 0x3)
    Sleep(300)
    Return()

    # Function_26_36E6 end

    def Function_27_36FB(): pass

    label("Function_27_36FB")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch51739.itc", 0x1E)
    LoadChrToIndex("chr/ch00050.itc", 0x1F)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00250.itc", 0x21)
    LoadChrToIndex("chr/ch03250.itc", 0x23)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3786")
    Call(0, 6)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3752")
    OP_CF(0x1, 0xF5, 0x4)
    LoadChrToIndex("chr/ch03150.itc", 0x24)

    label("loc_3752")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_376C")
    OP_CF(0x1, 0xF5, 0x8)
    LoadChrToIndex("chr/ch02950.itc", 0x24)

    label("loc_376C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3786")
    OP_CF(0x1, 0xF5, 0x9)
    LoadChrToIndex("chr/ch00950.itc", 0x24)

    label("loc_3786")

    LoadChrToIndex("chr/ch00350.itc", 0x25)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_379F")
    Call(0, 6)

    label("loc_379F")

    LoadEffect(0x0, "event/ev17012.eff")
    SetChrPos(0x101, -2540, 35000, 20690, 0)
    SetChrPos(0x102, -1270, 35000, 20070, 0)
    SetChrPos(0x103, 420, 35000, 19370, 0)
    SetChrPos(0x104, 1120, 35000, 20700, 0)
    SetChrPos(0xF4, 0, 35000, 22340, 0)
    SetChrPos(0xF5, 2540, 35000, 20490, 0)
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
    SetChrChipByIndex(0x104, 0x25)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0xF4, 0x23)
    SetChrSubChip(0xF4, 0x0)
    SetChrChipByIndex(0xF5, 0x24)
    SetChrSubChip(0xF5, 0x0)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x3)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x1000)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x2)
    SetChrFlags(0x8, 0x800)
    SetChrPos(0x8, 0, 35000, 26500, 90)
    SetMapObjFrame(0xFF, "magi_04_add", 0x0, 0x1)
    OP_68(0, 36000, 36000, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(31500, 0)
    SetCameraDistance(29500, 2600)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(300)
    PlayEffect(0x0, 0x0, 0xFF, 0x0, 0, 35000, 36000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Fade(500)
    Sound(935, 0, 80, 0)
    SetMapObjFrame(0xFF, "magi10_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "magi11_add", 0x1, 0x1)
    Sleep(200)
    SetMapObjFrame(0xFF, "point_add", 0x1, 0x1)
    Sleep(600)
    StopEffect(0x0, 0x2)
    OP_6F(0x79)
    Fade(500)
    OP_68(-320, 36100, 21970, 0)
    MoveCamera(41, 19, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15780, 0)
    OP_0D()
    Sleep(300)
    BeginChrThread(0x101, 0, 0, 28)
    BeginChrThread(0x102, 0, 0, 29)
    BeginChrThread(0x103, 0, 0, 30)
    BeginChrThread(0x104, 0, 0, 31)
    BeginChrThread(0xF4, 0, 0, 32)
    BeginChrThread(0xF5, 0, 0, 33)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)
    Sleep(300)

    ChrTalk(
        0x106,
        "#10706F#11PAhh\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#12Ptruly……\x01",
            "It was a noisy little girl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#11PHa\x01",
            "Sorry, my girlfriend.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#6PBut … … about Kea\x01",
            "He seemed to care.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)

    def lambda_3AB1():
        TurnDirection(0x101, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3AB1)
    Sleep(50)

    def lambda_3AC1():
        TurnDirection(0x104, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_3AC1)
    Sleep(50)

    def lambda_3AD1():
        TurnDirection(0x103, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_3AD1)
    Sleep(50)

    def lambda_3AE1():
        TurnDirection(0xF5, 0x106, 500)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_3AE1)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0xF5, 0)

    ChrTalk(
        0x101,
        (
            "#00001F#6PLisa.\x01",
            "Is the body okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10704F#11P……Yes.\x01",
            "It is thanks to you guys.\x02\x03",
            "#10708FAnd … I'm inside\x01",
            "Iria gave me the power.\x02\x03",
            "#10710FI think that's why we won\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3BFE")

    ChrTalk(
        0x109,
        "#10109F#11PHuhu, I see. ….\x02",
    )

    CloseMessageWindow()
    Jump("loc_3C6B")

    label("loc_3BFE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3C36")

    ChrTalk(
        0x105,
        "#10404F#11PHuh, I see.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3C6B")

    label("loc_3C36")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3C6B")

    ChrTalk(
        0x10A,
        "#00604F#11PHmm. I see…\x02",
    )

    CloseMessageWindow()

    label("loc_3C6B")


    ChrTalk(
        0x103,
        (
            "#00202F#12PIndeed it is\x01",
            "Mr. Charlie will win the game\x01",
            "I guess it was not there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10704F#11PYeah ….\x01",
            "There is no reason to lose.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x106, 0xE1, 0x1F4)
    Sleep(300)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A8, 0)), scpexpr(EXPR_END)), "loc_3D5D")

    ChrTalk(
        0x106,
        (
            "#10702F#5PWith this, this \"area\" also\x01",
            "I think I was able to release it.\x02\x03",
            "Should we return to the gate for now?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3DBA")

    label("loc_3D5D")


    ChrTalk(
        0x106,
        (
            "#10702F#5PNow, this \"area\"\x01",
            "I think I was able to release it.\x02\x03",
            "Should we return to the gate for now?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3DBA")


    ChrTalk(
        0x101,
        "#00000F#6PYeah, let's do that\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x8, 500)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#00308F#11PIt's ……\x01",
            "Well, until you wake up\x01",
            "I have to leave it alone.\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(16030, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0x8, 0x8000)
    SetChrPos(0x0, 0, 35000, 18500, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    OP_37()
    SetScenarioFlags(0x1A8, 3)
    OP_29(0xB2, 0x1, 0x4)
    ModifyEventFlags(0, 0, 0x80)
    OP_1B(0x1, 0x0, 0x22)
    StopBGM(0xFA0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7351", 0)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x15F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_27_36FB end

    def Function_28_3EAA(): pass

    label("Function_28_3EAA")

    Sleep(200)
    Sound(805, 0, 50, 0)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_28_3EAA end

    def Function_29_3EBC(): pass

    label("Function_29_3EBC")

    Sleep(300)
    Sound(531, 0, 50, 0)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_29_3EBC end

    def Function_30_3ECE(): pass

    label("Function_30_3ECE")

    Sleep(400)
    Sound(805, 0, 50, 0)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_30_3ECE end

    def Function_31_3EE0(): pass

    label("Function_31_3EE0")

    Sleep(100)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_31_3EE0 end

    def Function_32_3EEC(): pass

    label("Function_32_3EEC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3F09")
    Sound(540, 0, 50, 0)
    Jump("loc_3F2E")

    label("loc_3F09")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3F2E")
    Sound(531, 0, 50, 0)

    label("loc_3F2E")

    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_32_3EEC end

    def Function_33_3F37(): pass

    label("Function_33_3F37")

    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3F57")
    Sound(540, 0, 50, 0)
    Jump("loc_3F7C")

    label("loc_3F57")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3F7C")
    Sound(531, 0, 50, 0)

    label("loc_3F7C")

    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_33_3F37 end

    def Function_34_3F85(): pass

    label("Function_34_3F85")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    LoadChrToIndex("apl/ch51739.itc", 0x1E)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3FBE")
    Call(0, 6)

    label("loc_3FBE")

    LoadEffect(0x1, "event/evwarp.eff")
    SoundLoad(3979)
    SoundLoad(3980)
    SoundLoad(3981)
    SoundLoad(3982)
    OP_8E(0x8, "Charlie")
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x1000)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x2)
    SetChrFlags(0x8, 0x800)
    SetChrPos(0x8, 0, 35000, 26500, 90)
    SetChrPos(0xF5, 650, 35000, 33200, 0)
    SetChrPos(0x102, -650, 35000, 33200, 0)
    SetChrPos(0x103, 1850, 35000, 33900, 0)
    SetChrPos(0x104, -1850, 35000, 33900, 0)
    SetChrPos(0x101, 650, 35000, 32500, 0)
    SetChrPos(0xF4, -650, 35000, 32500, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_92(0xF5, 0x0, 0x8CA0, 0x0)
    OP_92(0x101, 0x0, 0x8CA0, 0x0)
    OP_92(0x102, 0x0, 0x8CA0, 0x0)
    OP_92(0x103, 0x0, 0x8CA0, 0x0)
    OP_92(0x104, 0x0, 0x8CA0, 0x0)
    OP_92(0xF4, 0x0, 0x8CA0, 0x0)
    OP_68(-1040, 37000, 33640, 0)
    MoveCamera(31, 15, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(13500, 0)
    SetCameraDistance(16230, 8000)
    FadeToBright(1000, 0)
    Sleep(400)
    BeginChrThread(0xF5, 0, 0, 35)
    Sleep(900)
    BeginChrThread(0x102, 0, 0, 35)
    Sleep(600)
    BeginChrThread(0x103, 0, 0, 35)
    Sleep(600)
    BeginChrThread(0x104, 0, 0, 35)
    Sleep(600)
    BeginChrThread(0x101, 0, 0, 35)
    Sleep(800)
    BeginChrThread(0xF4, 0, 0, 35)
    Sleep(600)
    StopBGM(0x1770)
    OP_6F(0x79)
    Sleep(300)
    BeginChrThread(0x8, 0, 0, 36)
    WaitChrThread(0x8, 0)
    Sleep(500)

    ChrTalk(
        0x8,
        "#04601F#12P#N….\x02",
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(-3200, 37000, 36160, 0)
    OP_68(-2950, 37000, 32200, 2500)
    MoveCamera(142, 14, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(8510, 0)
    OP_63(0x8, 0xFFFFFEA2, 1050, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2500)
    OP_64(0x8)
    OP_6F(0x79)
    Sleep(500)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x8,
        (
            "#04606F#3979V#5P#50WAh … … If it's the current timing\x01",
            "Some of you blew off my head … …\x02\x03",
            "#04600F#3980V#50WReally ….\x01",
            "…… I will be feeling healthy ……\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xF8C)
    Sleep(300)
    OP_63(0x8, 0xFFFFFEA2, 1050, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x8)
    Sleep(500)
    BeginChrThread(0x8, 0, 0, 37)
    WaitChrThread(0x8, 0)
    Sleep(300)
    SetCameraDistance(20940, 20000)
    Sleep(500)

    ChrTalk(
        0x8,
        "#04606F#3981V#5P#60W#40A#3SIt's no good… I'm falling\x02",
    )

    CloseMessageWindow()
    Sleep(1500)

    ChrTalk(
        0x8,
        (
            "#04606F#3982V#5P#60W#60A#2S…… After all scouts ……\x01",
            "Who told me … Is it okay …?\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    Sleep(500)
    StopSound(124, 1000, 80)
    FadeToDark(1500, 0, -1)
    OP_0D()
    OP_37()
    SetScenarioFlags(0x1A8, 4)
    WaitBGM()
    Sleep(1000)
    EventEnd(0x5)
    NewScene("m9002", 108, 0, 0)
    IdleLoop()
    Return()

    # Function_34_3F85 end

    def Function_35_439F(): pass

    label("Function_35_439F")

    OP_95(0xFE, 0, 36000, 36000, 1500, 0x0)
    Sound(936, 0, 80, 0)
    PlayEffect(0x1, 0xFF, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    Return()

    # Function_35_439F end

    def Function_36_43FC(): pass

    label("Function_36_43FC")

    SetChrSubChip(0xFE, 0x4)
    Sound(358, 0, 50, 0)
    Sleep(150)
    Sound(531, 0, 50, 0)
    SetChrSubChip(0xFE, 0x5)
    Fade(250)
    OP_0D()
    Sleep(450)
    Return()

    # Function_36_43FC end

    def Function_37_441D(): pass

    label("Function_37_441D")

    SetChrSubChip(0xFE, 0x6)
    Sound(358, 0, 40, 0)
    Sleep(150)
    Sound(531, 0, 40, 0)
    SetChrSubChip(0xFE, 0x7)
    Sleep(300)
    Return()

    # Function_37_441D end

    def Function_38_4438(): pass

    label("Function_38_4438")

    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x3)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x1000)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x2)
    SetChrFlags(0x8, 0x800)
    Return()

    # Function_38_4438 end

    SaveToFile()

Try(main)
