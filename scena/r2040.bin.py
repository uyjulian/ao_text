﻿from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "r2040.bin",                # FileName
        "r2040",                    # MapName
        "r2040",                    # Location
        0x0062,                     # MapIndex
        "ed7202",
        0x00000000,                 # Flags
        ("r2040", "r0000_1", "", "", "", ""),   # include
        0x02,                       # PlaceNameNumber
        0x14,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 98, 0, 2, 0, 3],
    )

    BuildStringList((
        "r2040",                  # 0
        "Humming Gator",          # 1
        "Humming Gator",          # 2
        "鉄鋼ドリュー",           # 3
        "鉄鋼ドリュー",           # 4
        "br2000",                 # 5
        "br2000",                 # 6
        "br2000",                 # 7
        "br2000",                 # 8
        "To Crossbell City/Mining Town Mainz",# 9
        "To Doll Studio",         # 10
    ))

    ATBonus("ATBonus_2C0", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_11FE", 5,   2,   0,   3,   0,   3,   2)
    Sepith("Sepith_11E6", 3,   0,   1,   5,   3,   2,   0)

    MonsterBattlePostion("MonsterBattlePostion_320", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_324", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_328", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_32C", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_330", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_334", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_338", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_33C", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_380", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_384", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_388", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_38C", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_390", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_394", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_398", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_39C", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_300", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_304", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_308", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_30C", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_310", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_314", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_318", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_31C", 2, 13, 180)

    # monster count: 6

    BattleInfo(
        "BattleInfo_3A0", 0x0010, 54, 6, 90, 0, 1, 5, 0, "br2000", "Sepith_11FE", 30, 40, 20, 10,
        (
            ("ms77400.dat", 0, 0, 0, 0, 0, "ms77400.dat", 0, "MonsterBattlePostion_320", "MonsterBattlePostion_380", "ed7450", "ed7453", "ATBonus_2C0"),
            ("ms77400.dat", "ms77400.dat", 0, 0, 0, 0, "ms77400.dat", 0, "MonsterBattlePostion_300", "MonsterBattlePostion_380", "ed7450", "ed7453", "ATBonus_2C0"),
            ("ms77400.dat", "ms77400.dat", "ms62500.dat", 0, 0, 0, "ms77400.dat", 0, "MonsterBattlePostion_320", "MonsterBattlePostion_380", "ed7450", "ed7453", "ATBonus_2C0"),
            ("ms77400.dat", "ms77400.dat", "ms77400.dat", "ms62500.dat", 0, 0, "ms77400.dat", 0, "MonsterBattlePostion_300", "MonsterBattlePostion_380", "ed7450", "ed7453", "ATBonus_2C0"),
        )
    )

    BattleInfo(
        "BattleInfo_468", 0x0000, 54, 6, 45, 10, 1, 40, 0, "br2000", "Sepith_11E6", 30, 40, 20, 10,
        (
            ("ms65500.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_320", "MonsterBattlePostion_380", "ed7450", "ed7453", "ATBonus_2C0"),
            ("ms65500.dat", "ms65500.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_300", "MonsterBattlePostion_380", "ed7450", "ed7453", "ATBonus_2C0"),
            ("ms65500.dat", "ms62500.dat", "ms65500.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_320", "MonsterBattlePostion_380", "ed7450", "ed7453", "ATBonus_2C0"),
            ("ms65500.dat", "ms65500.dat", "ms69400.dat", "ms65500.dat", 0, 0, 0, 0, "MonsterBattlePostion_300", "MonsterBattlePostion_380", "ed7450", "ed7453", "ATBonus_2C0"),
        )
    )

    # event battle count: 4

    BattleInfo(
        "BattleInfo_530", 0x0C00, 255, 6, 0, 0, 3, 0, 0, "br2000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65500.dat", "ms65500.dat", "ms65500.dat", "ms65500.dat", "ms65500.dat", "ms65500.dat", "ms65500.dat", "ms65500.dat", "MonsterBattlePostion_300", "MonsterBattlePostion_380", "ed7453", "ed7453", "ATBonus_2C0"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_574", 0x0C00, 255, 6, 0, 0, 3, 0, 0, "br2000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms76001.dat", "ms76001.dat", "ms76001.dat", "ms76001.dat", "ms76001.dat", "ms76001.dat", 0, 0, "MonsterBattlePostion_320", "MonsterBattlePostion_380", "ed7453", "ed7453", "ATBonus_2C0"),
            (),
            (),
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
        "monster/ch77450.itc",               # 10
        "monster/ch77450.itc",               # 11
        "monster/ch65550.itc",               # 12
        "monster/ch65551.itc",               # 13
        "monster/ch76050.itc",               # 14
        "monster/ch76051.itc",               # 15
    ))

    DeclNpc(7150,    18010,   49779,   270,  484,  0x0, 0,   18,  0,   0,   0,   255, 255, 255,  0)
    DeclNpc(27010,   30000,   110900,  270,  484,  0x0, 0,   18,  0,   0,   0,   255, 255, 255,  0)
    DeclNpc(7150,    18010,   49779,   270,  484,  0x0, 0,   20,  0,   0,   1,   255, 255, 255,  0)
    DeclNpc(27010,   30000,   110900,  270,  484,  0x0, 0,   20,  0,   0,   1,   255, 255, 255,  0)

    DeclMonster(12080,   52050,   17990,   0x1010000,    "BattleInfo_3A0", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(10960,   58330,   18000,   0x1010000,    "BattleInfo_468", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(50640,   68970,   26000,   0x1010000,    "BattleInfo_3A0", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(43200,   97050,   30000,   0x1010000,    "BattleInfo_468", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(17560,   116590,  30000,   0x1010000,    "BattleInfo_3A0", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(70050,   122300,  40000,   0x1010000,    "BattleInfo_3A0", 0,   16,  0xFFFF, 2,  3)

    DeclActor(16000,   30000,   114000,  1200,    16000,   31000,   114000,  0x007C, 0,  4,  0x0000)
    DeclActor(7150,    18010,   49780,   1200,    7150,    18010,   49780,   0x007C, 0,  5,  0x0000)
    DeclActor(27010,   30000,   110900,  1200,    27010,   30000,   110900,  0x007C, 0,  6,  0x0000)

    PlaceName(-3.25, 0.0, -1.25, 0x0000, 0x0000, "To Crossbell City/Mining Town Mainz")
    PlaceName(81.0, 0.0, 161.5, 0x0000, 0x0000, "To Doll Studio")

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 0
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 1
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 2
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 3

    ScpFunction((
        "Function_0_608",          # 00, 0
        "Function_1_627",          # 01, 1
        "Function_2_646",          # 02, 2
        "Function_3_647",          # 03, 3
        "Function_4_9A4",          # 04, 4
        "Function_5_AF6",          # 05, 5
        "Function_6_E54",          # 06, 6
        "Function_7_11B2",         # 07, 7
    ))


    def Function_0_608(): pass

    label("Function_0_608")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_626")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_0_608")

    label("loc_626")

    Return()

    # Function_0_608 end

    def Function_1_627(): pass

    label("Function_1_627")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_645")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_1_627")

    label("loc_645")

    Return()

    # Function_1_627 end

    def Function_2_646(): pass

    label("Function_2_646")

    Return()

    # Function_2_646 end

    def Function_3_647(): pass

    label("Function_3_647")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_659")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0xFB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_659")

    OP_52(0xA, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_845")
    LoadEffect(0x9, "map/mprain00.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    SetMapObjFrame(0xFF, "model07_shade", 0x0, 0x1)
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x78, 0x0)
    Sound(128, 1, 100, 0)

    label("loc_845")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_8A5")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x78, 0x0)
    SetMapObjFrame(0xFF, "model07_shade", 0x0, 0x1)
    ClearMapObjFlags(0x1, 0x4)
    ClearMapObjFlags(0x2, 0x4)
    ClearMapObjFlags(0x3, 0x4)
    ClearMapObjFlags(0x4, 0x4)
    ClearMapObjFlags(0x5, 0x4)
    ClearMapObjFlags(0x6, 0x4)
    Jump("loc_8C9")

    label("loc_8A5")

    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x6, 0x4)

    label("loc_8C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E6, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8DC")
    OP_70(0x0, 0x0)
    Jump("loc_8E0")

    label("loc_8DC")

    OP_70(0x0, 0x1E)

    label("loc_8E0")

    LoadEffect(0x10, "event\\eva00_00.eff")
    OP_65(0x1, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 7)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_941")
    PlayEffect(0x10, 0x9, 0xFF, 0x0, 7150, 18010, 49780, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x1, 0x1)

    label("loc_941")

    OP_65(0x2, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3B, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_98D")
    PlayEffect(0x10, 0xA, 0xFF, 0x0, 27010, 30000, 110900, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x2, 0x1)

    label("loc_98D")

    OP_1C(0x0, 0x7, 0x0, 0x32, 0x0, 0x7, 0x0, 0x0)
    OP_1C(0x0, 0x8, 0x0, 0x32, 0x0, 0x7, 0x0, 0x0)
    Return()

    # Function_3_647 end

    def Function_4_9A4(): pass

    label("Function_4_9A4")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E6, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AA0")
    Sound(14, 0, 100, 0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x643, 1)"), scpexpr(EXPR_END)), "loc_A29")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x643),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1E6, 7)
    OP_E0(0x5, 0x0)
    Jump("loc_A9B")

    label("loc_A29")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x643),
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

    label("loc_A9B")

    Jump("loc_AEA")

    label("loc_AA0")

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

    label("loc_AEA")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_9A4 end

    def Function_5_AF6(): pass

    label("Function_5_AF6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_CAE")
    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 7)), scpexpr(EXPR_END)), "loc_C8F")
    LoadEffect(0x7, "event\\eva07_00.eff")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "It looks like something is buried.\x01",
            "Dig it out?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C8A")
    ClearScenarioFlags(0x3A, 7)
    OP_65(0x1, 0x1)
    StopEffect(0x9, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 7)), scpexpr(EXPR_END)), "loc_C87")
    ClearScenarioFlags(0x38, 7)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_BAC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_BAC)
    TurnDirection(0x8, 0x0, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    PlayEffect(0x7, 0x1, 0x8, 0x1, 0, 0, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    Sound(601, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Monsters appeared!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Battle("BattleInfo_530", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0x8, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C82")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C69")
    Call(1, 5)
    Jump("loc_C82")

    label("loc_C69")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C7F")
    Call(1, 4)
    Jump("loc_C82")

    label("loc_C7F")

    Call(1, 3)

    label("loc_C82")

    Jump("loc_C8A")

    label("loc_C87")

    Call(1, 1)

    label("loc_C8A")

    Jump("loc_CA5")

    label("loc_C8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 7)), scpexpr(EXPR_END)), "loc_CA5")
    ClearScenarioFlags(0x38, 7)
    OP_65(0x1, 0x1)
    StopEffect(0x9, 0x2)
    Call(1, 0)

    label("loc_CA5")

    TalkEnd(0xFF)
    Return()

    label("loc_CAE")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 7)), scpexpr(EXPR_END)), "loc_E39")
    LoadEffect(0x7, "event\\eva07_00.eff")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "It looks like something is buried.\x01",
            "Dig it out?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E34")
    ClearScenarioFlags(0x3A, 7)
    OP_65(0x1, 0x1)
    StopEffect(0x9, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 7)), scpexpr(EXPR_END)), "loc_E31")
    ClearScenarioFlags(0x38, 7)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_D56():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_D56)
    TurnDirection(0xA, 0x0, 0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    PlayEffect(0x7, 0x1, 0xA, 0x1, 0, 0, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    Sound(601, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Monsters appeared!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Battle("BattleInfo_574", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xA, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E2C")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E13")
    Call(1, 5)
    Jump("loc_E2C")

    label("loc_E13")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E29")
    Call(1, 4)
    Jump("loc_E2C")

    label("loc_E29")

    Call(1, 3)

    label("loc_E2C")

    Jump("loc_E34")

    label("loc_E31")

    Call(1, 1)

    label("loc_E34")

    Jump("loc_E4F")

    label("loc_E39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 7)), scpexpr(EXPR_END)), "loc_E4F")
    ClearScenarioFlags(0x38, 7)
    OP_65(0x1, 0x1)
    StopEffect(0x9, 0x2)
    Call(1, 0)

    label("loc_E4F")

    TalkEnd(0xFF)
    Return()

    # Function_5_AF6 end

    def Function_6_E54(): pass

    label("Function_6_E54")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_100C")
    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3B, 0)), scpexpr(EXPR_END)), "loc_FED")
    LoadEffect(0x7, "event\\eva07_00.eff")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "It looks like something is buried.\x01",
            "Dig it out?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FE8")
    ClearScenarioFlags(0x3B, 0)
    OP_65(0x2, 0x1)
    StopEffect(0xA, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 0)), scpexpr(EXPR_END)), "loc_FE5")
    ClearScenarioFlags(0x39, 0)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_F0A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_F0A)
    TurnDirection(0x9, 0x0, 0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    PlayEffect(0x7, 0x1, 0x9, 0x1, 0, 0, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    Sound(601, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Monsters appeared!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Battle("BattleInfo_530", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x9, 0x80)
    ClearChrFlags(0x9, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FE0")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_FC7")
    Call(1, 5)
    Jump("loc_FE0")

    label("loc_FC7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_FDD")
    Call(1, 4)
    Jump("loc_FE0")

    label("loc_FDD")

    Call(1, 3)

    label("loc_FE0")

    Jump("loc_FE8")

    label("loc_FE5")

    Call(1, 1)

    label("loc_FE8")

    Jump("loc_1003")

    label("loc_FED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 0)), scpexpr(EXPR_END)), "loc_1003")
    ClearScenarioFlags(0x39, 0)
    OP_65(0x2, 0x1)
    StopEffect(0xA, 0x2)
    Call(1, 0)

    label("loc_1003")

    TalkEnd(0xFF)
    Return()

    label("loc_100C")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3B, 0)), scpexpr(EXPR_END)), "loc_1197")
    LoadEffect(0x7, "event\\eva07_00.eff")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "It looks like something is buried.\x01",
            "Dig it out?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1192")
    ClearScenarioFlags(0x3B, 0)
    OP_65(0x2, 0x1)
    StopEffect(0xA, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 0)), scpexpr(EXPR_END)), "loc_118F")
    ClearScenarioFlags(0x39, 0)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_10B4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_10B4)
    TurnDirection(0xB, 0x0, 0)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    PlayEffect(0x7, 0x1, 0xB, 0x1, 0, 0, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    Sound(601, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Monsters appeared!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Battle("BattleInfo_574", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0xB, 0x80)
    ClearChrFlags(0xB, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_118A")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1171")
    Call(1, 5)
    Jump("loc_118A")

    label("loc_1171")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1187")
    Call(1, 4)
    Jump("loc_118A")

    label("loc_1187")

    Call(1, 3)

    label("loc_118A")

    Jump("loc_1192")

    label("loc_118F")

    Call(1, 1)

    label("loc_1192")

    Jump("loc_11AD")

    label("loc_1197")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 0)), scpexpr(EXPR_END)), "loc_11AD")
    ClearScenarioFlags(0x39, 0)
    OP_65(0x2, 0x1)
    StopEffect(0xA, 0x2)
    Call(1, 0)

    label("loc_11AD")

    TalkEnd(0xFF)
    Return()

    # Function_6_E54 end

    def Function_7_11B2(): pass

    label("Function_7_11B2")

    Call(1, 6)
    Return()

    # Function_7_11B2 end

    SaveToFile()

Try(main)
