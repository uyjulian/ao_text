from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "Cao",                    # 1
        "Lau",                    # 2
        "Heiyue Member",          # 3
        "Heiyue Member",          # 4
        "Heiyue Member",          # 5
        "Heiyue Member",          # 6
        "Heiyue Member",          # 7
        "Heiyue Member",          # 8
        "Heiyue Member",          # 9
        "Rixia",                  # 10
        "オドロンドロ",           # 11
        "br3000",                 # 12
        "br3000",                 # 13
        "br3000",                 # 14
        "br3000",                 # 15
        "br3000",                 # 16
        "br3000",                 # 17
        "To Armorica Old Road",   # 18
    ))

    ATBonus("ATBonus_540", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_4E0A", 8,   14,  0,   10,  4,   2,   0)
    Sepith("Sepith_4E12", 0,   0,   6,   14,  6,   6,   6)
    Sepith("Sepith_4E22", 8,   8,   8,   8,   8,   8,   8)
    Sepith("Sepith_4E1A", 8,   6,   3,   0,   7,   7,   7)
    Sepith("Sepith_4E32", 10,  10,  10,  10,  3,   3,   3)

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
        "BattleInfo_878", 0x0000, 73, 6, 60, 8, 1, 20, 0, "br3000", "Sepith_4E0A", 30, 30, 20, 20,
        (
            ("ms69500.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_5A0", "MonsterBattlePostion_600", "ed7450", "ed7453", "ATBonus_540"),
            ("ms69500.dat", "ms69500.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_580", "MonsterBattlePostion_600", "ed7450", "ed7453", "ATBonus_540"),
            ("ms69500.dat", "ms63400.dat", "ms69500.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_5A0", "MonsterBattlePostion_600", "ed7450", "ed7453", "ATBonus_540"),
            ("ms69500.dat", "ms64100.dat", "ms64100.dat", "ms64100.dat", 0, 0, 0, 0, "MonsterBattlePostion_580", "MonsterBattlePostion_600", "ed7450", "ed7453", "ATBonus_540"),
        )
    )

    BattleInfo(
        "BattleInfo_7B0", 0x0000, 73, 6, 60, 8, 1, 40, 0, "br3000", "Sepith_4E12", 30, 40, 20, 10,
        (
            ("ms63400.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_5A0", "MonsterBattlePostion_600", "ed7450", "ed7453", "ATBonus_540"),
            ("ms63400.dat", "ms63400.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_580", "MonsterBattlePostion_600", "ed7450", "ed7453", "ATBonus_540"),
            ("ms63400.dat", "ms63400.dat", "ms63400.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_5A0", "MonsterBattlePostion_600", "ed7450", "ed7453", "ATBonus_540"),
            ("ms63400.dat", "ms63400.dat", "ms63400.dat", "ms63400.dat", 0, 0, 0, 0, "MonsterBattlePostion_580", "MonsterBattlePostion_600", "ed7450", "ed7453", "ATBonus_540"),
        )
    )

    BattleInfo(
        "BattleInfo_620", 0x0000, 73, 6, 60, 8, 1, 40, 0, "br3000", "Sepith_4E22", 30, 40, 20, 10,
        (
            ("ms66800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_5A0", "MonsterBattlePostion_600", "ed7450", "ed7453", "ATBonus_540"),
            ("ms66800.dat", "ms66800.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_580", "MonsterBattlePostion_600", "ed7450", "ed7453", "ATBonus_540"),
            ("ms66800.dat", "ms69500.dat", "ms66800.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_5A0", "MonsterBattlePostion_600", "ed7450", "ed7453", "ATBonus_540"),
            ("ms66800.dat", "ms69500.dat", "ms66800.dat", "ms69500.dat", 0, 0, 0, 0, "MonsterBattlePostion_580", "MonsterBattlePostion_600", "ed7450", "ed7453", "ATBonus_540"),
        )
    )

    BattleInfo(
        "BattleInfo_6E8", 0x0000, 73, 6, 60, 8, 1, 10, 0, "br3000", "Sepith_4E1A", 30, 40, 20, 10,
        (
            ("ms63500.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_5A0", "MonsterBattlePostion_600", "ed7450", "ed7453", "ATBonus_540"),
            ("ms63500.dat", "ms63500.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_580", "MonsterBattlePostion_600", "ed7450", "ed7453", "ATBonus_540"),
            ("ms63500.dat", "ms63400.dat", "ms63500.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_5A0", "MonsterBattlePostion_600", "ed7450", "ed7453", "ATBonus_540"),
            ("ms63500.dat", "ms63500.dat", "ms63400.dat", "ms63500.dat", 0, 0, 0, 0, "MonsterBattlePostion_580", "MonsterBattlePostion_600", "ed7450", "ed7453", "ATBonus_540"),
        )
    )

    BattleInfo(
        "BattleInfo_940", 0x0000, 73, 6, 60, 8, 1, 60, 0, "br3000", "Sepith_4E32", 30, 40, 20, 10,
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

    PlaceName(-84.0, 0.0, 48.0, 0x0000, 0x0000, "To Armorica Old Road")

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
        "Function_5_1CA1",         # 05, 5
        "Function_6_1DF2",         # 06, 6
        "Function_7_1DF6",         # 07, 7
        "Function_8_4640",         # 08, 8
        "Function_9_467F",         # 09, 9
        "Function_10_46BE",        # 0A, 10
        "Function_11_46FD",        # 0B, 11
        "Function_12_473C",        # 0C, 12
        "Function_13_477B",        # 0D, 13
        "Function_14_47BA",        # 0E, 14
        "Function_15_47F9",        # 0F, 15
        "Function_16_4D9E",        # 10, 16
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F4, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A31")
    Sound(14, 0, 100, 0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1FA, 1)"), scpexpr(EXPR_END)), "loc_19BA")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1FA),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1F4, 4)
    OP_E0(0x5, 0x0)
    Jump("loc_1A2C")

    label("loc_19BA")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1FA),
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

    label("loc_1A2C")

    Jump("loc_1A7A")

    label("loc_1A31")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x217, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B89")
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
            "Monsters appeared!\x07\x00\x02",
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
        (0, "loc_1B6A"),
        (2, "loc_1B79"),
        (1, "loc_1B86"),
        (SWITCH_DEFAULT, "loc_1B89"),
    )


    label("loc_1B6A")

    SetScenarioFlags(0x217, 5)
    OP_70(0x1, 0x1E)
    Sleep(500)
    Jump("loc_1B89")

    label("loc_1B79")

    OP_70(0x1, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_1B86")

    OP_B9(0x0)
    Return()

    label("loc_1B89")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x6A, 1)"), scpexpr(EXPR_END)), "loc_1BE2")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x6A),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x6A),
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

    label("loc_1C52")

    Jump("loc_1C95")

    label("loc_1C57")

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

    label("loc_1C95")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_1A86 end

    def Function_5_1CA1(): pass

    label("Function_5_1CA1")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D9D")
    Sound(14, 0, 100, 0)
    OP_74(0x2, 0x1E)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x64E, 1)"), scpexpr(EXPR_END)), "loc_1D26")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x64E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x64E),
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

    label("loc_1D98")

    Jump("loc_1DE6")

    label("loc_1D9D")

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

    label("loc_1DE6")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_1CA1 end

    def Function_6_1DF2(): pass

    label("Function_6_1DF2")

    Call(1, 6)
    Return()

    # Function_6_1DF2 end

    def Function_7_1DF6(): pass

    label("Function_7_1DF6")

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
            "#00006F#6PI see...\x02\x03",
            "#00001FSo you've been hiding\x01",
            "around here since the\x01",
            "attack?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#03204F#5PYes, the site of the old\x01",
            "cult ruins is a convenient\x01",
            "place to hide, as well.\x02\x03",
            "#03210FWe also observed the\x01",
            "Snakes setting up the\x01",
            "giant bell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00201F#6PThe place where that\x01",
            "Doctor was...?\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(500)
    SetMessageWindowPos(0, 170, -1, -1)

    AnonymousTalk(
        0x105,
        (
            "#10403FThe giant bell used in the ceremony\x01",
            "to complete the Sept-Terrion of\x01",
            "Zero, located in Central Square?\x02\x03",
            "#10401FThere's no doubt that it's some\x01",
            "kind of Artifact.\x02",
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
            "#11PIncidentally, it appears that the\x01",
            "bell has been moved again and was\x01",
            "returned to Crossbell City.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PAt present, it can be\x01",
            "said that only we Heiyue\x01",
            "inhabit these lands.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PMaster Yin excepted, of\x01",
            "course.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_24D5():
        TurnDirection(0x101, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_24D5)
    Sleep(50)

    def lambda_24E5():
        TurnDirection(0x103, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_24E5)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x103, 0)

    def lambda_24FD():
        OP_93(0x8, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_24FD)
    Sleep(50)

    def lambda_250D():
        OP_93(0x9, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_250D)
    Sleep(50)
    WaitChrThread(0x8, 0)
    WaitChrThread(0x9, 0)

    ChrTalk(
        0x106,
        "#10708F#11P...............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008F#12PRixia...\x02",
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
            "#10706F#5P... Lloyd. For now, please\x01",
            "overlook my presence here...\x02\x03",
            "#10708FAnd the many illegal acts\x01",
            "I've done in these lands...\x02\x03",
            "#10711FI can't be caught. I intend\x01",
            "to go back to Calvard and not\x01",
            "cause any further trouble.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_A0(0x106, 1500, 0x3, 0x5)
    Sleep(300)

    ChrTalk(
        0x106,
        (
            "#10703F#5P─After I finish what I've\x01",
            "started, I'll return to\x01",
            "Calvard for good.\x02",
        )
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
        "#00208F#12PIsn't that...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#12P...Revenge?\x02",
    )

    CloseMessageWindow()
    Sleep(50)
    OP_A0(0x106, 1300, 0x5, 0x3)
    Sleep(100)

    ChrTalk(
        0x106,
        "#10708F#5P#30W...............\x02",
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
            "#10703F#11P#30WThose people... They\x01",
            "took away the most\x01",
            "precious thing.\x02\x03",
            "Everyone's sun... An\x01",
            "irreplaceable hope.\x02\x03",
            "#10708FI'll never... ever...\x01",
            "forgive them.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0xE1, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#03204F#5PHaha, that's why I let you re-sign\x01",
            "the contract you broke.\x02\x03",
            "#03210FIn order to collaborate in the\x01",
            "takedown of our formidable enemy,\x01",
            "Red Constellation, isn't that right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#6P...You stay silent.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00003F#12PSay, Rixia.\x02\x03",
            "#00001FDo you know that Ilya\x01",
            "has woken up?\x02",
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
            "#10707F#3SR-Really!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00204F#12PYes, it seems she regained\x01",
            "consciousness immediately\x01",
            "after that strange phenomenon.\x02\x03",
            "#00202FShe hasn't fully healed yet,\x01",
            "but... She is quite full of\x01",
            "energy.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_A0(0x106, 1200, 0x1B, 0x1C)
    Sleep(200)

    ChrTalk(
        0x106,
        (
            "#10704F#5P#40W...Ah, oh Aidios...\x02\x03",
            "#10710F#40W...Thank you... Thank\x01",
            "you for your mercy.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x10E, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#03204F#11PHehe, aren't you glad?\x02\x03",
            "#03210FAlthough, according to my sources, the lower\x01",
            "half of her body is paralyzed, so it may never\x01",
            "be possible for her to return to the stage.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    OP_A1(0x106, 0x5DC, 0x3, 0x1C, 0x1B, 0x3)
    Sleep(100)

    ChrTalk(
        0x106,
        "#10708F#5P......\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00013F#6PYou...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10401F#12PIt looks like you\x01",
            "already know that, don't\x01",
            "you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#03204F#11PYes, but since Master\x01",
            "Yin said she didn't want\x01",
            "to hear a word of it...\x02\x03",
            "#03210FI didn't dare say a\x01",
            "thing.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x106, 0xA)
    Sleep(150)

    ChrTalk(
        0x106,
        "#10701F#5P............(*glare*)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PMaster Cao... Not\x01",
            "another word.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11P─Master Yin. Please,\x01",
            "don't misunderstand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PIt was Master Cao's regard\x01",
            "for you, in order to not make\x01",
            "you anxious or discouraged...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    SetChrSubChip(0x106, 0x3)
    Sleep(300)

    ChrTalk(
        0x106,
        (
            "#10703F#5P...No explanation is\x01",
            "necessary.\x02\x03",
            "#10708FWhat I heard won't change\x01",
            "what I've decided to do.\x02\x03",
            "#10711FAfter I have settled things\x01",
            "in my own way... I'll leave\x01",
            "the land of Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11P............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#03204F#11PAnd we would be\x01",
            "extremely grateful if\x01",
            "you did that.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#03200F#5P─Lloyd and you all as well. We each\x01",
            "have our own circumstances, but\x01",
            "also a common enemy we must fight.\x02\x03",
            "#03209FAt this time, I was thinking I'd\x01",
            "like to form a cooperative\x01",
            "relationship with you all.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x2D, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        "#00001F#6P............\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00006F#6PYeah, I don't mind.\x02\x03",
            "#00000F─However. Rixia stays\x01",
            "with us.\x02",
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

    def lambda_30D8():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_30D8)
    Sleep(0)

    def lambda_30E8():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_30E8)
    Sleep(0)

    def lambda_30F8():
        TurnDirection(0x107, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_30F8)
    Sleep(0)

    def lambda_3108():
        TurnDirection(0x8, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_3108)
    Sleep(0)

    def lambda_3118():
        TurnDirection(0x9, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_3118)
    Sleep(0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x107, 0)
    WaitChrThread(0x8, 0)
    WaitChrThread(0x9, 0)

    ChrTalk(
        0x106,
        "#10705F#5P...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00205F#6PLloyd...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#03201F#5P...Hm?\x02",
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
            "#00001F#12PRixia. I have a message\x01",
            "for you from Ilya.\x02\x03",
            "#00003F"─What's the most\x01",
            "precious thing to you?"\x02\x03",
            ""Can you be in front of\x01",
            "that precious thing and\x01",
            "not do your best for it?"\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x106,
        "#10712F#5P#30W...Ah...\x02",
    )

    CloseMessageWindow()

    def lambda_32A6():
        TurnDirection(0x101, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_32A6)
    Sleep(0)

    def lambda_32B6():
        TurnDirection(0x103, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_32B6)
    Sleep(0)

    def lambda_32C6():
        TurnDirection(0x105, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_32C6)
    Sleep(0)

    def lambda_32D6():
        TurnDirection(0x107, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_32D6)
    Sleep(0)

    def lambda_32E6():
        TurnDirection(0x106, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_32E6)
    Sleep(0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x107, 0)
    WaitChrThread(0x106, 0)

    def lambda_330A():
        OP_93(0x8, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_330A)
    Sleep(50)

    def lambda_331A():
        OP_93(0x9, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_331A)
    Sleep(50)
    WaitChrThread(0x8, 0)
    WaitChrThread(0x9, 0)

    ChrTalk(
        0x101,
        (
            "#00003F#12PYou see, Ilya... wasn't sad at\x01",
            "all.\x02\x03",
            "#00008FAt first I thought she was just\x01",
            "hiding her true feelings,\x01",
            "but...\x02\x03",
            "#00000FShe'll come back on stage for\x01",
            "sure... She seemed to believe\x01",
            "that firmly without any doubts.\x02\x03",
            "#00004FEven after properly\x01",
            "understanding how hard that\x01",
            "it's actually going to be.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#10708F#5P#30W............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10406F#12PWell, frankly speaking, I think\x01",
            "it's difficult to stick to\x01",
            "one's beliefs that much, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00204F#12PEven so, just by hearing\x01",
            "that, we were encouraged\x01",
            "too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#03201F#11P............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#12PWhile Ilya's trying her\x01",
            "damned hardest to get\x01",
            "back on that stage...\x02\x03",
            "#00001FWhat's the most\x01",
            "important thing to you?\x02\x03",
            "Revenge against Red\x01",
            "Constellation?\x02\x03",
            "The creed of Yin that\x01",
            "you've inherited?\x02\x03",
            "Or something else─\x02",
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

    def lambda_3658():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_3658)
    WaitChrThread(0x106, 2)
    Sleep(500)

    def lambda_3678():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_3678)
    WaitChrThread(0x106, 2)
    Sleep(500)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x106,
        (
            "#10708F#3272V#11P#40W#20A...There's no...\x02\x03",
            "#3273V#45AThere's no way I... There's no\x01",
            "way I can say that.\x02\x03",
            "#10706F#3274V#45A...I, smeared with blood...\x01",
            "Someone like me, who's ensnared\x01",
            "within the darkness...\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00006F#12P─Don't dodge the question, Rixia.\x02\x03",
            "#00013FI'm asking you what the most\x01",
            "precious thing in the world is to\x01",
            "you.\x02\x03",
            "The one thing you can't help but do\x01",
            "your best for... The precious thing\x01",
            "your soul can't help but desire?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x106,
        "#10708F#11P...!\x02",
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
            "#10713F#3256V#4S#5P#30AThat's─ That's Arc-en-\x01",
            "Ciel, of course!\x02",
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
            "#10714F#3257V#5P#40AI... I want to dance on\x01",
            "that stage again!\x02\x03",
            "#3258V#40AWith Ilya, Sully and\x01",
            "everyone in our troupe!\x02\x03",
            "#10713F#3259V#30AThat's─ That's all!\x02",
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
        "#00214F#12PAh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10404F#12P...Hehe...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002F#12P...I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#03201F#11P............\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x8)

    ChrTalk(
        0x9,
        "#11P...Master Cao.\x02",
    )

    CloseMessageWindow()

    def lambda_3A7B():
        TurnDirection(0x101, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3A7B)
    Sleep(50)

    def lambda_3A8B():
        TurnDirection(0x103, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_3A8B)
    Sleep(50)

    def lambda_3A9B():
        TurnDirection(0x105, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_3A9B)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x105, 0)
    OP_A0(0x106, 1500, 0x14, 0x15)
    Sleep(150)

    ChrTalk(
        0x106,
        "#10708F#5P...Ah...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00013F#6P............\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    OP_A0(0x106, 1500, 0x15, 0x17)
    Sleep(150)

    ChrTalk(
        0x8,
        (
            "#03204F#60W#2S#11P#12A......Hehe......\x01",
            "Hahaha......\x02",
        )
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
            "#03210F#5PHehe... That's Lloyd for\x01",
            "you.\x02\x03",
            "You've done a splendid\x01",
            "job of messing up all my\x01",
            "plans, haven't you?\x02\x03",
            "#03203FNo, in this case, should\x01",
            "I say that Ilya has won\x01",
            "this one?\x02\x03",
            "#03202FI've been defeated...\x01",
            "Yes─ Completely and\x01",
            "utterly defeated.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#10708F#5PCao...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#6P...Got anything else to\x01",
            "say?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#03202F#5PThe truth is that I'm\x01",
            "extremely furious, but...\x02\x03",
            "#03204FWe'll be working together in\x01",
            "the future, after all. So I'll\x01",
            "leave it at this for today.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x10E, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#03204F#11PMaster Yin... No, Rixia\x01",
            "Mao.\x02\x03",
            "I will terminate your\x01",
            "current contract with\x01",
            "Heiyue.\x02\x03",
            "#03200FFeel free to go wherever\x01",
            "you want.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10712F#5PAh...\x02\x03",
            "#10710F...Cao. Thank you very\x01",
            "much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#03210F#11PRemember though that I am only\x01",
            "conceding this time.\x02\x03",
            "#03203FBut to accomplish what I, no,\x01",
            "what Heiyue wants... We do\x01",
            "need your power.\x02\x03",
            "#03210FWell, for now, you should make\x01",
            "an effort to put your heart\x01",
            "and soul into the stage.\x02",
        )
    )

    CloseMessageWindow()
    OP_A0(0x106, 1200, 0x17, 0x19)
    Sleep(300)

    ChrTalk(
        0x106,
        (
            "#10704F#5P...Yes. I won't ever let\x01",
            "up.\x02",
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
        "#00006F#5P*sigh*...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00204F#6P... Lloyd. Thank you\x01",
            "very much for your hard\x01",
            "work.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 500)
    Sleep(100)

    ChrTalk(
        0x105,
        (
            "#10402F#11PHehe, I'd never thought\x01",
            "you'd pull it off as\x01",
            "well as you did.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#01203F#12P#3CYes, I guess that's to\x01",
            "be expected from the the\x01",
            "Divine Child's favorite.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x107, 500)
    Sleep(100)

    ChrTalk(
        0x101,
        (
            "#00012F#5PN-No no, I was just\x01",
            "relaying a message.\x02\x03",
            "#00002FBut... I'm glad it got\x01",
            "through to her.\x02",
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
            "#03203F#11P─By the way, Lloyd.\x02\x03",
            "#03201FI wonder where should I\x01",
            "direct this anger of\x01",
            "mine?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_41BC():
        TurnDirection(0x101, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_41BC)
    Sleep(0)

    def lambda_41CC():
        TurnDirection(0x103, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_41CC)
    Sleep(0)

    def lambda_41DC():
        TurnDirection(0x105, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_41DC)
    Sleep(0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x101,
        "#00005F#6PHuh...?\x02",
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
            "#03204F#5PHmm, let's see.\x02\x03",
            "#03202FShould I have you join Heiyue\x01",
            "in place of Rixia, who has\x01",
            "left?\x02\x03",
            "#03209FYou seem able to be trained in\x01",
            "many ways and you would be a\x01",
            "wonderful help to us in battle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00011F#6PHuh...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#10705F#5PCao!?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 500)
    Sleep(100)

    ChrTalk(
        0x9,
        "#11PHaha, indeed.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PConsidering your skill with those\x01",
            "tonfas, if you mastered our kenpｷ,\x01",
            "you could reach even further heights.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#6PN-No way! I'm not that\x01",
            "skilled but I'm\x01",
            "flattered by your words!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10402F#12PHehe, you're the popular\x01",
            "one, aren't you?\x02\x03",
            "#10409FShould I not lose to\x01",
            "them and invite you to\x01",
            "join the knights, then?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00211F#6P... Wazy. Enough with\x01",
            "your jokes.\x02",
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
            "Thus, Lloyd and the others formed a\x01",
            "cooperative relationship with Heiyue,\x01",
            "although only temporarily...\x02\x03",
            "They promised to cooperate if\x01",
            "something happened and to contact each\x01",
            "other if there was any new intel.\x02\x03",
            "Also, Yin... ─Rixia Mao, decided...\x02\x03",
            "To cooperate with Lloyd and the others\x01",
            "again, for the sake of her new goal.\x07\x00\x02",
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

    # Function_7_1DF6 end

    def Function_8_4640(): pass

    label("Function_8_4640")

    OP_95(0xFE, 69000, 14000, 7400, 2000, 0x0)
    ClearChrFlags(0xFE, 0x4)

    def lambda_465E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_465E)
    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_8_4640 end

    def Function_9_467F(): pass

    label("Function_9_467F")

    OP_95(0xFE, 69000, 14000, 6900, 2000, 0x0)
    ClearChrFlags(0xFE, 0x4)

    def lambda_469D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_469D)
    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_9_467F end

    def Function_10_46BE(): pass

    label("Function_10_46BE")

    OP_95(0xFE, 69000, 14000, 7900, 2000, 0x0)
    ClearChrFlags(0xFE, 0x4)

    def lambda_46DC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_46DC)
    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_10_46BE end

    def Function_11_46FD(): pass

    label("Function_11_46FD")

    OP_95(0xFE, 69000, 14000, 7400, 2000, 0x0)
    ClearChrFlags(0xFE, 0x4)

    def lambda_471B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_471B)
    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_11_46FD end

    def Function_12_473C(): pass

    label("Function_12_473C")

    OP_95(0xFE, 69000, 14000, 7900, 2000, 0x0)
    ClearChrFlags(0xFE, 0x4)

    def lambda_475A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_475A)
    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_12_473C end

    def Function_13_477B(): pass

    label("Function_13_477B")

    OP_95(0xFE, 69000, 14000, 6900, 2000, 0x0)
    ClearChrFlags(0xFE, 0x4)

    def lambda_4799():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4799)
    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_13_477B end

    def Function_14_47BA(): pass

    label("Function_14_47BA")

    OP_95(0xFE, 69000, 14000, 7200, 2000, 0x0)
    ClearChrFlags(0xFE, 0x4)

    def lambda_47D8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_47D8)
    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_14_47BA end

    def Function_15_47F9(): pass

    label("Function_15_47F9")

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
        "#10708F...............\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Youth's Voice",
        (
            "#1PHehe, they showed me\x01",
            "something interesting,\x01",
            "didn't they.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(69460, 22600, 20450, 3000)
    MoveCamera(83, 18, 0, 3000)
    OP_6E(510, 3000)
    SetCameraDistance(11200, 3000)

    def lambda_49D9():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_49D9)
    Sleep(50)

    def lambda_49F1():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_49F1)
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
            "Thanks to them, it ended without\x01",
            "any troublesome "cleaning".\x02\x03",
            "I'll have to thank them.\x02",
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
        "#10703F...............\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x11, 500)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#03204F#6PWhat's wrong? Rixia─ No,\x01",
            "Master Yin.\x02\x03",
            "#03200FAs I feared... You have\x01",
            "regrets about accepting\x01",
            "another contract with us?\x02",
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
            "#3254V#30W...It's nothing.\x02\x03",
            "#3255V#30WNow we must wait for our chance...\x01",
            "Let's go.\x02",
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
        "#12PMaster Yin...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#03209F#6PHehe...very well.\x02\x03",
            "#03204FWe too, in order to\x01",
            "oppose "them", are in\x01",
            "need of your strength.\x02\x03",
            "#03210FIt is nice to be working\x01",
            "with you once again.\x02",
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

    # Function_15_47F9 end

    def Function_16_4D9E(): pass

    label("Function_16_4D9E")

    OP_93(0xFE, 0x10E, 0x1F4)
    OP_95(0xFE, 72030, 18000, 20890, 2000, 0x0)
    OP_95(0xFE, 71490, 18000, 16230, 2000, 0x0)
    OP_95(0xFE, 67840, 16920, 16270, 2000, 0x0)
    Return()

    # Function_16_4D9E end

    SaveToFile()

Try(main)
