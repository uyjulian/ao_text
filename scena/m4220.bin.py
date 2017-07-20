from ScenarioHelper import *

def main():
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
        "Noel",                 # 1
        "Waji",                   # 2
        "Friend Aolia",         # 3
        "Zookoist Rin",             # 4
        "Mad Bloom",         # 5
        "bm4200",                 # 6
        "bm4200",                 # 7
        "bm4200",                 # 8
        "bm4200",                 # 9
    ))

    ATBonus("ATBonus_3A4", 100, 5, 1, 5, 1, 5, 1, 5, 5, 5, 5, 5, 5, 0, 0, 0)
    ATBonus("ATBonus_3B4", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    Sepith("Sepith_383A", 4,   2,   10,  4,   8,   2,   10)
    Sepith("Sepith_3832", 5,   2,   8,   8,   2,   8,   2)
    Sepith("Sepith_3822", 8,   8,   6,   6,   6,   8,   6)

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
        "BattleInfo_5AC", 0x0000, 71, 6, 60, 10, 1, 20, 0, "bm4200", "Sepith_383A", 40, 30, 20, 0,
        (
            ("ms86800.dat", "ms82700.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3D4", "MonsterBattlePostion_454", "ed7450", "ed7453", "ATBonus_3A4"),
            ("ms86800.dat", "ms82700.dat", "ms82700.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_3F4", "MonsterBattlePostion_454", "ed7450", "ed7453", "ATBonus_3A4"),
            ("ms86800.dat", "ms82700.dat", "ms82700.dat", "ms82700.dat", 0, 0, 0, 0, "MonsterBattlePostion_3D4", "MonsterBattlePostion_454", "ed7450", "ed7453", "ATBonus_3A4"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_510", 0x0000, 71, 6, 60, 10, 1, 30, 0, "bm4200", "Sepith_3832", 40, 30, 20, 0,
        (
            ("ms83300.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3F4", "MonsterBattlePostion_454", "ed7450", "ed7453", "ATBonus_3A4"),
            ("ms83300.dat", "ms83300.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3D4", "MonsterBattlePostion_454", "ed7450", "ed7453", "ATBonus_3A4"),
            ("ms83300.dat", "ms83300.dat", "ms83300.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_3F4", "MonsterBattlePostion_454", "ed7450", "ed7453", "ATBonus_3A4"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_474", 0x0000, 71, 6, 60, 10, 1, 40, 0, "bm4200", "Sepith_3822", 50, 25, 25, 0,
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
        "Function_8_14C6",         # 08, 8
        "Function_9_162D",         # 09, 9
        "Function_10_177E",        # 0A, 10
        "Function_11_18CF",        # 0B, 11
        "Function_12_1B92",        # 0C, 12
        "Function_13_1E2B",        # 0D, 13
        "Function_14_1F51",        # 0E, 14
        "Function_15_2106",        # 0F, 15
        "Function_16_2202",        # 10, 16
        "Function_17_223D",        # 11, 17
        "Function_18_2275",        # 12, 18
        "Function_19_22CB",        # 13, 19
        "Function_20_2328",        # 14, 20
        "Function_21_2384",        # 15, 21
        "Function_22_23DA",        # 16, 22
        "Function_23_37DD",        # 17, 23
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F3, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_110D")
    Sound(14, 0, 100, 0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('破言之牙', 1)"), scpexpr(EXPR_END)), "loc_1096")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '破言之牙'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1F3, 1)
    OP_E0(0x5, 0x0)
    Jump("loc_1108")

    label("loc_1096")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            "In the treasure box",
            scpstr(SCPSTR_CODE_ITEM, '破言之牙'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Is contained.\x01",
            "Because my belongings are full,",
            scpstr(SCPSTR_CODE_ITEM, '破言之牙'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I gave up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x0, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1108")

    Jump("loc_1152")

    label("loc_110D")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F3, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_125E")
    Sound(14, 0, 100, 0)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('祭司法衣', 1)"), scpexpr(EXPR_END)), "loc_11E7")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '祭司法衣'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1F3, 2)
    OP_E0(0x5, 0x0)
    Jump("loc_1259")

    label("loc_11E7")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            "In the treasure box",
            scpstr(SCPSTR_CODE_ITEM, '祭司法衣'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Is contained.\x01",
            "Because my belongings are full,",
            scpstr(SCPSTR_CODE_ITEM, '祭司法衣'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I gave up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x1, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1259")

    Jump("loc_12A3")

    label("loc_125E")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x217, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13AE")
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
            "A monster appeared!\x07\x00\x02",
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
        (0, "loc_138F"),
        (2, "loc_139E"),
        (1, "loc_13AB"),
        (SWITCH_DEFAULT, "loc_13AE"),
    )


    label("loc_138F")

    SetScenarioFlags(0x217, 4)
    OP_70(0x2, 0x1E)
    Sleep(500)
    Jump("loc_13AE")

    label("loc_139E")

    OP_70(0x2, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_13AB")

    OP_B9(0x0)
    Return()

    label("loc_13AE")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('防御３', 1)"), scpexpr(EXPR_END)), "loc_140B")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '防御３'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
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
            "In the treasure box",
            scpstr(SCPSTR_CODE_ITEM, '防御３'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Is contained.\x01",
            "Because my belongings are full,",
            scpstr(SCPSTR_CODE_ITEM, '防御３'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I gave up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x2, 0x1E, 0x0, 0x0, 0x0)

    label("loc_147B")

    Jump("loc_14BA")

    label("loc_1480")

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

    label("loc_14BA")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_12AF end

    def Function_8_14C6(): pass

    label("Function_8_14C6")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F3, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15F6")
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
            "#56ISepis of the Earth × 80\x01\x07\x02",
            "#57IWater sepis × 80\x01\x07\x02",
            "#58IFire sepis × 80\x01\x07\x02",
            "#59IWind sepice × 80\x01\x07\x02",
            "#60ITime sepis × 80\x01\x07\x02",
            "#61IEmpty Sepis × 80\x01\x07\x02",
            "#62IThe phantom sepis × 80\x01\x07\x00",
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x1F3, 4)
    OP_E0(0x5, 0x0)
    Jump("loc_161B")

    label("loc_15F6")


    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is nothing in the treasure box.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_161B")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_14C6 end

    def Function_9_162D(): pass

    label("Function_9_162D")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F3, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_172D")
    Sound(14, 0, 100, 0)
    OP_74(0x4, 0x1E)
    OP_71(0x4, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('大回复药', 1)"), scpexpr(EXPR_END)), "loc_16B6")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '大回复药'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1F3, 5)
    OP_E0(0x5, 0x0)
    Jump("loc_1728")

    label("loc_16B6")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            "In the treasure box",
            scpstr(SCPSTR_CODE_ITEM, '大回复药'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Is contained.\x01",
            "Because my belongings are full,",
            scpstr(SCPSTR_CODE_ITEM, '大回复药'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I gave up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x4, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1728")

    Jump("loc_1772")

    label("loc_172D")

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

    label("loc_1772")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_9_162D end

    def Function_10_177E(): pass

    label("Function_10_177E")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_187E")
    Sound(14, 0, 100, 0)
    OP_74(0x5, 0x1E)
    OP_71(0x5, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('圣灵药·改', 1)"), scpexpr(EXPR_END)), "loc_1807")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '圣灵药·改'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1F3, 6)
    OP_E0(0x5, 0x0)
    Jump("loc_1879")

    label("loc_1807")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            "In the treasure box",
            scpstr(SCPSTR_CODE_ITEM, '圣灵药·改'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Is contained.\x01",
            "Because my belongings are full,",
            scpstr(SCPSTR_CODE_ITEM, '圣灵药·改'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I gave up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x5, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1879")

    Jump("loc_18C3")

    label("loc_187E")

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

    label("loc_18C3")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_10_177E end

    def Function_11_18CF(): pass

    label("Function_11_18CF")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_18DC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B8E")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "talk\x01",            # 0
            "Replace with Wadi\x01",      # 1
            "quit\x01",              # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19B5")

    ChrTalk(
        0x105,
        "#10300FWell then, I will ask you later.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#10100FYes, leave it!\x02",
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
    Jump("loc_1B89")

    label("loc_19B5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_19C9")
    Jump("loc_1B89")

    label("loc_19C9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B89")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AF5")

    ChrTalk(
        0x8,
        (
            "#10101FJorg Meister said\x01",
            "Gurus who bears the synonym of \"steel\" …\x01",
            "It seems like you are a partner who is not extraordinary.\x02\x03",
            "#10103F…… Arios also\x01",
            "I think that I will arrive after a while.\x02\x03",
            "#10101FWe were able to protect the hittermen,\x01",
            "Do not push yourself too hard.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1B89")

    label("loc_1AF5")


    ChrTalk(
        0x8,
        (
            "#10103FArios also\x01",
            "I think that I will arrive after a while.\x02\x03",
            "#10101FWe were able to protect the hittermen,\x01",
            "Do not push yourself too hard.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B89")

    Jump("loc_18DC")

    label("loc_1B8E")

    TalkEnd(0xFE)
    Return()

    # Function_11_18CF end

    def Function_12_1B92(): pass

    label("Function_12_1B92")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1B9F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E27")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "talk\x01",              # 0
            "To replace Noel\x01",      # 1
            "quit\x01",                # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C7A")

    ChrTalk(
        0x109,
        "#10100FWaji, I left it to you later!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#10300FHuh, I understand.\x02",
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
    Jump("loc_1E22")

    label("loc_1C7A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C8E")
    Jump("loc_1E22")

    label("loc_1C8E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E22")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D98")

    ChrTalk(
        0x9,
        (
            "#10301FAs Jorggu old man,\x01",
            "Even \"association\" but only people who seem to be dangerous\x01",
            "It seems they are coming.\x02\x03",
            "#10304FYou can also go back to Cross Bell City like this\x01",
            "After all the aftertaste is bad … …\x02\x03",
            "#10300FAt least their plot is\x01",
            "I wonder to keep track of it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1E22")

    label("loc_1D98")


    ChrTalk(
        0x9,
        (
            "#10303FYou can also go back to Cross Bell City like this\x01",
            "After all the aftertaste is bad … …\x02\x03",
            "#10300FAt least, the plot of \"association\"\x01",
            "I wonder to keep track of it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E22")

    Jump("loc_1B9F")

    label("loc_1E27")

    TalkEnd(0xFE)
    Return()

    # Function_12_1B92 end

    def Function_13_1E2B(): pass

    label("Function_13_1E2B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EE4")

    ChrTalk(
        0xFE,
        "Fu … … Rin is safe and good.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Perhaps, people in \"association\"\x01",
            "I guess it was not serious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… But at one such place,\x01",
            "I wonder what I'm trying to do ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1F4D")

    label("loc_1EE4")


    ChrTalk(
        0xFE,
        "Anyway, although phosphorus was okay, it was okay ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The people of \"association\"\x01",
            "I wonder what I'm trying to do ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F4D")

    TalkEnd(0xFE)
    Return()

    # Function_13_1E2B end

    def Function_14_1F51(): pass

    label("Function_14_1F51")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_207F")

    ChrTalk(
        0xFE,
        (
            "\"Harlequar\" and dressed as a knight\x01",
            "My girls were also troublesome … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That creepy masker\x01",
            "It was too different.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To be honest, even though there are legends' hatreds\x01",
            "Minutes may be bad …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#00700F… … If it stands up it will only die.\x02\x03",
            "If there is room to spare useless feelings\x01",
            "You concentrate on healing yourself.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2102")

    label("loc_207F")


    ChrTalk(
        0xFE,
        (
            "That creepy masker\x01",
            "It was too different.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To be honest, even though there are legends' hatreds\x01",
            "Minutes may be bad …\x01",
            "Please be careful enough.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2102")

    TalkEnd(0xFE)
    Return()

    # Function_14_1F51 end

    def Function_15_2106(): pass

    label("Function_15_2106")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_21F3")
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

    label("loc_21F3")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_15_2106 end

    def Function_16_2202(): pass

    label("Function_16_2202")

    OP_9B(0x0, 0xFE, 0x0, 0x2328, 0xFA0, 0x1)
    OP_9B(0x0, 0xFE, 0x159, 0x258, 0xFA0, 0x0)
    OP_93(0xFE, 0x0, 0x12C)
    Sleep(250)
    OP_9B(0x0, 0xFE, 0x0, 0x320, 0x7D0, 0x0)
    Sleep(100)
    Return()

    # Function_16_2202 end

    def Function_17_223D(): pass

    label("Function_17_223D")

    OP_9B(0x0, 0xFE, 0x0, 0x2328, 0xFA0, 0x1)
    OP_9B(0x0, 0xFE, 0xF, 0x320, 0xFA0, 0x1)
    OP_9B(0x0, 0xFE, 0x159, 0x320, 0xFA0, 0x0)
    TurnDirection(0xFE, 0xB, 500)
    Sleep(400)
    Return()

    # Function_17_223D end

    def Function_18_2275(): pass

    label("Function_18_2275")

    OP_9B(0x0, 0xFE, 0x0, 0x2328, 0xFA0, 0x1)
    Sleep(100)
    OP_9B(0x0, 0xFE, 0x159, 0x4B0, 0xFA0, 0x1)
    OP_9B(0x0, 0xFE, 0x1E, 0x7D0, 0xFA0, 0x1)
    OP_9B(0x0, 0xFE, 0xF, 0x4E2, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0xF, 0x4E2, 0x7D0, 0x0)
    TurnDirection(0xFE, 0xB, 500)
    Return()

    # Function_18_2275 end

    def Function_19_22CB(): pass

    label("Function_19_22CB")

    OP_9B(0x0, 0xFE, 0x0, 0x2328, 0xFA0, 0x1)
    OP_9B(0x0, 0xFE, 0xA, 0x5DC, 0xFA0, 0x1)
    OP_9B(0x0, 0xFE, 0x14, 0x7D0, 0xFA0, 0x1)
    OP_9B(0x0, 0xFE, 0x14A, 0xDAC, 0xFA0, 0x0)
    OP_93(0xFE, 0x13B, 0x1F4)
    TurnDirection(0xFE, 0xB, 500)
    Sleep(250)
    OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0x7D0, 0x0)
    Return()

    # Function_19_22CB end

    def Function_20_2328(): pass

    label("Function_20_2328")

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

    # Function_20_2328 end

    def Function_21_2384(): pass

    label("Function_21_2384")

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

    # Function_21_2384 end

    def Function_22_23DA(): pass

    label("Function_22_23DA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch51448.itc", 0x1E)
    LoadEffect(0x2, "event/ev17017.eff")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2414")
    OP_CF(0x1, 0xF4, 0x8)

    label("loc_2414")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2428")
    OP_CF(0x1, 0xF4, 0x4)

    label("loc_2428")

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

    def lambda_2553():
        OP_9B(0x0, 0x101, 0x154, 0xDAC, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2553)
    Sleep(30)

    def lambda_256B():
        OP_9B(0x0, 0x102, 0x154, 0xDAC, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_256B)
    Sleep(30)

    def lambda_2583():
        OP_9B(0x0, 0x103, 0x154, 0xDAC, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_2583)
    Sleep(30)

    def lambda_259B():
        OP_9B(0x0, 0x104, 0x154, 0xDAC, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_259B)
    Sleep(30)

    def lambda_25B3():
        OP_9B(0x0, 0xF4, 0x154, 0xDAC, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_25B3)
    Sleep(30)

    def lambda_25CB():
        OP_9B(0x0, 0x106, 0x154, 0xDAC, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_25CB)
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
        "#00013F#11P…!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#00700F#12PShe's there\x07\x00\x02",
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
            "#00010F#12PDamn\x01",
            "Mr. Lin, are you okay? Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00208F#6P…… Apparently to life\x01",
            "It seems that there is no other way … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#00700F#12PProbably exhausted power\x01",
            "It probably has fallen.\x02\x03",
            "#00702FMove. I'll give her some life\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2817():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2817)
    Sleep(50)

    def lambda_2827():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2827)
    Sleep(50)

    def lambda_2837():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_2837)
    Sleep(50)

    def lambda_2847():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_2847)
    Sleep(50)

    def lambda_2857():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_2857)
    Sleep(50)
    Sleep(300)

    ChrTalk(
        0x101,
        "#00011F#5PR-right, please do\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 2)

    def lambda_288E():
        OP_96(0xFE, 0x8930, 0x0, 0xFFFFE4BC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_288E)
    Sleep(350)

    def lambda_28AB():
        OP_9B(0x1, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_28AB)
    Sleep(300)

    def lambda_28C3():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_28C3)
    Sleep(50)

    def lambda_28D3():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_28D3)
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
            "#11P#60W#10A#00700FOhhh!\x07\x00\x02",
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
            "#11P#4S#00707FActive#2RAnd#It is!#12A\x07\x00\x02",
        )
    )

    Sleep(300)
    PlayEffect(0x2, 0xFF, 0xB, 0x1, 0, 350, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    StopEffect(0x7, 0x2)
    Sound(833, 0, 30, 0)
    CancelBlur(500)
    CloseMessageWindow()

    def lambda_29DA():
        TurnDirection(0xFE, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_29DA)
    Sleep(50)

    def lambda_29EA():
        TurnDirection(0xFE, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_29EA)
    Sleep(50)

    def lambda_29FA():
        TurnDirection(0xFE, 0xB, 500)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_29FA)
    Sleep(500)

    def lambda_2A0A():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_2A0A)
    WaitChrThread(0xB, 2)
    Sleep(500)

    ChrTalk(
        0xB,
        "#5P#50WUu\x02",
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

    def lambda_2AC0():
        OP_9B(0x1, 0xFE, 0xF, 0xFFFFFE70, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_2AC0)
    WaitChrThread(0x106, 1)

    ChrTalk(
        0xB,
        "#5P#30WAh!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5P#30WI see.\x01",
            "Have you fallen ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#6PLin san …. apparently\x01",
            "Do you seem to be grasping the situation?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#5P#30WYes… how shameful\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5P#30W……That's it……\x01",
            "Is Eolia safe …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00104F#12PYes. No need to worry\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd's in Lynn\x01",
            "I explained the circumstances until then.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xB,
        (
            "#5P#30W……Really……\x01",
            "I was really sorry ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5P#30WDamn\x01",
            "I am still inadequate in training ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5P#30WNo way to ah\x01",
            "I was treated like a child … ….\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2D09")

    ChrTalk(
        0x109,
        (
            "#10101F#11PHe said that he dressed as a knight\x01",
            "Do you mean girls?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D43")

    label("loc_2D09")


    ChrTalk(
        0x105,
        (
            "#10301F#11PHe said that he dressed as a knight\x01",
            "Do you mean girls?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D43")


    ChrTalk(
        0xB,
        (
            "#5P#30W……Disagreeable……\x01",
            "He was always tough.\x01",
            "There is one person exceptionally … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5P#30WIt's not a strong monster … …\x01",
            "…… Should I say that the dimensions are different …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5P#30WPerhaps Arios says\x01",
            "It may not be an enemy ……\x02",
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
        "#00007F#6PAh!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00307F#5PCome on … …\x01",
            "Is there such a good winning! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#12PMr. Jorg said\x01",
            "Perhaps one of the \"apostles\" …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00201F#6P\"steel#2RGlasses#\"It was named after the alias\x01",
            "It seems to be a terrible master, but …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#5P#30WI think that's who it was\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5P#30WAnd with a boy like a \"clown\"\x01",
            "I saw a middle-aged man in white coat ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5P#30WHow much the legendary haters#4RSchool#Even though\x01",
            "…… I guess the minutes may be bad … ….?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008F#6PThat is…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#00700F#12P…\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_68(37280, 1000, -6640, 1500)
    OP_96(0x106, 0x8D18, 0x0, 0xFFFFDFBC, 0x7D0, 0x1)
    OP_93(0x106, 0xE1, 0x190)

    def lambda_30DD():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_30DD)
    Sleep(50)

    def lambda_30ED():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_30ED)
    Sleep(50)

    def lambda_30FD():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_30FD)
    Sleep(50)

    def lambda_310D():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_310D)
    Sleep(50)

    def lambda_311D():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_311D)
    Sleep(250)

    ChrTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#00700F#5P── Our name is \"silver#2RIn#\".\x01",
            "Whatever your opponent is\x01",
            "It only disappears if necessary.\x02\x03",
            "#00702FIf you are afraid\x01",
            "Let's accompany this line.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00013F#5PW-wait a minute\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00107F#11PNo matter how much you are\x01",
            "It is unreasonable to go alone.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_327F")

    ChrTalk(
        0x109,
        (
            "#10101F#11PAnd, for the time being, please contact Waji\x01",
            "Let's leave Mr. Lin.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_32C5")

    label("loc_327F")


    ChrTalk(
        0x105,
        (
            "#10306F#11PTell me Noel for the time being\x01",
            "Shall I leave this older sister?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32C5")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3304")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 40670, 0, -5530, 180)
    ClearChrFlags(0x9, 0x80)
    OP_4B(0x9, 0xFF)
    Jump("loc_3323")

    label("loc_3304")

    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 40670, 0, -5530, 180)
    ClearChrFlags(0x8, 0x80)
    OP_4B(0x8, 0xFF)

    label("loc_3323")

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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_34AB")

    ChrTalk(
        0x9,
        (
            "#10301F#5P……Are you okay?\x01",
            "It seems to be a very bad partner.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34EE")

    label("loc_34AB")


    ChrTalk(
        0x8,
        (
            "#10101F#5PIs that okay?\x01",
            "It seems like an opponent who is not ordinary.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34EE")


    ChrTalk(
        0x101,
        (
            "#00000F#12PAh……\x01",
            "Anyway I will ask.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#12PWell, \"steel\" and\x01",
            "It seems that it will not be a matter of mutual respect,\x01",
            "Be careful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108F#12PRight…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#00700F#12PHmm\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5P#30WYes that should be good\x02\x03",
            "#5P#30W…… Goti armor and long cloak\x01",
            "It was supposed to be attached … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11PArios are coming, too,\x01",
            "Do not you feel uncomfortable do not you?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_366C():
        TurnDirection(0x101, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_366C)
    Sleep(50)

    def lambda_367C():
        TurnDirection(0x103, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_367C)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x103, 0)

    ChrTalk(
        0x101,
        "#00000F#6PYes, we know\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00201F#6PRoger that\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_370D")

    ChrTalk(
        0x109,
        "#10107F#12PLet's go then!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3732")

    label("loc_370D")


    ChrTalk(
        0x105,
        "#10301F#12POk then let's go\x02",
    )

    CloseMessageWindow()

    label("loc_3732")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3767")
    SetChrPos(0x9, 44360, 0, -7020, 270)
    OP_4C(0x9, 0xFF)
    Jump("loc_377C")

    label("loc_3767")

    SetChrPos(0x8, 44360, 0, -7020, 270)
    OP_4C(0x8, 0xFF)

    label("loc_377C")

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

    # Function_22_23DA end

    def Function_23_37DD(): pass

    label("Function_23_37DD")

    SetChrSubChip(0xB, 0x0)
    Sleep(100)
    SetChrSubChip(0xB, 0x1)
    Sleep(100)
    SetChrSubChip(0xB, 0x0)
    Sleep(100)
    SetChrSubChip(0xB, 0x1)
    Sleep(100)
    Return()

    # Function_23_37DD end

    SaveToFile()

Try(main)
