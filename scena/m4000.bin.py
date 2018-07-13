from ScenarioHelper import *

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
        "Function_5_677",          # 05, 5
        "Function_6_19BF",         # 06, 6
        "Function_7_1A1A",         # 07, 7
        "Function_8_1AB2",         # 08, 8
        "Function_9_1B4A",         # 09, 9
        "Function_10_1BDE",        # 0A, 10
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

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_669")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_429")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "Board Merkabah")
    MenuCmd(1, 0, "Quit")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_409"),
        (SWITCH_DEFAULT, "loc_41A"),
    )


    label("loc_409")

    SetScenarioFlags(0x22, 0)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Jump("loc_424")

    label("loc_41A")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_424")

    Jump("loc_664")

    label("loc_429")

    MenuCmd(0, 0)
    MenuCmd(1, 0, "Use Orbal Car")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_45B")
    MenuCmd(1, 0, "Rest in Orbal Car")

    label("loc_45B")

    MenuCmd(1, 0, "Quit")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_48D"),
        (1, "loc_591"),
        (2, "loc_622"),
        (SWITCH_DEFAULT, "loc_65A"),
    )


    label("loc_48D")

    SetMapObjFrame(0x0, "light", 0x0, 0x1)
    OP_74(0x0, 0x1E)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4BE")
    OP_70(0x0, 0x12C)
    OP_71(0x0, 0x12C, 0x14A, 0x0, 0x0)
    Jump("loc_4CE")

    label("loc_4BE")

    OP_70(0x0, 0xF0)
    OP_71(0x0, 0xF0, 0x10E, 0x0, 0x0)

    label("loc_4CE")

    Sound(462, 0, 100, 0)
    SoundLoad(2500)
    SoundLoad(3538)
    SoundLoad(3345)
    Sleep(700)
    FadeToDark(300, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_524")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_524")

    FadeToDark(0, 0, -1)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_547")
    Sound(461, 0, 100, 0)

    label("loc_547")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_567")
    OP_70(0x0, 0x14A)
    OP_71(0x0, 0x14A, 0x12C, 0x0, 0x0)
    Jump("loc_577")

    label("loc_567")

    OP_70(0x0, 0x10E)
    OP_71(0x0, 0x10E, 0xF0, 0x0, 0x0)

    label("loc_577")

    Sleep(1000)
    OP_0D()
    SetMapObjFrame(0x0, "light", 0x1, 0x1)
    OP_70(0x0, 0x0)
    Jump("loc_3B6")

    label("loc_591")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_603")
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 0)), scpexpr(EXPR_END)), "loc_5C6")
    OP_32(0xFF, 0xFF, 0x0)
    Jump("loc_5DE")

    label("loc_5C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_5D9")
    OP_32(0xFF, 0xFE, 0x0)
    Jump("loc_5DE")

    label("loc_5D9")

    OP_32(0xFF, 0xFA, 0x0)

    label("loc_5DE")

    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_61D")

    label("loc_603")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_613")
    OP_AF(0xFB)
    Jump("loc_61D")

    label("loc_613")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_61D")

    Jump("loc_664")

    label("loc_622")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_63B")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_655")

    label("loc_63B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_64B")
    OP_AF(0xFB)
    Jump("loc_655")

    label("loc_64B")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_655")

    Jump("loc_664")

    label("loc_65A")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_664")

    Jump("loc_3B6")

    label("loc_669")

    ClearMapFlags(0x8000000)
    OP_60(0x0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    # Function_4_33E end

    def Function_5_677(): pass

    label("Function_5_677")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 7)), scpexpr(EXPR_END)), "loc_682")
    OutputDebugInt(0xC8)

    label("loc_682")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5A, 0)), scpexpr(EXPR_END)), "loc_68D")
    OutputDebugInt(0x6F)

    label("loc_68D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetScenarioFlags(0x20, 0)
    OP_C9(0x0, 0x10000)
    SetScenarioFlags(0x20, 2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 3)), scpexpr(EXPR_END)), "loc_6B7")
    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 4)), scpexpr(EXPR_END)), "loc_6C9")
    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 5)), scpexpr(EXPR_END)), "loc_6DB")
    OP_50(0x67, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 5)), scpexpr(EXPR_END)), "loc_6E7")
    SetScenarioFlags(0x2C, 0)

    label("loc_6E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 6)), scpexpr(EXPR_END)), "loc_6FC")
    SetScenarioFlags(0x2C, 2)
    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 7)), scpexpr(EXPR_END)), "loc_711")
    SetScenarioFlags(0x2C, 4)
    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_711")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF1, 0)), scpexpr(EXPR_END)), "loc_726")
    SetScenarioFlags(0x2C, 6)
    OP_50(0x67, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_726")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x21), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_73C")
    AddMira(20000)
    Jump("loc_76B")

    label("loc_73C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x21), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_752")
    AddMira(10000)
    Jump("loc_76B")

    label("loc_752")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x21), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_768")
    AddMira(5000)
    Jump("loc_76B")

    label("loc_768")

    AddMira(2000)

    label("loc_76B")

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
            "#30W#40ASeptian Calendar 1204 ── On a certain month ",
            scpstr(0x6),
            scpstr(SCPSTR_CODE_ENTER),
        )
    )

    CloseMessageWindow()
    Sleep(1000)

    AnonymousTalk(
        0xFF,
        (
            "#30W#50AWestern border of the Calvard Republic\x01",
            "Altair City outskirts──",
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

    def lambda_ABE():
        OP_97(0x8, 0x0, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_ABE)
    Sleep(50)

    def lambda_ADB():
        OP_97(0x101, 0x0, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_ADB)
    Sleep(50)

    def lambda_AF8():
        OP_97(0x109, 0x0, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_AF8)
    Sleep(50)

    def lambda_B15():
        OP_97(0x108, 0x0, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 0, lambda_B15)
    Sleep(50)

    def lambda_B32():
        OP_97(0x10A, 0x0, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_B32)
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
        "──Here we are.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x101,
        "#00005F#3306V#5P#30WAh...!\x02",
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
        "#01400F#4042V#3P#N#30W...Hasn't changed at all, hm.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        "#00001F#3307V#4P#N#30WThis is the Altair Lodge...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x109,
        (
            "#10101F#3508V#4P#N#30WSo this is the place Tio was\x01",
            "saved from six years ago...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x10A,
        (
            "#00601F#3443V#3P#N#30WHmph...\x01",
            "Such a distasteful entrance.\x02",
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

    def lambda_E04():
        OP_97(0x8, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_E04)
    Sleep(50)

    def lambda_E21():
        OP_97(0x101, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_E21)
    Sleep(50)

    def lambda_E3E():
        OP_97(0x109, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_E3E)
    Sleep(50)

    def lambda_E5B():
        OP_97(0x108, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 0, lambda_E5B)
    Sleep(50)

    def lambda_E78():
        OP_97(0x10A, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_E78)
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
        "#11PThis is as far as my guidance goes.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PI'll leave this place in your\x01",
            "hands until 17:00 today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PIf you fail to meet the deadline,\x01",
            "our army forces will take over.\x02",
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
        "#01400F#4043VWe appreciate the thorough guidance.\x02",
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    OP_24(0xFCB)
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x8,
        "#11PJust try to be careful. Although...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PGoing in with the famous "Divine Blade of Wind",\x01",
            "there should be nothing to worry about.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    def lambda_1072():

        label("loc_1072")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_1072")

    QueueWorkItem2(0x101, 2, lambda_1072)

    def lambda_1084():

        label("loc_1084")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_1084")

    QueueWorkItem2(0x109, 2, lambda_1084)

    def lambda_1096():

        label("loc_1096")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_1096")

    QueueWorkItem2(0x108, 2, lambda_1096)

    def lambda_10A8():

        label("loc_10A8")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_10A8")

    QueueWorkItem2(0x10A, 2, lambda_10A8)

    def lambda_10BA():
        OP_95(0xFE, 3800, 0, 31600, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_10BA)
    WaitChrThread(0x8, 1)
    OP_68(2000, 1100, 31600, 3000)

    def lambda_10E9():
        OP_95(0xFE, 1000, 0, 21000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_10E9)
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
            "#12P#10106F#3509V#30WHmm... I get the impression that\x01",
            "we're not really welcome here.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00006F#3308V#11P#30WWell, from their perspective it's like\x01",
            "having outsiders take care of criminals\x01",
            "on their own territory.\x02\x03",
            "#00001F#3309V──What are we going to do?\x01",
            "Just go ahead and step right in?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_124E():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_124E)
    Sleep(50)

    def lambda_125E():
        TurnDirection(0x108, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x108, 0, lambda_125E)
    Sleep(50)

    def lambda_126E():
        TurnDirection(0x109, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_126E)
    Sleep(50)
    WaitChrThread(0x108, 0)
    WaitChrThread(0x109, 0)

    ChrTalk(
        0x10A,
        "#6P#00603F#3445V#30WExactly, we can't waste time.\x02",
    )

    CloseMessageWindow()
    OP_24(0xD75)
    TurnDirection(0x10A, 0x108, 500)
    Sleep(300)

    ChrTalk(
        0x10A,
        (
            "#6P#00601F#3446V#30W...MacLaine. What are the chances\x01",
            "on traps and similar mechanisms?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1326():
        TurnDirection(0xFE, 0x108, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1326)
    Sleep(100)

    def lambda_1336():
        TurnDirection(0xFE, 0x108, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1336)
    Sleep(200)

    ChrTalk(
        0x108,
        (
            "#01403F#4044V#5P#30WI assume most traps have been left shut down\x01",
            "due to the suppression operations six years ago.\x02\x03",
            "#01401F#4045VRoaming monsters, however──\x02",
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

    def lambda_149A():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_149A)
    Sleep(50)

    def lambda_14AA():
        OP_93(0x10A, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_14AA)
    Sleep(50)

    def lambda_14BA():
        OP_93(0x109, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_14BA)
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
        "#3P#00610F#3447V#30WWha!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10107F#3510V#30WM-Monsters...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00010F#3310V#30WThey came from within the lodge...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        "#01407F#4046V#30W──Here they come!\x02",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 7)), scpexpr(EXPR_END)), "loc_16A3")
    OP_50(0x1F, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_17C3")

    label("loc_16A3")

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

    label("loc_17C3")

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

    # Function_5_677 end

    def Function_6_19BF(): pass

    label("Function_6_19BF")


    def lambda_19C4():
        OP_95(0xFE, 23500, 0, -43000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_19C4)
    WaitChrThread(0xFE, 1)

    def lambda_19E2():
        OP_95(0xFE, 12000, 0, -36000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_19E2)
    WaitChrThread(0xFE, 1)

    def lambda_1A00():
        OP_95(0xFE, 8000, 0, -26000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1A00)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_6_19BF end

    def Function_7_1A1A(): pass

    label("Function_7_1A1A")

    ClearChrFlags(0x9, 0x80)
    SetChrChipByIndex(0x9, 0x24)
    SetChrSubChip(0x9, 0x0)
    OP_52(0x9, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x9, 0x20)

    def lambda_1A52():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x7D0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1A52)
    BeginChrThread(0x9, 0, 0, 1)

    def lambda_1A69():
        OP_96(0xFE, 0x12C, 0x0, 0x9858, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1A69)
    WaitChrThread(0x9, 1)
    SetChrChipByIndex(0x9, 0x23)
    SetChrSubChip(0x9, 0x0)
    OP_52(0x9, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x9, 0, 0, 0)
    Return()

    # Function_7_1A1A end

    def Function_8_1AB2(): pass

    label("Function_8_1AB2")

    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xA, 0x24)
    SetChrSubChip(0xA, 0x0)
    OP_52(0xA, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xA, 0x20)

    def lambda_1AEA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x7D0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1AEA)
    BeginChrThread(0xA, 0, 0, 1)

    def lambda_1B01():
        OP_96(0xFE, 0xBB8, 0x0, 0x98BC, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1B01)
    WaitChrThread(0xA, 1)
    SetChrChipByIndex(0xA, 0x23)
    SetChrSubChip(0xA, 0x0)
    OP_52(0xA, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xA, 0, 0, 0)
    Return()

    # Function_8_1AB2 end

    def Function_9_1B4A(): pass

    label("Function_9_1B4A")

    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x4)
    OP_52(0xFE, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_1B7C():
        OP_A6(0xFE, 0x32, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1B7C)
    WaitChrThread(0xFE, 2)
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x4)
    OP_52(0xFE, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 0, 0, 1)

    def lambda_1BC8():
        OP_96(0xFE, 0x6A4, 0x0, 0x4E20, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1BC8)
    Return()

    # Function_9_1B4A end

    def Function_10_1BDE(): pass

    label("Function_10_1BDE")

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
            "#3P#00607F#3448V#30WTsk...\x01",
            "Where do monstrosities like that come from!?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x109,
        (
            "#6P#10101F#3511V#30WThey gave off a similar vibe to the ones\x01",
            "in the "Tower" and "Temple".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#5P#00003F#3311V#30W...And the exact same species showed up\x01",
            "in the lower strata of the "Fort of Sun".\x02\x03",
            "#00013F#3312VLooks like they somehow managed\x01",
            "to find shelter down here.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x10A,
        (
            "#3P#00610F#3449V#30WTsk... They just don't\x01",
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
            "#01403F#4047V#5P#30W──We are running out of time.\x01",
            "If we go in now...\x02\x03",
            "#01401F#4048VWe should still be able to make it in time.\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xFD0)

    def lambda_1F9D():
        TurnDirection(0xFE, 0x108, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1F9D)
    Sleep(100)
    TurnDirection(0x109, 0x108, 500)
    Sleep(200)

    ChrTalk(
        0x101,
        "#2P#00007F#3313V#30WYes...!\x02",
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
            "#3P#00607F#3450V#30WHmph...\x01",
            "I won't let them get away!\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    OP_24(0xD7A)

    def lambda_203D():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_203D)
    Sleep(50)

    def lambda_204D():
        OP_93(0x108, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x108, 0, lambda_204D)
    Sleep(50)

    def lambda_205D():
        OP_93(0x109, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_205D)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x108, 0)
    WaitChrThread(0x109, 0)
    OP_68(1700, 1300, 38600, 4000)
    SetCameraDistance(18000, 4000)

    def lambda_2093():
        OP_97(0x101, 0x0, 0x0, 0x3A98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2093)
    Sleep(50)

    def lambda_20B0():
        OP_97(0x109, 0x0, 0x0, 0x3A98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_20B0)
    Sleep(50)

    def lambda_20CD():
        OP_97(0x108, 0x0, 0x0, 0x3A98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 0, lambda_20CD)
    Sleep(50)

    def lambda_20EA():
        OP_97(0x10A, 0x0, 0x0, 0x3A98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_20EA)
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

    # Function_10_1BDE end

    SaveToFile()

Try(main)
