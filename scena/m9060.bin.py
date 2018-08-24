from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "m9060.bin",                # FileName
        "m9060",                    # MapName
        "m9060",                    # Location
        0x00C1,                     # MapIndex
        "ed7354",
        0x00000000,                 # Flags
        ("m9060", "r0000_1", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x2A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, -1400, 0, 1400, 0, 0, 1, 193, 0, 1, 0, 2],
    )

    BuildStringList((
        "m9060",                  # 0
        "ゴートヘッド",           # 1
        "bm9040",                 # 2
        "bm9040",                 # 3
        "bm9040",                 # 4
        "bm9040",                 # 5
    ))

    ATBonus("ATBonus_3FC", 100, 5, 1, 5, 1, 5, 1, 5, 5, 5, 5, 5, 5, 0, 0, 0)
    ATBonus("ATBonus_40C", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    Sepith("Sepith_2A9E", 13,  8,   11,  6,   3,   5,   12)
    Sepith("Sepith_2A8E", 7,   2,   14,  9,   14,  24,  4)
    Sepith("Sepith_2A86", 14,  18,  9,   16,  5,   5,   1)

    MonsterBattlePostion("MonsterBattlePostion_42C", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_430", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_434", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_438", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_43C", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_440", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_444", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_448", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_4AC", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_4B0", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_4B4", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_4B8", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_4BC", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_4C0", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_4C4", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_4C8", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_44C", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_450", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_454", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_458", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_45C", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_460", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_464", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_468", 8, 14, 180)

    # monster count: 17

    BattleInfo(
        "BattleInfo_65C", 0x0000, 103, 6, 60, 6, 1, 30, 0, "bm9040", "Sepith_2A9E", 40, 30, 20, 10,
        (
            ("ms85800.dat", "ms85800.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_42C", "MonsterBattlePostion_4AC", "ed7452", "ed7453", "ATBonus_3FC"),
            ("ms85800.dat", "ms85800.dat", "ms85800.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_44C", "MonsterBattlePostion_4AC", "ed7452", "ed7453", "ATBonus_3FC"),
            ("ms85800.dat", "ms85800.dat", "ms85800.dat", "ms85800.dat", 0, 0, 0, 0, "MonsterBattlePostion_42C", "MonsterBattlePostion_4AC", "ed7452", "ed7453", "ATBonus_3FC"),
            ("ms85800.dat", "ms85800.dat", "ms85800.dat", "ms85800.dat", "ms85800.dat", 0, 0, 0, "MonsterBattlePostion_44C", "MonsterBattlePostion_4AC", "ed7452", "ed7453", "ATBonus_3FC"),
        )
    )

    BattleInfo(
        "BattleInfo_594", 0x0000, 103, 6, 60, 6, 1, 30, 0, "bm9040", "Sepith_2A8E", 40, 30, 20, 10,
        (
            ("ms81400.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_44C", "MonsterBattlePostion_4AC", "ed7452", "ed7453", "ATBonus_3FC"),
            ("ms81400.dat", "ms81400.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_42C", "MonsterBattlePostion_4AC", "ed7452", "ed7453", "ATBonus_3FC"),
            ("ms81400.dat", "ms85800.dat", "ms85800.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_44C", "MonsterBattlePostion_4AC", "ed7452", "ed7453", "ATBonus_3FC"),
            ("ms81400.dat", "ms85800.dat", "ms81400.dat", "ms85800.dat", 0, 0, 0, 0, "MonsterBattlePostion_42C", "MonsterBattlePostion_4AC", "ed7452", "ed7453", "ATBonus_3FC"),
        )
    )

    BattleInfo(
        "BattleInfo_4CC", 0x0000, 103, 6, 60, 10, 1, 30, 0, "bm9040", "Sepith_2A86", 40, 30, 20, 10,
        (
            ("ms78000.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_44C", "MonsterBattlePostion_4AC", "ed7452", "ed7453", "ATBonus_3FC"),
            ("ms78000.dat", "ms78000.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_42C", "MonsterBattlePostion_4AC", "ed7452", "ed7453", "ATBonus_3FC"),
            ("ms78000.dat", "ms78000.dat", "ms78000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_44C", "MonsterBattlePostion_4AC", "ed7452", "ed7453", "ATBonus_3FC"),
            ("ms78000.dat", "ms78000.dat", "ms78000.dat", "ms78000.dat", 0, 0, 0, 0, "MonsterBattlePostion_42C", "MonsterBattlePostion_4AC", "ed7452", "ed7453", "ATBonus_3FC"),
        )
    )

    # event battle count: 1

    BattleInfo(
        "BattleInfo_724", 0x0C00, 255, 6, 0, 0, 3, 0, 0, "bm9040", 0x00000000, 100, 0, 0, 0,
        (
            ("ms81400.dat", "ms85800.dat", "ms81400.dat", "ms85800.dat", "ms81400.dat", "ms85800.dat", "ms81400.dat", "ms85800.dat", "MonsterBattlePostion_44C", "MonsterBattlePostion_4AC", "ed7452", "ed7453", "ATBonus_40C"),
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
        "monster/ch78050.itc",               # 10
        "monster/ch78051.itc",               # 11
        "monster/ch81450.itc",               # 12
        "monster/ch81450.itc",               # 13
        "monster/ch85850.itc",               # 14
        "monster/ch85851.itc",               # 15
    ))

    DeclNpc(4294890296, 4294966796, 64000,   0,    484,  0x0, 0,   18,  0,   0,   0,   255, 255, 255,  0)

    DeclMonster(4294941036, 6670,    0,       0x101005A,    "BattleInfo_65C", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(4294938146, 28540,   0,       0x101007E,    "BattleInfo_594", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(4294897676, 27490,   4294966296, 0x1010073,    "BattleInfo_4CC", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(4294905836, 44190,   4294966296, 0x10100B4,    "BattleInfo_65C", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(4294931046, 66260,   4294965296, 0x10100B4,    "BattleInfo_594", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(4294943936, 55650,   4294965296, 0x101010E,    "BattleInfo_594", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(5230,    33360,   4294965296, 0x1010168,    "BattleInfo_594", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(45700,   60040,   4294966296, 0x10100C7,    "BattleInfo_65C", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(45690,   90870,   0,       0x10100D8,    "BattleInfo_4CC", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(14730,   78200,   0,       0x1010035,    "BattleInfo_65C", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(8029,    98420,   0,       0x10100A8,    "BattleInfo_594", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(4294955706, 68810,   1000,    0x101005A,    "BattleInfo_4CC", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(4294959346, 44730,   1000,    0x10100B4,    "BattleInfo_594", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(4294960566, 101760,  1000,    0x10100AB,    "BattleInfo_65C", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(4294940456, 85930,   0,       0x1010168,    "BattleInfo_594", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(4294915226, 93250,   0,       0x101005A,    "BattleInfo_4CC", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(4294912876, 81530,   0,       0x1010168,    "BattleInfo_65C", 0,   20,  0xFFFF, 4,  5)

    DeclActor(4294894296, 4294966296, 34000,   1200,    4294894296, 0,       34000,   0x007C, 0,  3,  0x0000)
    DeclActor(4294890296, 4294966296, 64000,   1200,    4294890296, 0,       64000,   0x007C, 0,  4,  0x0000)
    DeclActor(4294958296, 1000,    39000,   1200,    4294958296, 2000,    39000,   0x007C, 0,  5,  0x0000)
    DeclActor(12190,   4294965296, 34000,   1200,    12190,   4294966296, 34000,   0x007C, 0,  6,  0x0000)
    DeclActor(14000,   0,       104000,  1200,    14000,   1000,    104000,  0x007C, 0,  7,  0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3])                         # 0
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 2
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4, 5])                   # 3
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 4
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4])                      # 5

    ScpFunction((
        "Function_0_804",          # 00, 0
        "Function_1_821",          # 01, 1
        "Function_2_853",          # 02, 2
        "Function_3_1593",         # 03, 3
        "Function_4_16E4",         # 04, 4
        "Function_5_18FF",         # 05, 5
        "Function_6_1A50",         # 06, 6
        "Function_7_1B0C",         # 07, 7
        "Function_8_1C5D",         # 08, 8
        "Function_9_1C61",         # 09, 9
        "Function_10_1EE1",        # 0A, 10
        "Function_11_2034",        # 0B, 11
        "Function_12_2075",        # 0C, 12
        "Function_13_25FB",        # 0D, 13
        "Function_14_26E9",        # 0E, 14
        "Function_15_2753",        # 0F, 15
        "Function_16_27BD",        # 10, 16
        "Function_17_2827",        # 11, 17
        "Function_18_2891",        # 12, 18
        "Function_19_28FB",        # 13, 19
        "Function_20_2965",        # 14, 20
    ))


    def Function_0_804(): pass

    label("Function_0_804")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_820")
    OP_A1(0xFE, 0x3E8, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Jump("Function_0_804")

    label("loc_820")

    Return()

    # Function_0_804 end

    def Function_1_821(): pass

    label("Function_1_821")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_832")
    Event(0, 9)

    label("loc_832")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_843")
    Event(0, 12)

    label("loc_843")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_852")
    ClearScenarioFlags(0x22, 0)
    Event(0, 13)

    label("loc_852")

    Return()

    # Function_1_821 end

    def Function_2_853(): pass

    label("Function_2_853")

    OP_F0(0x1, 0x320)
    OP_1B(0x0, 0x0, 0xA)
    OP_52(0xB, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xE5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xE5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xE5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xE5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xE5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xE5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xE5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xE5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xE5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xE5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xE5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xE5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xE5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xE5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xE5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xE5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xE5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xE5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xE5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xE5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xE5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xE5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xE5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xE5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xE5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xE5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xE5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xE5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xE5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xE5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xE5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xE5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x204, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11EE")
    OP_70(0x8, 0x0)
    Jump("loc_11F2")

    label("loc_11EE")

    OP_70(0x8, 0x1E)

    label("loc_11F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x204, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1205")
    OP_70(0x9, 0x0)
    Jump("loc_1209")

    label("loc_1205")

    OP_70(0x9, 0x1E)

    label("loc_1209")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x204, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_121C")
    OP_70(0xA, 0x0)
    Jump("loc_1220")

    label("loc_121C")

    OP_70(0xA, 0x1E)

    label("loc_1220")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x204, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1233")
    OP_70(0xB, 0x0)
    Jump("loc_1237")

    label("loc_1233")

    OP_70(0xB, 0x1E)

    label("loc_1237")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x204, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_124A")
    OP_70(0xC, 0x0)
    Jump("loc_124E")

    label("loc_124A")

    OP_70(0xC, 0x1E)

    label("loc_124E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 7)), scpexpr(EXPR_END)), "loc_12EB")
    SetMapObjFrame(0xFF, "hikari00_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari01_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari02_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari03_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari04_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari05_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari99_add", 0x0, 0x1)
    OP_24(0x9A)
    Jump("loc_1525")

    label("loc_12EB")

    OP_C3(0x0, 0x6, 0x3, 0x1E, 0x0, 0x1, -12000, -4000, 5000, 5000, 30000, 0)
    OP_C3(0x1, 0x6, 0x3, 0x1E, 0x0, 0x1, -29000, -4000, 21000, 5000, 30000, 0)
    OP_C3(0x2, 0x6, 0x3, 0x1E, 0x0, 0x1, 6000, -4000, 43000, 5000, 30000, 0)
    OP_C3(0x3, 0x6, 0x3, 0x1E, 0x0, 0x1, -3000, -4000, 57000, 5000, 30000, 0)
    OP_C3(0x4, 0x6, 0x3, 0x1E, 0x0, 0x1, 32000, -4000, 88000, 5000, 30000, 0)
    OP_C3(0x5, 0x6, 0x3, 0x1E, 0x0, 0x1, -26000, -4000, 66000, 5000, 30000, 0)
    OP_C3(0x6, 0x6, 0x3, 0x1E, 0x0, 0x1, -44000, -4000, 87000, 5000, 30000, 0)
    OP_C3(0x7, 0x6, 0x3, 0x1E, 0x0, 0x1, -63000, -4000, 44000, 5000, 30000, 0)
    OP_C3(0x8, 0x6, 0x3, 0x1E, 0x0, 0x1, -12000, -4000, 20000, 7000, 30000, 0)
    OP_C3(0x9, 0x6, 0x3, 0x1E, 0x0, 0x1, 17000, -4000, 55000, 7000, 30000, 0)
    OP_C3(0xA, 0x6, 0x3, 0x1E, 0x0, 0x1, 17000, -4000, 85000, 7000, 30000, 0)
    OP_C3(0xB, 0x6, 0x3, 0x1E, 0x0, 0x1, -32000, -4000, 94000, 7000, 30000, 0)
    OP_C3(0xC, 0x6, 0x3, 0x1E, 0x0, 0x1, -31000, -4000, 53000, 7000, 30000, 0)
    OP_C3(0xD, 0x6, 0x3, 0x1E, 0x0, 0x1, -57000, -4000, 23000, 7000, 30000, 0)
    OP_C3(0xE, 0x6, 0x3, 0x1E, 0x0, 0x1, -77000, -4000, 64000, 7000, 30000, 0)
    OP_C3(0xF, 0x6, 0x3, 0x1E, 0x0, 0x1, 48000, -4000, 70000, 7000, 30000, 0)
    LoadEffect(0x11, "eff\\\\trapdmg0.eff")
    Sound(154, 1, 100, 0)

    label("loc_1525")

    OP_1C(0x0, 0x5, 0x0, 0x0, 0x0, 0x0, 0x1080, 0x0)
    OP_1C(0x0, 0x7, 0x0, 0x0, 0x0, 0x0, 0x1081, 0x0)
    OP_1C(0x0, 0x0, 0x0, 0x32, 0x0, 0x8, 0x0, 0x0)
    OP_1C(0x0, 0x1, 0x0, 0x32, 0x0, 0x8, 0x0, 0x0)
    OP_1C(0x0, 0x2, 0x0, 0x32, 0x0, 0x8, 0x0, 0x0)
    OP_1C(0x0, 0x3, 0x0, 0x32, 0x0, 0x8, 0x0, 0x0)
    OP_1C(0x0, 0x4, 0x0, 0x32, 0x0, 0x8, 0x0, 0x0)
    OP_1C(0x0, 0x6, 0x0, 0x32, 0x0, 0x8, 0x0, 0x0)
    LoadEffect(0x10, "event\\eva00_00.eff")
    Return()

    # Function_2_853 end

    def Function_3_1593(): pass

    label("Function_3_1593")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x204, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_168F")
    Sound(14, 0, 100, 0)
    OP_74(0x8, 0x1E)
    OP_71(0x8, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1FD, 1)"), scpexpr(EXPR_END)), "loc_1618")
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
    SetScenarioFlags(0x204, 2)
    OP_E0(0x5, 0x0)
    Jump("loc_168A")

    label("loc_1618")

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
    OP_71(0x8, 0x1E, 0x0, 0x0, 0x0)

    label("loc_168A")

    Jump("loc_16D8")

    label("loc_168F")

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

    label("loc_16D8")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_1593 end

    def Function_4_16E4(): pass

    label("Function_4_16E4")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x204, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18B5")
    Sound(14, 0, 100, 0)
    OP_74(0x9, 0x1E)
    OP_71(0x9, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x219, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17E7")
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0x8, 0x0, 0)
    OP_98(0x8, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_1741():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1741)

    def lambda_175B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_175B)
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
    Battle("BattleInfo_724", 0x0, 0x0, 0x0, 0xB, 0xFF)
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0x8, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_17C8"),
        (2, "loc_17D7"),
        (1, "loc_17E4"),
        (SWITCH_DEFAULT, "loc_17E7"),
    )


    label("loc_17C8")

    SetScenarioFlags(0x219, 0)
    OP_70(0x9, 0x1E)
    Sleep(500)
    Jump("loc_17E7")

    label("loc_17D7")

    OP_70(0x9, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_17E4")

    OP_B9(0x0)
    Return()

    label("loc_17E7")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x444, 1)"), scpexpr(EXPR_END)), "loc_1840")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x444),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x204, 3)
    OP_E0(0x5, 0x0)
    Jump("loc_18B0")

    label("loc_1840")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x444),
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

    label("loc_18B0")

    Jump("loc_18F3")

    label("loc_18B5")

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

    label("loc_18F3")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_16E4 end

    def Function_5_18FF(): pass

    label("Function_5_18FF")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x204, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19FB")
    Sound(14, 0, 100, 0)
    OP_74(0xA, 0x1E)
    OP_71(0xA, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x59, 1)"), scpexpr(EXPR_END)), "loc_1984")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x59),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x204, 4)
    OP_E0(0x5, 0x0)
    Jump("loc_19F6")

    label("loc_1984")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x59),
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

    label("loc_19F6")

    Jump("loc_1A44")

    label("loc_19FB")

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

    label("loc_1A44")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_18FF end

    def Function_6_1A50(): pass

    label("Function_6_1A50")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x204, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1ADC")
    Sound(14, 0, 100, 0)
    OP_74(0xB, 0x1E)
    OP_71(0xB, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    OP_70(0xB, 0x1E)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddSepith(0x0, 2000)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#56I Earth Sepith x2000\x07\x00\x01",
            "obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x204, 5)
    OP_E0(0x5, 0x0)
    Jump("loc_1AFA")

    label("loc_1ADC")


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

    label("loc_1AFA")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_1A50 end

    def Function_7_1B0C(): pass

    label("Function_7_1B0C")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x204, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C08")
    Sound(14, 0, 100, 0)
    OP_74(0xC, 0x1E)
    OP_71(0xC, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1FA, 1)"), scpexpr(EXPR_END)), "loc_1B91")
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
    SetScenarioFlags(0x204, 6)
    OP_E0(0x5, 0x0)
    Jump("loc_1C03")

    label("loc_1B91")

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
    OP_71(0xC, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1C03")

    Jump("loc_1C51")

    label("loc_1C08")

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

    label("loc_1C51")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_1B0C end

    def Function_8_1C5D(): pass

    label("Function_8_1C5D")

    Call(1, 6)
    Return()

    # Function_8_1C5D end

    def Function_9_1C61(): pass

    label("Function_9_1C61")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    LoadEffect(0x1, "event\\ev202_00.eff")
    OP_68(-140, 1000, -790, 0)
    MoveCamera(356, 34, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(13270, 0)
    SetChrPos(0x0, 0, 0, 0, 315)
    SetChrPos(0x1, 0, 0, 0, 315)
    SetChrPos(0x2, 0, 0, 0, 315)
    SetChrPos(0x3, 0, 0, 0, 315)
    OP_A7(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    Sound(920, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x0, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_1D71():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_1D71)

    def lambda_1D82():
        OP_95(0xFE, -1800, 0, 1810, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1D82)
    Sleep(500)
    PlayEffect(0x1, 0xFF, 0x1, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_1DD9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_1DD9)

    def lambda_1DEA():
        OP_95(0xFE, -380, 0, 2370, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_1DEA)
    Sleep(500)
    Sound(920, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x2, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_1E47():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2, 2, lambda_1E47)

    def lambda_1E58():
        OP_95(0xFE, -2480, 0, 1070, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_1E58)
    Sleep(500)
    PlayEffect(0x1, 0xFF, 0x3, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_1EAF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x3, 2, lambda_1EAF)

    def lambda_1EC0():
        OP_95(0xFE, -1920, 0, -630, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_1EC0)
    WaitChrThread(0x3, 1)
    Sleep(1000)
    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_9_1C61 end

    def Function_10_1EE1(): pass

    label("Function_10_1EE1")

    EventBegin(0x0)
    OP_E2(0x3)
    LoadEffect(0x1, "event\\evwarp.eff")
    Sound(936, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x0, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_1F3A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_1F3A)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0x1, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_1F85():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_1F85)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0x2, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_1FD0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2, 2, lambda_1FD0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0x3, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_201B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x3, 2, lambda_201B)
    Sleep(1000)
    NewScene("m9002", 109, 0, 0)
    IdleLoop()
    Return()

    # Function_10_1EE1 end

    def Function_11_2034(): pass

    label("Function_11_2034")

    OP_CF(0x1, 0xF4, 0x4)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_204C")
    OP_CF(0x1, 0xF5, 0x5)

    label("loc_204C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2060")
    OP_CF(0x1, 0xF5, 0x8)

    label("loc_2060")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2074")
    OP_CF(0x1, 0xF5, 0x9)

    label("loc_2074")

    Return()

    # Function_11_2034 end

    def Function_12_2075(): pass

    label("Function_12_2075")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    OP_69(0x0, 0x0)
    LoadEffect(0x1, "event\\ev202_00.eff")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_20AF")
    Call(0, 11)

    label("loc_20AF")

    SetChrPos(0xF4, 0, 0, 0, 320)
    SetChrPos(0x101, 0, 0, 0, 339)
    SetChrPos(0x102, 0, 0, 0, 302)
    SetChrPos(0x103, 0, 0, 0, 326)
    SetChrPos(0x104, 0, 0, 0, 352)
    SetChrPos(0xF5, 0, 0, 0, 292)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xF4, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xF5, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_68(-18810, 900, 59120, 0)
    MoveCamera(23, 13, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(26720, 0)
    OP_68(-8280, 900, 30280, 6500)
    MoveCamera(23, 13, 0, 6500)
    OP_6E(700, 6500)
    SetCameraDistance(32479, 6500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    OP_68(-27860, 900, 30190, 0)
    MoveCamera(316, 14, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(34290, 0)
    OP_68(-5050, 900, 5110, 7500)
    MoveCamera(317, 14, 0, 7500)
    OP_6E(700, 7500)
    SetCameraDistance(30870, 7500)
    Sleep(500)
    PlaceName2(340, 200, "c_plac58", 0x0, 0)
    Sleep(1000)
    BeginChrThread(0xF4, 0, 0, 14)
    Sleep(600)
    BeginChrThread(0x101, 0, 0, 15)
    Sleep(600)
    BeginChrThread(0x102, 0, 0, 16)
    Sleep(600)
    Sound(920, 0, 100, 0)
    BeginChrThread(0x103, 0, 0, 17)
    Sleep(600)
    BeginChrThread(0x104, 0, 0, 18)
    Sleep(600)
    Sound(920, 0, 100, 0)
    BeginChrThread(0xF5, 0, 0, 19)
    WaitChrThread(0xF5, 0)
    OP_6F(0x79)
    Fade(500)
    OP_68(-3300, 900, 4350, 0)
    MoveCamera(356, 23, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(15000, 0)
    OP_0D()
    Sleep(300)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A8, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2303")

    ChrTalk(
        0x102,
        (
            "#00108F#12PThis place is a\x01",
            "Territory...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2328")

    label("loc_2303")


    ChrTalk(
        0x102,
        "#00108F#12PAnother Territory...\x02",
    )

    CloseMessageWindow()

    label("loc_2328")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2364")

    ChrTalk(
        0x10A,
        "#00601F#12PA vast wasteland, huh?\x02",
    )

    CloseMessageWindow()
    Jump("loc_23D1")

    label("loc_2364")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_239D")

    ChrTalk(
        0x106,
        "#10701F#12PA vast wasteland...\x02",
    )

    CloseMessageWindow()
    Jump("loc_23D1")

    label("loc_239D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_23D1")

    ChrTalk(
        0x109,
        "#10111F#12PA vast wasteland...\x02",
    )

    CloseMessageWindow()

    label("loc_23D1")


    ChrTalk(
        0x104,
        (
            "#00306F#12P...Just like that guy's\x01",
            "personality, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00201F#12PThose things... look\x01",
            "like some kind of\x01",
            "negative energy...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10406F#11P─Oh man. I seem to have\x01",
            "underestimated him just a\x01",
            "tiny bit.\x02\x03",
            "#10408FWho could've thought some\x01",
            "street fighter could\x01",
            ""transform" this much...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008F#11PWazy...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2533")

    ChrTalk(
        0x109,
        "#10108F#12P...Wazy.\x02",
    )

    CloseMessageWindow()

    label("loc_2533")


    ChrTalk(
        0x105,
        (
            "#10402F#11P─Let's go. Wald is\x01",
            "waiting for me up ahead.\x02\x03",
            "#10404FAnd this time, I'll have\x01",
            "to beat him down with\x01",
            "everything I've got.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -1500, 0, 2500, 315)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x1A7, 6)
    OP_E2(0x2)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_12_2075 end

    def Function_13_25FB(): pass

    label("Function_13_25FB")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x1)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xF4, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xF5, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(-29410, 1000, 58000, 0)
    MoveCamera(15, 21, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(31650, 0)
    OP_68(-5640, 1000, 5570, 10000)
    MoveCamera(316, 18, 0, 10000)
    OP_6E(700, 10000)
    SetCameraDistance(31650, 10000)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    FadeToBright(1000, 0)
    OP_0D()
    BeginChrThread(0x101, 0, 0, 20)
    WaitChrThread(0x101, 0)
    OP_6F(0x79)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 0)
    NewScene("m9002", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_13_25FB end

    def Function_14_26E9(): pass

    label("Function_14_26E9")

    PlayEffect(0x1, 0xFF, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_2728():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2728)
    OP_9B(0x0, 0xFE, 0x0, 0x1482, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x7D0, 0x0)
    Return()

    # Function_14_26E9 end

    def Function_15_2753(): pass

    label("Function_15_2753")

    PlayEffect(0x1, 0xFF, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_2792():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2792)
    OP_9B(0x0, 0xFE, 0x0, 0x10FE, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x155, 0x3E8, 0x7D0, 0x0)
    Return()

    # Function_15_2753 end

    def Function_16_27BD(): pass

    label("Function_16_27BD")

    PlayEffect(0x1, 0xFF, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_27FC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_27FC)
    OP_9B(0x0, 0xFE, 0x0, 0x1036, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x12, 0x3E8, 0x7D0, 0x0)
    Return()

    # Function_16_27BD end

    def Function_17_2827(): pass

    label("Function_17_2827")

    PlayEffect(0x1, 0xFF, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_2866():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2866)
    OP_9B(0x0, 0xFE, 0x0, 0xD48, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x162, 0x3E8, 0x7D0, 0x0)
    Return()

    # Function_17_2827 end

    def Function_18_2891(): pass

    label("Function_18_2891")

    PlayEffect(0x1, 0xFF, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_28D0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_28D0)
    OP_9B(0x0, 0xFE, 0x0, 0xC4E, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x148, 0x3E8, 0x7D0, 0x0)
    Return()

    # Function_18_2891 end

    def Function_19_28FB(): pass

    label("Function_19_28FB")

    PlayEffect(0x1, 0xFF, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_293A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_293A)
    OP_9B(0x0, 0xFE, 0x0, 0xB22, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x1C, 0x3E8, 0x7D0, 0x0)
    Return()

    # Function_19_28FB end

    def Function_20_2965(): pass

    label("Function_20_2965")

    Sleep(500)
    SetMapObjFrame(0xFF, "hikari00_add", 0x0, 0x1)
    Sleep(200)
    SetMapObjFrame(0xFF, "hikari01_add", 0x0, 0x1)
    Sleep(200)
    StopSound(154, 2000, 100)
    Sound(954, 0, 100, 0)
    SetMapObjFrame(0xFF, "hikari02_add", 0x0, 0x1)
    Sleep(200)
    SetMapObjFrame(0xFF, "hikari03_add", 0x0, 0x1)
    Sleep(200)
    SetMapObjFrame(0xFF, "hikari04_add", 0x0, 0x1)
    Sleep(200)
    SetMapObjFrame(0xFF, "hikari05_add", 0x0, 0x1)
    Sleep(200)
    SetMapObjFrame(0xFF, "hikari99_add", 0x0, 0x1)
    Sleep(200)
    Return()

    # Function_20_2965 end

    SaveToFile()

Try(main)
