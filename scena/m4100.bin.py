﻿from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "m4100.bin",                # FileName
        "m4100",                    # MapName
        "m4100",                    # Location
        0x00C8,                     # MapIndex
        "ed7351",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x28,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 200, 0, 0, 0, 1],
    )

    BuildStringList((
        "m4100",                  # 0
        "bm4110",                 # 1
        "bm4110",                 # 2
        "bm4110",                 # 3
    ))

    ATBonus("ATBonus_1A4", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_2A44", 2,   7,   2,   2,   0,   3,   0)
    Sepith("Sepith_2A4C", 2,   3,   4,   3,   2,   0,   2)
    Sepith("Sepith_2A54", 3,   0,   4,   2,   3,   4,   0)

    MonsterBattlePostion("MonsterBattlePostion_1E4", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_1E8", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_1EC", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_1F0", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_1F4", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_1F8", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_1FC", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_200", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_264", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_268", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_26C", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_270", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_274", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_278", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_27C", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_280", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_204", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_208", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_20C", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_210", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_214", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_218", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_21C", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_220", 8, 14, 180)

    # monster count: 3

    BattleInfo(
        "BattleInfo_284", 0x0000, 54, 6, 45, 10, 1, 30, 0, "bm4110", "Sepith_2A44", 40, 30, 20, 0,
        (
            ("ms83400.dat", "ms83400.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_1E4", "MonsterBattlePostion_264", "ed7450", "ed7453", "ATBonus_1A4"),
            ("ms83400.dat", "ms83400.dat", "ms83400.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_204", "MonsterBattlePostion_264", "ed7450", "ed7453", "ATBonus_1A4"),
            ("ms83400.dat", "ms83400.dat", "ms83400.dat", "ms83400.dat", 0, 0, 0, 0, "MonsterBattlePostion_1E4", "MonsterBattlePostion_264", "ed7450", "ed7453", "ATBonus_1A4"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_320", 0x0010, 54, 6, 45, 10, 1, 40, 0, "bm4110", "Sepith_2A4C", 40, 30, 20, 0,
        (
            ("ms78100.dat", "ms78100.dat", 0, 0, 0, 0, "ms78100.dat", 0, "MonsterBattlePostion_1E4", "MonsterBattlePostion_264", "ed7450", "ed7453", "ATBonus_1A4"),
            ("ms78100.dat", "ms78100.dat", "ms78100.dat", 0, 0, 0, "ms78100.dat", 0, "MonsterBattlePostion_204", "MonsterBattlePostion_264", "ed7450", "ed7453", "ATBonus_1A4"),
            ("ms78100.dat", "ms78100.dat", "ms78100.dat", "ms78100.dat", 0, 0, "ms78100.dat", 0, "MonsterBattlePostion_1E4", "MonsterBattlePostion_264", "ed7450", "ed7453", "ATBonus_1A4"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_3BC", 0x0000, 54, 6, 45, 10, 1, 20, 0, "bm4110", "Sepith_2A54", 40, 30, 20, 0,
        (
            ("ms78300.dat", "ms78300.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_1E4", "MonsterBattlePostion_264", "ed7450", "ed7453", "ATBonus_1A4"),
            ("ms78300.dat", "ms78300.dat", "ms78300.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_204", "MonsterBattlePostion_264", "ed7450", "ed7453", "ATBonus_1A4"),
            ("ms78300.dat", "ms78300.dat", "ms78300.dat", "ms78300.dat", 0, 0, 0, 0, "MonsterBattlePostion_1E4", "MonsterBattlePostion_264", "ed7450", "ed7453", "ATBonus_1A4"),
            (),
        )
    )

    AddCharChip((
        "chr/ch00000.itc",                   # 00
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
        "monster/ch83450.itc",               # 10
        "monster/ch83451.itc",               # 11
        "monster/ch78150.itc",               # 12
        "monster/ch78151.itc",               # 13
        "monster/ch78350.itc",               # 14
        "monster/ch78350.itc",               # 15
    ))

    DeclMonster(4294967156, 176610,  0,       0x10100CC,    "BattleInfo_284", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(8140,    163790,  0,       0x10100E1,    "BattleInfo_320", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(4294960576, 321220,  0,       0x1010087,    "BattleInfo_3BC", 0,   20,  0xFFFF, 4,  5)

    DeclActor(2500,    0,       319000,  1200,    2500,    1000,    319000,  0x007C, 0,  2,  0x0000)
    DeclActor(3240,    0,       7750,    1200,    3240,    1500,    7750,    0x007C, 0,  3,  0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 0
    ChipFrameInfo(1200, 0, [0, 1, 2, 3, 4])                      # 1
    ChipFrameInfo(800, 0, [0, 1, 2, 3, 4])                       # 2
    ChipFrameInfo(1000, 0, [0, 1, 2])                            # 3
    ChipFrameInfo(800, 0, [0, 1, 2, 3])                          # 4
    ChipFrameInfo(1000, 0, [0, 1, 2, 3])                         # 5

    ScpFunction((
        "Function_0_4E0",          # 00, 0
        "Function_1_504",          # 01, 1
        "Function_2_6EA",          # 02, 2
        "Function_3_83C",          # 03, 3
        "Function_4_932",          # 04, 4
        "Function_5_136F",         # 05, 5
        "Function_6_13AE",         # 06, 6
        "Function_7_13ED",         # 07, 7
        "Function_8_1426",         # 08, 8
        "Function_9_145F",         # 09, 9
        "Function_10_1495",        # 0A, 10
        "Function_11_14CE",        # 0B, 11
        "Function_12_1507",        # 0C, 12
        "Function_13_1540",        # 0D, 13
        "Function_14_2978",        # 0E, 14
        "Function_15_29CA",        # 0F, 15
    ))


    def Function_0_4E0(): pass

    label("Function_0_4E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_4F4")
    ClearScenarioFlags(0x22, 0)
    Event(0, 4)
    Jump("loc_503")

    label("loc_4F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_503")
    ClearScenarioFlags(0x22, 1)
    Event(0, 13)

    label("loc_503")

    Return()

    # Function_0_4E0 end

    def Function_1_504(): pass

    label("Function_1_504")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x166, 7)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_570")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_541")
    Sound(120, 1, 100, 0)
    Jump("loc_547")

    label("loc_541")

    Sound(120, 1, 70, 0)

    label("loc_547")

    SoundDistance(0x6E, 0xFFFF86DE, 0x0, 0xFFFFDC38, 0xC350, 0x186A0, 0x64, 0x0)
    OP_E3(0x76C, 0x0, 0xFFFF6488)

    label("loc_570")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x166, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_588")
    OP_1B(0x1, 0x0, 0xE)
    OP_1B(0x3, 0x0, 0xF)

    label("loc_588")

    OP_52(0x9, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1FA, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_656")
    OP_70(0x0, 0x0)
    Jump("loc_65A")

    label("loc_656")

    OP_70(0x0, 0x1E)

    label("loc_65A")

    SetBarrier(0x0, 0x0, 0x1, 0x0, -13730, 0, -12170, 6000, 2000, 60000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 4)), scpexpr(EXPR_END)), "loc_6A3")
    SetMapObjFrame(0xFF, "shadow", 0x0, 0x1)
    SetMapObjFrame(0xFF, "rock", 0x0, 0x1)
    SetBarrier(0x2, 0x0, 0x1)
    Jump("loc_6E9")

    label("loc_6A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 2)), scpexpr(EXPR_END)), "loc_6CB")
    SetMapObjFrame(0xFF, "shadow", 0x1, 0x1)
    SetMapObjFrame(0xFF, "rock", 0x1, 0x1)
    Jump("loc_6E9")

    label("loc_6CB")

    SetMapObjFrame(0xFF, "shadow", 0x0, 0x1)
    SetMapObjFrame(0xFF, "rock", 0x0, 0x1)
    SetBarrier(0x2, 0x0, 0x1)

    label("loc_6E9")

    Return()

    # Function_1_504 end

    def Function_2_6EA(): pass

    label("Function_2_6EA")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1FA, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7E6")
    Sound(14, 0, 100, 0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x42, 1)"), scpexpr(EXPR_END)), "loc_76F")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x42),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1FA, 0)
    OP_E0(0x5, 0x0)
    Jump("loc_7E1")

    label("loc_76F")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x42),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " is inside the chest.\x01",
            "Since you have too many, you gave it up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x0, 0x1E, 0x0, 0x0, 0x0)

    label("loc_7E1")

    Jump("loc_830")

    label("loc_7E6")

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

    label("loc_830")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_6EA end

    def Function_3_83C(): pass

    label("Function_3_83C")

    OP_F4(0x2)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is an orbment charging station.\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Rest Here\x01",      # 0
            "Quit\x01",           # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_923")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_74(0x1, 0x1E)
    Sound(7, 0, 100, 0)
    OP_70(0x1, 0x0)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    OP_79(0x1)
    OP_71(0x1, 0x1F, 0x186, 0x0, 0x20)
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
    OP_70(0x1, 0x0)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_923")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_3_83C end

    def Function_4_932(): pass

    label("Function_4_932")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x0, "event/ev11007.eff")
    LoadEffect(0x1, "event/ev11009.eff")
    LoadEffect(0x2, "event/ev11008.eff")
    SetMapObjFrame(0xFF, "shadow", 0x0, 0x1)
    SetMapObjFrame(0xFF, "rock", 0x0, 0x1)
    SetMapObjFrame(0xFF, "m4100:Layer6", 0x1, 0x1)
    SetMapObjFrame(0xFF, "black3", 0x0, 0x1)
    SoundLoad(995)
    SoundLoad(996)
    OP_68(-14090, 1300, -12840, 0)
    MoveCamera(12, 23, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(17000, 0)
    SetChrPos(0x101, -18770, 0, -15230, 55)
    SetChrPos(0x102, -17970, 0, -16530, 55)
    SetChrPos(0x109, -20070, 0, -15930, 55)
    SetChrPos(0x105, -19270, 0, -17130, 55)
    SetCameraDistance(15000, 2500)
    FadeToBright(1000, 0)

    def lambda_A45():
        OP_9B(0x0, 0x101, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_A45)
    Sleep(100)

    def lambda_A5D():
        OP_9B(0x0, 0x102, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_A5D)
    Sleep(100)

    def lambda_A75():
        OP_9B(0x0, 0x109, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_A75)
    Sleep(100)

    def lambda_A8D():
        OP_9B(0x0, 0x105, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_A8D)
    Sleep(100)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    OP_0D()
    OP_6F(0x79)
    OP_68(3140, 1300, 5290, 4000)
    MoveCamera(34, 13, 0, 4000)
    OP_6E(700, 4000)
    SetCameraDistance(43210, 4000)
    OP_6F(0x79)
    CloseMessageWindow()
    OP_68(26000, 1300, 5460, 4000)
    MoveCamera(58, 11, 0, 4000)
    OP_6E(700, 4000)
    SetCameraDistance(43210, 4000)
    PlaceName2(340, 200, "c_plac52", 0x0, 0)
    OP_6F(0x79)
    Sleep(500)
    Fade(500)
    OP_68(810, 500, 1150, 0)
    MoveCamera(22, 51, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(37460, 0)
    OP_68(810, 500, 1150, 4000)
    MoveCamera(71, 41, 0, 4000)
    OP_6E(500, 4000)
    SetCameraDistance(30510, 4000)
    OP_6F(0x79)
    Sleep(300)

    ChrTalk(
        0x101,
        "#00013F#12P#NThis is...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x109,
        (
            "#10111F#12P#NIndeed...\x01",
            "It's not normal.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        (
            "#00106F#12P#NThe earth surface and the walls\x01",
            "seem to be vaguely glittering...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-13240, 1500, -12060, 0)
    MoveCamera(45, 13, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(13150, 0)
    OP_0D()
    Sleep(150)
    OP_93(0x102, 0x87, 0x1F4)
    Sleep(500)
    OP_93(0x102, 0x5A, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#00108F#6PAlso, what could this...\x01",
            "...This stagnating air be...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10306F#6PHmm.\x01",
            "Maybe it's a kind of miasma.\x02\x03",
            "#10308F...The high elements could\x01",
            "be at work here.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_D80():
        TurnDirection(0x101, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_D80)
    Sleep(100)

    def lambda_D90():
        TurnDirection(0x102, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_D90)
    Sleep(100)

    def lambda_DA0():
        TurnDirection(0x109, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_DA0)
    Sleep(100)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x109, 0)

    ChrTalk(
        0x101,
        "#00011F#5PWhat!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105F#11PWazy, you...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105F#5PW-Why are you exactly saying\x01",
            "something like Tio would...!?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x105, 0xA, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x105,
        (
            "#10304F#12PHu hu, it's not at that child's level, but I have \x01",
            "quite the ability to sense the supernatural.\x02\x03",
            "#10302FWhat do we do?\x01",
            "I have a feeling that investigating further in\x01",
            "is going to be pretty dangerous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#5PYou're right, but...\x02",
    )

    CloseMessageWindow()
    Sound(995, 2, 70, 0)
    Sleep(300)
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1200)

    def lambda_FAA():
        OP_93(0x101, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_FAA)
    Sleep(50)

    def lambda_FBA():
        OP_93(0x109, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_FBA)
    Sleep(50)

    def lambda_FCA():
        OP_93(0x105, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_FCA)
    Sleep(50)

    def lambda_FDA():
        OP_93(0x102, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_FDA)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x102, 0)
    Sleep(300)

    ChrTalk(
        0x102,
        "#00105F#11PW-What could've been?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10305F#11P...This sound...\x02",
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x109,
        "#10110F#5P──Oh no!\x02",
    )

    CloseMessageWindow()
    OP_93(0x109, 0x37, 0x2EE)
    Sleep(150)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x109,
        "#10107F#6P#4SEveryone, please get back!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00010F#5PGh!?\x02",
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    BeginChrThread(0x101, 3, 0, 5)
    BeginChrThread(0x102, 3, 0, 6)
    BeginChrThread(0x109, 3, 0, 8)
    BeginChrThread(0x105, 3, 0, 7)
    OP_68(-8230, 1300, -8780, 1100)
    MoveCamera(46, 10, 0, 1100)
    OP_6E(700, 1100)
    SetCameraDistance(11270, 1100)
    Sleep(800)
    StopSound(995, 500, 60)
    Sound(996, 2, 100, 0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)
    PlayEffect(0x0, 0x0, 0xFF, 0x0, -15000, 0, -13000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x2, 0xFF, 0x0, -15000, 0, -13000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    EndChrThread(0x101, 0x3)
    EndChrThread(0x102, 0x3)
    EndChrThread(0x109, 0x3)
    EndChrThread(0x105, 0x3)
    OP_68(-192400, 2000, 7880, 0)
    MoveCamera(67, 4, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(14860, 0)
    SetChrPos(0x101, -189740, 250, 8600, 235)
    SetChrPos(0x102, -190490, 250, 10170, 235)
    SetChrPos(0x109, -188420, 250, 9380, 235)
    SetChrPos(0x105, -189230, 250, 10700, 235)
    Fade(500)
    Sound(200, 0, 100, 0)
    StopEffect(0x0, 0x0)
    StopEffect(0x1, 0x0)
    StopEffect(0x2, 0x0)
    PlayEffect(0x0, 0x2, 0xFF, 0x0, -184500, 0, 12500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    PlayEffect(0x1, 0x3, 0xFF, 0x0, -180650, 0, 16750, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_82(0xC8, 0x0, 0xBB8, 0x3E8)
    BeginChrThread(0x101, 3, 0, 9)
    BeginChrThread(0x102, 3, 0, 10)
    BeginChrThread(0x109, 3, 0, 12)
    BeginChrThread(0x105, 3, 0, 11)
    Sleep(400)
    PlayEffect(0x0, 0x5, 0xFF, 0x0, -182500, 0, 20000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    CancelBlur(0)
    OP_0D()
    Sleep(500)
    Sound(196, 0, 100, 0)
    StopSound(996, 5000, 100)
    StopEffect(0x3, 0x2)
    Sleep(1200)
    Sound(833, 0, 100, 0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(4000)
    WaitBGM()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1D), scpexpr(EXPR_PUSH_LONG, 0x21205000), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1360")
    SetScenarioFlags(0x12B, 4)

    label("loc_1360")

    SetScenarioFlags(0x22, 0)
    NewScene("r2060", 0, 0, 0)
    IdleLoop()
    EventEnd(0x5)
    Return()

    # Function_4_932 end

    def Function_5_136F(): pass

    label("Function_5_136F")

    Sleep(100)
    OP_9B(0x0, 0xFE, 0xBE, 0xAF0, 0x1388, 0x1)
    Sound(809, 0, 100, 0)
    OP_9C(0xFE, 0xBB8, 0x0, 0x7D0, 0x15E, 0x44C)
    OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0xFA0, 0x1)
    Return()

    # Function_5_136F end

    def Function_6_13AE(): pass

    label("Function_6_13AE")

    Sleep(150)
    OP_9B(0x0, 0xFE, 0xBE, 0xAF0, 0x1388, 0x1)
    Sound(844, 0, 50, 0)
    OP_9C(0xFE, 0xBB8, 0x0, 0x7D0, 0x15E, 0x44C)
    OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0xFA0, 0x1)
    Return()

    # Function_6_13AE end

    def Function_7_13ED(): pass

    label("Function_7_13ED")

    Sleep(250)
    OP_9B(0x0, 0xFE, 0xBE, 0xAF0, 0x1388, 0x1)
    OP_9C(0xFE, 0xBB8, 0x0, 0x7D0, 0x15E, 0x44C)
    OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0xFA0, 0x1)
    Return()

    # Function_7_13ED end

    def Function_8_1426(): pass

    label("Function_8_1426")

    Sleep(300)
    OP_9B(0x0, 0xFE, 0x0, 0xAF0, 0x1388, 0x1)
    OP_9C(0xFE, 0xBB8, 0x0, 0x7D0, 0x15E, 0x44C)
    OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0xFA0, 0x1)
    Return()

    # Function_8_1426 end

    def Function_9_145F(): pass

    label("Function_9_145F")

    OP_9C(0xFE, 0xFFFFF448, 0xFFFFFF06, 0xFFFFF448, 0x15E, 0x190)
    OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0xFA0, 0x1)
    OP_9B(0x0, 0xFE, 0x0, 0x2904, 0xFA0, 0x1)
    Return()

    # Function_9_145F end

    def Function_10_1495(): pass

    label("Function_10_1495")

    Sleep(50)
    OP_9C(0xFE, 0xFFFFF448, 0xFFFFFF06, 0xFFFFF448, 0x15E, 0x190)
    OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0xFA0, 0x1)
    OP_9B(0x0, 0xFE, 0x0, 0x2904, 0xFA0, 0x1)
    Return()

    # Function_10_1495 end

    def Function_11_14CE(): pass

    label("Function_11_14CE")

    Sleep(100)
    OP_9C(0xFE, 0xFFFFF830, 0xFFFFFF06, 0xFFFFF830, 0x15E, 0x190)
    OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0xFA0, 0x1)
    OP_9B(0x0, 0xFE, 0x0, 0x2904, 0xFA0, 0x1)
    Return()

    # Function_11_14CE end

    def Function_12_1507(): pass

    label("Function_12_1507")

    Sleep(150)
    OP_9C(0xFE, 0xFFFFF830, 0xFFFFFF06, 0xFFFFF830, 0x15E, 0x190)
    OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0xFA0, 0x1)
    OP_9B(0x0, 0xFE, 0x0, 0x2904, 0xFA0, 0x1)
    Return()

    # Function_12_1507 end

    def Function_13_1540(): pass

    label("Function_13_1540")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch51115.itc", 0x1E)
    SoundLoad(841)
    SetMapObjFrame(0xFF, "shadow", 0x1, 0x1)
    SetMapObjFrame(0xFF, "rock", 0x1, 0x1)
    SetMapObjFrame(0xFF, "m4100:Layer6", 0x0, 0x1)
    SetMapObjFrame(0xFF, "black3", 0x1, 0x1)
    OP_68(-185970, 2400, 12000, 0)
    MoveCamera(35, 1, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(50080, 0)
    SetChrPos(0x101, -184750, 0, 12750, 45)
    SetChrPos(0x109, -185000, 0, 11500, 45)
    SetChrPos(0x102, -186000, 0, 12300, 45)
    SetChrPos(0x105, -187250, 0, 11750, 45)
    FadeToBright(1000, 0)
    OP_68(-185970, 1700, 12000, 6500)
    MoveCamera(74, 22, 0, 6500)
    OP_6E(500, 6500)
    SetCameraDistance(33640, 6500)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    OP_68(-183110, 1000, 13310, 0)
    MoveCamera(81, 15, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18590, 0)
    OP_0D()
    Sleep(500)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x101,
        "#00007F#4S#12PMr. Gantz, can you hear me!?\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x109,
        "#10101F#4S#12PIf you can, please answer!\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_64(0x109)
    OP_68(-184820, 1000, 11980, 1500)
    MoveCamera(91, 28, 0, 1500)
    OP_6E(500, 1500)
    SetCameraDistance(18590, 1500)

    def lambda_1757():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1757)
    Sleep(150)

    def lambda_1767():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1767)
    Sleep(100)
    Sleep(200)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#00006F#5PNo good...\x01",
            "It looks like it's completely plugged.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_93(0x102, 0x5A, 0x1F4)

    ChrTalk(
        0x102,
        (
            "#00106F#6PB-But why all of a sudden...\x02\x03",
            "#00108FRight before the cave-in it seemed\x01",
            "there was some kind of sound...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    TurnDirection(0x105, 0x109, 500)

    ChrTalk(
        0x105,
        (
            "#10305F#12POh, by the way, how did you\x01",
            "know it was going to collapse?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    TurnDirection(0x109, 0x105, 500)

    def lambda_189D():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_189D)

    ChrTalk(
        0x109,
        (
            "#10106F#11PAh, yes.\x02\x03",
            "#10101FI felt a faint gunpowder smell\x01",
            "and I thought it was dangerous...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10301F#12PGunpowder...?\x02\x03",
            "#10308FNow that you mention it, there's a\x01",
            "faint smell like something's burnt.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103F#6PBut something like gunpowder should\x01",
            "be used quite rarely nowadays...\x02\x03",
            "#00101FCould some explosives used back\x01",
            "in the day have detonated...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#5P...No, whatever the circumstances are there\x01",
            "shouldn't be any remaining in such a place.\x02\x03",
            "#00013FI guess a trap which uses\x01",
            "explosives was set off.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_1B05():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1B05)
    Sleep(50)

    def lambda_1B15():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1B15)
    Sleep(50)

    def lambda_1B25():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_1B25)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x102,
        "#00107F#6PA t-trap!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10108F#11PB-But, indeed, I can\x01",
            "only think of that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303F#12PI see, now I get it...\x02\x03",
            "#10301FSo that *bz bz bz* was the sound\x01",
            "of the mechanism's sparks?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#5P...Most likely.\x02\x03",
            "#00008FAfter entering inside, someone\x01",
            "set it to cut our path of retreat.\x02\x03",
            "#00001FThey were probably lurking nearby and\x01",
            "made it explode with a remote control.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108F#6PB-But who would do such a thing...?\x02",
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#00101F#6PD-Don't tell me that they're who\x01",
            "destroyed the entrance gate...!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#5PYeah, the possibility is high.\x02\x03",
            "#00013F...I don't know who they're, but it\x01",
            "seems we completely felled for it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00106F#6PNo way...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x102, 500)

    ChrTalk(
        0x109,
        (
            "#10102F#11PI-It's fine!\x02\x03",
            "#10112FIt's for times like this\x01",
            "that there's the ENIGMA!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    SetChrFlags(0x109, 0x20)
    SetChrFlags(0x109, 0x2)
    SetChrChipByIndex(0x109, 0x1E)
    SetChrSubChip(0x109, 0x0)
    Sound(802, 0, 100, 0)
    Sleep(500)
    SetChrSubChip(0x109, 0x1)
    Sound(804, 0, 100, 0)
    Sleep(500)

    def lambda_1E82():
        TurnDirection(0x102, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1E82)
    Sleep(50)

    def lambda_1E92():
        TurnDirection(0x105, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_1E92)
    Sleep(50)

    def lambda_1EA2():
        TurnDirection(0x101, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1EA2)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x101, 0)
    Sound(841, 2, 100, 0)
    Sleep(2000)
    OP_24(0x349)
    Sound(840, 0, 100, 0)
    Sleep(1000)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x109,
        "#10111F#11PEehm, this is...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#6PProbably the alert that orbal\x01",
            "waves do not reach...\x02\x03",
            "#00101FIt was written in the manual that it's\x01",
            "difficult they reach in airtight places.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10106F#11PUuh, is that so...?\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x109, 0x0)
    Sound(804, 0, 100, 0)
    Sleep(500)
    Fade(250)
    ClearChrFlags(0x109, 0x20)
    ClearChrFlags(0x109, 0x2)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    Sound(802, 0, 100, 0)
    OP_0D()

    ChrTalk(
        0x105,
        (
            "#10306F#12POh boy.\x01",
            "Quite inconvenient, then.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_93(0x101, 0xE1, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00003F#5P──It can't be helped.\x01",
            "Being this the situation, let's move forward.\x02\x03",
            "#00008FWe could be able to find a\x01",
            "different exit, maybe...\x02\x03",
            "#00013FIf we remain here ineptly, we\x01",
            "could be blasted away again.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2121():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_2121)
    Sleep(50)

    def lambda_2131():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2131)
    Sleep(50)

    def lambda_2141():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_2141)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x109,
        (
            "#10108F#11PY-You're right...\x01",
            "It's possible they're doing a remote operation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103F#6PAlthough i think that\x01",
            "Mr. Gantz, who was outside,\x01",
            "has gone to call for help...\x02\x03",
            "#00101FIt's true that, thinking about the culprits'\x01",
            "motive, it could be better to move.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F#12POh boy. Staying or advancing...\x01",
            "Whatever we choose, it's a thorny path.\x02\x03",
            "#10302FWhen I'm with you,\x01",
            "I'm never bored.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#5PThat impudent talking of yours is now reassuring.\x02\x03",
            "#00007F──We can't resupply.\x01",
            "At any rate, let's work together\x01",
            "and cut through this place somehow!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00101F#6PYes...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10304F#12PJaー.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10107F#11PRoger!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis301.itp")
    Sleep(500)
    Sound(814, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "You have become able to use #2CBurst#5C in battle.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sound(18, 0, 100, 0)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_57(0x3)
    OP_CB(0x0, 0x3, 0x80FFFFFF, 0x1F4, 0x0, 0x0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※In every chapter, when the story reaches a certain\x01",
            "  climax, you will be able to use "Burst".\x02\x03",
            "※When the "Burst Gauge" at the top right of the battle\x01",
            "  screen is at MAX, by selecting Burst #2Cyour allies can\x01",
            "  act one-sidedly#5C up to when the gauge is depleted.\x02\x03",
            "※During this time, #2Call allies' ailments are recovered#5C\x01",
            "  and while active, #2Cattack power is 20% up and you gain\x01",
            "  CPs automatically too#5C.\x02\x03",
            "※Furthermore, Arts which originally take time to activate,\x01",
            "  #2Ccan be activated immediately#5C.\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※Still more, the Burst Gauge is something\x01",
            "  that reflects all characters' "tension".\x02\x03",
            "※It increases each time an ally attacks,\x01",
            "  but by attacking consecutively by using \x01",
            "  TEAMRUSH, it goes up all the way.\x02\x03",
            "※Conversely, it decreases a little when attacked\x01",
            " by the enemy and if not used for some turns when\x01",
            " in MAX status, the gauge goes down one level.\x02\x03",
            "※Still more, please pay attention\x01",
            "  that #2Cwhen characters are in KO\x01",
            "  condition it cannot be activated#5C.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(800)
    OP_50(0x1F, (scpexpr(EXPR_PUSH_LONG, 0x2000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Sound(814, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※"Burst" was added to the Detective Notebook\x01",
            "  manual and you can read about it there.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CC(0x1, 0xFF, 0x0)
    Sleep(500)
    OP_D7(0x1E)
    OP_37()
    SetChrPos(0x0, -13380, 0, -11360, 45)
    SetScenarioFlags(0x12A, 2)
    OP_29(0xA2, 0x1, 0x2)
    SetBarrier(0x3, 0x0, 0x1)
    OP_C9(0x1, 0x10000)
    OP_50(0x52, (scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_IMUL), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x21, 5)
    OP_24(0x349)
    EventEnd(0x5)
    Return()

    # Function_13_1540 end

    def Function_14_2978(): pass

    label("Function_14_2978")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00001FThere's no time...\x01",
            "Let's hurry up to the exit!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 29200, 3510, -3510, 270)
    EventEnd(0x4)
    Return()

    # Function_14_2978 end

    def Function_15_29CA(): pass

    label("Function_15_29CA")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00001FThere's no time...\x01",
            "Let's hurry up to the exit!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -1900, 0, 28210, 180)
    EventEnd(0x4)
    Return()

    # Function_15_29CA end

    SaveToFile()

Try(main)
