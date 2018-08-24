from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "Shirley",                # 1
        "台詞表示用ダミーキャラ", # 2
        "Shirley's Companion",    # 3
        "Shirley's Companion",    # 4
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
        "Function_3_911",          # 03, 3
        "Function_4_A05",          # 04, 4
        "Function_5_C85",          # 05, 5
        "Function_6_DD8",          # 06, 6
        "Function_7_E19",          # 07, 7
        "Function_8_E56",          # 08, 8
        "Function_9_2C79",         # 09, 9
        "Function_10_2CA4",        # 0A, 10
        "Function_11_2CCF",        # 0B, 11
        "Function_12_2CFA",        # 0C, 12
        "Function_13_2D25",        # 0D, 13
        "Function_14_2D50",        # 0E, 14
        "Function_15_2D7B",        # 0F, 15
        "Function_16_2D8D",        # 10, 16
        "Function_17_2D9F",        # 11, 17
        "Function_18_2DAB",        # 12, 18
        "Function_19_2DBD",        # 13, 19
        "Function_20_2DEE",        # 14, 20
        "Function_21_2E37",        # 15, 21
        "Function_22_2E80",        # 16, 22
        "Function_23_2E9F",        # 17, 23
        "Function_24_2EC0",        # 18, 24
        "Function_25_3892",        # 19, 25
        "Function_26_38B9",        # 1A, 26
        "Function_27_38CE",        # 1B, 27
        "Function_28_409B",        # 1C, 28
        "Function_29_40AD",        # 1D, 29
        "Function_30_40BF",        # 1E, 30
        "Function_31_40D1",        # 1F, 31
        "Function_32_40DD",        # 20, 32
        "Function_33_4128",        # 21, 33
        "Function_34_4176",        # 22, 34
        "Function_35_45A7",        # 23, 35
        "Function_36_4604",        # 24, 36
        "Function_37_4625",        # 25, 37
        "Function_38_4640",        # 26, 38
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CE, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8D0")

    ChrTalk(
        0x8,
        "...............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F...It appears she's lost\x01",
            "consciousness. The wound\x01",
            "doesn't seem fatal...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_672")

    ChrTalk(
        0x106,
        (
            "#10701F...What do we do? We\x01",
            "could carry her to the\x01",
            "Merkabah...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6B3")

    label("loc_672")


    ChrTalk(
        0x102,
        (
            "#00101FWhat do we do? We could\x01",
            "carry her to the\x01",
            "Merkabah...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6B3")


    ChrTalk(
        0x104,
        (
            "#00301FNo, we'd best leave her alone.\x02\x03",
            "#00306FIf she woke up inside the ship, that\x01",
            "would come with its own set of problems,\x01",
            "so let's leave her be for the time being.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FYou're right... The fact\x01",
            "that she's an enemy hasn't\x01",
            "changed.\x02\x03",
            "#00000FAlthough, just to be safe,\x01",
            "maybe we should give her a\x01",
            "minimum level of treatment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FRight, then...\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd and the others\x01",
            "administered first aid\x01",
            "to Shirley.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x102,
        (
            "#00104F...Alright, this should\x01",
            "be fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FIn that case, let's go.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1CE, 6)
    Jump("loc_90D")

    label("loc_8D0")


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
            "It seems she is out\x01",
            "cold.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_90D")

    TalkEnd(0x8)
    Return()

    # Function_2_59E end

    def Function_3_911(): pass

    label("Function_3_911")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9F6")
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

    label("loc_9F6")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_3_911 end

    def Function_4_A05(): pass

    label("Function_4_A05")

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

    def lambda_B15():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_B15)

    def lambda_B26():
        OP_95(0xFE, -640, 35000, 32810, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_B26)
    Sleep(500)
    PlayEffect(0x1, 0xFF, 0x1, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_B7D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_B7D)

    def lambda_B8E():
        OP_95(0xFE, -1720, 35000, 33060, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_B8E)
    Sleep(500)
    Sound(920, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x2, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_BEB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2, 2, lambda_BEB)

    def lambda_BFC():
        OP_95(0xFE, 930, 35000, 34060, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_BFC)
    Sleep(500)
    PlayEffect(0x1, 0xFF, 0x3, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_C53():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x3, 2, lambda_C53)

    def lambda_C64():
        OP_95(0xFE, -2850, 35000, 33620, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_C64)
    WaitChrThread(0x3, 1)
    Sleep(1000)
    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_4_A05 end

    def Function_5_C85(): pass

    label("Function_5_C85")

    EventBegin(0x0)
    OP_E2(0x3)
    LoadEffect(0x1, "event\\evwarp.eff")
    Sound(936, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x0, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_CDE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_CDE)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0x1, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_D29():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_D29)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0x2, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_D74():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2, 2, lambda_D74)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0x3, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_DBF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x3, 2, lambda_DBF)
    Sleep(1000)
    NewScene("m9002", 108, 0, 0)
    IdleLoop()
    Return()

    # Function_5_C85 end

    def Function_6_DD8(): pass

    label("Function_6_DD8")

    OP_CF(0x1, 0xF4, 0x5)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DF0")
    OP_CF(0x1, 0xF5, 0x4)

    label("loc_DF0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E04")
    OP_CF(0x1, 0xF5, 0x8)

    label("loc_E04")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E18")
    OP_CF(0x1, 0xF5, 0x9)

    label("loc_E18")

    Return()

    # Function_6_DD8 end

    def Function_7_E19(): pass

    label("Function_7_E19")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E2D")
    OP_CF(0x1, 0xF5, 0x4)

    label("loc_E2D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E41")
    OP_CF(0x1, 0xF5, 0x8)

    label("loc_E41")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E55")
    OP_CF(0x1, 0xF5, 0x9)

    label("loc_E55")

    Return()

    # Function_7_E19 end

    def Function_8_E56(): pass

    label("Function_8_E56")

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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F94")
    Call(0, 6)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F60")
    OP_CF(0x1, 0xF5, 0x4)
    LoadChrToIndex("chr/ch03150.itc", 0x24)

    label("loc_F60")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F7A")
    OP_CF(0x1, 0xF5, 0x8)
    LoadChrToIndex("chr/ch02950.itc", 0x24)

    label("loc_F7A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F94")
    OP_CF(0x1, 0xF5, 0x9)
    LoadChrToIndex("chr/ch00950.itc", 0x24)

    label("loc_F94")

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

    def lambda_11BC():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_11BC)
    Sleep(100)

    def lambda_11D4():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_11D4)
    Sleep(100)

    def lambda_11EC():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_11EC)
    Sleep(100)

    def lambda_1204():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1204)
    Sleep(100)

    def lambda_121C():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_121C)
    Sleep(100)

    def lambda_1234():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_1234)
    OP_0D()
    Sleep(2100)
    StopBGM(0x9C4)
    StopSound(124, 3000, 80)
    OP_C9(0x0, 0x80000000)

    NpcTalk(
        0x9,
        "Young Girl's Voice",
        (
            "#3964V#N#30W#20AAha! ...You're finally\x01",
            "here!\x02",
        )
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
        "#10701F#12PBloody Shirley...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#12PHah... You were waitin'\x01",
            "'n behavin' properly?\x02\x03",
            "#00301FYour usual self would've\x01",
            "come to attack us\x01",
            "impatiently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04606F#5PBoo, boo. That's mean, Randy.\x02\x03",
            "#04602FAlthough, well, it's true that just for\x01",
            "Randy and his pals, I'd have done a\x01",
            "rapid sortie and annihilated you all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00310F#12P...Hey.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00211F#12P(She's too blunt...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109F#12P(A-Ahaha... She's not\x01",
            "joking.)\x02",
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
            "Well then─ Rixia.\x02\x03",
            "You're quite fired up, aren't you?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(150)
    SetMessageWindowPos(14, 280, -1, 3)

    AnonymousTalk(
        0x106,
        "#10708F............\x02",
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
            "The sequel to what\x01",
            "happened at Arc-en-Ciel...\x02\x03",
            "Shall we begin the best\x01",
            ""Duel to the Death" ever?\x02\x03",
            "Poor lil' Shirley has been\x01",
            "waiting here all alone\x01",
            "just for that, you know?\x02",
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
        "#10703F#3260V#30W#15A─I refuse.\x02",
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
        "#00005F#6P#NHuh...\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1857")

    ChrTalk(
        0x10A,
        "#00605F#12POh?\x02",
    )

    CloseMessageWindow()
    Jump("loc_18AB")

    label("loc_1857")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1881")

    ChrTalk(
        0x105,
        "#10402F#12PHuh?\x02",
    )

    CloseMessageWindow()
    Jump("loc_18AB")

    label("loc_1881")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_18AB")

    ChrTalk(
        0x109,
        "#10105F#12PRixia...?\x02",
    )

    CloseMessageWindow()

    label("loc_18AB")

    OP_63(0x8, 0x64, 1800, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#04601F#5PW-Wait a moment!\x02\x03",
            "You're really gonna come\x01",
            "all the way here and say\x01",
            "that!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10703F#12PIt's true that you and I... may be\x01",
            "similar in some respects.\x02\x03",
            "#10708FI, as Yin... I was brought up as\x01",
            "him from the day I was born.\x02\x03",
            "#10701FIt's probably the same with you.\x01",
            "The battlefield has been your world\x01",
            "for as long as you can remember.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04605F#5PYep, sounds about right.\x02\x03",
            "#04604FMy first real battles were when\x01",
            "I was 9 years old, so I guess\x01",
            "I'm the same as you, Randy?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00308F#12PHmph... I can only say that\x01",
            "my ol' man and my uncle\x01",
            "were both completely crazy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04609F#5PHowever, Shirley has never thought even\x01",
            "once that she didn't want to do it.\x02\x03",
            "#04602FIt's true that it hurts and painful stuff\x01",
            "happens too, but the battlefield sparkles\x01",
            "and I can get the best excitement there.\x02\x03",
            "Weren't you the same, Rixia?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10706F#12PUnfortunately... I neither\x01",
            "liked it nor hated it.\x02\x03",
            "#10708FTo me, battle was as natural\x01",
            "as the air...\x02\x03",
            "Even snatching away a\x01",
            "target's life didn't give me\x01",
            "any strong feelings at all.\x02\x03",
            "#10710FIn that sense, I was less of\x01",
            "a person than you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F#6P#N...Rixia.\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x102,
        "#00108F#12PRixia...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04606F#5PHmm, how sad.\x02\x03",
            "#04602FStill, aren't you glad? To find\x01",
            "so much excitement at that Arc-\x01",
            "en-Ciel or whatever it's called.\x02\x03",
            "#04609FShirley also doesn't really give\x01",
            "a crap if you're Yin or\x01",
            "whatever.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_82(0x28, 0x0, 0x7D0, 0xC8)

    ChrTalk(
        0x106,
        "#10708F#12P............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00206F#12P...How cruel.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#12P...You... You're really\x01",
            "messed up inside...\x02\x03",
            "#00311FDo you really understand\x01",
            "what you've done?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04605F#5PAttacking Arc-en-Ciel?\x02\x03",
            "#04606FBut, if I hadn't done that, Rixia\x01",
            "would've never wanted to kill\x01",
            "Shirley with all her heart, right?\x02\x03",
            "#04600FThough I think it was a little\x01",
            "mean, I couldn't help it, see?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00310F#12P...Damn...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2008")

    ChrTalk(
        0x10A,
        (
            "#00606F#12PWords won't get through\x01",
            "to her, huh...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_209C")

    label("loc_2008")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2055")

    ChrTalk(
        0x105,
        (
            "#10406F#12P...Words won't get\x01",
            "through to her, huh.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_209C")

    label("loc_2055")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_209C")

    ChrTalk(
        0x109,
        (
            "#10108F#12PWords won't get through\x01",
            "to her, huh...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_209C")


    ChrTalk(
        0x101,
        "#00008F#6P#N...Rixia...\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x106,
        (
            "#10704F#11P─It's all right. I\x01",
            "understand her.\x02\x03",
            "#10708FIf I had found joy and\x01",
            "fulfillment in the path\x01",
            "of Yin...\x02\x03",
            "#10710FI'm certain I would've\x01",
            "become just like her.\x02",
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

    def lambda_2198():
        OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_2198)
    OP_6F(0x79)
    Sleep(300)

    ChrTalk(
        0x106,
        (
            "#10703F#12P─Shirley. I'll say it\x01",
            "clearly.\x02\x03",
            "#10701FI don't want to die.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x64, 1800, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x8,
        "#04605F#5P......Huh.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10706F#12PUntil I came to Crossbell... I\x01",
            "didn't think I would care even\x01",
            "if I lost my life some day.\x02\x03",
            "#10708FNo, the thought of my own death\x01",
            "never even crossed my mind.\x02\x03",
            "#10710FHowever─ Now I want to live.\x02\x03",
            "To live, to pursue this new\x01",
            "light I've grabbed hold of with\x01",
            "those who are precious to me.\x02\x03",
            "#10704FThat's why... I can't accept a\x01",
            ""Duel to the Death" with you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002F#6P#NRixia...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        "#00104F#12P#NRixia...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        "#00302F#12P...Well said, Rixia.\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x64, 1800, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x8)

    ChrTalk(
        0x8,
        (
            "#04601F#5P...Then...\x02\x03",
            "#04606FThen why did you come to\x01",
            "this place?\x02\x03",
            "#04602FDidn't you want to fight\x01",
            "Shirley too?\x02\x03",
            "Didn't you want to\x01",
            "avenge Ilya who is\x01",
            "beyond recovery!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10703F#12PIlya WILL recover─ No\x01",
            "matter what happens.\x02\x03",
            "#10701FIn that sense, I have no\x01",
            "reason to seek revenge\x01",
            "against you.\x02\x03",
            "#10706FIf I wanted revenge, I'd\x01",
            "have you visit Ilya\x01",
            "after she's recovered.\x02\x03",
            "#10710FI think you'd get an\x01",
            "intense slap to the\x01",
            "face.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_82(0x32, 0x0, 0x7D0, 0xC8)

    ChrTalk(
        0x8,
        "#04601F#5P......!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012F#6P#N...Haha...\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x103,
        (
            "#00204F#12PIndeed, I think Ilya\x01",
            "would end things with\x01",
            "just that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10704F#12PThe reason why I tagged\x01",
            "along with Lloyd and the\x01",
            "others is...\x02\x03",
            "To prove to you in\x01",
            "person that...\x02\x03",
            "#10702FAs I am now, I'm─\x01",
            "stronger than you.\x02",
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
            "#10703F#3261V#12P#40W#40A─To me, who has found out a\x01",
            "new light at the end of the\x01",
            "darkness...\x02\x03",
            "#3262V#40AYou, who knows only the\x01",
            "bloody path of gunpowder and\x01",
            "smoke, are no match for me.\x02\x03",
            "#10701F#3263V#25AAnd I intend to prove it.\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    Sleep(500)

    def lambda_2877():
        OP_A6(0xFE, 0x0, 0x28, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_2877)
    WaitChrThread(0x8, 2)
    Sleep(500)

    def lambda_2897():
        OP_A6(0xFE, 0x0, 0x28, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_2897)
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
            "#04604F#5P#30W...Ahaha... Really,\x01",
            "you're the best,\x01",
            "Rixia...\x02\x03",
            "This is way more\x01",
            "exciting than... a mere\x01",
            "duel to the death...\x02\x03",
            "#04611FReally... I'm glad I\x01",
            "came to Crossbell!\x02",
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
            "#3965V#5P#40W#35A─Fine! Then, let's get started\x01",
            "already!\x02\x03",
            "#3966V#30ASince you're here, I'll face Randy\x01",
            "and the rest of you as well!\x02\x03",
            "#3967V#35AWill you be able to keep up in a\x01",
            "fight with the great Shirley!?\x02",
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
            "#00007F#6P#N#15A─Let's stop her! Support\x01",
            "Rixia with all our\x01",
            "might!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    SetMessageWindowPos(-1, 160, -1, -1)
    SetChrName("Members")
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    AnonymousTalk(
        0xFF,
        "#4S#12ARight!\x02",
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

    # Function_8_E56 end

    def Function_9_2C79(): pass

    label("Function_9_2C79")

    OP_9B(0x0, 0xFE, 0x0, 0x1770, 0xFA0, 0x1)
    OP_96(0xFE, 0x0, 0x88B8, 0x4614, 0xFA0, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_9_2C79 end

    def Function_10_2CA4(): pass

    label("Function_10_2CA4")

    OP_9B(0x0, 0xFE, 0x0, 0x157C, 0xFA0, 0x1)
    OP_96(0xFE, 0x460, 0x88B8, 0x413C, 0xFA0, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_10_2CA4 end

    def Function_11_2CCF(): pass

    label("Function_11_2CCF")

    OP_9B(0x0, 0xFE, 0x0, 0x157C, 0xFA0, 0x1)
    OP_96(0xFE, 0x1A4, 0x88B8, 0x3C0A, 0xFA0, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_11_2CCF end

    def Function_12_2CFA(): pass

    label("Function_12_2CFA")

    OP_9B(0x0, 0xFE, 0x0, 0x157C, 0xFA0, 0x1)
    OP_96(0xFE, 0xFFFFFB0A, 0x88B8, 0x3EC6, 0xFA0, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_12_2CFA end

    def Function_13_2D25(): pass

    label("Function_13_2D25")

    OP_9B(0x0, 0xFE, 0x0, 0x1996, 0xFA0, 0x1)
    OP_96(0xFE, 0xFFFFF614, 0x88B8, 0x4132, 0xFA0, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_13_2D25 end

    def Function_14_2D50(): pass

    label("Function_14_2D50")

    OP_9B(0x0, 0xFE, 0x0, 0x1AC2, 0xFA0, 0x1)
    OP_96(0xFE, 0x9EC, 0x88B8, 0x406A, 0xFA0, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_14_2D50 end

    def Function_15_2D7B(): pass

    label("Function_15_2D7B")

    Sleep(50)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_15_2D7B end

    def Function_16_2D8D(): pass

    label("Function_16_2D8D")

    Sleep(100)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_16_2D8D end

    def Function_17_2D9F(): pass

    label("Function_17_2D9F")

    Sleep(150)
    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_17_2D9F end

    def Function_18_2DAB(): pass

    label("Function_18_2DAB")

    Sleep(200)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_18_2DAB end

    def Function_19_2DBD(): pass

    label("Function_19_2DBD")

    Sleep(250)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2DE5")
    Sound(531, 0, 100, 0)

    label("loc_2DE5")

    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_19_2DBD end

    def Function_20_2DEE(): pass

    label("Function_20_2DEE")

    PlayEffect(0x0, 0x5, 0xFE, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    StopEffect(0x5, 0x2)
    Return()

    # Function_20_2DEE end

    def Function_21_2E37(): pass

    label("Function_21_2E37")

    PlayEffect(0x0, 0x6, 0xFE, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    StopEffect(0x6, 0x2)
    Return()

    # Function_21_2E37 end

    def Function_22_2E80(): pass

    label("Function_22_2E80")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2E9E")
    OP_A1(0xFE, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_22_2E80")

    label("loc_2E9E")

    Return()

    # Function_22_2E80 end

    def Function_23_2E9F(): pass

    label("Function_23_2E9F")

    SetChrChipByIndex(0x106, 0x27)
    SetChrSubChip(0x106, 0x0)
    SetChrFlags(0x106, 0x2)
    SetChrFlags(0x106, 0x1000)
    SetChrSubChip(0x106, 0x0)
    Sleep(143)
    SetChrSubChip(0x106, 0x1)
    Sleep(429)
    Return()

    # Function_23_2E9F end

    def Function_24_2EC0(): pass

    label("Function_24_2EC0")

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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2F6D")
    Call(0, 6)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2F39")
    OP_CF(0x1, 0xF5, 0x4)
    LoadChrToIndex("chr/ch03150.itc", 0x24)

    label("loc_2F39")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2F53")
    OP_CF(0x1, 0xF5, 0x8)
    LoadChrToIndex("chr/ch02950.itc", 0x24)

    label("loc_2F53")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2F6D")
    OP_CF(0x1, 0xF5, 0x9)
    LoadChrToIndex("chr/ch00950.itc", 0x24)

    label("loc_2F6D")

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
    OP_8E(0x8, "Shirley")
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
            "#04606F#3968V#6P#80W#30A*pant*... *pant*...#800W...\x01",
            "#04609F#40W#4S......Ahahahahahahaha!\x02\x03",
            "#04602F#3969V#40AI give up... You really proved it...\x02",
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
        "#10706F#12P#40W#16A*pant*... *pant*...\x02",
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#04604F#5P#40WBut wasn't that... a bit\x01",
            "of foul play, hmm?\x02\x03",
            "#04600FYou had Randy and the\x01",
            "others... That wasn't\x01",
            "just your own strength.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10704F#12P#40W...That is exactly...\x01",
            "what I've obtained...\x02\x03",
            "#10710FIf you want to complain\x01",
            "about it... Why don't\x01",
            "you obtain it yourself?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04604F#5P#40WHaha... I think that's\x01",
            "impossible for Shirley\x01",
            "now...\x02\x03",
            "#04602FWell, whatever... Then,\x01",
            "chop-chop, hurry up and\x01",
            "kill me...\x02\x03",
            "#04604FIf it's now... I have no\x01",
            "regrets...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10706F#12P#40W...I already told you,\x01",
            "I'm not going to kill\x01",
            "you...\x02\x03",
            "#10701FPlease listen properly\x01",
            "when people talk to\x01",
            "you...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04606F#5P#40WTch... Aah, geez...\x02\x03",
            "And here I was thinking I\x01",
            "could go to the other side\x01",
            "when I was feeling so great...\x02",
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
            "#00307F#11P─Hey! Brats don't get to\x01",
            "say cheeky things!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04604F#5P#40WAhaha! You're mean,\x01",
            "Randy...\x02\x03",
            "#04601FLet me just say this...\x01",
            "Papa is dying to see\x01",
            "you, you know?\x02\x03",
            "You should make up your\x01",
            "mind... Prepare\x01",
            "yourself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00306F#11P...Hmph. I know.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04604F#5P#40WYou guys too... Well... do\x01",
            "your very best...\x02\x03",
            "That Divine Blade is amazing\x01",
            "too... That young lady seems\x01",
            "dangerous herself...\x02\x03",
            "#04606FBut well... That kid... She\x01",
            "looked like she was in pain,\x01",
            "so...\x02\x03",
            "#04600FTo get her smile back... I\x01",
            "know you're going to do your\x01",
            "best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001F#12P#N...Yeah. Of course we\x01",
            "are.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x8,
        (
            "#04606F#5P#50W...It's no good... I'm\x01",
            "passing out...\x02\x03",
            "#04604F#60WRixia... Let's play\x01",
            "again... another time...\x02",
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

    # Function_24_2EC0 end

    def Function_25_3892(): pass

    label("Function_25_3892")

    OP_9B(0x0, 0xFE, 0x15E, 0xDAC, 0x7D0, 0x0)
    SetChrChipByIndex(0x104, 0x25)
    SetChrSubChip(0x104, 0x0)
    Sound(802, 0, 50, 0)
    Sound(805, 0, 20, 0)
    Sleep(150)
    Return()

    # Function_25_3892 end

    def Function_26_38B9(): pass

    label("Function_26_38B9")

    SetChrSubChip(0xFE, 0x2)
    Sleep(300)
    Sound(812, 0, 100, 0)
    SetChrSubChip(0xFE, 0x3)
    Sleep(300)
    Return()

    # Function_26_38B9 end

    def Function_27_38CE(): pass

    label("Function_27_38CE")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch51739.itc", 0x1E)
    LoadChrToIndex("chr/ch00050.itc", 0x1F)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00250.itc", 0x21)
    LoadChrToIndex("chr/ch03250.itc", 0x23)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3959")
    Call(0, 6)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3925")
    OP_CF(0x1, 0xF5, 0x4)
    LoadChrToIndex("chr/ch03150.itc", 0x24)

    label("loc_3925")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_393F")
    OP_CF(0x1, 0xF5, 0x8)
    LoadChrToIndex("chr/ch02950.itc", 0x24)

    label("loc_393F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3959")
    OP_CF(0x1, 0xF5, 0x9)
    LoadChrToIndex("chr/ch00950.itc", 0x24)

    label("loc_3959")

    LoadChrToIndex("chr/ch00350.itc", 0x25)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3972")
    Call(0, 6)

    label("loc_3972")

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
        "#10706F#11P...Phew...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#12PReally... What a\x01",
            "troublemaker.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#11P*sigh*... Sorry, she's\x01",
            "my relative after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#6PHowever... It seemed she\x01",
            "was worried about KeA.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)

    def lambda_3C85():
        TurnDirection(0x101, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3C85)
    Sleep(50)

    def lambda_3C95():
        TurnDirection(0x104, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_3C95)
    Sleep(50)

    def lambda_3CA5():
        TurnDirection(0x103, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_3CA5)
    Sleep(50)

    def lambda_3CB5():
        TurnDirection(0xF5, 0x106, 500)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_3CB5)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0xF5, 0)

    ChrTalk(
        0x101,
        (
            "#00001F#6PRixia. How are you\x01",
            "feeling?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10704F#11P...Fine. Thanks to all\x01",
            "of you having been by my\x01",
            "side.\x02\x03",
            "#10708FAlso... The Ilya inside\x01",
            "me gave me strength.\x02\x03",
            "#10710FI think that's why I\x01",
            "won.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3DCC")

    ChrTalk(
        0x109,
        "#10109F#11PHaha, I see...\x02",
    )

    CloseMessageWindow()
    Jump("loc_3E2D")

    label("loc_3DCC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3DFE")

    ChrTalk(
        0x105,
        "#10404F#11PHehe, I see.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3E2D")

    label("loc_3DFE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3E2D")

    ChrTalk(
        0x10A,
        "#00604F#11PHmph... I see.\x02",
    )

    CloseMessageWindow()

    label("loc_3E2D")


    ChrTalk(
        0x103,
        (
            "#00202F#12PThen Shirley really had\x01",
            "no chance to win.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10704F#11PYes... There's no way I\x01",
            "could lose.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x106, 0xE1, 0x1F4)
    Sleep(300)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A8, 0)), scpexpr(EXPR_END)), "loc_3F2F")

    ChrTalk(
        0x106,
        (
            "#10702F#5PWith this, I think we\x01",
            "were able to release\x01",
            "this Territory as well.\x02\x03",
            "Should we head back to\x01",
            "the gate for now?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F9C")

    label("loc_3F2F")


    ChrTalk(
        0x106,
        (
            "#10702F#5PWith this, I think we\x01",
            "have released this\x01",
            "Territory.\x02\x03",
            "Should we head back to\x01",
            "the gate for now?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F9C")


    ChrTalk(
        0x101,
        "#00000F#6PYeah, let's.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x8, 500)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#00308F#11PAs for her... Well, we have\x01",
            "no choice but to leave her\x01",
            "be until she wakes up.\x02",
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

    # Function_27_38CE end

    def Function_28_409B(): pass

    label("Function_28_409B")

    Sleep(200)
    Sound(805, 0, 50, 0)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_28_409B end

    def Function_29_40AD(): pass

    label("Function_29_40AD")

    Sleep(300)
    Sound(531, 0, 50, 0)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_29_40AD end

    def Function_30_40BF(): pass

    label("Function_30_40BF")

    Sleep(400)
    Sound(805, 0, 50, 0)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_30_40BF end

    def Function_31_40D1(): pass

    label("Function_31_40D1")

    Sleep(100)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_31_40D1 end

    def Function_32_40DD(): pass

    label("Function_32_40DD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_40FA")
    Sound(540, 0, 50, 0)
    Jump("loc_411F")

    label("loc_40FA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_411F")
    Sound(531, 0, 50, 0)

    label("loc_411F")

    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_32_40DD end

    def Function_33_4128(): pass

    label("Function_33_4128")

    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4148")
    Sound(540, 0, 50, 0)
    Jump("loc_416D")

    label("loc_4148")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_416D")
    Sound(531, 0, 50, 0)

    label("loc_416D")

    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_33_4128 end

    def Function_34_4176(): pass

    label("Function_34_4176")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    LoadChrToIndex("apl/ch51739.itc", 0x1E)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_41AF")
    Call(0, 6)

    label("loc_41AF")

    LoadEffect(0x1, "event/evwarp.eff")
    SoundLoad(3979)
    SoundLoad(3980)
    SoundLoad(3981)
    SoundLoad(3982)
    OP_8E(0x8, "Shirley")
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
        "#04601F#12P#N............\x02",
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
            "#04606F#3979V#5P#50WAah, geez... With this timing,\x01",
            "I could've blown off some of\x01",
            "their heads, and yet...\x02\x03",
            "#04600F#3980V#50WReally, geez... I'm so out of\x01",
            "it...\x02",
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
        (
            "#04606F#3981V#5P#60W#40A#3SIt's no good... This\x01",
            "time I'm really passing\x01",
            "out...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(1500)

    ChrTalk(
        0x8,
        (
            "#04606F#3982V#5P#60W#60A#2S...As expected, should I\x01",
            "accept... her offer...\x01",
            "maybe?\x02",
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

    # Function_34_4176 end

    def Function_35_45A7(): pass

    label("Function_35_45A7")

    OP_95(0xFE, 0, 36000, 36000, 1500, 0x0)
    Sound(936, 0, 80, 0)
    PlayEffect(0x1, 0xFF, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    Return()

    # Function_35_45A7 end

    def Function_36_4604(): pass

    label("Function_36_4604")

    SetChrSubChip(0xFE, 0x4)
    Sound(358, 0, 50, 0)
    Sleep(150)
    Sound(531, 0, 50, 0)
    SetChrSubChip(0xFE, 0x5)
    Fade(250)
    OP_0D()
    Sleep(450)
    Return()

    # Function_36_4604 end

    def Function_37_4625(): pass

    label("Function_37_4625")

    SetChrSubChip(0xFE, 0x6)
    Sound(358, 0, 40, 0)
    Sleep(150)
    Sound(531, 0, 40, 0)
    SetChrSubChip(0xFE, 0x7)
    Sleep(300)
    Return()

    # Function_37_4625 end

    def Function_38_4640(): pass

    label("Function_38_4640")

    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x3)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x1000)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x2)
    SetChrFlags(0x8, 0x800)
    Return()

    # Function_38_4640 end

    SaveToFile()

Try(main)
