from ScenarioHelper import *

def main():
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
        "Defense Forces soldier",             # 1
        "Defense Forces soldier",             # 2
        "Defense Forces soldier",             # 3
        "Defense Forces soldier",             # 4
        "Lieutenant Noel",             # 5
        "Garcia",               # 6
        "Nursery Melvin",           # 7
        "SE control",                 # 8
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
        "Function_3_7B9",          # 03, 3
        "Function_4_89F",          # 04, 4
        "Function_5_985",          # 05, 5
        "Function_6_A2A",          # 06, 6
        "Function_7_B52",          # 07, 7
        "Function_8_BDF",          # 08, 8
        "Function_9_D7D",          # 09, 9
        "Function_10_EDF",         # 0A, 10
        "Function_11_107C",        # 0B, 11
        "Function_12_45C3",        # 0C, 12
        "Function_13_45F0",        # 0D, 13
        "Function_14_4617",        # 0E, 14
        "Function_15_464B",        # 0F, 15
        "Function_16_4685",        # 10, 16
        "Function_17_46C7",        # 11, 17
        "Function_18_470D",        # 12, 18
        "Function_19_4749",        # 13, 19
        "Function_20_4785",        # 14, 20
        "Function_21_4990",        # 15, 21
        "Function_22_4C0D",        # 16, 22
        "Function_23_4C30",        # 17, 23
        "Function_24_4C97",        # 18, 24
        "Function_25_4CCC",        # 19, 25
        "Function_26_4D0A",        # 1A, 26
        "Function_27_4D48",        # 1B, 27
        "Function_28_5104",        # 1C, 28
        "Function_29_5150",        # 1D, 29
        "Function_30_51CD",        # 1E, 30
        "Function_31_5582",        # 1F, 31
        "Function_32_55E9",        # 20, 32
        "Function_33_6417",        # 21, 33
        "Function_34_64B6",        # 22, 34
        "Function_35_650F",        # 23, 35
        "Function_36_6568",        # 24, 36
        "Function_37_65C1",        # 25, 37
        "Function_38_661A",        # 26, 38
        "Function_39_6673",        # 27, 39
        "Function_40_66CC",        # 28, 40
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F6, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_782")
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
            scpstr(SCPSTR_CODE_ITEM, '战斗探测器'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got ten pieces.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('战斗探测器', 10)
    SetMessageWindowPos(14, 280, 60, 3)
    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x1F6, 0)
    OP_E0(0x5, 0x0)
    Jump("loc_7A7")

    label("loc_782")


    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is nothing in the treasure box.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_7A7")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_6D1 end

    def Function_3_7B9(): pass

    label("Function_3_7B9")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F6, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_868")
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
            scpstr(SCPSTR_CODE_ITEM, '圣灵药'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got 5 pieces.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('圣灵药', 5)
    SetMessageWindowPos(14, 280, 60, 3)
    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x1F6, 1)
    OP_E0(0x5, 0x0)
    Jump("loc_88D")

    label("loc_868")


    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is nothing in the treasure box.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_88D")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_7B9 end

    def Function_4_89F(): pass

    label("Function_4_89F")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F6, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_94E")
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
            scpstr(SCPSTR_CODE_ITEM, '土人偶'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got two of them.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('土人偶', 2)
    SetMessageWindowPos(14, 280, 60, 3)
    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x1F6, 2)
    OP_E0(0x5, 0x0)
    Jump("loc_973")

    label("loc_94E")


    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is nothing in the treasure box.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_973")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_89F end

    def Function_5_985(): pass

    label("Function_5_985")

    OP_F4(0x3)
    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A0C")
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

    label("loc_A0C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A28")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_A28")

    Return()

    # Function_5_985 end

    def Function_6_A2A(): pass

    label("Function_6_A2A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B23")

    ChrTalk(
        0xFE,
        "…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F…… It sounds like I'm completely fainting.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10B,
        (
            "#11102FKuku, what else to do with other people's affairs.\x01",
            "I guess we did it with our hands?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F……I know.\x02\x03",
            "#00001FIt's bad for them,\x01",
            "Let me go on as it is.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_B4E")

    label("loc_B23")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Defense forces soldiers are fainting.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_B4E")

    TalkEnd(0xFE)
    Return()

    # Function_6_A2A end

    def Function_7_B52(): pass

    label("Function_7_B52")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BB0")

    ChrTalk(
        0xFE,
        "…\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Defense forces soldiers are fainting.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x0, 1)
    Jump("loc_BDB")

    label("loc_BB0")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Defense forces soldiers are fainting.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_BDB")

    TalkEnd(0xFE)
    Return()

    # Function_7_B52 end

    def Function_8_BDF(): pass

    label("Function_8_BDF")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CB2")
    SetMessageWindowPos(160, 160, -1, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x193, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C08")
    SetChrName("voice")
    Jump("loc_C16")

    label("loc_C08")

    SetChrName("Voice of the Mafia")

    label("loc_C16")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "… … Have not you heard anything loud now?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetMessageWindowPos(160, 160, -1, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x193, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C6C")
    SetChrName("voice")
    Jump("loc_C7A")

    label("loc_C6C")

    SetChrName("Voice of the Mafia")

    label("loc_C7A")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Ah……?\x01",
            "Is not it a sky?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_D6C")

    label("loc_CB2")

    SetMessageWindowPos(160, 160, -1, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x193, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CCE")
    SetChrName("voice")
    Jump("loc_CDC")

    label("loc_CCE")

    SetChrName("Voice of the Mafia")

    label("loc_CDC")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "What is this noise? Is it?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetMessageWindowPos(160, 160, -1, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x193, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D2A")
    SetChrName("voice")
    Jump("loc_D38")

    label("loc_D2A")

    SetChrName("Voice of the Mafia")

    label("loc_D38")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Come on, something happened! Is it?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_D6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x193, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D79")
    Call(0, 9)

    label("loc_D79")

    TalkEnd(0xFF)
    Return()

    # Function_8_BDF end

    def Function_9_D7D(): pass

    label("Function_9_D7D")


    ChrTalk(
        0x101,
        "#00005FIs this room …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10B,
        (
            "#11100F(In this room and the other room\x01",
            "My#4RRubathe#The subordinates of\x01",
            "It should be pushed together. )\x02\x03",
            "#11103F(It seems that manpower is not enough,\x01",
            "Troublesome people on this floor\x01",
            "I guess they are going to watch them altogether. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(got it……)\x02\x03",
            "#00001F(… … Anyway, let's hurry.\x01",
            "You will break through before reinforcement comes. )\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x193, 0)
    Return()

    # Function_9_D7D end

    def Function_10_EDF(): pass

    label("Function_10_EDF")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FB0")
    SetMessageWindowPos(120, 10, -1, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x193, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F08")
    SetChrName("voice")
    Jump("loc_F16")

    label("loc_F08")

    SetChrName("Voice of the Mafia")

    label("loc_F16")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "From a young head room\x01",
            "I heard a damn sound!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetMessageWindowPos(120, 10, -1, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x193, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F6D")
    SetChrName("voice")
    Jump("loc_F7B")

    label("loc_F6D")

    SetChrName("Voice of the Mafia")

    label("loc_F7B")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Is everything okay, young head! Is it?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_106B")

    label("loc_FB0")

    SetMessageWindowPos(120, 10, -1, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x193, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FCC")
    SetChrName("voice")
    Jump("loc_FDA")

    label("loc_FCC")

    SetChrName("Voice of the Mafia")

    label("loc_FDA")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "This time it is an alarm …! Is it?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetMessageWindowPos(120, 10, -1, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x193, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1026")
    SetChrName("voice")
    Jump("loc_1034")

    label("loc_1026")

    SetChrName("Voice of the Mafia")

    label("loc_1034")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Young head!\x01",
            "Are you OK? Is it?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_106B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x193, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1078")
    Call(0, 9)

    label("loc_1078")

    TalkEnd(0xFF)
    Return()

    # Function_10_EDF end

    def Function_11_107C(): pass

    label("Function_11_107C")

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
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_129C")
    Jump("loc_34E6")

    label("loc_129C")

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

    def lambda_130F():
        OP_9B(0x0, 0xFE, 0x0, 0x88B8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_130F)
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
        "#00015F#5P#40W….\x02",
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
            "#10203F#5P── Other members of the support department\x01",
            "I am protecting it in another place.\x02\x03",
            "#10208FOne Lloyd, in such a place\x01",
            "I am sorry to be detained … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#11PI don't care about myself\x02\x03",
            "#00008FBut \"protection\" is\x01",
            "That's a strange way of saying!\x02\x03",
            "#00002FWhat on earth ……\x01",
            "Does it protect me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#10206F#5P…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#11P… … you are already\x01",
            "You should have noticed a long time ago.\x02\x03",
            "#00008FI attempted to attack the city of Crossbell\x01",
            "It is also said that there is a true masterpiece.\x02\x03",
            "#00013FFran, - your sister\x01",
            "It is also said that someone who hurt … …\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0xC8)

    ChrTalk(
        0xC,
        "#10215F#5P#4SEven still!\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    ChrTalk(
        0xC,
        (
            "#10207F#5P… but still I\x01",
            "Because it is a member of the guard!\x02\x03",
            "As it changed its name to \"Defense Army\"\x01",
            "It only fulfills the duty as a soldier!\x02\x03",
            "#10208FIf I don't, Crossbell..\x02\x03",
            "#10206F…… Crossbell really\x01",
            "It will be destroyed by the Empire and the Republic!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#11PNoe…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#10206F#5PKa'a thing about … …\x01",
            "I do not think it is good as it is!\x02\x03",
            "The unknown person like \"Society\"\x01",
            "You owe the power of those guys …!\x02\x03",
            "#10210FBut ─ ─ Imperial troops really#6R噵 噵 噵#\x01",
            "I shot that horrible train cannon!\x02\x03",
            "Hitting hundreds of victims\x01",
            "Weapons of mass destruction that may have come out!\x02\x03",
            "#10215FIf it was … ….\x01",
            "Well, it can not be helped!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008F#11P….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#10206F#5PExcuse me…\x02\x03",
            "…… Such things to Mr. Lloyd,\x01",
            "There is no obligation to say it is not it?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xC, 0xB4, 0x1F4)
    Sleep(400)

    ChrTalk(
        0xC,
        (
            "#10208F#11P── Period of detention\x01",
            "I think that it will not last so long.\x02\x03",
            "Once Crossbell overcame the crisis\x01",
            "I think that it will surely be released … …\x02\x03",
            "#10203FSo please ….\x01",
            "Please be patient with me now.\x02",
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
            "#00006F#5P#30W(……At that time……\x01",
            "I could not return the word. )\x02\x03",
            "#00008F(Not only that……\x01",
            "Ka'a had been stuck around\x01",
            "I did not notice at all … …)\x02\x03",
            "(Just being mad at busy … …\x01",
            "I can not keep things I really need to protect … …)\x02\x03",
            "#00006F(… even if it is the feature of Ka'aa\x01",
            "Even if it is a culprit who killed his brother ……)\x02\x03",
            "#00015F(Trying to locate it properly\x01",
            "It ought to have sworn to my heart … ….! )\x02",
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
            "#30WGuy Bannings ----\x01",
            "Are you the one who killed the older brother?\x02",
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
            "#4119V#30WYes. That's correct.\x07\x00\x02",
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
            "#3630V#30Wsorry.\x01",
            "… … Thank you for everything.\x02\x03",
            "#3631VI love you all.\x07\x00\x02",
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
            "#00006F#5P#30W(Brother… sorry…)\x02\x03",
            "(As I thought ….\x01",
            "Overtook my brother at all\x01",
            "It seems they did not … …)\x02\x03",
            "#00015F(Because it is already ……\x01",
            "What should I do ……)\x02\x03",
            "(If I only knew that)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(2854, 255, 100, 0)
    Sleep(500)

    NpcTalk(
        0x10B,
        "Sturdy voice",
        "#5PHah, you're a mess\x02",
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
            "I chased you down and we played\x01",
            "What does the leader work on … …\x02\x03",
            "Over half a year in this place,\x01",
            "I am eating cold rice\x01",
            "I'm getting stupid.\x02",
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
            "#00006F#6P#30WLeave me alone\x02\x03",
            "You are in this place\x01",
            "Even though I think about it, it's self-owned … …\x02\x03",
            "You could have arrested you\x01",
            "I was lucky just overlapped ……\x02\x03",
            "#00008FThat's right … … Separately we are skilled\x01",
            "I did not cross the \"wall\" ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10B,
        "#11101F#11PTch, you're a real pain in the ass you know\x02",
    )

    CloseMessageWindow()
    OP_63(0x10B, 0xFFFFFF38, 2100, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x10B)
    Sleep(500)

    ChrTalk(
        0x10B,
        (
            "#11104F#11PWell it's understandable\x02\x03",
            "As long as I hear the rumor, it is unbearable\x01",
            "It seems to be in a situation.\x02\x03",
            "#11101FIBC president in all the blacklights\x01",
            "President of a dictatorship now … …\x02\x03",
            "Red constellations and associations,\x01",
            "The defense army up to the wind sword Saint\x01",
            "All are turning to the enemy.\x02\x03",
            "#11102FKuku, Triple full of excitement\x01",
            "You do not seem to be talking?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#6P#30W…\x02",
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
            "#11104F#5PWell, now that the storm passes by\x01",
            "Waiting is the right answer.\x02\x03",
            "In this situation anti#2RArka#Why\x01",
            "There is only a genuine fool.\x02\x03",
            "#11100FSomeone like your brother\x02",
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
            "#00011F#6P#30W…Ah…\x02\x03",
            "#00001F#20WThat said, my brother and\x01",
            "Did you have some acquaintance …?\x02",
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
            "#11100F#5PHun, knowledgeable\x01",
            "I was not a lukewarm.\x02\x03",
            "#11103FEven though this threatens how much\x01",
            "It sniffs without disciplining … …\x02\x03",
            "…… If you think,\x01",
            "When I came across a grasshopper stall\x01",
            "I'm going to recommend a cup of stuff … …\x02\x03",
            "#11101FHe was really a troublesome young guy\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00004F#6P#30WHaha, that sounds like him\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    OP_A1(0x10B, 0x3E8, 0x2, 0x5, 0x6)
    Sleep(300)

    ChrTalk(
        0x10B,
        (
            "#11103F#5PWell, even if you kill\x01",
            "I did not look like a dead tama\x01",
            "Because Assassi passed away.\x02\x03",
            "The world is a confusing place\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008F#6P#30W….\x02\x03",
            "#00001F…… Brother has always ……\x01",
            "Anti#2RArka#Was it continued?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10B,
        (
            "#11104F#5POh, my place.#4RRubathe#Besides\x01",
            "I wish I could thrust my neck.\x02\x03",
            "From the corruption of big troops\x01",
            "Intelligence activities of the Empire and the Republic,\x01",
            "Until the move of Joachim's bastard ……\x02\x03",
            "#11100FI was energetic enough to be amazed\x01",
            "You do not mistake.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#6P#30WI see..\x02",
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
            "#11103F#11P─ ─ Hey.\x01",
            "Although it seems that Kang is different.\x02\x03",
            "#11101FApart from Guy Bannings\x01",
            "I was not a \"sneaky man\" why?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x12C, 1800, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005F#6PHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10B,
        (
            "#11104F#11PIf you say it with fury\x01",
            "McCullin would be on top.\x02\x03",
            "搦#2RFrom#If it was a crowd and a foundation\x01",
            "Sergei may be higher.\x02\x03",
            "#11100FIf it is reasonable judgment and processing ability\x01",
            "Dudley in section One is on … …\x02\x03",
            "So that's about how it was\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00011F#6PThat is..\x02\x03",
            "#00008F(… … If you think about it\x01",
            "It may be true. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10B,
        (
            "#11103F#11PI was excusing himself\x01",
            "If so … …\x02\x03",
            "#11101FAt best not \"give up\"\x01",
            "It will be.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x12C, 1800, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005F#6PAh…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10B,
        (
            "#11100F#11PThat is probably, Hamper, I'm acting\x01",
            "I guess it was connected … …\x02\x03",
            "Even bigger counterparts\x01",
            "I guess it was the driving force.\x02\x03",
            "#11103FStill, we can not see the surroundings\x01",
            "I could not read the air ……\x02\x03",
            "#11101F…… What is this young woman saying?\x01",
            "At that time I thought it was a monkey.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008F#6P…\x02",
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
            "#30WListen up Lloyd\x02\x03",
            "If you are a man, in front of you\x01",
            "Try to hit by body.\x02\x03",
            "With a heart of tame, only a tame\x01",
            "Take the truth.\x02\x03",
            "That's right.\x01",
            "You should see what you want to do.\x07\x00\x02",
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
            "#00006F#6P… …. Maybe, the bad thing about my brother's giving up\x01",
            "I think that it was to protect important things.\x02\x03",
            "#00008FNot only in the family,\x01",
            "The city itself called Cross Bell ……\x02\x03",
            "#00000F…… In that sense,\x01",
            "Even you are even Luberce\x01",
            "Perhaps it was the object to protect.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x10B, 0xFFFFFF38, 2100, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x10B,
        "#11105F#11PWhat?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#6PHa ha, to protect\x01",
            "It may be obstructive … ….\x02\x03",
            "#00008FPerhaps, big brother is on body\x01",
            "The flow that made the crossbell now\x01",
            "I think that I was trying to figure it out.\x02\x03",
            "#00004FOn top of that, cross bell itself\x01",
            "I was scratching to protect myself … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10B,
        (
            "#11103F#11PThat is..\x02\x03",
            "#11110FMore than an idiot.\x01",
            "It is a big idiot, is not it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#6PYeah…\x02\x03",
            "#00008F…… I, indeed,\x01",
            "I can not be a fool like that … …\x02\x03",
            "#00000F─ ─ But there are only brothers\x01",
            "There seems to be similar parts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10B,
        "#11105F#11PWhat?\x02",
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

    def lambda_3267():
        OP_96(0xFE, 0x0, 0x0, 0x7918, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3267)
    Sleep(500)
    SetChrSubChip(0x10B, 0x7)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0xB4, 0x1F4)
    OP_6F(0x79)

    ChrTalk(
        0x10B,
        (
            "#11101F#5PYou, no way\x02\x03",
            "You're planning to run out of here?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x0, 0x1F4)
    Sleep(150)

    ChrTalk(
        0x101,
        (
            "#00003F#12PDo not run away.\x01",
            "I am going to find out the truth.\x02\x03",
            "#00001FCrossbell Police, to the Special Affairs Support Division\x01",
            "As an belonging investigator ……\x02\x03",
            "Liberate everyone captured,\x01",
            "Even to regain Ka'aa.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x10B, 0xFFFFFF38, 2100, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x10B)

    ChrTalk(
        0x10B,
        (
            "#11104F#5PEheh, Haha\x02\x03",
            "#11102FTame well enough,\x01",
            "I guess it is a big idiot.\x02",
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
        "#00005F#12PGarcia…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10B,
        (
            "#11103F#5PShow me, brat\x02\x03",
            "In this situation, to a man named Tame\x01",
            "What can we do ……\x02\x03",
            "#11102FPrepare yourself\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    SetCameraDistance(25650, 2000)
    OP_6F(0x79)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()

    label("loc_34E6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_34F6")
    Jump("loc_3AE6")

    label("loc_34F6")

    Sleep(1000)
    OP_68(28000, 1100, -1000, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(27500, 0)
    SetChrPos(0x8, 33000, 0, -1600, 270)
    ClearChrFlags(0x9, 0x8)

    def lambda_3542():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3542)
    Sleep(50)

    def lambda_355A():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_355A)
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
        "#11PWhat?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#5PFrom inside?\x02",
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

    def lambda_364A():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_364A)
    Sleep(50)

    def lambda_3662():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3662)
    WaitChrThread(0x8, 1)

    def lambda_367B():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_367B)
    WaitChrThread(0x9, 1)

    def lambda_368C():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_368C)
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
        "Voice of Garcia",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#3S#11POla Oh!\x01",
            "That extent or oyster is ah ah!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    NpcTalk(
        0x101,
        "Voice of Lloyd",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#1S#11P#50WUgh … cough cough\x07\x00\x02",
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
            "#11Pquarrel……\x01",
            "No, is it Lynch?\x02",
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
            "#11P#4SHey, stop it!\x01",
            "What are you doing!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)

    NpcTalk(
        0x10B,
        "Voice of Garcia",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#4S#11PBecause of you\x01",
            "I decided to eat cold rice!\x02\x03",
            "#4SI'll beat the shit out of you!\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x101,
        "Voice of Lloyd",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#2S#11P#60WCough…\x07\x00\x02",
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
            "#11P……It is useless.\x01",
            "I have not heard.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x9, 0xB4, 0x1F4)

    ChrTalk(
        0x9,
        "#5PNo helping it, we're going in\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PYes, be careful\x02",
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

    def lambda_3A69():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3A69)
    Sleep(100)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    SetChrChipByIndex(0x9, 0x24)
    SetChrSubChip(0x9, 0x0)
    OP_93(0x9, 0x10E, 0x1F4)
    OP_9B(0x0, 0x9, 0x0, 0x7D0, 0xFA0, 0x1)
    OP_93(0x9, 0x0, 0x1F4)

    def lambda_3AB1():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3AB1)
    Sleep(100)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    WaitChrThread(0x8, 1)
    WaitChrThread(0x9, 1)
    EndChrThread(0xF, 0x1)
    FadeToDark(1000, 0, -1)
    OP_0D()

    label("loc_3AE6")

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
        "#12P#4SStop, Garcia!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#6PI'll shoot if you do any more!\x02",
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
            "#11104F#5P#30WEheh, Haha\x02\x03",
            "#11102F…… I got what I did,\x01",
            "It seems that it got too hot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#12PYou asshole..\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6PAlways since I entered here\x01",
            "If you think you were grown-up … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#6PGet back and put your hands up!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10B,
        "#11104F#5PHa\x02",
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
            "#11PAlthough it is not enough manpower,\x01",
            "Should I be in the same room …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11POi, you ok?\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    OP_A6(0x101, 0x0, 0x14, 0x190, 0x7D0)
    Sleep(300)

    ChrTalk(
        0x101,
        "#1S#60W#5P….ah..\x02",
    )

    CloseMessageWindow()
    Fade(100)
    PlayEffect(0x0, 0xFF, 0x101, 0x1, -400, 0, 100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)
    OP_0D()

    ChrTalk(
        0x101,
        "#5P#2S#40WCough cough\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PDamn\x01",
            "The internal organs may have burst.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11PCall a doctor!\x02",
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
        "#5PNo, no need\x02",
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
        "#11PAsshole!\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x10B, 3, 0, 21)
    WaitChrThread(0x10B, 3)
    Sleep(500)
    OP_68(-79350, 1800, 34650, 3000)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#00006F#5PHuh …… I feel bad#2RAnd#Do not.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10B,
        (
            "#11100F#5PHaha, what are you saying now\x02\x03",
            "#11104F\"Please hit me\" or\x01",
            "When I said something\x01",
            "I thought that it was crazy, but …\x02\x03",
            "#11102FYou can really take it\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x10B, 500)
    Sleep(150)

    ChrTalk(
        0x101,
        (
            "#00006F#5PYou are only\x01",
            "It was truly a performance.\x02\x03",
            "#00010FTsu\x01",
            "To truly break my back teeth\x01",
            "I did not think so …\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10B, 0x101, 500)

    ChrTalk(
        0x10B,
        (
            "#11100F#11PThanks, Hun\x01",
            "It would have been like that.\x02\x03",
            "#11103F… … as promised, from here\x01",
            "Let's cooperate until we leave.\x02\x03",
            "#11101FSo what do we do?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#5PThis is the third floor of a detention center ……\x01",
            "There should be few soldiers stuffing up.\x02\x03",
            "#00013FBreak through breaks somehow\x01",
            "Let's escape from the exit on the first floor!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10B,
        (
            "#11104F#11PHa, sounds fine\x02\x03",
            "#11107FEven after a long time …\x01",
            "I suppose you are going to rampage!\x02",
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
            "Lloyd built with a quick\x01",
            "Equipped with a pipe tongue.\x02",
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
            "Garcia joined the party\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Because you are deprived of Enigma ため,\x01",
            "I can not use Arts.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Also, as all the items were robbed\x01",
            "Please be careful of HP.\x07\x00\x02",
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
    AddItemNumber('调查手册', 1)
    AddItemNumber('战斗手册', 1)
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

    # Function_11_107C end

    def Function_12_45C3(): pass

    label("Function_12_45C3")


    def lambda_45C8():
        OP_96(0xFE, 0xFFFE2B40, 0x0, 0x7148, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_45C8)
    Sleep(3000)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_12_45C3 end

    def Function_13_45F0(): pass

    label("Function_13_45F0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4616")
    OP_A6(0xFE, 0x0, 0x23, 0x1F4, 0x1388)
    Sleep(1000)
    Jump("Function_13_45F0")

    label("loc_4616")

    Return()

    # Function_13_45F0 end

    def Function_14_4617(): pass

    label("Function_14_4617")


    def lambda_461C():
        OP_9B(0x0, 0xFE, 0x0, 0xDAC, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_461C)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    WaitChrThread(0xFE, 1)
    TurnDirection(0xFE, 0x10B, 500)
    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_14_4617 end

    def Function_15_464B(): pass

    label("Function_15_464B")


    def lambda_4650():
        OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4650)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    WaitChrThread(0xFE, 1)
    TurnDirection(0xFE, 0x10B, 500)
    Sound(531, 0, 70, 0)
    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_15_464B end

    def Function_16_4685(): pass

    label("Function_16_4685")

    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)

    def lambda_4699():
        OP_9B(0x1, 0xFE, 0x0, 0x7D0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4699)
    WaitChrThread(0xFE, 1)

    def lambda_46B2():
        TurnDirection(0xFE, 0x10B, 500)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_46B2)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_16_4685 end

    def Function_17_46C7(): pass

    label("Function_17_46C7")

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

    # Function_17_46C7 end

    def Function_18_470D(): pass

    label("Function_18_470D")

    Sound(802, 0, 100, 0)
    Sleep(150)

    def lambda_471B():
        OP_98(0xFE, 0x0, 0xFFFFFDA8, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_471B)
    WaitChrThread(0xFE, 1)
    SetChrSubChip(0xFE, 0x2)
    Sound(811, 0, 100, 0)
    ClearChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x1)
    Return()

    # Function_18_470D end

    def Function_19_4749(): pass

    label("Function_19_4749")

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

    # Function_19_4749 end

    def Function_20_4785(): pass

    label("Function_20_4785")

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
        "#11PTrepidation\x05\x02",
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

    def lambda_492E():
        OP_98(0xFE, 0x0, 0xFFFFFD12, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_492E)
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

    # Function_20_4785 end

    def Function_21_4990(): pass

    label("Function_21_4990")

    OP_68(-79500, 1500, 35150, 500)
    MoveCamera(157, 22, 0, 500)
    SetCameraDistance(18500, 500)
    Fade(250)

    def lambda_49BF():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_49BF)
    Sleep(150)
    Sound(802, 0, 100, 0)
    ClearChrFlags(0x10B, 0x20)
    ClearChrFlags(0x10B, 0x2)
    SetChrChipByIndex(0xFE, 0x29)

    def lambda_49E3():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_49E3)
    OP_A1(0xFE, 0x3E8, 0x2, 0x0, 0x1)
    WaitChrThread(0x8, 2)
    WaitChrThread(0xFE, 2)
    OP_0D()
    OP_6F(0x79)
    Sound(2820, 255, 100, 0)

    ChrTalk(
        0x10B,
        "#11107F#4S#5PDamn it!\x05\x02",
    )

    Sound(534, 0, 100, 0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_68(-82180, 1800, 31820, 500)
    SetCameraDistance(23500, 500)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x2)

    def lambda_4A60():
        OP_9B(0x1, 0xFE, 0x0, 0x4B0, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4A60)
    Sleep(100)
    CancelBlur(500)
    Sound(815, 0, 100, 0)
    OP_82(0xFA, 0x1F4, 0x2710, 0x1F4)
    BeginChrThread(0xFE, 2, 0, 22)

    ChrTalk(
        0x8,
        "#11PHappening …!\x05\x02",
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

    def lambda_4BBD():
        OP_98(0xFE, 0x0, 0xFFFFFA24, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_4BBD)
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

    # Function_21_4990 end

    def Function_22_4C0D(): pass

    label("Function_22_4C0D")

    Sleep(500)
    SetChrSubChip(0xFE, 0x3)
    Sleep(125)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x20)
    ClearChrFlags(0xFE, 0x1000)
    Return()

    # Function_22_4C0D end

    def Function_23_4C30(): pass

    label("Function_23_4C30")

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

    # Function_23_4C30 end

    def Function_24_4C97(): pass

    label("Function_24_4C97")

    Sound(882, 0, 100, 0)
    Sleep(2600)
    Sound(882, 0, 80, 0)

    label("loc_4CA6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4CCB")
    Sleep(3800)
    Sound(882, 0, 40, 0)
    Sleep(2200)
    Sound(882, 0, 40, 0)
    Sleep(500)
    Jump("loc_4CA6")

    label("loc_4CCB")

    Return()

    # Function_24_4C97 end

    def Function_25_4CCC(): pass

    label("Function_25_4CCC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4D09")
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
    Jump("Function_25_4CCC")

    label("loc_4D09")

    Return()

    # Function_25_4CCC end

    def Function_26_4D0A(): pass

    label("Function_26_4D0A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4D47")
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
    Jump("Function_26_4D0A")

    label("loc_4D47")

    Return()

    # Function_26_4D0A end

    def Function_27_4D48(): pass

    label("Function_27_4D48")

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
            "…… These guys\x01",
            "What on earth are you doing?\x05\x02",
        )
    )

    OP_6F(0x79)
    OP_68(34500, 1000, -1000, 4000)

    ChrTalk(
        0xB,
        (
            "#11PPlease hand over this early.\x01",
            "I want to go home ……\x05\x02",
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
        "#5PEh\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#11PYou guys are!\x02",
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

    def lambda_505E():
        OP_9B(0x0, 0xFE, 0x0, 0x2134, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_505E)

    def lambda_5073():
        OP_9B(0x0, 0xFE, 0x0, 0x2134, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x10B, 1, lambda_5073)

    ChrTalk(
        0x10B,
        "#11107F#5PHere we go\x05\x02",
    )


    ChrTalk(
        0x101,
        "#00007F#6P#NToo slow!\x05\x02",
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

    # Function_27_4D48 end

    def Function_28_5104(): pass

    label("Function_28_5104")


    def lambda_5109():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5109)
    OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Sleep(800)
    OP_93(0xFE, 0x0, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x1964, 0x7D0, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_28_5104 end

    def Function_29_5150(): pass

    label("Function_29_5150")

    Sleep(1000)

    def lambda_5158():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5158)
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

    # Function_29_5150 end

    def Function_30_51CD(): pass

    label("Function_30_51CD")

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
        "#5P#30WYou assholes…\x02",
    )

    CloseMessageWindow()

    def lambda_52D3():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_52D3)
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
        "#11P#30WYou plan to run…\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(25500, 1000)

    def lambda_5337():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_5337)
    Sleep(150)
    Fade(250)
    Sound(802, 0, 100, 0)
    SetChrSubChip(0xB, 0x2)
    OP_0D()
    WaitChrThread(0xB, 2)
    Sleep(500)

    def lambda_536A():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_536A)
    Sleep(150)
    Fade(250)
    Sound(804, 0, 100, 0)
    OP_0D()
    WaitChrThread(0xB, 2)

    def lambda_5396():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_5396)
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
            "#00010F#6PCuddly, I used Enigma\x01",
            "Emergency alarm system …!\x02",
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
            "#11104F#5PPowered by Translate\x01",
            "Well, what do you do?\x02",
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
            "#00007F#12PIt is supposed … ….\x01",
            "Breakthrough as it is!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10B,
        "#11102F#5PHah, sounds good!\x02",
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

    # Function_30_51CD end

    def Function_31_5582(): pass

    label("Function_31_5582")

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

    # Function_31_5582 end

    def Function_32_55E9(): pass

    label("Function_32_55E9")

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
        "… … the visiting time is about 10 minutes.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Because the other person is an injured person this time,\x01",
            "As an extra measure visiting in the room\x01",
            "I decided to allow it … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Directly touching the other party or giving things,\x01",
            "It is forbidden to make a noise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FYes, I understand.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Yes.\x02",
    )

    CloseMessageWindow()
    OP_93(0xE, 0x0, 0x1F4)

    ChrTalk(
        0xE,
        "#11P── Garcia, it's an interview!\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(120, 10, -1, -1)
    SetChrName("Voice of Garcia")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "… …. Why do not you enter.\x07\x00\x02",
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

    def lambda_5931():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_5931)
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
        "#6P#00000FGarcia …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11100FKuku, I met him again.\x02\x03",
            "#11104FIt seems that we were able to see them again and again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00305FOh, Osan.\x01",
            "Are you up and getting over it?\x02\x03",
            "#00303FCombating with the Defense Army anyhow,\x01",
            "I heard that it was quite exhausted.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11103FHuang, even if you're okay.\x01",
            "With any bare hands with rifles and Halberd\x01",
            "You got to get in touch with each other.\x02\x03",
            "#11101FHey maiden ……\x01",
            "I finally got to get up.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5D33")

    ChrTalk(
        0x10A,
        (
            "#6P#00600FHun, that's it\x01",
            "It will make you feel comfortable.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5DC4")

    label("loc_5D33")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5D7F")

    ChrTalk(
        0x109,
        (
            "#6P#10102FThat's it.\x01",
            "I feel a margin.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5DC4")

    label("loc_5D7F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5DC4")

    ChrTalk(
        0x106,
        (
            "#6P#10701FIn that case\x01",
            "I let you feel a margin ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5DC4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5E18")

    ChrTalk(
        0x105,
        (
            "#6P#10402FHugh, as expected\x01",
            "\"Killing Bear\" is the place.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5EC9")

    label("loc_5E18")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5E82")

    ChrTalk(
        0x106,
        (
            "#6P#10703FWestern brigade brigades \"Murderer Bear#6RKilling Bear#\",\x01",
            "Is it the place you said as expected?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5EC9")

    label("loc_5E82")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5EC9")

    ChrTalk(
        0x109,
        (
            "#6P#10106FWell, as a former soldier\x01",
            "What to say ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5EC9")


    ChrTalk(
        0x103,
        (
            "#6P#00200FWell, either way for the time being\x01",
            "It looks like it will not move … …\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#6P#00001F…… Garcia, to you\x01",
            "I can not thank you enough.\x02\x03",
            "#00003FAt that time, you escape from jail\x01",
            "If you do not lend me a hand …\x02\x03",
            "#00000FReuniting with my friends,\x01",
            "You can also reach here\x01",
            "I think that it was sure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00102FLloyd …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11101F…… Head, to say such a thing\x01",
            "Do you really want to come see me?\x02\x03",
            "#11103FThe compatibility with you,\x01",
            "In the place where I left the gate of jail\x01",
            "You should have finished.\x02\x03",
            "#11102FTo me, Tameie\x01",
            "A foolish asshole who crushed the organization …\x01",
            "That still does not change yet?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00004FBut even so\x01",
            "I want you to say a word.\x02\x03",
            "#00000FThank you, Garcia.\x01",
            "What I can do now is\x01",
            "I owe it to you.\x02\x03",
            "#00000FThis series of cases,\x01",
            "Be sure to get to the truth,\x01",
            "I'll protect the crossbells.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xD)

    ChrTalk(
        0xD,
        (
            "#11103FPhew\x01",
            "I remembered a chest poor thing.\x02\x03",
            "Whatever happens, no matter how many times you dismiss it,\x01",
            "I do not like to give up\x01",
            "The eyes of persistent persistent … …\x02\x03",
            "#11102FBannings …\x01",
            "Tame is definitely Guy 's younger brother.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00305FOssan ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00004F…… Haha, thank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11103F…… Chi.\x01",
            "Do not be afraid of gara\x01",
            "It seems I have noticed.\x02\x03",
            "#11101FYou guys, in a place like this\x01",
            "Tintara talkative\x01",
            "I do not have free time doing it.\x02\x03",
            "#11103F…… I can lose it at last.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00004F…… Oh, I understand.\x02\x03",
            "#00000FLet's say that everyone will go soon.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 1)
    NewScene("t6000", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_32_55E9 end

    def Function_33_6417(): pass

    label("Function_33_6417")


    def lambda_641C():
        OP_95(0xFE, 0, 0, 29000, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_641C)

    def lambda_6436():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6436)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_644F():
        OP_95(0xFE, 0, 0, 31000, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_644F)
    WaitChrThread(0xFE, 1)

    def lambda_646D():
        OP_95(0xFE, 2000, 0, 31000, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_646D)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(5000)

    def lambda_6495():
        OP_95(0xFE, 0, 0, 31000, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6495)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_33_6417 end

    def Function_34_64B6(): pass

    label("Function_34_64B6")


    def lambda_64BB():
        OP_95(0xFE, 0, 0, 29000, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_64BB)

    def lambda_64D5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_64D5)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_64EE():
        OP_95(0xFE, -1370, 0, 39290, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_64EE)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_34_64B6 end

    def Function_35_650F(): pass

    label("Function_35_650F")


    def lambda_6514():
        OP_95(0xFE, 0, 0, 29000, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6514)

    def lambda_652E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_652E)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_6547():
        OP_95(0xFE, -160, 0, 39190, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6547)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_35_650F end

    def Function_36_6568(): pass

    label("Function_36_6568")


    def lambda_656D():
        OP_95(0xFE, 0, 0, 29000, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_656D)

    def lambda_6587():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6587)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_65A0():
        OP_95(0xFE, -1240, 0, 38210, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_65A0)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_36_6568 end

    def Function_37_65C1(): pass

    label("Function_37_65C1")


    def lambda_65C6():
        OP_95(0xFE, 0, 0, 29000, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_65C6)

    def lambda_65E0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_65E0)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_65F9():
        OP_95(0xFE, 0, 0, 38000, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_65F9)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_37_65C1 end

    def Function_38_661A(): pass

    label("Function_38_661A")


    def lambda_661F():
        OP_95(0xFE, 0, 0, 29000, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_661F)

    def lambda_6639():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6639)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_6652():
        OP_95(0xFE, -300, 0, 36920, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6652)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_38_661A end

    def Function_39_6673(): pass

    label("Function_39_6673")


    def lambda_6678():
        OP_95(0xFE, 0, 0, 29000, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6678)

    def lambda_6692():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6692)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_66AB():
        OP_95(0xFE, -1470, 0, 36720, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_66AB)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_39_6673 end

    def Function_40_66CC(): pass

    label("Function_40_66CC")

    OP_96(0xFE, 0x3E8, 0x96, 0x3E8, 0x7D0, 0x0)

    def lambda_66E5():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_66E5)
    Sleep(100)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    Return()

    # Function_40_66CC end

    SaveToFile()

Try(main)
