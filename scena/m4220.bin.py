from ScenarioHelper import *

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

    Sepith("Sepith_39BA", 4,   2,   10,  4,   8,   2,   10)
    Sepith("Sepith_39B2", 5,   2,   8,   8,   2,   8,   2)
    Sepith("Sepith_39A2", 8,   8,   6,   6,   6,   8,   6)

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
        "BattleInfo_5AC", 0x0000, 71, 6, 60, 10, 1, 20, 0, "bm4200", "Sepith_39BA", 40, 30, 20, 0,
        (
            ("ms86800.dat", "ms82700.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3D4", "MonsterBattlePostion_454", "ed7450", "ed7453", "ATBonus_3A4"),
            ("ms86800.dat", "ms82700.dat", "ms82700.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_3F4", "MonsterBattlePostion_454", "ed7450", "ed7453", "ATBonus_3A4"),
            ("ms86800.dat", "ms82700.dat", "ms82700.dat", "ms82700.dat", 0, 0, 0, 0, "MonsterBattlePostion_3D4", "MonsterBattlePostion_454", "ed7450", "ed7453", "ATBonus_3A4"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_510", 0x0000, 71, 6, 60, 10, 1, 30, 0, "bm4200", "Sepith_39B2", 40, 30, 20, 0,
        (
            ("ms83300.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3F4", "MonsterBattlePostion_454", "ed7450", "ed7453", "ATBonus_3A4"),
            ("ms83300.dat", "ms83300.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3D4", "MonsterBattlePostion_454", "ed7450", "ed7453", "ATBonus_3A4"),
            ("ms83300.dat", "ms83300.dat", "ms83300.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_3F4", "MonsterBattlePostion_454", "ed7450", "ed7453", "ATBonus_3A4"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_474", 0x0000, 71, 6, 60, 10, 1, 40, 0, "bm4200", "Sepith_39A2", 50, 25, 25, 0,
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
        "Function_6_115F",         # 06, 6
        "Function_7_12B1",         # 07, 7
        "Function_8_14CD",         # 08, 8
        "Function_9_1627",         # 09, 9
        "Function_10_1779",        # 0A, 10
        "Function_11_18CB",        # 0B, 11
        "Function_12_1BBB",        # 0C, 12
        "Function_13_1E78",        # 0D, 13
        "Function_14_1FAC",        # 0E, 14
        "Function_15_2206",        # 0F, 15
        "Function_16_22FC",        # 10, 16
        "Function_17_2337",        # 11, 17
        "Function_18_236F",        # 12, 18
        "Function_19_23C5",        # 13, 19
        "Function_20_2422",        # 14, 20
        "Function_21_247E",        # 15, 21
        "Function_22_24D4",        # 16, 22
        "Function_23_395D",        # 17, 23
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
            "Since you have too many, you gave it up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x0, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1104")

    Jump("loc_1153")

    label("loc_1109")

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

    label("loc_1153")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_100D end

    def Function_6_115F(): pass

    label("Function_6_115F")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F3, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_125B")
    Sound(14, 0, 100, 0)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x5E8, 1)"), scpexpr(EXPR_END)), "loc_11E4")
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
    Jump("loc_1256")

    label("loc_11E4")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x5E8),
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

    label("loc_1256")

    Jump("loc_12A5")

    label("loc_125B")

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

    label("loc_12A5")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_115F end

    def Function_7_12B1(): pass

    label("Function_7_12B1")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1482")
    Sound(14, 0, 100, 0)
    OP_74(0x2, 0x1E)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x217, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13B4")
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0xC, 0x0, 0)
    OP_98(0xC, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_130E():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_130E)

    def lambda_1328():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_1328)
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
        (0, "loc_1395"),
        (2, "loc_13A4"),
        (1, "loc_13B1"),
        (SWITCH_DEFAULT, "loc_13B4"),
    )


    label("loc_1395")

    SetScenarioFlags(0x217, 4)
    OP_70(0x2, 0x1E)
    Sleep(500)
    Jump("loc_13B4")

    label("loc_13A4")

    OP_70(0x2, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_13B1")

    OP_B9(0x0)
    Return()

    label("loc_13B4")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x72, 1)"), scpexpr(EXPR_END)), "loc_140D")
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
    Jump("loc_147D")

    label("loc_140D")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x72),
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

    label("loc_147D")

    Jump("loc_14C1")

    label("loc_1482")

    FadeToDark(300, 0, 100)

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

    label("loc_14C1")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_12B1 end

    def Function_8_14CD(): pass

    label("Function_8_14CD")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F3, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15F7")
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
            "#56IEarth Sepith x80\x01\x07\x02",
            "#57IWater Sepith x80\x01\x07\x02",
            "#58IFire Sepith x80\x01\x07\x02",
            "#59IWind Sepith x80\x01\x07\x02",
            "#60ITime Sepith x80\x01\x07\x02",
            "#61ISpace Sepith x80\x01\x07\x02",
            "#62IMirage Sepith x80\x01\x07\x00",
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x1F3, 4)
    OP_E0(0x5, 0x0)
    Jump("loc_1615")

    label("loc_15F7")


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

    label("loc_1615")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_14CD end

    def Function_9_1627(): pass

    label("Function_9_1627")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F3, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1723")
    Sound(14, 0, 100, 0)
    OP_74(0x4, 0x1E)
    OP_71(0x4, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1F6, 1)"), scpexpr(EXPR_END)), "loc_16AC")
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
    Jump("loc_171E")

    label("loc_16AC")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1F6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " is inside the chest.\x01",
            "Since you have too many, you gave it up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x4, 0x1E, 0x0, 0x0, 0x0)

    label("loc_171E")

    Jump("loc_176D")

    label("loc_1723")

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

    label("loc_176D")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_9_1627 end

    def Function_10_1779(): pass

    label("Function_10_1779")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1875")
    Sound(14, 0, 100, 0)
    OP_74(0x5, 0x1E)
    OP_71(0x5, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1FD, 1)"), scpexpr(EXPR_END)), "loc_17FE")
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
    Jump("loc_1870")

    label("loc_17FE")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1FD),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " is inside the chest.\x01",
            "Since you have too many, you gave it up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x5, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1870")

    Jump("loc_18BF")

    label("loc_1875")

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

    label("loc_18BF")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_10_1779 end

    def Function_11_18CB(): pass

    label("Function_11_18CB")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_18D8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BB7")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",                 # 0
            "Switch Wazy Out\x01",      # 1
            "Quit\x01",                 # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19B8")

    ChrTalk(
        0x105,
        "#10300FThen, take care of the rest.\x02",
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
    Jump("loc_1BB2")

    label("loc_19B8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_19CC")
    Jump("loc_1BB2")

    label("loc_19CC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BB2")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B16")

    ChrTalk(
        0x8,
        (
            "#10101FThe expert known with the alias of "Steel" \x01",
            "who Meister Jｶrg  was talking about...\x01",
            "Looks like not your common opponent.\x02\x03",
            "#10103F...I think that Mr. Arios and \x01",
            "the others will be arriving soon.\x02\x03",
            "#10101FWe were able to recover the Bracers,\x01",
            "so please don't do anything foolish.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1BB2")

    label("loc_1B16")


    ChrTalk(
        0x8,
        (
            "#10103FI think that Mr. Arios and \x01",
            "the others will be arriving soon.\x02\x03",
            "#10101FWe were able to recover the Bracers,\x01",
            "so please don't do anything foolish.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BB2")

    Jump("loc_18D8")

    label("loc_1BB7")

    TalkEnd(0xFE)
    Return()

    # Function_11_18CB end

    def Function_12_1BBB(): pass

    label("Function_12_1BBB")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1BC8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E74")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",                  # 0
            "Switch Noｱl Out\x01",      # 1
            "Quit\x01",                  # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CA3")

    ChrTalk(
        0x109,
        "#10100FWazy, I leave the rest to you!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#10300FHu hu, roger.\x02",
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
    Jump("loc_1E6F")

    label("loc_1CA3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1CB7")
    Jump("loc_1E6F")

    label("loc_1CB7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E6F")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DD6")

    ChrTalk(
        0x9,
        (
            "#10301FLike Meister Jｶrg said, it\x01",
            "appears that the "Society"\x01",
            "has only dangerous persons.\x02\x03",
            "#10304FIt would leave a bad aftertaste returning\x01",
            "to Crossbell City like this...\x02\x03",
            "#10300FI would at least like to make\x01",
            "sure of what they're scheming.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1E6F")

    label("loc_1DD6")


    ChrTalk(
        0x9,
        (
            "#10303FIt would leave a bad aftertaste returning\x01",
            "to Crossbell City like this..\x02\x03",
            "#10300FI would at least like to make\x01",
            "sure of what they're scheming.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E6F")

    Jump("loc_1BC8")

    label("loc_1E74")

    TalkEnd(0xFE)
    Return()

    # Function_12_1BBB end

    def Function_13_1E78(): pass

    label("Function_13_1E78")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F35")

    ChrTalk(
        0xFE,
        "*phew*...I'm glad Ling is all right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Maybe the "Society" people\x01",
            "too didn't go all out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...However, what are they trying\x01",
            "to do in such a place, I wonder?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1FA8")

    label("loc_1F35")


    ChrTalk(
        0xFE,
        "In any case, I'm happy Ling is safe, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The "Society" people... \x01",
            "I wonder what they're trying to do?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FA8")

    TalkEnd(0xFE)
    Return()

    # Function_13_1E78 end

    def Function_14_1FAC(): pass

    label("Function_14_1FAC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2149")

    ChrTalk(
        0xFE,
        (
            "The "Fool" and also the girls\x01",
            "in armor were bad news, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That one with the creepy mask\x01",
            "was in a totally different league.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Frankly speaking, even if the legendary\x01",
            "assassin is with you, you could have no edge...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#00700F...Whoever stands in my way, I'll just crush it.\x02\x03",
            "If you have the time for useless and groundless\x01",
            "suspicions, you should use it to heal your body.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2202")

    label("loc_2149")


    ChrTalk(
        0xFE,
        (
            "That one with the creepy mask\x01",
            "was in a totally different league.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Frankly speaking, even if the legendary\x01",
            "assassin is with you, you could have no edge...\x01",
            "Be extremely careful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2202")

    TalkEnd(0xFE)
    Return()

    # Function_14_1FAC end

    def Function_15_2206(): pass

    label("Function_15_2206")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_22ED")
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

    label("loc_22ED")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_15_2206 end

    def Function_16_22FC(): pass

    label("Function_16_22FC")

    OP_9B(0x0, 0xFE, 0x0, 0x2328, 0xFA0, 0x1)
    OP_9B(0x0, 0xFE, 0x159, 0x258, 0xFA0, 0x0)
    OP_93(0xFE, 0x0, 0x12C)
    Sleep(250)
    OP_9B(0x0, 0xFE, 0x0, 0x320, 0x7D0, 0x0)
    Sleep(100)
    Return()

    # Function_16_22FC end

    def Function_17_2337(): pass

    label("Function_17_2337")

    OP_9B(0x0, 0xFE, 0x0, 0x2328, 0xFA0, 0x1)
    OP_9B(0x0, 0xFE, 0xF, 0x320, 0xFA0, 0x1)
    OP_9B(0x0, 0xFE, 0x159, 0x320, 0xFA0, 0x0)
    TurnDirection(0xFE, 0xB, 500)
    Sleep(400)
    Return()

    # Function_17_2337 end

    def Function_18_236F(): pass

    label("Function_18_236F")

    OP_9B(0x0, 0xFE, 0x0, 0x2328, 0xFA0, 0x1)
    Sleep(100)
    OP_9B(0x0, 0xFE, 0x159, 0x4B0, 0xFA0, 0x1)
    OP_9B(0x0, 0xFE, 0x1E, 0x7D0, 0xFA0, 0x1)
    OP_9B(0x0, 0xFE, 0xF, 0x4E2, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0xF, 0x4E2, 0x7D0, 0x0)
    TurnDirection(0xFE, 0xB, 500)
    Return()

    # Function_18_236F end

    def Function_19_23C5(): pass

    label("Function_19_23C5")

    OP_9B(0x0, 0xFE, 0x0, 0x2328, 0xFA0, 0x1)
    OP_9B(0x0, 0xFE, 0xA, 0x5DC, 0xFA0, 0x1)
    OP_9B(0x0, 0xFE, 0x14, 0x7D0, 0xFA0, 0x1)
    OP_9B(0x0, 0xFE, 0x14A, 0xDAC, 0xFA0, 0x0)
    OP_93(0xFE, 0x13B, 0x1F4)
    TurnDirection(0xFE, 0xB, 500)
    Sleep(250)
    OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0x7D0, 0x0)
    Return()

    # Function_19_23C5 end

    def Function_20_2422(): pass

    label("Function_20_2422")

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

    # Function_20_2422 end

    def Function_21_247E(): pass

    label("Function_21_247E")

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

    # Function_21_247E end

    def Function_22_24D4(): pass

    label("Function_22_24D4")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch51448.itc", 0x1E)
    LoadEffect(0x2, "event/ev17017.eff")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_250E")
    OP_CF(0x1, 0xF4, 0x8)

    label("loc_250E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2522")
    OP_CF(0x1, 0xF4, 0x4)

    label("loc_2522")

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

    def lambda_264D():
        OP_9B(0x0, 0x101, 0x154, 0xDAC, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_264D)
    Sleep(30)

    def lambda_2665():
        OP_9B(0x0, 0x102, 0x154, 0xDAC, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_2665)
    Sleep(30)

    def lambda_267D():
        OP_9B(0x0, 0x103, 0x154, 0xDAC, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_267D)
    Sleep(30)

    def lambda_2695():
        OP_9B(0x0, 0x104, 0x154, 0xDAC, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_2695)
    Sleep(30)

    def lambda_26AD():
        OP_9B(0x0, 0xF4, 0x154, 0xDAC, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_26AD)
    Sleep(30)

    def lambda_26C5():
        OP_9B(0x0, 0x106, 0x154, 0xDAC, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_26C5)
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
        "#00013F#11P......!\x02",
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
            "#00010F#12PKh...\x01",
            "Miss Ling, are you all right!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00208F#6P...It looks like her\x01",
            "life is not in danger...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#00700F#12PShe probably used up all her\x01",
            "energy and ended up collapsing.\x02\x03",
            "#00702FMove aside── I'll try to reanimate her.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2933():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2933)
    Sleep(50)

    def lambda_2943():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2943)
    Sleep(50)

    def lambda_2953():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_2953)
    Sleep(50)

    def lambda_2963():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_2963)
    Sleep(50)

    def lambda_2973():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_2973)
    Sleep(50)
    Sleep(300)

    ChrTalk(
        0x101,
        "#00011F#5PY-Yeah, please.\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 2)

    def lambda_29A9():
        OP_96(0xFE, 0x8930, 0x0, 0xFFFFE4BC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_29A9)
    Sleep(350)

    def lambda_29C6():
        OP_9B(0x1, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_29C6)
    Sleep(300)

    def lambda_29DE():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_29DE)
    Sleep(50)

    def lambda_29EE():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_29EE)
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
            "#11P#4S#00707F──REVIVE!#12A\x07\x00\x02",
        )
    )

    Sleep(300)
    PlayEffect(0x2, 0xFF, 0xB, 0x1, 0, 350, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    StopEffect(0x7, 0x2)
    Sound(833, 0, 30, 0)
    CancelBlur(500)
    CloseMessageWindow()

    def lambda_2AEB():
        TurnDirection(0xFE, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2AEB)
    Sleep(50)

    def lambda_2AFB():
        TurnDirection(0xFE, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_2AFB)
    Sleep(50)

    def lambda_2B0B():
        TurnDirection(0xFE, 0xB, 500)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_2B0B)
    Sleep(500)

    def lambda_2B1B():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_2B1B)
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

    def lambda_2BD1():
        OP_9B(0x1, 0xFE, 0xF, 0xFFFFFE70, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_2BD1)
    WaitChrThread(0x106, 1)

    ChrTalk(
        0xB,
        "#5P#30W...Kh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5P#30WI see... \x01",
            "I collapsed...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#6PMiss Ling... It seems you\x01",
            "know what happened?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#5P#30WYeah... What a shame...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5P#30W...Oh...\x01",
            "Is Eolia safe...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00104F#12PYes, you don't need to worry.\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd and the others explained\x01",
            "to Ling what happened until then.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xB,
        (
            "#5P#30W...I see...\x01",
            "I'm really thankful...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5P#30WKh...\x01",
            "I still lack training, eh...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5P#30WI'd never thought I'd been\x01",
            "treated like a child like that...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2E1B")

    ChrTalk(
        0x109,
        (
            "#10101F#11PAre you talking about\x01",
            "the girls in armor?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E4D")

    label("loc_2E1B")


    ChrTalk(
        0x105,
        (
            "#10301F#11PTalking about\x01",
            "the girls in armor?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E4D")


    ChrTalk(
        0xB,
        (
            "#5P#30W...No...\x01",
            "They were strong too, but there's\x01",
            "someone on a different league...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5P#30WIt's not strong...\x01",
            "...It's on a different plane, I'd say...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5P#30WMaybe not even Mr. Arios\x01",
            "could be a match...\x02",
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
            "#00307F#5PHey now...\x01",
            "That's impossible, you know!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#12PCould it be the "Anguis"\x01",
            "Mr. Jｶrg was talking about...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00201F#6PIt seems it is a fearsome master\x01",
            "whose alias is "Steel"...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#5P#30W...It's probably that one.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5P#30WAlso, I spotted a boy called the "Fool"\x01",
            "and a middle age man in a white robe....\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5P#30WNo matter if the legendary assassin is with you...\x01",
            "...You could have no edge, you know...?\x02",
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

    def lambda_3207():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3207)
    Sleep(50)

    def lambda_3217():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3217)
    Sleep(50)

    def lambda_3227():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_3227)
    Sleep(50)

    def lambda_3237():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_3237)
    Sleep(50)

    def lambda_3247():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_3247)
    Sleep(250)

    ChrTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#00700F#5P──My name is "Yin".\x01",
            "No matter the opponent,\x01",
            "if needed, I just crush it.\x02\x03",
            "#00702FIf you all are frightened, then\x01",
            "I'll stop accompanying you here.\x07\x00\x02",
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
            "alone is unreasonable!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_33B7")

    ChrTalk(
        0x109,
        (
            "#10101F#11PF-For now let's contact Wazy\x01",
            "and entrust Miss Ling to him.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3400")

    label("loc_33B7")


    ChrTalk(
        0x105,
        (
            "#10306F#11PFor now let's contact Noｱl and\x01",
            "entrust this lady to her.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3400")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_343F")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 40670, 0, -5530, 180)
    ClearChrFlags(0x9, 0x80)
    OP_4B(0x9, 0xFF)
    Jump("loc_345E")

    label("loc_343F")

    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 40670, 0, -5530, 180)
    ClearChrFlags(0x8, 0x80)
    OP_4B(0x8, 0xFF)

    label("loc_345E")

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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_35F3")

    ChrTalk(
        0x9,
        (
            "#10301F#5P...Will you be ok?\x01",
            "It looks like quite the dangerous opponent.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3643")

    label("loc_35F3")


    ChrTalk(
        0x8,
        (
            "#10101F#5PW-Will you be all right?\x01",
            "It looks like not your common opponent.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3643")


    ChrTalk(
        0x101,
        (
            "#00000F#12PYeah...\x01",
            "At any rate, we'll monitor the situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#12PWell, we'll be careful to\x01",
            "not get down to business\x01",
            "with the "Steel" guy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108F#12P......Right......\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#00700F#12P............Hmph.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5P#30WYeah, that would be nice...\x02\x03",
            "#5P#30W...You'll recognize the guy since it dons\x01",
            "a bulky armor and a long mantle...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11PMr. Arios and the others are coming too,\x01",
            "so don't do anything rash, ok?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_37F9():
        TurnDirection(0x101, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_37F9)
    Sleep(50)

    def lambda_3809():
        TurnDirection(0x103, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_3809)
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
        "#00201F#6P...Roger that.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_388F")

    ChrTalk(
        0x109,
        "#10107F#12PThen, let's go!\x02",
    )

    CloseMessageWindow()
    Jump("loc_38B2")

    label("loc_388F")


    ChrTalk(
        0x105,
        "#10301F#12PThen, shall we go?\x02",
    )

    CloseMessageWindow()

    label("loc_38B2")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_38E7")
    SetChrPos(0x9, 44360, 0, -7020, 270)
    OP_4C(0x9, 0xFF)
    Jump("loc_38FC")

    label("loc_38E7")

    SetChrPos(0x8, 44360, 0, -7020, 270)
    OP_4C(0x8, 0xFF)

    label("loc_38FC")

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

    # Function_22_24D4 end

    def Function_23_395D(): pass

    label("Function_23_395D")

    SetChrSubChip(0xB, 0x0)
    Sleep(100)
    SetChrSubChip(0xB, 0x1)
    Sleep(100)
    SetChrSubChip(0xB, 0x0)
    Sleep(100)
    SetChrSubChip(0xB, 0x1)
    Sleep(100)
    Return()

    # Function_23_395D end

    SaveToFile()

Try(main)
