from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "m4250.bin",                # FileName
        "m4250",                    # MapName
        "m4250",                    # Location
        0x00D7,                     # MapIndex
        "ed7350",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x2E,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 215, 0, 0, 0, 1],
    )

    BuildStringList((
        "m4250",                  # 0
        "Cryptid",                # 1
        "bm4250",                 # 2
    ))

    ATBonus("ATBonus_164", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_224", 8, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_228", 2, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_22C", 14, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_230", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_234", 14, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_238", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_23C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_240", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_204", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_208", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_20C", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_210", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_214", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_218", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_21C", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_220", 5, 5, 45)

    # monster count: 0

    # event battle count: 1

    BattleInfo(
        "BattleInfo_244", 0x0C40, 255, 6, 0, 0, 3, 0, 0, "bm4250", 0x00000000, 25, 25, 25, 25,
        (
            ("ms89200.dat", "ms81001.dat", "ms81001.dat", "ms81001.dat", "ms81001.dat", 0, 0, 0, "MonsterBattlePostion_224", "MonsterBattlePostion_204", "ed7554", "ed7554", "ATBonus_164"),
            ("ms89200.dat", "ms87800.dat", "ms87800.dat", "ms87800.dat", "ms87800.dat", 0, 0, 0, "MonsterBattlePostion_224", "MonsterBattlePostion_204", "ed7554", "ed7554", "ATBonus_164"),
            ("ms89200.dat", "ms87600.dat", "ms87600.dat", "ms87600.dat", "ms87600.dat", 0, 0, 0, "MonsterBattlePostion_224", "MonsterBattlePostion_204", "ed7554", "ed7554", "ATBonus_164"),
            ("ms89200.dat", "ms81201.dat", "ms81201.dat", "ms81201.dat", "ms81201.dat", 0, 0, 0, "MonsterBattlePostion_224", "MonsterBattlePostion_204", "ed7554", "ed7554", "ATBonus_164"),
        )
    )

    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0040, 0, 3,   18.0,                  70.0,                  -1.0,                  36.0,                  [0.0833333358168602,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.0833333358168602,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.25,                  0.0,                   -1.5,                  -5.833333492279053,    0.25,                  1.0])

    DeclActor(500,     0,       3000,    1200,    500,     2000,    3000,    0x007C, 0,  2,  0x0000)

    ChipFrameInfo(796, 0)                                        # 0

    ScpFunction((
        "Function_0_31C",          # 00, 0
        "Function_1_366",          # 01, 1
        "Function_2_411",          # 02, 2
        "Function_3_74E",          # 03, 3
    ))


    def Function_0_31C(): pass

    label("Function_0_31C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_332")
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x2E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_332")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_365")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_365")
    SetChrPos(0x0, 500, 0, 3000, 315)
    OP_31(0x1)
    OP_69(0xFF, 0x0)
    ClearMapFlags(0x8000000)

    label("loc_365")

    Return()

    # Function_0_31C end

    def Function_1_366(): pass

    label("Function_1_366")

    MiniGame(0x2F, 0xFFFFFFFF, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 7)), scpexpr(EXPR_END)), "loc_3A1")
    ModifyEventFlags(0, 0, 0x80)
    SetMapObjFlags(0x1, 0x4)
    Jump("loc_40A")

    label("loc_3A1")

    OP_78(0x1, 0x8)
    ClearMapObjFlags(0x1, 0x4)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x8, 0x8)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x1)
    SetChrPos(0x8, 18000, 0, 70000, 180)
    OP_93(0x8, 0xB4, 0x0)
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1F40), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetBarrier(0x0, 0x0, 0x2, 0x0, 18000, 0, 70000, 3000, 3000, 90000)

    label("loc_40A")

    Sound(123, 1, 80, 0)
    Return()

    # Function_1_366 end

    def Function_2_411(): pass

    label("Function_2_411")

    SetMapFlags(0x80)
    SetMapFlags(0x8000000)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x31, 2)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_443")
    SetScenarioFlags(0x31, 2)

    label("loc_443")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_489")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_483")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_478")
    Sound(2499, 255, 100, 0)
    Jump("loc_47E")

    label("loc_478")

    Sound(3537, 255, 100, 0)

    label("loc_47E")

    Jump("loc_489")

    label("loc_483")

    Sound(3344, 255, 100, 0)

    label("loc_489")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_740")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_4FE")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "Board Merkabah")
    MenuCmd(1, 0, "Cancel")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4DE"),
        (SWITCH_DEFAULT, "loc_4EF"),
    )


    label("loc_4DE")

    SetScenarioFlags(0x22, 0)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Jump("loc_4F9")

    label("loc_4EF")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4F9")

    Jump("loc_73B")

    label("loc_4FE")

    MenuCmd(0, 0)
    MenuCmd(1, 0, "Use Orbal Car")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_530")
    MenuCmd(1, 0, "Rest in Orbal Car")

    label("loc_530")

    MenuCmd(1, 0, "Cancel")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_564"),
        (1, "loc_668"),
        (2, "loc_6F9"),
        (SWITCH_DEFAULT, "loc_731"),
    )


    label("loc_564")

    SetMapObjFrame(0x0, "light", 0x0, 0x1)
    OP_74(0x0, 0x1E)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_595")
    OP_70(0x0, 0x12C)
    OP_71(0x0, 0x12C, 0x14A, 0x0, 0x0)
    Jump("loc_5A5")

    label("loc_595")

    OP_70(0x0, 0xF0)
    OP_71(0x0, 0xF0, 0x10E, 0x0, 0x0)

    label("loc_5A5")

    Sound(462, 0, 100, 0)
    SoundLoad(2500)
    SoundLoad(3538)
    SoundLoad(3345)
    Sleep(700)
    FadeToDark(300, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5FB")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5FB")

    FadeToDark(0, 0, -1)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_61E")
    Sound(461, 0, 100, 0)

    label("loc_61E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_63E")
    OP_70(0x0, 0x14A)
    OP_71(0x0, 0x14A, 0x12C, 0x0, 0x0)
    Jump("loc_64E")

    label("loc_63E")

    OP_70(0x0, 0x10E)
    OP_71(0x0, 0x10E, 0xF0, 0x0, 0x0)

    label("loc_64E")

    Sleep(1000)
    OP_0D()
    SetMapObjFrame(0x0, "light", 0x1, 0x1)
    OP_70(0x0, 0x0)
    Jump("loc_489")

    label("loc_668")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_6DA")
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 0)), scpexpr(EXPR_END)), "loc_69D")
    OP_32(0xFF, 0xFF, 0x0)
    Jump("loc_6B5")

    label("loc_69D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_6B0")
    OP_32(0xFF, 0xFE, 0x0)
    Jump("loc_6B5")

    label("loc_6B0")

    OP_32(0xFF, 0xFA, 0x0)

    label("loc_6B5")

    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6F4")

    label("loc_6DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_6EA")
    OP_AF(0xFB)
    Jump("loc_6F4")

    label("loc_6EA")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6F4")

    Jump("loc_73B")

    label("loc_6F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_712")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_72C")

    label("loc_712")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_722")
    OP_AF(0xFB)
    Jump("loc_72C")

    label("loc_722")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_72C")

    Jump("loc_73B")

    label("loc_731")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_73B")

    Jump("loc_489")

    label("loc_740")

    ClearMapFlags(0x8000000)
    OP_60(0x0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    # Function_2_411 end

    def Function_3_74E(): pass

    label("Function_3_74E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 7)), scpexpr(EXPR_END)), "loc_758")
    Return()

    label("loc_758")

    EventBegin(0x1)
    OP_52(0x0, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x4, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x5, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x6, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x7, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrSubChip(0x0, 0x0)
    SetChrSubChip(0x1, 0x0)
    SetChrSubChip(0x2, 0x0)
    SetChrSubChip(0x3, 0x0)
    SetChrSubChip(0x4, 0x0)
    SetChrSubChip(0x5, 0x0)
    SetChrSubChip(0x6, 0x0)
    SetChrSubChip(0x7, 0x0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a monster\x01",
            "harboring an incredible\x01",
            "power.\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[Exterminate]\x01",      # 0
            "[Cancel]\x01",           # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_844"),
        (SWITCH_DEFAULT, "loc_85D"),
    )


    label("loc_844")

    Sleep(500)
    OP_E2(0x2)
    OP_90(0x0, 18000, 0, 57000, 180)
    EventEnd(0x5)
    Return()

    label("loc_85D")

    Battle("BattleInfo_244", 0x0, 0x0, 0x100, 0xC, 0xFF)
    OP_E2(0x2)
    EventBegin(0x1)
    OP_68(18000, 1000, 57000, 0)
    OP_90(0x0, 18000, 0, 57000, 180)
    OP_90(0x1, 18000, 0, 57000, 180)
    OP_90(0x2, 18000, 0, 57000, 180)
    OP_90(0x3, 18000, 0, 57000, 180)
    OP_90(0x4, 18000, 0, 57000, 180)
    OP_90(0x5, 18000, 0, 57000, 180)
    OP_90(0x6, 18000, 0, 57000, 180)
    OP_90(0x7, 18000, 0, 57000, 180)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (2, "loc_91F"),
        (1, "loc_924"),
        (SWITCH_DEFAULT, "loc_927"),
    )


    label("loc_91F")

    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    label("loc_924")

    OP_B9(0x0)
    Return()

    label("loc_927")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x8, 0x80)
    OP_E2(0x3)
    Sleep(400)
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_E0(0x2B, 0x0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Monster defeated!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4A), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9A9")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x39),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    AddItemNumber(0x39, 1)
    Jump("loc_9C2")

    label("loc_9A9")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x38),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    AddItemNumber(0x38, 1)

    label("loc_9C2")

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x21E, 7)
    ModifyEventFlags(0, 0, 0x80)
    SetMapObjFlags(0x1, 0x4)
    SetBarrier(0x2, 0x0, 0x1)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8)
    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_3_74E end

    SaveToFile()

Try(main)
