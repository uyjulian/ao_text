from ScenarioHelper import *

def main():
    CreateScenaFile(
        "r3060.bin",                # FileName
        "r3060",                    # MapName
        "r3060",                    # Location
        0x0065,                     # MapIndex
        "ed7203",
        0x00000000,                 # Flags
        ("r3060", "r0000_1", "", "", "", ""),   # include
        0x01,                       # PlaceNameNumber
        0x17,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 101, 0, 1, 0, 2],
    )

    BuildStringList((
        "r3060",                  # 0
        "Tsao",                 # 1
        "Row",                   # 2
        "Black moon member",             # 3
        "Black moon member",             # 4
        "Black moon member",             # 5
        "Black moon member",             # 6
        "Black moon member",             # 7
        "Black moon member",             # 8
        "Black moon member",             # 9
        "Lisha",               # 10
        "Odorondo",           # 11
        "br3000",                 # 12
        "br3000",                 # 13
        "br3000",                 # 14
        "br3000",                 # 15
        "br3000",                 # 16
        "br3000",                 # 17
        "Direction to Almorica Kodo",     # 18
    ))

    ATBonus("ATBonus_540", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_4BFD", 8,   14,  0,   10,  4,   2,   0)
    Sepith("Sepith_4C05", 0,   0,   6,   14,  6,   6,   6)
    Sepith("Sepith_4C15", 8,   8,   8,   8,   8,   8,   8)
    Sepith("Sepith_4C0D", 8,   6,   3,   0,   7,   7,   7)
    Sepith("Sepith_4C25", 10,  10,  10,  10,  3,   3,   3)

    MonsterBattlePostion("MonsterBattlePostion_5A0", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_5A4", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_5A8", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_5AC", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_5B0", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_5B4", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_5B8", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_5BC", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_600", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_604", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_608", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_60C", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_610", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_614", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_618", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_61C", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_580", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_584", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_588", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_58C", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_590", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_594", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_598", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_59C", 2, 13, 180)

    # monster count: 20

    BattleInfo(
        "BattleInfo_878", 0x0000, 73, 6, 60, 8, 1, 20, 0, "br3000", "Sepith_4BFD", 30, 30, 20, 20,
        (
            ("ms69500.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_5A0", "MonsterBattlePostion_600", "ed7450", "ed7453", "ATBonus_540"),
            ("ms69500.dat", "ms69500.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_580", "MonsterBattlePostion_600", "ed7450", "ed7453", "ATBonus_540"),
            ("ms69500.dat", "ms63400.dat", "ms69500.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_5A0", "MonsterBattlePostion_600", "ed7450", "ed7453", "ATBonus_540"),
            ("ms69500.dat", "ms64100.dat", "ms64100.dat", "ms64100.dat", 0, 0, 0, 0, "MonsterBattlePostion_580", "MonsterBattlePostion_600", "ed7450", "ed7453", "ATBonus_540"),
        )
    )

    BattleInfo(
        "BattleInfo_7B0", 0x0000, 73, 6, 60, 8, 1, 40, 0, "br3000", "Sepith_4C05", 30, 40, 20, 10,
        (
            ("ms63400.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_5A0", "MonsterBattlePostion_600", "ed7450", "ed7453", "ATBonus_540"),
            ("ms63400.dat", "ms63400.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_580", "MonsterBattlePostion_600", "ed7450", "ed7453", "ATBonus_540"),
            ("ms63400.dat", "ms63400.dat", "ms63400.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_5A0", "MonsterBattlePostion_600", "ed7450", "ed7453", "ATBonus_540"),
            ("ms63400.dat", "ms63400.dat", "ms63400.dat", "ms63400.dat", 0, 0, 0, 0, "MonsterBattlePostion_580", "MonsterBattlePostion_600", "ed7450", "ed7453", "ATBonus_540"),
        )
    )

    BattleInfo(
        "BattleInfo_620", 0x0000, 73, 6, 60, 8, 1, 40, 0, "br3000", "Sepith_4C15", 30, 40, 20, 10,
        (
            ("ms66800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_5A0", "MonsterBattlePostion_600", "ed7450", "ed7453", "ATBonus_540"),
            ("ms66800.dat", "ms66800.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_580", "MonsterBattlePostion_600", "ed7450", "ed7453", "ATBonus_540"),
            ("ms66800.dat", "ms69500.dat", "ms66800.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_5A0", "MonsterBattlePostion_600", "ed7450", "ed7453", "ATBonus_540"),
            ("ms66800.dat", "ms69500.dat", "ms66800.dat", "ms69500.dat", 0, 0, 0, 0, "MonsterBattlePostion_580", "MonsterBattlePostion_600", "ed7450", "ed7453", "ATBonus_540"),
        )
    )

    BattleInfo(
        "BattleInfo_6E8", 0x0000, 73, 6, 60, 8, 1, 10, 0, "br3000", "Sepith_4C0D", 30, 40, 20, 10,
        (
            ("ms63500.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_5A0", "MonsterBattlePostion_600", "ed7450", "ed7453", "ATBonus_540"),
            ("ms63500.dat", "ms63500.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_580", "MonsterBattlePostion_600", "ed7450", "ed7453", "ATBonus_540"),
            ("ms63500.dat", "ms63400.dat", "ms63500.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_5A0", "MonsterBattlePostion_600", "ed7450", "ed7453", "ATBonus_540"),
            ("ms63500.dat", "ms63500.dat", "ms63400.dat", "ms63500.dat", 0, 0, 0, 0, "MonsterBattlePostion_580", "MonsterBattlePostion_600", "ed7450", "ed7453", "ATBonus_540"),
        )
    )

    BattleInfo(
        "BattleInfo_940", 0x0000, 73, 6, 60, 8, 1, 60, 0, "br3000", "Sepith_4C25", 30, 40, 20, 10,
        (
            ("ms75600.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_5A0", "MonsterBattlePostion_600", "ed7450", "ed7453", "ATBonus_540"),
            ("ms75600.dat", "ms75600.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_580", "MonsterBattlePostion_600", "ed7450", "ed7453", "ATBonus_540"),
            ("ms75600.dat", "ms75600.dat", "ms75600.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_5A0", "MonsterBattlePostion_600", "ed7450", "ed7453", "ATBonus_540"),
            ("ms75600.dat", "ms75600.dat", "ms75600.dat", "ms75600.dat", 0, 0, 0, 0, "MonsterBattlePostion_580", "MonsterBattlePostion_600", "ed7450", "ed7453", "ATBonus_540"),
        )
    )

    # event battle count: 1

    BattleInfo(
        "BattleInfo_A08", 0x0C00, 255, 6, 0, 0, 3, 0, 0, "br3000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms63400.dat", "ms63400.dat", "ms63400.dat", "ms63400.dat", "ms63400.dat", "ms63400.dat", "ms63400.dat", "ms63400.dat", "MonsterBattlePostion_5A0", "MonsterBattlePostion_600", "ed7451", "ed7453", "ATBonus_540"),
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
        "monster/ch66850.itc",               # 10
        "monster/ch66851.itc",               # 11
        "monster/ch63550.itc",               # 12
        "monster/ch63550.itc",               # 13
        "monster/ch63450.itc",               # 14
        "monster/ch63450.itc",               # 15
        "monster/ch69550.itc",               # 16
        "monster/ch69550.itc",               # 17
        "monster/ch75650.itc",               # 18
        "monster/ch75651.itc",               # 19
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(4294933377, 4294965897, 2369,    0,    484,  0x0, 0,   20,  0,   0,   0,   255, 255, 255,  0)

    DeclMonster(4294918716, 33400,   4294965296, 0x1010000,    "BattleInfo_878", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(4294906296, 11790,   4294965296, 0x1010000,    "BattleInfo_7B0", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(4294958126, 4294956036, 6000,    0x1010000,    "BattleInfo_620", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(990,     4294965526, 6000,    0x1010000,    "BattleInfo_6E8", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(12630,   4294937686, 6000,    0x1010000,    "BattleInfo_7B0", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(24750,   4294934696, 6000,    0x1010000,    "BattleInfo_878", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(46240,   4294954576, 6000,    0x1010000,    "BattleInfo_620", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(4294955626, 20490,   6000,    0x1010000,    "BattleInfo_7B0", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(25610,   11790,   14000,   0x1010000,    "BattleInfo_6E8", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(51790,   19370,   14000,   0x1010000,    "BattleInfo_878", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(4294918716, 33400,   4294965296, 0x1010000,    "BattleInfo_940", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(4294906296, 11790,   4294965296, 0x1010000,    "BattleInfo_940", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(4294958126, 4294956036, 6000,    0x1010000,    "BattleInfo_940", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(990,     4294965526, 6000,    0x1010000,    "BattleInfo_940", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(12630,   4294937686, 6000,    0x1010000,    "BattleInfo_940", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(24750,   4294934696, 6000,    0x1010000,    "BattleInfo_940", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(46240,   4294954576, 6000,    0x1010000,    "BattleInfo_940", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(4294955626, 20490,   6000,    0x1010000,    "BattleInfo_940", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(25610,   11790,   14000,   0x1010000,    "BattleInfo_940", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(51790,   19370,   14000,   0x1010000,    "BattleInfo_940", 0,   24,  0xFFFF, 8,  9)

    DeclActor(39430,   14100,   1210,    1200,    39430,   15100,   1210,    0x007C, 0,  3,  0x0000)
    DeclActor(4294933376, 4294965396, 2370,    1200,    4294933376, 4294966396, 2370,    0x007C, 0,  4,  0x0000)
    DeclActor(50000,   6100,    4294957296, 1200,    50000,   7100,    4294957296, 0x007C, 0,  5,  0x0000)

    PlaceName(-84.0, 0.0, 48.0, 0x0000, 0x0000, "Direction to Almorica Kodo")

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 0
    ChipFrameInfo(1500, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 2
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 3
    ChipFrameInfo(1000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 4
    ChipFrameInfo(1500, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 5
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 6
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4])                      # 7
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 8
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 9

    ScpFunction((
        "Function_0_B08",          # 00, 0
        "Function_1_B27",          # 01, 1
        "Function_2_BDC",          # 02, 2
        "Function_3_1935",         # 03, 3
        "Function_4_1A86",         # 04, 4
        "Function_5_1C9D",         # 05, 5
        "Function_6_1DEE",         # 06, 6
        "Function_7_1DF2",         # 07, 7
        "Function_8_4446",         # 08, 8
        "Function_9_4485",         # 09, 9
        "Function_10_44C4",        # 0A, 10
        "Function_11_4503",        # 0B, 11
        "Function_12_4542",        # 0C, 12
        "Function_13_4581",        # 0D, 13
        "Function_14_45C0",        # 0E, 14
        "Function_15_45FF",        # 0F, 15
        "Function_16_4B91",        # 10, 16
    ))


    def Function_0_B08(): pass

    label("Function_0_B08")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B26")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x3, 0x4, 0x3)
    Jump("Function_0_B08")

    label("loc_B26")

    Return()

    # Function_0_B08 end

    def Function_1_B27(): pass

    label("Function_1_B27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_B3E")
    ClearScenarioFlags(0x22, 0)
    SetScenarioFlags(0x0, 0)
    Event(0, 7)
    Jump("loc_B4D")

    label("loc_B3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_B4D")
    ClearScenarioFlags(0x22, 1)
    Event(0, 15)

    label("loc_B4D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_2A(0x91, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x91, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x91, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BA9")
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1C, 0x80)
    Jump("loc_BDB")

    label("loc_BA9")

    SetChrFlags(0x1D, 0x80)
    SetChrFlags(0x1E, 0x80)
    SetChrFlags(0x1F, 0x80)
    SetChrFlags(0x20, 0x80)
    SetChrFlags(0x21, 0x80)
    SetChrFlags(0x22, 0x80)
    SetChrFlags(0x23, 0x80)
    SetChrFlags(0x24, 0x80)
    SetChrFlags(0x25, 0x80)
    SetChrFlags(0x26, 0x80)

    label("loc_BDB")

    Return()

    # Function_1_B27 end

    def Function_2_BDC(): pass

    label("Function_2_BDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_BF1")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 0)

    label("loc_BF1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_CD8")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x190, 0x0)
    ClearMapObjFlags(0x4, 0x4)
    ClearMapObjFlags(0x5, 0x4)
    ClearMapObjFlags(0x6, 0x4)
    ClearMapObjFlags(0x7, 0x4)
    ClearMapObjFlags(0x8, 0x4)
    ClearMapObjFlags(0x9, 0x4)
    ClearMapObjFlags(0xA, 0x4)
    ClearMapObjFlags(0xB, 0x4)
    ClearMapObjFlags(0xC, 0x4)
    ClearMapObjFlags(0xD, 0x4)
    ClearMapObjFlags(0xE, 0x4)
    ClearMapObjFlags(0xF, 0x4)
    ClearMapObjFlags(0x10, 0x4)
    ClearMapObjFlags(0x11, 0x4)
    ClearMapObjFlags(0x12, 0x4)
    ClearMapObjFlags(0x13, 0x4)
    ClearMapObjFlags(0x14, 0x4)
    ClearMapObjFlags(0x15, 0x4)
    ClearMapObjFlags(0x16, 0x4)
    ClearMapObjFlags(0x17, 0x4)
    ClearMapObjFlags(0x18, 0x4)
    ClearMapObjFlags(0x19, 0x4)
    ClearMapObjFlags(0x1A, 0x4)
    ClearMapObjFlags(0x1B, 0x4)
    ClearMapObjFlags(0x1C, 0x4)
    ClearMapObjFlags(0x1D, 0x4)
    ClearMapObjFlags(0x1E, 0x4)
    ClearMapObjFlags(0x1F, 0x4)
    ClearMapObjFlags(0x20, 0x4)
    ClearMapObjFlags(0x21, 0x4)
    ClearMapObjFlags(0x22, 0x4)
    ClearMapObjFlags(0x23, 0x4)
    Jump("loc_D98")

    label("loc_CD8")

    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xB, 0x4)
    SetMapObjFlags(0xC, 0x4)
    SetMapObjFlags(0xD, 0x4)
    SetMapObjFlags(0xE, 0x4)
    SetMapObjFlags(0xF, 0x4)
    SetMapObjFlags(0x10, 0x4)
    SetMapObjFlags(0x11, 0x4)
    SetMapObjFlags(0x12, 0x4)
    SetMapObjFlags(0x13, 0x4)
    SetMapObjFlags(0x14, 0x4)
    SetMapObjFlags(0x15, 0x4)
    SetMapObjFlags(0x16, 0x4)
    SetMapObjFlags(0x17, 0x4)
    SetMapObjFlags(0x18, 0x4)
    SetMapObjFlags(0x19, 0x4)
    SetMapObjFlags(0x1A, 0x4)
    SetMapObjFlags(0x1B, 0x4)
    SetMapObjFlags(0x1C, 0x4)
    SetMapObjFlags(0x1D, 0x4)
    SetMapObjFlags(0x1E, 0x4)
    SetMapObjFlags(0x1F, 0x4)
    SetMapObjFlags(0x20, 0x4)
    SetMapObjFlags(0x21, 0x4)
    SetMapObjFlags(0x22, 0x4)
    SetMapObjFlags(0x23, 0x4)

    label("loc_D98")

    OP_52(0x15, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F4, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18CC")
    OP_70(0x0, 0x0)
    Jump("loc_18D0")

    label("loc_18CC")

    OP_70(0x0, 0x1E)

    label("loc_18D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F4, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18E3")
    OP_70(0x1, 0x0)
    Jump("loc_18E7")

    label("loc_18E3")

    OP_70(0x1, 0x1E)

    label("loc_18E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18FA")
    OP_70(0x2, 0x0)
    Jump("loc_18FE")

    label("loc_18FA")

    OP_70(0x2, 0x1E)

    label("loc_18FE")

    OP_1C(0x0, 0x24, 0x0, 0x32, 0x0, 0x6, 0x0, 0x0)
    OP_1C(0x0, 0x25, 0x0, 0x32, 0x0, 0x6, 0x0, 0x0)
    OP_1C(0x0, 0x26, 0x0, 0x32, 0x0, 0x6, 0x0, 0x0)
    LoadEffect(0x10, "event\\eva00_00.eff")
    Return()

    # Function_2_BDC end

    def Function_3_1935(): pass

    label("Function_3_1935")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F4, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A35")
    Sound(14, 0, 100, 0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('ＥＰ填充剂Ⅲ', 1)"), scpexpr(EXPR_END)), "loc_19BE")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 'ＥＰ填充剂Ⅲ'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1F4, 4)
    OP_E0(0x5, 0x0)
    Jump("loc_1A30")

    label("loc_19BE")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            "In the treasure box",
            scpstr(SCPSTR_CODE_ITEM, 'ＥＰ填充剂Ⅲ'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Is contained.\x01",
            "Because my belongings are full,",
            scpstr(SCPSTR_CODE_ITEM, 'ＥＰ填充剂Ⅲ'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I gave up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x0, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1A30")

    Jump("loc_1A7A")

    label("loc_1A35")

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

    label("loc_1A7A")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_1935 end

    def Function_4_1A86(): pass

    label("Function_4_1A86")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F4, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C57")
    Sound(14, 0, 100, 0)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x217, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B85")
    OP_A7(0x12, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0x12, 0x0, 0)
    OP_98(0x12, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_1AE3():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1AE3)

    def lambda_1AFD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_1AFD)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8000)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A monster appeared!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    WaitChrThread(0x12, 1)
    Battle("BattleInfo_A08", 0x0, 0x0, 0x0, 0xB, 0xFF)
    SetChrFlags(0x12, 0x80)
    ClearChrFlags(0x12, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_1B66"),
        (2, "loc_1B75"),
        (1, "loc_1B82"),
        (SWITCH_DEFAULT, "loc_1B85"),
    )


    label("loc_1B66")

    SetScenarioFlags(0x217, 5)
    OP_70(0x1, 0x1E)
    Sleep(500)
    Jump("loc_1B85")

    label("loc_1B75")

    OP_70(0x1, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_1B82")

    OP_B9(0x0)
    Return()

    label("loc_1B85")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('ＥＰ３', 1)"), scpexpr(EXPR_END)), "loc_1BE2")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 'ＥＰ３'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1F4, 5)
    OP_E0(0x5, 0x0)
    Jump("loc_1C52")

    label("loc_1BE2")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0x3E7,
        (
            "In the treasure box",
            scpstr(SCPSTR_CODE_ITEM, 'ＥＰ３'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Is contained.\x01",
            "Because my belongings are full,",
            scpstr(SCPSTR_CODE_ITEM, 'ＥＰ３'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I gave up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x1, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1C52")

    Jump("loc_1C91")

    label("loc_1C57")

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

    label("loc_1C91")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_1A86 end

    def Function_5_1C9D(): pass

    label("Function_5_1C9D")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D9D")
    Sound(14, 0, 100, 0)
    OP_74(0x2, 0x1E)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('骑士护腿', 1)"), scpexpr(EXPR_END)), "loc_1D26")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '骑士护腿'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1F4, 6)
    OP_E0(0x5, 0x0)
    Jump("loc_1D98")

    label("loc_1D26")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            "In the treasure box",
            scpstr(SCPSTR_CODE_ITEM, '骑士护腿'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Is contained.\x01",
            "Because my belongings are full,",
            scpstr(SCPSTR_CODE_ITEM, '骑士护腿'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I gave up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x2, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1D98")

    Jump("loc_1DE2")

    label("loc_1D9D")

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

    label("loc_1DE2")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_1C9D end

    def Function_6_1DEE(): pass

    label("Function_6_1DEE")

    Call(1, 6)
    Return()

    # Function_6_1DEE end

    def Function_7_1DF2(): pass

    label("Function_7_1DF2")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    LoadChrToIndex("chr/ch06300.itc", 0x1E)
    LoadChrToIndex("chr/ch31400.itc", 0x1F)
    LoadChrToIndex("chr/ch31500.itc", 0x20)
    LoadChrToIndex("chr/ch12500.itc", 0x21)
    LoadChrToIndex("apl/ch51705.itc", 0x22)
    LoadChrToIndex("apl/ch50237.itc", 0x23)
    SoundLoad(3272)
    SoundLoad(3273)
    SoundLoad(3274)
    SoundLoad(3256)
    SoundLoad(3257)
    SoundLoad(3258)
    SoundLoad(3259)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis283.itp")
    SetChrSubChip(0x107, 0x5)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrChipByIndex(0xA, 0x20)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrChipByIndex(0xB, 0x21)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrChipByIndex(0xC, 0x20)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrChipByIndex(0xD, 0x21)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    SetChrChipByIndex(0xE, 0x20)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)
    SetChrChipByIndex(0xF, 0x21)
    SetChrSubChip(0xF, 0x0)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8000)
    SetChrChipByIndex(0x10, 0x20)
    SetChrSubChip(0x10, 0x0)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x8000)
    SetMapObjFlags(0x26, 0x4)
    SetChrPos(0xA, 64000, 14000, 7400, 90)
    SetChrPos(0xB, 61500, 14000, 6900, 90)
    SetChrPos(0xC, 61000, 14000, 7900, 90)
    SetChrPos(0xD, 59000, 14000, 7400, 90)
    SetChrPos(0xE, 57000, 14000, 7900, 90)
    SetChrPos(0xF, 56000, 14000, 6900, 90)
    SetChrPos(0x10, 54500, 14000, 7200, 90)
    OP_68(90290, 21000, 26800, 0)
    MoveCamera(78, 8, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(20000, 0)
    OP_68(68650, 16250, 7000, 10000)
    MoveCamera(90, 20, 0, 10000)
    OP_6E(510, 10000)
    SetCameraDistance(30000, 10000)
    PlayBGM("ed7563", 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(4000)
    BeginChrThread(0xA, 1, 0, 8)
    BeginChrThread(0xB, 1, 0, 9)
    BeginChrThread(0xC, 1, 0, 10)
    BeginChrThread(0xD, 1, 0, 11)
    BeginChrThread(0xE, 1, 0, 12)
    BeginChrThread(0xF, 1, 0, 13)
    BeginChrThread(0x10, 1, 0, 14)
    OP_6F(0x79)
    Fade(500)
    EndChrThread(0xA, 0x1)
    EndChrThread(0xB, 0x1)
    EndChrThread(0xC, 0x1)
    EndChrThread(0xD, 0x1)
    EndChrThread(0xE, 0x1)
    EndChrThread(0xF, 0x1)
    EndChrThread(0x10, 0x1)
    SetChrPos(0x101, 48000, 14000, 20000, 45)
    SetChrPos(0x103, 47250, 14000, 19000, 45)
    SetChrPos(0x105, 48750, 14000, 19000, 0)
    SetChrPos(0x107, 48000, 14000, 17500, 0)
    SetChrPos(0x106, 48000, 14000, 23300, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x8, 50000, 14000, 22100, 225)
    SetChrPos(0x9, 51000, 14000, 21100, 225)
    OP_52(0x101, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x103, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x103, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x103, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x105, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x105, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x105, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x107, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x107, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x107, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x106, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x106, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x106, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(48550, 15000, 21800, 0)
    MoveCamera(50, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(20760, 0)
    SetCameraDistance(19760, 1500)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#00006F#6PI see..\x02\x03",
            "#00001FFrom that attack all the time,\x01",
            "Did you hide around here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#03204F#5PYes, there is a site of the cult,\x01",
            "It is convenient for you to lose yourself.\x02\x03",
            "#03210FA group of \"snakes\", a huge bell\x01",
            "I could observe how to install it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00201F#6PThe place that professor was working?\x02",
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(500)
    SetMessageWindowPos(0, 170, -1, -1)

    AnonymousTalk(
        0x105,
        (
            "#10403FIt was in the central square,\x01",
            "In the ceremony to complete \"Zero no Treasure\"\x01",
            "It's a huge bell you used.\x02\x03",
            "#10401FSome artifacts are\x01",
            "I think that it is no mistake.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)

    ChrTalk(
        0x9,
        (
            "#11PBy the way the bells were removed again,\x01",
            "It seems that it was returned to Cros Bell City.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PCurrently, you are in this area\x01",
            "We can only say \"black moon\".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11P\"Silver#2RIn#\"What should I save?\x02",
    )

    CloseMessageWindow()

    def lambda_2484():
        TurnDirection(0x101, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2484)
    Sleep(50)

    def lambda_2494():
        TurnDirection(0x103, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_2494)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x103, 0)

    def lambda_24AC():
        OP_93(0x8, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_24AC)
    Sleep(50)

    def lambda_24BC():
        OP_93(0x9, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_24BC)
    Sleep(50)
    WaitChrThread(0x8, 0)
    WaitChrThread(0x9, 0)

    ChrTalk(
        0x106,
        "#10708F#11P….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008F#12PRixia…\x02",
    )

    CloseMessageWindow()
    OP_63(0x106, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x106)
    TurnDirection(0x106, 0x101, 500)
    Fade(250)
    SetChrFlags(0x106, 0x2)
    SetChrChipByIndex(0x106, 0x22)
    SetChrSubChip(0x106, 0x3)
    OP_0D()
    Sleep(150)

    ChrTalk(
        0x106,
        (
            "#10706F#5P…… Lloyd.\x01",
            "Please do not miss it now.\x02\x03",
            "#10708FI went there this neighborhood\x01",
            "Numerous illegal activities …\x02\x03",
            "#10711FI can not be caught,\x01",
            "At the very least not to disturb you any more\x01",
            "I am going to return to Cal bird.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_A0(0x106, 1500, 0x3, 0x5)
    Sleep(300)

    ChrTalk(
        0x106,
        "#10703F#5POnce I accomplish what I must do\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x103,
        "#00208F#12PThat is…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#12PRevenge, right?\x02",
    )

    CloseMessageWindow()
    Sleep(50)
    OP_A0(0x106, 1300, 0x5, 0x3)
    Sleep(100)

    ChrTalk(
        0x106,
        "#10708F#5P#30W….\x02",
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x106, 0xFF)
    SetChrSubChip(0x106, 0x0)
    ClearChrFlags(0x106, 0x2)
    OP_93(0x106, 0x0, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x106,
        (
            "#10703F#11P#30WThey are …\x01",
            "I robbed the most important thing.\x02\x03",
            "Everyone's sun ……\x01",
            "Hopeful irreplaceable.\x02\x03",
            "#10708Fnever……\x01",
            "It is not acceptable.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0xE1, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#03204F#5PHuff, I canceled the contract there\x01",
            "I had it again.\x02\x03",
            "#03210FTo a strong enemy \"red constellation\"\x01",
            "To cooperate and compete.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#6PYou shut up\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00003F#12PHey Rixia\x02\x03",
            "#00001FIria was awake by\x01",
            "Do you know?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x106, 0x101, 500)
    Fade(250)
    SetChrFlags(0x106, 0x2)
    SetChrChipByIndex(0x106, 0x22)
    OP_A0(0x106, 1500, 0x7, 0x8)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x106,
        (
            "#10712F#5P#4S!!?\x02\x03",
            "#10707F#3SI-is that true?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00204F#12PYes, immediately after the incident\x01",
            "He seems to have regained consciousness.\x02\x03",
            "#00202FIt's not a good idea … …\x01",
            "It sounds very good.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_A0(0x106, 1200, 0x1B, 0x1C)
    Sleep(200)

    ChrTalk(
        0x106,
        (
            "#10704F#5P#40W…… Oh, goddess#4REidos#Yo\x02\x03",
            "#10710F#40W………Thank you………\x01",
            "I appreciate your mercy … …\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x10E, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#03204F#11PAha, well that's fantastic\x02\x03",
            "#03210FWell heard in a story, unrelated lower part,\x01",
            "It seems that returning to the stage is hopeless.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    OP_A1(0x106, 0x5DC, 0x3, 0x1C, 0x1B, 0x3)
    Sleep(100)

    ChrTalk(
        0x106,
        "#10708F#5PAh…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00013F#6PYou…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10401F#12PThat information was\x01",
            "You seem to have grabbed it, did not you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#03204F#11PYeah, \"Silver#2RIn#The donor is\x01",
            "Because I was saying that I do not want to know.\x02\x03",
            "#03210FSo I did not end up telling her\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x106, 0xA)
    Sleep(150)

    ChrTalk(
        0x106,
        "#10701F#5P…(glare)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11PCao, why would you…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11P─ ─ \"Silver\".\x01",
            "Please do not get me wrong.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PI do not want you to feel depressed,\x01",
            "With care of Mr. Tsao ……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    SetChrSubChip(0x106, 0x3)
    Sleep(300)

    ChrTalk(
        0x106,
        (
            "#10703F#5PNo need for excuses\x02\x03",
            "#10708FBesides, at what I heard\x01",
            "My will will not change.\x02\x03",
            "#10711FAfter attaching my rush … …\x01",
            "I just leave the crossbell land.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11P…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#03204F#11PHuh, as we are\x01",
            "It is a very grateful story.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#03200F#5P── Lloyd's also.\x01",
            "There will be circumstances of each other,\x01",
            "The partners to fight have in common.\x02\x03",
            "#03209FWe are looking forward to cooperating with you.\x01",
            "It is a place you want to connect.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x2D, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        "#00001F#6P….\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00006F#6PYes. That's fine with me\x02\x03",
            "#00000F── However, however.\x01",
            "Girlfriend#4RLisha#I will take over.\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_2FB7():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_2FB7)
    Sleep(0)

    def lambda_2FC7():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_2FC7)
    Sleep(0)

    def lambda_2FD7():
        TurnDirection(0x107, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_2FD7)
    Sleep(0)

    def lambda_2FE7():
        TurnDirection(0x8, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_2FE7)
    Sleep(0)

    def lambda_2FF7():
        TurnDirection(0x9, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_2FF7)
    Sleep(0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x107, 0)
    WaitChrThread(0x8, 0)
    WaitChrThread(0x9, 0)

    ChrTalk(
        0x106,
        "#10705F#5P!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00205F#6PLloyd…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#03201F#5POhh?\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    OP_68(48580, 15000, 22190, 60000)
    MoveCamera(46, 21, 0, 60000)
    SetCameraDistance(18740, 60000)
    PlayBGM("ed7568", 0)
    OP_93(0x101, 0x0, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00001F#12PLisa.\x01",
            "It is a message from Iria.\x02\x03",
            "#00003F\"── For you,\x01",
            "What is the most important thing? \"\x02\x03",
            "\"Before that important thing\x01",
            "Can you go without trying hard? \"\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x106,
        "#10712F#5P#30W…Ah\x02",
    )

    CloseMessageWindow()

    def lambda_318C():
        TurnDirection(0x101, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_318C)
    Sleep(0)

    def lambda_319C():
        TurnDirection(0x103, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_319C)
    Sleep(0)

    def lambda_31AC():
        TurnDirection(0x105, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_31AC)
    Sleep(0)

    def lambda_31BC():
        TurnDirection(0x107, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_31BC)
    Sleep(0)

    def lambda_31CC():
        TurnDirection(0x106, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_31CC)
    Sleep(0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x107, 0)
    WaitChrThread(0x106, 0)

    def lambda_31F0():
        OP_93(0x8, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_31F0)
    Sleep(50)

    def lambda_3200():
        OP_93(0x9, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_3200)
    Sleep(50)
    WaitChrThread(0x8, 0)
    WaitChrThread(0x9, 0)

    ChrTalk(
        0x101,
        (
            "#00003F#12PIria-san is ……\x01",
            "I was not at all.\x02\x03",
            "#00008FWhile feeling anxious at first\x01",
            "I wonder if he is dying\x01",
            "I thought that … ….\x02\x03",
            "#00000FAbsolutely return to the stage ……\x01",
            "I believe it does not seem to doubt.\x02\x03",
            "#00004FMaybe it's too hard\x01",
            "Please understand properly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#10708F#5P#30W….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10406F#12PWell, to be honest, that only belief\x01",
            "I think it is difficult to penetrate … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00204F#12PStill just listening to the story\x01",
            "We have also been encouraged.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#03201F#11P….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#12PIria is so enthusiastic\x01",
            "While aiming for returning to the stage ……\x02\x03",
            "#00001FFor you\x01",
            "What is the most important thing?\x02\x03",
            "Is it revenge against the Red Constellation?\x02\x03",
            "We inherited \"Silver#2RIn#\"Way of?\x02\x03",
            "Or \x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(250)
    SetChrChipByIndex(0x106, 0xFF)
    SetChrSubChip(0x106, 0x0)
    ClearChrFlags(0x106, 0x2)
    OP_0D()
    OP_93(0x106, 0x0, 0x190)

    def lambda_34F3():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_34F3)
    WaitChrThread(0x106, 2)
    Sleep(500)

    def lambda_3513():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_3513)
    WaitChrThread(0x106, 2)
    Sleep(500)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x106,
        (
            "#10708F#3272V#11P#40W#20A………such a…………\x02\x03",
            "#3273V#45AThat's why …\x01",
            "I can not say it.\x02\x03",
            "#10706F#3274V#45A…… I was blooded … …\x01",
            "I have lived in the dark … …\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00006F#12PDon't misunderstand, Rixia\x02\x03",
            "#00013FI, you really, what is important#18R噵 噵 噵 噵 噵 噵 噵 噵 噵#\x01",
            "something#4R噵 噵#I'm asking.\x02\x03",
            "I can not help but do my best …\x01",
            "I can not help seeking your soul\x01",
            "What is important?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x106,
        "#10708F#11P…\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x101, 500)
    Fade(250)
    SetChrFlags(0x106, 0x2)
    SetChrChipByIndex(0x106, 0x22)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0xA)
    SetCameraDistance(16740, 500)
    OP_A0(0x106, 2000, 0xC, 0xE)
    Sleep(300)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x106,
        (
            "#10713F#3256V#4S#5P#30ASuch a thing\x01",
            "It is decided to be alkane shell!\x02",
        )
    )

    OP_6F(0x10)
    OP_82(0xC8, 0x0, 0xBB8, 0x320)
    CloseMessageWindow()
    MoveCamera(42, 21, 0, 12000)
    OP_A0(0x106, 1200, 0xE, 0x13)
    OP_A0(0x106, 1200, 0x13, 0x11)
    Sleep(300)

    ChrTalk(
        0x106,
        (
            "#10714F#3257V#5P#40AI am also ……\x01",
            "That stage#4Rstage#I want to dance!\x02\x03",
            "#3258V#40AIria, Shri-chan,\x01",
            "With everyone in the theater company!\x02\x03",
            "#10713F#3259V#30AThat's all I want\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    SetCameraDistance(17690, 800)
    OP_6F(0x79)
    CancelBlur(0)
    Sleep(300)

    ChrTalk(
        0x103,
        "#00214F#12PAh\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10404F#12PEhe\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002F#12PI see…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#03201F#11P….\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x8)

    ChrTalk(
        0x9,
        "#11PCao\x02",
    )

    CloseMessageWindow()

    def lambda_3929():
        TurnDirection(0x101, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3929)
    Sleep(50)

    def lambda_3939():
        TurnDirection(0x103, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_3939)
    Sleep(50)

    def lambda_3949():
        TurnDirection(0x105, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_3949)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x105, 0)
    OP_A0(0x106, 1500, 0x14, 0x15)
    Sleep(150)

    ChrTalk(
        0x106,
        "#10708F#5P…Ah\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00013F#6P….\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    OP_A0(0x106, 1500, 0x15, 0x17)
    Sleep(150)

    ChrTalk(
        0x8,
        "#03204F#60W#2S#11P#12AEhehAhaha\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    SetCameraDistance(18690, 500)
    OP_82(0x64, 0x0, 0xBB8, 0x3E8)

    ChrTalk(
        0x8,
        "#03209F#4S#11P#15AAHAHAHAHA!!\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    TurnDirection(0x8, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#03210F#5POh that's our Lloyd for you\x02\x03",
            "Brilliant, this setup\x01",
            "Did you mess up?\x02\x03",
            "#03203FNo, in this case,\x01",
            "Should I say that Lady Iria wins … …\x02\x03",
            "#03202FI was killed.\x01",
            "Yeah ─ ─ It has been brilliantly done!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#10708F#5PCao…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#6PI wont give any excuses\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#03202F#5PHuff, indeed, indeed\x01",
            "Intestine#2RHalawata#Although it is boiling down … …\x02\x03",
            "#03204FWell, there are also future cooperation,\x01",
            "Let's leave this time.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x10E, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#03204F#11P\"Silver#2RIn#Tomorrow\x01",
            "No, Lisa Mao.\x02\x03",
            "\"Black moon#4RHayuue#\"Agreement with\x01",
            "Let's quit about this time.\x02\x03",
            "#03200FYou can go anywhere you like\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10712F#5PAh\x02\x03",
            "#10710F…… Mr. Tsao.\x01",
            "Thank you very much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#03210F#11PTo the last this time#4R噵 噵#Is\x01",
            "Because I just gave up.\x02\x03",
            "#03203FI am\x01",
            "How to aim for height as \"black moon\"\x01",
            "I still want your power.\x02\x03",
            "#03210FWell at best, at the least\x01",
            "You might as well step on the stage.\x02",
        )
    )

    CloseMessageWindow()
    OP_A0(0x106, 1200, 0x17, 0x19)
    Sleep(300)

    ChrTalk(
        0x106,
        (
            "#10704F#5P…. Yeah.\x01",
            "I will never give up.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(48720, 15000, 21530, 2000)
    MoveCamera(51, 21, 0, 2000)
    OP_6E(510, 2000)
    SetCameraDistance(19710, 2000)
    StopBGM(0x1770)
    Sleep(500)
    OP_A0(0x106, 1000, 0x19, 0x17)
    OP_6F(0x79)
    Sleep(300)

    ChrTalk(
        0x101,
        "#00006F#5PWhat……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00204F#6P…… Lloyd.\x01",
            "Thank you very much.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 500)
    Sleep(100)

    ChrTalk(
        0x105,
        (
            "#10402F#11PHuh, in no case over there\x01",
            "I do not mean to take it like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#01203F#12P#3CHmm, as expected to the treasured child\x01",
            "It seems there is only to be fond of.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x107, 500)
    Sleep(100)

    ChrTalk(
        0x101,
        (
            "#00012F#5PNo, no.\x01",
            "I just transmitted a message.\x02\x03",
            "#00002FBut …\x01",
            "It was good to be told somehow.\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x8, 0x23)
    OP_A1(0x8, 0x514, 0x4, 0x0, 0x1, 0x2, 0x3)
    Sound(318, 0, 100, 0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7114", 0)
    Sleep(500)

    ChrTalk(
        0x8,
        (
            "#03203F#11PBy the way Lloyd\x02\x03",
            "#03201FThis my wrath#4RPervaded#Unity,\x01",
            "Where should I hit it?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_404B():
        TurnDirection(0x101, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_404B)
    Sleep(0)

    def lambda_405B():
        TurnDirection(0x103, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_405B)
    Sleep(0)

    def lambda_406B():
        TurnDirection(0x105, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_406B)
    Sleep(0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x101,
        "#00005F#6PHuh!?\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    OP_A1(0x8, 0x5DC, 0x3, 0x2, 0x1, 0x0)
    Sleep(50)
    SetChrChipByIndex(0x8, 0x1E)
    Sleep(300)
    TurnDirection(0x8, 0x101, 500)
    Sleep(150)

    ChrTalk(
        0x8,
        (
            "#03204F#5PHmm. Well let's see\x02\x03",
            "#03202FInstead of leaving to Leisha\x01",
            "Shall I invite you to come to \"Black Monday\"?\x02\x03",
            "#03209FIt seems that there are a lot of work to train,\x01",
            "It seems to be a wonderful strength.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00011F#6PHuh!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#10705F#5PCao?!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 500)
    Sleep(100)

    ChrTalk(
        0x9,
        "#11PHa, indeed\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PEven if it is your toffee\x01",
            "If we fix our Kenpo\x01",
            "You can go even further.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#6PNo!\x01",
            "Your words are appreciated!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10402F#12PEhe, you're pretty popular\x02\x03",
            "#10409FThis is an Order#6RUchi#Without defeating\x01",
            "Let's solicit it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00211F#6P…… Wasan.\x01",
            "I can not hear a joke.\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(21210, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Thus, Lloyd's \"Black Moon\" and\x01",
            "Temporary but concluding cooperation ……\x02\x03",
            "In the future, if there is something cooperation,\x01",
            "We will contact you when new information is available\x01",
            "They promised each other.\x02\x03",
            "And \"Silver#2RIn#\"─ ─ Lisa Mao also.\x02\x03",
            "For our own new purpose,\x01",
            "It was to cooperate with Lloyd's.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x22, 4)
    NewScene("e4300", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_7_1DF2 end

    def Function_8_4446(): pass

    label("Function_8_4446")

    OP_95(0xFE, 69000, 14000, 7400, 2000, 0x0)
    ClearChrFlags(0xFE, 0x4)

    def lambda_4464():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4464)
    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_8_4446 end

    def Function_9_4485(): pass

    label("Function_9_4485")

    OP_95(0xFE, 69000, 14000, 6900, 2000, 0x0)
    ClearChrFlags(0xFE, 0x4)

    def lambda_44A3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_44A3)
    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_9_4485 end

    def Function_10_44C4(): pass

    label("Function_10_44C4")

    OP_95(0xFE, 69000, 14000, 7900, 2000, 0x0)
    ClearChrFlags(0xFE, 0x4)

    def lambda_44E2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_44E2)
    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_10_44C4 end

    def Function_11_4503(): pass

    label("Function_11_4503")

    OP_95(0xFE, 69000, 14000, 7400, 2000, 0x0)
    ClearChrFlags(0xFE, 0x4)

    def lambda_4521():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4521)
    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_11_4503 end

    def Function_12_4542(): pass

    label("Function_12_4542")

    OP_95(0xFE, 69000, 14000, 7900, 2000, 0x0)
    ClearChrFlags(0xFE, 0x4)

    def lambda_4560():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4560)
    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_12_4542 end

    def Function_13_4581(): pass

    label("Function_13_4581")

    OP_95(0xFE, 69000, 14000, 6900, 2000, 0x0)
    ClearChrFlags(0xFE, 0x4)

    def lambda_459F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_459F)
    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_13_4581 end

    def Function_14_45C0(): pass

    label("Function_14_45C0")

    OP_95(0xFE, 69000, 14000, 7200, 2000, 0x0)
    ClearChrFlags(0xFE, 0x4)

    def lambda_45DE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_45DE)
    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_14_45C0 end

    def Function_15_45FF(): pass

    label("Function_15_45FF")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch06300.itc", 0x1E)
    LoadChrToIndex("chr/ch03200.itc", 0x1F)
    LoadChrToIndex("chr/ch31400.itc", 0x20)
    SoundLoad(3254)
    SoundLoad(3255)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu03200.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu10700.itp")
    OP_68(72390, 24300, 23330, 0)
    MoveCamera(80, 14, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(15240, 0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 72600, 18000, 21400, 90)
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x11, 0x1F)
    SetChrSubChip(0x11, 0x0)
    SetChrFlags(0x11, 0x8000)
    SetChrPos(0x11, 80270, 18000, 21350, 40)
    ClearChrFlags(0x11, 0x80)
    SetChrChipByIndex(0x9, 0x20)
    SetChrSubChip(0x9, 0x0)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 71580, 18000, 20440, 90)
    ClearChrFlags(0x9, 0x80)
    OP_68(72390, 22500, 23330, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    ChrTalk(
        0x11,
        "#10708F….\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Voice of a young man",
        (
            "#1PHuff, have fun stuff\x01",
            "You showed me.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(69460, 22600, 20450, 3000)
    MoveCamera(83, 18, 0, 3000)
    OP_6E(510, 3000)
    SetCameraDistance(11200, 3000)

    def lambda_47DA():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_47DA)
    Sleep(50)

    def lambda_47F2():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_47F2)
    WaitChrThread(0x9, 1)
    OP_6F(0x79)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x8,
        (
            "Thanks to you\x01",
            "I did not do \"cleaning\".\x02\x03",
            "I must thank them.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    ChrTalk(
        0x11,
        "#10703F….\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x11, 500)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#03204F#6PWhat's wrong?\x01",
            "Mr. Lisha - No, \"silver\".\x02\x03",
            "#03200FAgain, that I signed up with us again …\x01",
            "Do you regret it?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x11, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x11)
    TurnDirection(0x11, 0x8, 500)
    Sleep(300)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    OP_C9(0x0, 0x80000000)

    AnonymousTalk(
        0x11,
        (
            "#3254V#30W……nothing.\x02\x03",
            "#3255V#30WNow I look at the aircraft#2RUkaga#When\x01",
            "let's go.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xCB7)
    OP_C9(0x1, 0x80000000)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)

    ChrTalk(
        0x9,
        "#12P\"Silver\" … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#03209F#6PHuh … Good.\x02\x03",
            "#03204FTo counter us \"them\"\x01",
            "I need your strength.\x02\x03",
            "#03210FOnce again, thanks for your time\x01",
            "Thank you.\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x8, 3, 0, 16)
    Sleep(1500)
    BeginChrThread(0x9, 3, 0, 16)
    Sleep(100)
    BeginChrThread(0x11, 3, 0, 16)
    Sleep(500)
    OP_68(69460, 23700, 20450, 5000)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    OP_CC(0x1, 0xFF, 0x0)
    Sleep(1000)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 1)
    NewScene("t2520", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_15_45FF end

    def Function_16_4B91(): pass

    label("Function_16_4B91")

    OP_93(0xFE, 0x10E, 0x1F4)
    OP_95(0xFE, 72030, 18000, 20890, 2000, 0x0)
    OP_95(0xFE, 71490, 18000, 16230, 2000, 0x0)
    OP_95(0xFE, 67840, 16920, 16270, 2000, 0x0)
    Return()

    # Function_16_4B91 end

    SaveToFile()

Try(main)
