﻿from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "m4020.bin",                # FileName
        "m4020",                    # MapName
        "m4020",                    # Location
        0x007B,                     # MapIndex
        "ed7350",
        0x00000000,                 # Flags
        ("m4020", "r0000_1", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x27,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 123, 0, 1, 0, 2],
    )

    BuildStringList((
        "m4020",                  # 0
        "イベント用モンスター",   # 1
        "イベント用モンスター",   # 2
        "イベント用モンスター",   # 3
        "イベント用モンスター",   # 4
        "bm4010",                 # 5
        "bm4010",                 # 6
        "bm4010",                 # 7
        "bm4010",                 # 8
        "bm4010",                 # 9
    ))

    ATBonus("ATBonus_418", 100, 5, 1, 5, 1, 5, 1, 5, 5, 5, 5, 5, 5, 0, 0, 0)
    ATBonus("ATBonus_428", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    Sepith("Sepith_1D12", 0,   4,   0,   4,   1,   1,   1)
    Sepith("Sepith_1D1A", 2,   2,   0,   2,   2,   2,   1)
    Sepith("Sepith_1D0A", 3,   4,   5,   2,   0,   0,   0)
    Sepith("Sepith_1D22", 2,   2,   2,   2,   0,   1,   1)

    MonsterBattlePostion("MonsterBattlePostion_468", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_46C", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_470", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_474", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_478", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_47C", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_480", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_484", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_4C8", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_4CC", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_4D0", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_4D4", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_4D8", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_4DC", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_4E0", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_4E4", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_448", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_44C", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_450", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_454", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_458", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_45C", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_460", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_464", 2, 13, 180)

    # monster count: 15

    BattleInfo(
        "BattleInfo_52C", 0x0000, 46, 6, 45, 6, 1, 40, 0, "bm4010", "Sepith_1D12", 60, 25, 10, 0,
        (
            ("ms83600.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_468", "MonsterBattlePostion_4C8", "ed7450", "ed7453", "ATBonus_418"),
            ("ms83600.dat", "ms83600.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_448", "MonsterBattlePostion_4C8", "ed7450", "ed7453", "ATBonus_418"),
            ("ms83600.dat", "ms83600.dat", "ms83600.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_468", "MonsterBattlePostion_4C8", "ed7450", "ed7453", "ATBonus_418"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_5C8", 0x0000, 46, 6, 45, 6, 1, 40, 0, "bm4010", "Sepith_1D1A", 60, 25, 10, 0,
        (
            ("ms83800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_468", "MonsterBattlePostion_4C8", "ed7450", "ed7453", "ATBonus_418"),
            ("ms83800.dat", "ms83800.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_448", "MonsterBattlePostion_4C8", "ed7450", "ed7453", "ATBonus_418"),
            ("ms83800.dat", "ms83800.dat", "ms83800.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_468", "MonsterBattlePostion_4C8", "ed7450", "ed7453", "ATBonus_418"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_4E8", 0x0000, 46, 6, 45, 6, 1, 40, 0, "bm4010", "Sepith_1D0A", 100, 0, 0, 0,
        (
            ("ms86200.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_468", "MonsterBattlePostion_4C8", "ed7450", "ed7453", "ATBonus_418"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_664", 0x0000, 46, 6, 45, 6, 1, 40, 0, "bm4010", "Sepith_1D22", 60, 25, 10, 0,
        (
            ("ms84600.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_468", "MonsterBattlePostion_4C8", "ed7450", "ed7453", "ATBonus_418"),
            ("ms84600.dat", "ms84600.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_448", "MonsterBattlePostion_4C8", "ed7450", "ed7453", "ATBonus_418"),
            ("ms84600.dat", "ms84600.dat", "ms84600.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_468", "MonsterBattlePostion_4C8", "ed7450", "ed7453", "ATBonus_418"),
            (),
        )
    )

    # event battle count: 1

    BattleInfo(
        "BattleInfo_700", 0x0002, 45, 6, 45, 3, 3, 30, 0, "bm4010", 0x00000000, 100, 0, 0, 0,
        (
            ("ms86200.dat", "ms86200.dat", "ms86200.dat", "ms86200.dat", 0, 0, 0, 0, "MonsterBattlePostion_448", "MonsterBattlePostion_4C8", "ed7452", "ed7453", "ATBonus_428"),
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
        "monster/ch86250.itc",               # 10
        "monster/ch86251.itc",               # 11
        "monster/ch83650.itc",               # 12
        "monster/ch83650.itc",               # 13
        "monster/ch83850.itc",               # 14
        "monster/ch83851.itc",               # 15
        "monster/ch84650.itc",               # 16
        "monster/ch84651.itc",               # 17
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(4294966586, 7680,    0,       0x10100B9,    "BattleInfo_52C", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(26610,   19630,   2000,    0x10100E6,    "BattleInfo_52C", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(33050,   33880,   1990,    0x10100B9,    "BattleInfo_5C8", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(207270,  47320,   2000,    0x1010113,    "BattleInfo_4E8", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(4294938656, 15950,   0,       0x101008C,    "BattleInfo_4E8", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(4294791186, 27680,   0,       0x101005F,    "BattleInfo_664", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(0,       216920,  4294962296, 0x10100E6,    "BattleInfo_4E8", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(2510,    222060,  4294962296, 0x101005F,    "BattleInfo_664", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(4294963696, 223190,  4294962296, 0x101008C,    "BattleInfo_664", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(2560,    227710,  4294962296, 0x10100B9,    "BattleInfo_664", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(4294966666, 251340,  4294962716, 0x101008C,    "BattleInfo_4E8", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(4294962846, 299250,  0,       0x1010032,    "BattleInfo_5C8", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(4294961986, 323910,  2380,    0x1010113,    "BattleInfo_5C8", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(4294814576, 248360,  2500,    0x101005F,    "BattleInfo_664", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(153850,  249300,  4294963796, 0x1010032,    "BattleInfo_664", 0,   22,  0xFFFF, 6,  7)

    DeclActor(210280,  2000,    43410,   1200,    210280,  3000,    43410,   0x007C, 0,  3,  0x0000)
    DeclActor(148030,  4294963796, 250310,  1200,    148030,  4294964796, 250310,  0x007C, 0,  4,  0x0000)
    DeclActor(4294805296, 2500,    254210,  1200,    4294805296, 3500,    254210,  0x007C, 0,  5,  0x0000)
    DeclActor(4294780276, 0,       39200,   1200,    4294780276, 1000,    39200,   0x007C, 0,  6,  0x0000)
    DeclActor(13350,   0,       388570,  1200,    13350,   1500,    388570,  0x007C, 0,  8,  0x0000)

    ChipFrameInfo(699, 0, [0, 1, 2, 3, 4, 3, 2, 1])              # 0
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 1
    ChipFrameInfo(699, 0, [0, 1, 2, 3, 4, 5, 6])                 # 2
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5, 6])                # 3
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 4
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4])                      # 5
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 6
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4])                      # 7

    ScpFunction((
        "Function_0_7D4",          # 00, 0
        "Function_1_7F0",          # 01, 1
        "Function_2_802",          # 02, 2
        "Function_3_BDF",          # 03, 3
        "Function_4_D31",          # 04, 4
        "Function_5_E83",          # 05, 5
        "Function_6_FD5",          # 06, 6
        "Function_7_112F",         # 07, 7
        "Function_8_1133",         # 08, 8
        "Function_9_1229",         # 09, 9
        "Function_10_16B0",        # 0A, 10
        "Function_11_1709",        # 0B, 11
    ))


    def Function_0_7D4(): pass

    label("Function_0_7D4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7EF")
    OP_A1(0xFE, 0x5DC, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_0_7D4")

    label("loc_7EF")

    Return()

    # Function_0_7D4 end

    def Function_1_7F0(): pass

    label("Function_1_7F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x120, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x120, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_801")
    Event(0, 9)

    label("loc_801")

    Return()

    # Function_1_7F0 end

    def Function_2_802(): pass

    label("Function_2_802")

    OP_52(0xF, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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
    OP_52(0x16, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B59")
    OP_70(0x0, 0x0)
    Jump("loc_B5D")

    label("loc_B59")

    OP_70(0x0, 0x1E)

    label("loc_B5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B70")
    OP_70(0x1, 0x0)
    Jump("loc_B74")

    label("loc_B70")

    OP_70(0x1, 0x1E)

    label("loc_B74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B87")
    OP_70(0x2, 0x0)
    Jump("loc_B8B")

    label("loc_B87")

    OP_70(0x2, 0x1E)

    label("loc_B8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B9E")
    OP_70(0x3, 0x0)
    Jump("loc_BA2")

    label("loc_B9E")

    OP_70(0x3, 0x1E)

    label("loc_BA2")

    Sound(129, 1, 100, 0)
    OP_1C(0x0, 0x4, 0x0, 0x32, 0x0, 0x7, 0x0, 0x0)
    OP_1C(0x0, 0x5, 0x0, 0x32, 0x0, 0x7, 0x0, 0x0)
    OP_1C(0x0, 0x6, 0x0, 0x32, 0x0, 0x7, 0x0, 0x0)
    LoadEffect(0x10, "event\\eva00_00.eff")
    Return()

    # Function_2_802 end

    def Function_3_BDF(): pass

    label("Function_3_BDF")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CDB")
    Sound(14, 0, 100, 0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1F8, 1)"), scpexpr(EXPR_END)), "loc_C64")
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
    SetScenarioFlags(0x1E0, 5)
    OP_E0(0x5, 0x0)
    Jump("loc_CD6")

    label("loc_C64")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1F8),
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

    label("loc_CD6")

    Jump("loc_D25")

    label("loc_CDB")

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

    label("loc_D25")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_BDF end

    def Function_4_D31(): pass

    label("Function_4_D31")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E2D")
    Sound(14, 0, 100, 0)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x4B, 1)"), scpexpr(EXPR_END)), "loc_DB6")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x4B),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1E0, 6)
    OP_E0(0x5, 0x0)
    Jump("loc_E28")

    label("loc_DB6")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x4B),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " is inside the chest.\x01",
            "Since you have too many, you gave it up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x1, 0x1E, 0x0, 0x0, 0x0)

    label("loc_E28")

    Jump("loc_E77")

    label("loc_E2D")

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

    label("loc_E77")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_D31 end

    def Function_5_E83(): pass

    label("Function_5_E83")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F7F")
    Sound(14, 0, 100, 0)
    OP_74(0x2, 0x1E)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1A7, 1)"), scpexpr(EXPR_END)), "loc_F08")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1A7),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1E0, 7)
    OP_E0(0x5, 0x0)
    Jump("loc_F7A")

    label("loc_F08")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1A7),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " is inside the chest.\x01",
            "Since you have too many, you gave it up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x2, 0x1E, 0x0, 0x0, 0x0)

    label("loc_F7A")

    Jump("loc_FC9")

    label("loc_F7F")

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

    label("loc_FC9")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_E83 end

    def Function_6_FD5(): pass

    label("Function_6_FD5")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10FF")
    Sound(14, 0, 100, 0)
    OP_74(0x3, 0x1E)
    OP_71(0x3, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    OP_70(0x3, 0x1E)
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
            "#56IEarth Sepith x30\x01\x07\x02",
            "#57IWater Sepith x30\x01\x07\x02",
            "#58IFire Sepith x30\x01\x07\x02",
            "#59IWind Sepith x30\x01\x07\x02",
            "#60ITime Sepith x30\x01\x07\x02",
            "#61ISpace Sepith x30\x01\x07\x02",
            "#62IMirage Sepith x30\x01\x07\x00",
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x1E1, 0)
    OP_E0(0x5, 0x0)
    Jump("loc_111D")

    label("loc_10FF")


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

    label("loc_111D")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_FD5 end

    def Function_7_112F(): pass

    label("Function_7_112F")

    Call(1, 6)
    Return()

    # Function_7_112F end

    def Function_8_1133(): pass

    label("Function_8_1133")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_121A")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_74(0x7, 0x1E)
    Sound(7, 0, 100, 0)
    OP_70(0x7, 0x0)
    OP_71(0x7, 0x0, 0x1E, 0x0, 0x0)
    OP_79(0x7)
    OP_71(0x7, 0x1F, 0x186, 0x0, 0x20)
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
    OP_70(0x7, 0x0)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_121A")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_8_1133 end

    def Function_9_1229(): pass

    label("Function_9_1229")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    LoadChrToIndex("monster/ch86251.itc", 0x1E)
    LoadChrToIndex("monster/ch86252.itc", 0x1F)
    LoadChrToIndex("chr/ch00050.itc", 0x20)
    LoadChrToIndex("chr/ch02950.itc", 0x21)
    LoadChrToIndex("chr/ch00950.itc", 0x22)
    LoadChrToIndex("chr/ch02450.itc", 0x23)
    SetChrPos(0x101, 500, 0, -10000, 0)
    SetChrPos(0x109, 500, 0, -11700, 0)
    SetChrPos(0x108, -1000, 0, -10500, 0)
    SetChrPos(0x10A, 2000, 0, -11000, 0)
    SetChrFlags(0x8, 0x20)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrPos(0x8, -900, 300, 3000, 180)
    OP_A7(0x8, 0x0, 0x0, 0x0, 0x0, 0x0)
    BeginChrThread(0x8, 0, 0, 0)
    OP_52(0x8, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x9, 0x20)
    SetChrChipByIndex(0x9, 0x1E)
    SetChrPos(0x9, 2200, 300, 3000, 180)
    OP_A7(0x9, 0x0, 0x0, 0x0, 0x0, 0x0)
    BeginChrThread(0x9, 0, 0, 0)
    OP_52(0x9, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xA, 0x20)
    SetChrChipByIndex(0xA, 0x1E)
    SetChrPos(0xA, -3600, 300, 2000, 180)
    OP_A7(0xA, 0x0, 0x0, 0x0, 0x0, 0x0)
    BeginChrThread(0xA, 0, 0, 0)
    OP_52(0xA, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xB, 0x20)
    SetChrChipByIndex(0xB, 0x1E)
    SetChrPos(0xB, 5400, 300, 1200, 180)
    OP_A7(0xB, 0x0, 0x0, 0x0, 0x0, 0x0)
    BeginChrThread(0xB, 0, 0, 0)
    OP_52(0xB, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(1000, 1000, -6800, 0)
    MoveCamera(320, 21, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(21500, 0)
    OP_68(1000, 1000, -1800, 3000)
    SetCameraDistance(19500, 3000)

    def lambda_141C():
        OP_97(0x101, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_141C)
    Sleep(50)

    def lambda_1439():
        OP_97(0x109, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1439)
    Sleep(50)

    def lambda_1456():
        OP_97(0x108, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 0, lambda_1456)
    Sleep(50)

    def lambda_1473():
        OP_97(0x10A, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_1473)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 0)
    ClearChrFlags(0x8, 0x80)

    def lambda_14A0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_14A0)

    def lambda_14B1():
        OP_96(0xFE, 0xFFFFFDA8, 0x0, 0x3E8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_14B1)
    Sleep(100)
    ClearChrFlags(0x9, 0x80)

    def lambda_14D3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_14D3)

    def lambda_14E4():
        OP_96(0xFE, 0x76C, 0x0, 0x3E8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_14E4)
    Sleep(100)
    ClearChrFlags(0xA, 0x80)

    def lambda_1506():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1506)

    def lambda_1517():
        OP_96(0xFE, 0xFFFFF448, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1517)
    Sleep(100)
    ClearChrFlags(0xB, 0x80)

    def lambda_1539():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_1539)

    def lambda_154A():
        OP_96(0xFE, 0x12C0, 0x0, 0xFFFFFCE0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_154A)
    OP_63(0x108, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Fade(250)
    SetChrChipByIndex(0x101, 0x20)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x109, 0x21)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x10A, 0x22)
    SetChrSubChip(0x10A, 0x0)
    SetChrChipByIndex(0x108, 0x23)
    SetChrSubChip(0x108, 0x0)
    Sound(531, 0, 100, 0)
    Sound(932, 0, 100, 0)
    Sound(540, 0, 30, 0)
    Sound(805, 0, 100, 0)
    OP_0D()
    Sound(830, 0, 100, 0)
    BeginChrThread(0x8, 3, 0, 10)
    Sleep(50)
    BeginChrThread(0x9, 3, 0, 10)
    Sleep(50)
    BeginChrThread(0xA, 3, 0, 10)
    Sleep(50)
    BeginChrThread(0xB, 3, 0, 10)
    Sleep(1000)
    SetChrSubChip(0x8, 0x1)
    SetChrSubChip(0x9, 0x1)
    SetChrSubChip(0xA, 0x1)
    SetChrSubChip(0xB, 0x1)
    BlurSwitch(0x12C, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetCameraDistance(17500, 300)
    Sleep(100)
    SetChrSubChip(0x8, 0x0)
    SetChrSubChip(0x9, 0x0)
    SetChrSubChip(0xA, 0x0)
    SetChrSubChip(0xB, 0x0)
    Sleep(200)
    EndChrThread(0x8, 0xFF)
    EndChrThread(0x9, 0xFF)
    EndChrThread(0xA, 0xFF)
    EndChrThread(0xB, 0xFF)
    Battle("BattleInfo_700", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    Call(0, 11)
    Return()

    # Function_9_1229 end

    def Function_10_16B0(): pass

    label("Function_10_16B0")

    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrSubChip(0xFE, 0x0)
    Sleep(100)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)

    def lambda_16F0():
        OP_A6(0xFE, 0x32, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_16F0)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_10_16B0 end

    def Function_11_1709(): pass

    label("Function_11_1709")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch02950.itc", 0x1F)
    LoadChrToIndex("chr/ch00950.itc", 0x20)
    LoadChrToIndex("chr/ch02450.itc", 0x21)
    OP_68(500, 1000, -4000, 0)
    MoveCamera(320, 21, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18000, 0)
    SetChrPos(0x101, -500, 0, -6300, 0)
    SetChrPos(0x109, 900, 0, -6700, 0)
    SetChrPos(0x108, -1000, 0, -3900, 0)
    SetChrPos(0x10A, 2000, 0, -5200, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x109, 0x1F)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x10A, 0x20)
    SetChrSubChip(0x10A, 0x0)
    SetChrChipByIndex(0x108, 0x21)
    SetChrSubChip(0x108, 0x0)
    SetCameraDistance(17000, 1500)
    FadeToBright(1000, 0)
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
    Sound(531, 0, 100, 0)
    Sound(932, 0, 100, 0)
    Sound(540, 0, 30, 0)
    Sound(805, 0, 100, 0)
    OP_0D()
    OP_96(0x10A, 0x7D0, 0x0, 0xFFFFEFFC, 0x5DC, 0x0)
    Sleep(300)
    OP_6F(0x79)

    ChrTalk(
        0x10A,
        "#00603F#5PHmph. That should do it.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x10A, 0x108, 500)
    Sleep(300)

    ChrTalk(
        0x10A,
        (
            "#12P#00600F──MacLaine.\x01",
            "Were the monsters six years ago\x01",
            "all small fries like these ones?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x108, 0x10A, 500)
    Sleep(100)

    ChrTalk(
        0x108,
        (
            "#01403F#5PNo. The swarms of monsters we ran into were\x01",
            "far more brutal than what we're seeing today.\x02\x03",
            "#01408FAnd apart from just monsters, \x01",
            "we also had to deal with a number of\x01",
            "mad cultists who fearlessly fought back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        "#12P#00606FHmph. Hearing that is enough to irritate me.\x02",
    )

    CloseMessageWindow()
    OP_68(500, 1100, -5000, 1200)
    MoveCamera(320, 19, 0, 1200)
    SetCameraDistance(16500, 1200)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#6P#00006F(....I expected no less of these two.)\x02\x03",
            "#00008F(I have to admit that I thought these\x01",
            "monsters put up quite the challenge.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10106F(Yeah. They're on a whole different level.)\x02\x03",
            "#10101F(It motivates me to work hard, too...!)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x10A, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x108, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_1B2C():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_1B2C)
    Sleep(50)
    TurnDirection(0x108, 0x101, 500)

    ChrTalk(
        0x10A,
        "#11P#00605FHey, is anything the matter?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        "#5P#01405FAre you injured from the battle?\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x109, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x101)
    OP_64(0x109)

    ChrTalk(
        0x101,
        "#6P#00012FNo. I'm fine..\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10112FNo scratches to be found!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        "#11P#00600FGood. Then let's move.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#01403F#5PThere should be a midway\x01",
            "intersection just beyond here.\x02\x03",
            "#01402FLet's make that our first goal.\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(16750, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    OP_37()
    SetChrPos(0x0, 500, 0, -5000, 0)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x120, 5)
    OP_E2(0x2)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_11_1709 end

    SaveToFile()

Try(main)
