﻿from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "m4000.bin",                # FileName
        "m4000",                    # MapName
        "m4000",                    # Location
        0x007A,                     # MapIndex
        "ed7151",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x2B,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 122, 0, 2, 0, 3],
    )

    BuildStringList((
        "m4000",                  # 0
        "Republic Military Officer",# 1
        "イベント用モンスター",   # 2
        "イベント用モンスター",   # 3
        "bm4000",                 # 4
    ))

    ATBonus("ATBonus_13C", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_15C", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_160", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_164", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_168", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_16C", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_170", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_174", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_178", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_1DC", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_1E0", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_1E4", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_1E8", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_1EC", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_1F0", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_1F4", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_1F8", 5, 5, 45)

    # monster count: 0

    # event battle count: 1

    BattleInfo(
        "BattleInfo_1FC", 0x0002, 3, 6, 45, 3, 3, 30, 0, "bm4000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms72200.dat", "ms72200.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_15C", "MonsterBattlePostion_1DC", "ed7452", "ed7453", "ATBonus_13C"),
            (),
            (),
            (),
        )
    )

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(4294960636, 0,       27520,   1200,    4294960636, 2000,    27520,   0x007C, 0,  4,  0x0000)

    ChipFrameInfo(620, 0)                                        # 0

    ScpFunction((
        "Function_0_26C",          # 00, 0
        "Function_1_28B",          # 01, 1
        "Function_2_2AA",          # 02, 2
        "Function_3_306",          # 03, 3
        "Function_4_33E",          # 04, 4
        "Function_5_67B",          # 05, 5
        "Function_6_196D",         # 06, 6
        "Function_7_19C8",         # 07, 7
        "Function_8_1A60",         # 08, 8
        "Function_9_1AF8",         # 09, 9
        "Function_10_1B8C",        # 0A, 10
    ))


    def Function_0_26C(): pass

    label("Function_0_26C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_28A")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_0_26C")

    label("loc_28A")

    Return()

    # Function_0_26C end

    def Function_1_28B(): pass

    label("Function_1_28B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2A9")
    OP_A1(0xFE, 0x4B0, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_1_28B")

    label("loc_2A9")

    Return()

    # Function_1_28B end

    def Function_2_2AA(): pass

    label("Function_2_2AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_2BC")
    ClearScenarioFlags(0x22, 0)
    Event(0, 5)
    SetScenarioFlags(0x0, 0)

    label("loc_2BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x37, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2D2")
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x2B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_305")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_305")
    SetChrPos(0x0, -6660, 0, 27520, 180)
    OP_31(0x1)
    OP_69(0xFF, 0x0)
    ClearMapFlags(0x8000000)

    label("loc_305")

    Return()

    # Function_2_2AA end

    def Function_3_306(): pass

    label("Function_3_306")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_31B")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 0)

    label("loc_31B")

    MiniGame(0x2F, 0xFFFFFFFF, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Return()

    # Function_3_306 end

    def Function_4_33E(): pass

    label("Function_4_33E")

    SetMapFlags(0x80)
    SetMapFlags(0x8000000)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x31, 2)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_370")
    SetScenarioFlags(0x31, 2)

    label("loc_370")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3B6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_3B0")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3A5")
    Sound(2499, 255, 100, 0)
    Jump("loc_3AB")

    label("loc_3A5")

    Sound(3537, 255, 100, 0)

    label("loc_3AB")

    Jump("loc_3B6")

    label("loc_3B0")

    Sound(3344, 255, 100, 0)

    label("loc_3B6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_66D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_42B")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "Board Merkabah")
    MenuCmd(1, 0, "Cancel")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_40B"),
        (SWITCH_DEFAULT, "loc_41C"),
    )


    label("loc_40B")

    SetScenarioFlags(0x22, 0)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Jump("loc_426")

    label("loc_41C")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_426")

    Jump("loc_668")

    label("loc_42B")

    MenuCmd(0, 0)
    MenuCmd(1, 0, "Use Orbal Car")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_45D")
    MenuCmd(1, 0, "Rest in Orbal Car")

    label("loc_45D")

    MenuCmd(1, 0, "Cancel")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_491"),
        (1, "loc_595"),
        (2, "loc_626"),
        (SWITCH_DEFAULT, "loc_65E"),
    )


    label("loc_491")

    SetMapObjFrame(0x0, "light", 0x0, 0x1)
    OP_74(0x0, 0x1E)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4C2")
    OP_70(0x0, 0x12C)
    OP_71(0x0, 0x12C, 0x14A, 0x0, 0x0)
    Jump("loc_4D2")

    label("loc_4C2")

    OP_70(0x0, 0xF0)
    OP_71(0x0, 0xF0, 0x10E, 0x0, 0x0)

    label("loc_4D2")

    Sound(462, 0, 100, 0)
    SoundLoad(2500)
    SoundLoad(3538)
    SoundLoad(3345)
    Sleep(700)
    FadeToDark(300, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_528")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_528")

    FadeToDark(0, 0, -1)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_54B")
    Sound(461, 0, 100, 0)

    label("loc_54B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_56B")
    OP_70(0x0, 0x14A)
    OP_71(0x0, 0x14A, 0x12C, 0x0, 0x0)
    Jump("loc_57B")

    label("loc_56B")

    OP_70(0x0, 0x10E)
    OP_71(0x0, 0x10E, 0xF0, 0x0, 0x0)

    label("loc_57B")

    Sleep(1000)
    OP_0D()
    SetMapObjFrame(0x0, "light", 0x1, 0x1)
    OP_70(0x0, 0x0)
    Jump("loc_3B6")

    label("loc_595")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_607")
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 0)), scpexpr(EXPR_END)), "loc_5CA")
    OP_32(0xFF, 0xFF, 0x0)
    Jump("loc_5E2")

    label("loc_5CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_5DD")
    OP_32(0xFF, 0xFE, 0x0)
    Jump("loc_5E2")

    label("loc_5DD")

    OP_32(0xFF, 0xFA, 0x0)

    label("loc_5E2")

    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_621")

    label("loc_607")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_617")
    OP_AF(0xFB)
    Jump("loc_621")

    label("loc_617")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_621")

    Jump("loc_668")

    label("loc_626")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_63F")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_659")

    label("loc_63F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_64F")
    OP_AF(0xFB)
    Jump("loc_659")

    label("loc_64F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_659")

    Jump("loc_668")

    label("loc_65E")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_668")

    Jump("loc_3B6")

    label("loc_66D")

    ClearMapFlags(0x8000000)
    OP_60(0x0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    # Function_4_33E end

    def Function_5_67B(): pass

    label("Function_5_67B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 7)), scpexpr(EXPR_END)), "loc_686")
    OutputDebugInt(0xC8)

    label("loc_686")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5A, 0)), scpexpr(EXPR_END)), "loc_691")
    OutputDebugInt(0x6F)

    label("loc_691")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetScenarioFlags(0x20, 0)
    OP_C9(0x0, 0x10000)
    SetScenarioFlags(0x20, 2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 3)), scpexpr(EXPR_END)), "loc_6BB")
    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 4)), scpexpr(EXPR_END)), "loc_6CD")
    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 5)), scpexpr(EXPR_END)), "loc_6DF")
    OP_50(0x67, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 5)), scpexpr(EXPR_END)), "loc_6EB")
    SetScenarioFlags(0x2C, 0)

    label("loc_6EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 6)), scpexpr(EXPR_END)), "loc_700")
    SetScenarioFlags(0x2C, 2)
    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_700")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 7)), scpexpr(EXPR_END)), "loc_715")
    SetScenarioFlags(0x2C, 4)
    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_715")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF1, 0)), scpexpr(EXPR_END)), "loc_72A")
    SetScenarioFlags(0x2C, 6)
    OP_50(0x67, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_72A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x21), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_740")
    AddMira(20000)
    Jump("loc_76F")

    label("loc_740")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x21), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_756")
    AddMira(10000)
    Jump("loc_76F")

    label("loc_756")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x21), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_76C")
    AddMira(5000)
    Jump("loc_76F")

    label("loc_76C")

    AddMira(2000)

    label("loc_76F")

    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    AddParty(0x8, 0xFF, 0xFF)
    AddParty(0x9, 0xFF, 0xFF)
    AddParty(0x7, 0xFF, 0xFF)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch02950.itc", 0x1F)
    LoadChrToIndex("chr/ch00950.itc", 0x20)
    LoadChrToIndex("chr/ch02450.itc", 0x21)
    LoadChrToIndex("chr/ch41200.itc", 0x22)
    LoadChrToIndex("monster/ch72250.itc", 0x23)
    LoadChrToIndex("monster/ch72250.itc", 0x24)
    LoadChrToIndex("monster/ch72252.itc", 0x25)
    CreatePortrait(0, 16, 20, 528, 84, 0, 10, 512, 64, 0, 0, 512, 64, 0xFFFFFF, 0x0, "c_vis500.itp")
    SoundLoad(3306)
    SoundLoad(3307)
    SoundLoad(3308)
    SoundLoad(3309)
    SoundLoad(3310)
    SoundLoad(3508)
    SoundLoad(3509)
    SoundLoad(3510)
    SoundLoad(3443)
    SoundLoad(3444)
    SoundLoad(3445)
    SoundLoad(3446)
    SoundLoad(3447)
    SoundLoad(4042)
    SoundLoad(4043)
    SoundLoad(4044)
    SoundLoad(4045)
    SoundLoad(4046)
    SetChrPos(0x101, 31000, 0, -56000, 330)
    SetChrPos(0x109, 31000, 0, -56000, 330)
    SetChrPos(0x108, 31000, 0, -56000, 330)
    SetChrPos(0x10A, 31000, 0, -56000, 330)
    SetChrPos(0x8, 31000, 0, -56000, 330)
    SetChrChipByIndex(0x8, 0x22)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrChipByIndex(0x9, 0x23)
    SetChrSubChip(0x9, 0x0)
    SetChrFlags(0x9, 0x8000)
    OP_A7(0x9, 0x0, 0x0, 0x0, 0x0, 0x0)
    SetChrPos(0x9, 1300, 0, 55000, 180)
    SetChrChipByIndex(0xA, 0x23)
    SetChrSubChip(0xA, 0x0)
    SetChrFlags(0xA, 0x8000)
    OP_A7(0xA, 0x0, 0x0, 0x0, 0x0, 0x0)
    SetChrPos(0xA, 2000, 0, 55000, 180)
    Sleep(1000)
    OP_C9(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            "#30W#40ASeptian Calendar 1204─\x01",
            "On a certain month",
            scpstr(0x6),
            scpstr(SCPSTR_CODE_ENTER),
        )
    )

    CloseMessageWindow()
    Sleep(1000)

    AnonymousTalk(
        0xFF,
        (
            "#30W#50AWestern Border of the\x01",
            "Calvard Republic,\x01",
            "Outskirts of Altair City─",
            scpstr(0x6),
            scpstr(SCPSTR_CODE_ENTER),
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x800)
    OP_68(23000, 2000, -43500, 0)
    MoveCamera(340, 23, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(36000, 0)
    PlayBGM("ed7151", 0)
    MoveCamera(325, 23, 0, 14000)
    SetCameraDistance(30000, 14000)
    FadeToBright(2000, 0)
    BeginChrThread(0x8, 3, 0, 6)
    Sleep(1000)
    BeginChrThread(0x101, 3, 0, 6)
    Sleep(800)
    BeginChrThread(0x109, 3, 0, 6)
    Sleep(800)
    BeginChrThread(0x108, 3, 0, 6)
    Sleep(800)
    BeginChrThread(0x10A, 3, 0, 6)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    OP_68(8000, 2000, -26600, 0)
    MoveCamera(335, 23, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(16000, 0)
    OP_68(8000, 2000, -20600, 5500)
    MoveCamera(335, 7, 0, 5500)
    SetCameraDistance(18000, 5500)
    EndChrThread(0x8, 0xFF)
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x109, 0xFF)
    EndChrThread(0x108, 0xFF)
    EndChrThread(0x10A, 0xFF)
    SetChrPos(0x8, 8000, 0, -31600, 0)
    SetChrPos(0x101, 8000, 0, -34400, 0)
    SetChrPos(0x109, 8400, 0, -36100, 0)
    SetChrPos(0x108, 6600, 0, -35100, 0)
    SetChrPos(0x10A, 7000, 0, -36500, 0)

    def lambda_AC0():
        OP_97(0x8, 0x0, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_AC0)
    Sleep(50)

    def lambda_ADD():
        OP_97(0x101, 0x0, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_ADD)
    Sleep(50)

    def lambda_AFA():
        OP_97(0x109, 0x0, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_AFA)
    Sleep(50)

    def lambda_B17():
        OP_97(0x108, 0x0, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 0, lambda_B17)
    Sleep(50)

    def lambda_B34():
        OP_97(0x10A, 0x0, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_B34)
    Sleep(50)
    WaitChrThread(0x8, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x108, 0)
    WaitChrThread(0x10A, 0)
    OP_6F(0x79)
    Sleep(500)

    ChrTalk(
        0x8,
        "...Here we are.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x101,
        "#00005F#3306V#5P#30WAh!\x02",
    )

    CloseMessageWindow()
    OP_24(0xCEA)
    OP_68(2000, 5000, 46000, 5000)
    MoveCamera(21, 17, 0, 5000)
    SetCameraDistance(42000, 5000)
    OP_6F(0x79)
    Sleep(500)
    Fade(1000)
    OP_68(2110, 23000, 50810, 0)
    MoveCamera(357, -7, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(55000, 0)
    OP_68(2110, 13000, 51000, 8000)
    Sleep(2000)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(3500)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_6F(0x79)
    Sleep(300)
    SetMessageWindowPos(14, 280, -1, 3)

    ChrTalk(
        0x108,
        (
            "#01400F#4042V#3P#N#30W...Hasn't changed at\x01",
            "all, huh.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00001F#3307V#4P#N#30WSo this is Altair\x01",
            "Lodge...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x109,
        (
            "#10101F#3508V#4P#N#30WSo this is where Tio was\x01",
            "rescued 6 years ago...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x10A,
        (
            "#00601F#3443V#3P#N#30WHmph... Such a\x01",
            "distasteful entrance.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x1, 0x80000000)
    OP_24(0xD73)
    Fade(500)
    OP_68(2000, 1100, 33600, 0)
    MoveCamera(330, 13, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(20500, 0)
    SetCameraDistance(17500, 3000)
    SetChrPos(0x101, 2000, 0, 27600, 0)
    SetChrPos(0x109, 2400, 0, 25900, 0)
    SetChrPos(0x108, 600, 0, 26900, 0)
    SetChrPos(0x10A, 1000, 0, 25500, 0)
    SetChrPos(0x8, 2000, 0, 30400, 0)

    def lambda_DF9():
        OP_97(0x8, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_DF9)
    Sleep(50)

    def lambda_E16():
        OP_97(0x101, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_E16)
    Sleep(50)

    def lambda_E33():
        OP_97(0x109, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_E33)
    Sleep(50)

    def lambda_E50():
        OP_97(0x108, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 0, lambda_E50)
    Sleep(50)

    def lambda_E6D():
        OP_97(0x10A, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_E6D)
    Sleep(50)
    WaitChrThread(0x8, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x108, 0)
    WaitChrThread(0x10A, 0)
    OP_6F(0x79)
    TurnDirection(0x8, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#11PThis is as far as I'll\x01",
            "take you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PI'll leave this place in\x01",
            "your hands until 17:00\x01",
            "today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PIf you fail to meet the\x01",
            "deadline, our army\x01",
            "forces will take over.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x10A,
        "#3P#00603F#3444V...Understood.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x108,
        (
            "#01400F#4043VThanks for taking us\x01",
            "this far.\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    OP_24(0xFCB)
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x8,
        "#11PJust try to be careful.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PThough you do have the famous Divine\x01",
            "Blade of Wind with you. There should\x01",
            "be nothing to worry about.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    def lambda_105E():

        label("loc_105E")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_105E")

    QueueWorkItem2(0x101, 2, lambda_105E)

    def lambda_1070():

        label("loc_1070")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_1070")

    QueueWorkItem2(0x109, 2, lambda_1070)

    def lambda_1082():

        label("loc_1082")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_1082")

    QueueWorkItem2(0x108, 2, lambda_1082)

    def lambda_1094():

        label("loc_1094")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_1094")

    QueueWorkItem2(0x10A, 2, lambda_1094)

    def lambda_10A6():
        OP_95(0xFE, 3800, 0, 31600, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_10A6)
    WaitChrThread(0x8, 1)
    OP_68(2000, 1100, 31600, 3000)

    def lambda_10D5():
        OP_95(0xFE, 1000, 0, 21000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_10D5)
    WaitChrThread(0x8, 1)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x109, 0x2)
    EndChrThread(0x108, 0x2)
    EndChrThread(0x10A, 0x2)
    SetChrFlags(0x8, 0x80)
    OP_6F(0x79)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x109,
        (
            "#12P#10106F#3509V#30WHmm... I get the\x01",
            "impression that we're\x01",
            "not really welcome here.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00006F#3308V#11P#30WWell, from their perspective,\x01",
            "outsiders are taking care of\x01",
            "criminals in their own territory.\x02\x03",
            "#00001F#3309VSo what do we do? Just go ahead\x01",
            "and step right in?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1225():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_1225)
    Sleep(50)

    def lambda_1235():
        TurnDirection(0x108, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x108, 0, lambda_1235)
    Sleep(50)

    def lambda_1245():
        TurnDirection(0x109, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1245)
    Sleep(50)
    WaitChrThread(0x108, 0)
    WaitChrThread(0x109, 0)

    ChrTalk(
        0x10A,
        (
            "#6P#00603F#3445V#30WExactly, there's no time\x01",
            "to waste.\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xD75)
    TurnDirection(0x10A, 0x108, 500)
    Sleep(300)

    ChrTalk(
        0x10A,
        (
            "#6P#00601F#3446V#30W...MacLaine. How likely\x01",
            "are we to run into any\x01",
            "active traps?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_12FC():
        TurnDirection(0xFE, 0x108, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_12FC)
    Sleep(100)

    def lambda_130C():
        TurnDirection(0xFE, 0x108, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_130C)
    Sleep(200)

    ChrTalk(
        0x108,
        (
            "#01403F#4044V#5P#30WI assume most traps were\x01",
            "shut down in the raid 6\x01",
            "years ago.\x02\x03",
            "#01401F#4045VOn the other hand,\x01",
            "wandering monsters─\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xFCD)
    StopBGM(0xFA0)
    OP_93(0x108, 0x0, 0x1F4)
    Fade(250)
    SetChrChipByIndex(0x108, 0x21)
    SetChrSubChip(0x108, 0x0)
    Sound(932, 0, 100, 0)
    Sleep(100)
    Sound(531, 0, 30, 0)
    Sound(540, 0, 30, 0)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(2000, 1500, 47500, 2000)
    MoveCamera(330, 15, 0, 2000)
    OP_6E(650, 2000)
    SetCameraDistance(14500, 2000)

    def lambda_1458():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1458)
    Sleep(50)

    def lambda_1468():
        OP_93(0x10A, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_1468)
    Sleep(50)

    def lambda_1478():
        OP_93(0x109, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1478)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x10A, 0)
    WaitChrThread(0x109, 0)
    OP_6F(0x79)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7452", 0)
    Sound(831, 0, 100, 0)
    OP_82(0x0, 0x32, 0xBB8, 0x1B58)
    BeginChrThread(0x9, 3, 0, 7)
    Sleep(900)
    BeginChrThread(0xA, 3, 0, 8)
    Sleep(1000)
    OP_68(2000, 1500, 45500, 3500)
    SetCameraDistance(17500, 3500)
    OP_6F(0x79)
    Sleep(500)
    Fade(500)
    OP_68(1700, 1300, 34600, 0)
    MoveCamera(325, 13, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(16000, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x109, 0x1F)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x10A, 0x20)
    SetChrSubChip(0x10A, 0x0)
    Sound(805, 0, 100, 0)
    Sound(531, 0, 100, 0)
    OP_0D()
    WaitChrThread(0x9, 3)
    WaitChrThread(0xA, 3)

    ChrTalk(
        0x10A,
        "#3P#00610F#3447V#30WWhat!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10107F#3510V#30WM-Monsters...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00010F#3310V#30WFrom inside the lodge!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        "#01407F#4046V#30WHere they come!\x02",
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    OP_24(0xFCE)
    Sound(830, 0, 100, 0)
    OP_82(0x96, 0x0, 0xBB8, 0x3E8)
    BeginChrThread(0x9, 3, 0, 9)
    Sleep(50)
    BeginChrThread(0xA, 3, 0, 9)
    Sleep(1050)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetCameraDistance(13000, 500)
    Sleep(500)
    EndChrThread(0x9, 0x1)
    EndChrThread(0xA, 0x1)
    EndChrThread(0x9, 0x3)
    EndChrThread(0xA, 0x3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 7)), scpexpr(EXPR_END)), "loc_1651")
    OP_50(0x1F, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1771")

    label("loc_1651")

    OP_50(0x1F, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_50(0x1F, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    OP_50(0x1F, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    OP_50(0x1F, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    OP_50(0x1F, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    OP_50(0x1F, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    OP_50(0x1F, (scpexpr(EXPR_PUSH_LONG, 0x20), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    OP_50(0x1F, (scpexpr(EXPR_PUSH_LONG, 0x40), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    OP_50(0x1F, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    OP_50(0x1F, (scpexpr(EXPR_PUSH_LONG, 0x100), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    OP_50(0x1F, (scpexpr(EXPR_PUSH_LONG, 0x200), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    OP_50(0x1F, (scpexpr(EXPR_PUSH_LONG, 0x400), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    OP_50(0x1F, (scpexpr(EXPR_PUSH_LONG, 0x800), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    OP_50(0x1F, (scpexpr(EXPR_PUSH_LONG, 0x1000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    OP_50(0x1F, (scpexpr(EXPR_PUSH_LONG, 0x4000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    OP_50(0x1F, (scpexpr(EXPR_PUSH_LONG, 0x8000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    OP_50(0x1F, (scpexpr(EXPR_PUSH_LONG, 0x10000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    OP_50(0x1F, (scpexpr(EXPR_PUSH_LONG, 0x20000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    OP_50(0x1F, (scpexpr(EXPR_PUSH_LONG, 0x40000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    OP_50(0x1F, (scpexpr(EXPR_PUSH_LONG, 0x80000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    OP_50(0x1F, (scpexpr(EXPR_PUSH_LONG, 0x100000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    OP_50(0x1F, (scpexpr(EXPR_PUSH_LONG, 0x200000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    OP_50(0x1F, (scpexpr(EXPR_PUSH_LONG, 0x400000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    OP_50(0x1F, (scpexpr(EXPR_PUSH_LONG, 0x800000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    OP_50(0x1F, (scpexpr(EXPR_PUSH_LONG, 0x1000000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    OP_50(0x1F, (scpexpr(EXPR_PUSH_LONG, 0x2000000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    OP_50(0x1F, (scpexpr(EXPR_PUSH_LONG, 0x4000000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    OP_50(0x1F, (scpexpr(EXPR_PUSH_LONG, 0x8000000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    OP_50(0x1F, (scpexpr(EXPR_PUSH_LONG, 0x10000000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    OP_50(0x1F, (scpexpr(EXPR_PUSH_LONG, 0x20000000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    OP_50(0x1F, (scpexpr(EXPR_PUSH_LONG, 0x40000000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    OP_50(0x1F, (scpexpr(EXPR_PUSH_LONG, 0x80000000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_1771")

    OP_C9(0x1, 0x80)
    OP_32(0x0, 0x0, 0x2D)
    OP_32(0x0, 0x5, 0x5A)
    OP_42(0x0, 0x3E8, 0xFF)
    OP_42(0x0, 0x5DC, 0xFF)
    OP_42(0x0, 0x640, 0xFF)
    RemoveCraft(0x0, 0xFFFF)
    OP_38(0x0, 0x80, 0x2)
    OP_38(0x0, 0x82, 0x1)
    OP_38(0x0, 0x85, 0x1)
    AddCraft(0x0, 0x96)
    AddCraft(0x0, 0x97)
    AddCraft(0x0, 0x98)
    AddCraft(0x0, 0x99)
    AddCraft(0x0, 0x9A)
    AddCraft(0x0, 0x118)
    AddCraft(0x0, 0x119)
    SetChrChipPat(0x0, 0x6, 0x119)
    SetChrChipPat(0x0, 0x6, 0x11B)
    SetChrChipPat(0x0, 0x6, 0x11C)
    SetChrChipPat(0x0, 0x6, 0x11A)
    OP_32(0x8, 0x0, 0x2D)
    OP_32(0x8, 0x5, 0x5A)
    OP_42(0x8, 0x44C, 0xFF)
    OP_42(0x8, 0x5DC, 0xFF)
    OP_42(0x8, 0x640, 0xFF)
    RemoveCraft(0x8, 0xFFFF)
    OP_38(0x8, 0x80, 0x2)
    OP_38(0x8, 0x81, 0x1)
    OP_38(0x8, 0x84, 0x1)
    AddCraft(0x8, 0xE6)
    AddCraft(0x8, 0xE7)
    AddCraft(0x8, 0xE8)
    AddCraft(0x8, 0xE9)
    AddCraft(0x8, 0x140)
    SetChrChipPat(0x8, 0x6, 0x140)
    SetChrChipPat(0x8, 0x6, 0x143)
    OP_32(0x9, 0x0, 0x3C)
    OP_32(0x9, 0x5, 0xC8)
    OP_42(0x9, 0x465, 0xFF)
    OP_42(0x9, 0x5DC, 0xFF)
    OP_42(0x9, 0x640, 0xFF)
    OP_42(0x9, 0x4C, 0x3)
    OP_42(0x9, 0x49, 0x4)
    RemoveCraft(0x9, 0xFFFF)
    OP_38(0x9, 0x80, 0x2)
    OP_38(0x9, 0x82, 0x1)
    OP_38(0x9, 0x83, 0x1)
    OP_38(0x9, 0x84, 0x1)
    OP_42(0x9, 0xE8, 0x0)
    OP_42(0x9, 0x6C, 0x2)
    OP_42(0x9, 0xBA, 0x3)
    OP_42(0x9, 0x88, 0x4)
    AddCraft(0x9, 0xF5)
    AddCraft(0x9, 0xF1)
    AddCraft(0x9, 0xF7)
    AddCraft(0x9, 0xF3)
    AddCraft(0x9, 0xF4)
    AddCraft(0x9, 0x145)
    SetChrChipPat(0x9, 0x6, 0x145)
    SetChrChipPat(0x9, 0x6, 0x148)
    SetChrChipPat(0x9, 0x6, 0x146)
    OP_32(0x7, 0x0, 0x3C)
    OP_32(0x7, 0x5, 0xC8)
    OP_42(0x7, 0x46A, 0xFF)
    OP_42(0x7, 0x5DC, 0xFF)
    OP_42(0x7, 0x640, 0xFF)
    OP_42(0x7, 0x33, 0x3)
    OP_42(0x7, 0x51, 0x4)
    RemoveCraft(0x7, 0xFFFF)
    OP_38(0x7, 0x80, 0x2)
    OP_38(0x7, 0x81, 0x1)
    OP_38(0x7, 0x82, 0x1)
    OP_38(0x7, 0x85, 0x1)
    OP_38(0x7, 0x86, 0x1)
    OP_84(0x15, 0x4)
    OP_42(0x7, 0xF1, 0x0)
    OP_42(0x7, 0x6C, 0x1)
    OP_42(0x7, 0x7C, 0x2)
    OP_42(0x7, 0x80, 0x5)
    OP_42(0x7, 0x88, 0x6)
    AddCraft(0x7, 0xDC)
    AddCraft(0x7, 0xDD)
    AddCraft(0x7, 0xDE)
    AddCraft(0x7, 0xDF)
    AddCraft(0x7, 0x13B)
    SetChrChipPat(0x7, 0x6, 0x13B)
    AddItemNumber(0x1F4, 20)
    AddItemNumber(0x1F8, 3)
    AddItemNumber(0x1FB, 3)
    AddItemNumber(0x20B, 3)
    AddItemNumber(0x20E, 10)
    AddItemNumber(0x1, 1)
    AddItemNumber(0x4, 1)
    AddItemNumber(0x320, 1)
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x21, 4)
    Battle("BattleInfo_1FC", 0x0, 0x0, 0x0, 0x8, 0xFF)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    OP_CC(0x1, 0xFF, 0x0)
    Call(0, 10)
    Return()

    # Function_5_67B end

    def Function_6_196D(): pass

    label("Function_6_196D")


    def lambda_1972():
        OP_95(0xFE, 23500, 0, -43000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1972)
    WaitChrThread(0xFE, 1)

    def lambda_1990():
        OP_95(0xFE, 12000, 0, -36000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1990)
    WaitChrThread(0xFE, 1)

    def lambda_19AE():
        OP_95(0xFE, 8000, 0, -26000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_19AE)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_6_196D end

    def Function_7_19C8(): pass

    label("Function_7_19C8")

    ClearChrFlags(0x9, 0x80)
    SetChrChipByIndex(0x9, 0x24)
    SetChrSubChip(0x9, 0x0)
    OP_52(0x9, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x9, 0x20)

    def lambda_1A00():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x7D0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1A00)
    BeginChrThread(0x9, 0, 0, 1)

    def lambda_1A17():
        OP_96(0xFE, 0x12C, 0x0, 0x9858, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1A17)
    WaitChrThread(0x9, 1)
    SetChrChipByIndex(0x9, 0x23)
    SetChrSubChip(0x9, 0x0)
    OP_52(0x9, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x9, 0, 0, 0)
    Return()

    # Function_7_19C8 end

    def Function_8_1A60(): pass

    label("Function_8_1A60")

    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xA, 0x24)
    SetChrSubChip(0xA, 0x0)
    OP_52(0xA, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xA, 0x20)

    def lambda_1A98():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x7D0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1A98)
    BeginChrThread(0xA, 0, 0, 1)

    def lambda_1AAF():
        OP_96(0xFE, 0xBB8, 0x0, 0x98BC, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1AAF)
    WaitChrThread(0xA, 1)
    SetChrChipByIndex(0xA, 0x23)
    SetChrSubChip(0xA, 0x0)
    OP_52(0xA, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xA, 0, 0, 0)
    Return()

    # Function_8_1A60 end

    def Function_9_1AF8(): pass

    label("Function_9_1AF8")

    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x4)
    OP_52(0xFE, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_1B2A():
        OP_A6(0xFE, 0x32, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1B2A)
    WaitChrThread(0xFE, 2)
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x4)
    OP_52(0xFE, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 0, 0, 1)

    def lambda_1B76():
        OP_96(0xFE, 0x6A4, 0x0, 0x4E20, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1B76)
    Return()

    # Function_9_1AF8 end

    def Function_10_1B8C(): pass

    label("Function_10_1B8C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis400.itp")
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch02950.itc", 0x1F)
    LoadChrToIndex("chr/ch00950.itc", 0x20)
    LoadChrToIndex("chr/ch02450.itc", 0x21)
    SoundLoad(3311)
    SoundLoad(3312)
    SoundLoad(3313)
    SoundLoad(3511)
    SoundLoad(3512)
    SoundLoad(3448)
    SoundLoad(3449)
    SoundLoad(3450)
    SoundLoad(4047)
    SoundLoad(4048)
    OP_68(1700, 1300, 34600, 0)
    MoveCamera(325, 13, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(16000, 0)
    SetChrPos(0x101, 2000, 0, 32600, 0)
    SetChrPos(0x109, 2400, 0, 30900, 0)
    SetChrPos(0x108, 600, 0, 31900, 0)
    SetChrPos(0x10A, 1000, 0, 30500, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x109, 0x1F)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x10A, 0x20)
    SetChrSubChip(0x10A, 0x0)
    SetChrChipByIndex(0x108, 0x21)
    SetChrSubChip(0x108, 0x0)
    OP_68(1700, 1300, 33600, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)
    Fade(250)
    SetChrChipByIndex(0x108, 0xFF)
    SetChrSubChip(0x108, 0x0)
    Sound(531, 0, 50, 0)
    Sound(540, 0, 50, 0)
    OP_0D()
    Fade(250)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x10A, 0xFF)
    SetChrSubChip(0x10A, 0x0)
    SetChrChipByIndex(0x108, 0xFF)
    SetChrSubChip(0x108, 0x0)
    Sound(805, 0, 100, 0)
    Sound(531, 0, 100, 0)
    OP_0D()
    OP_6F(0x79)
    Sleep(500)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x10A,
        (
            "#3P#00607F#3448V#30WTch... Monsters like\x01",
            "that, here!?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x109,
        (
            "#6P#10101F#3511V#30WThey gave off a similar\x01",
            "vibe to the ones in the\x01",
            "Tower and Temple.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#5P#00003F#3311V#30W...And the exact same species\x01",
            "showed up in the lower levels\x01",
            "of the Fort of the Sun.\x02\x03",
            "#00013F#3312VThey're hiding down there.\x01",
            "I'm sure of it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x10A,
        (
            "#3P#00610F#3449V#30WTch... They just don't\x01",
            "know when to give up.\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xD79)
    TurnDirection(0x108, 0x109, 500)
    Sleep(300)

    ChrTalk(
        0x108,
        (
            "#01403F#4047V#5P#30W...We're running out of\x01",
            "time. If we go in now,\x02\x03",
            "#01401F#4048Vwe should be able to\x01",
            "make it in time.\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xFD0)

    def lambda_1F1D():
        TurnDirection(0xFE, 0x108, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1F1D)
    Sleep(100)
    TurnDirection(0x109, 0x108, 500)
    Sleep(200)

    ChrTalk(
        0x101,
        "#2P#00007F#3313V#30WRight!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#4P#10107F#3512V#30WRoger!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#3P#00607F#3450V#30WHmph... I won't let them\x01",
            "get away!\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    OP_24(0xD7A)

    def lambda_1FBC():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1FBC)
    Sleep(50)

    def lambda_1FCC():
        OP_93(0x108, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x108, 0, lambda_1FCC)
    Sleep(50)

    def lambda_1FDC():
        OP_93(0x109, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1FDC)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x108, 0)
    WaitChrThread(0x109, 0)
    OP_68(1700, 1300, 38600, 4000)
    SetCameraDistance(18000, 4000)

    def lambda_2012():
        OP_97(0x101, 0x0, 0x0, 0x3A98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2012)
    Sleep(50)

    def lambda_202F():
        OP_97(0x109, 0x0, 0x0, 0x3A98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_202F)
    Sleep(50)

    def lambda_204C():
        OP_97(0x108, 0x0, 0x0, 0x3A98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 0, lambda_204C)
    Sleep(50)

    def lambda_2069():
        OP_97(0x10A, 0x0, 0x0, 0x3A98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_2069)
    Sleep(2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x109, 0xFF)
    EndChrThread(0x10A, 0xFF)
    EndChrThread(0x108, 0xFF)
    OP_E5(0xA)
    Sleep(500)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_57(0x3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_E5(0xB)
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x22, 0)
    NewScene("m4010", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_10_1B8C end

    SaveToFile()

Try(main)
