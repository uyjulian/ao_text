﻿from ScenarioHelper import *

def main():
    CreateScenaFile(
        "r4060.bin",                # FileName
        "r4060",                    # MapName
        "r4060",                    # Location
        0x00A6,                     # MapIndex
        "ed7354",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x26,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, -14000, -4500, 26000, 0, 0, 1, 166, 0, 0, 0, 1],
    )

    BuildStringList((
        "r4060",                  # 0
        "br4010",                 # 1
        "br4010",                 # 2
        "br4010",                 # 3
        "br4010",                 # 4
        "br4010",                 # 5
    ))

    ATBonus("ATBonus_32C", 100, 5, 1, 5, 1, 5, 1, 5, 5, 5, 5, 5, 5, 0, 0, 0)
    ATBonus("ATBonus_33C", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    Sepith("Sepith_127D", 6,   0,   2,   15,  8,   4,   0)
    Sepith("Sepith_1295", 10,  6,   4,   10,  0,   0,   0)
    Sepith("Sepith_1285", 4,   10,  4,   6,   0,   9,   0)
    Sepith("Sepith_128D", 6,   3,   12,  3,   0,   0,   11)

    MonsterBattlePostion("MonsterBattlePostion_37C", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_380", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_384", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_388", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_38C", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_390", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_394", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_398", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_3DC", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_3E0", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_3E4", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_3E8", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_3EC", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_3F0", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_3F4", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_3F8", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_35C", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_360", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_364", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_368", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_36C", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_370", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_374", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_378", 2, 13, 180)

    # monster count: 9

    BattleInfo(
        "BattleInfo_3FC", 0x0000, 68, 6, 60, 8, 1, 40, 0, "br4010", "Sepith_127D", 40, 30, 20, 10,
        (
            ("ms78400.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_37C", "MonsterBattlePostion_3DC", "ed7450", "ed7453", "ATBonus_32C"),
            ("ms78400.dat", "ms78400.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_35C", "MonsterBattlePostion_3DC", "ed7450", "ed7453", "ATBonus_32C"),
            ("ms78400.dat", "ms78400.dat", "ms78400.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_37C", "MonsterBattlePostion_3DC", "ed7450", "ed7453", "ATBonus_32C"),
            ("ms78400.dat", "ms78400.dat", "ms78400.dat", "ms78400.dat", 0, 0, 0, 0, "MonsterBattlePostion_35C", "MonsterBattlePostion_3DC", "ed7450", "ed7453", "ATBonus_32C"),
        )
    )

    BattleInfo(
        "BattleInfo_654", 0x0000, 68, 6, 60, 8, 1, 30, 0, "br4010", "Sepith_1295", 50, 30, 20, 0,
        (
            ("ms86700.dat", "ms86700.dat", "ms86700.dat", "ms86700.dat", 0, 0, 0, 0, "MonsterBattlePostion_35C", "MonsterBattlePostion_3DC", "ed7450", "ed7453", "ATBonus_32C"),
            ("ms86700.dat", "ms86700.dat", "ms86700.dat", "ms86700.dat", "ms86700.dat", "ms86700.dat", 0, 0, "MonsterBattlePostion_35C", "MonsterBattlePostion_3DC", "ed7450", "ed7453", "ATBonus_32C"),
            ("ms86700.dat", "ms86700.dat", "ms86700.dat", "ms86700.dat", "ms86700.dat", "ms86700.dat", "ms86700.dat", "ms86700.dat", "MonsterBattlePostion_35C", "MonsterBattlePostion_3DC", "ed7450", "ed7453", "ATBonus_32C"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_4C4", 0x0000, 68, 6, 60, 8, 1, 20, 0, "br4010", "Sepith_1285", 40, 30, 20, 10,
        (
            ("ms82400.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_37C", "MonsterBattlePostion_3DC", "ed7450", "ed7453", "ATBonus_32C"),
            ("ms82400.dat", "ms82400.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_35C", "MonsterBattlePostion_3DC", "ed7450", "ed7453", "ATBonus_32C"),
            ("ms82400.dat", "ms82400.dat", "ms82400.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_37C", "MonsterBattlePostion_3DC", "ed7450", "ed7453", "ATBonus_32C"),
            ("ms82400.dat", "ms82400.dat", "ms82400.dat", "ms82400.dat", 0, 0, 0, 0, "MonsterBattlePostion_35C", "MonsterBattlePostion_3DC", "ed7450", "ed7453", "ATBonus_32C"),
        )
    )

    BattleInfo(
        "BattleInfo_58C", 0x0000, 68, 6, 60, 8, 1, 30, 0, "br4010", "Sepith_128D", 40, 30, 20, 10,
        (
            ("ms82800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_37C", "MonsterBattlePostion_3DC", "ed7450", "ed7453", "ATBonus_32C"),
            ("ms82800.dat", "ms82800.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_35C", "MonsterBattlePostion_3DC", "ed7450", "ed7453", "ATBonus_32C"),
            ("ms82800.dat", "ms82800.dat", "ms82800.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_37C", "MonsterBattlePostion_3DC", "ed7450", "ed7453", "ATBonus_32C"),
            ("ms82800.dat", "ms82800.dat", "ms82800.dat", "ms82800.dat", 0, 0, 0, 0, "MonsterBattlePostion_35C", "MonsterBattlePostion_3DC", "ed7450", "ed7453", "ATBonus_32C"),
        )
    )

    BattleInfo(
        "BattleInfo_6F0", 0x0C00, 255, 6, 0, 0, 0, 0, 0, "br4010", 0x00000000, 100, 0, 0, 0,
        (
            ("ms78001.dat", "ms78001.dat", "ms78001.dat", "ms78001.dat", "ms78001.dat", "ms78001.dat", 0, 0, "MonsterBattlePostion_35C", "MonsterBattlePostion_3DC", "ed7451", "ed7453", "ATBonus_33C"),
            (),
            (),
            (),
        )
    )

    # event battle count: 1

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
        "monster/ch78450.itc",               # 10
        "monster/ch78450.itc",               # 11
        "monster/ch82450.itc",               # 12
        "monster/ch82450.itc",               # 13
        "monster/ch82850.itc",               # 14
        "monster/ch82851.itc",               # 15
        "monster/ch78050.itc",               # 16
        "monster/ch78051.itc",               # 17
        "monster/ch86750.itc",               # 18
        "monster/ch86750.itc",               # 19
    ))

    DeclMonster(4294958966, 4294960426, 4294961296, 0x1010004,    "BattleInfo_3FC", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(3110,    4294929666, 0,       0x101005F,    "BattleInfo_654", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(11750,   4294934537, 0,       0x10100E6,    "BattleInfo_4C4", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(11240,   4294925556, 0,       0x1010140,    "BattleInfo_654", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(40260,   4294955016, 0,       0x101008C,    "BattleInfo_3FC", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(48650,   26130,   4294963296, 0x10100E6,    "BattleInfo_654", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(47050,   16440,   4294963296, 0x1010140,    "BattleInfo_58C", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(16270,   1390,    2000,    0x101008C,    "BattleInfo_3FC", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(53800,   4294923066, 4294962296, 0x1850113,    "BattleInfo_6F0", 0,   22,  0xFFFF, 6,  7)

    DeclEvent(0x0040, 0, 6,   53.79999923706055,     -44.22999954223633,    -5.0,                  16.0,                  [0.125,                -0.0,                  0.0,                   0.0,                   -0.0,                  0.125,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.25,                  0.0,                   -6.724999904632568,    5.528749942779541,     1.25,                  1.0])

    DeclActor(48740,   4294965546, 4294940626, 1200,    48740,   4294965546, 4294940626, 0x007C, 0,  2,  0x0000)
    DeclActor(31950,   4294961796, 4240,    1200,    31950,   4294961796, 4240,    0x007C, 0,  3,  0x0000)
    DeclActor(4294967206, 4294965296, 15210,   1200,    4294967206, 4294965296, 15210,   0x007C, 0,  4,  0x0000)
    DeclActor(4294927416, 4294963396, 4294954166, 1200,    4294927416, 4294964896, 4294954166, 0x007C, 0,  5,  0x0000)

    ChipFrameInfo(699, 0, [0, 1, 2, 3, 4])                       # 0
    ChipFrameInfo(1700, 0, [0, 1, 2, 3, 4])                      # 1
    ChipFrameInfo(699, 0, [0, 1, 2, 3, 4])                       # 2
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4])                      # 3
    ChipFrameInfo(699, 0, [0, 1, 2, 3, 4])                       # 4
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 5
    ChipFrameInfo(1000, 0, [0, 1, 2, 3])                         # 6
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 7
    ChipFrameInfo(699, 0, [0, 1, 2, 3, 4, 5])                    # 8
    ChipFrameInfo(1200, 0, [0, 1, 2, 3, 4, 5])                   # 9

    ScpFunction((
        "Function_0_7C8",          # 00, 0
        "Function_1_7C9",          # 01, 1
        "Function_2_ABC",          # 02, 2
        "Function_3_C23",          # 03, 3
        "Function_4_D74",          # 04, 4
        "Function_5_EC5",          # 05, 5
        "Function_6_FC1",          # 06, 6
    ))


    def Function_0_7C8(): pass

    label("Function_0_7C8")

    Return()

    # Function_0_7C8 end

    def Function_1_7C9(): pass

    label("Function_1_7C9")

    OP_50(0x51, (scpexpr(EXPR_PUSH_LONG, 0xFF2D100C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_7F9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7F4")
    ClearChrFlags(0x10, 0x80)
    ModifyEventFlags(1, 0, 0x80)
    SetChrFlags(0x10, 0x8000)

    label("loc_7F4")

    Jump("loc_803")

    label("loc_7F9")

    SetChrFlags(0x10, 0x80)
    ModifyEventFlags(0, 0, 0x80)

    label("loc_803")

    OP_52(0xA, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E4, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A89")
    OP_70(0x0, 0x0)
    Jump("loc_A8D")

    label("loc_A89")

    OP_70(0x0, 0x1E)

    label("loc_A8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E5, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AA0")
    OP_70(0x1, 0x0)
    Jump("loc_AA4")

    label("loc_AA0")

    OP_70(0x1, 0x1E)

    label("loc_AA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E5, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AB7")
    OP_70(0x2, 0x0)
    Jump("loc_ABB")

    label("loc_AB7")

    OP_70(0x2, 0x1E)

    label("loc_ABB")

    Return()

    # Function_1_7C9 end

    def Function_2_ABC(): pass

    label("Function_2_ABC")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E4, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BEC")
    Sound(14, 0, 100, 0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    OP_70(0x0, 0x1E)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddSepith(0x0, 80)
    AddSepith(0x1, 80)
    AddSepith(0x2, 80)
    AddSepith(0x3, 80)
    AddSepith(0x4, 80)
    AddSepith(0x5, 80)
    AddSepith(0x6, 80)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#56I地のセピス×８０\x01\x07\x02",
            "#57I水のセピス×８０\x01\x07\x02",
            "#58I火のセピス×８０\x01\x07\x02",
            "#59I風のセピス×８０\x01\x07\x02",
            "#60I時のセピス×８０\x01\x07\x02",
            "#61I空のセピス×８０\x01\x07\x02",
            "#62I幻のセピス×８０\x01\x07\x00",
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x1E4, 7)
    OP_E0(0x5, 0x0)
    Jump("loc_C11")

    label("loc_BEC")


    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱には何も入っていない。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_C11")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_ABC end

    def Function_3_C23(): pass

    label("Function_3_C23")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E5, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D23")
    Sound(14, 0, 100, 0)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('牛仔皮衣', 1)"), scpexpr(EXPR_END)), "loc_CAC")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '牛仔皮衣'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1E5, 0)
    OP_E0(0x5, 0x0)
    Jump("loc_D1E")

    label("loc_CAC")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, '牛仔皮衣'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, '牛仔皮衣'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x1, 0x1E, 0x0, 0x0, 0x0)

    label("loc_D1E")

    Jump("loc_D68")

    label("loc_D23")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱には何も入っていない。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_D68")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_C23 end

    def Function_4_D74(): pass

    label("Function_4_D74")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E5, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E74")
    Sound(14, 0, 100, 0)
    OP_74(0x2, 0x1E)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('大回复药', 1)"), scpexpr(EXPR_END)), "loc_DFD")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '大回复药'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1E5, 1)
    OP_E0(0x5, 0x0)
    Jump("loc_E6F")

    label("loc_DFD")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, '大回复药'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, '大回复药'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x2, 0x1E, 0x0, 0x0, 0x0)

    label("loc_E6F")

    Jump("loc_EB9")

    label("loc_E74")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱には何も入っていない。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_EB9")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_D74 end

    def Function_5_EC5(): pass

    label("Function_5_EC5")

    OP_F4(0x2)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "オーブメントを回復できる装置がある。\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "ここで休憩する\x01",      # 0
            "やめる\x01",              # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FB2")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_74(0x3, 0x1E)
    Sound(7, 0, 100, 0)
    OP_70(0x3, 0x0)
    OP_71(0x3, 0x0, 0x1E, 0x0, 0x0)
    OP_79(0x3)
    OP_71(0x3, 0x1F, 0x186, 0x0, 0x20)
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
    OP_70(0x3, 0x0)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_FB2")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_5_EC5 end

    def Function_6_FC1(): pass

    label("Function_6_FC1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_FCB")
    Return()

    label("loc_FCB")

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
            "大型の魔獣が徘徊#4Rはいかい#している。\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【退治する】\x01",      # 0
            "【やめる】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_10AD"),
        (SWITCH_DEFAULT, "loc_10C6"),
    )


    label("loc_10AD")

    Sleep(500)
    OP_E2(0x2)
    OP_90(0x0, 48970, -5000, -44010, 275)
    EventEnd(0x5)
    Return()

    label("loc_10C6")

    Battle("BattleInfo_6F0", 0x0, 0x0, 0x100, 0xC, 0xFF)
    OP_E2(0x2)
    EventBegin(0x1)
    OP_68(48970, -4000, -44010, 0)
    OP_90(0x0, 48970, -5000, -44010, 275)
    OP_90(0x1, 48970, -5000, -44010, 275)
    OP_90(0x2, 48970, -5000, -44010, 275)
    OP_90(0x3, 48970, -5000, -44010, 275)
    OP_90(0x4, 48970, -5000, -44010, 275)
    OP_90(0x5, 48970, -5000, -44010, 275)
    OP_90(0x6, 48970, -5000, -44010, 275)
    OP_90(0x7, 48970, -5000, -44010, 275)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (2, "loc_1188"),
        (1, "loc_118D"),
        (SWITCH_DEFAULT, "loc_1190"),
    )


    label("loc_1188")

    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    label("loc_118D")

    OP_B9(0x0)
    Return()

    label("loc_1190")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x10, 0x80)
    OP_E2(0x3)
    Sleep(400)
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "手配魔獣を退治した！\x02",
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
            scpstr(SCPSTR_CODE_ITEM, '银耀珠'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    AddItemNumber('银耀珠', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x21E, 0)
    OP_29(0x9C, 0x4, 0x2)
    OP_29(0x9C, 0x4, 0x10)
    OP_29(0x9C, 0x1, 0x0)
    OP_E2(0x2)
    ModifyEventFlags(0, 0, 0x80)
    EventEnd(0x5)
    Return()

    # Function_6_FC1 end

    SaveToFile()

Try(main)
