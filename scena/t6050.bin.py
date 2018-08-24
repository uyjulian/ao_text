﻿from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t6050.bin",                # FileName
        "t6050",                    # MapName
        "t6050",                    # Location
        0x00CA,                     # MapIndex
        "ed7000",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x25,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 202, 0, 0, 0, 1],
    )

    BuildStringList((
        "t6050",                  # 0
        "State Guard Soldier",    # 1
        "State Guard Soldier",    # 2
        "State Guard Soldier",    # 3
        "State Guard Soldier",    # 4
        "2nd Lt. Noｱl",          # 5
        "Garcｵa",                # 6
        "Jailkeeper Melvin",      # 7
        "SE制御",                 # 8
        "BT6010",                 # 9
    ))

    ATBonus("ATBonus_334", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_414", 6, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_418", 10, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_41C", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_420", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_424", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_428", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_42C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_430", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_3F4", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_3F8", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_3FC", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_400", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_404", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_408", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_40C", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_410", 5, 5, 45)

    # monster count: 0

    # event battle count: 1

    BattleInfo(
        "BattleInfo_434", 0x004A, 3, 6, 45, 3, 3, 30, 0, "BT6010", 0x00000000, 100, 0, 0, 0,
        (
            ("ms41400.dat", "ms41500.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_414", "MonsterBattlePostion_3F4", "ed7540", "ed7453", "ATBonus_334"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "apl/ch51611.itc",                   # 00
        "chr/ch00000.itc",                   # 01
        "chr/ch00000.itc",                   # 02
        "chr/ch00000.itc",                   # 03
        "chr/ch00000.itc",                   # 04
        "chr/ch00000.itc",                   # 05
        "chr/ch00000.itc",                   # 06
        "chr/ch00000.itc",                   # 07
        "chr/ch00000.itc",                   # 08
        "chr/ch00000.itc",                   # 09
        "chr/ch00000.itc",                   # 0A
        "chr/ch00000.itc",                   # 0B
        "chr/ch00000.itc",                   # 0C
        "chr/ch00000.itc",                   # 0D
        "chr/ch00000.itc",                   # 0E
        "chr/ch00000.itc",                   # 0F
        "chr/ch00000.itc",                   # 10
        "chr/ch00000.itc",                   # 11
        "chr/ch00000.itc",                   # 12
        "chr/ch00000.itc",                   # 13
        "chr/ch00000.itc",                   # 14
        "chr/ch00000.itc",                   # 15
        "chr/ch00000.itc",                   # 16
        "chr/ch00000.itc",                   # 17
        "chr/ch00000.itc",                   # 18
        "chr/ch00000.itc",                   # 19
        "chr/ch00000.itc",                   # 1A
        "chr/ch00000.itc",                   # 1B
        "chr/ch00000.itc",                   # 1C
        "chr/ch00000.itc",                   # 1D
    ))

    DeclNpc(0,       0,       0,       0,    405,  0x0, 0,   0,   0,   255, 255, 0,   6,   255,  0)
    DeclNpc(0,       0,       0,       0,    405,  0x0, 0,   0,   0,   255, 255, 0,   6,   255,  0)
    DeclNpc(0,       0,       0,       0,    405,  0x0, 0,   0,   0,   255, 255, 0,   7,   255,  0)
    DeclNpc(0,       0,       0,       0,    405,  0x0, 0,   0,   0,   255, 255, 0,   7,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 27,  30.0,                  -1.0,                  -1.0,                  144.0,                 [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.125,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000001788139343,   0.0,                   -10.0,                 0.125,                 0.20000001788139343,   1.0])

    DeclActor(83000,   0,       38500,   1200,    83000,   1000,    38500,   0x007C, 0,  2,  0x0000)
    DeclActor(42500,   0,       41000,   1200,    42500,   1000,    41000,   0x007C, 0,  3,  0x0000)
    DeclActor(80000,   0,       4294949796, 1200,    80000,   1000,    4294949796, 0x007C, 0,  4,  0x0000)
    DeclActor(1000,    0,       4294962796, 1200,    1000,    1200,    4294963296, 0x007C, 0,  8,  0x0000)
    DeclActor(13000,   0,       2500,    1200,    13000,   1200,    1750,    0x007C, 0,  10, 0x0000)
    DeclActor(4294964776, 0,       38190,   1200,    4294964776, 1000,    38190,   0x007C, 0,  5,  0x0000)

    ChipFrameInfo(1308, 0)                                       # 0

    ScpFunction((
        "Function_0_51C",          # 00, 0
        "Function_1_540",          # 01, 1
        "Function_2_6D1",          # 02, 2
        "Function_3_7AB",          # 03, 3
        "Function_4_885",          # 04, 4
        "Function_5_95F",          # 05, 5
        "Function_6_9FF",          # 06, 6
        "Function_7_B55",          # 07, 7
        "Function_8_BE6",          # 08, 8
        "Function_9_DA6",          # 09, 9
        "Function_10_F1E",         # 0A, 10
        "Function_11_10BF",        # 0B, 11
        "Function_12_4964",        # 0C, 12
        "Function_13_4991",        # 0D, 13
        "Function_14_49B8",        # 0E, 14
        "Function_15_49EC",        # 0F, 15
        "Function_16_4A26",        # 10, 16
        "Function_17_4A68",        # 11, 17
        "Function_18_4AAE",        # 12, 18
        "Function_19_4AEA",        # 13, 19
        "Function_20_4B26",        # 14, 20
        "Function_21_4D2E",        # 15, 21
        "Function_22_4FA3",        # 16, 22
        "Function_23_4FC6",        # 17, 23
        "Function_24_502D",        # 18, 24
        "Function_25_5062",        # 19, 25
        "Function_26_50A0",        # 1A, 26
        "Function_27_50DE",        # 1B, 27
        "Function_28_5494",        # 1C, 28
        "Function_29_54E0",        # 1D, 29
        "Function_30_555D",        # 1E, 30
        "Function_31_594A",        # 1F, 31
        "Function_32_59B1",        # 20, 32
        "Function_33_686F",        # 21, 33
        "Function_34_690E",        # 22, 34
        "Function_35_6967",        # 23, 35
        "Function_36_69C0",        # 24, 36
        "Function_37_6A19",        # 25, 37
        "Function_38_6A72",        # 26, 38
        "Function_39_6ACB",        # 27, 39
        "Function_40_6B24",        # 28, 40
    ))


    def Function_0_51C(): pass

    label("Function_0_51C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_530")
    ClearScenarioFlags(0x22, 0)
    Event(0, 11)
    Jump("loc_53F")

    label("loc_530")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_53F")
    ClearScenarioFlags(0x22, 1)
    Event(0, 32)

    label("loc_53F")

    Return()

    # Function_0_51C end

    def Function_1_540(): pass

    label("Function_1_540")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x184, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_55C")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x21C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_56E")

    label("loc_55C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_56E")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x233), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_56E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_59F")
    OP_52(0x10B, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10B, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10B, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_59F")

    OP_52(0xD, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5D8")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_5D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x184, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_618")
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFrame(0xFF, "red00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "red01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "red02", 0x0, 0x1)
    Jump("loc_64B")

    label("loc_618")

    SetMapObjFlags(0x5, 0x4)
    SetMapObjFrame(0xFF, "green00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "green01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "green02", 0x0, 0x1)

    label("loc_64B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F6, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_65E")
    OP_70(0xB, 0x0)
    Jump("loc_662")

    label("loc_65E")

    OP_70(0xB, 0x1E)

    label("loc_662")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F6, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_675")
    OP_70(0xC, 0x0)
    Jump("loc_679")

    label("loc_675")

    OP_70(0xC, 0x1E)

    label("loc_679")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F6, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_68C")
    OP_70(0xD, 0x0)
    Jump("loc_690")

    label("loc_68C")

    OP_70(0xD, 0x1E)

    label("loc_690")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x184, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6A1")
    Call(0, 23)

    label("loc_6A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x184, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6B2")
    Call(0, 31)

    label("loc_6B2")

    OP_65(0x3, 0x1)
    OP_65(0x4, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x184, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6D0")
    OP_66(0x3, 0x1)
    OP_66(0x4, 0x1)

    label("loc_6D0")

    Return()

    # Function_1_540 end

    def Function_2_6D1(): pass

    label("Function_2_6D1")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F6, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_77B")
    Sound(14, 0, 100, 0)
    OP_74(0xB, 0x1E)
    OP_71(0xB, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    OP_70(0xB, 0x1E)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x20E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "x10 obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x20E, 10)
    SetMessageWindowPos(14, 280, 60, 3)
    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x1F6, 0)
    OP_E0(0x5, 0x0)
    Jump("loc_799")

    label("loc_77B")


    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The chest is empty.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_799")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_6D1 end

    def Function_3_7AB(): pass

    label("Function_3_7AB")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F6, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_855")
    Sound(14, 0, 100, 0)
    OP_74(0xC, 0x1E)
    OP_71(0xC, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    OP_70(0xC, 0x1E)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1FC),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x5 received.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x1FC, 5)
    SetMessageWindowPos(14, 280, 60, 3)
    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x1F6, 1)
    OP_E0(0x5, 0x0)
    Jump("loc_873")

    label("loc_855")


    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The chest is empty.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_873")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_7AB end

    def Function_4_885(): pass

    label("Function_4_885")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F6, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_92F")
    Sound(14, 0, 100, 0)
    OP_74(0xD, 0x1E)
    OP_71(0xD, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    OP_70(0xD, 0x1E)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x55),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x2 received.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x55, 2)
    SetMessageWindowPos(14, 280, 60, 3)
    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x1F6, 2)
    OP_E0(0x5, 0x0)
    Jump("loc_94D")

    label("loc_92F")


    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The chest is empty.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_94D")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_885 end

    def Function_5_95F(): pass

    label("Function_5_95F")

    OP_F4(0x3)
    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9E1")
    SoundLoad(13)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    Sound(13, 0, 100, 0)
    OP_0D()
    OP_32(0xFF, 0xFE, 0x0)
    OP_6A(0x0, 0x0)
    OP_31(0x1)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_9E1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9FD")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_9FD")

    Return()

    # Function_5_95F end

    def Function_6_9FF(): pass

    label("Function_6_9FF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B1E")

    ChrTalk(
        0xFE,
        "............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001F...He seems to have\x01",
            "completely lost\x01",
            "consciousness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10B,
        (
            "#11102FHehe, you say it like it's\x01",
            "someone else's business. We did\x01",
            "that with our own hands, no?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F...I know.\x02\x03",
            "#00001FI feel sorry for them,\x01",
            "but let's keep moving\x01",
            "forward.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_B51")

    label("loc_B1E")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The State Guard soldier\x01",
            "is out cold.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_B51")

    TalkEnd(0xFE)
    Return()

    # Function_6_9FF end

    def Function_7_B55(): pass

    label("Function_7_B55")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BAF")

    ChrTalk(
        0xFE,
        "............\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The State Guard soldier\x01",
            "is out cold.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x0, 1)
    Jump("loc_BE2")

    label("loc_BAF")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The State Guard soldier\x01",
            "is out cold.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_BE2")

    TalkEnd(0xFE)
    Return()

    # Function_7_B55 end

    def Function_8_BE6(): pass

    label("Function_8_BE6")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CD4")
    SetMessageWindowPos(160, 160, -1, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x193, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C12")
    SetChrName("Voice")
    Jump("loc_C21")

    label("loc_C12")

    SetChrName("Mafia's Voice")

    label("loc_C21")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "...Wasn't there some\x01",
            "kind of loud sound just\x01",
            "now?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetMessageWindowPos(160, 160, -1, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x193, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C87")
    SetChrName("Voice")
    Jump("loc_C96")

    label("loc_C87")

    SetChrName("Mafia's Voice")

    label("loc_C96")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Huh...? You must be\x01",
            "hearin' things.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_D95")

    label("loc_CD4")

    SetMessageWindowPos(160, 160, -1, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x193, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CF3")
    SetChrName("Voice")
    Jump("loc_D02")

    label("loc_CF3")

    SetChrName("Mafia's Voice")

    label("loc_D02")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "W-What's with this\x01",
            "ruckus...!?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetMessageWindowPos(160, 160, -1, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x193, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D55")
    SetChrName("Voice")
    Jump("loc_D64")

    label("loc_D55")

    SetChrName("Mafia's Voice")

    label("loc_D64")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Hey, did something\x01",
            "happen!?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_D95")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x193, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DA2")
    Call(0, 9)

    label("loc_DA2")

    TalkEnd(0xFF)
    Return()

    # Function_8_BE6 end

    def Function_9_DA6(): pass

    label("Function_9_DA6")


    ChrTalk(
        0x101,
        (
            "#00005F(What's this room\x01",
            "for...?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10B,
        (
            "#11100F(Revache's underlings are bein' kept all\x01",
            "together in this room and the one on the\x01",
            "other side.)\x02\x03",
            "#11103F(It seems they lack personnel. They\x01",
            "probably intend to guard all the\x01",
            "troublesome guys together on this floor.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(I see...)\x02\x03",
            "#00001F(...Anyway, let's hurry.\x01",
            "Let's break through before\x01",
            "reinforcements arrive.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x193, 0)
    Return()

    # Function_9_DA6 end

    def Function_10_F1E(): pass

    label("Function_10_F1E")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FF6")
    SetMessageWindowPos(120, 10, -1, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x193, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F4A")
    SetChrName("Voice")
    Jump("loc_F59")

    label("loc_F4A")

    SetChrName("Mafia's Voice")

    label("loc_F59")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I've heard a crazy sound\x01",
            "from the boss' room!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetMessageWindowPos(120, 10, -1, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x193, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FBB")
    SetChrName("Voice")
    Jump("loc_FCA")

    label("loc_FBB")

    SetChrName("Mafia's Voice")

    label("loc_FCA")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "You ok, boss...!?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_10AE")

    label("loc_FF6")

    SetMessageWindowPos(120, 10, -1, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x193, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1015")
    SetChrName("Voice")
    Jump("loc_1024")

    label("loc_1015")

    SetChrName("Mafia's Voice")

    label("loc_1024")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "A-And now the alarm\x01",
            "is...!?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetMessageWindowPos(120, 10, -1, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x193, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1074")
    SetChrName("Voice")
    Jump("loc_1083")

    label("loc_1074")

    SetChrName("Mafia's Voice")

    label("loc_1083")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Boss! You all right!?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_10AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x193, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10BB")
    Call(0, 9)

    label("loc_10BB")

    TalkEnd(0xFF)
    Return()

    # Function_10_F1E end

    def Function_11_10BF(): pass

    label("Function_11_10BF")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    AddParty(0xA, 0xFF, 0xFF)
    OP_52(0x10B, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10B, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10B, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_32(0xA, 0x0, 0x52)
    OP_32(0xA, 0x5, 0x64)
    OP_42(0xA, 0x46F, 0xFF)
    AddCraft(0xA, 0xFA)
    AddCraft(0xA, 0xFB)
    AddCraft(0xA, 0xFC)
    AddCraft(0xA, 0xFD)
    AddCraft(0xA, 0x14A)
    SetChrChipPat(0xA, 0x6, 0x14A)
    OP_32(0xFF, 0xFF, 0x0)
    LoadChrToIndex("chr/ch03900.itc", 0x1E)
    LoadChrToIndex("apl/ch51616.itc", 0x1F)
    LoadChrToIndex("chr/ch00002.itc", 0x21)
    LoadChrToIndex("apl/ch51606.itc", 0x22)
    LoadChrToIndex("chr/ch41450.itc", 0x23)
    LoadChrToIndex("chr/ch41451.itc", 0x24)
    LoadChrToIndex("chr/ch41452.itc", 0x25)
    LoadChrToIndex("chr/ch41453.itc", 0x26)
    LoadChrToIndex("apl/ch51608.itc", 0x27)
    LoadChrToIndex("apl/ch51609.itc", 0x28)
    LoadChrToIndex("chr/ch04156.itc", 0x29)
    LoadChrToIndex("apl/ch51605.itc", 0x2A)
    SoundLoad(4119)
    SoundLoad(3630)
    SoundLoad(3631)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis270.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis271.itp")
    CreatePortrait(2, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu11100.itp")
    LoadEffect(0x0, "event/ev16000.eff")
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x2A)
    SetChrSubChip(0x101, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrPos(0x101, -42100, 150, 38000, 90)
    SetChrFlags(0x10B, 0x2)
    SetChrChipByIndex(0x10B, 0x22)
    SetChrSubChip(0x10B, 0x0)
    SetChrFlags(0x10B, 0x4)
    SetChrPos(0x10B, 2100, 150, 37500, 270)
    SetChrFlags(0x10B, 0x8)
    SetChrChipByIndex(0xC, 0x1E)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, -121100, 0, 36000, 0)
    SetChrFlags(0xC, 0x8)
    SetChrChipByIndex(0x8, 0x1F)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, -5000, 0, -1000, 90)
    SetChrFlags(0x8, 0x40)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 33000, 0, -400, 270)
    SetChrFlags(0x9, 0x40)
    SetChrFlags(0x9, 0x8)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_12DF")
    Jump("loc_37AE")

    label("loc_12DF")

    BeginChrThread(0xF, 1, 0, 24)
    Sleep(3000)
    OP_68(27000, 1600, 0, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24000, 0)
    FadeToBright(1000, 0)
    OP_68(3000, 1600, 0, 10000)
    MoveCamera(60, 12, 0, 10000)
    OP_6E(400, 10000)
    SetCameraDistance(33000, 10000)

    def lambda_1352():
        OP_9B(0x0, 0xFE, 0x0, 0x88B8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1352)
    PlaceName2(340, 200, "c_plac70", 0x0, 3000)
    Sleep(9000)
    OP_0D()
    EndChrThread(0xF, 0x1)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-42100, 3000, 38000, 0)
    MoveCamera(270, 36, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14650, 0)
    FadeToBright(1000, 0)
    OP_68(-42100, 1000, 38000, 5000)
    MoveCamera(270, 27, 0, 5000)
    OP_6F(0x79)
    OP_0D()
    Sleep(500)
    OP_A1(0x101, 0x3E8, 0x2, 0x1, 0x2)
    Sleep(150)

    ChrTalk(
        0x101,
        "#00015F#5P#40W...............\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    Sleep(500)
    FadeToDark(2000, 0, -1)
    SetCameraDistance(14400, 2000)
    OP_6F(0x79)
    OP_0D()
    Sleep(500)
    SetChrPos(0x101, -122100, 150, 38000, 90)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x21)
    SetChrSubChip(0x101, 0x2)
    ClearChrFlags(0xC, 0x8)
    ClearMapObjFlags(0x9, 0x10)
    OP_70(0x9, 0xA)
    OP_7D(0xCF, 0xAE, 0x5D, 0x0, 0x0)
    OP_68(-121550, 1600, 37000, 0)
    MoveCamera(230, 24, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(19720, 0)
    PlayBGM("ed7534", 0)
    VolumeBGM(0x46, 0x64)
    FadeToBright(2500, 0)
    SetCameraDistance(20720, 2500)
    OP_6F(0x79)
    MoveCamera(226, 24, 0, 50000)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0xC,
        (
            "#10203F#5P─The other SSS members\x01",
            "are under our protection\x01",
            "elsewhere.\x02\x03",
            "#10208FI'm terribly sorry that\x01",
            "only you were locked up\x01",
            "here...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#11P...I don't mind.\x02\x03",
            "#00008FHowever, "protection"...\x01",
            "That's a funny way of\x01",
            "putting it, right?\x02\x03",
            "#00002FI wonder what you're...\x01",
            "protecting them from?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#10206F#5P............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#11P...Even you must've\x01",
            "realized it a long time\x01",
            "ago.\x02\x03",
            "#00008FThe true mastermind\x01",
            "behind the attack on\x01",
            "Crossbell City.\x02\x03",
            "#00013FAnd the one who hurt\x01",
            "Fran─ Your younger\x01",
            "sister.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0xC8)

    ChrTalk(
        0xC,
        "#10215F#5P#4SBut even so...!\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    ChrTalk(
        0xC,
        (
            "#10207F#5P...Even so, I'm a CGF member!\x02\x03",
            "Even after it changed its name to\x01",
            ""State Guard", I need only carry\x01",
            "out my duties as a soldier!\x02\x03",
            "#10208FIf I don't, Crossbell...\x02\x03",
            "#10206F...Crossbell will really end up\x01",
            "being crushed by the Empire and\x01",
            "the Republic!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#11PNoｱl...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#10206F#5PEven about KeA... I don't think\x01",
            "this is right!\x02\x03",
            "Even getting help from a\x01",
            "mysterious bunch like\x01",
            "Ouroboros...!\x02\x03",
            "#10210FBut─ The Imperial Army really\x01",
            "fired those dreadful Railway\x01",
            "Cannons!\x02\x03",
            "Those weapons of mass destruction\x01",
            "could've produced hundreds of\x01",
            "victims if they'd hit!\x02\x03",
            "#10215F...So that's why... That's why\x01",
            "there's no other way!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008F#11P...............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#10206F#5PI'm sorry...\x02\x03",
            "...I had no right to\x01",
            "tell you this.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xC, 0xB4, 0x1F4)
    Sleep(400)

    ChrTalk(
        0xC,
        (
            "#10208F#11P─I don't think you'll be\x01",
            "confined for so long.\x02\x03",
            "I'm sure that, after the\x01",
            "crisis in Crossbell has\x01",
            "passed, you'll be acquitted...\x02\x03",
            "#10203FSo, please... Please be\x01",
            "patient for now.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetCameraDistance(21220, 3000)
    BeginChrThread(0xC, 3, 0, 12)
    Sleep(1000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    EndChrThread(0xC, 0x3)
    SetChrFlags(0xC, 0x80)
    SetMapObjFlags(0x9, 0x10)
    OP_7D(0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x101, -42100, 150, 38000, 90)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x2A)
    SetChrSubChip(0x101, 0x0)
    OP_68(-42100, 1000, 38000, 0)
    MoveCamera(270, 27, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14400, 0)
    VolumeBGM(0x64, 0xBB8)
    FadeToBright(2000, 0)
    SetCameraDistance(14650, 2000)
    OP_6F(0x79)
    OP_0D()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    Sleep(500)
    OP_A1(0x101, 0x3E8, 0x2, 0xD, 0xE)

    ChrTalk(
        0x101,
        (
            "#00006F#5P#30W(...Back then... I had nothing good\x01",
            "to say back.)\x02\x03",
            "#00008F(And that's not all, either... I\x01",
            "never had the slightest notion that\x01",
            "KeA was worried about something...)\x02\x03",
            "(Being tossed about by busyness...\x01",
            "I failed to protect who I really\x01",
            "should have...)\x02\x03",
            "#00006F(...KeA's birth... The culprit who\x01",
            "killed my big brother...)\x02\x03",
            "#00015F(Even though I swore to myself I'd\x01",
            "discover them!)\x02",
        )
    )

    CloseMessageWindow()
    VolumeBGM(0x46, 0x3E8)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(300)
    OP_C9(0x0, 0x800)
    SetMessageWindowPos(250, 20, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#30WThen, was it you who\x01",
            "killed Guy Bannings─ my\x01",
            "big brother?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(110, 65, -1, -1)
    OP_C9(0x0, 0x80000000)

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#4119V#30WYes─ Exactly right.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0x1017)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x800)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(300)
    OP_C9(0x0, 0x800)
    SetMessageWindowPos(85, 110, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#3630V#30WI'm sorry. ...And thank\x01",
            "you for everything.\x02\x03",
            "#3631VI really do love you──\x01",
            "everyone.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xE2F)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x800)
    OP_C9(0x1, 0x80000000)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    VolumeBGM(0x64, 0x7D0)
    Sleep(500)
    OP_A1(0x101, 0x514, 0x4, 0x4, 0x5, 0x6, 0x7)

    ChrTalk(
        0x101,
        (
            "#00006F#5P#30W(Big brother... I'm\x01",
            "sorry...)\x02\x03",
            "(I knew it... It seems I\x01",
            "couldn't catch up with\x01",
            "you after all...)\x02\x03",
            "#00015F(What could I... What\x01",
            "should I do now...?)\x02\x03",
            "(...If only I knew...)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(2854, 255, 100, 0)
    Sleep(500)

    NpcTalk(
        0x10B,
        "Husky Voice",
        "#5P─How pathetic.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 1500, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Fade(500)
    OP_68(-1500, 1300, 38000, 0)
    OP_68(0, 1300, 38000, 2500)
    MoveCamera(49, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22500, 0)
    SetChrPos(0x101, -2100, 150, 38000, 90)
    SetChrSubChip(0x101, 0x8)
    ClearChrFlags(0x10B, 0x8)
    OP_6F(0x79)
    OP_0D()
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x10B,
        (
            "To think the leader who cornered\x01",
            "and arrested us is in such a sorry\x01",
            "state...\x02\x03",
            "After bein' locked up in a place\x01",
            "like this for half a year, you'll\x01",
            "be spoutin' nonsense like some has-\x02\x03",
            "been.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)
    OP_A1(0x101, 0x3E8, 0x2, 0x9, 0xA)
    Sleep(150)

    ChrTalk(
        0x101,
        (
            "#00006F#6P#30W...Leave me alone.\x02\x03",
            "No matter how I think about it,\x01",
            "you're here because you deserve\x01",
            "to be...\x02\x03",
            "But we were only able to arrest\x01",
            "you guys because we got lucky\x01",
            "several times in a row...\x02\x03",
            "#00008FThat's right... It wasn't a\x01",
            "Barrier we got over with our\x01",
            "own skills...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10B,
        "#11101F#11PTch, borin' kid.\x02",
    )

    CloseMessageWindow()
    OP_63(0x10B, 0xFFFFFF38, 2100, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x10B)
    Sleep(500)

    ChrTalk(
        0x10B,
        (
            "#11104F#11PWell, I can't blame you.\x02\x03",
            "Accordin' to rumors, things have gotten\x01",
            "crazy.\x02\x03",
            "#11101FThe IBC president was behind it all, and\x01",
            "now he's President of a dictatorship...\x02\x03",
            "You've made enemies of Red Constellation,\x01",
            "Ouroboros and even the State Guard and\x01",
            "that Divine Blade of Wind.\x02\x03",
            "#11102FHehe. Now that's some serious shit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#6P#30W............\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Sound(2852, 255, 100, 0)
    Sleep(500)
    OP_68(570, 1300, 37950, 1500)
    MoveCamera(51, 20, 0, 1500)
    Sound(898, 0, 100, 0)
    Sound(811, 0, 20, 0)
    OP_A1(0x10B, 0x4B0, 0x4, 0x1, 0x2, 0x3, 0x4)
    OP_6F(0x79)

    ChrTalk(
        0x10B,
        (
            "#11104F#5PWell for now, the right\x01",
            "choice is to wait for\x01",
            "the storm to pass.\x02\x03",
            "Only a true idiot would\x01",
            "try to fight back\x01",
            "against those odds.\x02\x03",
            "#11100F─Like your older brother\x01",
            "did, yeah?\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    OP_63(0x101, 0x12C, 1800, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_A1(0x101, 0x3E8, 0x2, 0xB, 0xC)

    ChrTalk(
        0x101,
        (
            "#00011F#6P#30W...Ah...\x02\x03",
            "#00001F#20WNow that you mention it,\x01",
            "did you know my brother?\x02",
        )
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7567", 0)
    SetCameraDistance(22000, 20000)

    ChrTalk(
        0x10B,
        (
            "#11100F#5PHmph. The closer you are to someone\x01",
            "the closer you have to watch them.\x02\x03",
            "#11103FNo matter how many times we threatened\x01",
            "him, he never learned and came\x01",
            "snooping around again...\x02\x03",
            "...Thinkin' about it, when we ran into\x01",
            "each other at food carts, he cooly\x01",
            "came to me recommendin' liquors...\x02\x03",
            "#11101FHe was a troublesome and annoyin'\x01",
            "youngster.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#6P#30WHaha... That sounds just\x01",
            "like him.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_A1(0x10B, 0x3E8, 0x2, 0x5, 0x6)
    Sleep(300)

    ChrTalk(
        0x10B,
        (
            "#11103F#5P...Well, I couldn't see a guy like\x01",
            "that dyin' even if we killed him, but\x01",
            "he gave up the ghost just like that.\x02\x03",
            "I don't get this world sometimes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008F#6P#30W...............\x02\x03",
            "#00001FDid my brother fight\x01",
            "against you guys that\x01",
            "entire time?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10B,
        (
            "#11104F#5PYeah. He stuck his nose into more than just\x01",
            "Revache, too.\x02\x03",
            "From big-shot corrupt congressmen to Imperial\x01",
            "and Republican intelligence activities, even\x01",
            "the actions of that Joachim...\x02\x03",
            "#11100FThere's no doubt he had amazing energy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#6P#30W...I see...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x12C, 1800, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    Sound(898, 0, 100, 0)
    Sound(802, 0, 50, 0)
    OP_A1(0x10B, 0x4B0, 0x5, 0x4, 0x3, 0x2, 0x1, 0x0)
    Sleep(150)

    ChrTalk(
        0x10B,
        (
            "#11103F#11P─Hey. Seems like you're\x01",
            "misunderstandin'\x01",
            "somethin'.\x02\x03",
            "#11101FGuy Bannings was in no\x01",
            "way an "amazing man",\x01",
            "you know?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x12C, 1800, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005F#6PHuh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10B,
        (
            "#11104F#11PIf we're talking quick-\x01",
            "wittedness and awesomeness,\x01",
            "MacLaine is better.\x02\x03",
            "For pinpointing enemy weaknesses\x01",
            "and makin' the necessary\x01",
            "preparations, Sergei is better.\x02\x03",
            "#11100FWhen it comes down to rational\x01",
            "judgment and management, Dudley\x01",
            "of Section One is better...\x02\x03",
            "In other words, those were his\x01",
            "limits.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00011F#6P...Well...\x02\x03",
            "#00008F(...Thinking about it\x01",
            "now, it really seems\x01",
            "true.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10B,
        (
            "#11103F#11PIf there was an area\x01",
            "where that guy wasn't\x01",
            "lacking...\x02\x03",
            "#11101FI guess it was "never\x01",
            "givin' up".\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x12C, 1800, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005F#6PAh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10B,
        (
            "#11100F#11PThat was probably\x01",
            "connected to his\x01",
            "impressive energy...\x02\x03",
            "It was probably also the\x01",
            "reason he was able to keep\x01",
            "after tough opponents.\x02\x03",
            "#11103FDespite all that, he was\x01",
            "narrow-minded and couldn't\x01",
            "see what was around him...\x02\x03",
            "#11101F..."What's wrong with this\x01",
            "youngster?"... That's what\x01",
            "I thought at the time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008F#6P............\x02",
    )

    CloseMessageWindow()
    VolumeBGM(0x46, 0x3E8)
    OP_CC(0x1, 0xFF, 0x0)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis000.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis008.itp")
    CreatePortrait(2, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis088.itp")
    CreatePortrait(4, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis091.itp")
    CreatePortrait(5, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis020.itp")
    CreatePortrait(6, 224, 0, 480, 256, 0, 16, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu07800.itp")
    FadeToDark(1000, 0, -1)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x3E8, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(500)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(300)
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    Sleep(300)
    OP_CB(0x4, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x4, 0x3)
    Sleep(300)
    OP_CB(0x5, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x5, 0x3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    OP_CB(0x3, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    OP_CB(0x4, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    Sleep(500)
    OP_CB(0x5, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x5, 0x3)
    OP_CB(0x6, 0x3, 0x99FFFFFF, 0x3E8, 0x0, 0x0)
    OP_CC(0x0, 0x6, 0x3)
    Sleep(500)
    OP_C9(0x0, 0x800)
    SetMessageWindowPos(45, 100, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xC),
            "#30W─Listen, Lloyd.\x02\x03",
            "If you're a man, throw\x01",
            "yourself at the things\x01",
            "in front of you.\x02\x03",
            "Grab with your hands\x01",
            "your only truth, the one\x01",
            "in your heart.\x02\x03",
            "If you do that, you'll\x01",
            "come to see what you\x01",
            "want to do.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x800)
    FadeToBright(1000, 0)
    OP_CB(0x6, 0x3, 0xFFFFFF, 0x3E8, 0x0, 0x0)
    OP_CC(0x0, 0x6, 0x3)
    VolumeBGM(0x64, 0x3E8)
    OP_63(0x101, 0x12C, 1800, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#00006F#6P...I think that maybe my big\x01",
            "brother's lack of giving up was to\x01",
            "protect the things important to him.\x02\x03",
            "#00008FNot only his family, but even\x01",
            "Crossbell City itself...\x02\x03",
            "#00000F...In that sense, maybe even Revache\x01",
            "was a target to protect.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x10B, 0xFFFFFF38, 2100, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x10B,
        "#11105F#11PWhat...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#6PHaha. It's presumptuous of me to\x01",
            "say "protect", but...\x02\x03",
            "#00008FI think maybe my big brother was\x01",
            "trying to see through the flow\x01",
            "that built the current Crossbell.\x02\x03",
            "#00004FIn addition, he was struggling to\x01",
            "protect Crossbell itself in his\x01",
            "own way...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10B,
        (
            "#11103F#11PHe...\x02\x03",
            "#11110F...Was the biggest fool\x01",
            "of them all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#6PYeah...\x02\x03",
            "#00008F...I can't possibly become\x01",
            "that big a fool...\x02\x03",
            "#00000F─However, because I'm his\x01",
            "younger brother, I resemble\x01",
            "him in some respects.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10B,
        "#11105F#11PWhat...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    Sound(812, 0, 100, 0)
    SetChrPos(0x101, -1600, 0, 38000, 90)
    ClearChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x101, 0x2)
    OP_0D()
    Sleep(300)
    OP_93(0x101, 0x0, 0x1F4)
    Sleep(900)
    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(500)
    OP_68(1500, 1100, 34500, 4000)
    MoveCamera(60, 18, 0, 4000)
    SetCameraDistance(24650, 4000)

    def lambda_34E0():
        OP_96(0xFE, 0x0, 0x0, 0x7918, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_34E0)
    Sleep(500)
    SetChrSubChip(0x10B, 0x7)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0xB4, 0x1F4)
    OP_6F(0x79)

    ChrTalk(
        0x10B,
        (
            "#11101F#5P...You... aren't\x01",
            "thinkin' of...\x02\x03",
            "You plannin' to escape?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x0, 0x1F4)
    Sleep(150)

    ChrTalk(
        0x101,
        (
            "#00003F#12PI'm not running away. I\x01",
            "want to go and discover\x01",
            "the truth.\x02\x03",
            "#00001FAs a detective assigned to\x01",
            "the Crossbell Police,\x01",
            "Special Support Section...\x02\x03",
            "To free my comrades who\x01",
            "were imprisoned, and even\x01",
            "to take back KeA.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x10B, 0xFFFFFF38, 2100, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x10B)

    ChrTalk(
        0x10B,
        (
            "#11104F#5PHehe... Haha...\x02\x03",
            "#11102FYou're quite the big\x01",
            "fool yourself, you know.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)
    Fade(250)
    Sound(812, 0, 100, 0)
    SetChrPos(0x10B, 1200, 0, 37500, 270)
    ClearChrFlags(0x10B, 0x4)
    SetChrChipByIndex(0x10B, 0xFF)
    SetChrSubChip(0x10B, 0x0)
    ClearChrFlags(0x10B, 0x2)
    OP_0D()
    Sleep(300)
    OP_93(0x10B, 0xB4, 0x1F4)

    ChrTalk(
        0x101,
        "#00005F#12PGarcｵa...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10B,
        (
            "#11103F#5P─Show me, kid.\x02\x03",
            "What a man like you can\x01",
            "accomplish in a\x01",
            "situation like this...\x02\x03",
            "#11102FShow me your resolve and\x01",
            "determination.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    SetCameraDistance(25650, 2000)
    OP_6F(0x79)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()

    label("loc_37AE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_37BE")
    Jump("loc_3DC8")

    label("loc_37BE")

    Sleep(1000)
    OP_68(28000, 1100, -1000, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(27500, 0)
    SetChrPos(0x8, 33000, 0, -1600, 270)
    ClearChrFlags(0x9, 0x8)

    def lambda_380A():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_380A)
    Sleep(50)

    def lambda_3822():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3822)
    FadeToBright(1000, 0)
    SetCameraDistance(25500, 2500)
    Sleep(2000)
    Sound(886, 0, 30, 0)
    Sleep(700)
    Sound(815, 0, 40, 0)
    Sleep(100)
    Sound(811, 0, 50, 0)
    WaitChrThread(0x8, 1)
    WaitChrThread(0x9, 1)

    ChrTalk(
        0x8,
        "#11PWhat the...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#5PFurther in, it seems...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    PlayBGM("ed7561", 0)
    BeginChrThread(0xF, 1, 0, 25)
    Fade(500)
    OP_68(2000, 1100, 1000, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25500, 0)
    OP_68(1000, 1100, 1000, 2000)
    SetChrPos(0x8, 7000, 0, -1600, 270)
    SetChrPos(0x9, 7000, 0, -400, 270)

    def lambda_3915():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3915)
    Sleep(50)

    def lambda_392D():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_392D)
    WaitChrThread(0x8, 1)

    def lambda_3946():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3946)
    WaitChrThread(0x9, 1)

    def lambda_3957():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3957)
    WaitChrThread(0x8, 1)
    WaitChrThread(0x9, 1)
    OP_6F(0x79)
    OP_0D()
    SetChrPos(0x101, 1000, 0, 2000, 180)
    SetChrPos(0x10B, 1000, 0, 2000, 180)
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0x10B, 0x8)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)

    NpcTalk(
        0x10B,
        "Garcｵa's Voice",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#3S#11PORAAAH! That's all you\x01",
            "have, you braaat!?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    NpcTalk(
        0x101,
        "Lloyd's Voice",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#1S#11P#50WUgh... *cough cough*...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#11PA fight... No, a\x01",
            "lynching?\x02",
        )
    )

    CloseMessageWindow()
    OP_9B(0x0, 0x9, 0x0, 0x5DC, 0x7D0, 0x0)
    EndChrThread(0xF, 0x1)
    Sound(100, 0, 50, 0)
    OP_71(0x8, 0x14, 0x19, 0x0, 0x8)
    OP_79(0x8)
    BeginChrThread(0xF, 1, 0, 26)
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x9,
        (
            "#11P#4SHey, stop! What the heck\x01",
            "are you doing!?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)

    NpcTalk(
        0x10B,
        "Garcｵa's Voice",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#4S#11PIt's your fault that\x01",
            "we've been in the\x01",
            "slammer!!\x02\x03",
            "#4SI'm gonna kill you!\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x101,
        "Lloyd's Voice",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#2S#11P#60W...Argh... Ugh...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Sound(100, 0, 50, 0)
    OP_71(0x8, 0x19, 0x14, 0x0, 0x8)
    OP_79(0x8)
    OP_9B(0x1, 0x9, 0x0, 0xFFFFFE0C, 0x7D0, 0x0)

    ChrTalk(
        0x9,
        (
            "#11P...It's no good. He\x01",
            "isn't listening.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x9, 0xB4, 0x1F4)

    ChrTalk(
        0x9,
        (
            "#5PIt can't be helped.\x01",
            "Let's go inside!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PYeah, stay on guard!\x02",
    )

    CloseMessageWindow()
    Fade(250)
    Sound(531, 0, 70, 0)
    SetChrChipByIndex(0x8, 0x23)
    SetChrSubChip(0x8, 0x0)
    SetChrChipByIndex(0x9, 0x23)
    SetChrSubChip(0x9, 0x0)
    OP_0D()
    SetChrChipByIndex(0x9, 0x24)
    SetChrSubChip(0x9, 0x0)
    OP_93(0x9, 0x5A, 0x1F4)
    OP_9B(0x0, 0x9, 0x0, 0x7D0, 0xFA0, 0x0)
    OP_93(0x9, 0x0, 0x1F4)
    SetChrChipByIndex(0x9, 0x23)
    SetChrSubChip(0x9, 0x0)
    Sleep(1)
    Fade(500)
    Sound(140, 0, 100, 0)
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFrame(0xFF, "red00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "red01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "red02", 0x0, 0x1)
    ClearMapObjFlags(0x5, 0x4)
    SetMapObjFrame(0xFF, "green00", 0x1, 0x1)
    SetMapObjFrame(0xFF, "green01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "green02", 0x1, 0x1)
    OP_0D()
    SetChrChipByIndex(0x8, 0x24)
    SetChrSubChip(0x8, 0x0)
    OP_9B(0x0, 0x8, 0x0, 0x7D0, 0xFA0, 0x0)
    SetChrChipByIndex(0x8, 0x23)
    SetChrSubChip(0x8, 0x0)
    Sound(105, 0, 100, 0)
    OP_71(0x5, 0x0, 0xA, 0x0, 0x8)
    OP_79(0x5)
    SetChrChipByIndex(0x8, 0x24)
    SetChrSubChip(0x8, 0x0)

    def lambda_3D4B():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3D4B)
    Sleep(100)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    SetChrChipByIndex(0x9, 0x24)
    SetChrSubChip(0x9, 0x0)
    OP_93(0x9, 0x10E, 0x1F4)
    OP_9B(0x0, 0x9, 0x0, 0x7D0, 0xFA0, 0x1)
    OP_93(0x9, 0x0, 0x1F4)

    def lambda_3D93():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3D93)
    Sleep(100)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    WaitChrThread(0x8, 1)
    WaitChrThread(0x9, 1)
    EndChrThread(0xF, 0x1)
    FadeToDark(1000, 0, -1)
    OP_0D()

    label("loc_3DC8")

    OP_68(3300, 1100, 35000, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21500, 0)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x27)
    SetChrSubChip(0x101, 0x0)
    SetChrFlags(0x101, 0x4)
    ClearChrFlags(0x101, 0x1)
    SetChrPos(0x101, 3300, 600, 35000, 270)
    ClearChrFlags(0x101, 0x8)
    BeginChrThread(0x101, 3, 0, 13)
    SetChrFlags(0x10B, 0x20)
    SetChrFlags(0x10B, 0x2)
    SetChrChipByIndex(0x10B, 0x28)
    SetChrSubChip(0x10B, 0x0)
    SetChrPos(0x10B, 2750, 0, 35000, 90)
    ClearChrFlags(0x10B, 0x8)
    SetChrChipByIndex(0x8, 0x24)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, 0, 0, 28000, 0)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x9, 0x24)
    SetChrSubChip(0x9, 0x0)
    SetChrPos(0x9, 0, 0, 28000, 0)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x9, 0x8)
    Sound(815, 0, 80, 0)
    Sleep(100)
    Sound(811, 0, 80, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(23500, 2000)
    OP_6F(0x79)
    OP_0D()
    Sleep(500)
    ClearMapObjFlags(0xA, 0x10)
    OP_70(0xA, 0xA)
    SetMapObjFlags(0xA, 0x1000)
    OP_68(1800, 1100, 33500, 2000)
    Sleep(300)
    BeginChrThread(0x8, 3, 0, 14)
    Sleep(700)
    BeginChrThread(0x9, 3, 0, 15)
    WaitChrThread(0x8, 3)
    WaitChrThread(0x9, 3)
    OP_6F(0x79)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x9,
        "#12P#4SStop, Garcｵa!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6PIf you keep it up, I'll\x01",
            "shoot!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x10B, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    EndChrThread(0x101, 0x3)
    BeginChrThread(0x101, 3, 0, 18)
    BeginChrThread(0x10B, 3, 0, 19)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x10B, 3)

    ChrTalk(
        0x10B,
        (
            "#11104F#5P#30WHehe... Haha...\x02\x03",
            "#11102F...It seems that I, of\x01",
            "all people, got too\x01",
            "carried away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#12PBastard...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6PJust when I thought you'd\x01",
            "been behaving yourself\x01",
            "since you got here...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6PThat's enough. Back\x01",
            "away, and hands up!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10B,
        "#11104F#5PHmph...\x02",
    )

    CloseMessageWindow()
    OP_9B(0x1, 0x10B, 0x0, 0xFFFFFC18, 0x3E8, 0x0)
    Sleep(100)
    Fade(150)
    Sound(812, 0, 100, 0)
    SetChrFlags(0x10B, 0x20)
    SetChrFlags(0x10B, 0x2)
    SetChrChipByIndex(0x10B, 0x28)
    OP_A1(0x10B, 0x4E2, 0x2, 0x1, 0x2)
    OP_0D()
    OP_68(3300, 1100, 35000, 1700)
    BeginChrThread(0x8, 3, 0, 16)
    BeginChrThread(0x9, 3, 0, 17)
    WaitChrThread(0x8, 3)
    WaitChrThread(0x9, 3)
    OP_6F(0x79)

    ChrTalk(
        0x9,
        (
            "#11PNo matter if we're shorthanded,\x01",
            "they shouldn't have been put in\x01",
            "the same cell...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11P─Hey, are you all right?\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    OP_A6(0x101, 0x0, 0x14, 0x190, 0x7D0)
    Sleep(300)

    ChrTalk(
        0x101,
        "#1S#60W#5P......uh...... ah......\x02",
    )

    CloseMessageWindow()
    Fade(100)
    PlayEffect(0x0, 0xFF, 0x101, 0x1, -400, 0, 100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)
    OP_0D()

    ChrTalk(
        0x101,
        "#5P#2S#40WGwah... *cough cough*!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PKh... Maybe his internal\x01",
            "organs have ruptured.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PAt any rate, let's call\x01",
            "a doct─\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    SetCameraDistance(22500, 1200)
    Sleep(300)
    OP_A1(0x101, 0x514, 0x6, 0x1, 0x2, 0x3, 0x2, 0x1, 0x2)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#5P─Nope, no need.\x02",
    )

    CloseMessageWindow()
    StopBGM(0x7D0)
    OP_63(0x9, 0xFFFFFED4, 1850, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Fade(250)
    OP_68(-77000, 1000, 35000, 0)
    MoveCamera(140, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(20500, 0)
    SetChrPos(0x101, -77000, 0, 35000, 180)
    SetChrPos(0x10B, -79500, 0, 35150, 90)
    SetChrPos(0x8, -80350, 0, 33500, 90)
    SetChrPos(0x9, -77000, 0, 33500, 0)
    SetChrSubChip(0x101, 0x4)
    SetChrSubChip(0x10B, 0x3)
    PlayEffect(0x0, 0xFF, 0x101, 0x1, -400, 0, 100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    BeginChrThread(0x101, 3, 0, 20)
    WaitChrThread(0x101, 3)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7540", 0)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x21C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(-78550, 1100, 34300, 1000)
    MoveCamera(157, 30, 0, 1000)
    SetCameraDistance(23500, 1000)
    OP_93(0x8, 0x2D, 0x1F4)
    Sound(531, 0, 70, 0)
    SetChrChipByIndex(0x8, 0x25)
    OP_A1(0x8, 0x7D0, 0x3, 0x0, 0x1, 0x2)
    OP_6F(0x79)

    ChrTalk(
        0x8,
        "#11PBastard─\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x10B, 3, 0, 21)
    WaitChrThread(0x10B, 3)
    Sleep(500)
    OP_68(-79350, 1800, 34650, 3000)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#00006F#5P*sigh*... I'm not sure\x01",
            "about this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10B,
        (
            "#11100F#5PHehe. You're saying that\x01",
            "now?\x02\x03",
            "#11104FWhen you suddenly said\x01",
            ""hit me", I thought\x01",
            "you'd gone crazy, but...\x02\x03",
            "#11102FAin't you quite the\x01",
            "schemer?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x10B, 500)
    Sleep(150)

    ChrTalk(
        0x101,
        (
            "#00006F#5PYou too. Your\x01",
            "performance was really\x01",
            "convincing.\x02\x03",
            "#00010FTch... Although I didn't\x01",
            "think you'd really break\x01",
            "one of my molars...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10B, 0x101, 500)

    ChrTalk(
        0x10B,
        (
            "#11100F#11PHmph. You're lucky it\x01",
            "ended with just that.\x02\x03",
            "#11103F...Like I promised, I'll\x01",
            "cooperate with you 'til\x01",
            "we get outside.\x02\x03",
            "#11101FSo, what's the plan?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#5PThis is the prison's 3F...\x01",
            "There shouldn't be many\x01",
            "soldiers around here.\x02\x03",
            "#00013FWe'll break through the\x01",
            "patrols somehow or other and\x01",
            "escape from the 1F exit!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10B,
        (
            "#11104F#11PHehe, very well.\x02\x03",
            "#11107FIt's been a while for me\x01",
            "too... I haven't gone\x01",
            "crazy in a long time!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    SetCameraDistance(23000, 1000)
    OP_6F(0x79)
    OP_0D()
    Sound(805, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd equipped some pipe\x01",
            "tonfas he improvised.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sound(814, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Garcｵa has joined the\x01",
            "party.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Because your ENIGMA II\x01",
            "was taken, arts cannot\x01",
            "be used.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Also, since all your\x01",
            "items were taken as well,\x01",
            "please watch your HP.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_BC(0x0)
    OP_42(0x0, 0x3F6, 0xFF)
    RemoveCraft(0x0, 0xFFFF)
    OP_DA(0x0)
    OP_42(0xA, 0x46F, 0xFF)
    RemoveCraft(0xA, 0xFFFF)
    AddItemNumber(0x1, 1)
    AddItemNumber(0x4, 1)
    OP_29(0xAE, 0x4, 0x2)
    OP_29(0xAE, 0x1, 0x0)
    OP_C9(0x0, 0x200000)
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x8000)
    ClearChrFlags(0x8, 0x40)
    ClearChrFlags(0x9, 0x40)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    Call(0, 23)
    SetMapObjFlags(0xA, 0x10)
    ClearMapObjFlags(0xA, 0x1000)
    OP_CC(0x1, 0xFF, 0x0)
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x21)
    OP_D7(0x22)
    OP_D7(0x23)
    OP_D7(0x24)
    OP_D7(0x25)
    OP_D7(0x26)
    OP_D7(0x27)
    OP_D7(0x28)
    OP_D7(0x29)
    OP_D7(0x2A)
    OP_37()
    SetChrPos(0x0, 0, 0, 33000, 180)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x183, 4)
    OP_C9(0x0, 0x8000)
    ModifyEventFlags(1, 0, 0x80)
    OP_C7(0x1, 0x4)
    OP_32(0x0, 0x11, 0x0)
    OP_32(0xA, 0x11, 0x0)
    OP_32(0xFF, 0xFE, 0x0)
    EventEnd(0x5)
    Return()

    # Function_11_10BF end

    def Function_12_4964(): pass

    label("Function_12_4964")


    def lambda_4969():
        OP_96(0xFE, 0xFFFE2B40, 0x0, 0x7148, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4969)
    Sleep(3000)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_12_4964 end

    def Function_13_4991(): pass

    label("Function_13_4991")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_49B7")
    OP_A6(0xFE, 0x0, 0x23, 0x1F4, 0x1388)
    Sleep(1000)
    Jump("Function_13_4991")

    label("loc_49B7")

    Return()

    # Function_13_4991 end

    def Function_14_49B8(): pass

    label("Function_14_49B8")


    def lambda_49BD():
        OP_9B(0x0, 0xFE, 0x0, 0xDAC, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_49BD)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    WaitChrThread(0xFE, 1)
    TurnDirection(0xFE, 0x10B, 500)
    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_14_49B8 end

    def Function_15_49EC(): pass

    label("Function_15_49EC")


    def lambda_49F1():
        OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_49F1)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    WaitChrThread(0xFE, 1)
    TurnDirection(0xFE, 0x10B, 500)
    Sound(531, 0, 70, 0)
    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_15_49EC end

    def Function_16_4A26(): pass

    label("Function_16_4A26")

    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)

    def lambda_4A3A():
        OP_9B(0x1, 0xFE, 0x0, 0x7D0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4A3A)
    WaitChrThread(0xFE, 1)

    def lambda_4A53():
        TurnDirection(0xFE, 0x10B, 500)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4A53)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_16_4A26 end

    def Function_17_4A68(): pass

    label("Function_17_4A68")

    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)
    OP_95(0xFE, 3300, 0, 33750, 3000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(100)
    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x0)
    Sleep(250)
    Fade(250)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x26)
    SetChrSubChip(0xFE, 0x2)
    OP_0D()
    Return()

    # Function_17_4A68 end

    def Function_18_4AAE(): pass

    label("Function_18_4AAE")

    Sound(802, 0, 100, 0)
    Sleep(150)

    def lambda_4ABC():
        OP_98(0xFE, 0x0, 0xFFFFFDA8, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4ABC)
    WaitChrThread(0xFE, 1)
    SetChrSubChip(0xFE, 0x2)
    Sound(811, 0, 100, 0)
    ClearChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x1)
    Return()

    # Function_18_4AAE end

    def Function_19_4AEA(): pass

    label("Function_19_4AEA")

    Fade(350)
    ClearChrFlags(0x10B, 0x20)
    ClearChrFlags(0x10B, 0x2)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    SetChrPos(0x10B, 2450, 0, 35000, 90)
    OP_0D()
    Sleep(300)
    OP_9B(0x1, 0xFE, 0x0, 0xFFFFFE3E, 0x3E8, 0x0)
    Return()

    # Function_19_4AEA end

    def Function_20_4B26(): pass

    label("Function_20_4B26")

    SetCameraDistance(19500, 500)
    Fade(250)
    Sound(802, 0, 100, 0)
    SetChrSubChip(0xFE, 0x5)
    OP_0D()
    Sleep(150)
    Sound(533, 0, 80, 0)
    Sound(2011, 255, 100, 0)
    SetChrSubChip(0xFE, 0x6)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_68(-77000, 1000, 31500, 500)
    MoveCamera(135, 25, 0, 500)
    SetCameraDistance(23500, 500)
    Sleep(1)
    CancelBlur(500)
    Sound(815, 0, 100, 0)
    OP_82(0xFA, 0x1F4, 0x2710, 0x1F4)

    ChrTalk(
        0x9,
        "#11PUrgh...\x05\x02",
    )

    PlayEffect(0x13, 0xFF, 0xFF, 0x0, -77000, 800, 34000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x12, 0xFF, 0xFF, 0x0, -77000, 800, 33500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrChip(0x0, 0x9, 0x5, 0x96)
    SetChrChipByIndex(0x9, 0x26)
    SetChrSubChip(0x9, 0x1)
    Sleep(100)
    SetChrFlags(0x9, 0x20)
    SetChrFlags(0x9, 0x1000)
    SetChrFlags(0x9, 0x4)
    SetChrFlags(0x9, 0x800)
    OP_52(0x9, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrSubChip(0x9, 0x0)
    OP_96(0x9, 0xFFFED338, 0x2EE, 0x7724, 0x2AF8, 0x0)
    Sound(862, 0, 100, 0)
    PlayEffect(0x13, 0xFF, 0xFF, 0x0, -77350, 1550, 30500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_A6(0x9, 0x0, 0x32, 0x1F4, 0x1388)
    SetChrChip(0x1, 0x9, 0x0, 0x0)
    SetChrSubChip(0x9, 0x1)

    def lambda_4CCC():
        OP_98(0xFE, 0x0, 0xFFFFFD12, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_4CCC)
    WaitChrThread(0x9, 1)
    OP_A1(0x9, 0x3E8, 0x2, 0x2, 0x3)
    ClearChrFlags(0x9, 0x20)
    ClearChrFlags(0x9, 0x1000)
    ClearChrFlags(0x9, 0x4)
    ClearChrFlags(0x9, 0x800)
    OP_52(0x9, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(250)
    Sound(514, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x20)
    ClearChrFlags(0xFE, 0x2)
    OP_0D()
    OP_6F(0x79)
    CloseMessageWindow()
    Return()

    # Function_20_4B26 end

    def Function_21_4D2E(): pass

    label("Function_21_4D2E")

    OP_68(-79500, 1500, 35150, 500)
    MoveCamera(157, 22, 0, 500)
    SetCameraDistance(18500, 500)
    Fade(250)

    def lambda_4D5D():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4D5D)
    Sleep(150)
    Sound(802, 0, 100, 0)
    ClearChrFlags(0x10B, 0x20)
    ClearChrFlags(0x10B, 0x2)
    SetChrChipByIndex(0xFE, 0x29)

    def lambda_4D81():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_4D81)
    OP_A1(0xFE, 0x3E8, 0x2, 0x0, 0x1)
    WaitChrThread(0x8, 2)
    WaitChrThread(0xFE, 2)
    OP_0D()
    OP_6F(0x79)
    Sound(2820, 255, 100, 0)

    ChrTalk(
        0x10B,
        "#11107F#4S#5PRaaah!\x05\x02",
    )

    Sound(534, 0, 100, 0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_68(-82180, 1800, 31820, 500)
    SetCameraDistance(23500, 500)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x2)

    def lambda_4DFA():
        OP_9B(0x1, 0xFE, 0x0, 0x4B0, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4DFA)
    Sleep(100)
    CancelBlur(500)
    Sound(815, 0, 100, 0)
    OP_82(0xFA, 0x1F4, 0x2710, 0x1F4)
    BeginChrThread(0xFE, 2, 0, 22)

    ChrTalk(
        0x8,
        "#11PArgh...!\x05\x02",
    )

    PlayEffect(0x13, 0xFF, 0xFF, 0x0, -80350, 800, 33500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x12, 0xFF, 0xFF, 0x0, -80350, 800, 33500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrChip(0x0, 0x8, 0x5, 0x96)
    SetChrChipByIndex(0x8, 0x26)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x1000)
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0x8, 0x800)
    OP_52(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_96(0x8, 0xFFFEBD8A, 0x5DC, 0x794A, 0x3A98, 0x0)
    Sound(862, 0, 100, 0)
    PlayEffect(0x13, 0xFF, 0xFF, 0x0, -82550, 2300, 31050, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_A6(0x8, 0x0, 0x32, 0x1F4, 0x1388)
    SetChrChip(0x1, 0x8, 0x0, 0x0)
    SetChrSubChip(0x8, 0x1)

    def lambda_4F53():
        OP_98(0xFE, 0x0, 0xFFFFFA24, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_4F53)
    WaitChrThread(0x8, 1)
    Sound(514, 0, 100, 0)
    OP_A1(0x8, 0x3E8, 0x2, 0x2, 0x3)
    ClearChrFlags(0x8, 0x20)
    ClearChrFlags(0x8, 0x1000)
    ClearChrFlags(0x8, 0x4)
    ClearChrFlags(0x8, 0x800)
    OP_52(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    CloseMessageWindow()
    Return()

    # Function_21_4D2E end

    def Function_22_4FA3(): pass

    label("Function_22_4FA3")

    Sleep(500)
    SetChrSubChip(0xFE, 0x3)
    Sleep(125)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x20)
    ClearChrFlags(0xFE, 0x1000)
    Return()

    # Function_22_4FA3 end

    def Function_23_4FC6(): pass

    label("Function_23_4FC6")

    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    OP_52(0x8, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x8, 0x40)
    ClearChrFlags(0x8, 0x1)
    SetChrPos(0x8, -3050, 0, 31450, 45)
    SetChrChipByIndex(0x9, 0x0)
    SetChrSubChip(0x9, 0x2)
    ClearChrFlags(0x9, 0x80)
    OP_52(0x9, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x9, 0x40)
    ClearChrFlags(0x9, 0x1)
    SetChrPos(0x9, 2650, 0, 33000, 0)
    Return()

    # Function_23_4FC6 end

    def Function_24_502D(): pass

    label("Function_24_502D")

    Sound(882, 0, 100, 0)
    Sleep(2600)
    Sound(882, 0, 80, 0)

    label("loc_503C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5061")
    Sleep(3800)
    Sound(882, 0, 40, 0)
    Sleep(2200)
    Sound(882, 0, 40, 0)
    Sleep(500)
    Jump("loc_503C")

    label("loc_5061")

    Return()

    # Function_24_502D end

    def Function_25_5062(): pass

    label("Function_25_5062")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_509F")
    Sound(815, 0, 40, 0)
    Sleep(100)
    Sound(811, 0, 40, 0)
    Sleep(600)
    Sound(886, 0, 40, 0)
    Sleep(700)
    Sound(862, 0, 30, 0)
    Sleep(100)
    Sound(815, 0, 30, 0)
    Sleep(700)
    Jump("Function_25_5062")

    label("loc_509F")

    Return()

    # Function_25_5062 end

    def Function_26_50A0(): pass

    label("Function_26_50A0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_50DD")
    Sound(815, 0, 60, 0)
    Sleep(100)
    Sound(811, 0, 60, 0)
    Sleep(600)
    Sound(886, 0, 50, 0)
    Sleep(700)
    Sound(862, 0, 50, 0)
    Sleep(100)
    Sound(815, 0, 40, 0)
    Sleep(700)
    Jump("Function_26_50A0")

    label("loc_50DD")

    Return()

    # Function_26_50A0 end

    def Function_27_50DE(): pass

    label("Function_27_50DE")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    LoadChrToIndex("apl/ch51616.itc", 0x1E)
    LoadChrToIndex("apl/ch51617.itc", 0x1F)
    LoadChrToIndex("chr/ch00051.itc", 0x20)
    LoadChrToIndex("chr/ch04151.itc", 0x21)
    SetChrPos(0x101, 27600, 0, -1600, 90)
    SetChrPos(0x10B, 27400, 0, -400, 90)
    SetChrChipByIndex(0xA, 0x1E)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 38500, 0, -7000, 270)
    SetChrFlags(0xA, 0x40)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0xB, 0x1F)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, 38500, 0, -7000, 270)
    SetChrFlags(0xB, 0x40)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetMapObjFlags(0x2, 0x1000)
    ClearMapObjFlags(0x2, 0x10)
    OP_70(0x2, 0x0)
    OP_68(27500, 1000, -1000, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(26500, 0)
    SetCameraDistance(25500, 1000)
    FadeToBright(1000, 0)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x10B, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(38000, 1000, -7000, 3000)
    MoveCamera(60, 26, 0, 3000)
    OP_6E(400, 3000)
    SetCameraDistance(25500, 3000)
    OP_6F(0x79)
    SetChrPos(0x101, 24500, 0, -1700, 90)
    SetChrPos(0x10B, 24500, 0, -300, 90)
    SetChrChipByIndex(0x101, 0x20)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x10B, 0x21)
    SetChrSubChip(0x10B, 0x0)
    Sleep(500)
    Sound(103, 0, 100, 0)
    OP_71(0x2, 0x0, 0x5, 0x0, 0x8)
    OP_79(0x2)
    Sleep(500)
    BeginChrThread(0xA, 3, 0, 28)
    BeginChrThread(0xB, 3, 0, 29)
    OP_68(34500, 1000, -7000, 3000)
    MoveCamera(45, 23, 0, 3000)
    Sleep(500)

    ChrTalk(
        0xA,
        (
            "...What the heck are\x01",
            "they doing?\x05\x02",
        )
    )

    OP_6F(0x79)
    OP_68(34500, 1000, -1000, 4000)

    ChrTalk(
        0xB,
        (
            "#11PI just wanna do the\x01",
            "shift change and go\x01",
            "home...\x05\x02",
        )
    )

    WaitChrThread(0xA, 3)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xA,
        "#5PHuh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#11PYou!\x02",
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(25500, 1000, -1000, 0)
    MoveCamera(45, 23, 0, 0)
    SetCameraDistance(33500, 0)
    OP_68(34500, 1000, -1000, 1500)
    SetCameraDistance(25500, 1500)
    SetChrFlags(0x101, 0x1000)
    SetChrFlags(0x10B, 0x1000)

    def lambda_53EB():
        OP_9B(0x0, 0xFE, 0x0, 0x2134, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_53EB)

    def lambda_5400():
        OP_9B(0x0, 0xFE, 0x0, 0x2134, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x10B, 1, lambda_5400)

    ChrTalk(
        0x10B,
        "#11107F#5PToo slow!\x05\x02",
    )


    ChrTalk(
        0x101,
        "#00007F#6P#NLet's do this!\x05\x02",
    )

    Sleep(1000)
    SetCameraDistance(23500, 500)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    Sleep(500)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x10B, 0x1)
    ClearChrFlags(0x101, 0x1000)
    ClearChrFlags(0x10B, 0x1000)
    Battle("BattleInfo_434", 0x0, 0x2, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    Call(0, 30)
    Return()

    # Function_27_50DE end

    def Function_28_5494(): pass

    label("Function_28_5494")


    def lambda_5499():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5499)
    OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Sleep(800)
    OP_93(0xFE, 0x0, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x1964, 0x7D0, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_28_5494 end

    def Function_29_54E0(): pass

    label("Function_29_54E0")

    Sleep(1000)

    def lambda_54E8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_54E8)
    OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Sleep(300)
    Sound(104, 0, 100, 0)
    OP_71(0x2, 0x5, 0x0, 0x0, 0x8)
    OP_79(0x2)
    Sleep(200)
    OP_93(0xFE, 0x10E, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x8CA, 0x7D0, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_29_54E0 end

    def Function_30_555D(): pass

    label("Function_30_555D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch41453.itc", 0x1E)
    LoadChrToIndex("chr/ch41553.itc", 0x1F)
    LoadChrToIndex("chr/ch00050.itc", 0x20)
    LoadChrToIndex("chr/ch04150.itc", 0x21)
    SoundLoad(907)
    SetChrPos(0x101, 32500, 0, -1800, 90)
    SetChrPos(0x10B, 32500, 0, -200, 90)
    SetChrChipByIndex(0x101, 0x20)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x10B, 0x21)
    SetChrSubChip(0x10B, 0x0)
    SetChrChipByIndex(0xA, 0x1E)
    SetChrSubChip(0xA, 0x3)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 35500, 0, 0, 270)
    SetChrChipByIndex(0xB, 0x1F)
    SetChrSubChip(0xB, 0x3)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, 35000, 0, -1600, 270)
    OP_68(34500, 1000, -1000, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24860, 0)
    SetCameraDistance(23860, 1500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0xA,
        "#5P#30WUgh... Damn you...\x02",
    )

    CloseMessageWindow()

    def lambda_5663():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_5663)
    Sleep(150)
    Fade(250)
    Sound(514, 0, 100, 0)
    SetChrChipByIndex(0xA, 0x0)
    SetChrSubChip(0xA, 0x2)
    ClearChrFlags(0xA, 0x1)
    OP_0D()
    WaitChrThread(0xA, 2)

    ChrTalk(
        0xB,
        (
            "#11P#30WA-As if I'd let you\x01",
            "escape...\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(25500, 1000)

    def lambda_56D0():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_56D0)
    Sleep(150)
    Fade(250)
    Sound(802, 0, 100, 0)
    SetChrSubChip(0xB, 0x2)
    OP_0D()
    WaitChrThread(0xB, 2)
    Sleep(500)

    def lambda_5703():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_5703)
    Sleep(150)
    Fade(250)
    Sound(804, 0, 100, 0)
    OP_0D()
    WaitChrThread(0xB, 2)

    def lambda_572F():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_572F)
    Sleep(150)
    Fade(250)
    Sound(514, 0, 100, 0)
    SetChrChipByIndex(0xB, 0x0)
    SetChrSubChip(0xB, 0x1)
    SetChrPos(0xB, 35000, 0, -1600, 90)
    ClearChrFlags(0xB, 0x1)
    OP_0D()
    WaitChrThread(0xB, 2)
    OP_6F(0x79)
    Sleep(500)
    Sound(907, 2, 100, 0)
    Sleep(800)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x10B, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00010F#6PUgh, the emergency\x01",
            "warning system that uses\x01",
            "the ENIGMA was...!\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0x10B, 0xFF)
    SetChrSubChip(0x10B, 0x0)
    OP_0D()
    TurnDirection(0x10B, 0x101, 500)

    ChrTalk(
        0x10B,
        (
            "#11104F#5PHehe... Well then, what\x01",
            "to do?\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    OP_0D()
    TurnDirection(0x101, 0x10B, 500)

    ChrTalk(
        0x101,
        (
            "#00007F#12PThis was within\x01",
            "expectations... Let's keep\x01",
            "forcing our way through!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10B,
        "#11102F#5PHaha, fine by me!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopSound(907, 2000, 100)
    ClearChrFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x8000)
    ClearChrFlags(0xA, 0x40)
    ClearChrFlags(0xB, 0x40)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    Call(0, 31)
    ClearMapObjFlags(0x2, 0x1000)
    SetMapObjFlags(0x2, 0x10)
    OP_70(0x2, 0x0)
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    OP_37()
    SetChrPos(0x0, 32500, 0, -1000, 90)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x183, 5)
    ModifyEventFlags(0, 0, 0x80)
    EventEnd(0x5)
    Return()

    # Function_30_555D end

    def Function_31_594A(): pass

    label("Function_31_594A")

    SetChrChipByIndex(0xA, 0x0)
    SetChrSubChip(0xA, 0x2)
    ClearChrFlags(0xA, 0x80)
    OP_52(0xA, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xA, 0x40)
    ClearChrFlags(0xA, 0x1)
    SetChrPos(0xA, 35500, 0, 0, 270)
    SetChrChipByIndex(0xB, 0x0)
    SetChrSubChip(0xB, 0x1)
    ClearChrFlags(0xB, 0x80)
    OP_52(0xB, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xB, 0x40)
    ClearChrFlags(0xB, 0x1)
    SetChrPos(0xB, 35000, 0, -1600, 90)
    Return()

    # Function_31_594A end

    def Function_32_59B1(): pass

    label("Function_32_59B1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch30000.itc", 0x1E)
    LoadChrToIndex("apl/ch51606.itc", 0x1F)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFrame(0xFF, "green00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "green01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "green02", 0x0, 0x1)
    SetChrChipByIndex(0xE, 0x1E)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)
    SetChrPos(0xE, 1000, 150, 1000, 180)
    OP_68(610, 1000, -310, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25500, 0)
    SetChrPos(0x101, 400, 0, -800, 0)
    SetChrPos(0x102, 1600, 0, -800, 0)
    SetChrPos(0x103, 300, 0, -2000, 0)
    SetChrPos(0x104, 1700, 0, -2000, 0)
    SetChrPos(0xF4, 200, 0, -3200, 0)
    SetChrPos(0xF5, 1800, 0, -3200, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0xE,
        (
            "...Your visitation time\x01",
            "is 10 minutes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Since the prisoner is wounded,\x01",
            "you will be allowed inside his\x01",
            "cell as a special measure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "However, you may not give\x01",
            "the prisoner anything or\x01",
            "cause a disturbance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FAlright, understood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Uhm, then...\x02",
    )

    CloseMessageWindow()
    OP_93(0xE, 0x0, 0x1F4)

    ChrTalk(
        0xE,
        "#11P─Garcｵa, visitors!\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(120, 10, -1, -1)
    SetChrName("Garcｵa's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "...All right, come in.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_93(0xE, 0x5A, 0x1F4)
    OP_9B(0x0, 0xE, 0x0, 0x7D0, 0x7D0, 0x0)
    OP_93(0xE, 0x0, 0x1F4)
    Sleep(1000)
    Fade(500)
    Sound(140, 0, 100, 0)
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFrame(0xFF, "red00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "red01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "red02", 0x0, 0x1)
    ClearMapObjFlags(0x5, 0x4)
    SetMapObjFrame(0xFF, "green00", 0x1, 0x1)
    SetMapObjFrame(0xFF, "green01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "green02", 0x1, 0x1)
    OP_0D()
    OP_93(0xE, 0x10E, 0x1F4)
    OP_9B(0x0, 0xE, 0x0, 0x7D0, 0x7D0, 0x0)
    OP_93(0xE, 0x0, 0x1F4)
    Sleep(1000)
    Sound(105, 0, 100, 0)
    OP_71(0x5, 0x0, 0xA, 0x0, 0x8)
    OP_79(0x5)

    def lambda_5D0E():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_5D0E)
    Sleep(100)
    OP_A7(0xE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    BeginChrThread(0x101, 3, 0, 40)
    Sleep(750)
    BeginChrThread(0x102, 3, 0, 40)
    Sleep(250)
    BeginChrThread(0x103, 3, 0, 40)
    Sleep(750)
    BeginChrThread(0x104, 3, 0, 40)
    Sleep(250)
    BeginChrThread(0xF4, 3, 0, 40)
    Sleep(750)
    BeginChrThread(0xF5, 3, 0, 40)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x102, 0xFF)
    EndChrThread(0x103, 0xFF)
    EndChrThread(0x104, 0xFF)
    EndChrThread(0xF4, 0xFF)
    EndChrThread(0xF5, 0xFF)
    SetChrChipByIndex(0xD, 0x1F)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0xD, 0x40)
    SetChrFlags(0xD, 0x20)
    SetChrFlags(0xD, 0x10)
    SetChrFlags(0xD, 0x2)
    SetChrPos(0xD, 2100, 150, 38000, 270)
    OP_68(-540, 1000, 34330, 0)
    MoveCamera(41, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(26500, 0)
    OP_A7(0xE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xF4, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xF5, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xE, 0, 0, 27000, 0)
    SetChrPos(0x101, 0, 0, 27000, 0)
    SetChrPos(0x102, 0, 0, 27000, 0)
    SetChrPos(0x103, 0, 0, 27000, 0)
    SetChrPos(0x104, 0, 0, 27000, 0)
    SetChrPos(0xF4, 0, 0, 27000, 0)
    SetChrPos(0xF5, 0, 0, 27000, 0)
    FadeToBright(1000, 0)
    OP_0D()
    BeginChrThread(0xE, 3, 0, 33)
    Sleep(1000)
    BeginChrThread(0x104, 3, 0, 34)
    Sleep(1000)
    BeginChrThread(0x102, 3, 0, 35)
    Sleep(1000)
    BeginChrThread(0xF4, 3, 0, 36)
    Sleep(1000)
    BeginChrThread(0x101, 3, 0, 37)
    Sleep(750)
    BeginChrThread(0x103, 3, 0, 38)
    Sleep(750)
    BeginChrThread(0xF5, 3, 0, 39)
    Sleep(2000)
    OP_68(810, 800, 39690, 6000)
    OP_6F(0x79)
    WaitChrThread(0xE, 3)
    WaitChrThread(0x104, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0xF4, 3)
    WaitChrThread(0xF5, 3)

    ChrTalk(
        0x101,
        "#6P#00000FGarcｵa...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11100FHeh, we meet again, kid.\x02\x03",
            "#11104FI'm glad you reunited\x01",
            "with your friends.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00305FHey there, ol' man. You're\x01",
            "already up?\x02\x03",
            "#00303FI've heard you were quite\x01",
            "exhausted after going all\x01",
            "out against the State Guard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11103FHmph, not fine as you would've been.\x01",
            "After all, I fought against their\x01",
            "rifles and halberds with my bare hands.\x02\x03",
            "#11101FIt's pathetic, but... I only woke up\x01",
            "just now.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6136")

    ChrTalk(
        0x10A,
        (
            "#6P#00600FHmph, considering the\x01",
            "circumstances, you make\x01",
            "it look easy.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_61E9")

    label("loc_6136")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6192")

    ChrTalk(
        0x109,
        (
            "#6P#10102FC-Considering the\x01",
            "circumstances, you make\x01",
            "it look easy.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_61E9")

    label("loc_6192")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_61E9")

    ChrTalk(
        0x106,
        (
            "#6P#10701FConsidering the\x01",
            "circumstances, you make\x01",
            "it look easy...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_61E9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6240")

    ChrTalk(
        0x105,
        (
            "#6P#10402FHehe, as expected of the\x01",
            "Killing Bear's\x01",
            "abilities.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_62F4")

    label("loc_6240")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_62A4")

    ChrTalk(
        0x106,
        (
            "#6P#10703FI should expect as much\x01",
            "from the Zephyr\x01",
            "Brigade's Killing Bear.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_62F4")

    label("loc_62A4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_62F4")

    ChrTalk(
        0x109,
        (
            "#6P#10106FShould I say that's\x01",
            "expected of a former\x01",
            "jaeger?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_62F4")


    ChrTalk(
        0x103,
        (
            "#6P#00200FWell, for right now, it\x01",
            "seems you can't move...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#6P#00001F...Garcｵa, words aren't\x01",
            "enough to thank you.\x02\x03",
            "#00003FIf you hadn't helped me\x01",
            "escape from prison back\x01",
            "then...\x02\x03",
            "#00000FI'm sure I wouldn't have\x01",
            "been able to reunite with my\x01",
            "friends or make it this far.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00102FLloyd...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11101F...Hah! Did you come here just to\x01",
            "tell me that?\x02\x03",
            "#11103FOur collusion ended the moment we\x01",
            "got outside the prison gate.\x02\x03",
            "#11102FTo me, you're the nasty bastard\x01",
            "who destroyed Revache... That\x01",
            "hasn't changed even now, you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00004F...Even so, I want to thank\x01",
            "you.\x02\x03",
            "#00000FThank you, Garcｵa. It's thanks\x01",
            "to you that I can be here like\x01",
            "this.\x02\x03",
            "#00000FI'll show you. I'll discover\x01",
            "the truth of the current\x01",
            "incident and protect Crossbell.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xD)

    ChrTalk(
        0xD,
        (
            "#11103FTch... You made me remember something\x01",
            "disgusting.\x02\x03",
            "The eyes of that shockingly persistent\x01",
            "bastard who stood his ground without\x01",
            ""givin' up" no matter the circumstances\x01",
            "and the many times he was beaten.\x02\x03",
            "#11102FBannings... You sure are Guy's younger\x01",
            "brother.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00305FOl' man...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00004F... Haha, thank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11103FTch. It seems I've said\x01",
            "something that's not my\x01",
            "style.\x02\x03",
            "#11101FYou don't have the time to\x01",
            "stay in a place like this\x01",
            "leisurely chatting, right?\x02\x03",
            "#11103F...Beat it, kid.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00004F...Yeah, I hear you.\x02\x03",
            "#00000FEveryone, let's go.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 1)
    NewScene("t6000", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_32_59B1 end

    def Function_33_686F(): pass

    label("Function_33_686F")


    def lambda_6874():
        OP_95(0xFE, 0, 0, 29000, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6874)

    def lambda_688E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_688E)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_68A7():
        OP_95(0xFE, 0, 0, 31000, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_68A7)
    WaitChrThread(0xFE, 1)

    def lambda_68C5():
        OP_95(0xFE, 2000, 0, 31000, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_68C5)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(5000)

    def lambda_68ED():
        OP_95(0xFE, 0, 0, 31000, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_68ED)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_33_686F end

    def Function_34_690E(): pass

    label("Function_34_690E")


    def lambda_6913():
        OP_95(0xFE, 0, 0, 29000, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6913)

    def lambda_692D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_692D)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_6946():
        OP_95(0xFE, -1370, 0, 39290, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6946)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_34_690E end

    def Function_35_6967(): pass

    label("Function_35_6967")


    def lambda_696C():
        OP_95(0xFE, 0, 0, 29000, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_696C)

    def lambda_6986():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6986)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_699F():
        OP_95(0xFE, -160, 0, 39190, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_699F)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_35_6967 end

    def Function_36_69C0(): pass

    label("Function_36_69C0")


    def lambda_69C5():
        OP_95(0xFE, 0, 0, 29000, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_69C5)

    def lambda_69DF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_69DF)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_69F8():
        OP_95(0xFE, -1240, 0, 38210, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_69F8)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_36_69C0 end

    def Function_37_6A19(): pass

    label("Function_37_6A19")


    def lambda_6A1E():
        OP_95(0xFE, 0, 0, 29000, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6A1E)

    def lambda_6A38():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6A38)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_6A51():
        OP_95(0xFE, 0, 0, 38000, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6A51)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_37_6A19 end

    def Function_38_6A72(): pass

    label("Function_38_6A72")


    def lambda_6A77():
        OP_95(0xFE, 0, 0, 29000, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6A77)

    def lambda_6A91():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6A91)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_6AAA():
        OP_95(0xFE, -300, 0, 36920, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6AAA)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_38_6A72 end

    def Function_39_6ACB(): pass

    label("Function_39_6ACB")


    def lambda_6AD0():
        OP_95(0xFE, 0, 0, 29000, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6AD0)

    def lambda_6AEA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6AEA)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_6B03():
        OP_95(0xFE, -1470, 0, 36720, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6B03)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_39_6ACB end

    def Function_40_6B24(): pass

    label("Function_40_6B24")

    OP_96(0xFE, 0x3E8, 0x96, 0x3E8, 0x7D0, 0x0)

    def lambda_6B3D():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6B3D)
    Sleep(100)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    Return()

    # Function_40_6B24 end

    SaveToFile()

Try(main)
