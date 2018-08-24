from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c1460.bin",                # FileName
        "c1460",                    # MapName
        "c1460",                    # Location
        0x0034,                     # MapIndex
        "ed7302",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 52, 0, 1, 0, 2],
    )

    BuildStringList((
        "c1460",                  # 0
        "ジェラルム・ポー",       # 1
        "bc1470",                 # 2
        "bc1470",                 # 3
        "bc1460",                 # 4
        "bc1460",                 # 5
        "bc1470",                 # 6
        "bc1470",                 # 7
        "bc1460",                 # 8
    ))

    ATBonus("ATBonus_398", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)
    ATBonus("ATBonus_3B8", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_3D8", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_3DC", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_3E0", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_3E4", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_3E8", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_3EC", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_3F0", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_3F4", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_458", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_45C", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_460", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_464", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_468", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_46C", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_470", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_474", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_418", 7, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_41C", 9, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_420", 6, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_424", 10, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_428", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_42C", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_430", 7, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_434", 9, 15, 180)
    MonsterBattlePostion("MonsterBattlePostion_478", 8, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_47C", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_480", 5, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_484", 11, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_488", 2, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_48C", 14, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_490", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_494", 0, 0, 180)

    # monster count: 10

    BattleInfo(
        "BattleInfo_564", 0x0000, 50, 6, 45, 10, 1, 30, 7, "bc1460", 0x00000000, 100, 0, 0, 0,
        (
            ("ms62001.dat", "ms62001.dat", "ms62001.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_3D8", "MonsterBattlePostion_458", "ed7450", "ed7453", "ATBonus_398"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_520", 0x0000, 50, 6, 45, 10, 1, 40, 7, "bc1460", 0x00000000, 100, 0, 0, 0,
        (
            ("ms69001.dat", "ms75900.dat", "ms75900.dat", "ms75900.dat", 0, 0, 0, 0, "MonsterBattlePostion_3D8", "MonsterBattlePostion_458", "ed7450", "ed7453", "ATBonus_398"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_5A8", 0x0000, 50, 6, 45, 10, 1, 40, 7, "bc1470", 0x00000000, 100, 0, 0, 0,
        (
            ("ms75900.dat", "ms75900.dat", "ms75900.dat", "ms75900.dat", "ms75900.dat", "ms75900.dat", 0, 0, "MonsterBattlePostion_418", "MonsterBattlePostion_458", "ed7450", "ed7453", "ATBonus_398"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_4DC", 0x0000, 50, 6, 45, 10, 1, 30, 7, "bc1470", 0x00000000, 100, 0, 0, 0,
        (
            ("ms62001.dat", "ms62001.dat", "ms62001.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_418", "MonsterBattlePostion_458", "ed7450", "ed7453", "ATBonus_398"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_630", 0x0812, 255, 6, 0, 0, 0, 0, 0, "bc1460", 0x00000000, 100, 0, 0, 0,
        (
            ("ms64900.dat", "ms75900.dat", "ms75900.dat", "ms75900.dat", "ms75900.dat", "ms75900.dat", "ms75900.dat", 0, "MonsterBattlePostion_478", "MonsterBattlePostion_458", "ed7451", "ed7453", "ATBonus_3B8"),
            (),
            (),
            (),
        )
    )

    # event battle count: 2

    BattleInfo(
        "BattleInfo_5EC", 0x0000, 50, 6, 45, 0, 1, 0, 0, "bc1470", 0x00000000, 100, 0, 0, 0,
        (
            ("ms69001.dat", "ms75900.dat", "ms69001.dat", "ms75900.dat", "ms75900.dat", "ms69001.dat", "ms69001.dat", "ms75900.dat", "MonsterBattlePostion_418", "MonsterBattlePostion_458", "ed7451", "ed7453", "ATBonus_398"),
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
        "monster/ch69050.itc",               # 10
        "monster/ch69051.itc",               # 11
        "monster/ch62050.itc",               # 12
        "monster/ch62051.itc",               # 13
        "monster/ch64950.itc",               # 14
        "monster/ch64951.itc",               # 15
        "monster/ch75950.itc",               # 16
        "monster/ch75950.itc",               # 17
    ))

    DeclNpc(4294925866, 500,     152000,  0,    484,  0x0, 0,   16,  0,   0,   0,   255, 255, 255,  0)

    DeclMonster(6980,    54510,   30,      0x1010000,    "BattleInfo_564", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(55560,   6870,    30,      0x1010000,    "BattleInfo_520", 0,   22,  0xFFFF, 0,  1)
    DeclMonster(4294850046, 4294966686, 0,       0x1010000,    "BattleInfo_5A8", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(4294862926, 56030,   30,      0x1010000,    "BattleInfo_520", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(4294859316, 4294913526, 30,      0x1010000,    "BattleInfo_4DC", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(4294871256, 159080,  0,       0x1010000,    "BattleInfo_4DC", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(4294922086, 156150,  30,      0x1010000,    "BattleInfo_520", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(4294860596, 98240,   0,       0x1010000,    "BattleInfo_520", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(4294858676, 93580,   0,       0x1010000,    "BattleInfo_564", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(4294867296, 211500,  0,       0x18500B4,    "BattleInfo_630", 0,   20,  0xFFFF, 4,  5)

    DeclEvent(0x0040, 0, 9,   -100.0,                211.5,                 0.0,                   16.0,                  [0.125,                -0.0,                  0.0,                   0.0,                   -0.0,                  0.125,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.25,                  0.0,                   12.5,                  -26.4375,              -0.0,                  1.0])

    DeclActor(4294857296, 0,       4294916296, 1200,    4294857296, 1000,    4294916296, 0x007C, 0,  3,  0x0000)
    DeclActor(4294858296, 0,       98000,   1200,    4294858296, 1000,    98000,   0x007C, 0,  4,  0x0000)
    DeclActor(4294925866, 0,       152000,  1200,    4294925866, 1000,    152000,  0x007C, 0,  5,  0x0000)
    DeclActor(57000,   0,       7000,    1200,    57000,   1000,    7000,    0x007C, 0,  6,  0x0000)
    DeclActor(4294871796, 0,       57000,   1200,    4294871796, 1000,    57000,   0x007C, 0,  7,  0x0000)
    DeclActor(4294880296, 3500,    160000,  1200,    4294880296, 5100,    160000,  0x007C, 0,  8,  0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 0
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4])                      # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 2
    ChipFrameInfo(2000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 3
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 4
    ChipFrameInfo(2000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 5
    ChipFrameInfo(1200, 0, [0, 1, 2, 3, 4, 5])                   # 6
    ChipFrameInfo(1200, 0, [0, 1, 2, 3, 4, 5])                   # 7

    ScpFunction((
        "Function_0_700",          # 00, 0
        "Function_1_71D",          # 01, 1
        "Function_2_727",          # 02, 2
        "Function_3_A30",          # 03, 3
        "Function_4_B81",          # 04, 4
        "Function_5_CD2",          # 05, 5
        "Function_6_F88",          # 06, 6
        "Function_7_10F1",         # 07, 7
        "Function_8_1242",         # 08, 8
        "Function_9_12F3",         # 09, 9
        "Function_10_19C2",        # 0A, 10
    ))


    def Function_0_700(): pass

    label("Function_0_700")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_71C")
    OP_A1(0xFE, 0x3E8, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Jump("Function_0_700")

    label("loc_71C")

    Return()

    # Function_0_700 end

    def Function_1_71D(): pass

    label("Function_1_71D")

    OP_50(0x3, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_1_71D end

    def Function_2_727(): pass

    label("Function_2_727")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_791")
    SetMapObjFrame(0xFF, "CA02", 0x0, 0x1)
    SetMapObjFrame(0xFF, "model5", 0x0, 0x1)
    SetMapObjFrame(0xFF, "break", 0x1, 0x1)
    SetMapObjFrame(0xFF, "CA03", 0x0, 0x1)
    SetMapObjFrame(0xFF, "all01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "CA02", 0x1, 0x2)
    SetMapObjFrame(0xFF, "model5", 0x1, 0x2)
    Jump("loc_7EA")

    label("loc_791")

    SetMapObjFrame(0xFF, "model5", 0x1, 0x1)
    SetMapObjFrame(0xFF, "CA03", 0x0, 0x1)
    SetMapObjFrame(0xFF, "break", 0x0, 0x1)
    SetMapObjFrame(0xFF, "CA02", 0x0, 0x1)
    SetMapObjFrame(0xFF, "all11", 0x0, 0x1)
    SetMapObjFrame(0xFF, "CA03", 0x1, 0x2)
    SetMapObjFrame(0xFF, "break", 0x1, 0x2)

    label("loc_7EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E5, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7FD")
    OP_70(0x9, 0x0)
    Jump("loc_801")

    label("loc_7FD")

    OP_70(0x9, 0x1E)

    label("loc_801")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E5, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_814")
    OP_70(0xA, 0x0)
    Jump("loc_818")

    label("loc_814")

    OP_70(0xA, 0x1E)

    label("loc_818")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E5, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_82B")
    OP_70(0xB, 0x0)
    Jump("loc_82F")

    label("loc_82B")

    OP_70(0xB, 0x1E)

    label("loc_82F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E5, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_842")
    OP_70(0xC, 0x0)
    Jump("loc_846")

    label("loc_842")

    OP_70(0xC, 0x1E)

    label("loc_846")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E5, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_859")
    OP_70(0xD, 0x0)
    Jump("loc_85D")

    label("loc_859")

    OP_70(0xD, 0x1E)

    label("loc_85D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_889")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21C, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_884")
    ClearChrFlags(0x12, 0x80)
    ModifyEventFlags(1, 0, 0x80)
    SetChrFlags(0x12, 0x8000)

    label("loc_884")

    Jump("loc_893")

    label("loc_889")

    SetChrFlags(0x12, 0x80)
    ModifyEventFlags(0, 0, 0x80)

    label("loc_893")

    OP_52(0x12, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_997")
    SetMapObjFrame(0xFF, "hikari00_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari01_add", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_997")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9D6")
    OP_7D(0xD2, 0xD2, 0xE6, 0x0, 0x0)
    SetMapObjFrame(0xFF, "hikari00_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari01_add", 0x0, 0x1)

    label("loc_9D6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x133, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A2F")
    OP_50(0x3, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_BF(0x0, 0xA)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_BF(0x1, 0xA)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_BF(0x4, 0xA)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_BF(0x8, 0xA)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A2F")
    Event(0, 10)

    label("loc_A2F")

    Return()

    # Function_2_727 end

    def Function_3_A30(): pass

    label("Function_3_A30")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E5, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B2C")
    Sound(14, 0, 100, 0)
    OP_74(0x9, 0x1E)
    OP_71(0x9, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x642, 1)"), scpexpr(EXPR_END)), "loc_AB5")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x642),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1E5, 3)
    OP_E0(0x5, 0x0)
    Jump("loc_B27")

    label("loc_AB5")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x642),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " is inside the chest.\x01",
            "Since you have too many,\x01",
            "you gave it up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x9, 0x1E, 0x0, 0x0, 0x0)

    label("loc_B27")

    Jump("loc_B75")

    label("loc_B2C")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is nothing in the\x01",
            "chest.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_B75")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_A30 end

    def Function_4_B81(): pass

    label("Function_4_B81")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E5, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C7D")
    Sound(14, 0, 100, 0)
    OP_74(0xA, 0x1E)
    OP_71(0xA, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x9C, 1)"), scpexpr(EXPR_END)), "loc_C06")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x9C),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1E5, 4)
    OP_E0(0x5, 0x0)
    Jump("loc_C78")

    label("loc_C06")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x9C),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " is inside the chest.\x01",
            "Since you have too many,\x01",
            "you gave it up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0xA, 0x1E, 0x0, 0x0, 0x0)

    label("loc_C78")

    Jump("loc_CC6")

    label("loc_C7D")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is nothing in the\x01",
            "chest.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_CC6")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_B81 end

    def Function_5_CD2(): pass

    label("Function_5_CD2")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E5, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EA3")
    Sound(14, 0, 100, 0)
    OP_74(0xB, 0x1E)
    OP_71(0xB, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x216, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DD5")
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0x8, 0x0, 0)
    OP_98(0x8, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_D2F():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_D2F)

    def lambda_D49():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_D49)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Monsters appeared!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    WaitChrThread(0x8, 1)
    Battle("BattleInfo_5EC", 0x0, 0x0, 0x0, 0xB, 0xFF)
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0x8, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_DB6"),
        (2, "loc_DC5"),
        (1, "loc_DD2"),
        (SWITCH_DEFAULT, "loc_DD5"),
    )


    label("loc_DB6")

    SetScenarioFlags(0x216, 0)
    OP_70(0xB, 0x1E)
    Sleep(500)
    Jump("loc_DD5")

    label("loc_DC5")

    OP_70(0xB, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_DD2")

    OP_B9(0x0)
    Return()

    label("loc_DD5")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x84, 1)"), scpexpr(EXPR_END)), "loc_E2E")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x84),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1E5, 5)
    OP_E0(0x5, 0x0)
    Jump("loc_E9E")

    label("loc_E2E")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x84),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " is inside the chest.\x01",
            "Since you have too many,\x01",
            "you gave it up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0xB, 0x1E, 0x0, 0x0, 0x0)

    label("loc_E9E")

    Jump("loc_EE1")

    label("loc_EA3")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is nothing in the\x01",
            "chest.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_EE1")

    Sleep(30)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x133, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F7F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_BF(0x0, 0xA)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_BF(0x1, 0xA)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_BF(0x4, 0xA)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_BF(0x8, 0xA)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F7F")
    OP_50(0x3, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(814, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Finished a battle with\x01",
            "Master Quartz set!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x133, 0)
    OP_29(0x65, 0x1, 0x2)

    label("loc_F7F")

    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_CD2 end

    def Function_6_F88(): pass

    label("Function_6_F88")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E5, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10C1")
    Sound(14, 0, 100, 0)
    OP_74(0xC, 0x1E)
    OP_71(0xC, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    OP_70(0xC, 0x1E)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddSepith(0x0, 30)
    AddSepith(0x1, 30)
    AddSepith(0x2, 30)
    AddSepith(0x3, 30)
    AddSepith(0x4, 30)
    AddSepith(0x5, 30)
    AddSepith(0x6, 30)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#56I Earth Sepith  x30\x01\x07\x02",
            "#57I Water Sepith  x30\x01\x07\x02",
            "#58I Fire Sepith   x30\x01\x07\x02",
            "#59I Wind Sepith   x30\x01\x07\x02",
            "#60I Time Sepith   x30\x01\x07\x02",
            "#61I Space Sepith  x30\x01\x07\x02",
            "#62I Mirage Sepith x30\x01\x07\x00",
            "obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x1E5, 6)
    OP_E0(0x5, 0x0)
    Jump("loc_10DF")

    label("loc_10C1")


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

    label("loc_10DF")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_F88 end

    def Function_7_10F1(): pass

    label("Function_7_10F1")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E5, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11ED")
    Sound(14, 0, 100, 0)
    OP_74(0xD, 0x1E)
    OP_71(0xD, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1F8, 1)"), scpexpr(EXPR_END)), "loc_1176")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1F8),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1E5, 7)
    OP_E0(0x5, 0x0)
    Jump("loc_11E8")

    label("loc_1176")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1F8),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " is inside the chest.\x01",
            "Since you have too many,\x01",
            "you gave it up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0xD, 0x1E, 0x0, 0x0, 0x0)

    label("loc_11E8")

    Jump("loc_1236")

    label("loc_11ED")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is nothing in the\x01",
            "chest.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_1236")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_10F1 end

    def Function_8_1242(): pass

    label("Function_8_1242")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            ""Seasonal Simple\x01",
            "Recipes" is here.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2, 0x0)"), scpexpr(EXPR_END)), "loc_12EF")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B2(0xB)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12EF")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Learned the \x07\x02",
            ""Light\x01",
            "Burger"\x07\x00",
            " recipe.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_12EF")

    TalkEnd(0xFF)
    Return()

    # Function_8_1242 end

    def Function_9_12F3(): pass

    label("Function_9_12F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21C, 0)), scpexpr(EXPR_END)), "loc_12FD")
    Return()

    label("loc_12FD")

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
            "A large monster is\x01",
            "wandering about.\x02",
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
        (1, "loc_13DB"),
        (SWITCH_DEFAULT, "loc_13F4"),
    )


    label("loc_13DB")

    Sleep(500)
    OP_E2(0x2)
    OP_90(0x0, -100110, 30, 206380, 0)
    EventEnd(0x5)
    Return()

    label("loc_13F4")

    Battle("BattleInfo_630", 0x0, 0x0, 0x100, 0xC, 0xFF)
    OP_E2(0x2)
    EventBegin(0x1)
    OP_68(-100110, 1030, 206380, 0)
    OP_90(0x0, -100110, 30, 206380, 0)
    OP_90(0x1, -100110, 30, 206380, 0)
    OP_90(0x2, -100110, 30, 206380, 0)
    OP_90(0x3, -100110, 30, 206380, 0)
    OP_90(0x4, -100110, 30, 206380, 0)
    OP_90(0x5, -100110, 30, 206380, 0)
    OP_90(0x6, -100110, 30, 206380, 0)
    OP_90(0x7, -100110, 30, 206380, 0)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (2, "loc_14B6"),
        (1, "loc_14BB"),
        (SWITCH_DEFAULT, "loc_14BE"),
    )


    label("loc_14B6")

    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    label("loc_14BB")

    OP_B9(0x0)
    Return()

    label("loc_14BE")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-100000, 1030, 207140, 0)
    MoveCamera(45, 32, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19000, 0)
    SetChrFlags(0x12, 0x80)
    OP_E2(0x3)
    Sleep(400)
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Wanted monster\x01",
            "exterminated!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0xA),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    AddItemNumber(0xA, 1)
    SetChrPos(0x101, -100000, 30, 206000, 0)
    SetChrPos(0x102, -100000, 30, 208000, 180)
    SetChrPos(0x105, -99000, 30, 207000, 270)
    SetChrPos(0x109, -101000, 30, 207000, 90)
    FadeToBright(300, 0)
    OP_0D()
    Sleep(400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1744")

    ChrTalk(
        0x101,
        "#00004FA craft book, huh.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10305FIt looks pretty old.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10103FIt looks like a\x01",
            "combination craft is\x01",
            "written in it, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FIt looks close to Lloyd and\x01",
            "Wazy's styles. I wonder if\x01",
            "you guys could reproduce it?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00002FI see. If it's like\x01",
            "this, then...\x02\x03",
            "Wazy, want to give it a\x01",
            "try?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10304FHaha, of course.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x21E, 1)
    Jump("loc_1816")

    label("loc_1744")


    ChrTalk(
        0x102,
        (
            "#00100FA craft book... It looks like\x01",
            "there's a usable combination\x01",
            "craft recorded in it.\x02\x03",
            "I feel like Lloyd and Wazy\x01",
            "could handle it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FWazy, want to give it a\x01",
            "try?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10300FHaha, of course.\x02",
    )

    CloseMessageWindow()

    label("loc_1816")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    Sound(517, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x29, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1844")
    AddCraft(0x0, 0x1A1)
    AddCraft(0x4, 0x1A1)
    Jump("loc_184C")

    label("loc_1844")

    AddCraft(0x0, 0x18D)
    AddCraft(0x4, 0x18D)

    label("loc_184C")

    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd and Wazy learned the\x01\x07\x02",
            "Strike Heaven\x07\x05",
            " Combi Craft.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "By each expending 100 CP,\x01",
            "a powerful combination\x01",
            "attack can be unleashed.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x21C, 0)
    OP_29(0x67, 0x4, 0x10)
    OP_29(0x67, 0x4, 0x2)
    OP_29(0x67, 0x1, 0x2)
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x133, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19B8")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_BF(0x0, 0xA)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_BF(0x1, 0xA)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_BF(0x4, 0xA)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_BF(0x8, 0xA)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_19B8")
    OP_50(0x3, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(300, 0)
    OP_0D()
    Sound(814, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Finished a battle with\x01",
            "Master Quartz set!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x133, 0)
    OP_29(0x65, 0x1, 0x2)
    FadeToDark(1000, 0, -1)
    OP_0D()

    label("loc_19B8")

    OP_E2(0x2)
    ModifyEventFlags(0, 0, 0x80)
    EventEnd(0x5)
    Return()

    # Function_9_12F3 end

    def Function_10_19C2(): pass

    label("Function_10_19C2")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Sound(814, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Finished a battle with\x01",
            "Master Quartz set!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x133, 0)
    OP_29(0x65, 0x1, 0x2)
    EventEnd(0x5)
    Return()

    # Function_10_19C2 end

    SaveToFile()

Try(main)
