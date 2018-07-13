from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t6051.bin",                # FileName
        "t6051",                    # MapName
        "t6051",                    # Location
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
        "t6051",                  # 0
        "State Guard Soldier",    # 1
        "State Guard Soldier",    # 2
        "State Guard Soldier",    # 3
        "State Guard Soldier",    # 4
        "State Guard Soldier",    # 5
        "State Guard Commander",  # 6
        "State Guard Soldier",    # 7
        "State Guard Soldier",    # 8
        "State Guard Soldier",    # 9
        "State Guard Soldier",    # 10
        "イベント用軍用犬",       # 11
        "イベント用軍用犬",       # 12
        "イベント用軍用犬",       # 13
        "SE制御",                 # 14
        "BT6010",                 # 15
        "BT6020",                 # 16
        "BT6030",                 # 17
    ))

    ATBonus("ATBonus_480", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_540", 6, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_544", 10, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_548", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_54C", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_550", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_554", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_558", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_55C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_520", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_524", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_528", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_52C", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_530", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_534", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_538", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_53C", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_560", 8, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_564", 5, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_568", 11, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_56C", 7, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_570", 9, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_574", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_578", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_57C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_580", 5, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_584", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_588", 8, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_58C", 11, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_590", 11, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_594", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_598", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_59C", 12, 14, 180)

    # monster count: 0

    # event battle count: 3

    BattleInfo(
        "BattleInfo_5A0", 0x004A, 3, 6, 45, 3, 3, 30, 0, "BT6010", 0x00000000, 100, 0, 0, 0,
        (
            ("ms80800.dat", "ms80800.dat", "ms41400.dat", "ms41500.dat", 0, 0, 0, 0, "MonsterBattlePostion_540", "MonsterBattlePostion_520", "ed7540", "ed7453", "ATBonus_480"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_5E4", 0x004A, 3, 6, 45, 3, 3, 30, 0, "BT6020", 0x00000000, 100, 0, 0, 0,
        (
            ("ms41500.dat", "ms41400.dat", "ms41400.dat", "ms80800.dat", "ms80800.dat", 0, 0, 0, "MonsterBattlePostion_560", "MonsterBattlePostion_520", "ed7540", "ed7453", "ATBonus_480"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_628", 0x004A, 3, 6, 45, 3, 3, 30, 0, "BT6030", 0x00000000, 100, 0, 0, 0,
        (
            ("ms41400.dat", "ms41400.dat", "ms41400.dat", "ms41500.dat", "ms41500.dat", "ms80800.dat", "ms80800.dat", "ms80800.dat", "MonsterBattlePostion_580", "MonsterBattlePostion_520", "ed7540", "ed7453", "ATBonus_480"),
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

    DeclNpc(0,       0,       0,       0,    405,  0x0, 0,   0,   0,   255, 255, 0,   4,   255,  0)
    DeclNpc(0,       0,       0,       0,    405,  0x0, 0,   0,   0,   255, 255, 0,   4,   255,  0)
    DeclNpc(0,       0,       0,       0,    405,  0x0, 0,   0,   0,   255, 255, 0,   4,   255,  0)
    DeclNpc(0,       0,       0,       0,    405,  0x0, 0,   0,   0,   255, 255, 0,   4,   255,  0)
    DeclNpc(0,       0,       0,       0,    405,  0x0, 0,   0,   0,   255, 255, 0,   4,   255,  0)
    DeclNpc(0,       0,       0,       0,    405,  0x0, 0,   0,   0,   255, 255, 0,   4,   255,  0)
    DeclNpc(0,       0,       0,       0,    405,  0x0, 0,   0,   0,   255, 255, 0,   4,   255,  0)
    DeclNpc(0,       0,       0,       0,    405,  0x0, 0,   0,   0,   255, 255, 0,   4,   255,  0)
    DeclNpc(0,       0,       0,       0,    405,  0x0, 0,   0,   0,   255, 255, 0,   4,   255,  0)
    DeclNpc(0,       0,       0,       0,    405,  0x0, 0,   0,   0,   255, 255, 0,   4,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 24,  70.0,                  3.0,                   0.0,                   144.0,                 [0.125,                -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000001788139343,   0.0,                   -8.75,                 -1.0,                  -0.0,                  1.0])
    DeclEvent(0x0000, 0, 33,  143.0,                 3.5,                   0.0,                   20.25,                 [0.6666666865348816,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.1666666716337204,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -95.33333587646484,    -0.5833333730697632,   -0.0,                  1.0])

    DeclActor(149250,  0,       3250,    1200,    149250,  1500,    3250,    0x007C, 0,  31, 0x0000)
    DeclActor(147000,  0,       4294963796, 1200,    147000,  1500,    4294963796, 0x007C, 0,  32, 0x0000)
    DeclActor(37000,   0,       59000,   1200,    37000,   1000,    59000,   0x007C, 0,  2,  0x0000)
    DeclActor(4294954796, 0,       14000,   1200,    4294954796, 1000,    14000,   0x007C, 0,  3,  0x0000)
    DeclActor(19000,   0,       4500,    1200,    19000,   1200,    3750,    0x007C, 0,  5,  0x0000)
    DeclActor(7000,    0,       4294964796, 1200,    7000,    1200,    4294965296, 0x007C, 0,  6,  0x0000)
    DeclActor(4294962296, 0,       4294964796, 1200,    4294962296, 1200,    4294965296, 0x007C, 0,  7,  0x0000)

    ChipFrameInfo(1780, 0)                                       # 0

    ScpFunction((
        "Function_0_6F4",          # 00, 0
        "Function_1_725",          # 01, 1
        "Function_2_8A9",          # 02, 2
        "Function_3_984",          # 03, 3
        "Function_4_AD6",          # 04, 4
        "Function_5_B67",          # 05, 5
        "Function_6_FD9",          # 06, 6
        "Function_7_137C",         # 07, 7
        "Function_8_19AF",         # 08, 8
        "Function_9_1D18",         # 09, 9
        "Function_10_1D34",        # 0A, 10
        "Function_11_1D50",        # 0B, 11
        "Function_12_1D6A",        # 0C, 12
        "Function_13_1FF1",        # 0D, 13
        "Function_14_2058",        # 0E, 14
        "Function_15_2437",        # 0F, 15
        "Function_16_2497",        # 10, 16
        "Function_17_24E0",        # 11, 17
        "Function_18_2527",        # 12, 18
        "Function_19_255C",        # 13, 19
        "Function_20_256E",        # 14, 20
        "Function_21_25BA",        # 15, 21
        "Function_22_261B",        # 16, 22
        "Function_23_28F2",        # 17, 23
        "Function_24_298C",        # 18, 24
        "Function_25_33FC",        # 19, 25
        "Function_26_3988",        # 1A, 26
        "Function_27_39BF",        # 1B, 27
        "Function_28_39E8",        # 1C, 28
        "Function_29_3A07",        # 1D, 29
        "Function_30_3A23",        # 1E, 30
        "Function_31_3B23",        # 1F, 31
        "Function_32_3D0A",        # 20, 32
        "Function_33_3F2F",        # 21, 33
    ))


    def Function_0_6F4(): pass

    label("Function_0_6F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_70A")
    Event(0, 8)
    Jump("loc_724")

    label("loc_70A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_724")
    Event(0, 14)

    label("loc_724")

    Return()

    # Function_0_6F4 end

    def Function_1_725(): pass

    label("Function_1_725")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x184, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_741")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x21C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_753")

    label("loc_741")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_753")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x233), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_753")

    OP_52(0x10B, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10B, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10B, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x184, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_78C")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_78C")

    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x184, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x184, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7A4")
    ModifyEventFlags(1, 1, 0x80)

    label("loc_7A4")

    OP_65(0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x184, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x184, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7BA")
    OP_66(0x0, 0x1)

    label("loc_7BA")

    OP_65(0x1, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x184, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x184, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7D0")
    OP_66(0x1, 0x1)

    label("loc_7D0")

    OP_65(0x4, 0x1)
    OP_65(0x5, 0x1)
    OP_65(0x6, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x184, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7F6")
    OP_66(0x4, 0x1)
    OP_66(0x5, 0x1)
    OP_66(0x6, 0x1)

    label("loc_7F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x184, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_807")
    Call(0, 13)

    label("loc_807")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x184, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_818")
    Call(0, 23)

    label("loc_818")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x184, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x184, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_829")
    Call(0, 30)

    label("loc_829")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x184, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_852")
    OP_70(0xA, 0x2D)
    SetMapObjFlags(0xA, 0x2)
    ClearMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    Jump("loc_868")

    label("loc_852")

    OP_70(0xA, 0x0)
    ClearMapObjFlags(0xA, 0x2)
    SetMapObjFlags(0x1, 0x4)
    ClearMapObjFlags(0x2, 0x4)

    label("loc_868")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F6, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_87B")
    OP_70(0xC, 0x0)
    Jump("loc_87F")

    label("loc_87B")

    OP_70(0xC, 0x1E)

    label("loc_87F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F6, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_892")
    OP_70(0xD, 0x0)
    Jump("loc_896")

    label("loc_892")

    OP_70(0xD, 0x1E)

    label("loc_896")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x184, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x184, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8A8")
    OP_70(0x0, 0xA)

    label("loc_8A8")

    Return()

    # Function_1_725 end

    def Function_2_8A9(): pass

    label("Function_2_8A9")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F6, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_954")
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
            scpstr(SCPSTR_CODE_ITEM, 0x1F6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x10 obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x1F6, 10)
    SetMessageWindowPos(14, 280, 60, 3)
    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x1F6, 3)
    OP_E0(0x5, 0x0)
    Jump("loc_972")

    label("loc_954")


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

    label("loc_972")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_8A9 end

    def Function_3_984(): pass

    label("Function_3_984")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F6, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A80")
    Sound(14, 0, 100, 0)
    OP_74(0xD, 0x1E)
    OP_71(0xD, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1FE, 1)"), scpexpr(EXPR_END)), "loc_A09")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1FE),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1F6, 4)
    OP_E0(0x5, 0x0)
    Jump("loc_A7B")

    label("loc_A09")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1FE),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " is inside the chest.\x01",
            "Since you have too many, you gave it up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0xD, 0x1E, 0x0, 0x0, 0x0)

    label("loc_A7B")

    Jump("loc_ACA")

    label("loc_A80")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is nothing in the chest. \x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_ACA")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_984 end

    def Function_4_AD6(): pass

    label("Function_4_AD6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B30")

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
            "The State Guard soldier is out cold.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x0, 0)
    Jump("loc_B63")

    label("loc_B30")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The State Guard soldier is out cold.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_B63")

    TalkEnd(0xFE)
    Return()

    # Function_4_AD6 end

    def Function_5_B67(): pass

    label("Function_5_B67")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x193, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F6C")
    SetMessageWindowPos(120, 10, -1, -1)
    SetChrName("Haughty-Like Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Y-You...\x01",
            "Is this commotion your doing!?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00005FT-This voice...\x01",
            "Could it be...President Marconi?\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(100, 10, -1, -1)
    SetChrName("Marconi's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Y-You're that police kid!?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetMessageWindowPos(100, 10, -1, -1)
    SetChrName("Marconi's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Garcｵa, why're you with him...!?\x01",
            "I-If you're going, take me with you!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x10B,
        (
            "#11103F...President, I'm very sorry\x01",
            "but I can't do that.\x02\x03",
            "#11101FPlease stay calm, because\x01",
            "I'll be back immediately.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(100, 10, -1, -1)
    SetChrName("Marconi's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "H-Hey, wait! Garcｵaaa!!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00011F(U-Unexpectedly he seemed to be doing fine...)\x02\x03",
            "#00006F(...It also seems that his haughty-like\x01",
            "personality didn't change too.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10B,
        (
            "#11100F(Eh eh, don't say that.)\x02\x03",
            "#11104F(To me, he's also the man I'm\x01",
            "indebted to for givin' me a\x01",
            "snug place called "Revache".)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F(...There're many kinds among you too, eh.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10B,
        (
            "#11103F(...Hmph, it seems I've blurted\x01",
            "out something not in my style.)\x02\x03",
            "#11101F(Let's move on, kid.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x193, 1)
    Jump("loc_FD5")

    label("loc_F6C")

    SetMessageWindowPos(100, 10, -1, -1)
    SetChrName("Marconi's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Garcｵa, police kid!!\x01",
            "I-If you're going, take me with you!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_FD5")

    TalkEnd(0xFF)
    Return()

    # Function_5_B67 end

    def Function_6_FD9(): pass

    label("Function_6_FD9")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x193, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12BF")
    SetMessageWindowPos(160, 160, -1, -1)
    SetChrName("Frightened Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "W-What the heck is going on!?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetMessageWindowPos(160, 160, -1, -1)
    SetChrName("Frightened Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Jailkeeper...where're you!?\x01",
            "S-Settle this situation quick!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x10B,
        (
            "#11103F(...If I remember correctly, who's in custody\x01",
            "in this cell is that Hartmann bastard.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001F(Former Chairman Hartmann...\x01",
            "He's been here since the Altair lodge case.)\x02\x03",
            "#00003F(Somehow he seemed\x01",
            "to have become frightened...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10B,
        (
            "#11104F(He's been that way all the time\x01",
            "since he was put in prison.)\x02\x03",
            "#11102F(Havin' lost wealth and status,\x01",
            "he maybe doesn't have anything\x01",
            "that can support him anymore.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(...He worries me a little, but...\x01",
            "This too is the punishment he was given.)\x02\x03",
            "#00001F(...It's time to go.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x193, 2)
    Jump("loc_1378")

    label("loc_12BF")

    SetMessageWindowPos(160, 160, -1, -1)
    SetChrName("Hartmann's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "W-What the heck is going on!?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetMessageWindowPos(160, 160, -1, -1)
    SetChrName("Hartmann's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Jailkeeper...where're you!?\x01",
            "S-Settle this situation quick!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_1378")

    TalkEnd(0xFF)
    Return()

    # Function_6_FD9 end

    def Function_7_137C(): pass

    label("Function_7_137C")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x193, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1884")
    SetMessageWindowPos(160, 160, -1, -1)
    SetChrName("Composed Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Who is there...\x01",
            "Could it be Lloyd?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetMessageWindowPos(160, 160, -1, -1)
    SetChrName("Composed Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I see, you're the cause of this ruckus...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00005FThis voice...could it\x01",
            "be Mr. Ernest!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10B,
        (
            "#11101F...The former mayor secretary?\x01",
            "Now that I think 'bout it,\x01",
            "he had been put in here.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(160, 160, -1, -1)
    SetChrName("Ernest's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I was surprised when I heard that\x01",
            "you were put in here, Lloyd, but...\x01",
            "...Ha ha, I'm happy I can meet you again.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        (
            "#00002FThank goodness...judging by your\x01",
            "condition, it seems the Gnosis\x01",
            "has almost completely worn out.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(160, 160, -1, -1)
    SetChrName("Ernest's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Yeah, thank goodness it has.\x01",
            "I really did something inexcusable to you all...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetMessageWindowPos(160, 160, -1, -1)
    SetChrName("Ernest's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "...No, I'll stop here for now.\x01",
            "It seems it's not the time for this.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetMessageWindowPos(160, 160, -1, -1)
    SetChrName("Ernest's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "After I atone from my sins and come out\x01",
            "from here, I want you to allow me to formally \x01",
            "apologise to you, Elie and the others.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetMessageWindowPos(160, 160, -1, -1)
    SetChrName("Ernest's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Please, don't mind me now and go.\x01",
            "...I'll pray the Goddess to keep you safe.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        "#00004F...Thank you very much.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10B,
        (
            "#11103F...Done talkin'?\x01",
            "There's no time to dawdle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001FYeah...let's hurry up!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x193, 3)
    Jump("loc_19AB")

    label("loc_1884")

    SetMessageWindowPos(160, 160, -1, -1)
    SetChrName("Ernest's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "After I atone from my sins and come out\x01",
            "from here, I want you to allow me to formally \x01",
            "apologise to you, Elie and the others.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetMessageWindowPos(160, 160, -1, -1)
    SetChrName("Ernest's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Please, don't mind me now and go.\x01",
            "...I'll pray the Goddess to keep you safe.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_19AB")

    TalkEnd(0xFF)
    Return()

    # Function_7_137C end

    def Function_8_19AF(): pass

    label("Function_8_19AF")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch41450.itc", 0x1E)
    LoadChrToIndex("chr/ch41451.itc", 0x1F)
    LoadChrToIndex("chr/ch41550.itc", 0x20)
    LoadChrToIndex("chr/ch41551.itc", 0x21)
    LoadChrToIndex("monster/ch80850.itc", 0x22)
    LoadChrToIndex("monster/ch80851.itc", 0x23)
    LoadChrToIndex("chr/ch00050.itc", 0x24)
    LoadChrToIndex("chr/ch04152.itc", 0x25)
    SetChrPos(0x101, 21200, 0, 200, 270)
    SetChrPos(0x10B, 21500, 0, 1600, 270)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 4500, 0, 400, 90)
    SetChrFlags(0x8, 0x40)
    SetChrChipByIndex(0x9, 0x20)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 4500, 0, 1600, 90)
    SetChrFlags(0x9, 0x40)
    SetChrChipByIndex(0x12, 0x22)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0x12, 7000, 0, 250, 90)
    SetChrFlags(0x12, 0x20)
    OP_52(0x12, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x12, 0, 0, 9)
    SetChrChipByIndex(0x13, 0x22)
    SetChrSubChip(0x13, 0x0)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, 7000, 0, 1750, 90)
    SetChrFlags(0x13, 0x20)
    OP_52(0x13, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x13, 0, 0, 9)
    OP_68(21400, 1000, 1000, 0)
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
    OP_68(6850, 1000, 1000, 2000)
    MoveCamera(45, 23, 0, 2000)
    OP_6E(400, 2000)
    SetCameraDistance(25500, 2000)
    OP_6F(0x79)

    ChrTalk(
        0x8,
        "#6PThere they're!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Freeze!!\x02",
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(12400, 1000, 1000, 0)
    MoveCamera(45, 23, 0, 0)
    SetCameraDistance(33500, 0)
    OP_68(21400, 1000, 1000, 1800)
    SetCameraDistance(25500, 1800)
    SetChrChipByIndex(0x8, 0x1F)
    SetChrSubChip(0x8, 0x0)

    def lambda_1C04():
        OP_9B(0x0, 0xFE, 0x0, 0x2EE0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1C04)
    SetChrChipByIndex(0x9, 0x21)
    SetChrSubChip(0x9, 0x0)

    def lambda_1C21():
        OP_9B(0x0, 0xFE, 0x0, 0x2EE0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1C21)
    EndChrThread(0x12, 0x0)
    SetChrChipByIndex(0x12, 0x23)
    SetChrSubChip(0x12, 0x0)
    OP_52(0x12, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x12, 0, 0, 10)
    BeginChrThread(0x15, 1, 0, 11)

    def lambda_1C59():
        OP_9B(0x0, 0xFE, 0x0, 0x2EE0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1C59)
    EndChrThread(0x13, 0x0)
    SetChrChipByIndex(0x13, 0x23)
    SetChrSubChip(0x13, 0x0)
    OP_52(0x13, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x13, 0, 0, 10)

    def lambda_1C8B():
        OP_9B(0x0, 0xFE, 0x0, 0x2EE0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_1C8B)
    Sleep(200)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0x101, 0x24)
    SetChrSubChip(0x101, 0x0)
    Sleep(100)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0x10B, 0x25)
    SetChrSubChip(0x10B, 0x0)
    Sleep(50)
    SetChrSubChip(0x10B, 0x1)
    OP_6F(0x79)
    SetCameraDistance(23500, 500)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    Sleep(500)
    EndChrThread(0x8, 0x1)
    EndChrThread(0x9, 0x1)
    EndChrThread(0x12, 0x1)
    EndChrThread(0x13, 0x1)
    EndChrThread(0x12, 0x0)
    EndChrThread(0x13, 0x0)
    EndChrThread(0x15, 0x1)
    Battle("BattleInfo_5A0", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    Call(0, 12)
    Return()

    # Function_8_19AF end

    def Function_9_1D18(): pass

    label("Function_9_1D18")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1D33")
    OP_A1(0xFE, 0x5DC, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_9_1D18")

    label("loc_1D33")

    Return()

    # Function_9_1D18 end

    def Function_10_1D34(): pass

    label("Function_10_1D34")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1D4F")
    OP_A1(0xFE, 0x7D0, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_10_1D34")

    label("loc_1D4F")

    Return()

    # Function_10_1D34 end

    def Function_11_1D50(): pass

    label("Function_11_1D50")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1D69")
    Sound(845, 0, 100, 0)
    Sleep(500)
    Jump("Function_11_1D50")

    label("loc_1D69")

    Return()

    # Function_11_1D50 end

    def Function_12_1D6A(): pass

    label("Function_12_1D6A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x101, 21400, 0, 400, 270)
    SetChrPos(0x10B, 21400, 0, 1600, 270)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x10B, 0xFF)
    SetChrSubChip(0x10B, 0x0)
    ClearChrFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x8000)
    ClearChrFlags(0x8, 0x40)
    ClearChrFlags(0x9, 0x40)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    Call(0, 13)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    OP_68(21070, 1100, 1110, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25500, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(24500, 1000)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00006F#11P...They began to use military dogs.\x02\x03",
            "#00008FWhen they were the CGF, they\x01",
            "wouldn't have used them...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10B,
        (
            "#11104F#5PHmph, they could've applied\x01",
            "Revache's results about them.\x02\x03",
            "#11102FPerhaps they're manipulatin'\x01",
            "them usin' drugs.\x02\x03",
            "#11109FEh eh, doesn't it seem they've\x01",
            "become nice and nasty?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x10B, 500)

    ChrTalk(
        0x101,
        (
            "#00010F#12PKh...shut up!\x02\x03",
            "#00008F(I can't think this was decided by Commander\x01",
            "Sonya or Vice Commander Douglas, but...)\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 21400, 0, 1000, 270)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x183, 6)
    EventEnd(0x5)
    Return()

    # Function_12_1D6A end

    def Function_13_1FF1(): pass

    label("Function_13_1FF1")

    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x2)
    ClearChrFlags(0x8, 0x80)
    OP_52(0x8, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x8, 0x40)
    ClearChrFlags(0x8, 0x1)
    SetChrPos(0x8, 18400, 0, -200, 45)
    SetChrChipByIndex(0x9, 0x0)
    SetChrSubChip(0x9, 0x3)
    ClearChrFlags(0x9, 0x80)
    OP_52(0x9, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x9, 0x40)
    ClearChrFlags(0x9, 0x1)
    SetChrPos(0x9, 17400, 0, 2250, 90)
    Return()

    # Function_13_1FF1 end

    def Function_14_2058(): pass

    label("Function_14_2058")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch41400.itc", 0x1E)
    LoadChrToIndex("chr/ch41500.itc", 0x1F)
    LoadChrToIndex("chr/ch41450.itc", 0x20)
    LoadChrToIndex("chr/ch41451.itc", 0x21)
    LoadChrToIndex("chr/ch41550.itc", 0x22)
    LoadChrToIndex("chr/ch41551.itc", 0x23)
    LoadChrToIndex("monster/ch80850.itc", 0x24)
    LoadChrToIndex("monster/ch80851.itc", 0x25)
    LoadChrToIndex("chr/ch00050.itc", 0x26)
    LoadChrToIndex("chr/ch04152.itc", 0x27)
    SetChrPos(0x101, -55500, 0, -1000, 270)
    SetChrPos(0x10B, -55500, 0, -1000, 270)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x10B, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0xA, 0x1E)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, -61600, 0, 2200, 270)
    SetChrFlags(0xA, 0x40)
    SetChrChipByIndex(0xB, 0x1E)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, -61600, 0, 3600, 225)
    SetChrFlags(0xB, 0x40)
    SetChrChipByIndex(0xC, 0x1F)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, -63000, 0, 2500, 90)
    SetChrFlags(0xC, 0x40)
    SetChrChipByIndex(0x12, 0x24)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0x12, -63150, 0, 6800, 180)
    SetChrFlags(0x12, 0x20)
    OP_52(0x12, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x12, 0, 0, 9)
    SetChrChipByIndex(0x13, 0x24)
    SetChrSubChip(0x13, 0x0)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, -61950, 0, 9700, 180)
    SetChrFlags(0x13, 0x20)
    OP_52(0x13, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x13, 0, 0, 9)
    SetMapObjFlags(0x8, 0x1000)
    ClearMapObjFlags(0x8, 0x10)
    OP_70(0x8, 0x0)
    OP_68(-62100, 1000, 3900, 0)
    MoveCamera(40, 23, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(26000, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(25500, 1000)
    OP_6F(0x79)
    OP_0D()
    Sound(103, 0, 100, 0)
    Sound(121, 0, 50, 0)
    Sleep(300)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(-60800, 1400, 950, 2000)
    MoveCamera(60, 23, 0, 2000)
    OP_6E(400, 2000)
    SetCameraDistance(25500, 2000)
    BeginChrThread(0x101, 3, 0, 15)
    BeginChrThread(0x10B, 3, 0, 16)

    def lambda_22CA():
        OP_93(0xA, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_22CA)
    Sleep(50)

    def lambda_22DA():
        OP_93(0xB, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_22DA)
    Sleep(50)

    def lambda_22EA():
        OP_93(0xC, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_22EA)
    Sleep(50)
    WaitChrThread(0xA, 0)
    WaitChrThread(0xB, 0)
    WaitChrThread(0xC, 0)
    OP_6F(0x79)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x10B, 3)
    Sleep(200)

    ChrTalk(
        0xA,
        "#5PG-Garcｵa!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#5PAnd the Support Section's youngster too!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#6PDamn it!\x01",
            "Arrest both of them!!\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    Sound(805, 0, 100, 0)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0xA, 0x20)
    SetChrSubChip(0xA, 0x0)
    SetChrChipByIndex(0xB, 0x20)
    SetChrSubChip(0xB, 0x0)
    SetChrChipByIndex(0xC, 0x22)
    SetChrSubChip(0xC, 0x0)
    OP_0D()
    OP_68(-59500, 1400, -1150, 1200)
    MoveCamera(36, 23, 0, 1200)
    BeginChrThread(0xA, 3, 0, 19)
    BeginChrThread(0xB, 3, 0, 17)
    BeginChrThread(0xC, 3, 0, 18)
    BeginChrThread(0x12, 3, 0, 20)
    BeginChrThread(0x13, 3, 0, 21)
    Sleep(1000)
    SetCameraDistance(22500, 500)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    Sleep(500)
    EndChrThread(0xA, 0x3)
    EndChrThread(0xB, 0x3)
    EndChrThread(0xC, 0x3)
    EndChrThread(0x12, 0x3)
    EndChrThread(0x13, 0x3)
    EndChrThread(0x12, 0x0)
    EndChrThread(0x13, 0x0)
    EndChrThread(0x15, 0x1)
    Battle("BattleInfo_5E4", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    Call(0, 22)
    Return()

    # Function_14_2058 end

    def Function_15_2437(): pass

    label("Function_15_2437")

    OP_93(0xFE, 0xF0, 0x0)
    OP_74(0x8, 0xA)
    OP_71(0x8, 0x0, 0x5, 0x0, 0x8)
    OP_79(0x8)
    OP_74(0x8, 0x1E)
    Sleep(100)

    def lambda_245D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_245D)
    OP_96(0xFE, 0xFFFF19BA, 0x0, 0xFFFFF79A, 0x1388, 0x0)
    OP_93(0xFE, 0x13B, 0x1F4)
    WaitChrThread(0xFE, 2)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0x101, 0x26)
    SetChrSubChip(0x101, 0x0)
    Return()

    # Function_15_2437 end

    def Function_16_2497(): pass

    label("Function_16_2497")

    Sleep(1300)

    def lambda_249F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_249F)
    OP_95(0xFE, -57850, 0, -1050, 5000, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    WaitChrThread(0xFE, 2)
    SetChrChipByIndex(0x10B, 0x27)
    SetChrSubChip(0x10B, 0x0)
    Sound(802, 0, 100, 0)
    Sleep(50)
    SetChrSubChip(0x10B, 0x1)
    Return()

    # Function_16_2497 end

    def Function_17_24E0(): pass

    label("Function_17_24E0")

    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    OP_95(0xFE, -60700, 0, 4700, 5000, 0x1)
    OP_95(0xFE, -58250, 0, 4700, 5000, 0x1)
    OP_93(0xFE, 0xB4, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x1388, 0x1)
    Return()

    # Function_17_24E0 end

    def Function_18_2527(): pass

    label("Function_18_2527")

    OP_93(0xFE, 0xB4, 0x1F4)
    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x1388, 0x1)
    OP_93(0xFE, 0x5A, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x1388, 0x1)
    Return()

    # Function_18_2527 end

    def Function_19_255C(): pass

    label("Function_19_255C")

    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(500)
    OP_93(0xFE, 0x87, 0x1F4)
    Return()

    # Function_19_255C end

    def Function_20_256E(): pass

    label("Function_20_256E")

    Sleep(300)
    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x15, 1, 0, 11)
    BeginChrThread(0xFE, 0, 0, 10)
    OP_9B(0x0, 0xFE, 0x0, 0x1F40, 0x1388, 0x1)
    OP_93(0xFE, 0x5A, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x1388, 0x1)
    Return()

    # Function_20_256E end

    def Function_21_25BA(): pass

    label("Function_21_25BA")

    Sleep(600)
    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 0, 0, 10)
    OP_95(0xFE, -63150, 0, 6800, 5000, 0x1)
    OP_93(0xFE, 0xB4, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x1F40, 0x1388, 0x1)
    OP_93(0xFE, 0x5A, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x1388, 0x1)
    Return()

    # Function_21_25BA end

    def Function_22_261B(): pass

    label("Function_22_261B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch04152.itc", 0x1F)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrPos(0x101, -58950, 0, -2350, 270)
    SetChrChipByIndex(0x10B, 0x1F)
    SetChrSubChip(0x10B, 0x1)
    SetChrPos(0x10B, -57850, 0, -850, 270)
    ClearChrFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x8000)
    ClearChrFlags(0xC, 0x8000)
    ClearChrFlags(0xA, 0x40)
    ClearChrFlags(0xB, 0x40)
    ClearChrFlags(0xC, 0x40)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    Call(0, 23)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    OP_68(-59800, 1400, -1100, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24000, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(23000, 1000)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x101,
        "#00015F#11PKh...*pant pant*.\x02",
    )

    CloseMessageWindow()
    Fade(250)
    SetChrSubChip(0x10B, 0x0)
    Sleep(180)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0x10B, 0xFF)
    SetChrSubChip(0x10B, 0x0)
    OP_0D()
    Sleep(200)
    TurnDirection(0x10B, 0x101, 500)

    ChrTalk(
        0x10B,
        (
            "#11102F#5PEh eh......\x01",
            "Out of breath, huh?\x02\x03",
            "Do you think you'll be able to cut through\x01",
            "what lies ahead in that state?\x02",
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
            "#00006F#12PYeah, I don't think\x01",
            "I could alone, but...\x02\x03",
            "#00000FWith your help, it'll be possible\x01",
            "to breakout of prison.\x02\x03",
            "I'll use all of your strength.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10B,
        (
            "#11104F#5P...Hmph.\x01",
            "You've gotten serious.\x02\x03",
            "#11107FVery well...\x01",
            "We'll sneak the hell away from here!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_37()
    SetChrPos(0x0, -59350, 0, -1450, 270)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x183, 7)
    ModifyEventFlags(1, 0, 0x80)
    EventEnd(0x5)
    Return()

    # Function_22_261B end

    def Function_23_28F2(): pass

    label("Function_23_28F2")

    SetChrChipByIndex(0xA, 0x0)
    SetChrSubChip(0xA, 0x2)
    ClearChrFlags(0xA, 0x80)
    OP_52(0xA, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xA, 0x40)
    ClearChrFlags(0xA, 0x1)
    SetChrPos(0xA, -58400, 0, 1950, 180)
    SetChrChipByIndex(0xB, 0x0)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x80)
    OP_52(0xB, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xB, 0x40)
    ClearChrFlags(0xB, 0x1)
    SetChrPos(0xB, -63350, 0, -1400, 135)
    SetChrChipByIndex(0xC, 0x0)
    SetChrSubChip(0xC, 0x3)
    ClearChrFlags(0xC, 0x80)
    OP_52(0xC, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xC, 0x40)
    ClearChrFlags(0xC, 0x1)
    SetChrPos(0xC, -61500, 0, -3350, 90)
    Return()

    # Function_23_28F2 end

    def Function_24_298C(): pass

    label("Function_24_298C")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    LoadChrToIndex("chr/ch41450.itc", 0x1E)
    LoadChrToIndex("chr/ch41451.itc", 0x1F)
    LoadChrToIndex("chr/ch41550.itc", 0x20)
    LoadChrToIndex("chr/ch41551.itc", 0x21)
    LoadChrToIndex("monster/ch80850.itc", 0x22)
    LoadChrToIndex("monster/ch80851.itc", 0x23)
    LoadChrToIndex("chr/ch00050.itc", 0x24)
    LoadChrToIndex("chr/ch04150.itc", 0x25)
    SetChrPos(0x101, 70300, 0, 3500, 135)
    SetChrPos(0x10B, 69100, 0, 3500, 135)
    SetChrChipByIndex(0xD, 0x1E)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    SetChrPos(0xD, 92000, 0, 1000, 180)
    SetChrFlags(0xD, 0x40)
    SetChrChipByIndex(0xE, 0x1E)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)
    SetChrPos(0xE, 91300, 0, -1500, 0)
    SetChrFlags(0xE, 0x40)
    SetChrChipByIndex(0xF, 0x1E)
    SetChrSubChip(0xF, 0x0)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xF, 92700, 0, -1500, 0)
    SetChrFlags(0xF, 0x40)
    SetChrChipByIndex(0x10, 0x20)
    SetChrSubChip(0x10, 0x0)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x8000)
    SetChrPos(0x10, 91300, 0, -3000, 0)
    SetChrFlags(0x10, 0x40)
    SetChrChipByIndex(0x11, 0x20)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8000)
    SetChrPos(0x11, 92700, 0, -3000, 0)
    SetChrFlags(0x11, 0x40)
    SetChrChipByIndex(0x12, 0x22)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0x12, 96000, 0, 500, 270)
    SetChrFlags(0x12, 0x20)
    OP_52(0x12, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x12, 0, 0, 9)
    SetChrChipByIndex(0x13, 0x22)
    SetChrSubChip(0x13, 0x0)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, 96000, 0, -1000, 270)
    SetChrFlags(0x13, 0x20)
    OP_52(0x13, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x13, 0, 0, 9)
    SetChrChipByIndex(0x14, 0x22)
    SetChrSubChip(0x14, 0x0)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x14, 96000, 0, -2500, 270)
    SetChrFlags(0x14, 0x20)
    OP_52(0x14, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x14, 0, 0, 9)
    OP_68(70000, 1000, 3500, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(26500, 0)
    SetCameraDistance(25500, 1000)
    FadeToBright(1000, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x184, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D04")
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x10B, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(92000, 1000, -1000, 3000)
    MoveCamera(45, 23, 0, 3000)
    OP_6E(400, 3000)
    SetCameraDistance(25500, 3000)
    OP_6F(0x79)
    SetCameraDistance(24500, 3000)
    OP_6F(0x79)
    Fade(500)
    OP_68(70000, 1000, 3500, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25500, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00013F#5P(Too many...\x01",
            "But, if we can break through...!)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10B,
        (
            "#11100F#5P(Hmph, are we gonna punch\x01",
            "all of 'em hard now?)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x184, 0)

    label("loc_2D04")

    OP_0D()
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Charge In Now\x01",        # 0
            "Prepare For Now\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2D5D"),
        (1, "loc_3369"),
        (SWITCH_DEFAULT, "loc_33FB"),
    )


    label("loc_2D5D")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(92390, 1000, -960, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25500, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0xD,
        "#5P──The fugitives are two!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#5PThey seem to be the former mafia executive\x01",
            "Garcｵa and the Support Section Bannings!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#5POn the pride of the State Guard,\x01",
            "don't let them get out of prison!!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    SetMessageWindowPos(260, 30, -1, -1)
    OP_82(0xC8, 0x0, 0xBB8, 0x190)
    SetChrName("State Guard Soldiers")

    AnonymousTalk(
        0xFF,
        "#4SYessir!!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x10B,
        "#11109FHah! ...So you've got pride, huh?\x02",
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_2F6F():
        OP_93(0xD, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 0, lambda_2F6F)
    Sleep(50)

    def lambda_2F7F():
        OP_93(0xE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_2F7F)
    Sleep(50)

    def lambda_2F8F():
        OP_93(0xF, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 0, lambda_2F8F)
    Sleep(50)

    def lambda_2F9F():
        OP_93(0x10, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_2F9F)
    Sleep(50)

    def lambda_2FAF():
        OP_93(0x11, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_2FAF)
    Sleep(50)
    WaitChrThread(0xD, 0)
    WaitChrThread(0xE, 0)
    WaitChrThread(0xF, 0)
    WaitChrThread(0x10, 0)
    WaitChrThread(0x11, 0)
    Fade(500)
    SetChrPos(0x101, 78700, 0, -1000, 90)
    SetChrPos(0x10B, 78700, 0, 400, 90)
    OP_68(92000, 1000, 1000, 0)
    MoveCamera(315, 23, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25500, 0)
    OP_68(85500, 1000, 1000, 3000)

    def lambda_3039():
        OP_9B(0x0, 0x101, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3039)
    Sleep(0)

    def lambda_3051():
        OP_9B(0x0, 0x10B, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10B, 0, lambda_3051)
    Sleep(0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x10B, 0)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0xE,
        "#11PWha...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#11PD-Did you come down already!?\x02",
    )

    CloseMessageWindow()
    Fade(250)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0x101, 0x24)
    SetChrSubChip(0x101, 0x0)
    BeginChrThread(0x101, 0, 0, 28)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00007F#5PI'm sorry, but...\x01",
            "We'll force our way through!\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    Sound(802, 0, 100, 0)
    Sound(908, 0, 100, 0)
    SetChrChipByIndex(0x10B, 0x25)
    SetChrSubChip(0x10B, 0x0)
    BeginChrThread(0x10B, 0, 0, 29)
    OP_0D()

    ChrTalk(
        0x10B,
        (
            "#11102F#5PEh eh, won't you show me\x01",
            "that pride or whatever of yours?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(90000, 1000, 0, 0)
    MoveCamera(315, 23, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(28500, 0)
    OP_0D()
    Sleep(300)
    OP_82(0xC8, 0x0, 0xBB8, 0x190)

    ChrTalk(
        0xD,
        "#11P#4SKh...charge!!\x02",
    )

    CloseMessageWindow()
    OP_68(85000, 1000, 0, 1000)
    SetCameraDistance(25500, 1000)
    SetChrChipByIndex(0xE, 0x1F)
    SetChrSubChip(0xE, 0x0)

    def lambda_31F4():
        OP_9B(0x0, 0xFE, 0x2, 0x1F40, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_31F4)
    Sleep(100)
    SetChrChipByIndex(0x10, 0x21)
    SetChrSubChip(0x10, 0x0)

    def lambda_3214():
        OP_9B(0x0, 0xFE, 0x2, 0x1F40, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_3214)
    Sleep(100)
    SetChrChipByIndex(0xF, 0x1F)
    SetChrSubChip(0xF, 0x0)

    def lambda_3234():
        OP_9B(0x0, 0xFE, 0x2, 0x1F40, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_3234)
    Sleep(50)
    SetChrChipByIndex(0x12, 0x23)
    SetChrSubChip(0x12, 0x0)
    OP_52(0x12, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x15, 1, 0, 11)
    BeginChrThread(0x12, 0, 0, 10)

    def lambda_326B():
        OP_9B(0x0, 0xFE, 0x2, 0x1F40, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_326B)
    SetChrChipByIndex(0x13, 0x23)
    SetChrSubChip(0x13, 0x0)
    OP_52(0x13, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x13, 0, 0, 10)

    def lambda_3299():
        OP_9B(0x0, 0xFE, 0x2, 0x1F40, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_3299)
    SetChrChipByIndex(0x14, 0x23)
    SetChrSubChip(0x14, 0x0)
    OP_52(0x14, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x14, 0, 0, 10)

    def lambda_32C7():
        OP_9B(0x0, 0xFE, 0x2, 0x1F40, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_32C7)
    Sleep(50)
    SetChrChipByIndex(0x11, 0x21)
    SetChrSubChip(0x11, 0x0)

    def lambda_32E7():
        OP_9B(0x0, 0xFE, 0x2, 0x1F40, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_32E7)
    SetCameraDistance(20500, 500)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    Sleep(500)
    EndChrThread(0xD, 0x1)
    EndChrThread(0xE, 0x1)
    EndChrThread(0xF, 0x1)
    EndChrThread(0x10, 0x1)
    EndChrThread(0x11, 0x1)
    EndChrThread(0x12, 0x1)
    EndChrThread(0x13, 0x1)
    EndChrThread(0x14, 0x1)
    EndChrThread(0x12, 0x0)
    EndChrThread(0x13, 0x0)
    EndChrThread(0x14, 0x0)
    EndChrThread(0x15, 0x1)
    EndChrThread(0x101, 0x0)
    EndChrThread(0x10B, 0x0)
    Battle("BattleInfo_628", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    Call(0, 25)
    Jump("loc_33FB")

    label("loc_3369")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrFlags(0xD, 0x80)
    ClearChrFlags(0xD, 0x8000)
    ClearChrFlags(0xD, 0x40)
    SetChrFlags(0xE, 0x80)
    ClearChrFlags(0xE, 0x8000)
    ClearChrFlags(0xE, 0x40)
    SetChrFlags(0xF, 0x80)
    ClearChrFlags(0xF, 0x8000)
    ClearChrFlags(0xF, 0x40)
    SetChrFlags(0x10, 0x80)
    ClearChrFlags(0x10, 0x8000)
    ClearChrFlags(0x10, 0x40)
    SetChrFlags(0x11, 0x80)
    ClearChrFlags(0x11, 0x8000)
    ClearChrFlags(0x11, 0x40)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    OP_D7(0x22)
    OP_D7(0x23)
    OP_D7(0x24)
    OP_D7(0x25)
    OP_37()
    SetChrPos(0x0, 70000, 0, 5000, 180)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Jump("loc_33FB")

    label("loc_33FB")

    Return()

    # Function_24_298C end

    def Function_25_33FC(): pass

    label("Function_25_33FC")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch04150.itc", 0x1F)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrPos(0x101, 86700, 0, -1000, 90)
    BeginChrThread(0x101, 0, 0, 28)
    SetChrChipByIndex(0x10B, 0x1F)
    SetChrSubChip(0x10B, 0x0)
    SetChrPos(0x10B, 86700, 0, 400, 90)
    BeginChrThread(0x10B, 0, 0, 29)
    ClearChrFlags(0xD, 0x8000)
    ClearChrFlags(0xE, 0x8000)
    ClearChrFlags(0xF, 0x8000)
    ClearChrFlags(0x10, 0x8000)
    ClearChrFlags(0x11, 0x8000)
    ClearChrFlags(0xD, 0x40)
    ClearChrFlags(0xE, 0x40)
    ClearChrFlags(0xF, 0x40)
    ClearChrFlags(0x10, 0x40)
    ClearChrFlags(0x11, 0x40)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    Call(0, 30)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    OP_68(90500, 1000, 0, 0)
    MoveCamera(315, 23, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24000, 0)
    FadeToBright(1000, 0)
    OP_68(86890, 1000, 250, 3000)
    OP_6F(0x79)
    OP_0D()
    Sleep(200)

    ChrTalk(
        0x101,
        "#00006F#5P*phew*...somehow we made it.\x02",
    )

    CloseMessageWindow()
    Fade(250)
    EndChrThread(0x101, 0x0)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Sleep(50)
    EndChrThread(0x10B, 0x0)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0x10B, 0xFF)
    SetChrSubChip(0x10B, 0x0)
    OP_0D()
    TurnDirection(0x101, 0x10B, 500)
    Sleep(100)

    ChrTalk(
        0x101,
        (
            "#00004F#6PAt any rate, you...\x01",
            "You've really got a tremendous fighting strength.\x02\x03",
            "#00000FRandy and the Red Constellation\x01",
            "boss were fairly strong, but...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10B, 0x101, 500)

    ChrTalk(
        0x10B,
        (
            "#11103F#11PHmph...\x01",
            "The "Ogre Rosso", Sigmund, eh?\x02\x03",
            "#11100FI encountered him many times in my jaeger days, \x01",
            "and frankly speakin', he was a real monster.\x02\x03",
            "Accordin' to rumors I've heard,\x01",
            "his daughter too is quite dangerous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001F#6PYeah... For pure fighting strength, maybe\x01",
            "she's stronger than the "Society" guys.\x02\x03",
            "#00006FWell, although even among the\x01",
            ""Society" there'e some crazy ones...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10B,
        (
            "#11104F#11PEh eh, and you need to go at it\x01",
            "with such monsters in the future.\x02\x03",
            "#11102FGrim prospects, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#6PYeah, you can say that.\x02",
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(91750, 1800, -4000, 0)
    OP_68(91750, 1000, -4000, 4000)
    MoveCamera(315, 26, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25500, 0)
    BeginChrThread(0x101, 3, 0, 26)
    BeginChrThread(0x10B, 3, 0, 27)
    WaitChrThread(0x101, 3)
    VolumeBGM(0x50, 0x1F4)
    WaitChrThread(0x10B, 3)
    OP_6F(0x79)
    Sound(807, 0, 100, 0)
    Sleep(300)
    VolumeBGM(0x64, 0x7D0)

    ChrTalk(
        0x101,
        (
            "#00001F#11PIt's locked...\x02\x03",
            "I think we can unlock\x01",
            "it nearby, though.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(91750, 1000, -2500, 1000)
    OP_93(0x10B, 0x0, 0x1F4)
    Sleep(500)
    OP_93(0x101, 0x0, 0x1F4)
    OP_6F(0x79)

    ChrTalk(
        0x10B,
        (
            "#11104F#5PHah, probably that room.\x02\x03",
            "#11100FLet's unlock it at once.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    SetCameraDistance(25150, 1000)
    OP_6F(0x79)
    OP_0D()
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_37()
    SetChrPos(0x0, 91400, 0, -4450, 0)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x184, 1)
    ModifyEventFlags(0, 0, 0x80)
    EventEnd(0x5)
    Return()

    # Function_25_33FC end

    def Function_26_3988(): pass

    label("Function_26_3988")

    OP_93(0xFE, 0x5A, 0x1F4)
    OP_95(0xFE, 90400, 0, -1800, 2300, 0x1)
    OP_95(0xFE, 92070, 0, -6230, 2500, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_26_3988 end

    def Function_27_39BF(): pass

    label("Function_27_39BF")

    Sleep(300)
    OP_93(0xFE, 0x87, 0x1F4)
    Sleep(700)
    OP_95(0xFE, 91230, 0, -2860, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_27_39BF end

    def Function_28_39E8(): pass

    label("Function_28_39E8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3A06")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x3, 0x4, 0x3)
    Jump("Function_28_39E8")

    label("loc_3A06")

    Return()

    # Function_28_39E8 end

    def Function_29_3A07(): pass

    label("Function_29_3A07")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3A22")
    OP_A1(0xFE, 0x3E8, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_29_3A07")

    label("loc_3A22")

    Return()

    # Function_29_3A07 end

    def Function_30_3A23(): pass

    label("Function_30_3A23")

    SetChrChipByIndex(0xD, 0x0)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x80)
    OP_52(0xD, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xD, 0x40)
    ClearChrFlags(0xD, 0x1)
    SetChrPos(0xD, 93100, 0, -950, 45)
    SetChrChipByIndex(0xE, 0x0)
    SetChrSubChip(0xE, 0x2)
    ClearChrFlags(0xE, 0x80)
    OP_52(0xE, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xE, 0x40)
    ClearChrFlags(0xE, 0x1)
    SetChrPos(0xE, 90000, 0, 2100, 270)
    SetChrChipByIndex(0xF, 0x0)
    SetChrSubChip(0xF, 0x2)
    ClearChrFlags(0xF, 0x80)
    OP_52(0xF, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xF, 0x40)
    ClearChrFlags(0xF, 0x1)
    SetChrPos(0xF, 89150, 0, -3300, 315)
    SetChrChipByIndex(0x10, 0x0)
    SetChrSubChip(0x10, 0x1)
    ClearChrFlags(0x10, 0x80)
    OP_52(0x10, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x10, 0x40)
    ClearChrFlags(0x10, 0x1)
    SetChrPos(0x10, 94350, 0, -3850, 270)
    SetChrChipByIndex(0x11, 0x0)
    SetChrSubChip(0x11, 0x3)
    ClearChrFlags(0x11, 0x80)
    OP_52(0x11, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x11, 0x40)
    ClearChrFlags(0x11, 0x1)
    SetChrPos(0x11, 96050, 0, -200, 90)
    Return()

    # Function_30_3A23 end

    def Function_31_3B23(): pass

    label("Function_31_3B23")

    EventBegin(0x0)
    Fade(500)
    OP_68(148250, 1000, 3250, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24500, 0)
    SetChrPos(0x101, 148100, 0, 3000, 90)
    SetChrPos(0x10B, 147000, 0, 3250, 90)
    OP_0D()
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x8)
    Sleep(150)
    Sound(139, 0, 100, 0)
    OP_79(0x1)
    Fade(500)
    Sound(140, 0, 100, 0)
    SetMapObjFlags(0x1, 0x4)
    ClearMapObjFlags(0x2, 0x4)
    OP_0D()
    Sleep(500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(92000, 1000, -5500, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25500, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(24500, 2500)
    OP_6F(0x79)
    OP_0D()
    Sound(454, 0, 100, 0)
    Sound(147, 0, 100, 0)
    OP_82(0x0, 0x19, 0x1388, 0x7D0)
    OP_74(0xA, 0x1E)
    OP_71(0xA, 0x2D, 0x0, 0x0, 0x8)
    OP_79(0xA)
    OP_82(0x32, 0x0, 0x1388, 0x1F4)
    ClearMapObjFlags(0xA, 0x2)
    Sleep(1000)
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_68(148250, 1000, 3250, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24500, 0)
    FadeToBright(500, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x101,
        "#00002F#5PAll right...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10B,
        "#11100F#5PGood, let's get out at once.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 147480, 0, 3020, 270)
    OP_69(0xFF, 0x0)
    OP_65(0x0, 0x1)
    SetScenarioFlags(0x184, 2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x184, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D07")
    ModifyEventFlags(1, 1, 0x80)

    label("loc_3D07")

    EventEnd(0x5)
    Return()

    # Function_31_3B23 end

    def Function_32_3D0A(): pass

    label("Function_32_3D0A")

    EventBegin(0x0)
    Fade(500)
    OP_68(147740, 1000, -1680, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24500, 0)
    SetChrPos(0x101, 147000, 0, -2300, 180)
    SetChrPos(0x10B, 146700, 0, -1200, 180)
    OP_0D()
    Sleep(300)
    Sound(14, 0, 100, 0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x8)
    OP_79(0x0)
    Sleep(200)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "You recovered all the equipment, items\x01",
            "and the ENIGMA II they took from you.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00006F#5PThank goodness...\x01",
            "So they were stored here, eh?\x02\x03",
            "#00002FIt seems that all\x01",
            "Quartzes are here too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10B,
        (
            "#11103F#5PHey, let's go now.\x02\x03",
            "#11100FUnless you want to be surrounded\x01",
            "by soldiers and thrown back inside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#5PYeah...!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 147000, 0, -1800, 0)
    OP_69(0xFF, 0x0)
    OP_65(0x1, 0x1)
    SetScenarioFlags(0x184, 3)
    ModifyEventFlags(0, 1, 0x80)
    OP_C7(0x1, 0x0)
    OP_32(0x0, 0x11, 0x0)
    OP_DA(0x2)
    EventEnd(0x5)
    Return()

    # Function_32_3D0A end

    def Function_33_3F2F(): pass

    label("Function_33_3F2F")

    EventBegin(0x0)
    Fade(500)
    OP_68(144140, 1000, 3510, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24500, 0)
    SetChrPos(0x101, 144000, 0, 3650, 270)
    SetChrPos(0x10B, 145500, 0, 4150, 270)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00005F#5P(Now that I think about it...\x01",
            "The equipment and possessions they took\x01",
            "away from me should be stored somewhere.)\x02\x03",
            "#00008F(Could it be...)\x02",
        )
    )

    CloseMessageWindow()
    OP_68(147390, 1000, -2320, 1500)
    SetCameraDistance(23010, 1500)

    def lambda_4059():
        OP_93(0x101, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4059)
    Sleep(200)

    def lambda_4069():
        OP_93(0x10B, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10B, 0, lambda_4069)
    Sleep(200)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x10B, 0)
    OP_6F(0x79)
    Sleep(500)
    SetChrPos(0x0, 145760, 0, 3760, 90)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_33_3F2F end

    SaveToFile()

Try(main)
