﻿from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "m4220.bin",                # FileName
        "m4220",                    # MapName
        "m4220",                    # Location
        0x007F,                     # MapIndex
        "ed7573",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x29,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 127, 0, 2, 0, 3],
    )

    BuildStringList((
        "m4220",                  # 0
        "Noｱl",                  # 1
        "Wazy",                   # 2
        "Bracer Eolia",           # 3
        "Bracer Ling",            # 4
        "Mad Bloom",              # 5
        "bm4200",                 # 6
        "bm4200",                 # 7
        "bm4200",                 # 8
        "bm4200",                 # 9
    ))

    ATBonus("ATBonus_3A4", 100, 5, 1, 5, 1, 5, 1, 5, 5, 5, 5, 5, 5, 0, 0, 0)
    ATBonus("ATBonus_3B4", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    Sepith("Sepith_393C", 4,   2,   10,  4,   8,   2,   10)
    Sepith("Sepith_3934", 5,   2,   8,   8,   2,   8,   2)
    Sepith("Sepith_3924", 8,   8,   6,   6,   6,   8,   6)

    MonsterBattlePostion("MonsterBattlePostion_3D4", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_3D8", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_3DC", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_3E0", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_3E4", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_3E8", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_3EC", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_3F0", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_454", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_458", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_45C", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_460", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_464", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_468", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_46C", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_470", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_3F4", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_3F8", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_3FC", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_400", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_404", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_408", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_40C", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_410", 8, 14, 180)

    # monster count: 8

    BattleInfo(
        "BattleInfo_5AC", 0x0000, 71, 6, 60, 10, 1, 20, 0, "bm4200", "Sepith_393C", 40, 30, 20, 0,
        (
            ("ms86800.dat", "ms82700.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3D4", "MonsterBattlePostion_454", "ed7450", "ed7453", "ATBonus_3A4"),
            ("ms86800.dat", "ms82700.dat", "ms82700.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_3F4", "MonsterBattlePostion_454", "ed7450", "ed7453", "ATBonus_3A4"),
            ("ms86800.dat", "ms82700.dat", "ms82700.dat", "ms82700.dat", 0, 0, 0, 0, "MonsterBattlePostion_3D4", "MonsterBattlePostion_454", "ed7450", "ed7453", "ATBonus_3A4"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_510", 0x0000, 71, 6, 60, 10, 1, 30, 0, "bm4200", "Sepith_3934", 40, 30, 20, 0,
        (
            ("ms83300.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3F4", "MonsterBattlePostion_454", "ed7450", "ed7453", "ATBonus_3A4"),
            ("ms83300.dat", "ms83300.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3D4", "MonsterBattlePostion_454", "ed7450", "ed7453", "ATBonus_3A4"),
            ("ms83300.dat", "ms83300.dat", "ms83300.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_3F4", "MonsterBattlePostion_454", "ed7450", "ed7453", "ATBonus_3A4"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_474", 0x0000, 71, 6, 60, 10, 1, 40, 0, "bm4200", "Sepith_3924", 50, 25, 25, 0,
        (
            ("ms78200.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3F4", "MonsterBattlePostion_454", "ed7450", "ed7453", "ATBonus_3A4"),
            ("ms78200.dat", "ms78200.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3D4", "MonsterBattlePostion_454", "ed7450", "ed7453", "ATBonus_3A4"),
            ("ms78200.dat", "ms82700.dat", "ms82700.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_3F4", "MonsterBattlePostion_454", "ed7450", "ed7453", "ATBonus_3A4"),
            (),
        )
    )

    # event battle count: 1

    BattleInfo(
        "BattleInfo_648", 0x0C00, 255, 6, 0, 0, 3, 0, 0, "bm4200", 0x00000000, 100, 0, 0, 0,
        (
            ("ms86800.dat", "ms82700.dat", "ms86800.dat", "ms82700.dat", "ms86800.dat", "ms82700.dat", "ms86800.dat", "ms82700.dat", "MonsterBattlePostion_3D4", "MonsterBattlePostion_454", "ed7451", "ed7453", "ATBonus_3B4"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch02900.itc",                   # 00
        "chr/ch03000.itc",                   # 01
        "apl/ch51406.itc",                   # 02
        "apl/ch51407.itc",                   # 03
        "chr/ch32053.itc",                   # 04
        "apl/ch51447.itc",                   # 05
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
        "monster/ch78250.itc",               # 10
        "monster/ch78251.itc",               # 11
        "chr/ch00000.itc",                   # 12
        "chr/ch00000.itc",                   # 13
        "chr/ch00000.itc",                   # 14
        "chr/ch00000.itc",                   # 15
        "monster/ch83350.itc",               # 16
        "monster/ch83351.itc",               # 17
        "monster/ch86850.itc",               # 18
        "monster/ch86850.itc",               # 19
    ))

    DeclNpc(44360,   0,       4294960277, 270,  389,  0x0, 0,   0,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(44360,   0,       4294960277, 270,  389,  0x0, 0,   1,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(43279,   0,       4294961796, 180,  389,  0x0, 0,   2,   0,   255, 255, 0,   13,  255,  0)
    DeclNpc(42290,   0,       4294961726, 180,  389,  0x0, 0,   3,   0,   255, 255, 0,   14,  255,  0)
    DeclNpc(4294923796, 500,     4294939296, 0,    484,  0x0, 0,   24,  0,   0,   1,   255, 255, 255,  0)

    DeclMonster(4294966696, 4294949906, 0,       0x101002D,    "BattleInfo_5AC", 0,   24,  0xFFFF, 4,  5)
    DeclMonster(4294923066, 4294961176, 0,       0x1010087,    "BattleInfo_510", 0,   22,  0xFFFF, 2,  3)
    DeclMonster(4294933886, 8380,    0,       0x1010087,    "BattleInfo_510", 0,   22,  0xFFFF, 2,  3)
    DeclMonster(4294894126, 4294962376, 0,       0x1010046,    "BattleInfo_5AC", 0,   24,  0xFFFF, 4,  5)
    DeclMonster(4294916266, 4294934186, 0,       0x10100FE,    "BattleInfo_510", 0,   22,  0xFFFF, 2,  3)
    DeclMonster(4294885716, 4294935926, 0,       0x10100D2,    "BattleInfo_474", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(4294853576, 4294921566, 0,       0x1010062,    "BattleInfo_5AC", 0,   24,  0xFFFF, 4,  5)
    DeclMonster(4294843686, 4294960396, 0,       0x1010094,    "BattleInfo_474", 0,   16,  0xFFFF, 0,  1)

    DeclActor(4294961296, 0,       4294928296, 1200,    4294961296, 1000,    4294928296, 0x007C, 0,  5,  0x0000)
    DeclActor(4294934296, 0,       15000,   1200,    4294934296, 1000,    15000,   0x007C, 0,  6,  0x0000)
    DeclActor(4294923796, 0,       4294939296, 1200,    4294923796, 1000,    4294939296, 0x007C, 0,  7,  0x0000)
    DeclActor(4294923296, 0,       1000,    1200,    4294923296, 1000,    1000,    0x007C, 0,  8,  0x0000)
    DeclActor(4294889796, 0,       0,       1200,    4294889796, 1000,    0,       0x007C, 0,  9,  0x0000)
    DeclActor(4294834796, 0,       4294946796, 1200,    4294834796, 1000,    4294946796, 0x007C, 0,  10, 0x0000)
    DeclActor(4294837296, 0,       19000,   1200,    4294837296, 1000,    19000,   0x007C, 0,  15, 0x0000)

    ChipFrameInfo(800, 0, [0, 1, 2, 3, 4])                       # 0
    ChipFrameInfo(1000, 0, [0, 1, 2, 3])                         # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 2, 1])                   # 2
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4])                      # 3
    ChipFrameInfo(800, 0, [0, 1, 2, 3, 4, 5])                    # 4
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 5])                   # 5

    ScpFunction((
        "Function_0_734",          # 00, 0
        "Function_1_7E4",          # 01, 1
        "Function_2_801",          # 02, 2
        "Function_3_850",          # 03, 3
        "Function_4_FD8",          # 04, 4
        "Function_5_100D",         # 05, 5
        "Function_6_115E",         # 06, 6
        "Function_7_12AF",         # 07, 7
        "Function_8_14CA",         # 08, 8
        "Function_9_1633",         # 09, 9
        "Function_10_1784",        # 0A, 10
        "Function_11_18D5",        # 0B, 11
        "Function_12_1BB6",        # 0C, 12
        "Function_13_1E6A",        # 0D, 13
        "Function_14_1F9D",        # 0E, 14
        "Function_15_21BF",        # 0F, 15
        "Function_16_22B3",        # 10, 16
        "Function_17_22EE",        # 11, 17
        "Function_18_2326",        # 12, 18
        "Function_19_237C",        # 13, 19
        "Function_20_23D9",        # 14, 20
        "Function_21_2435",        # 15, 21
        "Function_22_248B",        # 16, 22
        "Function_23_38DF",        # 17, 23
    ))


    def Function_0_734(): pass

    label("Function_0_734")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_76C"),
        (1, "loc_778"),
        (2, "loc_784"),
        (3, "loc_790"),
        (4, "loc_79C"),
        (5, "loc_7A8"),
        (6, "loc_7B4"),
        (SWITCH_DEFAULT, "loc_7C0"),
    )


    label("loc_76C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_7CC")

    label("loc_778")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_7CC")

    label("loc_784")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_7CC")

    label("loc_790")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_7CC")

    label("loc_79C")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_7CC")

    label("loc_7A8")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_7CC")

    label("loc_7B4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_7CC")

    label("loc_7C0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_7CC")

    label("loc_7CC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7E3")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_7CC")

    label("loc_7E3")

    Return()

    # Function_0_734 end

    def Function_1_7E4(): pass

    label("Function_1_7E4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_800")
    OP_A1(0xFE, 0x320, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Jump("Function_1_7E4")

    label("loc_800")

    Return()

    # Function_1_7E4 end

    def Function_2_801(): pass

    label("Function_2_801")

    SetChrChipByIndex(0xA, 0x2)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    SetChrChipByIndex(0xB, 0x3)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_834")
    Event(0, 22)

    label("loc_834")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_84F")
    Call(0, 4)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)

    label("loc_84F")

    Return()

    # Function_2_801 end

    def Function_3_850(): pass

    label("Function_3_850")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_872")
    LoadEffect(0x9, "event/ev14011.eff")

    label("loc_872")

    OP_52(0x12, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F3, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F5A")
    OP_70(0x0, 0x0)
    Jump("loc_F5E")

    label("loc_F5A")

    OP_70(0x0, 0x1E)

    label("loc_F5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F3, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F71")
    OP_70(0x1, 0x0)
    Jump("loc_F75")

    label("loc_F71")

    OP_70(0x1, 0x1E)

    label("loc_F75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F88")
    OP_70(0x2, 0x0)
    Jump("loc_F8C")

    label("loc_F88")

    OP_70(0x2, 0x1E)

    label("loc_F8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F3, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F9F")
    OP_70(0x3, 0x0)
    Jump("loc_FA3")

    label("loc_F9F")

    OP_70(0x3, 0x1E)

    label("loc_FA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F3, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FB6")
    OP_70(0x4, 0x0)
    Jump("loc_FBA")

    label("loc_FB6")

    OP_70(0x4, 0x1E)

    label("loc_FBA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FCD")
    OP_70(0x5, 0x0)
    Jump("loc_FD1")

    label("loc_FCD")

    OP_70(0x5, 0x1E)

    label("loc_FD1")

    Sound(123, 1, 80, 0)
    Return()

    # Function_3_850 end

    def Function_4_FD8(): pass

    label("Function_4_FD8")

    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_LEQ), scpexpr(EXPR_END)), "loc_FF7")
    ClearChrFlags(0x8, 0x80)

    label("loc_FF7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_LEQ), scpexpr(EXPR_END)), "loc_100C")
    ClearChrFlags(0x9, 0x80)

    label("loc_100C")

    Return()

    # Function_4_FD8 end

    def Function_5_100D(): pass

    label("Function_5_100D")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F3, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1109")
    Sound(14, 0, 100, 0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0xA1, 1)"), scpexpr(EXPR_END)), "loc_1092")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0xA1),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1F3, 1)
    OP_E0(0x5, 0x0)
    Jump("loc_1104")

    label("loc_1092")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0xA1),
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
    OP_71(0x0, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1104")

    Jump("loc_1152")

    label("loc_1109")

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

    label("loc_1152")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_100D end

    def Function_6_115E(): pass

    label("Function_6_115E")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F3, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_125A")
    Sound(14, 0, 100, 0)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x5E8, 1)"), scpexpr(EXPR_END)), "loc_11E3")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x5E8),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1F3, 2)
    OP_E0(0x5, 0x0)
    Jump("loc_1255")

    label("loc_11E3")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x5E8),
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
    OP_71(0x1, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1255")

    Jump("loc_12A3")

    label("loc_125A")

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

    label("loc_12A3")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_115E end

    def Function_7_12AF(): pass

    label("Function_7_12AF")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1480")
    Sound(14, 0, 100, 0)
    OP_74(0x2, 0x1E)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x217, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13B2")
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0xC, 0x0, 0)
    OP_98(0xC, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_130C():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_130C)

    def lambda_1326():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_1326)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Monsters appeared!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    WaitChrThread(0xC, 1)
    Battle("BattleInfo_648", 0x0, 0x0, 0x0, 0xB, 0xFF)
    SetChrFlags(0xC, 0x80)
    ClearChrFlags(0xC, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_1393"),
        (2, "loc_13A2"),
        (1, "loc_13AF"),
        (SWITCH_DEFAULT, "loc_13B2"),
    )


    label("loc_1393")

    SetScenarioFlags(0x217, 4)
    OP_70(0x2, 0x1E)
    Sleep(500)
    Jump("loc_13B2")

    label("loc_13A2")

    OP_70(0x2, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_13AF")

    OP_B9(0x0)
    Return()

    label("loc_13B2")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x72, 1)"), scpexpr(EXPR_END)), "loc_140B")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x72),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1F3, 3)
    OP_E0(0x5, 0x0)
    Jump("loc_147B")

    label("loc_140B")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x72),
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
    OP_71(0x2, 0x1E, 0x0, 0x0, 0x0)

    label("loc_147B")

    Jump("loc_14BE")

    label("loc_1480")

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

    label("loc_14BE")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_12AF end

    def Function_8_14CA(): pass

    label("Function_8_14CA")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F3, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1603")
    Sound(14, 0, 100, 0)
    OP_74(0x3, 0x1E)
    OP_71(0x3, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    OP_70(0x3, 0x1E)
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
            "#56I Earth Sepith  x80\x01\x07\x02",
            "#57I Water Sepith  x80\x01\x07\x02",
            "#58I Fire Sepith   x80\x01\x07\x02",
            "#59I Wind Sepith   x80\x01\x07\x02",
            "#60I Time Sepith   x80\x01\x07\x02",
            "#61I Space Sepith  x80\x01\x07\x02",
            "#62I Mirage Sepith x80\x01\x07\x00",
            "obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x1F3, 4)
    OP_E0(0x5, 0x0)
    Jump("loc_1621")

    label("loc_1603")


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

    label("loc_1621")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_14CA end

    def Function_9_1633(): pass

    label("Function_9_1633")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F3, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_172F")
    Sound(14, 0, 100, 0)
    OP_74(0x4, 0x1E)
    OP_71(0x4, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1F6, 1)"), scpexpr(EXPR_END)), "loc_16B8")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1F6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1F3, 5)
    OP_E0(0x5, 0x0)
    Jump("loc_172A")

    label("loc_16B8")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1F6),
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
    OP_71(0x4, 0x1E, 0x0, 0x0, 0x0)

    label("loc_172A")

    Jump("loc_1778")

    label("loc_172F")

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

    label("loc_1778")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_9_1633 end

    def Function_10_1784(): pass

    label("Function_10_1784")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1880")
    Sound(14, 0, 100, 0)
    OP_74(0x5, 0x1E)
    OP_71(0x5, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1FD, 1)"), scpexpr(EXPR_END)), "loc_1809")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1FD),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1F3, 6)
    OP_E0(0x5, 0x0)
    Jump("loc_187B")

    label("loc_1809")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1FD),
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
    OP_71(0x5, 0x1E, 0x0, 0x0, 0x0)

    label("loc_187B")

    Jump("loc_18C9")

    label("loc_1880")

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

    label("loc_18C9")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_10_1784 end

    def Function_11_18D5(): pass

    label("Function_11_18D5")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_18E2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BB2")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",                 # 0
            "Switch Wazy Out\x01",      # 1
            "Cancel\x01",               # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19C4")

    ChrTalk(
        0x105,
        (
            "#10300FThen, take care of the\x01",
            "rest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#10100FYes, leave it to me!\x02",
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_32(0x4, 0xF9, 0x0)
    OP_32(0x8, 0xF9, 0x0)
    RemoveParty(0x4, 0xFF)
    ClearChrFlags(0x9, 0x80)
    RemoveParty(0x8, 0xFF)
    AddParty(0x8, 0xF4, 0xFF)
    OP_CF(0x1, 0xF4, 0x8)
    OP_37()
    Call(0, 4)
    FadeToBright(500, 0)
    OP_0D()
    Jump("loc_1BAD")

    label("loc_19C4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_19D8")
    Jump("loc_1BAD")

    label("loc_19D8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BAD")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B1B")

    ChrTalk(
        0x8,
        (
            "#10101FThe master known to have the alias of Steel\x01",
            "that Meister Jｶrg was talking about...\x01",
            "Looks like they're not your common foe.\x02\x03",
            "#10103F...I think Arios and the others will be\x01",
            "arriving soon.\x02\x03",
            "#10101FWe were able to recover the bracers, so\x01",
            "please don't do anything foolish.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1BAD")

    label("loc_1B1B")


    ChrTalk(
        0x8,
        (
            "#10103FI think Arios and the\x01",
            "others will be arriving\x01",
            "soon.\x02\x03",
            "#10101FWe were able to recover\x01",
            "the bracers, so please\x01",
            "don't do anything foolish.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BAD")

    Jump("loc_18E2")

    label("loc_1BB2")

    TalkEnd(0xFE)
    Return()

    # Function_11_18D5 end

    def Function_12_1BB6(): pass

    label("Function_12_1BB6")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1BC3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E66")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",                  # 0
            "Switch Noｱl Out\x01",      # 1
            "Cancel\x01",                # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CA4")

    ChrTalk(
        0x109,
        (
            "#10100FWazy, I leave the rest\x01",
            "to you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#10300FHehe, understood.\x02",
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_32(0x4, 0xF9, 0x0)
    OP_32(0x8, 0xF9, 0x0)
    RemoveParty(0x8, 0xFF)
    ClearChrFlags(0x8, 0x80)
    RemoveParty(0x4, 0xFF)
    AddParty(0x4, 0xF4, 0xFF)
    OP_CF(0x1, 0xF4, 0x4)
    OP_37()
    Call(0, 4)
    FadeToBright(500, 0)
    OP_0D()
    Jump("loc_1E61")

    label("loc_1CA4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1CB8")
    Jump("loc_1E61")

    label("loc_1CB8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E61")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DD3")

    ChrTalk(
        0x9,
        (
            "#10301FLike Meister Jｶrg said, it\x01",
            "appears Ouroboros is composed of\x01",
            "nothing but dangerous people.\x02\x03",
            "#10304FReturning to Crossbell City like\x01",
            "this would leave a bad\x01",
            "aftertaste...\x02\x03",
            "#10300FI'd like to at least confirm\x01",
            "what they're scheming.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1E61")

    label("loc_1DD3")


    ChrTalk(
        0x9,
        (
            "#10303FReturning to Crossbell\x01",
            "City like this would\x01",
            "leave a bad aftertaste...\x02\x03",
            "#10300FI'd like to at least\x01",
            "confirm what they're\x01",
            "scheming.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E61")

    Jump("loc_1BC3")

    label("loc_1E66")

    TalkEnd(0xFE)
    Return()

    # Function_12_1BB6 end

    def Function_13_1E6A(): pass

    label("Function_13_1E6A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F25")

    ChrTalk(
        0xFE,
        (
            "Phew... I'm glad Ling is\x01",
            "all right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Those Ouroboros guys\x01",
            "must not have been\x01",
            "serious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...However, what are\x01",
            "they trying to do in\x01",
            "such a place, I wonder?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1F99")

    label("loc_1F25")


    ChrTalk(
        0xFE,
        (
            "In any case, I'm happy\x01",
            "Ling is safe, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "These Ouroboros\x01",
            "people... I wonder what\x01",
            "they're trying to do?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F99")

    TalkEnd(0xFE)
    Return()

    # Function_13_1E6A end

    def Function_14_1F9D(): pass

    label("Function_14_1F9D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_210F")

    ChrTalk(
        0xFE,
        (
            "The Fool and those\x01",
            "knight girls were bad\x01",
            "news too, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The one with the creepy\x01",
            "mask was in a whole\x01",
            "other league.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Honestly, even if the legendary\x01",
            "assassin is with you, you might\x01",
            "have no chance...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#00700F...I will simply crush any\x01",
            "who stands in my way.\x02\x03",
            "If you have time for\x01",
            "unnecessary musings, focus\x01",
            "on healing your body.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_21BB")

    label("loc_210F")


    ChrTalk(
        0xFE,
        (
            "The one with the creepy\x01",
            "mask was in a whole\x01",
            "other league.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Honestly, even if the legendary\x01",
            "assassin is with you, you might have\x01",
            "no chance... Be extremely careful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21BB")

    TalkEnd(0xFE)
    Return()

    # Function_14_1F9D end

    def Function_15_21BF(): pass

    label("Function_15_21BF")

    OP_F4(0x2)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's an orbment charging station.\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Rest Here\x01",      # 0
            "Cancel\x01",         # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_22A4")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_74(0x6, 0x1E)
    Sound(7, 0, 100, 0)
    OP_70(0x6, 0x0)
    OP_71(0x6, 0x0, 0x1E, 0x0, 0x0)
    OP_79(0x6)
    OP_71(0x6, 0x1F, 0x186, 0x0, 0x20)
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
    OP_70(0x6, 0x0)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_22A4")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_15_21BF end

    def Function_16_22B3(): pass

    label("Function_16_22B3")

    OP_9B(0x0, 0xFE, 0x0, 0x2328, 0xFA0, 0x1)
    OP_9B(0x0, 0xFE, 0x159, 0x258, 0xFA0, 0x0)
    OP_93(0xFE, 0x0, 0x12C)
    Sleep(250)
    OP_9B(0x0, 0xFE, 0x0, 0x320, 0x7D0, 0x0)
    Sleep(100)
    Return()

    # Function_16_22B3 end

    def Function_17_22EE(): pass

    label("Function_17_22EE")

    OP_9B(0x0, 0xFE, 0x0, 0x2328, 0xFA0, 0x1)
    OP_9B(0x0, 0xFE, 0xF, 0x320, 0xFA0, 0x1)
    OP_9B(0x0, 0xFE, 0x159, 0x320, 0xFA0, 0x0)
    TurnDirection(0xFE, 0xB, 500)
    Sleep(400)
    Return()

    # Function_17_22EE end

    def Function_18_2326(): pass

    label("Function_18_2326")

    OP_9B(0x0, 0xFE, 0x0, 0x2328, 0xFA0, 0x1)
    Sleep(100)
    OP_9B(0x0, 0xFE, 0x159, 0x4B0, 0xFA0, 0x1)
    OP_9B(0x0, 0xFE, 0x1E, 0x7D0, 0xFA0, 0x1)
    OP_9B(0x0, 0xFE, 0xF, 0x4E2, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0xF, 0x4E2, 0x7D0, 0x0)
    TurnDirection(0xFE, 0xB, 500)
    Return()

    # Function_18_2326 end

    def Function_19_237C(): pass

    label("Function_19_237C")

    OP_9B(0x0, 0xFE, 0x0, 0x2328, 0xFA0, 0x1)
    OP_9B(0x0, 0xFE, 0xA, 0x5DC, 0xFA0, 0x1)
    OP_9B(0x0, 0xFE, 0x14, 0x7D0, 0xFA0, 0x1)
    OP_9B(0x0, 0xFE, 0x14A, 0xDAC, 0xFA0, 0x0)
    OP_93(0xFE, 0x13B, 0x1F4)
    TurnDirection(0xFE, 0xB, 500)
    Sleep(250)
    OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0x7D0, 0x0)
    Return()

    # Function_19_237C end

    def Function_20_23D9(): pass

    label("Function_20_23D9")

    OP_9B(0x0, 0xFE, 0x0, 0x2328, 0xFA0, 0x0)
    Sleep(100)
    OP_9B(0x0, 0xFE, 0x2D, 0x6D6, 0xFA0, 0x0)
    Sleep(50)
    OP_9B(0x0, 0xFE, 0x15E, 0x9C4, 0xFA0, 0x1)
    OP_9B(0x0, 0xFE, 0x154, 0x5DC, 0xFA0, 0x1)
    OP_9B(0x0, 0xFE, 0x159, 0x3E8, 0x7D0, 0x0)
    Sleep(250)
    TurnDirection(0xFE, 0xB, 500)
    Return()

    # Function_20_23D9 end

    def Function_21_2435(): pass

    label("Function_21_2435")

    OP_9B(0x0, 0xFE, 0x0, 0x2328, 0xFA0, 0x0)
    Sleep(250)
    OP_9B(0x0, 0xFE, 0xA, 0x41A, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x15E, 0x41A, 0x7D0, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(400)
    OP_93(0xFE, 0x13B, 0x1F4)
    OP_93(0xFE, 0x2D, 0x1F4)
    Sleep(400)
    TurnDirection(0xFE, 0xB, 500)
    Sleep(400)
    Return()

    # Function_21_2435 end

    def Function_22_248B(): pass

    label("Function_22_248B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch51448.itc", 0x1E)
    LoadEffect(0x2, "event/ev17017.eff")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_24C5")
    OP_CF(0x1, 0xF4, 0x8)

    label("loc_24C5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_24D9")
    OP_CF(0x1, 0xF4, 0x4)

    label("loc_24D9")

    OP_68(40820, 1000, -18740, 0)
    MoveCamera(36, 19, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(18000, 0)
    SetChrPos(0x101, 40750, 0, -21250, 0)
    SetChrPos(0x102, 42250, 0, -21250, 0)
    SetChrPos(0x103, 40150, 0, -22500, 0)
    SetChrPos(0x104, 42850, 0, -22500, 0)
    SetChrPos(0x106, 40750, 0, -23750, 0)
    SetChrPos(0xF4, 42250, 0, -23750, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0xB, 37500, 0, -6000, 180)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrChipByIndex(0xB, 0x4)
    SetChrSubChip(0xB, 0x3)
    ClearChrBattleFlags(0xA, 0x4)
    SetChrFlags(0xA, 0x80)
    PlayEffect(0x9, 0x7, 0xB, 0x5, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_68(40430, 1000, -16630, 1500)
    FadeToBright(1000, 0)

    def lambda_2604():
        OP_9B(0x0, 0x101, 0x154, 0xDAC, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2604)
    Sleep(30)

    def lambda_261C():
        OP_9B(0x0, 0x102, 0x154, 0xDAC, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_261C)
    Sleep(30)

    def lambda_2634():
        OP_9B(0x0, 0x103, 0x154, 0xDAC, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_2634)
    Sleep(30)

    def lambda_264C():
        OP_9B(0x0, 0x104, 0x154, 0xDAC, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_264C)
    Sleep(30)

    def lambda_2664():
        OP_9B(0x0, 0xF4, 0x154, 0xDAC, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_2664)
    Sleep(30)

    def lambda_267C():
        OP_9B(0x0, 0x106, 0x154, 0xDAC, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_267C)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0x106, 0)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#00013F#11P...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#00700F#12PFound her.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_68(37480, 1000, -6000, 3000)
    MoveCamera(45, 18, 0, 3000)
    OP_6E(650, 3000)
    SetCameraDistance(15500, 3000)
    BeginChrThread(0x101, 3, 0, 16)
    Sleep(50)
    BeginChrThread(0x102, 3, 0, 17)
    Sleep(50)
    BeginChrThread(0x103, 3, 0, 18)
    Sleep(50)
    BeginChrThread(0x104, 3, 0, 19)
    Sleep(50)
    BeginChrThread(0x106, 3, 0, 21)
    Sleep(50)
    BeginChrThread(0xF4, 3, 0, 20)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    WaitChrThread(0xF4, 3)
    WaitChrThread(0x106, 3)

    ChrTalk(
        0x101,
        (
            "#00010F#12PUgh... Ling, are you all\x01",
            "right!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00208F#6PIt appears her life is\x01",
            "not in danger, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#00700F#12PShe probably used up all\x01",
            "her energy and\x01",
            "collapsed.\x02\x03",
            "#00702FMove aside─ I'll try\x01",
            "resuscitating her.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    def lambda_28D7():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_28D7)
    Sleep(50)

    def lambda_28E7():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_28E7)
    Sleep(50)

    def lambda_28F7():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_28F7)
    Sleep(50)

    def lambda_2907():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_2907)
    Sleep(50)

    def lambda_2917():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_2917)
    Sleep(50)
    Sleep(300)

    ChrTalk(
        0x101,
        "#00011F#5PY-Yeah, please.\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 2)

    def lambda_294D():
        OP_96(0xFE, 0x8930, 0x0, 0xFFFFE4BC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_294D)
    Sleep(350)

    def lambda_296A():
        OP_9B(0x1, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_296A)
    Sleep(300)

    def lambda_2982():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2982)
    Sleep(50)

    def lambda_2992():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2992)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x106, 1)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x102, 2)
    Sleep(300)
    SetCameraDistance(14660, 2000)
    Sound(2580, 255, 100, 0)

    ChrTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11P#60W#10A#00700F......OOOOH......\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_6F(0x79)
    Sleep(500)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)
    Sound(253, 0, 60, 0)
    Sound(2590, 255, 100, 0)

    ChrTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11P#4S#00707F─REVIVE!#12A\x07\x00\x02",
        )
    )

    Sleep(300)
    PlayEffect(0x2, 0xFF, 0xB, 0x1, 0, 350, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    StopEffect(0x7, 0x2)
    Sound(833, 0, 30, 0)
    CancelBlur(500)
    CloseMessageWindow()

    def lambda_2A8D():
        TurnDirection(0xFE, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2A8D)
    Sleep(50)

    def lambda_2A9D():
        TurnDirection(0xFE, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_2A9D)
    Sleep(50)

    def lambda_2AAD():
        TurnDirection(0xFE, 0xB, 500)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_2AAD)
    Sleep(500)

    def lambda_2ABD():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_2ABD)
    WaitChrThread(0xB, 2)
    Sleep(500)

    ChrTalk(
        0xB,
        "#5P#50WUgh...\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_9B(0x0, 0x104, 0x159, 0x2BC, 0x7D0, 0x0)
    SetChrChipByIndex(0x104, 0x1E)
    SetChrSubChip(0x104, 0x0)
    SetChrFlags(0x104, 0x1000)
    SetChrFlags(0x104, 0x20)
    SetChrFlags(0x104, 0x2)
    SetChrChipByIndex(0xB, 0x5)
    SetChrSubChip(0xB, 0x0)
    SetChrFlags(0xB, 0x1000)
    SetChrFlags(0xB, 0x20)
    SetChrFlags(0xB, 0x2)
    SetChrPos(0xB, 37500, -70, -6000, 180)
    Sleep(300)
    SetCameraDistance(13500, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(14000, 2000)
    Sleep(1000)
    BeginChrThread(0xB, 0, 0, 23)
    Sleep(1000)

    def lambda_2B73():
        OP_9B(0x1, 0xFE, 0xF, 0xFFFFFE70, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_2B73)
    WaitChrThread(0x106, 1)

    ChrTalk(
        0xB,
        "#5P#30W...*cough*...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5P#30WI see... I collapsed,\x01",
            "just like that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#6PLing... It seems you\x01",
            "know what happened?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#5P#30WYeah... I'm ashamed...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5P#30W...That's right... Is\x01",
            "Eolia safe?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00104F#12PYes, no need to worry.\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd and the others\x01",
            "explained the events that\x01",
            "happened up until that point.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xB,
        (
            "#5P#30W...I see... I'm really\x01",
            "sorry...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5P#30WUgh... I still lack\x01",
            "training, huh...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5P#30WI'd never thought I'd be\x01",
            "treated like a child\x01",
            "like that...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2DD4")

    ChrTalk(
        0x109,
        (
            "#10101F#11PAre you talking about\x01",
            "those knight girls?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E0E")

    label("loc_2DD4")


    ChrTalk(
        0x105,
        (
            "#10301F#11PAre you talking about\x01",
            "those knight girls?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E0E")


    ChrTalk(
        0xB,
        (
            "#5P#30W...No... They were tough\x01",
            "too, but one of them was\x01",
            "special...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5P#30WI wouldn't call them\x01",
            "strong... It was more like\x01",
            "a whole other dimension.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5P#30WI don't even think Arios\x01",
            "would stand a chance...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x101,
        "#00007F#6PWha...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00307F#5PWhoa... Is something\x01",
            "like that even\x01",
            "possible!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#12PCould it be one of the\x01",
            "Anguis Jｶrg was talking\x01",
            "about?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00201F#6PA fearsome master\x01",
            "crowned with the name of\x01",
            "Steel, he said.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#5P#30W...It's probably them.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5P#30WAlso, I spotted a boy called\x01",
            ""Fool" and a middle-aged man\x01",
            "in a white robe....\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5P#30WEven if the legendary assassin's\x01",
            "with you... You might not even\x01",
            "stand a chance, you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008F#6PThat's....\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#00700F#12P............\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_68(37280, 1000, -6640, 1500)
    OP_96(0x106, 0x8D18, 0x0, 0xFFFFDFBC, 0x7D0, 0x1)
    OP_93(0x106, 0xE1, 0x190)

    def lambda_31C6():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_31C6)
    Sleep(50)

    def lambda_31D6():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_31D6)
    Sleep(50)

    def lambda_31E6():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_31E6)
    Sleep(50)

    def lambda_31F6():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_31F6)
    Sleep(50)

    def lambda_3206():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_3206)
    Sleep(250)

    ChrTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#00700F#5P─My name is Yin. No matter\x01",
            "the opponent, if needed, I\x01",
            "simply crush it.\x02\x03",
            "#00702FIf you all have lost your\x01",
            "nerve, then I'll end our\x01",
            "cooperation here.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00013F#5PW-Wait a moment!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00107F#11PEven if it's you, going\x01",
            "alone is reckless!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_336F")

    ChrTalk(
        0x109,
        (
            "#10101F#11PF-For now let's contact\x01",
            "Wazy and leave Ling with\x01",
            "him.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33B8")

    label("loc_336F")


    ChrTalk(
        0x105,
        (
            "#10306F#11PFor now let's contact\x01",
            "Noｱl and leave this lady\x01",
            "with her.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33B8")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_33F7")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 40670, 0, -5530, 180)
    ClearChrFlags(0x9, 0x80)
    OP_4B(0x9, 0xFF)
    Jump("loc_3416")

    label("loc_33F7")

    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 40670, 0, -5530, 180)
    ClearChrFlags(0x8, 0x80)
    OP_4B(0x8, 0xFF)

    label("loc_3416")

    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 43280, 0, -5500, 180)
    ClearChrFlags(0xA, 0x1000)
    ClearChrFlags(0xA, 0x20)
    ClearChrFlags(0xA, 0x2)
    SetChrChipByIndex(0xA, 0x2)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    SetChrSubChip(0xA, 0x2)
    SetChrPos(0xB, 42290, 0, -5570, 180)
    ClearChrFlags(0xB, 0x1000)
    ClearChrFlags(0xB, 0x20)
    ClearChrFlags(0xB, 0x2)
    SetChrChipByIndex(0xB, 0x3)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    SetChrSubChip(0xB, 0x2)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    ClearChrFlags(0x104, 0x1000)
    ClearChrFlags(0x104, 0x20)
    ClearChrFlags(0x104, 0x2)
    SetChrPos(0x101, 39800, 0, -7300, 0)
    SetChrPos(0x102, 41200, 0, -7300, 0)
    SetChrPos(0x103, 39500, 0, -8500, 0)
    SetChrPos(0x104, 41500, 0, -8500, 0)
    SetChrPos(0x106, 39800, 0, -9700, 0)
    SetChrPos(0xF4, 41200, 0, -9700, 0)
    OP_68(41100, 1200, -7240, 0)
    MoveCamera(60, 27, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(15620, 0)
    Sleep(500)
    SetCameraDistance(14620, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_35AD")

    ChrTalk(
        0x9,
        (
            "#10301F#5P...Will you be ok? They\x01",
            "look like quite the\x01",
            "dangerous opponents.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35FC")

    label("loc_35AD")


    ChrTalk(
        0x8,
        (
            "#10101F#5PW-Will you be all right?\x01",
            "They don't look like\x01",
            "your common foes.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35FC")


    ChrTalk(
        0x101,
        (
            "#00000F#12PYeah... Anyway, we'll\x01",
            "pay them a visit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#12PWell, let's take care\x01",
            "not to go up against\x01",
            "this Steel guy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108F#12P...Right...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#00700F#12P...Hmph.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5P#30WYeah, that would be\x01",
            "best...\x02\x03",
            "#5P#30W...You'll know him from\x01",
            "the bulky armor and long\x01",
            "mantle he wears...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11PArios and the others are\x01",
            "coming too, so don't do\x01",
            "anything rash, ok?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_377E():
        TurnDirection(0x101, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_377E)
    Sleep(50)

    def lambda_378E():
        TurnDirection(0x103, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_378E)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x103, 0)

    ChrTalk(
        0x101,
        "#00000F#6PYes, understood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00201F#6PRoger that.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3811")

    ChrTalk(
        0x109,
        "#10107F#12PThen, let's go!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3834")

    label("loc_3811")


    ChrTalk(
        0x105,
        "#10301F#12PThen, shall we go?\x02",
    )

    CloseMessageWindow()

    label("loc_3834")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3869")
    SetChrPos(0x9, 44360, 0, -7020, 270)
    OP_4C(0x9, 0xFF)
    Jump("loc_387E")

    label("loc_3869")

    SetChrPos(0x8, 44360, 0, -7020, 270)
    OP_4C(0x8, 0xFF)

    label("loc_387E")

    ClearChrFlags(0xB, 0x8000)
    SetChrPos(0x0, 38980, 0, -8290, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, 38980, 0, -8290, 270)
    OP_93(0xB, 0xB4, 0x0)
    OP_93(0xA, 0xB4, 0x0)
    SetChrSubChip(0xB, 0x0)
    SetChrSubChip(0xA, 0x0)
    SetScenarioFlags(0x165, 4)
    OP_29(0xA9, 0x1, 0x6)
    OP_37()
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_22_248B end

    def Function_23_38DF(): pass

    label("Function_23_38DF")

    SetChrSubChip(0xB, 0x0)
    Sleep(100)
    SetChrSubChip(0xB, 0x1)
    Sleep(100)
    SetChrSubChip(0xB, 0x0)
    Sleep(100)
    SetChrSubChip(0xB, 0x1)
    Sleep(100)
    Return()

    # Function_23_38DF end

    SaveToFile()

Try(main)
