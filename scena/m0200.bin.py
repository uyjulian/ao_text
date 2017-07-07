﻿from ScenarioHelper import *

def main():
    CreateScenaFile(
        "m0200.bin",                # FileName
        "m0200",                    # MapName
        "m0200",                    # Location
        0x00A7,                     # MapIndex
        "ed7300",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 167, 0, 1, 0, 2],
    )

    BuildStringList((
        "m0200",                  # 0
        "terrorist",             # 1
        "terrorist",             # 2
        "terrorist",             # 3
        "terrorist",             # 4
        "terrorist",             # 5
        "terrorist",             # 6
        "terrorist",             # 7
        "Arios",               # 8
        "Dudley investigator",         # 9
        "Silver",                     # 10
        "Tsao",                 # 11
        "Row",                   # 12
        "Black moon member",             # 13
        "Black moon member",             # 14
        "Black moon member",             # 15
        "Black moon member",             # 16
        "Black moon member",             # 17
        "SE control",                 # 18
        "bm0200",                 # 19
        "bm0200",                 # 20
        "bm0200",                 # 21
    ))

    ATBonus("ATBonus_59C", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_4851", 8,   6,   10,  4,   4,   4,   4)
    Sepith("Sepith_4841", 2,   0,   20,  2,   4,   5,   2)
    Sepith("Sepith_4849", 6,   6,   0,   14,  4,   4,   6)

    MonsterBattlePostion("MonsterBattlePostion_5FC", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_600", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_604", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_608", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_60C", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_610", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_614", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_618", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_65C", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_660", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_664", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_668", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_66C", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_670", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_674", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_678", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_5DC", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_5E0", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_5E4", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_5E8", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_5EC", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_5F0", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_5F4", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_5F8", 2, 13, 180)

    # monster count: 7

    BattleInfo(
        "BattleInfo_80C", 0x0000, 74, 6, 60, 6, 1, 30, 0, "bm0200", "Sepith_4851", 40, 30, 20, 10,
        (
            ("ms84900.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_5FC", "MonsterBattlePostion_65C", "ed7450", "ed7453", "ATBonus_59C"),
            ("ms84900.dat", "ms84900.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_5DC", "MonsterBattlePostion_65C", "ed7450", "ed7453", "ATBonus_59C"),
            ("ms84900.dat", "ms84900.dat", "ms84900.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_5FC", "MonsterBattlePostion_65C", "ed7450", "ed7453", "ATBonus_59C"),
            ("ms84900.dat", "ms84900.dat", "ms84900.dat", "ms84900.dat", 0, 0, 0, 0, "MonsterBattlePostion_5DC", "MonsterBattlePostion_65C", "ed7450", "ed7453", "ATBonus_59C"),
        )
    )

    BattleInfo(
        "BattleInfo_67C", 0x0000, 74, 6, 60, 6, 1, 30, 0, "bm0200", "Sepith_4841", 40, 30, 20, 10,
        (
            ("ms84800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_5FC", "MonsterBattlePostion_65C", "ed7450", "ed7453", "ATBonus_59C"),
            ("ms84800.dat", "ms84800.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_5DC", "MonsterBattlePostion_65C", "ed7450", "ed7453", "ATBonus_59C"),
            ("ms84800.dat", "ms84800.dat", "ms84800.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_5FC", "MonsterBattlePostion_65C", "ed7450", "ed7453", "ATBonus_59C"),
            ("ms84800.dat", "ms84800.dat", "ms84800.dat", "ms84800.dat", 0, 0, 0, 0, "MonsterBattlePostion_5DC", "MonsterBattlePostion_65C", "ed7450", "ed7453", "ATBonus_59C"),
        )
    )

    BattleInfo(
        "BattleInfo_744", 0x0000, 74, 6, 60, 6, 1, 30, 0, "bm0200", "Sepith_4849", 40, 30, 20, 10,
        (
            ("ms79000.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_5FC", "MonsterBattlePostion_65C", "ed7450", "ed7453", "ATBonus_59C"),
            ("ms79000.dat", "ms79000.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_5DC", "MonsterBattlePostion_65C", "ed7450", "ed7453", "ATBonus_59C"),
            ("ms79000.dat", "ms79000.dat", "ms79000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_5FC", "MonsterBattlePostion_65C", "ed7450", "ed7453", "ATBonus_59C"),
            ("ms79000.dat", "ms79000.dat", "ms79000.dat", "ms79000.dat", 0, 0, 0, 0, "MonsterBattlePostion_5DC", "MonsterBattlePostion_65C", "ed7450", "ed7453", "ATBonus_59C"),
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
        "monster/ch84850.itc",               # 10
        "monster/ch84850.itc",               # 11
        "monster/ch79050.itc",               # 12
        "monster/ch79050.itc",               # 13
        "monster/ch84950.itc",               # 14
        "monster/ch84951.itc",               # 15
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
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(4294767296, 4294767696, 4000,    0x10100E1,    "BattleInfo_80C", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(4294563206, 4294775146, 0,       0x1010087,    "BattleInfo_67C", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(4294564986, 4294759836, 4294961296, 0x101013B,    "BattleInfo_744", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(4294763136, 4294961906, 4294965296, 0x10100A0,    "BattleInfo_80C", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(4294766926, 4294758696, 4294965296, 0x101010A,    "BattleInfo_67C", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(4294751096, 4294759236, 4294965296, 0x1010047,    "BattleInfo_744", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(4294770926, 4294566776, 0,       0x1010001,    "BattleInfo_80C", 0,   20,  0xFFFF, 4,  5)

    DeclEvent(0x0000, 0, 8,   -6.5,                  0.0,                   1.0,                   25.0,                  [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   0.0,                   3.25,                  -0.0,                  -0.19999998807907104,  1.0])

    DeclActor(2500,    2000,    5500,    1200,    2500,    3000,    5500,    0x007C, 0,  11, 0x0000)
    DeclActor(2500,    4294947296, 5500,    1200,    2500,    4294948296, 5500,    0x007C, 0,  12, 0x0000)
    DeclActor(4294777186, 6000,    4294375526, 1200,    4294777186, 8000,    4294375526, 0x007C, 0,  10, 0x0000)
    DeclActor(4294579296, 0,       4294204796, 1200,    4294579296, 1000,    4294204796, 0x007C, 0,  13, 0x0000)
    DeclActor(187500,  0,       242000,  1200,    187500,  1000,    242000,  0x007C, 0,  15, 0x0000)
    DeclActor(4294567296, 4294961296, 4294759296, 1200,    4294567296, 4294962296, 4294759296, 0x007C, 0,  3,  0x0000)
    DeclActor(4294561296, 0,       4294567296, 1200,    4294561296, 1000,    4294567296, 0x007C, 0,  4,  0x0000)
    DeclActor(4294771796, 6000,    4294958296, 1200,    4294771796, 7000,    4294958296, 0x007C, 0,  5,  0x0000)
    DeclActor(4294570296, 0,       4294189296, 1200,    4294570296, 1000,    4294189296, 0x007C, 0,  6,  0x0000)
    DeclActor(204000,  4294965296, 4294764296, 1200,    204000,  4294966296, 4294764296, 0x007C, 0,  7,  0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 0
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4])                      # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 2
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 3
    ChipFrameInfo(1000, 0, [0, 1, 2, 3])                         # 4
    ChipFrameInfo(1000, 0, [0, 1, 2, 3])                         # 5

    ScpFunction((
        "Function_0_9B0",          # 00, 0
        "Function_1_A60",          # 01, 1
        "Function_2_B61",          # 02, 2
        "Function_3_DFB",          # 03, 3
        "Function_4_F4C",          # 04, 4
        "Function_5_10C1",         # 05, 5
        "Function_6_1212",         # 06, 6
        "Function_7_1363",         # 07, 7
        "Function_8_14B4",         # 08, 8
        "Function_9_166C",         # 09, 9
        "Function_10_1813",        # 0A, 10
        "Function_11_18A6",        # 0B, 11
        "Function_12_1A46",        # 0C, 12
        "Function_13_1BDB",        # 0D, 13
        "Function_14_1D6E",        # 0E, 14
        "Function_15_1E9E",        # 0F, 15
        "Function_16_2031",        # 10, 16
        "Function_17_2161",        # 11, 17
        "Function_18_2AE0",        # 12, 18
        "Function_19_2B23",        # 13, 19
        "Function_20_2BC1",        # 14, 20
        "Function_21_2C5F",        # 15, 21
        "Function_22_2D4E",        # 16, 22
        "Function_23_2F52",        # 17, 23
        "Function_24_315D",        # 18, 24
        "Function_25_319A",        # 19, 25
        "Function_26_31EB",        # 1A, 26
        "Function_27_3AAF",        # 1B, 27
        "Function_28_43C0",        # 1C, 28
        "Function_29_440E",        # 1D, 29
        "Function_30_445C",        # 1E, 30
        "Function_31_44B1",        # 1F, 31
        "Function_32_4506",        # 20, 32
        "Function_33_455B",        # 21, 33
        "Function_34_45B0",        # 22, 34
        "Function_35_4668",        # 23, 35
        "Function_36_46C9",        # 24, 36
    ))


    def Function_0_9B0(): pass

    label("Function_0_9B0")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_9E8"),
        (1, "loc_9F4"),
        (2, "loc_A00"),
        (3, "loc_A0C"),
        (4, "loc_A18"),
        (5, "loc_A24"),
        (6, "loc_A30"),
        (SWITCH_DEFAULT, "loc_A3C"),
    )


    label("loc_9E8")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_A48")

    label("loc_9F4")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_A48")

    label("loc_A00")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_A48")

    label("loc_A0C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_A48")

    label("loc_A18")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_A48")

    label("loc_A24")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_A48")

    label("loc_A30")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_A48")

    label("loc_A3C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_A48")

    label("loc_A48")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A5F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_A48")

    label("loc_A5F")

    Return()

    # Function_0_9B0 end

    def Function_1_A60(): pass

    label("Function_1_A60")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x84), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x86), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A7D")
    OP_C9(0x1, 0x1000)

    label("loc_A7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AA8")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x85), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3D)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AA8")
    SetMapFlags(0x10000000)
    Event(0, 9)

    label("loc_AA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_ABC")
    ClearScenarioFlags(0x22, 0)
    Event(0, 34)
    Jump("loc_ACB")

    label("loc_ABC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_ACB")
    ClearScenarioFlags(0x22, 1)
    Event(0, 17)

    label("loc_ACB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6D), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AE5")
    Event(0, 26)

    label("loc_AE5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x77), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AFF")
    Event(0, 27)

    label("loc_AFF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B10")
    SetScenarioFlags(0x194, 0)

    label("loc_B10")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x85), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B2F")
    ClearScenarioFlags(0x0, 0)
    Jump("loc_B32")

    label("loc_B2F")

    SetScenarioFlags(0x0, 0)

    label("loc_B32")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_ADD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B49")
    Event(0, 14)

    label("loc_B49")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_ADD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B60")
    Event(0, 16)

    label("loc_B60")

    Return()

    # Function_1_A60 end

    def Function_2_B61(): pass

    label("Function_2_B61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x194, 0)), scpexpr(EXPR_END)), "loc_B91")
    SetMapObjFrame(0x3, "lock_g", 0x1, 0x1)
    SetMapObjFrame(0x3, "lock_r", 0x0, 0x1)
    SetMapObjFlags(0x3, 0x10)
    Jump("loc_BB3")

    label("loc_B91")

    SetMapObjFrame(0x3, "lock_g", 0x0, 0x1)
    SetMapObjFrame(0x3, "lock_r", 0x1, 0x1)
    ClearMapObjFlags(0x3, 0x10)

    label("loc_BB3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BCE")
    OP_71(0x10, 0x0, 0x5, 0x0, 0x20)
    Jump("loc_BDA")

    label("loc_BCE")

    OP_71(0x10, 0x78, 0x7D, 0x0, 0x20)

    label("loc_BDA")

    OP_10(0x1, 0x0)
    OP_10(0x18, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C3D")
    SetMapObjFrame(0x12, "Null_color", 0x0, 0x1)
    SetMapObjFrame(0x12, "Null_color2", 0x0, 0x1)
    SetMapObjFrame(0x11, "Null_color2", 0x0, 0x1)
    SetMapObjFrame(0x11, "Null_color", 0x0, 0x1)
    Jump("loc_D03")

    label("loc_C3D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_ADD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C7B")
    SetMapObjFrame(0x12, "Null_color", 0x0, 0x1)
    SetMapObjFrame(0x12, "Null_color2", 0x1, 0x1)
    Jump("loc_CA0")

    label("loc_C7B")

    SetMapObjFrame(0x12, "Null_color", 0x1, 0x1)
    SetMapObjFrame(0x12, "Null_color2", 0x0, 0x1)

    label("loc_CA0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_ADD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CDE")
    SetMapObjFrame(0x11, "Null_color", 0x1, 0x1)
    SetMapObjFrame(0x11, "Null_color2", 0x0, 0x1)
    Jump("loc_D03")

    label("loc_CDE")

    SetMapObjFrame(0x11, "Null_color", 0x0, 0x1)
    SetMapObjFrame(0x11, "Null_color2", 0x1, 0x1)

    label("loc_D03")

    ClearMapObjFlags(0x5, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D22")
    OP_70(0x5, 0x0)
    SetMapObjFlags(0x14, 0x4)
    Jump("loc_D3B")

    label("loc_D22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_D3B")
    SetMapObjFlags(0x14, 0x4)
    OP_70(0x5, 0x28)
    ClearMapObjFlags(0x5, 0x2)

    label("loc_D3B")

    OP_10(0x20, 0x0)
    OP_10(0x22, 0x0)
    OP_10(0x0, 0x0)
    OP_10(0x21, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1FC, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D5A")
    OP_70(0x0, 0x0)
    Jump("loc_D5E")

    label("loc_D5A")

    OP_70(0x0, 0x1E)

    label("loc_D5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1FC, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D71")
    OP_70(0x1, 0x0)
    Jump("loc_D75")

    label("loc_D71")

    OP_70(0x1, 0x1E)

    label("loc_D75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1FC, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D88")
    OP_70(0x13, 0x0)
    Jump("loc_D8C")

    label("loc_D88")

    OP_70(0x13, 0x1E)

    label("loc_D8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E9, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D9F")
    OP_70(0x15, 0x0)
    Jump("loc_DA3")

    label("loc_D9F")

    OP_70(0x15, 0x1E)

    label("loc_DA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E9, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DB6")
    OP_70(0x16, 0x0)
    Jump("loc_DBA")

    label("loc_DB6")

    OP_70(0x16, 0x1E)

    label("loc_DBA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x85), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x84), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_DF4")
    OP_24(0x85)
    Jump("loc_DFA")

    label("loc_DF4")

    Sound(133, 1, 100, 0)

    label("loc_DFA")

    Return()

    # Function_2_B61 end

    def Function_3_DFB(): pass

    label("Function_3_DFB")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1FC, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EFB")
    Sound(14, 0, 100, 0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('星辰灵摆', 1)"), scpexpr(EXPR_END)), "loc_E84")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '星辰灵摆'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1FC, 0)
    OP_E0(0x5, 0x0)
    Jump("loc_EF6")

    label("loc_E84")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            "In the treasure box",
            scpstr(SCPSTR_CODE_ITEM, '星辰灵摆'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Is contained.\x01",
            "Because my belongings are full,",
            scpstr(SCPSTR_CODE_ITEM, '星辰灵摆'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I gave up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x0, 0x1E, 0x0, 0x0, 0x0)

    label("loc_EF6")

    Jump("loc_F40")

    label("loc_EFB")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "In the treasure box何も入っていない。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_F40")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_DFB end

    def Function_4_F4C(): pass

    label("Function_4_F4C")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1FC, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_108A")
    Sound(14, 0, 100, 0)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    OP_70(0x1, 0x1E)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddSepith(0x0, 100)
    AddSepith(0x1, 100)
    AddSepith(0x2, 100)
    AddSepith(0x3, 100)
    AddSepith(0x4, 100)
    AddSepith(0x5, 100)
    AddSepith(0x6, 100)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#56ISepis of the earth × 100\x01\x07\x02",
            "#57IWater sepis × 100\x01\x07\x02",
            "#58IFire sepis × 100\x01\x07\x02",
            "#59IWind sepice × 100\x01\x07\x02",
            "#60ITime sepis × 100\x01\x07\x02",
            "#61IEmpty Sepis × 100\x01\x07\x02",
            "#62IPhantom Sepis × 100\x01\x07\x00",
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x1FC, 1)
    OP_E0(0x5, 0x0)
    Jump("loc_10AF")

    label("loc_108A")


    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "In the treasure box何も入っていない。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_10AF")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_F4C end

    def Function_5_10C1(): pass

    label("Function_5_10C1")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1FC, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11C1")
    Sound(14, 0, 100, 0)
    OP_74(0x13, 0x1E)
    OP_71(0x13, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('龙华树之服', 1)"), scpexpr(EXPR_END)), "loc_114A")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '龙华树之服'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1FC, 2)
    OP_E0(0x5, 0x0)
    Jump("loc_11BC")

    label("loc_114A")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            "In the treasure box",
            scpstr(SCPSTR_CODE_ITEM, '龙华树之服'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Is contained.\x01",
            "Because my belongings are full,",
            scpstr(SCPSTR_CODE_ITEM, '龙华树之服'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I gave up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x13, 0x1E, 0x0, 0x0, 0x0)

    label("loc_11BC")

    Jump("loc_1206")

    label("loc_11C1")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "In the treasure box何も入っていない。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_1206")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_10C1 end

    def Function_6_1212(): pass

    label("Function_6_1212")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E9, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1312")
    Sound(14, 0, 100, 0)
    OP_74(0x15, 0x1E)
    OP_71(0x15, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('ＥＰ填充剂Ⅲ', 1)"), scpexpr(EXPR_END)), "loc_129B")
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
    SetScenarioFlags(0x1E9, 6)
    OP_E0(0x5, 0x0)
    Jump("loc_130D")

    label("loc_129B")

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
    OP_71(0x15, 0x1E, 0x0, 0x0, 0x0)

    label("loc_130D")

    Jump("loc_1357")

    label("loc_1312")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "In the treasure box何も入っていない。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_1357")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_1212 end

    def Function_7_1363(): pass

    label("Function_7_1363")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E9, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1463")
    Sound(14, 0, 100, 0)
    OP_74(0x16, 0x1E)
    OP_71(0x16, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('圣灵药·改', 1)"), scpexpr(EXPR_END)), "loc_13EC")
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
    SetScenarioFlags(0x1E9, 7)
    OP_E0(0x5, 0x0)
    Jump("loc_145E")

    label("loc_13EC")

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
    OP_71(0x16, 0x1E, 0x0, 0x0, 0x0)

    label("loc_145E")

    Jump("loc_14A8")

    label("loc_1463")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "In the treasure box何も入っていない。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_14A8")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_1363 end

    def Function_8_14B4(): pass

    label("Function_8_14B4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3D)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_166B")
    EventBegin(0x0)
    Fade(500)
    OP_68(-3720, 2000, 1200, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17960, 0)
    SetChrPos(0x101, -5200, 2000, 0, 90)
    SetChrPos(0x104, -5200, 2000, -1200, 90)
    SetChrPos(0x102, -5200, 2000, 1200, 90)
    SetChrPos(0x109, -6200, 2000, 0, 90)
    SetChrPos(0x103, -6200, 2000, -1200, 90)
    SetChrPos(0x105, -6200, 2000, 1200, 90)
    SetChrPos(0x13E, -2930, 2000, 40, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_0D()

    ChrTalk(
        0x13E,
        "#11P#02305FDo you intend to go outside?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FOh, just a bit.\x01",
            "I will be back soon as I get ready.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13E,
        (
            "#11P#02306FWell, hurry up.\x01",
            "I am waiting for you here.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    RemoveParty(0x3D, 0xFF)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x22, 1)
    NewScene("c120D", 0, 0, 0)
    IdleLoop()

    label("loc_166B")

    Return()

    # Function_8_14B4 end

    def Function_9_166C(): pass

    label("Function_9_166C")

    EventBegin(0x0)
    AddParty(0x3D, 0xFF, 0xFF)
    Fade(500)
    OP_68(-3720, 2000, 1200, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17960, 0)
    SetChrPos(0x101, -5200, 2000, 0, 90)
    SetChrPos(0x104, -5200, 2000, -1200, 90)
    SetChrPos(0x102, -5200, 2000, 1200, 90)
    SetChrPos(0x109, -6200, 2000, 0, 90)
    SetChrPos(0x103, -6200, 2000, -1200, 90)
    SetChrPos(0x105, -6200, 2000, 1200, 90)
    SetChrPos(0x13E, -2930, 2000, 40, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_0D()

    ChrTalk(
        0x13E,
        (
            "#11P#02305FO, it looks like it came back.\x02\x03",
            "#02302FWell then, quickly\x01",
            "Head to the 4th control terminal!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FOh, I understand.\x01",
            "Come along firmly.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -5200, 2000, 0, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    ClearMapFlags(0x10000000)
    Return()

    # Function_9_166C end

    def Function_10_1813(): pass

    label("Function_10_1813")

    EventBegin(0x1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a ladder.\x01",
            "Do you want to climb it?\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18A3")
    FadeToDark(500, 0, -1)
    OP_0D()
    EventEnd(0x5)
    OP_C9(0x0, 0x1000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1895")
    NewScene("c120D", 105, 0, 0)
    IdleLoop()
    Jump("loc_189E")

    label("loc_1895")

    NewScene("c1200", 108, 0, 0)
    IdleLoop()

    label("loc_189E")

    Jump("loc_18A5")

    label("loc_18A3")

    EventEnd(0x5)

    label("loc_18A5")

    Return()

    # Function_10_1813 end

    def Function_11_18A6(): pass

    label("Function_11_18A6")

    SetMapFlags(0x8000000)
    EventBegin(0x1)
    SoundLoad(144)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is an elevator control panel.\x01",
            "Do you want to operate it?\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A3E")
    Fade(500)
    SetChrPos(0x0, 1400, 2000, 5300, 90)
    SetChrPos(0x1, 1400, 2000, 6300, 90)
    SetChrPos(0x2, 0, 2000, 5300, 90)
    SetChrPos(0x3, 0, 2000, 6300, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3D)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_197F")
    SetChrPos(0x13E, -1000, 2000, 5800, 90)

    label("loc_197F")

    OP_68(1280, 2000, 6880, 0)
    MoveCamera(21, 44, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14970, 0)
    OP_0D()
    Sleep(500)
    Sound(143, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_71(0x10, 0x5, 0x78, 0x0, 0x0)
    Sleep(200)
    Sound(145, 0, 100, 0)
    Sleep(800)
    Fade(500)
    OP_68(1280, -10000, 6880, 0)
    MoveCamera(21, 38, 0, 0)
    SetCameraDistance(20000, 0)
    OP_0D()
    OP_68(1280, -20000, 6880, 1800)
    Sleep(2200)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_79(0x10)
    OP_6F(0x1)
    SetScenarioFlags(0x0, 0)

    label("loc_1A3E")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_11_18A6 end

    def Function_12_1A46(): pass

    label("Function_12_1A46")

    SetMapFlags(0x8000000)
    EventBegin(0x1)
    SoundLoad(144)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is an elevator control panel.\x01",
            "Do you want to operate it?\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BD3")
    Fade(500)
    SetChrPos(0x0, 1400, -20000, 5300, 90)
    SetChrPos(0x1, 1400, -20000, 6300, 90)
    SetChrPos(0x2, 200, -20000, 5300, 90)
    SetChrPos(0x3, 200, -20000, 6300, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3D)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B1F")
    SetChrPos(0x13E, -1000, -20000, 5800, 90)

    label("loc_1B1F")

    OP_68(1280, -20000, 6880, 0)
    MoveCamera(21, 44, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14970, 0)
    OP_0D()
    Sleep(500)
    Sound(143, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_71(0x10, 0x7D, 0xF5, 0x0, 0x0)
    OP_68(1280, -12000, 6880, 2000)
    Sleep(200)
    Sound(145, 0, 100, 0)
    Sleep(1800)
    Fade(500)
    OP_68(1280, 2000, 6880, 0)
    SetCameraDistance(16970, 0)
    OP_0D()
    Sleep(1300)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_79(0x10)
    OP_6F(0x1)
    ClearScenarioFlags(0x0, 0)

    label("loc_1BD3")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_12_1A46 end

    def Function_13_1BDB(): pass

    label("Function_13_1BDB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1BED")
    Call(0, 36)
    Return()

    label("loc_1BED")

    SetMapFlags(0x8000000)
    EventBegin(0x1)
    SoundLoad(144)
    SoundLoad(150)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a lift control panel.\x01",
            "Do you want to operate it?\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D66")
    Fade(500)
    SetChrPos(0x0, -387500, 0, -764000, 0)
    SetChrPos(0x1, -388500, 0, -764000, 0)
    SetChrPos(0x2, -387500, 0, -765000, 0)
    SetChrPos(0x3, -388500, 0, -765000, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3D)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1CC3")
    SetChrPos(0x13E, -388000, 0, -766000, 0)

    label("loc_1CC3")

    OP_68(-387800, 0, -763430, 0)
    MoveCamera(50, 53, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(25000, 0)
    OP_0D()
    Sleep(500)
    Sound(144, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_71(0x12, 0x104, 0x1C2, 0x0, 0x0)
    Sleep(200)
    OP_68(-387600, 0, -753410, 3800)
    MoveCamera(31, 61, 0, 3800)
    Sleep(1800)
    Sound(150, 2, 100, 0)
    Sleep(200)
    FadeToDark(500, 0, -1)
    Sleep(4000)
    StopSound(150, 1000, 100)
    Sleep(1000)
    OP_0D()
    NewScene("m0202", 100, 0, 0)
    IdleLoop()

    label("loc_1D66")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_13_1BDB end

    def Function_14_1D6E(): pass

    label("Function_14_1D6E")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    OP_6F(0x1)
    OP_70(0x12, 0x64)
    Sleep(1)
    OP_68(-385270, 0, -759650, 0)
    MoveCamera(35, 51, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(25000, 0)
    OP_90(0x0, -390000, -1290, -754000, 270)
    OP_90(0x1, -390000, -1290, -755000, 270)
    OP_90(0x2, -389000, -1290, -754000, 270)
    OP_90(0x3, -389000, -1290, -755000, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3D)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E1B")
    SetChrPos(0x13E, -388500, -2500, -753000, 270)

    label("loc_1E1B")

    Sound(145, 0, 100, 0)
    OP_68(-390500, 0, -764340, 3200)
    MoveCamera(43, 43, 0, 3200)
    OP_71(0x12, 0x15E, 0x104, 0x0, 0x0)
    FadeToBright(500, 0)
    Sleep(3400)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_79(0x12)
    OP_6F(0x1)
    Sleep(500)
    SetMapObjFrame(0x12, "Null_color", 0x1, 0x1)
    SetMapObjFrame(0x12, "Null_color2", 0x0, 0x1)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_14_1D6E end

    def Function_15_1E9E(): pass

    label("Function_15_1E9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1EB0")
    Call(0, 36)
    Return()

    label("loc_1EB0")

    SetMapFlags(0x8000000)
    EventBegin(0x1)
    SoundLoad(144)
    SoundLoad(150)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a lift control panel.\x01",
            "Do you want to operate it?\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2029")
    Fade(500)
    SetChrPos(0x0, 189000, 0, 241500, 270)
    SetChrPos(0x1, 189000, 0, 242500, 270)
    SetChrPos(0x2, 190000, 0, 241500, 270)
    SetChrPos(0x3, 190000, 0, 242500, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3D)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F86")
    SetChrPos(0x13E, 192500, 0, 242000, 270)

    label("loc_1F86")

    OP_68(190000, 0, 242550, 0)
    MoveCamera(42, 49, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(25000, 0)
    OP_0D()
    Sleep(500)
    Sound(144, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_71(0x11, 0x2F8, 0x3B6, 0x0, 0x0)
    Sleep(200)
    OP_68(177000, -2000, 241550, 3800)
    MoveCamera(62, 29, 0, 3800)
    Sleep(1800)
    Sound(150, 2, 100, 0)
    Sleep(200)
    FadeToDark(500, 0, -1)
    Sleep(7000)
    StopSound(150, 1000, 100)
    Sleep(1000)
    OP_0D()
    NewScene("m0209", 101, 0, 0)
    IdleLoop()

    label("loc_2029")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_15_1E9E end

    def Function_16_2031(): pass

    label("Function_16_2031")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    OP_6F(0x1)
    OP_70(0x11, 0x352)
    Sleep(1)
    OP_68(180000, -2500, 240000, 0)
    MoveCamera(60, 17, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(25000, 0)
    OP_90(0x0, 178000, -2500, 239500, 180)
    OP_90(0x1, 177000, -2500, 239500, 180)
    OP_90(0x2, 178000, -2500, 240500, 180)
    OP_90(0x3, 177000, -2500, 240500, 180)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3D)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_20DE")
    SetChrPos(0x13E, 177500, -2500, 250500, 180)

    label("loc_20DE")

    Sound(145, 0, 100, 0)
    OP_68(193500, 0, 239000, 3200)
    MoveCamera(43, 43, 0, 3200)
    OP_71(0x11, 0x352, 0x2F8, 0x0, 0x0)
    FadeToBright(500, 0)
    Sleep(3400)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_79(0x11)
    OP_6F(0x1)
    Sleep(500)
    SetMapObjFrame(0x11, "Null_color", 0x0, 0x1)
    SetMapObjFrame(0x11, "Null_color2", 0x1, 0x1)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_16_2031 end

    def Function_17_2161(): pass

    label("Function_17_2161")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x1)
    LoadChrToIndex("chr/ch02400.itc", 0x1E)
    LoadChrToIndex("chr/ch00900.itc", 0x1F)
    LoadChrToIndex("chr/ch42500.itc", 0x20)
    LoadChrToIndex("chr/ch00500.itc", 0x21)
    LoadChrToIndex("chr/ch06300.itc", 0x22)
    LoadChrToIndex("chr/ch31400.itc", 0x23)
    LoadChrToIndex("chr/ch31500.itc", 0x24)
    LoadChrToIndex("chr/ch12500.itc", 0x25)
    LoadChrToIndex("chr/ch42553.itc", 0x26)
    LoadChrToIndex("apl/ch50220.itc", 0x27)
    SoundLoad(844)
    SetChrChipByIndex(0xF, 0x1E)
    SetChrSubChip(0xF, 0x0)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xF, -212000, -2000, -207300, 90)
    SetChrChipByIndex(0x10, 0x1F)
    SetChrSubChip(0x10, 0x0)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x8000)
    SetChrPos(0x10, -212200, -2000, -208600, 90)
    SetChrChipByIndex(0x8, 0x26)
    SetChrSubChip(0x8, 0x3)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, -205000, -2000, -208800, 270)
    SetChrChipByIndex(0x9, 0x26)
    SetChrSubChip(0x9, 0x3)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, -205000, -2000, -206500, 180)
    SetChrChipByIndex(0xA, 0x26)
    SetChrSubChip(0xA, 0x3)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, -203600, -2000, -208800, 0)
    SetChrChipByIndex(0xB, 0x26)
    SetChrSubChip(0xB, 0x3)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, -203600, -2000, -206500, 225)
    SetChrChipByIndex(0xC, 0x26)
    SetChrSubChip(0xC, 0x3)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, -202300, -2000, -208000, 135)
    SetChrChipByIndex(0xD, 0x26)
    SetChrSubChip(0xD, 0x3)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    SetChrPos(0xD, -202600, -2000, -210000, 315)
    SetChrChipByIndex(0xE, 0x26)
    SetChrSubChip(0xE, 0x3)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)
    SetChrPos(0xE, -204600, -2000, -210200, 270)
    SetChrChipByIndex(0x11, 0x21)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8000)
    SetChrPos(0x11, -206600, -2000, -206600, 270)
    SetChrChipByIndex(0x12, 0x22)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0x12, -207400, -2000, -208000, 270)
    SetChrChipByIndex(0x13, 0x23)
    SetChrSubChip(0x13, 0x0)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, -206900, -2000, -209000, 270)
    SetChrChipByIndex(0x14, 0x24)
    SetChrSubChip(0x14, 0x0)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x14, -204800, -2000, -211600, 0)
    SetChrChipByIndex(0x15, 0x25)
    SetChrSubChip(0x15, 0x0)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x8000)
    SetChrPos(0x15, -204300, -2000, -205100, 180)
    SetChrChipByIndex(0x16, 0x25)
    SetChrSubChip(0x16, 0x0)
    ClearChrFlags(0x16, 0x80)
    SetChrFlags(0x16, 0x8000)
    SetChrPos(0x16, -202900, -2000, -211400, 0)
    SetChrChipByIndex(0x17, 0x24)
    SetChrSubChip(0x17, 0x0)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x17, 0x8000)
    SetChrPos(0x17, -201800, -2000, -206400, 225)
    SetChrChipByIndex(0x18, 0x25)
    SetChrSubChip(0x18, 0x0)
    ClearChrFlags(0x18, 0x80)
    SetChrFlags(0x18, 0x8000)
    SetChrPos(0x18, -201000, -2000, -208900, 270)
    OP_68(-208800, 9500, -208000, 0)
    MoveCamera(35, 25, 0, 0)
    OP_6E(760, 0)
    SetCameraDistance(22000, 0)
    OP_68(-208800, -500, -208000, 10000)
    SetCameraDistance(17000, 10000)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(2000)
    PlaceName2(100, 40, "c_plac54", 0x0, 0)
    OP_6F(0x79)
    Sleep(500)
    Fade(500)
    OP_68(-208300, -1100, -208000, 0)
    MoveCamera(57, 13, 0, 0)
    OP_6E(560, 0)
    SetCameraDistance(17500, 0)
    OP_0D()

    def lambda_24A5():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_24A5)
    Sleep(500)

    ChrTalk(
        0x8,
        (
            "#5P#30WDamn\x01",
            "\"Black moon\" … …!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_24E9():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_24E9)
    Sleep(500)

    ChrTalk(
        0xE,
        (
            "#11P#30WAre you stupid?\x01",
            "Why are they …!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    ChrTalk(
        0x10,
        (
            "#6P#00607F──Tsao支社長！\x01",
            "They have serious suspicion!\x02\x03",
            "Even if the Representative's power of attorney\x01",
            "There should be no right to take along!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#03204F#11PHuh, even if so told\x01",
            "Elders - It is a mission from the top.\x02\x03",
            "#03210FIf you do not seem convinced\x01",
            "It is fine even if you are exercising your ability.\x02\x03",
            "If there is \"Wind sword of the wind\" there\x01",
            "It will be a good game with our friends.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#00700F#5P………… Hun ………………\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#6P#01401F……伝説の凶手《Silver#2Rイン#》。\x01",
            "Is this the first time to match your face?\x02\x03",
            "#01403FOther than that, considerable practice ……\x01",
            "As expected, a minute seems to be bad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#6P#00610F… … cum ……………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#03209F#11PWithout worrying, Huff\x01",
            "もう一方のterroristほど\x01",
            "It should not be terrible eyes.\x02\x03",
            "#03202FAs a political criminal at most\x01",
            "To restrain nationalists\x01",
            "It will only be used.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x8,
        "#5PDo not be silly!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11PBecause of you Toho people\x01",
            "Our Calvert is - ─\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2865():
        OP_99(0xFE, 0xE, 0x258, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_2865)
    WaitChrThread(0x14, 1)

    def lambda_287D():
        OP_96(0xFE, 0xFFFCE000, 0xFFFFF830, 0xFFFCC570, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_287D)
    Sound(811, 0, 100, 0)

    def lambda_289D():
        OP_A6(0xFE, 0x32, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_289D)
    Sleep(500)

    ChrTalk(
        0xE,
        "#11PHuh …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#6P#00606FRock Smith President ……\x01",
            "It looks like a raccoon more than I thought.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#03204F#11PHuh, personally\x01",
            "Although it is a person who feels affinity.\x02\x03",
            "#03210FIf you have complaints or protests\x01",
            "Please go to Cheong Wa Dae … …\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x12, 0x5A, 0x1F4)
    Sleep(150)

    ChrTalk(
        0x12,
        "#6P#03209FLet's increase it.\x02",
    )

    CloseMessageWindow()

    def lambda_29BE():
        TurnDirection(0x13, 0x12, 500)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_29BE)
    Sleep(50)

    def lambda_29CE():
        TurnDirection(0x14, 0x12, 500)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_29CE)
    Sleep(50)

    def lambda_29DE():
        TurnDirection(0x15, 0x12, 500)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_29DE)
    Sleep(50)

    def lambda_29EE():
        TurnDirection(0x16, 0x12, 500)
        ExitThread()

    QueueWorkItem(0x16, 0, lambda_29EE)
    Sleep(50)

    def lambda_29FE():
        TurnDirection(0x17, 0x12, 500)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_29FE)
    Sleep(50)

    def lambda_2A0E():
        TurnDirection(0x18, 0x12, 500)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_2A0E)
    WaitChrThread(0x13, 0)
    WaitChrThread(0x14, 0)
    WaitChrThread(0x15, 0)
    WaitChrThread(0x16, 0)
    WaitChrThread(0x17, 0)
    WaitChrThread(0x18, 0)
    Sleep(50)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    SetMessageWindowPos(280, 20, -1, -1)
    SetChrName("Members")

    AnonymousTalk(
        0xFF,
        "#4SIs!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#00700F#5P………………………………\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(20500, 5500)
    BeginChrThread(0xF, 3, 0, 18)
    Sleep(3500)
    StopSound(133, 2000, 100)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ReplaceBGM(-1, -1)
    SetScenarioFlags(0x23, 1)
    NewScene("c1540", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_17_2161 end

    def Function_18_2AE0(): pass

    label("Function_18_2AE0")

    BeginChrThread(0x17, 3, 0, 23)
    Sleep(300)
    BeginChrThread(0x18, 3, 0, 21)
    Sleep(300)
    BeginChrThread(0x11, 3, 0, 25)
    BeginChrThread(0x15, 3, 0, 22)
    Sleep(600)
    BeginChrThread(0x14, 3, 0, 19)
    Sleep(200)
    BeginChrThread(0x16, 3, 0, 20)
    Sleep(1400)
    BeginChrThread(0x12, 3, 0, 24)
    Sleep(800)
    BeginChrThread(0x13, 3, 0, 24)
    Return()

    # Function_18_2AE0 end

    def Function_19_2B23(): pass

    label("Function_19_2B23")


    def lambda_2B28():
        OP_95(0xFE, -204700, -2000, -210900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_2B28)
    WaitChrThread(0x14, 1)
    SetChrChipByIndex(0xE, 0x20)
    SetChrSubChip(0xE, 0x0)
    OP_93(0xE, 0x0, 0x1F4)

    def lambda_2B55():
        OP_98(0xFE, 0x0, 0x0, 0x34BC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_2B55)

    def lambda_2B6F():
        OP_98(0xFE, 0x0, 0x0, 0x34BC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_2B6F)
    WaitChrThread(0xE, 1)
    WaitChrThread(0x14, 1)

    def lambda_2B91():
        OP_97(0xFE, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_2B91)

    def lambda_2BAB():
        OP_97(0xFE, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_2BAB)
    Return()

    # Function_19_2B23 end

    def Function_20_2BC1(): pass

    label("Function_20_2BC1")


    def lambda_2BC6():
        OP_95(0xFE, -202800, -2000, -210500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_2BC6)
    WaitChrThread(0x16, 1)
    SetChrChipByIndex(0xD, 0x20)
    SetChrSubChip(0xD, 0x0)
    OP_93(0xD, 0x0, 0x1F4)

    def lambda_2BF3():
        OP_98(0xFE, 0x0, 0x0, 0x32C8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_2BF3)

    def lambda_2C0D():
        OP_98(0xFE, 0x0, 0x0, 0x32C8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_2C0D)
    WaitChrThread(0xD, 1)
    WaitChrThread(0x16, 1)

    def lambda_2C2F():
        OP_97(0xFE, 0xFA0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_2C2F)

    def lambda_2C49():
        OP_97(0xFE, 0xFA0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_2C49)
    Return()

    # Function_20_2BC1 end

    def Function_21_2C5F(): pass

    label("Function_21_2C5F")


    def lambda_2C64():
        OP_95(0xFE, -202200, -2000, -207400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_2C64)
    WaitChrThread(0x18, 1)
    OP_93(0x18, 0x0, 0x1F4)
    SetChrChipByIndex(0xC, 0x20)
    SetChrSubChip(0xC, 0x0)
    OP_93(0xC, 0xB4, 0x0)

    def lambda_2C98():
        OP_98(0xFE, 0xFFFFFC18, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_2C98)

    def lambda_2CB2():
        OP_98(0xFE, 0xFFFFFC18, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_2CB2)
    WaitChrThread(0xC, 1)
    WaitChrThread(0x18, 1)

    def lambda_2CD4():
        OP_98(0xFE, 0x0, 0x0, 0x1D4C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_2CD4)

    def lambda_2CEE():
        OP_98(0xFE, 0x0, 0x0, 0x1D4C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_2CEE)
    WaitChrThread(0xC, 1)
    WaitChrThread(0x18, 1)
    OP_93(0xC, 0x10E, 0x0)
    OP_93(0x18, 0x10E, 0x0)

    def lambda_2D1E():
        OP_97(0xFE, 0xFA0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_2D1E)

    def lambda_2D38():
        OP_98(0xFE, 0xFA0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_2D38)
    Return()

    # Function_21_2C5F end

    def Function_22_2D4E(): pass

    label("Function_22_2D4E")


    def lambda_2D53():
        OP_95(0xFE, -204200, -2000, -205900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_2D53)
    WaitChrThread(0x15, 1)
    Fade(250)
    SetChrSubChip(0x9, 0x0)
    SetChrFlags(0x9, 0x20)
    SetChrPos(0x9, -204300, -2200, -206700, 180)

    def lambda_2D90():
        OP_98(0xFE, 0x0, 0x0, 0x2904, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2D90)
    SetChrSubChip(0xB, 0x0)
    SetChrFlags(0xB, 0x20)
    SetChrPos(0xB, -203500, -2200, -206700, 180)

    def lambda_2DC4():
        OP_98(0xFE, 0x0, 0x0, 0x2904, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2DC4)

    def lambda_2DDE():
        OP_98(0xFE, 0x0, 0x0, 0x2904, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_2DDE)
    WaitChrThread(0xB, 1)
    WaitChrThread(0x9, 1)
    WaitChrThread(0x15, 1)

    def lambda_2E04():
        OP_9E(0xFE, 0xFFFCE258, 0xFFFD04B8, 0x15F90, 0x1388, 0x3)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2E04)

    def lambda_2E1F():
        OP_9E(0xFE, 0xFFFCE258, 0xFFFD04B8, 0x15F90, 0x1388, 0x3)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2E1F)

    def lambda_2E3A():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_2E3A)
    WaitChrThread(0xB, 1)
    WaitChrThread(0x9, 1)
    WaitChrThread(0x15, 2)

    def lambda_2E53():
        OP_98(0xFE, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2E53)

    def lambda_2E6D():
        OP_98(0xFE, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2E6D)

    def lambda_2E87():
        OP_98(0xFE, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_2E87)
    WaitChrThread(0xB, 1)
    WaitChrThread(0x9, 1)
    WaitChrThread(0x15, 1)

    def lambda_2EAD():
        OP_9E(0xFE, 0xFFFCF5E0, 0xFFFD04B8, 0xFFFEA070, 0x1388, 0x3)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2EAD)

    def lambda_2EC8():
        OP_9E(0xFE, 0xFFFCF5E0, 0xFFFD04B8, 0xFFFEA070, 0x1388, 0x3)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2EC8)

    def lambda_2EE3():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_2EE3)
    WaitChrThread(0xB, 1)
    WaitChrThread(0x9, 1)
    WaitChrThread(0x15, 2)

    def lambda_2EFC():
        OP_98(0xFE, 0x0, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2EFC)

    def lambda_2F16():
        OP_98(0xFE, 0x0, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2F16)

    def lambda_2F30():
        OP_98(0xFE, 0x0, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_2F30)
    WaitChrThread(0xB, 1)
    WaitChrThread(0x9, 1)
    WaitChrThread(0x15, 1)
    Return()

    # Function_22_2D4E end

    def Function_23_2F52(): pass

    label("Function_23_2F52")


    def lambda_2F57():
        OP_95(0xFE, -204400, -2000, -208000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_2F57)
    WaitChrThread(0x17, 1)
    OP_93(0x17, 0xB4, 0x1F4)
    Fade(250)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x20)
    SetChrPos(0x8, -204500, -2200, -208800, 180)

    def lambda_2F9B():
        OP_98(0xFE, 0x0, 0x0, 0x2CEC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2F9B)
    SetChrSubChip(0xA, 0x0)
    SetChrFlags(0xA, 0x20)
    SetChrPos(0xA, -203700, -2200, -208800, 180)

    def lambda_2FCF():
        OP_98(0xFE, 0x0, 0x0, 0x2CEC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_2FCF)

    def lambda_2FE9():
        OP_98(0xFE, 0x0, 0x0, 0x2CEC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_2FE9)
    WaitChrThread(0x8, 1)
    WaitChrThread(0xA, 1)
    WaitChrThread(0x17, 1)

    def lambda_300F():
        OP_9E(0xFE, 0xFFFCE190, 0xFFFD006C, 0x15F90, 0x1388, 0x3)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_300F)

    def lambda_302A():
        OP_9E(0xFE, 0xFFFCE190, 0xFFFD006C, 0x15F90, 0x1388, 0x3)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_302A)

    def lambda_3045():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_3045)
    WaitChrThread(0x8, 1)
    WaitChrThread(0xA, 1)
    WaitChrThread(0x17, 2)

    def lambda_305E():
        OP_98(0xFE, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_305E)

    def lambda_3078():
        OP_98(0xFE, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_3078)

    def lambda_3092():
        OP_98(0xFE, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_3092)
    WaitChrThread(0x8, 1)
    WaitChrThread(0xA, 1)
    WaitChrThread(0x17, 1)

    def lambda_30B8():
        OP_9E(0xFE, 0xFFFCF518, 0xFFFD006C, 0xFFFEA070, 0x1388, 0x3)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_30B8)

    def lambda_30D3():
        OP_9E(0xFE, 0xFFFCF518, 0xFFFD006C, 0xFFFEA070, 0x1388, 0x3)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_30D3)

    def lambda_30EE():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_30EE)
    WaitChrThread(0x8, 1)
    WaitChrThread(0xA, 1)
    WaitChrThread(0x17, 2)

    def lambda_3107():
        OP_98(0xFE, 0x0, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3107)

    def lambda_3121():
        OP_98(0xFE, 0x0, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_3121)

    def lambda_313B():
        OP_98(0xFE, 0x0, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_313B)
    WaitChrThread(0x8, 1)
    WaitChrThread(0xA, 1)
    WaitChrThread(0x17, 1)
    Return()

    # Function_23_2F52 end

    def Function_24_315D(): pass

    label("Function_24_315D")


    def lambda_3162():
        OP_95(0xFE, -204700, -2000, -207600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3162)
    WaitChrThread(0xFE, 1)

    def lambda_3180():
        OP_95(0xFE, -204700, -2000, -197300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3180)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_24_315D end

    def Function_25_319A(): pass

    label("Function_25_319A")

    OP_93(0xFE, 0x0, 0x1F4)
    SetChrChipByIndex(0x11, 0x27)
    SetChrSubChip(0x11, 0x1)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(700)
    SetChrSubChip(0x11, 0x0)
    SetChrChip(0x0, 0xFE, 0x1E, 0x12C)
    Sound(844, 0, 100, 0)

    def lambda_31CE():
        OP_9C(0xFE, 0x0, 0x1B58, 0x2710, 0x2328, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_31CE)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_25_319A end

    def Function_26_31EB(): pass

    label("Function_26_31EB")

    EventBegin(0x0)
    OP_E2(0x3)
    FadeToDark(0, 0, -1)
    SetChrPos(0x101, -182900, 4000, -199900, 270)
    SetChrPos(0x102, -182900, 4000, -201200, 270)
    SetChrPos(0x103, -181800, 4000, -200000, 270)
    SetChrPos(0x104, -181800, 4000, -198700, 270)
    SetChrPos(0x109, -180700, 4000, -199900, 270)
    SetChrPos(0x105, -180700, 4000, -201200, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x13E, -179400, 4000, -200000, 270)
    OP_68(-191500, -1000, -201500, 0)
    MoveCamera(55, 13, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17000, 0)
    OP_68(-191500, -1000, -201500, 6000)
    MoveCamera(65, 19, 0, 6000)
    SetCameraDistance(20500, 6000)
    FadeToBright(2000, 0)
    OP_6F(0x79)
    Sleep(500)
    Fade(500)
    OP_68(-182000, 4000, -199500, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(760, 0)
    SetCameraDistance(15000, 0)
    OP_68(-211000, 4000, -196000, 9000)
    MoveCamera(65, 13, 0, 9000)
    SetCameraDistance(23000, 9000)
    OP_0D()
    Sleep(5500)
    PlaceName2(340, 200, "c_plac54", 0x0, 0)
    OP_6F(0x79)
    Sleep(1000)
    Fade(500)
    OP_68(-180900, 5000, -200350, 0)
    MoveCamera(60, 25, 0, 0)
    OP_6E(560, 0)
    SetCameraDistance(17500, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#11P#00011FThis … …. It is also a terrific place.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#11P#00200FAccording to the database\x01",
            "Heat treatment plant and garbage incineration place\x01",
            "It seems like an area you built.\x02\x03",
            "#00203FBy drawing water from the Lupine River\x01",
            "While cooling the plant ……\x02\x03",
            "Distribute steam throughout the city\x01",
            "Central heating is\x01",
            "Either way it seems possible.\x02\x03",
            "#00211FTo the end it is the original schedule, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#5PWhat is it?\x01",
            "Only the hako is awful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00106FWell … this area also\x01",
            "It is said that it is fully utilized\x01",
            "It seems to be difficult to say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10305F#11PBut here …\x02\x03",
            "#10301FDuring the Trade Council, Dudley\x01",
            "共和国のterroristたちを\x01",
            "Was not it a tracked place?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_3650():
        TurnDirection(0x101, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3650)
    Sleep(50)

    def lambda_3660():
        TurnDirection(0x102, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_3660)
    Sleep(50)

    def lambda_3670():
        TurnDirection(0x103, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_3670)
    Sleep(50)

    def lambda_3680():
        TurnDirection(0x104, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_3680)
    Sleep(50)

    def lambda_3690():
        TurnDirection(0x109, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3690)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)

    ChrTalk(
        0x101,
        "#6P#00001Fby the way……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FCertainly \"Black Moon\" is overcome\x01",
            "I did it ……\x02\x03",
            "#10108FSomewhat like a long time ago\x01",
            "I can imagine … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00108FIt's only about 2 months\x01",
            "Even though it has not passed …\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_63(0x13E, 0x0, 1700, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0x109)
    OP_64(0x105)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x13E,
        (
            "#02311F#11POh, it's already soaked in sentiment\x01",
            "It's a shitty last!\x02\x03",
            "#02310FIt's hot and it's going to be bullshittish\x01",
            "That's why I do not like real …\x02\x03",
            "#02306FIf the air conditioning in the terminal room is broken by this\x01",
            "I'm seriously deaf …\x02",
        )
    )

    CloseMessageWindow()

    def lambda_38E6():
        TurnDirection(0x102, 0x13E, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_38E6)
    Sleep(50)

    def lambda_38F6():
        TurnDirection(0x109, 0x13E, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_38F6)
    Sleep(50)

    def lambda_3906():
        TurnDirection(0x105, 0x13E, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_3906)
    Sleep(50)

    def lambda_3916():
        TurnDirection(0x104, 0x13E, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_3916)
    Sleep(50)

    def lambda_3926():
        TurnDirection(0x103, 0x13E, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_3926)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x103, 0)

    ChrTalk(
        0x101,
        "#6P#00006FYou …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00211F#6PIf you have so much complaints\x01",
            "Shall I turn back?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13E,
        (
            "#02309F#11PUso!\x01",
            "I do not have any complaints!\x02\x03",
            "#02302F\"Fourth control terminal\"\x01",
            "It should be at the very end of the area.\x02\x03",
            "Finally coming out\x01",
            "Let's hit a cool wind!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00306FGeez……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10112F#6PHehu ……\x01",
            "Shall we go.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -181000, 4000, -200000, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x181, 5)
    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_26_31EB end

    def Function_27_3AAF(): pass

    label("Function_27_3AAF")

    EventBegin(0x0)
    OP_E2(0x3)
    FadeToDark(0, 0, -1)
    OP_68(-400000, -900, -579300, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(560, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x101, -400000, -2000, -577000, 180)
    SetChrPos(0x102, -400000, -2000, -577000, 180)
    SetChrPos(0x103, -400000, -2000, -577000, 180)
    SetChrPos(0x104, -400000, -2000, -577000, 180)
    SetChrPos(0x109, -400000, -2000, -577000, 180)
    SetChrPos(0x105, -400000, -2000, -577000, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x13E, -400000, -2000, -577000, 180)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x13E, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(-399150, -900, -583440, 6000)
    SetCameraDistance(18500, 6000)
    FadeToBright(1000, 0)
    Sleep(500)
    Sound(102, 0, 100, 0)
    ClearMapObjFlags(0xC, 0x10)
    OP_71(0xC, 0x0, 0xA, 0x0, 0x0)
    OP_79(0xC)
    BeginChrThread(0x101, 3, 0, 28)
    Sleep(500)
    BeginChrThread(0x102, 3, 0, 29)
    Sleep(500)
    BeginChrThread(0x103, 3, 0, 30)
    Sleep(500)
    BeginChrThread(0x104, 3, 0, 31)
    Sleep(500)
    BeginChrThread(0x109, 3, 0, 32)
    Sleep(500)
    BeginChrThread(0x105, 3, 0, 33)
    Sleep(700)

    def lambda_3C3F():
        OP_96(0xFE, 0xFFF9E580, 0xFFFFF830, 0xFFF71D64, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x13E, 1, lambda_3C3F)

    def lambda_3C59():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13E, 2, lambda_3C59)
    Sleep(1000)
    Sound(102, 0, 100, 0)
    OP_71(0xC, 0xA, 0x0, 0x0, 0x0)
    OP_79(0xC)
    SetMapObjFlags(0xC, 0x10)
    WaitChrThread(0x13E, 1)

    ChrTalk(
        0x101,
        (
            "#5P#00006FHowever, as usual a strange machine\x01",
            "Is it moving? …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#00108FOr blowing a fire ……\x01",
            "I wonder if it is dangerous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5P#00211FApparently \"association\"\x01",
            "It seems not to be a puppet weapon … …\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3D55():
        TurnDirection(0x101, 0x13E, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3D55)
    Sleep(0)

    def lambda_3D65():
        TurnDirection(0x102, 0x13E, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_3D65)
    Sleep(0)

    def lambda_3D75():
        TurnDirection(0x103, 0x13E, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_3D75)
    Sleep(0)

    def lambda_3D85():
        TurnDirection(0x104, 0x13E, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_3D85)
    Sleep(0)

    def lambda_3D95():
        TurnDirection(0x109, 0x13E, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3D95)
    Sleep(0)

    def lambda_3DA5():
        TurnDirection(0x105, 0x13E, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_3DA5)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x13E, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0x109)
    OP_64(0x105)
    OP_64(0x13E)
    OP_63(0x13E, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(500)

    ChrTalk(
        0x13E,
        (
            "#02305F#5PBo, it's not my fault!\x02\x03",
            "#02306FThat's right, the B parcel cleaning machine\x01",
            "I got a runaway … ….\x02\x03",
            "#02310FIt was my first time to enter this area!\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x13E)

    ChrTalk(
        0x104,
        "#00303F#11PSuspected …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10112FI will not be angry with you.\x01",
            "To be honest it's okay?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x13E, 0x109, 500)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x13E,
        "#11P#02311F#4SThat is different from!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#11P#10305Fby the way……\x02\x03",
            "#10300FThis place is the Orkis Tower\x01",
            "It is connected also from the base, is not it?\x02\x03",
            "The option of going from there is\x01",
            "Was not there?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x13E, 0x105, 500)
    Sleep(100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x194, 4)), scpexpr(EXPR_END)), "loc_41F0")

    ChrTalk(
        0x13E,
        (
            "#02306F#6Pあー、例のterroristの件以来、\x01",
            "It seems that the underground was blocked.\x02\x03",
            "From there, the \"fourth control terminal\" also\x01",
            "It seems to be close to mecha mecha\x01",
            "I think I could go alone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00203FCertainly, in the direction of the D block\x01",
            "The route was also blockade.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x13E, 0x101, 500)
    Sleep(100)

    ChrTalk(
        0x13E,
        (
            "#02300F#5PAlso, near the \"fourth control terminal\"\x01",
            "There seems to be a direct lift to the exit.\x02\x03",
            "#02309FIf you start it up,\x01",
            "You do not disturb you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_432B")

    label("loc_41F0")


    ChrTalk(
        0x13E,
        (
            "#02306F#6Pあー、例のterroristの件以来、\x01",
            "It seems that the underground was blocked.\x02\x03",
            "From there, the \"fourth control terminal\" also\x01",
            "It seems to be close to mecha mecha\x01",
            "I think I could go alone.\x02\x03",
            "#02300FAlso, near the \"fourth control terminal\"\x01",
            "There seems to be a direct lift to the exit.\x02\x03",
            "#02309FIf you start it up,\x01",
            "You do not disturb you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_432B")


    ChrTalk(
        0x101,
        "#12P#00006FI am in good condition at all.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00102FHehu ……\x01",
            "Let 's rush ahead.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -400000, -2000, -583500, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x181, 6)
    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_27_3AAF end

    def Function_28_43C0(): pass

    label("Function_28_43C0")


    def lambda_43C5():
        OP_96(0xFE, 0xFFF9E580, 0xFFFFF830, 0xFFF71E90, 0x9C4, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_43C5)

    def lambda_43DF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_43DF)
    WaitChrThread(0xFE, 1)

    def lambda_43F4():
        OP_96(0xFE, 0xFFF9E2F6, 0xFFFFF830, 0xFFF71594, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_43F4)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_28_43C0 end

    def Function_29_440E(): pass

    label("Function_29_440E")


    def lambda_4413():
        OP_96(0xFE, 0xFFF9E580, 0xFFFFF830, 0xFFF71E90, 0x9C4, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4413)

    def lambda_442D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_442D)
    WaitChrThread(0xFE, 1)

    def lambda_4442():
        OP_96(0xFE, 0xFFF9E80A, 0xFFFFF830, 0xFFF71594, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4442)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_29_440E end

    def Function_30_445C(): pass

    label("Function_30_445C")


    def lambda_4461():
        OP_96(0xFE, 0xFFF9E580, 0xFFFFF830, 0xFFF71E90, 0x9C4, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4461)

    def lambda_447B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_447B)
    WaitChrThread(0xFE, 1)

    def lambda_4490():
        OP_95(0xFE, -401650, -2000, -583700, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4490)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_30_445C end

    def Function_31_44B1(): pass

    label("Function_31_44B1")


    def lambda_44B6():
        OP_96(0xFE, 0xFFF9E580, 0xFFFFF830, 0xFFF71E90, 0x9C4, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_44B6)

    def lambda_44D0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_44D0)
    WaitChrThread(0xFE, 1)

    def lambda_44E5():
        OP_95(0xFE, -398350, -2000, -583700, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_44E5)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_31_44B1 end

    def Function_32_4506(): pass

    label("Function_32_4506")


    def lambda_450B():
        OP_96(0xFE, 0xFFF9E580, 0xFFFFF830, 0xFFF71E90, 0x9C4, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_450B)

    def lambda_4525():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4525)
    WaitChrThread(0xFE, 1)

    def lambda_453A():
        OP_95(0xFE, -401300, -2000, -582300, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_453A)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_32_4506 end

    def Function_33_455B(): pass

    label("Function_33_455B")


    def lambda_4560():
        OP_96(0xFE, 0xFFF9E580, 0xFFFFF830, 0xFFF71E90, 0x9C4, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4560)

    def lambda_457A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_457A)
    WaitChrThread(0xFE, 1)

    def lambda_458F():
        OP_95(0xFE, -398700, -2000, -582300, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_458F)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_33_455B end

    def Function_34_45B0(): pass

    label("Function_34_45B0")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x1)
    SoundLoad(931)
    SoundLoad(825)
    OP_68(-183000, 6000, -200000, 0)
    MoveCamera(45, 33, 0, 0)
    OP_6E(900, 0)
    SetCameraDistance(19000, 0)
    ClearMapObjFlags(0x6, 0x10)
    OP_70(0x6, 0xA)
    ClearMapObjFlags(0x17, 0x4)
    OP_75(0x17, 0x2, 0x2328)
    OP_7D(0xFF, 0x7D, 0x69, 0x0, 0x2328)
    Sound(930, 0, 100, 0)
    OP_68(-212000, 6000, -200000, 9000)
    MoveCamera(33, 33, 0, 9000)
    SetCameraDistance(24000, 9000)
    FadeToBright(1000, 0)
    OP_0D()
    BeginChrThread(0x19, 1, 0, 35)
    Sleep(7000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 1)
    NewScene("m0400", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_34_45B0 end

    def Function_35_4668(): pass

    label("Function_35_4668")

    Sound(931, 2, 30, 0)
    Sound(825, 2, 30, 0)
    Sleep(400)
    OP_25(0x3A3, 0x28)
    OP_25(0x339, 0x28)
    Sleep(400)
    OP_25(0x3A3, 0x32)
    OP_25(0x339, 0x32)
    Sleep(400)
    OP_25(0x3A3, 0x3C)
    OP_25(0x339, 0x3C)
    Sleep(400)
    OP_25(0x3A3, 0x46)
    OP_25(0x339, 0x46)
    Sleep(400)
    OP_25(0x3A3, 0x50)
    OP_25(0x339, 0x50)
    Sleep(400)
    OP_25(0x339, 0x5A)
    Sleep(400)
    OP_25(0x339, 0x64)
    Sleep(4200)
    StopSound(931, 1000, 80)
    StopSound(825, 1000, 100)
    Return()

    # Function_35_4668 end

    def Function_36_46C9(): pass

    label("Function_36_46C9")

    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The power seems to be falling.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BF, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4815")

    ChrTalk(
        0x101,
        "#00005F…… It seems not to move.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FThe future is at the base of the Orkis Tower\x01",
            "It should be connected … …\x02\x03",
            "#00103FPerhaps the presidents\x01",
            "I wonder if it is stopping.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00200FIndeed, it seems possible.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FFrom the Geo Front\x01",
            "What breaks into the tower\x01",
            "You seemed better to give up.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BF, 5)

    label("loc_4815")

    TalkEnd(0xFF)
    Return()

    # Function_36_46C9 end

    SaveToFile()

Try(main)
