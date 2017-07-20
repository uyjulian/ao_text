﻿from ScenarioHelper import *

def main():
    CreateScenaFile(
        "m2040.bin",                # FileName
        "m2040",                    # MapName
        "m2040",                    # Location
        0x0074,                     # MapIndex
        "ed7303",
        0x00080000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x23,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 116, 0, 1, 0, 2],
    )

    BuildStringList((
        "m2040",                  # 0
        "Durahan",           # 1
        "Hammer pack",         # 2
        "Val Gem",           # 3
        "Val Gem",           # 4
        "bm2000",                 # 5
        "bm2000",                 # 6
        "bm2000",                 # 7
        "bm2000",                 # 8
        "bm2000",                 # 9
    ))

    ATBonus("ATBonus_2FC", 100, 5, 1, 5, 1, 5, 1, 5, 5, 5, 5, 5, 5, 0, 0, 0)
    ATBonus("ATBonus_30C", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    Sepith("Sepith_239C", 2,   10,  4,   2,   6,   0,   3)
    Sepith("Sepith_23A4", 5,   4,   0,   3,   8,   10,  0)
    Sepith("Sepith_2394", 6,   6,   0,   4,   6,   0,   6)
    Sepith("Sepith_238C", 9,   6,   2,   5,   3,   0,   3)

    MonsterBattlePostion("MonsterBattlePostion_34C", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_350", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_354", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_358", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_35C", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_360", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_364", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_368", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_3AC", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_3B0", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_3B4", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_3B8", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_3BC", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_3C0", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_3C4", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_3C8", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_32C", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_330", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_334", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_338", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_33C", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_340", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_344", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_348", 2, 13, 180)

    # monster count: 7

    BattleInfo(
        "BattleInfo_55C", 0x0000, 63, 6, 45, 4, 1, 30, 0, "bm2000", "Sepith_239C", 40, 30, 20, 10,
        (
            ("ms74500.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_34C", "MonsterBattlePostion_3AC", "ed7450", "ed7453", "ATBonus_2FC"),
            ("ms74500.dat", "ms74500.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_32C", "MonsterBattlePostion_3AC", "ed7450", "ed7453", "ATBonus_2FC"),
            ("ms74500.dat", "ms74400.dat", "ms74500.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_34C", "MonsterBattlePostion_3AC", "ed7450", "ed7453", "ATBonus_2FC"),
            ("ms74500.dat", "ms74500.dat", "ms74400.dat", "ms74500.dat", 0, 0, 0, 0, "MonsterBattlePostion_32C", "MonsterBattlePostion_3AC", "ed7450", "ed7453", "ATBonus_2FC"),
        )
    )

    BattleInfo(
        "BattleInfo_624", 0x0000, 63, 6, 45, 4, 1, 30, 0, "bm2000", "Sepith_23A4", 40, 30, 20, 10,
        (
            ("ms74600.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_34C", "MonsterBattlePostion_3AC", "ed7450", "ed7453", "ATBonus_2FC"),
            ("ms74600.dat", "ms74600.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_32C", "MonsterBattlePostion_3AC", "ed7450", "ed7453", "ATBonus_2FC"),
            ("ms74600.dat", "ms74500.dat", "ms74600.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_34C", "MonsterBattlePostion_3AC", "ed7450", "ed7453", "ATBonus_2FC"),
            ("ms74600.dat", "ms74600.dat", "ms74500.dat", "ms74600.dat", 0, 0, 0, 0, "MonsterBattlePostion_32C", "MonsterBattlePostion_3AC", "ed7450", "ed7453", "ATBonus_2FC"),
        )
    )

    BattleInfo(
        "BattleInfo_494", 0x0000, 63, 6, 45, 4, 1, 30, 0, "bm2000", "Sepith_2394", 40, 30, 20, 10,
        (
            ("ms74400.dat", "ms74400.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_32C", "MonsterBattlePostion_3AC", "ed7450", "ed7453", "ATBonus_2FC"),
            ("ms74400.dat", "ms74400.dat", "ms74400.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_34C", "MonsterBattlePostion_3AC", "ed7450", "ed7453", "ATBonus_2FC"),
            ("ms74400.dat", "ms74400.dat", "ms74400.dat", "ms74400.dat", 0, 0, 0, 0, "MonsterBattlePostion_32C", "MonsterBattlePostion_3AC", "ed7450", "ed7453", "ATBonus_2FC"),
            ("ms74400.dat", "ms74400.dat", "ms74400.dat", "ms74400.dat", "ms74400.dat", 0, 0, 0, "MonsterBattlePostion_34C", "MonsterBattlePostion_3AC", "ed7450", "ed7453", "ATBonus_2FC"),
        )
    )

    BattleInfo(
        "BattleInfo_3CC", 0x0000, 63, 6, 45, 4, 1, 30, 0, "bm2000", "Sepith_238C", 40, 30, 20, 10,
        (
            ("ms74300.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_34C", "MonsterBattlePostion_3AC", "ed7450", "ed7453", "ATBonus_2FC"),
            ("ms74300.dat", "ms74300.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_32C", "MonsterBattlePostion_3AC", "ed7450", "ed7453", "ATBonus_2FC"),
            ("ms74300.dat", "ms74600.dat", "ms74300.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_34C", "MonsterBattlePostion_3AC", "ed7450", "ed7453", "ATBonus_2FC"),
            ("ms74300.dat", "ms74300.dat", "ms74600.dat", "ms74300.dat", 0, 0, 0, 0, "MonsterBattlePostion_32C", "MonsterBattlePostion_3AC", "ed7450", "ed7453", "ATBonus_2FC"),
        )
    )

    # event battle count: 1

    BattleInfo(
        "BattleInfo_6EC", 0x0000, 63, 6, 45, 0, 1, 0, 0, "bm2000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms74000.dat", "ms74000.dat", "ms73000.dat", "ms73000.dat", "ms73000.dat", "ms74000.dat", "ms73000.dat", "ms74000.dat", "MonsterBattlePostion_32C", "MonsterBattlePostion_3AC", "ed7451", "ed7453", "ATBonus_30C"),
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
        "monster/ch74350.itc",               # 10
        "monster/ch74350.itc",               # 11
        "monster/ch74450.itc",               # 12
        "monster/ch74450.itc",               # 13
        "monster/ch74550.itc",               # 14
        "monster/ch74551.itc",               # 15
        "monster/ch74650.itc",               # 16
        "monster/ch74651.itc",               # 17
        "monster/ch74050.itc",               # 18
        "monster/ch74051.itc",               # 19
    ))

    DeclNpc(4294954227, 12500,   12899,   0,    484,  0x0, 0,   24,  0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   20,  0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   22,  0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   22,  0,   255, 255, 255, 255, 255,  0)

    DeclMonster(4294956276, 16020,   4000,    0x1010000,    "BattleInfo_55C", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(4294956916, 15850,   4294963296, 0x1010000,    "BattleInfo_624", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(4294957276, 16470,   4294955296, 0x1010000,    "BattleInfo_624", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(2170,    4294750186, 4000,    0x1010000,    "BattleInfo_494", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(1740,    4294751176, 12000,   0x1010000,    "BattleInfo_3CC", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(4280,    4294750776, 20000,   0x1010000,    "BattleInfo_624", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(150,     4294870556, 0,       0x1010000,    "BattleInfo_55C", 0,   20,  0xFFFF, 4,  5)

    DeclActor(4294954226, 12000,   12900,   1200,    4294954226, 13000,   12900,   0x007C, 0,  3,  0x0000)
    DeclActor(4294954296, 4294951296, 4294965326, 1200,    4294954296, 4294952296, 4294965326, 0x007C, 0,  4,  0x0000)
    DeclActor(4294950796, 8000,    0,       1200,    4294950796, 10000,   0,       0x007C, 0,  6,  0x0000)
    DeclActor(4294950796, 4294959296, 0,       1200,    4294950796, 4294960296, 0,       0x007C, 0,  5,  0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 0
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4])                      # 1
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 5])                   # 2
    ChipFrameInfo(3000, 0, [0, 1, 2, 3, 4, 5])                   # 3
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 4
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4, 5])                   # 5
    ChipFrameInfo(1000, 0, [0, 1, 2, 3])                         # 6
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4, 5])                   # 7

    ScpFunction((
        "Function_0_7C4",          # 00, 0
        "Function_1_7E1",          # 01, 1
        "Function_2_814",          # 02, 2
        "Function_3_CF2",          # 03, 3
        "Function_4_F09",          # 04, 4
        "Function_5_105A",         # 05, 5
        "Function_6_1086",         # 06, 6
        "Function_7_1186",         # 07, 7
        "Function_8_223E",         # 08, 8
        "Function_9_225B",         # 09, 9
        "Function_10_2276",        # 0A, 10
        "Function_11_22B8",        # 0B, 11
        "Function_12_230A",        # 0C, 12
    ))


    def Function_0_7C4(): pass

    label("Function_0_7C4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7E0")
    OP_A1(0xFE, 0x320, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Jump("Function_0_7C4")

    label("loc_7E0")

    Return()

    # Function_0_7C4 end

    def Function_1_7E1(): pass

    label("Function_1_7E1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x157, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7C, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7C, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7C, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_813")
    SetMapFlags(0x10000000)
    Event(0, 7)

    label("loc_813")

    Return()

    # Function_1_7E1 end

    def Function_2_814(): pass

    label("Function_2_814")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 5)), scpexpr(EXPR_END)), "loc_826")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x130), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_826")

    Sound(129, 1, 100, 0)
    OP_52(0x10, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xA7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xA7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xA7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xA7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xA7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xA7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xA7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xA7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    PlayEffect(0x2F, 0x0, 0xC, 0x41, 0, 0, 0, 0, 0, 0, 1250, 750, 1250, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2F, 0x1, 0xD, 0x41, 0, 0, 0, 0, 0, 0, 1250, 750, 1250, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2F, 0x2, 0xE, 0x41, 0, 0, 0, 0, 0, 0, 1250, 750, 1250, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2F, 0x3, 0xF, 0x41, 0, 0, 0, 0, 0, 0, 1250, 750, 1250, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2F, 0x4, 0x10, 0x41, 0, 0, 0, 0, 0, 0, 1250, 750, 1250, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2F, 0x5, 0x11, 0x41, 0, 0, 0, 0, 0, 0, 1250, 750, 1250, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2F, 0x6, 0x12, 0x41, 0, 0, 0, 0, 0, 0, 1250, 750, 1250, 0xFF, 0, 0, 0, 0)
    SetBarrier(0x0, 0x0, 0x1, 0x0, -16500, -8000, 0, 6000, 3000, 90000)
    SetBarrier(0x3, 0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x150, 7)), scpexpr(EXPR_END)), "loc_CB1")
    SetMapObjFrame(0x4, "root", 0x2, "on")
    ClearMapObjFlags(0x4, 0x2)
    OP_65(0x2, 0x1)
    Jump("loc_CC3")

    label("loc_CB1")

    SetMapObjFrame(0x4, "root", 0x2, "off")
    SetMapObjFlags(0x4, 0x2)

    label("loc_CC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EE, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CD6")
    OP_70(0x5, 0x0)
    Jump("loc_CDA")

    label("loc_CD6")

    OP_70(0x5, 0x1E)

    label("loc_CDA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EE, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CED")
    OP_70(0x6, 0x0)
    Jump("loc_CF1")

    label("loc_CED")

    OP_70(0x6, 0x1E)

    label("loc_CF1")

    Return()

    # Function_2_814 end

    def Function_3_CF2(): pass

    label("Function_3_CF2")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EE, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EC3")
    Sound(14, 0, 100, 0)
    OP_74(0x5, 0x1E)
    OP_71(0x5, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x218, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DF1")
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0x8, 0x0, 0)
    OP_98(0x8, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_D4F():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_D4F)

    def lambda_D69():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_D69)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A monster appeared!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    WaitChrThread(0x8, 1)
    Battle("BattleInfo_6EC", 0x0, 0x0, 0x0, 0xB, 0xFF)
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0x8, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_DD2"),
        (2, "loc_DE1"),
        (1, "loc_DEE"),
        (SWITCH_DEFAULT, "loc_DF1"),
    )


    label("loc_DD2")

    SetScenarioFlags(0x218, 1)
    OP_70(0x5, 0x1E)
    Sleep(500)
    Jump("loc_DF1")

    label("loc_DE1")

    OP_70(0x5, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_DEE")

    OP_B9(0x0)
    Return()

    label("loc_DF1")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('苍耀珠', 1)"), scpexpr(EXPR_END)), "loc_E4E")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '苍耀珠'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1EE, 6)
    OP_E0(0x5, 0x0)
    Jump("loc_EBE")

    label("loc_E4E")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0x3E7,
        (
            "In the treasure box",
            scpstr(SCPSTR_CODE_ITEM, '苍耀珠'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Is contained.\x01",
            "Because my belongings are full,",
            scpstr(SCPSTR_CODE_ITEM, '苍耀珠'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I gave up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x5, 0x1E, 0x0, 0x0, 0x0)

    label("loc_EBE")

    Jump("loc_EFD")

    label("loc_EC3")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is nothing in the treasure box.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_EFD")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_CF2 end

    def Function_4_F09(): pass

    label("Function_4_F09")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EE, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1009")
    Sound(14, 0, 100, 0)
    OP_74(0x6, 0x1E)
    OP_71(0x6, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('结晶碎片', 1)"), scpexpr(EXPR_END)), "loc_F92")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '结晶碎片'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1EE, 7)
    OP_E0(0x5, 0x0)
    Jump("loc_1004")

    label("loc_F92")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            "In the treasure box",
            scpstr(SCPSTR_CODE_ITEM, '结晶碎片'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Is contained.\x01",
            "Because my belongings are full,",
            scpstr(SCPSTR_CODE_ITEM, '结晶碎片'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I gave up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x6, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1004")

    Jump("loc_104E")

    label("loc_1009")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is nothing in the treasure box.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_104E")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_F09 end

    def Function_5_105A(): pass

    label("Function_5_105A")

    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The door is tightly closed.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_5_105A end

    def Function_6_1086(): pass

    label("Function_6_1086")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x150, 7)), scpexpr(EXPR_END)), "loc_10C7")
    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The key has already been removed.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Jump("loc_1185")

    label("loc_10C7")

    EventBegin(0x1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A lock is hanging on the door.\x01",
            "Would you like to remove it?\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Yes\x01",      # 0
            "No\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_117E")
    Fade(500)
    OP_68(-12910, 8600, 1580, 0)
    MoveCamera(60, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(19500, 0)
    OP_0D()
    Sleep(1000)
    Sound(119, 0, 100, 0)
    SetMapObjFrame(0x4, "root", 0x2, "move")
    Sleep(1500)
    ClearMapObjFlags(0x4, 0x2)
    OP_65(0x2, 0x1)
    SetScenarioFlags(0x150, 7)

    label("loc_117E")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)

    label("loc_1185")

    Return()

    # Function_6_1086 end

    def Function_7_1186(): pass

    label("Function_7_1186")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x1)
    SetChrChipByIndex(0x9, 0x15)
    SetChrChipByIndex(0xA, 0x17)
    SetChrChipByIndex(0xB, 0x17)
    SetChrSubChip(0x9, 0x0)
    SetChrSubChip(0xA, 0x0)
    SetChrSubChip(0xB, 0x0)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x8000)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0x9, 0x20)
    SetChrFlags(0xA, 0x20)
    SetChrFlags(0xB, 0x20)
    SetChrPos(0x9, -11020, 4000, 16020, 0)
    SetChrPos(0xA, -10380, -4000, 15850, 0)
    SetChrPos(0xB, -10020, -12000, 16470, 0)
    OP_52(0x9, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    PlayEffect(0x2F, 0x0, 0x9, 0x41, 0, 0, 0, 0, 0, 0, 1250, 750, 1250, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2F, 0x1, 0xA, 0x41, 0, 0, 0, 0, 0, 0, 1250, 750, 1250, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2F, 0x2, 0xB, 0x41, 0, 0, 0, 0, 0, 0, 1250, 750, 1250, 0xFF, 0, 0, 0, 0)
    OP_68(-17670, 7800, 10230, 0)
    MoveCamera(52, 16, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(11430, 0)
    SetChrPos(0x101, -13240, 8000, 930, 90)
    SetChrPos(0x102, -13840, 8000, -490, 90)
    SetChrPos(0x103, -14390, 8000, -1630, 90)
    SetChrPos(0x104, -14200, 8000, 1870, 90)
    SetChrPos(0x109, -15200, 8000, 620, 90)
    SetChrPos(0x105, -15170, 8000, -630, 90)
    SetChrPos(0x18D, -12000, 8000, -20, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_68(-17670, -8200, 10230, 10000)
    BeginChrThread(0x9, 3, 0, 10)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)
    BeginChrThread(0xA, 3, 0, 11)
    Sleep(2000)
    BeginChrThread(0xB, 3, 0, 12)
    OP_6F(0x1)
    Sleep(1000)
    Fade(500)
    OP_68(-12650, 8900, 250, 0)
    MoveCamera(53, 26, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(22100, 0)
    SetCameraDistance(20100, 2000)
    OP_6F(0x10)
    StopEffect(0x0, 0x0)
    StopEffect(0x1, 0x0)
    StopEffect(0x2, 0x0)
    OP_0D()

    ChrTalk(
        0x18D,
        (
            "#04400Fsurely……\x01",
            "The atmosphere of the top three attributes\x01",
            "I feel it is dark.\x02\x03",
            "#04403FIt is the same as that time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10302FWell ……\x02\x03",
            "#10304FAfter all the church people\x01",
            "Such a thing\x01",
            "You seem to feel it?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x18D, 0x10E, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x18D,
        (
            "#04403FYes, spiritual signs\x01",
            "I have a technique to feel.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x18D, 0x103, 500)

    ChrTalk(
        0x18D,
        (
            "#04405Fby the way,\x01",
            "Tio also like that\x01",
            "It seems to have it … ….?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x18D, 500)

    ChrTalk(
        0x103,
        (
            "#12P#00203F… Well, well.\x02\x03",
            "#00208FIn my case I got acquired afterwards\x01",
            "Even \"sensitive ability\"\x01",
            "It should be said … …\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x18D, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x18D,
        (
            "#04403F……Excuse me.\x02\x03",
            "#04408FYou have entered\x01",
            "You seem to have heard it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#00203FNo, it is a matter of course.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003F(These two people, somewhere\x01",
            "Is there a similar place …? )\x02\x03",
            "#00001F── Anyway, tighten your mind\x01",
            "It seems necessary to go.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x18D, 0x10E, 0x1F4)

    ChrTalk(
        0x109,
        (
            "#6P#10103FOnce, when I came before\x01",
            "I have released the gimmick … ….\x02\x03",
            "#10100FTo go to the bell tower with \"bell\"\x01",
            "There should not be any difficulties to that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00300FWell, to that ghost\x01",
            "Let's say you are going to move on carefully.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10304FHuh, if you go enjoy it\x01",
            "Let's try it.\x02\x03",
            "#10302FRumored horror house tour\x01",
            "Well, yeah.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x105, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#11P#00106FWaji, you seem to play halfway\x01",
            "Please stop speechless.\x02\x03",
            "#00111F…… Because I am desperate for this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10309FOops, this is rude.\x01",
            "Did you not like this kind of thing?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#5P#00003FAnd anyway … …\x02\x03",
            "#00001FAlthough it searched once\x01",
            "An incomprehensible existence\x01",
            "There is a possibility of involvement.\x02\x03",
            "Take care and proceed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#00200FIt is okay.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('枫糖蛋糕', 0x0)"), scpexpr(EXPR_END)), "loc_2148")
    OP_63(0x18D, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x18D)

    ChrTalk(
        0x18D,
        (
            "#04403Fby the way……\x02\x03",
            "#04400FFrom a little while ago, Mr. Lloyd\x01",
            "I have a very fragrant smell.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_1BF2():
        TurnDirection(0xFE, 0x18D, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1BF2)
    Sleep(50)

    def lambda_1C02():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1C02)
    Sleep(50)

    def lambda_1C12():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1C12)
    Sleep(50)

    def lambda_1C22():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1C22)
    Sleep(50)

    def lambda_1C32():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1C32)
    Sleep(50)

    def lambda_1C42():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1C42)
    Sleep(300)

    ChrTalk(
        0x101,
        "#6P#00005FHuh……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00105FPerhaps,\x01",
            "I got a Ka'a-chan yesterday.\x01",
            "The smell of Maple muffin … Is that right?\x02\x03",
            "#00103FI can not eat them all\x01",
            "I was getting too caught … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00005FOh, that's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00202FIt's been a day.\x01",
            "It still smells nice,\x01",
            "It is truly bread made by Kia.\x02",
        )
    )

    CloseMessageWindow()
    Sound(906, 0, 100, 0)
    Sleep(300)

    def lambda_1D84():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1D84)
    Sleep(50)

    def lambda_1D94():
        TurnDirection(0xFE, 0x18D, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1D94)
    Sleep(50)

    def lambda_1DA4():
        TurnDirection(0xFE, 0x18D, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1DA4)
    Sleep(50)

    def lambda_1DB4():
        TurnDirection(0xFE, 0x18D, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1DB4)
    Sleep(50)

    def lambda_1DC4():
        TurnDirection(0xFE, 0x18D, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1DC4)
    Sleep(300)

    ChrTalk(
        0x101,
        "#6P#00011FWhat……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00105FThere, now ….\x02",
    )

    CloseMessageWindow()
    OP_63(0x18D, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x18D)

    ChrTalk(
        0x18D,
        (
            "#04403F……I'm sorry.\x01",
            "Actually, on Sunday school work back home\x01",
            "I did not say anything.\x02\x03",
            "#04401FThat muffin, if you do not mind\x01",
            "Will not you give me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00012FLet me see……\x01",
            "If it is okay with the remainder.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            "To lease",
            scpstr(SCPSTR_CODE_ITEM, '枫糖蛋糕'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    Sound(17, 0, 100, 0)
    CloseMessageWindow()
    FadeToBright(300, 0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    SubItemNumber('枫糖蛋糕', 1)

    ChrTalk(
        0x18D,
        (
            "#04403F(Munegu … …)\x02\x03",
            "#04405F…………delicious…………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00309FHello, Lease also\x01",
            "She seems to like it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18D,
        (
            "#04404F… what the heck,\x01",
            "I had a very happy taste.\x02\x03",
            "#04402FUm, what is it instead? …\x01",
            "Could you please accept this?\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '爆灵宝玉'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('爆灵宝玉', 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x18D,
        (
            "#04402FBefore I go to work here\x01",
            "It is a thing which was given from the direct superior.\x02\x03",
            "#04404FIf you do not mind, please use it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00002FThank you.\x02\x03",
            "#00000FAlright, then take corrective action\x01",
            "Let's go forward.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2148")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x157, 6)
    OP_29(0x7C, 0x1, 0x3)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x0, -13240, 8000, -130, 90)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    OP_E2(0x0)
    PlayEffect(0x2F, 0x0, 0xC, 0x41, 0, 0, 0, 0, 0, 0, 1250, 750, 1250, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2F, 0x1, 0xD, 0x41, 0, 0, 0, 0, 0, 0, 1250, 750, 1250, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2F, 0x2, 0xE, 0x41, 0, 0, 0, 0, 0, 0, 1250, 750, 1250, 0xFF, 0, 0, 0, 0)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_7_1186 end

    def Function_8_223E(): pass

    label("Function_8_223E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_225A")
    OP_A1(0xFE, 0x5DC, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Jump("Function_8_223E")

    label("loc_225A")

    Return()

    # Function_8_223E end

    def Function_9_225B(): pass

    label("Function_9_225B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2275")
    OP_A1(0xFE, 0x3E8, 0x4, 0x0, 0x1, 0x2, 0x3)
    Jump("Function_9_225B")

    label("loc_2275")

    Return()

    # Function_9_225B end

    def Function_10_2276(): pass

    label("Function_10_2276")

    BeginChrThread(0xFE, 1, 0, 8)
    OP_95(0xFE, -11220, 4010, 14610, 1000, 0x0)
    SetChrChipByIndex(0xFE, 0x14)
    SetChrSubChip(0xFE, 0x0)
    Sleep(2000)
    SetChrChipByIndex(0xFE, 0x15)
    SetChrSubChip(0xFE, 0x0)
    OP_95(0xFE, -14140, 4000, 17140, 1000, 0x0)
    Return()

    # Function_10_2276 end

    def Function_11_22B8(): pass

    label("Function_11_22B8")

    BeginChrThread(0xFE, 1, 0, 8)
    OP_95(0xFE, -13470, -4000, 17470, 1000, 0x0)
    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x16)
    SetChrSubChip(0xFE, 0x0)
    BeginChrThread(0xFE, 1, 0, 9)
    Sleep(2000)
    SetChrChipByIndex(0xFE, 0x17)
    SetChrSubChip(0xFE, 0x0)
    BeginChrThread(0xFE, 0, 0, 8)
    OP_95(0xFE, -12930, -4000, 13990, 1000, 0x0)
    Return()

    # Function_11_22B8 end

    def Function_12_230A(): pass

    label("Function_12_230A")

    BeginChrThread(0xFE, 0, 0, 8)
    OP_95(0xFE, -7490, -12000, 15970, 1000, 0x0)
    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x16)
    SetChrSubChip(0xFE, 0x0)
    BeginChrThread(0xFE, 1, 0, 9)
    Sleep(2000)
    SetChrChipByIndex(0xFE, 0x17)
    SetChrSubChip(0xFE, 0x0)
    BeginChrThread(0xFE, 0, 0, 8)
    OP_95(0xFE, -10820, -12000, 17090, 1000, 0x0)
    Return()

    # Function_12_230A end

    SaveToFile()

Try(main)
