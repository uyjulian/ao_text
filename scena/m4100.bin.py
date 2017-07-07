from ScenarioHelper import *

def main():
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

    Sepith("Sepith_282C", 2,   7,   2,   2,   0,   3,   0)
    Sepith("Sepith_2834", 2,   3,   4,   3,   2,   0,   2)
    Sepith("Sepith_283C", 3,   0,   4,   2,   3,   4,   0)

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
        "BattleInfo_284", 0x0000, 54, 6, 45, 10, 1, 30, 0, "bm4110", "Sepith_282C", 40, 30, 20, 0,
        (
            ("ms83400.dat", "ms83400.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_1E4", "MonsterBattlePostion_264", "ed7450", "ed7453", "ATBonus_1A4"),
            ("ms83400.dat", "ms83400.dat", "ms83400.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_204", "MonsterBattlePostion_264", "ed7450", "ed7453", "ATBonus_1A4"),
            ("ms83400.dat", "ms83400.dat", "ms83400.dat", "ms83400.dat", 0, 0, 0, 0, "MonsterBattlePostion_1E4", "MonsterBattlePostion_264", "ed7450", "ed7453", "ATBonus_1A4"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_320", 0x0010, 54, 6, 45, 10, 1, 40, 0, "bm4110", "Sepith_2834", 40, 30, 20, 0,
        (
            ("ms78100.dat", "ms78100.dat", 0, 0, 0, 0, "ms78100.dat", 0, "MonsterBattlePostion_1E4", "MonsterBattlePostion_264", "ed7450", "ed7453", "ATBonus_1A4"),
            ("ms78100.dat", "ms78100.dat", "ms78100.dat", 0, 0, 0, "ms78100.dat", 0, "MonsterBattlePostion_204", "MonsterBattlePostion_264", "ed7450", "ed7453", "ATBonus_1A4"),
            ("ms78100.dat", "ms78100.dat", "ms78100.dat", "ms78100.dat", 0, 0, "ms78100.dat", 0, "MonsterBattlePostion_1E4", "MonsterBattlePostion_264", "ed7450", "ed7453", "ATBonus_1A4"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_3BC", 0x0000, 54, 6, 45, 10, 1, 20, 0, "bm4110", "Sepith_283C", 40, 30, 20, 0,
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
        "Function_3_83B",          # 03, 3
        "Function_4_937",          # 04, 4
        "Function_5_133D",         # 05, 5
        "Function_6_137C",         # 06, 6
        "Function_7_13BB",         # 07, 7
        "Function_8_13F4",         # 08, 8
        "Function_9_142D",         # 09, 9
        "Function_10_1463",        # 0A, 10
        "Function_11_149C",        # 0B, 11
        "Function_12_14D5",        # 0C, 12
        "Function_13_150E",        # 0D, 13
        "Function_14_2772",        # 0E, 14
        "Function_15_27BB",        # 0F, 15
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1FA, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7EA")
    Sound(14, 0, 100, 0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('幻彩围巾', 1)"), scpexpr(EXPR_END)), "loc_773")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '幻彩围巾'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1FA, 0)
    OP_E0(0x5, 0x0)
    Jump("loc_7E5")

    label("loc_773")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            "In the treasure box",
            scpstr(SCPSTR_CODE_ITEM, '幻彩围巾'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Is contained.\x01",
            "Because my belongings are full,",
            scpstr(SCPSTR_CODE_ITEM, '幻彩围巾'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I gave up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x0, 0x1E, 0x0, 0x0, 0x0)

    label("loc_7E5")

    Jump("loc_82F")

    label("loc_7EA")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "In the treasure box何も入っていない。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_82F")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_6EA end

    def Function_3_83B(): pass

    label("Function_3_83B")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_928")
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

    label("loc_928")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_3_83B end

    def Function_4_937(): pass

    label("Function_4_937")

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

    def lambda_A4A():
        OP_9B(0x0, 0x101, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_A4A)
    Sleep(100)

    def lambda_A62():
        OP_9B(0x0, 0x102, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_A62)
    Sleep(100)

    def lambda_A7A():
        OP_9B(0x0, 0x109, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_A7A)
    Sleep(100)

    def lambda_A92():
        OP_9B(0x0, 0x105, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_A92)
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
        "#00013F#12P#Nthis is……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x109,
        (
            "#10111F#12P#Nsurely……\x01",
            "It's a bit unusual, is not it?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        (
            "#00106F#12P#NGrounds and walls blush\x01",
            "It seems to be shining ….\x02",
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
            "#00108F#6PBesides, something ……\x01",
            "…… This stagnation#2RAll over#The air is …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10306F#6PWell.\x01",
            "Brazen#4RAgriculture#It may be a lot of it.\x02\x03",
            "#10308F…… This has higher attributes\x01",
            "You may be working.\x02",
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

    def lambda_D94():
        TurnDirection(0x101, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_D94)
    Sleep(100)

    def lambda_DA4():
        TurnDirection(0x102, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_DA4)
    Sleep(100)

    def lambda_DB4():
        TurnDirection(0x109, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_DB4)
    Sleep(100)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x109, 0)

    ChrTalk(
        0x101,
        "#00011F#5PHeck! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105F#11PWaj, you …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105F#5PHow, why Tio\x01",
            "Similar things ……! Is it?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x105, 0xA, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x105,
        (
            "#10304F#12PHuh, it's not as good as that girl\x01",
            "There is a pretty inspirational direction.\x02\x03",
            "#10302Fwhat will you do?\x01",
            "As I am going to check the back\x01",
            "I guess that seems quite yabba.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#5PThat's right, but …\x02",
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

    def lambda_F75():
        OP_93(0x101, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_F75)
    Sleep(50)

    def lambda_F85():
        OP_93(0x109, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_F85)
    Sleep(50)

    def lambda_F95():
        OP_93(0x105, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_F95)
    Sleep(50)

    def lambda_FA5():
        OP_93(0x102, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_FA5)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x102, 0)
    Sleep(300)

    ChrTalk(
        0x102,
        "#00105F#11PWhat, something?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10305F#11P…… This sound ……\x02",
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x109,
        "#10110F#5P── Dont you!\x02",
    )

    CloseMessageWindow()
    OP_93(0x109, 0x37, 0x2EE)
    Sleep(150)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x109,
        "#10107F#6P#4SEveryone, please go down!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00010F#5PCow! Is it?\x02",
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
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1D), scpexpr(EXPR_PUSH_LONG, 0x21205000), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_132E")
    SetScenarioFlags(0x12B, 4)

    label("loc_132E")

    SetScenarioFlags(0x22, 0)
    NewScene("r2060", 0, 0, 0)
    IdleLoop()
    EventEnd(0x5)
    Return()

    # Function_4_937 end

    def Function_5_133D(): pass

    label("Function_5_133D")

    Sleep(100)
    OP_9B(0x0, 0xFE, 0xBE, 0xAF0, 0x1388, 0x1)
    Sound(809, 0, 100, 0)
    OP_9C(0xFE, 0xBB8, 0x0, 0x7D0, 0x15E, 0x44C)
    OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0xFA0, 0x1)
    Return()

    # Function_5_133D end

    def Function_6_137C(): pass

    label("Function_6_137C")

    Sleep(150)
    OP_9B(0x0, 0xFE, 0xBE, 0xAF0, 0x1388, 0x1)
    Sound(844, 0, 50, 0)
    OP_9C(0xFE, 0xBB8, 0x0, 0x7D0, 0x15E, 0x44C)
    OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0xFA0, 0x1)
    Return()

    # Function_6_137C end

    def Function_7_13BB(): pass

    label("Function_7_13BB")

    Sleep(250)
    OP_9B(0x0, 0xFE, 0xBE, 0xAF0, 0x1388, 0x1)
    OP_9C(0xFE, 0xBB8, 0x0, 0x7D0, 0x15E, 0x44C)
    OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0xFA0, 0x1)
    Return()

    # Function_7_13BB end

    def Function_8_13F4(): pass

    label("Function_8_13F4")

    Sleep(300)
    OP_9B(0x0, 0xFE, 0x0, 0xAF0, 0x1388, 0x1)
    OP_9C(0xFE, 0xBB8, 0x0, 0x7D0, 0x15E, 0x44C)
    OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0xFA0, 0x1)
    Return()

    # Function_8_13F4 end

    def Function_9_142D(): pass

    label("Function_9_142D")

    OP_9C(0xFE, 0xFFFFF448, 0xFFFFFF06, 0xFFFFF448, 0x15E, 0x190)
    OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0xFA0, 0x1)
    OP_9B(0x0, 0xFE, 0x0, 0x2904, 0xFA0, 0x1)
    Return()

    # Function_9_142D end

    def Function_10_1463(): pass

    label("Function_10_1463")

    Sleep(50)
    OP_9C(0xFE, 0xFFFFF448, 0xFFFFFF06, 0xFFFFF448, 0x15E, 0x190)
    OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0xFA0, 0x1)
    OP_9B(0x0, 0xFE, 0x0, 0x2904, 0xFA0, 0x1)
    Return()

    # Function_10_1463 end

    def Function_11_149C(): pass

    label("Function_11_149C")

    Sleep(100)
    OP_9C(0xFE, 0xFFFFF830, 0xFFFFFF06, 0xFFFFF830, 0x15E, 0x190)
    OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0xFA0, 0x1)
    OP_9B(0x0, 0xFE, 0x0, 0x2904, 0xFA0, 0x1)
    Return()

    # Function_11_149C end

    def Function_12_14D5(): pass

    label("Function_12_14D5")

    Sleep(150)
    OP_9C(0xFE, 0xFFFFF830, 0xFFFFFF06, 0xFFFFF830, 0x15E, 0x190)
    OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0xFA0, 0x1)
    OP_9B(0x0, 0xFE, 0x0, 0x2904, 0xFA0, 0x1)
    Return()

    # Function_12_14D5 end

    def Function_13_150E(): pass

    label("Function_13_150E")

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
        "#00007F#4S#12PCan you hear Gantz! Is it?\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x109,
        "#10101F#4S#12PPlease reply me when you hear it!\x02",
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

    def lambda_1729():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1729)
    Sleep(150)

    def lambda_1739():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1739)
    Sleep(100)
    Sleep(200)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#00006F#5PIt is useless……\x01",
            "It seems I completely occupied it.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_93(0x102, 0x5A, 0x1F4)

    ChrTalk(
        0x102,
        (
            "#00106F#6PBut why are you sudden ……\x02\x03",
            "#00108FJust before the collapse,\x01",
            "It seems that something sounded ….\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    TurnDirection(0x105, 0x109, 500)

    ChrTalk(
        0x105,
        (
            "#10305F#12PWell, why are you\x01",
            "Did you see that it collapsed?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    TurnDirection(0x109, 0x105, 500)

    def lambda_1847():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1847)

    ChrTalk(
        0x109,
        (
            "#10106F#11POh, yeah.\x02\x03",
            "#10101FFeeling a slight smell of gunpowder\x01",
            "I thought it was dangerous ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10301F#12PGunpowder …?\x02\x03",
            "#10308FBy the way\x01",
            "I smell like burnt smell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103F#6PHowever, recently in the case of gunpowder\x01",
            "It should be rarely used … …\x02\x03",
            "#00101FIn the past, blasts used in mines#4RHa ha#But\x01",
            "I wonder if it exploded …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#5P… Well, anything\x01",
            "It will not remain in such a place.\x02\x03",
            "#00013FProbably I used an explosive\x01",
            "I think that the trap was activated.\x02",
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

    def lambda_1A65():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1A65)
    Sleep(50)

    def lambda_1A75():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1A75)
    Sleep(50)

    def lambda_1A85():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_1A85)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x102,
        "#00107F#6PT, trap! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10108F#11PBut, certainly\x01",
            "Maybe it seems so … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303F#12PI see.\x02\x03",
            "#10301FThat \"Zejiji\" is\x01",
            "It was the sound of a spark of the trick?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#5P… … Probably.\x02\x03",
            "#00008FSince someone entered\x01",
            "It will be a trick to break off the retreat.\x02\x03",
            "#00001FDo you hide in the vicinity?\x01",
            "It may have blown up by remote control.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108F#6PBut, who is going to do that … …\x02",
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#00101F#6PWell, maybe the entrance door\x01",
            "Destroyed ……! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#5POh, the possibility seems high.\x02\x03",
            "#00013F…… I do not know anyone\x01",
            "Completely fit#2RIs#It seems like I was wrested.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00106F#6PSomething like that ….\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x102, 500)

    ChrTalk(
        0x109,
        (
            "#10102F#11PAll right!\x02\x03",
            "#10112FFor such a time\x01",
            "There is Enigma!\x02",
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

    def lambda_1D94():
        TurnDirection(0x102, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1D94)
    Sleep(50)

    def lambda_1DA4():
        TurnDirection(0x105, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_1DA4)
    Sleep(50)

    def lambda_1DB4():
        TurnDirection(0x101, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1DB4)
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
        "#10111F#11PEr, this is ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#6PPerhaps, the wave has not arrived yet\x01",
            "alarm#6RAlert#maybe……\x02\x03",
            "#00101FIt's hard to reach if it's a sealed place\x01",
            "It was written in the manual.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10106F#11PWell, is that so …?\x02",
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
            "#10306F#12PWhew.\x01",
            "Will not you go so well?\x02",
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
            "#00003F#5P── It can not be helped.\x01",
            "Let's go ahead if this is the case.\x02\x03",
            "#00008FPerhaps another exit\x01",
            "It might be found … …\x02\x03",
            "#00013FIf you remain here poorly\x01",
            "It may be blown up again.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_200D():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_200D)
    Sleep(50)

    def lambda_201D():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_201D)
    Sleep(50)

    def lambda_202D():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_202D)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x109,
        (
            "#10108F#11PThat's right.\x01",
            "There is also possibility of remote operation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103F#6PMr. Ganz who was outside\x01",
            "He says he is calling for help\x01",
            "I think, but ….\x02\x03",
            "#00101FCertainly, considering the aim of the criminal\x01",
            "You may as well move it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F#12PWell, staying in hell,\x01",
            "Is advancing a place like hardships?\x02\x03",
            "#10302FWith you guys\x01",
            "I really do not need to get bored.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#5PThat decrease, I am encouraging now.\x02\x03",
            "#00007F── Supply is not possible.\x01",
            "Anyway we can work together\x01",
            "Let's get through this place somehow!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00101F#6PYeah … …!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10304F#12PJa#4RYa#.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10107F#11PI understand.\x02",
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
            "During battle#2Cburst#5CIs now available.\x02",
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
            "* When the story comes to the brave in each chapter,\x01",
            "\"Burst\" will be available during battle.\x02\x03",
            "※ \"Burst gauge\" at the upper right of the battle screen when MAX\x01",
            "If you select burst, until the gauge expires\x01",
            "In the case of#2CAlly can act unilaterally#5CIt will look like.\x02\x03",
            "※At this time,#2CState abnormality of all allies recovers#5CIn addition,\x01",
            "During activation#2CIncreases attack power by 20, CP also rises automatically#5CTo do.\x02\x03",
            "※ Further ── Arts that take time to activate\x01",
            "In the case of#2CIt can be activated immediately#5C.\x02",
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
            "※ Burst gauge is for all the fellows\x01",
            "It reflects \"tension\".\x02\x03",
            "※ Every time an ally attacks, it will rise,\x01",
            "When attacking continuously or attacking all at once\x01",
            "I'm going up and down.\x02\x03",
            "※ Conversely, if attacked by the enemy will be a little lower\x01",
            "If you do not use several turns in the MAX state,\x01",
            "The gauge falls by one level.\x02\x03",
            "It is still#2CWhen there are companions of the battle impossible state\x01",
            "I can not activate a burst#5CBecause\x01",
            " be careful.\x02",
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
            "※ \"burst\" was added to the manual of the investigation notebook,\x01",
            "It is now available for viewing.\x02",
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

    # Function_13_150E end

    def Function_14_2772(): pass

    label("Function_14_2772")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00001Fno time--\x01",
            "Let's hurry and head to the exit!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 29200, 3510, -3510, 270)
    EventEnd(0x4)
    Return()

    # Function_14_2772 end

    def Function_15_27BB(): pass

    label("Function_15_27BB")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00001Fno time--\x01",
            "Let's hurry and head to the exit!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -1900, 0, 28210, 180)
    EventEnd(0x4)
    Return()

    # Function_15_27BB end

    SaveToFile()

Try(main)
