from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "Terrorist",              # 1
        "Terrorist",              # 2
        "Terrorist",              # 3
        "Terrorist",              # 4
        "Terrorist",              # 5
        "Terrorist",              # 6
        "Terrorist",              # 7
        "Arios",                  # 8
        "Detective Dudley",       # 9
        "Yin",                    # 10
        "Cao",                    # 11
        "Lau",                    # 12
        "Heiyue Member",          # 13
        "Heiyue Member",          # 14
        "Heiyue Member",          # 15
        "Heiyue Member",          # 16
        "Heiyue Member",          # 17
        "SE制御",                 # 18
        "bm0200",                 # 19
        "bm0200",                 # 20
        "bm0200",                 # 21
    ))

    ATBonus("ATBonus_59C", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_4ABF", 8,   6,   10,  4,   4,   4,   4)
    Sepith("Sepith_4AAF", 2,   0,   20,  2,   4,   5,   2)
    Sepith("Sepith_4AB7", 6,   6,   0,   14,  4,   4,   6)

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
        "BattleInfo_80C", 0x0000, 74, 6, 60, 6, 1, 30, 0, "bm0200", "Sepith_4ABF", 40, 30, 20, 10,
        (
            ("ms84900.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_5FC", "MonsterBattlePostion_65C", "ed7450", "ed7453", "ATBonus_59C"),
            ("ms84900.dat", "ms84900.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_5DC", "MonsterBattlePostion_65C", "ed7450", "ed7453", "ATBonus_59C"),
            ("ms84900.dat", "ms84900.dat", "ms84900.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_5FC", "MonsterBattlePostion_65C", "ed7450", "ed7453", "ATBonus_59C"),
            ("ms84900.dat", "ms84900.dat", "ms84900.dat", "ms84900.dat", 0, 0, 0, 0, "MonsterBattlePostion_5DC", "MonsterBattlePostion_65C", "ed7450", "ed7453", "ATBonus_59C"),
        )
    )

    BattleInfo(
        "BattleInfo_67C", 0x0000, 74, 6, 60, 6, 1, 30, 0, "bm0200", "Sepith_4AAF", 40, 30, 20, 10,
        (
            ("ms84800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_5FC", "MonsterBattlePostion_65C", "ed7450", "ed7453", "ATBonus_59C"),
            ("ms84800.dat", "ms84800.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_5DC", "MonsterBattlePostion_65C", "ed7450", "ed7453", "ATBonus_59C"),
            ("ms84800.dat", "ms84800.dat", "ms84800.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_5FC", "MonsterBattlePostion_65C", "ed7450", "ed7453", "ATBonus_59C"),
            ("ms84800.dat", "ms84800.dat", "ms84800.dat", "ms84800.dat", 0, 0, 0, 0, "MonsterBattlePostion_5DC", "MonsterBattlePostion_65C", "ed7450", "ed7453", "ATBonus_59C"),
        )
    )

    BattleInfo(
        "BattleInfo_744", 0x0000, 74, 6, 60, 6, 1, 30, 0, "bm0200", "Sepith_4AB7", 40, 30, 20, 10,
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
        "Function_4_F4D",          # 04, 4
        "Function_5_10AE",         # 05, 5
        "Function_6_1200",         # 06, 6
        "Function_7_1352",         # 07, 7
        "Function_8_14A4",         # 08, 8
        "Function_9_1676",         # 09, 9
        "Function_10_182E",        # 0A, 10
        "Function_11_18BB",        # 0B, 11
        "Function_12_1A54",        # 0C, 12
        "Function_13_1BE2",        # 0D, 13
        "Function_14_1D6F",        # 0E, 14
        "Function_15_1E9F",        # 0F, 15
        "Function_16_202C",        # 10, 16
        "Function_17_215C",        # 11, 17
        "Function_18_2BB4",        # 12, 18
        "Function_19_2BF7",        # 13, 19
        "Function_20_2C95",        # 14, 20
        "Function_21_2D33",        # 15, 21
        "Function_22_2E22",        # 16, 22
        "Function_23_3026",        # 17, 23
        "Function_24_3231",        # 18, 24
        "Function_25_326E",        # 19, 25
        "Function_26_32BF",        # 1A, 26
        "Function_27_3C65",        # 1B, 27
        "Function_28_45FA",        # 1C, 28
        "Function_29_4648",        # 1D, 29
        "Function_30_4696",        # 1E, 30
        "Function_31_46EB",        # 1F, 31
        "Function_32_4740",        # 20, 32
        "Function_33_4795",        # 21, 33
        "Function_34_47EA",        # 22, 34
        "Function_35_48A2",        # 23, 35
        "Function_36_4903",        # 24, 36
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1FC, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EF7")
    Sound(14, 0, 100, 0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x4A, 1)"), scpexpr(EXPR_END)), "loc_E80")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x4A),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1FC, 0)
    OP_E0(0x5, 0x0)
    Jump("loc_EF2")

    label("loc_E80")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x4A),
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

    label("loc_EF2")

    Jump("loc_F41")

    label("loc_EF7")

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

    label("loc_F41")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_DFB end

    def Function_4_F4D(): pass

    label("Function_4_F4D")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1FC, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_107E")
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
            "#56IEarth Sepith x100\x01\x07\x02",
            "#57IWater Sepith x100\x01\x07\x02",
            "#58IFire Sepith x100\x01\x07\x02",
            "#59IWind Sepith x100\x01\x07\x02",
            "#60ITime Sepith x100\x01\x07\x02",
            "#61ISpace Sepith x100\x01\x07\x02",
            "#62IMirage Sepith x100\x01\x07\x00",
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x1FC, 1)
    OP_E0(0x5, 0x0)
    Jump("loc_109C")

    label("loc_107E")


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

    label("loc_109C")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_F4D end

    def Function_5_10AE(): pass

    label("Function_5_10AE")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1FC, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11AA")
    Sound(14, 0, 100, 0)
    OP_74(0x13, 0x1E)
    OP_71(0x13, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x5EA, 1)"), scpexpr(EXPR_END)), "loc_1133")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x5EA),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1FC, 2)
    OP_E0(0x5, 0x0)
    Jump("loc_11A5")

    label("loc_1133")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x5EA),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " is inside the chest.\x01",
            "Since you have too many, you gave it up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x13, 0x1E, 0x0, 0x0, 0x0)

    label("loc_11A5")

    Jump("loc_11F4")

    label("loc_11AA")

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

    label("loc_11F4")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_10AE end

    def Function_6_1200(): pass

    label("Function_6_1200")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E9, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12FC")
    Sound(14, 0, 100, 0)
    OP_74(0x15, 0x1E)
    OP_71(0x15, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1FA, 1)"), scpexpr(EXPR_END)), "loc_1285")
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
    SetScenarioFlags(0x1E9, 6)
    OP_E0(0x5, 0x0)
    Jump("loc_12F7")

    label("loc_1285")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1FA),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " is inside the chest.\x01",
            "Since you have too many, you gave it up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x15, 0x1E, 0x0, 0x0, 0x0)

    label("loc_12F7")

    Jump("loc_1346")

    label("loc_12FC")

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

    label("loc_1346")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_1200 end

    def Function_7_1352(): pass

    label("Function_7_1352")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E9, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_144E")
    Sound(14, 0, 100, 0)
    OP_74(0x16, 0x1E)
    OP_71(0x16, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1FD, 1)"), scpexpr(EXPR_END)), "loc_13D7")
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
    SetScenarioFlags(0x1E9, 7)
    OP_E0(0x5, 0x0)
    Jump("loc_1449")

    label("loc_13D7")

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
    OP_71(0x16, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1449")

    Jump("loc_1498")

    label("loc_144E")

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

    label("loc_1498")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_1352 end

    def Function_8_14A4(): pass

    label("Function_8_14A4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3D)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1675")
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
        "#11P#02305FHm? Planning to go out?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FYeah, just for a little bit though. After we finish \x01",
            "our preparations, we'll be back immediately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13E,
        (
            "#11P#02306FTsk, do it fast.\x01",
            "I'll wait here for you.\x02",
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

    label("loc_1675")

    Return()

    # Function_8_14A4 end

    def Function_9_1676(): pass

    label("Function_9_1676")

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
            "#11P#02305FOh, it looks like you've come back.\x02\x03",
            "#02302FThen, let's head over to the\x01",
            "No. 4 control terminal at once!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FYeah, got it.\x01",
            "Follow us closely, ok?\x02",
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

    # Function_9_1676 end

    def Function_10_182E(): pass

    label("Function_10_182E")

    EventBegin(0x1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a ladder.\x01",
            "Climb it?\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18B8")
    FadeToDark(500, 0, -1)
    OP_0D()
    EventEnd(0x5)
    OP_C9(0x0, 0x1000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_18AA")
    NewScene("c120D", 105, 0, 0)
    IdleLoop()
    Jump("loc_18B3")

    label("loc_18AA")

    NewScene("c1200", 108, 0, 0)
    IdleLoop()

    label("loc_18B3")

    Jump("loc_18BA")

    label("loc_18B8")

    EventEnd(0x5)

    label("loc_18BA")

    Return()

    # Function_10_182E end

    def Function_11_18BB(): pass

    label("Function_11_18BB")

    SetMapFlags(0x8000000)
    EventBegin(0x1)
    SoundLoad(144)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is an elevator control panel.\x01",
            "Operate it?\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A4C")
    Fade(500)
    SetChrPos(0x0, 1400, 2000, 5300, 90)
    SetChrPos(0x1, 1400, 2000, 6300, 90)
    SetChrPos(0x2, 0, 2000, 5300, 90)
    SetChrPos(0x3, 0, 2000, 6300, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3D)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_198D")
    SetChrPos(0x13E, -1000, 2000, 5800, 90)

    label("loc_198D")

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

    label("loc_1A4C")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_11_18BB end

    def Function_12_1A54(): pass

    label("Function_12_1A54")

    SetMapFlags(0x8000000)
    EventBegin(0x1)
    SoundLoad(144)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is an elevator control panel.\x01",
            "Operate it?\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BDA")
    Fade(500)
    SetChrPos(0x0, 1400, -20000, 5300, 90)
    SetChrPos(0x1, 1400, -20000, 6300, 90)
    SetChrPos(0x2, 200, -20000, 5300, 90)
    SetChrPos(0x3, 200, -20000, 6300, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3D)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B26")
    SetChrPos(0x13E, -1000, -20000, 5800, 90)

    label("loc_1B26")

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

    label("loc_1BDA")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_12_1A54 end

    def Function_13_1BE2(): pass

    label("Function_13_1BE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1BF4")
    Call(0, 36)
    Return()

    label("loc_1BF4")

    SetMapFlags(0x8000000)
    EventBegin(0x1)
    SoundLoad(144)
    SoundLoad(150)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a lift control panel.\x01",
            "Operate it?\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D67")
    Fade(500)
    SetChrPos(0x0, -387500, 0, -764000, 0)
    SetChrPos(0x1, -388500, 0, -764000, 0)
    SetChrPos(0x2, -387500, 0, -765000, 0)
    SetChrPos(0x3, -388500, 0, -765000, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3D)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1CC4")
    SetChrPos(0x13E, -388000, 0, -766000, 0)

    label("loc_1CC4")

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

    label("loc_1D67")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_13_1BE2 end

    def Function_14_1D6F(): pass

    label("Function_14_1D6F")

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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3D)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E1C")
    SetChrPos(0x13E, -388500, -2500, -753000, 270)

    label("loc_1E1C")

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

    # Function_14_1D6F end

    def Function_15_1E9F(): pass

    label("Function_15_1E9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1EB1")
    Call(0, 36)
    Return()

    label("loc_1EB1")

    SetMapFlags(0x8000000)
    EventBegin(0x1)
    SoundLoad(144)
    SoundLoad(150)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a lift control panel.\x01",
            "Operate it?\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2024")
    Fade(500)
    SetChrPos(0x0, 189000, 0, 241500, 270)
    SetChrPos(0x1, 189000, 0, 242500, 270)
    SetChrPos(0x2, 190000, 0, 241500, 270)
    SetChrPos(0x3, 190000, 0, 242500, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3D)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F81")
    SetChrPos(0x13E, 192500, 0, 242000, 270)

    label("loc_1F81")

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

    label("loc_2024")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_15_1E9F end

    def Function_16_202C(): pass

    label("Function_16_202C")

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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3D)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_20D9")
    SetChrPos(0x13E, 177500, -2500, 250500, 180)

    label("loc_20D9")

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

    # Function_16_202C end

    def Function_17_215C(): pass

    label("Function_17_215C")

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

    def lambda_24A0():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_24A0)
    Sleep(500)

    ChrTalk(
        0x8,
        (
            "#5P#30WKh...\x01",
            "Those damn "Heiyue"...!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_24E6():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_24E6)
    Sleep(500)

    ChrTalk(
        0xE,
        (
            "#11P#30WImpossible...\x01",
            "Why are these guys...!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    ChrTalk(
        0x10,
        (
            "#6P#00607F──Branch Manager Cao!\x01",
            "There're heavy suspicions on those persons!\x02\x03",
            "Even if you have a warrant of attorney\x01",
            "of the Republican government, you don't\x01",
            "have any right to take them away!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#03204F#11PUh uh, even if you say that, these are company\x01",
            "orders from the elders── From the top.\x02\x03",
            "#03210FIf you can't comprehend, I'm fine\x01",
            "with the use of force, you know?\x02\x03",
            "The "Divine Blade of Wind" over there\x01",
            "should be a good match for my friend here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#00700F#5P......Hmph............\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#6P#01401F...The legendary assassin, "Yin".\x01",
            "It's my first time meeting him.\x02\x03",
            "#01403FIn addition, he's quite skilled...\x01",
            "As expected, we're a bit at a disadvantage...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#6P#00610F......Kh............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#03209F#11PUh uh, you can rest assured,\x01",
            "the other terrorists won't\x01",
            "have a bad time.\x02\x03",
            "#03202FAt best, they'll be used as\x01",
            "political offenders to keep\x01",
            "in check the nationalists.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x8,
        "#5PD-Don't screw with us!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11PIt's your Easterners' fault\x01",
            "that our Calvard has──\x02",
        )
    )

    CloseMessageWindow()

    def lambda_291E():
        OP_99(0xFE, 0xE, 0x258, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_291E)
    WaitChrThread(0x14, 1)

    def lambda_2936():
        OP_96(0xFE, 0xFFFCE000, 0xFFFFF830, 0xFFFCC570, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_2936)
    Sound(811, 0, 100, 0)

    def lambda_2956():
        OP_A6(0xFE, 0x32, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_2956)
    Sleep(500)

    ChrTalk(
        0xE,
        "#11PGwoh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#6P#00606FPresident Rocksmith... It seems\x01",
            "he's more a sly fox than I thought.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#03204F#11PUh uh, I personally\x01",
            "feel an affinity.\x02\x03",
            "#03210FIf you have complaints or objections,\x01",
            "please send them to the President's\x01",
            "Executive Office...\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x12, 0x5A, 0x1F4)
    Sleep(150)

    ChrTalk(
        0x12,
        "#6P#03209FThen, let's withdraw.\x02",
    )

    CloseMessageWindow()

    def lambda_2AA1():
        TurnDirection(0x13, 0x12, 500)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_2AA1)
    Sleep(50)

    def lambda_2AB1():
        TurnDirection(0x14, 0x12, 500)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_2AB1)
    Sleep(50)

    def lambda_2AC1():
        TurnDirection(0x15, 0x12, 500)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_2AC1)
    Sleep(50)

    def lambda_2AD1():
        TurnDirection(0x16, 0x12, 500)
        ExitThread()

    QueueWorkItem(0x16, 0, lambda_2AD1)
    Sleep(50)

    def lambda_2AE1():
        TurnDirection(0x17, 0x12, 500)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_2AE1)
    Sleep(50)

    def lambda_2AF1():
        TurnDirection(0x18, 0x12, 500)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_2AF1)
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
        "#4SSir!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#00700F#5P............\x07\x00\x02",
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

    # Function_17_215C end

    def Function_18_2BB4(): pass

    label("Function_18_2BB4")

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

    # Function_18_2BB4 end

    def Function_19_2BF7(): pass

    label("Function_19_2BF7")


    def lambda_2BFC():
        OP_95(0xFE, -204700, -2000, -210900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_2BFC)
    WaitChrThread(0x14, 1)
    SetChrChipByIndex(0xE, 0x20)
    SetChrSubChip(0xE, 0x0)
    OP_93(0xE, 0x0, 0x1F4)

    def lambda_2C29():
        OP_98(0xFE, 0x0, 0x0, 0x34BC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_2C29)

    def lambda_2C43():
        OP_98(0xFE, 0x0, 0x0, 0x34BC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_2C43)
    WaitChrThread(0xE, 1)
    WaitChrThread(0x14, 1)

    def lambda_2C65():
        OP_97(0xFE, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_2C65)

    def lambda_2C7F():
        OP_97(0xFE, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_2C7F)
    Return()

    # Function_19_2BF7 end

    def Function_20_2C95(): pass

    label("Function_20_2C95")


    def lambda_2C9A():
        OP_95(0xFE, -202800, -2000, -210500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_2C9A)
    WaitChrThread(0x16, 1)
    SetChrChipByIndex(0xD, 0x20)
    SetChrSubChip(0xD, 0x0)
    OP_93(0xD, 0x0, 0x1F4)

    def lambda_2CC7():
        OP_98(0xFE, 0x0, 0x0, 0x32C8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_2CC7)

    def lambda_2CE1():
        OP_98(0xFE, 0x0, 0x0, 0x32C8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_2CE1)
    WaitChrThread(0xD, 1)
    WaitChrThread(0x16, 1)

    def lambda_2D03():
        OP_97(0xFE, 0xFA0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_2D03)

    def lambda_2D1D():
        OP_97(0xFE, 0xFA0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_2D1D)
    Return()

    # Function_20_2C95 end

    def Function_21_2D33(): pass

    label("Function_21_2D33")


    def lambda_2D38():
        OP_95(0xFE, -202200, -2000, -207400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_2D38)
    WaitChrThread(0x18, 1)
    OP_93(0x18, 0x0, 0x1F4)
    SetChrChipByIndex(0xC, 0x20)
    SetChrSubChip(0xC, 0x0)
    OP_93(0xC, 0xB4, 0x0)

    def lambda_2D6C():
        OP_98(0xFE, 0xFFFFFC18, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_2D6C)

    def lambda_2D86():
        OP_98(0xFE, 0xFFFFFC18, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_2D86)
    WaitChrThread(0xC, 1)
    WaitChrThread(0x18, 1)

    def lambda_2DA8():
        OP_98(0xFE, 0x0, 0x0, 0x1D4C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_2DA8)

    def lambda_2DC2():
        OP_98(0xFE, 0x0, 0x0, 0x1D4C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_2DC2)
    WaitChrThread(0xC, 1)
    WaitChrThread(0x18, 1)
    OP_93(0xC, 0x10E, 0x0)
    OP_93(0x18, 0x10E, 0x0)

    def lambda_2DF2():
        OP_97(0xFE, 0xFA0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_2DF2)

    def lambda_2E0C():
        OP_98(0xFE, 0xFA0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_2E0C)
    Return()

    # Function_21_2D33 end

    def Function_22_2E22(): pass

    label("Function_22_2E22")


    def lambda_2E27():
        OP_95(0xFE, -204200, -2000, -205900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_2E27)
    WaitChrThread(0x15, 1)
    Fade(250)
    SetChrSubChip(0x9, 0x0)
    SetChrFlags(0x9, 0x20)
    SetChrPos(0x9, -204300, -2200, -206700, 180)

    def lambda_2E64():
        OP_98(0xFE, 0x0, 0x0, 0x2904, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2E64)
    SetChrSubChip(0xB, 0x0)
    SetChrFlags(0xB, 0x20)
    SetChrPos(0xB, -203500, -2200, -206700, 180)

    def lambda_2E98():
        OP_98(0xFE, 0x0, 0x0, 0x2904, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2E98)

    def lambda_2EB2():
        OP_98(0xFE, 0x0, 0x0, 0x2904, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_2EB2)
    WaitChrThread(0xB, 1)
    WaitChrThread(0x9, 1)
    WaitChrThread(0x15, 1)

    def lambda_2ED8():
        OP_9E(0xFE, 0xFFFCE258, 0xFFFD04B8, 0x15F90, 0x1388, 0x3)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2ED8)

    def lambda_2EF3():
        OP_9E(0xFE, 0xFFFCE258, 0xFFFD04B8, 0x15F90, 0x1388, 0x3)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2EF3)

    def lambda_2F0E():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_2F0E)
    WaitChrThread(0xB, 1)
    WaitChrThread(0x9, 1)
    WaitChrThread(0x15, 2)

    def lambda_2F27():
        OP_98(0xFE, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2F27)

    def lambda_2F41():
        OP_98(0xFE, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2F41)

    def lambda_2F5B():
        OP_98(0xFE, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_2F5B)
    WaitChrThread(0xB, 1)
    WaitChrThread(0x9, 1)
    WaitChrThread(0x15, 1)

    def lambda_2F81():
        OP_9E(0xFE, 0xFFFCF5E0, 0xFFFD04B8, 0xFFFEA070, 0x1388, 0x3)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2F81)

    def lambda_2F9C():
        OP_9E(0xFE, 0xFFFCF5E0, 0xFFFD04B8, 0xFFFEA070, 0x1388, 0x3)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2F9C)

    def lambda_2FB7():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_2FB7)
    WaitChrThread(0xB, 1)
    WaitChrThread(0x9, 1)
    WaitChrThread(0x15, 2)

    def lambda_2FD0():
        OP_98(0xFE, 0x0, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2FD0)

    def lambda_2FEA():
        OP_98(0xFE, 0x0, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2FEA)

    def lambda_3004():
        OP_98(0xFE, 0x0, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_3004)
    WaitChrThread(0xB, 1)
    WaitChrThread(0x9, 1)
    WaitChrThread(0x15, 1)
    Return()

    # Function_22_2E22 end

    def Function_23_3026(): pass

    label("Function_23_3026")


    def lambda_302B():
        OP_95(0xFE, -204400, -2000, -208000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_302B)
    WaitChrThread(0x17, 1)
    OP_93(0x17, 0xB4, 0x1F4)
    Fade(250)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x20)
    SetChrPos(0x8, -204500, -2200, -208800, 180)

    def lambda_306F():
        OP_98(0xFE, 0x0, 0x0, 0x2CEC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_306F)
    SetChrSubChip(0xA, 0x0)
    SetChrFlags(0xA, 0x20)
    SetChrPos(0xA, -203700, -2200, -208800, 180)

    def lambda_30A3():
        OP_98(0xFE, 0x0, 0x0, 0x2CEC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_30A3)

    def lambda_30BD():
        OP_98(0xFE, 0x0, 0x0, 0x2CEC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_30BD)
    WaitChrThread(0x8, 1)
    WaitChrThread(0xA, 1)
    WaitChrThread(0x17, 1)

    def lambda_30E3():
        OP_9E(0xFE, 0xFFFCE190, 0xFFFD006C, 0x15F90, 0x1388, 0x3)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_30E3)

    def lambda_30FE():
        OP_9E(0xFE, 0xFFFCE190, 0xFFFD006C, 0x15F90, 0x1388, 0x3)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_30FE)

    def lambda_3119():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_3119)
    WaitChrThread(0x8, 1)
    WaitChrThread(0xA, 1)
    WaitChrThread(0x17, 2)

    def lambda_3132():
        OP_98(0xFE, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3132)

    def lambda_314C():
        OP_98(0xFE, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_314C)

    def lambda_3166():
        OP_98(0xFE, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_3166)
    WaitChrThread(0x8, 1)
    WaitChrThread(0xA, 1)
    WaitChrThread(0x17, 1)

    def lambda_318C():
        OP_9E(0xFE, 0xFFFCF518, 0xFFFD006C, 0xFFFEA070, 0x1388, 0x3)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_318C)

    def lambda_31A7():
        OP_9E(0xFE, 0xFFFCF518, 0xFFFD006C, 0xFFFEA070, 0x1388, 0x3)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_31A7)

    def lambda_31C2():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_31C2)
    WaitChrThread(0x8, 1)
    WaitChrThread(0xA, 1)
    WaitChrThread(0x17, 2)

    def lambda_31DB():
        OP_98(0xFE, 0x0, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_31DB)

    def lambda_31F5():
        OP_98(0xFE, 0x0, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_31F5)

    def lambda_320F():
        OP_98(0xFE, 0x0, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_320F)
    WaitChrThread(0x8, 1)
    WaitChrThread(0xA, 1)
    WaitChrThread(0x17, 1)
    Return()

    # Function_23_3026 end

    def Function_24_3231(): pass

    label("Function_24_3231")


    def lambda_3236():
        OP_95(0xFE, -204700, -2000, -207600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3236)
    WaitChrThread(0xFE, 1)

    def lambda_3254():
        OP_95(0xFE, -204700, -2000, -197300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3254)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_24_3231 end

    def Function_25_326E(): pass

    label("Function_25_326E")

    OP_93(0xFE, 0x0, 0x1F4)
    SetChrChipByIndex(0x11, 0x27)
    SetChrSubChip(0x11, 0x1)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(700)
    SetChrSubChip(0x11, 0x0)
    SetChrChip(0x0, 0xFE, 0x1E, 0x12C)
    Sound(844, 0, 100, 0)

    def lambda_32A2():
        OP_9C(0xFE, 0x0, 0x1B58, 0x2710, 0x2328, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_32A2)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_25_326E end

    def Function_26_32BF(): pass

    label("Function_26_32BF")

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
        "#11P#00011FThis is...another amazing place.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#11P#00200FAccording to the database, it seems\x01",
            "this is an area established with a heat\x01",
            "treatment plant and a waste incinerator.\x02\x03",
            "#00203FBy drawing in water from the Lupinus River,\x01",
            "the plants are continuously cooled...\x02\x03",
            "It appears that one day it could become\x01",
            "the central heating which distributes\x01",
            "steam to all the city areas.\x02\x03",
            "#00211FAt least, according to the original plans.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#5PMore like...\x01",
            "For just bein' a box, it's cool.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00106FRight... This area too...\x01",
            "It seems hard to say it's\x01",
            "been used properly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10305F#11PStill, this place...\x02\x03",
            "#10301FWasn't it where, at the time of the Trade\x01",
            "Conference, Dudley and Arios chased the\x01",
            "Republican terrorists?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_379B():
        TurnDirection(0x101, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_379B)
    Sleep(50)

    def lambda_37AB():
        TurnDirection(0x102, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_37AB)
    Sleep(50)

    def lambda_37BB():
        TurnDirection(0x103, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_37BB)
    Sleep(50)

    def lambda_37CB():
        TurnDirection(0x104, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_37CB)
    Sleep(50)

    def lambda_37DB():
        TurnDirection(0x109, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_37DB)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)

    ChrTalk(
        0x101,
        "#6P#00001FNow that you mention it...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FI think they were forestalled\x01",
            "by the "Heiyue"...\x02\x03",
            "#10108FSomehow I can look at it as something\x01",
            "way back in the past, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00108FNot even two months have\x01",
            "passed from that, right?\x02",
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
            "#02311F#11POh, jeez, leave the\x01",
            "sentimentalism for later!\x02\x03",
            "#02310FIt's hot and humid...\x01",
            "That's why I hate the "real" world...\x02\x03",
            "#02306FI couldn't really bear if the terminal\x01",
            "room air-conditioning broke down...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3A74():
        TurnDirection(0x102, 0x13E, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_3A74)
    Sleep(50)

    def lambda_3A84():
        TurnDirection(0x109, 0x13E, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3A84)
    Sleep(50)

    def lambda_3A94():
        TurnDirection(0x105, 0x13E, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_3A94)
    Sleep(50)

    def lambda_3AA4():
        TurnDirection(0x104, 0x13E, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_3AA4)
    Sleep(50)

    def lambda_3AB4():
        TurnDirection(0x103, 0x13E, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_3AB4)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x103, 0)

    ChrTalk(
        0x101,
        "#6P#00006FListen now...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00211F#6PSince you have such complaints,\x01",
            "should we retrace our steps?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13E,
        (
            "#02309F#11PN-No no no!\x01",
            "No complaints here!\x02\x03",
            "#02302FThe "No. 4 Control Terminal"\x01",
            "should be in the deepest area.\x02\x03",
            "Let's get through here on the double\x01",
            "and get some fresh breeze!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00306F...Man...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10112F#6PUh uh...\x01",
            "Let's go.\x02",
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

    # Function_26_32BF end

    def Function_27_3C65(): pass

    label("Function_27_3C65")

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

    def lambda_3DF5():
        OP_96(0xFE, 0xFFF9E580, 0xFFFFF830, 0xFFF71D64, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x13E, 1, lambda_3DF5)

    def lambda_3E0F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13E, 2, lambda_3E0F)
    Sleep(1000)
    Sound(102, 0, 100, 0)
    OP_71(0xC, 0xA, 0x0, 0x0, 0x0)
    OP_79(0xC)
    SetMapObjFlags(0xC, 0x10)
    WaitChrThread(0x13E, 1)

    ChrTalk(
        0x101,
        (
            "#5P#00006FAt any rate, some strange machines\x01",
            "are running around as always...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#00108FThey spit fire...\x01",
            "Isn't it dangerous?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5P#00211FIt looks like they aren't\x01",
            ""Society" archaism, but...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3F0D():
        TurnDirection(0x101, 0x13E, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3F0D)
    Sleep(0)

    def lambda_3F1D():
        TurnDirection(0x102, 0x13E, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_3F1D)
    Sleep(0)

    def lambda_3F2D():
        TurnDirection(0x103, 0x13E, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_3F2D)
    Sleep(0)

    def lambda_3F3D():
        TurnDirection(0x104, 0x13E, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_3F3D)
    Sleep(0)

    def lambda_3F4D():
        TurnDirection(0x109, 0x13E, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3F4D)
    Sleep(0)

    def lambda_3F5D():
        TurnDirection(0x105, 0x13E, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_3F5D)
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
            "#02305F#5PI-It's not my fault!\x02\x03",
            "#02306FWell, it was me who set the B-Division\x01",
            "cleaning machines haywire, but...\x02\x03",
            "#02310FIt's the first time I've entered this Division!\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x13E)

    ChrTalk(
        0x104,
        "#00303F#11PFishy...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10112FWe aren't angry at all, so it's\x01",
            "fine if you tell us honestly.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x13E, 0x109, 500)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x13E,
        "#11P#02311F#4SI TOLD YOU it's not my fault!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#11P#10305FBy the way...\x02\x03",
            "#10300FThis place is even connected to the\x01",
            "Orchis Tower foundations, right?\x02\x03",
            "Why didn't you choose\x01",
            "to go from there?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x13E, 0x105, 500)
    Sleep(100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x194, 4)), scpexpr(EXPR_END)), "loc_43F7")

    ChrTalk(
        0x13E,
        (
            "#02306F#6PWell, since those terrorists' matter,\x01",
            "it seems the basement was sealed.\x02\x03",
            "The "No. 4 Control Terminal" seems\x01",
            "to be really close from there, so I\x01",
            "think I could've gone even alone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00203FIndeed, the D-Division area\x01",
            "route has been sealed.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x13E, 0x101, 500)
    Sleep(100)

    ChrTalk(
        0x13E,
        (
            "#02300F#5PWell, it also appears that there's a direct lift\x01",
            "to the exit near the "No. 4 Control Terminal".\x02\x03",
            "#02309FAfter we activate that, I won't\x01",
            "cause you any trouble.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4564")

    label("loc_43F7")


    ChrTalk(
        0x13E,
        (
            "#02306F#6PWell, since those terrorists' matter,\x01",
            "it seems the basement was sealed.\x02\x03",
            "The "No. 4 Control Terminal" seems\x01",
            "to be really close from there, so I\x01",
            "think I could've gone even alone.\x02\x03",
            "#02300FWell, it also appears that there's a direct lift\x01",
            "to the exit near the "No. 4 Control Terminal".\x02\x03",
            "#02309FAfter we activate that, I won't\x01",
            "cause you any more trouble.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4564")


    ChrTalk(
        0x101,
        "#12P#00006FHonestly, how unctuous.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00102F*giggle*...\x01",
            "Let's hurry on ahead.\x02",
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

    # Function_27_3C65 end

    def Function_28_45FA(): pass

    label("Function_28_45FA")


    def lambda_45FF():
        OP_96(0xFE, 0xFFF9E580, 0xFFFFF830, 0xFFF71E90, 0x9C4, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_45FF)

    def lambda_4619():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4619)
    WaitChrThread(0xFE, 1)

    def lambda_462E():
        OP_96(0xFE, 0xFFF9E2F6, 0xFFFFF830, 0xFFF71594, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_462E)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_28_45FA end

    def Function_29_4648(): pass

    label("Function_29_4648")


    def lambda_464D():
        OP_96(0xFE, 0xFFF9E580, 0xFFFFF830, 0xFFF71E90, 0x9C4, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_464D)

    def lambda_4667():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4667)
    WaitChrThread(0xFE, 1)

    def lambda_467C():
        OP_96(0xFE, 0xFFF9E80A, 0xFFFFF830, 0xFFF71594, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_467C)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_29_4648 end

    def Function_30_4696(): pass

    label("Function_30_4696")


    def lambda_469B():
        OP_96(0xFE, 0xFFF9E580, 0xFFFFF830, 0xFFF71E90, 0x9C4, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_469B)

    def lambda_46B5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_46B5)
    WaitChrThread(0xFE, 1)

    def lambda_46CA():
        OP_95(0xFE, -401650, -2000, -583700, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_46CA)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_30_4696 end

    def Function_31_46EB(): pass

    label("Function_31_46EB")


    def lambda_46F0():
        OP_96(0xFE, 0xFFF9E580, 0xFFFFF830, 0xFFF71E90, 0x9C4, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_46F0)

    def lambda_470A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_470A)
    WaitChrThread(0xFE, 1)

    def lambda_471F():
        OP_95(0xFE, -398350, -2000, -583700, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_471F)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_31_46EB end

    def Function_32_4740(): pass

    label("Function_32_4740")


    def lambda_4745():
        OP_96(0xFE, 0xFFF9E580, 0xFFFFF830, 0xFFF71E90, 0x9C4, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4745)

    def lambda_475F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_475F)
    WaitChrThread(0xFE, 1)

    def lambda_4774():
        OP_95(0xFE, -401300, -2000, -582300, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4774)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_32_4740 end

    def Function_33_4795(): pass

    label("Function_33_4795")


    def lambda_479A():
        OP_96(0xFE, 0xFFF9E580, 0xFFFFF830, 0xFFF71E90, 0x9C4, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_479A)

    def lambda_47B4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_47B4)
    WaitChrThread(0xFE, 1)

    def lambda_47C9():
        OP_95(0xFE, -398700, -2000, -582300, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_47C9)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_33_4795 end

    def Function_34_47EA(): pass

    label("Function_34_47EA")

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

    # Function_34_47EA end

    def Function_35_48A2(): pass

    label("Function_35_48A2")

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

    # Function_35_48A2 end

    def Function_36_4903(): pass

    label("Function_36_4903")

    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It appears the orbal energy is down.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BF, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A83")

    ChrTalk(
        0x101,
        "#00005F...It looks like it doesn't move.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FThis path should be connected to\x01",
            "the Orchis Tower foundations...\x02\x03",
            "#00103FMaybe the President and\x01",
            "the others have stopped it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00200FI see, it could be possible.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FSeems it's better to give up\x01",
            "the idea to infiltrate the\x01",
            "tower from the Geofront.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BF, 5)

    label("loc_4A83")

    TalkEnd(0xFF)
    Return()

    # Function_36_4903 end

    SaveToFile()

Try(main)
