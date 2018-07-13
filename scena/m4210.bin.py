from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "m4210.bin",                # FileName
        "m4210",                    # MapName
        "m4210",                    # Location
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
        "m4210",                  # 0
        "Noｱl",                  # 1
        "Wazy",                   # 2
        "Bracer Eolia",           # 3
        "Mad Bloom",              # 4
        "bm4200",                 # 5
        "bm4200",                 # 6
        "bm4200",                 # 7
        "bm4200",                 # 8
    ))

    ATBonus("ATBonus_3E0", 100, 5, 1, 5, 1, 5, 1, 5, 5, 5, 5, 5, 5, 0, 0, 0)
    ATBonus("ATBonus_3F0", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    Sepith("Sepith_3123", 4,   2,   10,  4,   8,   2,   10)
    Sepith("Sepith_311B", 5,   2,   8,   8,   2,   8,   2)
    Sepith("Sepith_310B", 8,   8,   6,   6,   6,   8,   6)

    MonsterBattlePostion("MonsterBattlePostion_410", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_414", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_418", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_41C", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_420", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_424", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_428", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_42C", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_490", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_494", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_498", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_49C", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_4A0", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_4A4", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_4A8", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_4AC", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_430", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_434", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_438", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_43C", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_440", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_444", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_448", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_44C", 8, 14, 180)

    # monster count: 10

    BattleInfo(
        "BattleInfo_5E8", 0x0000, 71, 6, 60, 10, 1, 20, 0, "bm4200", "Sepith_3123", 40, 30, 20, 0,
        (
            ("ms86800.dat", "ms82700.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_410", "MonsterBattlePostion_490", "ed7450", "ed7453", "ATBonus_3E0"),
            ("ms86800.dat", "ms82700.dat", "ms82700.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_430", "MonsterBattlePostion_490", "ed7450", "ed7453", "ATBonus_3E0"),
            ("ms86800.dat", "ms82700.dat", "ms82700.dat", "ms82700.dat", 0, 0, 0, 0, "MonsterBattlePostion_410", "MonsterBattlePostion_490", "ed7450", "ed7453", "ATBonus_3E0"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_54C", 0x0000, 71, 6, 60, 10, 1, 30, 0, "bm4200", "Sepith_311B", 40, 30, 20, 0,
        (
            ("ms83300.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_430", "MonsterBattlePostion_490", "ed7450", "ed7453", "ATBonus_3E0"),
            ("ms83300.dat", "ms83300.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_410", "MonsterBattlePostion_490", "ed7450", "ed7453", "ATBonus_3E0"),
            ("ms83300.dat", "ms83300.dat", "ms83300.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_430", "MonsterBattlePostion_490", "ed7450", "ed7453", "ATBonus_3E0"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_4B0", 0x0000, 71, 6, 60, 10, 1, 40, 0, "bm4200", "Sepith_310B", 50, 25, 25, 0,
        (
            ("ms78200.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_430", "MonsterBattlePostion_490", "ed7450", "ed7453", "ATBonus_3E0"),
            ("ms78200.dat", "ms78200.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_410", "MonsterBattlePostion_490", "ed7450", "ed7453", "ATBonus_3E0"),
            ("ms78200.dat", "ms82700.dat", "ms82700.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_430", "MonsterBattlePostion_490", "ed7450", "ed7453", "ATBonus_3E0"),
            (),
        )
    )

    # event battle count: 1

    BattleInfo(
        "BattleInfo_684", 0x0C00, 255, 6, 0, 0, 3, 0, 0, "bm4200", 0x00000000, 100, 0, 0, 0,
        (
            ("ms86800.dat", "ms82700.dat", "ms86800.dat", "ms82700.dat", "ms86800.dat", "ms82700.dat", "ms86800.dat", "ms82700.dat", "MonsterBattlePostion_410", "MonsterBattlePostion_490", "ed7451", "ed7453", "ATBonus_3F0"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch02900.itc",                   # 00
        "chr/ch03000.itc",                   # 01
        "apl/ch51406.itc",                   # 02
        "chr/ch32153.itc",                   # 03
        "apl/ch51446.itc",                   # 04
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

    DeclNpc(39619,   0,       4294960527, 270,  389,  0x0, 0,   0,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(39619,   0,       4294960527, 270,  389,  0x0, 0,   1,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(38650,   0,       4294961907, 180,  389,  0x0, 0,   2,   0,   255, 255, 0,   12,  255,  0)
    DeclNpc(4294921296, 500,     30000,   0,    484,  0x0, 0,   24,  0,   0,   1,   255, 255, 255,  0)

    DeclMonster(4294964066, 4294935166, 0,       0x1010070,    "BattleInfo_5E8", 0,   24,  0xFFFF, 4,  5)
    DeclMonster(4294954686, 4294958546, 0,       0x1010087,    "BattleInfo_54C", 0,   22,  0xFFFF, 2,  3)
    DeclMonster(8530,    7730,    0,       0x10100FD,    "BattleInfo_4B0", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(4294958796, 28300,   0,       0x10100A5,    "BattleInfo_54C", 0,   22,  0xFFFF, 2,  3)
    DeclMonster(4294948706, 4294939466, 0,       0x101013B,    "BattleInfo_5E8", 0,   24,  0xFFFF, 4,  5)
    DeclMonster(4294916226, 4294965566, 0,       0x1010094,    "BattleInfo_4B0", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(4294894256, 23790,   0,       0x10100C4,    "BattleInfo_5E8", 0,   24,  0xFFFF, 4,  5)
    DeclMonster(4294908366, 37820,   0,       0x1010122,    "BattleInfo_4B0", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(4294908156, 63620,   0,       0x1010125,    "BattleInfo_54C", 0,   22,  0xFFFF, 2,  3)
    DeclMonster(4294886936, 70400,   0,       0x1010044,    "BattleInfo_54C", 0,   22,  0xFFFF, 2,  3)

    DeclEvent(0x0000, 0, 14,  47.0,                  -10.0,                 -1.0,                  56.25,                 [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -15.666666984558105,   2.0,                   0.20000000298023224,   1.0])

    DeclActor(32500,   0,       24000,   1200,    32500,   1000,    24000,   0x007C, 0,  5,  0x0000)
    DeclActor(10000,   0,       4294953296, 1200,    10000,   1000,    4294953296, 0x007C, 0,  6,  0x0000)
    DeclActor(4294948796, 0,       4294935296, 1200,    4294948796, 1000,    4294935296, 0x007C, 0,  7,  0x0000)
    DeclActor(4294921296, 0,       30000,   1200,    4294921296, 1000,    30000,   0x007C, 0,  8,  0x0000)
    DeclActor(4294913796, 0,       63500,   1200,    4294913796, 1000,    63500,   0x007C, 0,  9,  0x0000)

    ChipFrameInfo(800, 0, [0, 1, 2, 3, 4])                       # 0
    ChipFrameInfo(1000, 0, [0, 1, 2, 3])                         # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 2, 1])                   # 2
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4])                      # 3
    ChipFrameInfo(800, 0, [0, 1, 2, 3, 4, 5])                    # 4
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 5])                   # 5

    ScpFunction((
        "Function_0_74C",          # 00, 0
        "Function_1_7FC",          # 01, 1
        "Function_2_819",          # 02, 2
        "Function_3_841",          # 03, 3
        "Function_4_11D9",         # 04, 4
        "Function_5_120E",         # 05, 5
        "Function_6_1360",         # 06, 6
        "Function_7_14B2",         # 07, 7
        "Function_8_1604",         # 08, 8
        "Function_9_1820",         # 09, 9
        "Function_10_1972",        # 0A, 10
        "Function_11_1BB6",        # 0B, 11
        "Function_12_1EB6",        # 0C, 12
        "Function_13_201F",        # 0D, 13
        "Function_14_20A8",        # 0E, 14
    ))


    def Function_0_74C(): pass

    label("Function_0_74C")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_784"),
        (1, "loc_790"),
        (2, "loc_79C"),
        (3, "loc_7A8"),
        (4, "loc_7B4"),
        (5, "loc_7C0"),
        (6, "loc_7CC"),
        (SWITCH_DEFAULT, "loc_7D8"),
    )


    label("loc_784")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_7E4")

    label("loc_790")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_7E4")

    label("loc_79C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_7E4")

    label("loc_7A8")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_7E4")

    label("loc_7B4")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_7E4")

    label("loc_7C0")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_7E4")

    label("loc_7CC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_7E4")

    label("loc_7D8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_7E4")

    label("loc_7E4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7FB")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_7E4")

    label("loc_7FB")

    Return()

    # Function_0_74C end

    def Function_1_7FC(): pass

    label("Function_1_7FC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_818")
    OP_A1(0xFE, 0x320, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Jump("Function_1_7FC")

    label("loc_818")

    Return()

    # Function_1_7FC end

    def Function_2_819(): pass

    label("Function_2_819")

    SetChrChipByIndex(0xA, 0x2)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_840")
    Call(0, 4)
    ClearChrFlags(0xA, 0x80)

    label("loc_840")

    Return()

    # Function_2_819 end

    def Function_3_841(): pass

    label("Function_3_841")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_863")
    LoadEffect(0x9, "event/ev14011.eff")

    label("loc_863")

    OP_52(0xE, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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
    OP_52(0x14, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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
    OP_52(0x12, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10CC")
    OP_70(0x0, 0x0)
    Jump("loc_10D0")

    label("loc_10CC")

    OP_70(0x0, 0x1E)

    label("loc_10D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10E3")
    OP_70(0x1, 0x0)
    Jump("loc_10E7")

    label("loc_10E3")

    OP_70(0x1, 0x1E)

    label("loc_10E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F2, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10FA")
    OP_70(0x2, 0x0)
    Jump("loc_10FE")

    label("loc_10FA")

    OP_70(0x2, 0x1E)

    label("loc_10FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1111")
    OP_70(0x3, 0x0)
    Jump("loc_1115")

    label("loc_1111")

    OP_70(0x3, 0x1E)

    label("loc_1115")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1128")
    OP_70(0x4, 0x0)
    Jump("loc_112C")

    label("loc_1128")

    OP_70(0x4, 0x1E)

    label("loc_112C")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1144")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_1144")

    SetMapObjFrame(0xFF, "CA_stop", 0x0, 0x1)
    SetMapObjFrame(0xFF, "bridge", 0x0, 0x1)
    SetMapObjFrame(0xFF, "MAP101", 0x0, 0x1)
    SetMapObjFrame(0xFF, "CA_stop", 0x0, 0x2)
    SetMapObjFlags(0x5, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 7)), scpexpr(EXPR_END)), "loc_11D2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_11CC")
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFrame(0xFF, "bridge", 0x1, 0x1)
    SetMapObjFrame(0xFF, "CA_stop", 0x1, 0x2)
    SetMapObjFrame(0xFF, "MAP101", 0x1, 0x1)
    Jump("loc_11D2")

    label("loc_11CC")

    ClearMapObjFlags(0x5, 0x4)

    label("loc_11D2")

    Sound(123, 1, 80, 0)
    Return()

    # Function_3_841 end

    def Function_4_11D9(): pass

    label("Function_4_11D9")

    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_LEQ), scpexpr(EXPR_END)), "loc_11F8")
    ClearChrFlags(0x8, 0x80)

    label("loc_11F8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_LEQ), scpexpr(EXPR_END)), "loc_120D")
    ClearChrFlags(0x9, 0x80)

    label("loc_120D")

    Return()

    # Function_4_11D9 end

    def Function_5_120E(): pass

    label("Function_5_120E")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_130A")
    Sound(14, 0, 100, 0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1F6, 1)"), scpexpr(EXPR_END)), "loc_1293")
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
    SetScenarioFlags(0x1F2, 4)
    OP_E0(0x5, 0x0)
    Jump("loc_1305")

    label("loc_1293")

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
    OP_71(0x0, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1305")

    Jump("loc_1354")

    label("loc_130A")

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

    label("loc_1354")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_120E end

    def Function_6_1360(): pass

    label("Function_6_1360")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_145C")
    Sound(14, 0, 100, 0)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x334, 1)"), scpexpr(EXPR_END)), "loc_13E5")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x334),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1F2, 5)
    OP_E0(0x5, 0x0)
    Jump("loc_1457")

    label("loc_13E5")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x334),
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

    label("loc_1457")

    Jump("loc_14A6")

    label("loc_145C")

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

    label("loc_14A6")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_1360 end

    def Function_7_14B2(): pass

    label("Function_7_14B2")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F2, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15AE")
    Sound(14, 0, 100, 0)
    OP_74(0x2, 0x1E)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x33, 1)"), scpexpr(EXPR_END)), "loc_1537")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x33),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1F2, 6)
    OP_E0(0x5, 0x0)
    Jump("loc_15A9")

    label("loc_1537")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x33),
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

    label("loc_15A9")

    Jump("loc_15F8")

    label("loc_15AE")

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

    label("loc_15F8")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_14B2 end

    def Function_8_1604(): pass

    label("Function_8_1604")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17D5")
    Sound(14, 0, 100, 0)
    OP_74(0x3, 0x1E)
    OP_71(0x3, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x217, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1707")
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0xB, 0x0, 0)
    OP_98(0xB, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_1661():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1661)

    def lambda_167B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_167B)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Monsters appeared!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    WaitChrThread(0xB, 1)
    Battle("BattleInfo_684", 0x0, 0x0, 0x0, 0xB, 0xFF)
    SetChrFlags(0xB, 0x80)
    ClearChrFlags(0xB, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_16E8"),
        (2, "loc_16F7"),
        (1, "loc_1704"),
        (SWITCH_DEFAULT, "loc_1707"),
    )


    label("loc_16E8")

    SetScenarioFlags(0x217, 3)
    OP_70(0x3, 0x1E)
    Sleep(500)
    Jump("loc_1707")

    label("loc_16F7")

    OP_70(0x3, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_1704")

    OP_B9(0x0)
    Return()

    label("loc_1707")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x82, 1)"), scpexpr(EXPR_END)), "loc_1760")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x82),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1F2, 7)
    OP_E0(0x5, 0x0)
    Jump("loc_17D0")

    label("loc_1760")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x82),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " is inside the chest.\x01",
            "Since you have too many, you gave it up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x3, 0x1E, 0x0, 0x0, 0x0)

    label("loc_17D0")

    Jump("loc_1814")

    label("loc_17D5")

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

    label("loc_1814")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_1604 end

    def Function_9_1820(): pass

    label("Function_9_1820")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_191C")
    Sound(14, 0, 100, 0)
    OP_74(0x4, 0x1E)
    OP_71(0x4, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1FD, 1)"), scpexpr(EXPR_END)), "loc_18A5")
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
    SetScenarioFlags(0x1F3, 0)
    OP_E0(0x5, 0x0)
    Jump("loc_1917")

    label("loc_18A5")

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
    OP_71(0x4, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1917")

    Jump("loc_1966")

    label("loc_191C")

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

    label("loc_1966")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_9_1820 end

    def Function_10_1972(): pass

    label("Function_10_1972")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_197F")

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
            "Quit\x01",                 # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A5F")

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
    Jump("loc_1BAD")

    label("loc_1A5F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A73")
    Jump("loc_1BAD")

    label("loc_1A73")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BAD")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B3D")

    ChrTalk(
        0x8,
        (
            "#10108FWho would've thought the\x01",
            ""Society" was involved...\x02\x03",
            "#10103FBut, why in such a place...?\x02\x03",
            "#10101FWhat could they possibly\x01",
            "be scheming in Crossbell?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1BAD")

    label("loc_1B3D")


    ChrTalk(
        0x8,
        (
            "#10103FWhy the "Society" is in such a place...?\x02\x03",
            "#10101FWhat could they possibly\x01",
            "be scheming in Crossbell?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BAD")

    Jump("loc_197F")

    label("loc_1BB2")

    TalkEnd(0xFE)
    Return()

    # Function_10_1972 end

    def Function_11_1BB6(): pass

    label("Function_11_1BB6")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1BC3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1EB2")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C9E")

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
    Jump("loc_1EAD")

    label("loc_1C9E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1CB2")
    Jump("loc_1EAD")

    label("loc_1CB2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1EAD")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E29")

    ChrTalk(
        0x9,
        "#10303FGirls in knight outfits, eh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#00705FWazy Hemisphere...\x01",
            "Do you have any idea?\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#10304FHu hu, no...\x01",
            "I was thinking what persons could they be to\x01",
            "be able to defeat some very skilled Bracers.\x02\x03",
            "#10302FThe enemy is "Ouroboros".\x01",
            "Shouldn't you be\x01",
            "careful too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#00700F...Hmph, yours is a needless worry.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1EAD")

    label("loc_1E29")


    ChrTalk(
        0x9,
        (
            "#10303FGirls in knight outfits...\x02\x03",
            "#10300FWhat persons could they be to be able to\x01",
            "defeat some very skilled Bracers, I wonder.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EAD")

    Jump("loc_1BC3")

    label("loc_1EB2")

    TalkEnd(0xFE)
    Return()

    # Function_11_1BB6 end

    def Function_12_1EB6(): pass

    label("Function_12_1EB6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FAB")

    ChrTalk(
        0xFE,
        (
            "When she sees a strong opponent,\x01",
            "Ling goes out of control.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If she tried to fight seriously against\x01",
            "those girls dressed like knights,\x01",
            "she won't be unscathed for sure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I beg you, please find\x01",
            "her immediately...!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_201B")

    label("loc_1FAB")


    ChrTalk(
        0xFE,
        (
            "When she sees a strong opponent,\x01",
            "Ling goes out of control.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I beg you, please find\x01",
            "her immediately...!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_201B")

    TalkEnd(0xFE)
    Return()

    # Function_12_1EB6 end

    def Function_13_201F(): pass

    label("Function_13_201F")


    def lambda_2024():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2024)

    def lambda_2031():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2031)

    def lambda_203E():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_203E)

    def lambda_204B():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_204B)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2070")

    def lambda_2068():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_2068)

    label("loc_2070")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_208D")

    def lambda_2085():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_2085)

    label("loc_208D")


    def lambda_2092():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_2092)

    def lambda_209F():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_209F)
    Return()

    # Function_13_201F end

    def Function_14_20A8(): pass

    label("Function_14_20A8")

    EventBegin(0x0)
    LoadChrToIndex("apl/ch51448.itc", 0x1E)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_20C4")
    OP_CF(0x1, 0xF4, 0x8)

    label("loc_20C4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_20D8")
    OP_CF(0x1, 0xF4, 0x4)

    label("loc_20D8")

    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 33000, 0, -7000, 180)
    SetChrChipByIndex(0xA, 0x3)
    SetChrSubChip(0xA, 0x3)
    ClearChrFlags(0xA, 0x1000)
    ClearChrFlags(0xA, 0x20)
    ClearChrFlags(0xA, 0x2)
    ClearChrBattleFlags(0xA, 0x4)
    PlayEffect(0x9, 0x7, 0xA, 0x5, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    BeginChrThread(0x0, 3, 0, 13)
    OP_63(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2195")

    ChrTalk(
        0x101,
        "#00007F#11PThat's...!\x02",
    )

    CloseMessageWindow()
    Jump("loc_22A3")

    label("loc_2195")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_21BF")

    ChrTalk(
        0x102,
        "#00101F#11PAh...!\x02",
    )

    CloseMessageWindow()
    Jump("loc_22A3")

    label("loc_21BF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_21F3")

    ChrTalk(
        0x103,
        "#00201F#11PThere she is...!\x02",
    )

    CloseMessageWindow()
    Jump("loc_22A3")

    label("loc_21F3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_221F")

    ChrTalk(
        0x104,
        "#00307F#11POoh...!?\x02",
    )

    CloseMessageWindow()
    Jump("loc_22A3")

    label("loc_221F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_224A")

    ChrTalk(
        0x109,
        "#10101F#11PAh...!?\x02",
    )

    CloseMessageWindow()
    Jump("loc_22A3")

    label("loc_224A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2275")

    ChrTalk(
        0x105,
        "#10305F#11PWhoa...\x02",
    )

    CloseMessageWindow()
    Jump("loc_22A3")

    label("loc_2275")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_22A3")

    ChrTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#00700F#11P...Mm......\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22A3")

    OP_68(33030, 1200, -6930, 2500)
    MoveCamera(45, 22, 0, 2500)
    OP_6E(650, 2500)
    SetCameraDistance(17000, 2500)
    OP_6F(0x79)
    Sleep(1000)
    Fade(500)
    SetChrPos(0x101, 46800, 0, -11200, 270)
    SetChrPos(0x102, 46600, 0, -12600, 270)
    SetChrPos(0x103, 48200, 0, -12800, 270)
    SetChrPos(0x104, 48200, 0, -11000, 270)
    SetChrPos(0xF4, 49600, 0, -11200, 270)
    SetChrPos(0x106, 50000, 0, -12600, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_68(33570, 1200, -7790, 0)
    MoveCamera(335, 28, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(14500, 0)
    SetCameraDistance(13200, 2500)

    def lambda_2391():
        OP_9B(0x0, 0x101, 0x13, 0x314C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2391)
    Sleep(0)

    def lambda_23A9():
        OP_9B(0x0, 0x102, 0x13, 0x314C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_23A9)
    Sleep(0)

    def lambda_23C1():
        OP_9B(0x0, 0x103, 0x13, 0x314C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_23C1)
    Sleep(0)

    def lambda_23D9():
        OP_9B(0x0, 0x104, 0x13, 0x314C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_23D9)
    Sleep(0)

    def lambda_23F1():
        OP_9B(0x0, 0xF4, 0x13, 0x314C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_23F1)
    Sleep(0)

    def lambda_2409():
        OP_9B(0x0, 0x106, 0x13, 0x314C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_2409)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0x106, 0)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x104,
        "#00301F#12PIsn't that Miss Eolia...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00010F#12PH-However, this...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00201F#12PA thorny ivy...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#00700F#12P#NHm, it looks like a different\x01",
            "plant than "Pleroma Grass"...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        "#00107F#6PA-Anyway, let's tend to her!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_68(35220, 1000, -8280, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(15000, 0)
    SetChrPos(0x101, 36000, 0, -9100, 315)
    SetChrPos(0x102, 34600, 0, -9650, 0)
    SetChrPos(0x103, 35400, 0, -10800, 0)
    SetChrPos(0xF4, 36800, 0, -7650, 270)
    SetChrPos(0x106, 38300, 0, -8390, 270)
    SetChrPos(0xA, 35000, 0, -8000, 180)
    SetChrChipByIndex(0x104, 0x1E)
    SetChrSubChip(0x104, 0x0)
    SetChrPos(0x104, 35170, 100, -6830, 180)
    SetChrFlags(0x104, 0x1000)
    SetChrFlags(0x104, 0x20)
    SetChrFlags(0x104, 0x2)
    SetChrChipByIndex(0xA, 0x4)
    SetChrSubChip(0xA, 0x0)
    SetChrFlags(0xA, 0x1000)
    SetChrFlags(0xA, 0x20)
    SetChrFlags(0xA, 0x2)
    StopEffect(0x7, 0x0)
    SetCameraDistance(14000, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0xA,
        "#5P#50W...Hmmm......\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2662")

    ChrTalk(
        0x109,
        "#10100F#11PAh...\x02",
    )

    CloseMessageWindow()
    Jump("loc_267A")

    label("loc_2662")


    ChrTalk(
        0x105,
        "#10302F#11POops...\x02",
    )

    CloseMessageWindow()

    label("loc_267A")


    ChrTalk(
        0x104,
        "#00300F#5PLooks like she came to.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00106F#12P*phew*...thank goodness.\x02",
    )

    CloseMessageWindow()
    Sound(812, 0, 70, 0)
    SetChrSubChip(0xA, 0x1)
    Sleep(200)
    OP_63(0xA, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xA)

    ChrTalk(
        0xA,
        "#5P#30W...Where am I...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5P#30WSince little Tio is here, could it\x01",
            "be heaven or something similar...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00211F#12POf course not.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#11P...Since you can crack a joke it seems\x01",
            "you completely regained your senses, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5P#30WYes, my body feels a\x01",
            "little weak, though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5P#30W...Did you come because you\x01",
            "were asked by Mr. Michel?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00101F#12PYes, actually...\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd and the others briefly explained to\x01",
            "Eolia the details about why they came there.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xA,
        "#5P#30WIs that so...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5P#30W...Ling and I followed a lead\x01",
            "about Cryptids and the Azure\x01",
            "Flowers and we arrived here...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5P#30WWhile investigating, we ended up\x01",
            "encountering a troublesome opponent...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00013F#11PA troublesome opponent...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A16")

    ChrTalk(
        0x109,
        "#10101F#11PA Cryptid, right?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2A3F")

    label("loc_2A16")


    ChrTalk(
        0x105,
        "#10301F#11PIt was a Cryptid, right?\x02",
    )

    CloseMessageWindow()

    label("loc_2A3F")


    ChrTalk(
        0xA,
        "#5P#30WNo...a human.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5P#30W...Probably from\x01",
            ""Ouroboros".\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00007F#11PWha...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108F#12PT-The one we heard about at the studio...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5P#30WVery skilled girls dressed like Middle\x01",
            "Ages knights accompanied her...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5P#30WWe used all our might just\x01",
            "to fight those girls...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#00700F#11PGirls dressed in armor...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2C6B")

    ChrTalk(
        0x109,
        "#10108F#11PW-Who could they be?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2C8D")

    label("loc_2C6B")


    ChrTalk(
        0x105,
        "#10308F#11P(...Them, eh...?)\x02",
    )

    CloseMessageWindow()

    label("loc_2C8D")


    ChrTalk(
        0xA,
        (
            "#5P#30W...While we were fighting, I\x01",
            "was separated from Ling...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5P#30WI was restrained by a\x01",
            ""fool" boy or something...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5P#30WSo I couldn't move due\x01",
            "to that ivy like things...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00310F#5PHe restrained you and left like that...?\x01",
            "What a maniac bastard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00206F#12PMr. Randy, that is not the problem.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#11P...I understand.\x02\x03",
            "#00001FWe'll be proceeding to confirm\x01",
            "Miss Ling's safety now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101F#12PWe will ask our member on\x01",
            "standby to come here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#5P#30WThank you...very much.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#5P#30W...I leave Ling to you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5P#30WWhen she sees a strong opponent,\x01",
            "she goes out of control...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#11P...Understood.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F77")

    ChrTalk(
        0x109,
        (
            "#10107F#11PIt seems we need to find\x01",
            "her as soon as possible...!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FB6")

    label("loc_2F77")


    ChrTalk(
        0x105,
        (
            "#10301F#11PWell, it appears we don't\x01",
            "have time to dawdle.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FB6")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(300)
    SetMessageWindowPos(-1, -1, -1, -1)
    Sound(814, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The member on standby was\x01",
            "informed and called here.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    ClearChrFlags(0xA, 0x8000)
    SetChrPos(0x0, 35100, 0, -7890, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3073")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 39620, 0, -6770, 270)
    Jump("loc_3089")

    label("loc_3073")

    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 39620, 0, -6770, 270)

    label("loc_3089")

    SetScenarioFlags(0x165, 3)
    OP_29(0xA9, 0x1, 0x5)
    ModifyEventFlags(0, 0, 0x80)
    SetChrPos(0xA, 38890, 0, -5780, 180)
    ClearChrFlags(0xA, 0x1000)
    ClearChrFlags(0xA, 0x20)
    ClearChrFlags(0xA, 0x2)
    SetChrChipByIndex(0xA, 0x2)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    ClearChrFlags(0x104, 0x1000)
    ClearChrFlags(0x104, 0x20)
    ClearChrFlags(0x104, 0x2)
    OP_37()
    EventEnd(0x5)
    Return()

    # Function_14_20A8 end

    SaveToFile()

Try(main)
