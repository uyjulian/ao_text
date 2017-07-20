from ScenarioHelper import *

def main():
    CreateScenaFile(
        "t1401.bin",                # FileName
        "t1401",                    # MapName
        "t1401",                    # Location
        0x00BB,                     # MapIndex
        "ed7304",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x1A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 187, 0, 1, 0, 2],
    )

    BuildStringList((
        "t1401",                  # 0
        "tourist",                 # 1
        "tourist",                 # 2
        "tourist",                 # 3
        "tourist",                 # 4
        "SE control",                 # 5
        "bt1410",                 # 6
        "bt1420",                 # 7
        "bt1400",                 # 8
        "bt1400",                 # 9
    ))

    ATBonus("ATBonus_37C", 100, 5, 1, 5, 1, 5, 1, 5, 5, 5, 5, 5, 5, 0, 0, 0)

    Sepith("Sepith_C3DA", 15,  5,   5,   5,   10,  5,   25)
    Sepith("Sepith_C3D2", 10,  6,   6,   6,   1,   4,   10)

    MonsterBattlePostion("MonsterBattlePostion_3CC", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_3D0", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_3D4", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_3D8", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_3DC", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_3E0", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_3E4", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_3E8", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_42C", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_430", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_434", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_438", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_43C", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_440", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_444", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_448", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_3AC", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_3B0", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_3B4", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_3B8", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_3BC", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_3C0", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_3C4", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_3C8", 2, 13, 180)

    # monster count: 6

    BattleInfo(
        "BattleInfo_6A4", 0x0000, 78, 6, 60, 6, 1, 20, 0, "bt1400", "Sepith_C3DA", 40, 30, 20, 10,
        (
            ("ms79600.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3CC", "MonsterBattlePostion_42C", "ed7450", "ed7453", "ATBonus_37C"),
            ("ms79600.dat", "ms82300.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3AC", "MonsterBattlePostion_42C", "ed7450", "ed7453", "ATBonus_37C"),
            ("ms79600.dat", "ms82300.dat", "ms82300.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_3CC", "MonsterBattlePostion_42C", "ed7450", "ed7453", "ATBonus_37C"),
            ("ms79600.dat", "ms82300.dat", "ms82300.dat", "ms82300.dat", 0, 0, 0, 0, "MonsterBattlePostion_3AC", "MonsterBattlePostion_42C", "ed7450", "ed7453", "ATBonus_37C"),
        )
    )

    BattleInfo(
        "BattleInfo_5DC", 0x0000, 78, 6, 45, 6, 1, 20, 0, "bt1400", "Sepith_C3D2", 40, 30, 20, 10,
        (
            ("ms82300.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3CC", "MonsterBattlePostion_42C", "ed7450", "ed7453", "ATBonus_37C"),
            ("ms82300.dat", "ms82300.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3AC", "MonsterBattlePostion_42C", "ed7450", "ed7453", "ATBonus_37C"),
            ("ms82300.dat", "ms82300.dat", "ms82300.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_3CC", "MonsterBattlePostion_42C", "ed7450", "ed7453", "ATBonus_37C"),
            ("ms82300.dat", "ms82300.dat", "ms82300.dat", "ms82300.dat", 0, 0, 0, 0, "MonsterBattlePostion_3AC", "MonsterBattlePostion_42C", "ed7450", "ed7453", "ATBonus_37C"),
        )
    )

    AddCharChip((
        "chr/ch22000.itc",                   # 00
        "chr/ch22100.itc",                   # 01
        "chr/ch24300.itc",                   # 02
        "chr/ch22200.itc",                   # 03
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
        "monster/ch82150.itc",               # 10
        "monster/ch82150.itc",               # 11
        "monster/ch82250.itc",               # 12
        "monster/ch82250.itc",               # 13
        "monster/ch82350.itc",               # 14
        "monster/ch82350.itc",               # 15
        "chr/ch00000.itc",                   # 16
        "chr/ch00000.itc",                   # 17
        "monster/ch79650.itc",               # 18
        "monster/ch79650.itc",               # 19
        "chr/ch00000.itc",                   # 1A
        "chr/ch00000.itc",                   # 1B
        "chr/ch00000.itc",                   # 1C
        "chr/ch00000.itc",                   # 1D
        "chr/ch00000.itc",                   # 1E
        "chr/ch00000.itc",                   # 1F
    ))

    DeclNpc(12500,   4294964296, 4294926896, 270,  389,  0x0, 0,   0,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(12560,   4294964296, 4294928646, 270,  389,  0x0, 0,   1,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(4294964116, 4294966296, 4294954076, 45,   389,  0x0, 0,   2,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(4294965017, 4294966296, 4294954897, 225,  389,  0x0, 0,   3,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(13840,   4294938766, 20500,   0x10100B4,    "BattleInfo_6A4", 0,   24,  0xFFFF, 6,  7)
    DeclMonster(4294953496, 4294937916, 20550,   0x1010168,    "BattleInfo_6A4", 0,   24,  0xFFFF, 6,  7)
    DeclMonster(509320,  4294947226, 0,       0x101010E,    "BattleInfo_6A4", 0,   24,  0xFFFF, 6,  7)
    DeclMonster(488860,  4294948126, 0,       0x101005A,    "BattleInfo_6A4", 0,   24,  0xFFFF, 6,  7)
    DeclMonster(499240,  4294960676, 50,      0x10100B4,    "BattleInfo_6A4", 0,   24,  0xFFFF, 6,  7)
    DeclMonster(481090,  4294964406, 16000,   0x10100B4,    "BattleInfo_5DC", 0,   20,  0xFFFF, 4,  5)

    DeclActor(515500,  8000,    4294955296, 1200,    515500,  9000,    4294955296, 0x007C, 0,  3,  0x0000)
    DeclActor(0,       44500,   4294966796, 1500,    0,       46500,   4294966796, 0x007C, 0,  12, 0x0000)
    DeclActor(512000,  0,       4294948296, 1200,    512000,  1000,    4294948296, 0x007C, 0,  4,  0x0000)
    DeclActor(4294965076, 40500,   4294940866, 2000,    0,       44000,   4294939246, 0x007C, 0,  19, 0x0000)
    DeclActor(2250,    40500,   4294939246, 2000,    0,       44000,   4294939246, 0x007C, 0,  19, 0x0000)
    DeclActor(0,       44500,   4294966756, 2000,    0,       46000,   4294966756, 0x007C, 0,  22, 0x0000)
    DeclActor(0,       44550,   4294961826, 1500,    0,       44550,   4294961826, 0x007C, 0,  43, 0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 0
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4])                      # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 2
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4])                      # 3
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 4
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 5
    ChipFrameInfo(800, 0, [0, 1, 2, 3, 4, 5])                    # 6
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 7

    ScpFunction((
        "Function_0_87C",          # 00, 0
        "Function_1_934",          # 01, 1
        "Function_2_A5D",          # 02, 2
        "Function_3_11AB",         # 03, 3
        "Function_4_12FC",         # 04, 4
        "Function_5_144D",         # 05, 5
        "Function_6_1487",         # 06, 6
        "Function_7_14C3",         # 07, 7
        "Function_8_14FF",         # 08, 8
        "Function_9_1533",         # 09, 9
        "Function_10_1B7C",        # 0A, 10
        "Function_11_21AE",        # 0B, 11
        "Function_12_21BE",        # 0C, 12
        "Function_13_2564",        # 0D, 13
        "Function_14_25D3",        # 0E, 14
        "Function_15_2642",        # 0F, 15
        "Function_16_26AB",        # 10, 16
        "Function_17_271A",        # 11, 17
        "Function_18_43F2",        # 12, 18
        "Function_19_5126",        # 13, 19
        "Function_20_5168",        # 14, 20
        "Function_21_547F",        # 15, 21
        "Function_22_54B1",        # 16, 22
        "Function_23_55BE",        # 17, 23
        "Function_24_5628",        # 18, 24
        "Function_25_5648",        # 19, 25
        "Function_26_5661",        # 1A, 26
        "Function_27_567A",        # 1B, 27
        "Function_28_56D8",        # 1C, 28
        "Function_29_615B",        # 1D, 29
        "Function_30_6B01",        # 1E, 30
        "Function_31_7409",        # 1F, 31
        "Function_32_7420",        # 20, 32
        "Function_33_7E1A",        # 21, 33
        "Function_34_884C",        # 22, 34
        "Function_35_9037",        # 23, 35
        "Function_36_904E",        # 24, 36
        "Function_37_9A36",        # 25, 37
        "Function_38_A400",        # 26, 38
        "Function_39_AE2D",        # 27, 39
        "Function_40_B7D8",        # 28, 40
        "Function_41_C29F",        # 29, 41
        "Function_42_C2EC",        # 2A, 42
        "Function_43_C339",        # 2B, 43
    ))


    def Function_0_87C(): pass

    label("Function_0_87C")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_8BC"),
        (1, "loc_8C8"),
        (2, "loc_8D4"),
        (3, "loc_8E0"),
        (4, "loc_8EC"),
        (5, "loc_8F8"),
        (6, "loc_904"),
        (SWITCH_DEFAULT, "loc_910"),
    )


    label("loc_8BC")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_91C")

    label("loc_8C8")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_91C")

    label("loc_8D4")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_91C")

    label("loc_8E0")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_91C")

    label("loc_8EC")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_91C")

    label("loc_8F8")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_91C")

    label("loc_904")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_91C")

    label("loc_910")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_91C")

    label("loc_91C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_933")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_91C")

    label("loc_933")

    Return()

    # Function_0_87C end

    def Function_1_934(): pass

    label("Function_1_934")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_942")
    Jump("loc_9D5")

    label("loc_942")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 7)), scpexpr(EXPR_END)), "loc_950")
    Jump("loc_9D5")

    label("loc_950")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_95E")
    Jump("loc_9D5")

    label("loc_95E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_994")
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x10)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x10)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x10)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x10)
    Jump("loc_9D5")

    label("loc_994")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_9A2")
    Jump("loc_9D5")

    label("loc_9A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_9B0")
    Jump("loc_9D5")

    label("loc_9B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_9BE")
    Jump("loc_9D5")

    label("loc_9BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_9CC")
    Jump("loc_9D5")

    label("loc_9CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_9D5")

    label("loc_9D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9EB")
    Event(0, 9)
    Jump("loc_A05")

    label("loc_9EB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6C), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A05")
    Event(0, 10)

    label("loc_A05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_A14")
    ClearScenarioFlags(0x22, 0)
    Event(0, 17)

    label("loc_A14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A42")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x70), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x40000000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A42")
    Event(0, 18)

    label("loc_A42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 5)), scpexpr(EXPR_END)), "loc_A5C")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A5C")
    SetScenarioFlags(0x194, 3)

    label("loc_A5C")

    Return()

    # Function_1_934 end

    def Function_2_A5D(): pass

    label("Function_2_A5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A79")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0xFB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A8B")

    label("loc_A79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_A8B")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x15F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A8B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6C), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6D), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6E), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x70), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_ACB")
    SetMapFlags(0x80000000)

    label("loc_ACB")

    OP_52(0x12, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xA1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xA1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xA1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xA1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xA1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xA1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xA1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xA1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xB, 0x4)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xC, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_FD9")
    ClearMapObjFlags(0x9, 0x4)
    ClearMapObjFlags(0xB, 0x4)
    ClearMapObjFlags(0xA, 0x4)
    ClearMapObjFlags(0xC, 0x4)

    label("loc_FD9")

    ClearMapObjFlags(0x1, 0x10)
    ClearMapObjFlags(0x5, 0x10)
    ClearMapObjFlags(0x6, 0x10)
    ClearMapObjFlags(0x7, 0x10)
    ClearMapObjFlags(0x8, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 5)), scpexpr(EXPR_END)), "loc_1031")
    OP_70(0x1, 0x0)
    OP_70(0x5, 0x1E)
    OP_70(0x6, 0x1E)
    ClearMapObjFlags(0x5, 0x2)
    ClearMapObjFlags(0x6, 0x2)
    OP_70(0x7, 0x1E)
    OP_70(0x8, 0x1E)
    ClearMapObjFlags(0x7, 0x2)
    ClearMapObjFlags(0x8, 0x2)
    Jump("loc_103B")

    label("loc_1031")

    OP_70(0x1, 0x1E)
    ClearMapObjFlags(0x1, 0x2)

    label("loc_103B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x194, 3)), scpexpr(EXPR_END)), "loc_104E")
    OP_70(0x1, 0x1E)
    ClearMapObjFlags(0x1, 0x2)

    label("loc_104E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1082")
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x80000000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1082")
    SetMapObjFrame(0xFF, "Null_bell", 0x2, "move")

    label("loc_1082")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1095")
    OP_1B(0x0, 0x0, 0x29)

    label("loc_1095")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LEQ), scpexpr(EXPR_END)), "loc_10AD")
    SetMapFlags(0x2000)
    Jump("loc_10B2")

    label("loc_10AD")

    ClearMapFlags(0x2000)

    label("loc_10B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_10C5")
    OP_1B(0xC, 0x0, 0x2A)
    Jump("loc_10CA")

    label("loc_10C5")

    OP_1B(0xC, 0xFF, 0xFFFF)

    label("loc_10CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1FD, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10DD")
    OP_70(0x0, 0x0)
    Jump("loc_10E1")

    label("loc_10DD")

    OP_70(0x0, 0x1E)

    label("loc_10E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1FD, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10F4")
    OP_70(0x2, 0x0)
    Jump("loc_10F8")

    label("loc_10F4")

    OP_70(0x2, 0x1E)

    label("loc_10F8")

    OP_65(0x1, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_110E")
    OP_66(0x1, 0x1)

    label("loc_110E")

    OP_65(0x3, 0x1)
    OP_65(0x4, 0x1)
    OP_65(0x5, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1148")
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x80000000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1144")
    OP_66(0x3, 0x1)
    OP_66(0x4, 0x1)

    label("loc_1144")

    OP_66(0x5, 0x1)

    label("loc_1148")

    LoadEffect(0x10, "event\\eva00_00.eff")
    OP_65(0x6, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18A, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_11AA")
    PlayEffect(0x10, 0x9, 0xFF, 0x0, 0, 44550, -5470, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x6, 0x1)

    label("loc_11AA")

    Return()

    # Function_2_A5D end

    def Function_3_11AB(): pass

    label("Function_3_11AB")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1FD, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12AB")
    Sound(14, 0, 100, 0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('圣灵药·改', 1)"), scpexpr(EXPR_END)), "loc_1234")
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
    SetScenarioFlags(0x1FD, 0)
    OP_E0(0x5, 0x0)
    Jump("loc_12A6")

    label("loc_1234")

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
    OP_71(0x0, 0x1E, 0x0, 0x0, 0x0)

    label("loc_12A6")

    Jump("loc_12F0")

    label("loc_12AB")

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

    label("loc_12F0")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_11AB end

    def Function_4_12FC(): pass

    label("Function_4_12FC")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1FD, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13FC")
    Sound(14, 0, 100, 0)
    OP_74(0x2, 0x1E)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('柔光凉鞋', 1)"), scpexpr(EXPR_END)), "loc_1385")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '柔光凉鞋'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1FD, 1)
    OP_E0(0x5, 0x0)
    Jump("loc_13F7")

    label("loc_1385")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            "In the treasure box",
            scpstr(SCPSTR_CODE_ITEM, '柔光凉鞋'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Is contained.\x01",
            "Because my belongings are full,",
            scpstr(SCPSTR_CODE_ITEM, '柔光凉鞋'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I gave up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x2, 0x1E, 0x0, 0x0, 0x0)

    label("loc_13F7")

    Jump("loc_1441")

    label("loc_13FC")

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

    label("loc_1441")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_12FC end

    def Function_5_144D(): pass

    label("Function_5_144D")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Oh, it's too beautiful\x01",
            "I will definitely take a look … …\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_5_144D end

    def Function_6_1487(): pass

    label("Function_6_1487")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "That planetarium,\x01",
            "What a beautiful thing ……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_6_1487 end

    def Function_7_14C3(): pass

    label("Function_7_14C3")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Huhu, even if it does not panicked\x01",
            "\"Mirror\" will not run away.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_7_14C3 end

    def Function_8_14FF(): pass

    label("Function_8_14FF")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Mommy, get well soon!\x01",
            "This is the staircase!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_8_14FF end

    def Function_9_1533(): pass

    label("Function_9_1533")

    EventBegin(0x0)
    OP_E2(0x3)
    FadeToDark(0, 0, -1)
    SetChrPos(0x101, 0, -1000, -51000, 0)
    SetChrPos(0x102, -1000, -1000, -51500, 0)
    SetChrPos(0x103, 1000, -1000, -52500, 0)
    SetChrPos(0x104, 0, -1000, -53500, 0)
    OP_68(0, 0, -30000, 0)
    MoveCamera(27, 52, 0, 0)
    OP_6E(540, 0)
    SetCameraDistance(49130, 0)
    FadeToBright(1000, 0)
    OP_68(0, 1000, -34000, 12000)
    MoveCamera(330, 16, 0, 12000)
    SetCameraDistance(47500, 12000)
    Sleep(7000)
    PlaceName2(340, 200, "c_plac47", 0x0, 0)
    Sleep(2000)

    def lambda_15FD():
        OP_9B(0x0, 0x101, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_15FD)
    Sleep(50)

    def lambda_1615():
        OP_9B(0x0, 0x102, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1615)
    Sleep(50)

    def lambda_162D():
        OP_9B(0x0, 0x103, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_162D)
    Sleep(50)

    def lambda_1645():
        OP_9B(0x0, 0x104, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1645)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    OP_6F(0x79)
    OP_0D()
    Sleep(500)
    Fade(1000)
    OP_68(0, 3200, -47500, 0)
    MoveCamera(0, 11, 0, 0)
    OP_6E(540, 0)
    SetCameraDistance(18000, 0)
    SetChrPos(0x101, 100, -1000, -46000, 0)
    SetChrPos(0x102, -1150, -1000, -46900, 0)
    SetChrPos(0x103, 1200, -1000, -47100, 0)
    SetChrPos(0x104, -100, -1000, -48000, 0)
    OP_68(0, 1200, -47500, 3000)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x102,
        "#00101F#6PThis light is..\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00201F#12PApparently Spiritual Particles\x01",
            "It seems like you climb up …\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1876")
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(0, 1700, -40000, 1800)
    Sleep(1000)
    Fade(1000)
    OP_68(0, 3000, -13000, 0)
    MoveCamera(0, 26, 0, 0)
    OP_6E(540, 0)
    SetCameraDistance(39000, 0)
    SetCameraDistance(37500, 5000)
    OP_0D()
    Sleep(500)
    SetMessageWindowPos(100, 140, -1, -1)

    AnonymousTalk(
        0x101,
        "#00013FThe main entrance to the stairs!\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(200, 140, -1, -1)

    AnonymousTalk(
        0x104,
        (
            "#00306FYeah… it's sealed up\x02\x03",
            "#00301FInstead of left and right\x01",
            "The entrance appears … …\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_19CF")

    label("loc_1876")

    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(0, 1700, -40000, 1800)
    Sleep(1000)
    Fade(1000)
    OP_68(0, 3000, -13000, 0)
    MoveCamera(0, 26, 0, 0)
    OP_6E(540, 0)
    SetCameraDistance(39000, 0)
    SetCameraDistance(37500, 5000)
    OP_0D()
    Sleep(500)
    SetMessageWindowPos(200, 140, -1, -1)

    AnonymousTalk(
        0x104,
        (
            "#00301FChit, the internal structure\x01",
            "You will be changing …!\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(100, 140, -1, -1)

    AnonymousTalk(
        0x101,
        "#00005FIs it so……?\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(200, 140, -1, -1)

    AnonymousTalk(
        0x104,
        (
            "#00303FOh, when I got in front\x01",
            "The front entrance was open … …\x02\x03",
            "#00301FInstead right now\x01",
            "The entrance appears … …\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_19CF")

    Fade(1000)
    OP_68(0, 1200, -47500, 0)
    MoveCamera(0, 11, 0, 0)
    OP_6E(540, 0)
    SetCameraDistance(18000, 0)
    OP_0D()

    ChrTalk(
        0x102,
        (
            "#00106F#6PAlthough I have been there several times\x01",
            "I thought that there was such a mechanism ……\x02\x03",
            "#00108FThis would be \"her\" doing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F#12P… … From the back\x01",
            "I hear strange working sounds.\x02\x03",
            "#00201FIf we're going on we have to be careful\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#5PAnyhow anyhow\x01",
            "There is no choice but to reach the top floor …\x02\x03",
            "#00013FI asked Arios,\x01",
            "Even to regain Ka'a …!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 0, -1000, -46000, 0)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x183, 1)
    OP_29(0xAD, 0x1, 0x4)
    OP_E2(0x2)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_9_1533 end

    def Function_10_1B7C(): pass

    label("Function_10_1B7C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x101, -19000, 40500, -33500, 90)
    SetChrPos(0x102, -20150, 40500, -33500, 90)
    SetChrPos(0x103, -19500, 40500, -34650, 90)
    SetChrPos(0x104, -20650, 40500, -34650, 90)
    OP_68(-14500, 42000, -34000, 0)
    MoveCamera(0, 21, 0, 0)
    OP_6E(640, 0)
    SetCameraDistance(17500, 0)
    SetCameraDistance(17000, 3000)
    FadeToBright(1000, 0)
    BeginChrThread(0x101, 3, 0, 11)
    Sleep(50)
    BeginChrThread(0x102, 3, 0, 11)
    Sleep(50)
    BeginChrThread(0x103, 3, 0, 11)
    Sleep(50)
    BeginChrThread(0x104, 3, 0, 11)
    WaitChrThread(0x101, 3)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_1CA2():
        OP_93(0x101, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1CA2)
    Sleep(30)

    def lambda_1CB2():
        OP_93(0x102, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1CB2)
    Sleep(30)

    def lambda_1CC2():
        OP_93(0x103, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1CC2)
    Sleep(30)

    def lambda_1CD2():
        OP_93(0x104, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1CD2)
    Sleep(30)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    Fade(1000)
    OP_68(0, 43500, -30500, 0)
    MoveCamera(36, 33, 0, 0)
    OP_6E(640, 0)
    SetCameraDistance(36000, 0)
    OP_68(0, 45900, -14500, 12000)
    MoveCamera(24, 6, 0, 12000)
    OP_6E(640, 12000)
    SetCameraDistance(26000, 12000)
    OP_6F(0x79)
    OP_0D()
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1DBA")
    SetMessageWindowPos(50, 140, -1, -1)

    AnonymousTalk(
        0x101,
        "#00013FWe finally got here\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(230, 140, -1, -1)

    AnonymousTalk(
        0x104,
        "#00301FYeah, the top floor\x02",
    )

    CloseMessageWindow()
    Jump("loc_1E0F")

    label("loc_1DBA")

    SetMessageWindowPos(50, 140, -1, -1)

    AnonymousTalk(
        0x101,
        "#00013FDid you arrive …?\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(230, 140, -1, -1)

    AnonymousTalk(
        0x104,
        (
            "#00301FYeah…\x01",
            "This is the top floor.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E0F")

    SetMessageWindowPos(70, 140, -1, -1)

    AnonymousTalk(
        0x102,
        (
            "#00108FBut,\x01",
            "Ka'a-chan and Arios also\x01",
            "It does not seem to be … …\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Fade(500)
    OP_68(-14500, 42000, -34250, 0)
    MoveCamera(0, 21, 0, 0)
    OP_6E(640, 0)
    SetCameraDistance(14580, 0)
    OP_0D()
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x103)

    ChrTalk(
        0x103,
        (
            "#00206F#6P…… When I visited before\x01",
            "I did not notice … ….\x02\x03",
            "#00201FIn the back of that glowing magnifying glass\x01",
            "There seems to be a hidden space.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_1F8E():
        TurnDirection(0x101, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1F8E)
    Sleep(50)

    def lambda_1F9E():
        TurnDirection(0x102, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1F9E)
    Sleep(50)

    def lambda_1FAE():
        TurnDirection(0x104, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1FAE)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)

    ChrTalk(
        0x101,
        "#00005F#11PSeriously!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F#6PYes, considerable spiritual power\x01",
            "It flows like a whirlpool.\x02\x03",
            "#00201FI think that's the end of the line\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00103F#5PI see..\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00304F#6P…… Apparently somehow\x01",
            "You seemed to catch up … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#11PYeah…\x02\x03",
            "#00007FEveryone - confirm equipment.\x01",
            "I will definitely get back to Ka'aa!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_20F5():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_20F5)
    Sleep(50)

    def lambda_2105():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_2105)
    Sleep(50)

    def lambda_2115():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_2115)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)

    ChrTalk(
        0x102,
        "#00107F#5PRight!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00201F#6PYes!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00307F#6PGot it!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -14000, 40500, -34000, 45)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x183, 2)
    OP_29(0xAD, 0x1, 0x5)
    OP_66(0x1, 0x1)
    EventEnd(0x5)
    Return()

    # Function_10_1B7C end

    def Function_11_21AE(): pass

    label("Function_11_21AE")

    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
    Return()

    # Function_11_21AE end

    def Function_12_21BE(): pass

    label("Function_12_21BE")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    SetChrPos(0x101, 100, 44500, -2000, 0)
    SetChrPos(0x102, -1000, 44500, -3000, 0)
    SetChrPos(0x103, 1000, 44500, -3000, 0)
    SetChrPos(0x104, -100, 44500, -4000, 0)
    LoadChrToIndex("apl/ch51779.itc", 0x1E)
    LoadEffect(0x0, "event\\ev15050.eff")
    OP_68(0, 49700, -2200, 0)
    MoveCamera(0, 11, 0, 0)
    OP_6E(640, 0)
    SetCameraDistance(15480, 0)
    FadeToBright(1000, 0)
    OP_68(-150, 46800, -2200, 3000)
    OP_6F(0x79)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23C9")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Fragments of light are fluttering around the mirror\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    Sleep(500)
    OP_9B(0x0, 0x101, 0x0, 0x1F4, 0x3E8, 0x0)
    Sleep(300)
    Fade(250)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    OP_0D()
    Sound(920, 0, 50, 0)
    Sound(935, 0, 40, 0)
    PlayEffect(0x0, 0xFF, 0x101, 0x0, 0, 1000, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(2500)
    Fade(250)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00006F#6P(Apparently this way\x01",
            "I'm going to be inside the mirror … …)\x02\x03",
            "#00013F(KeA… We're coming!)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x183, 3)
    Jump("loc_2420")

    label("loc_23C9")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Fragments of light are fluttering around the mirror\x02\x03",
            "I am going to put it in the mirror like this.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_2420")

    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Step into the mirror\x01",      # 0
            "Leave the spot\x01",              # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2480"),
        (1, "loc_2539"),
        (SWITCH_DEFAULT, "loc_2563"),
    )


    label("loc_2480")

    SetChrPos(0x101, 0, 44500, -2000, 0)
    Fade(1000)
    OP_68(0, 47500, -2000, 0)
    MoveCamera(0, 15, 0, 0)
    OP_6E(640, 0)
    SetCameraDistance(14700, 0)
    OP_68(0, 47500, -2000, 5000)
    MoveCamera(0, 35, 0, 5000)
    SetCameraDistance(17000, 5000)
    BeginChrThread(0x101, 3, 0, 13)
    Sleep(200)
    BeginChrThread(0x102, 3, 0, 14)
    Sleep(200)
    BeginChrThread(0x103, 3, 0, 15)
    Sleep(200)
    BeginChrThread(0x104, 3, 0, 16)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    OP_6F(0x79)
    OP_0D()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D7(0x1E)
    OP_37()
    NewScene("t1490", 0, 0, 0)
    IdleLoop()
    Jump("loc_2563")

    label("loc_2539")

    FadeToDark(500, 0, -1)
    OP_0D()
    OP_D7(0x1E)
    OP_37()
    SetChrPos(0x0, 0, 44500, -4000, 180)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Jump("loc_2563")

    label("loc_2563")

    Return()

    # Function_12_21BE end

    def Function_13_2564(): pass

    label("Function_13_2564")


    def lambda_2569():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2569)
    Sleep(500)
    Sound(341, 0, 100, 0)

    def lambda_2587():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2587)
    PlayEffect(0x0, 0xFF, 0xFE, 0x0, 0, 1000, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0xFE, 2)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_13_2564 end

    def Function_14_25D3(): pass

    label("Function_14_25D3")


    def lambda_25D8():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_25D8)
    Sleep(1000)

    def lambda_25F0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_25F0)
    Sound(920, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0xFE, 0x0, 0, 1000, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0xFE, 2)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_14_25D3 end

    def Function_15_2642(): pass

    label("Function_15_2642")


    def lambda_2647():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2647)
    Sleep(1000)

    def lambda_265F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_265F)
    PlayEffect(0x0, 0xFF, 0xFE, 0x0, 0, 1000, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0xFE, 2)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_15_2642 end

    def Function_16_26AB(): pass

    label("Function_16_26AB")


    def lambda_26B0():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_26B0)
    Sleep(1500)

    def lambda_26C8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_26C8)
    Sound(920, 0, 60, 0)
    PlayEffect(0x0, 0xFF, 0xFE, 0x0, 0, 1000, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0xFE, 2)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_16_26AB end

    def Function_17_271A(): pass

    label("Function_17_271A")

    EventBegin(0x0)
    OP_E2(0x3)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_40F8")
    SetChrPos(0x101, -500, -950, -51000, 0)
    SetChrPos(0xEF, 500, -950, -51000, 0)
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0xEF, 0x8)
    OP_68(0, 18000, -30000, 0)
    MoveCamera(330, 48, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(40000, 0)
    FadeToBright(1000, 0)
    OP_68(0, 0, -30000, 15000)
    MoveCamera(345, 18, 0, 15000)
    SetCameraDistance(40000, 15000)
    Sleep(9000)
    PlaceName2(340, 200, "c_plac47", 0x0, 0)
    OP_6F(0x79)
    OP_0D()
    Fade(1000)
    ClearChrFlags(0x101, 0x8)
    ClearChrFlags(0xEF, 0x8)
    OP_68(0, 1050, -46000, 0)
    MoveCamera(0, 10, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(16500, 0)
    SetCameraDistance(13500, 3000)

    def lambda_2826():
        OP_9B(0x0, 0x101, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2826)
    Sleep(50)

    def lambda_283E():
        OP_9B(0x0, 0xEF, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_283E)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0xEF, 0)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00000FIs this \"a castle of a mirror\"?\x02\x03",
            "It is also a symbol of the theme park\x01",
            "It seems to be an attraction ….\x02\x03",
            "#00006F… … what he says,\x01",
            "I can only say it is amazing.\x02",
        )
    )

    CloseMessageWindow()
    Switch(
        (scpexpr(EXPR_23, 0x5), scpexpr(EXPR_END)),
        (0, "loc_293D"),
        (1, "loc_2B77"),
        (2, "loc_2D97"),
        (3, "loc_2FBA"),
        (4, "loc_31DF"),
        (5, "loc_3407"),
        (6, "loc_361C"),
        (7, "loc_3857"),
        (8, "loc_3A73"),
        (9, "loc_3C68"),
        (10, "loc_3E68"),
        (SWITCH_DEFAULT, "loc_40F3"),
    )


    label("loc_293D")


    ChrTalk(
        0x102,
        (
            "#00104FOn the planetarium over there,\x01",
            "You seem to make a fantastic atmosphere.\x02\x03",
            "#00100FBy the time I was studying at Libert\x01",
            "I went to the Grand Castle of the Kingdom,\x01",
            "I think that it can not be caught in the atmosphere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FThat's really amazing.\x01",
            "Well as expected IBC …\x02\x03",
            "#00005FBy the way, here\x01",
            "What is \"a mirror that makes a wish come true\"\x01",
            "I was talking about being placed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FYes, when I ring the bell and stand in front of the mirror\x01",
            "It is said that your wish will come true.\x02\x03",
            "#00104FIn the story you heard, on the top floor of the castle\x01",
            "It seems to be placed … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FWell then, for now\x01",
            "Let's go up to the top floor and look for it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FYes, I understand.\x02",
    )

    CloseMessageWindow()
    Jump("loc_40F3")

    label("loc_2B77")


    ChrTalk(
        0x103,
        (
            "#00204FThanks to the central planetarium,\x01",
            "A fantastic aura is born.\x02\x03",
            "#00200FIt's as if it comes out in a fairy tale\x01",
            "It looks like a castle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FOh, it feels like that.\x01",
            "Well as expected IBC …\x02\x03",
            "#00005FBy the way, here\x01",
            "What is \"a mirror that makes a wish come true\"\x01",
            "I was talking about being placed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FIn the story of Ellie,\x01",
            "Ringing the bell and standing in front of the mirror\x01",
            "It seems that your wish will come true.\x02\x03",
            "#00204FAnything, on the top floor of the castle\x01",
            "It is said that it is put … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FWell then, for now\x01",
            "Let's go up to the top floor and look for it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00200FYes, let's go.\x02",
    )

    CloseMessageWindow()
    Jump("loc_40F3")

    label("loc_2D97")


    ChrTalk(
        0x104,
        (
            "#00304FIn the planetarium turning in the center,\x01",
            "It seems that it is directing a fantastic atmosphere.\x02\x03",
            "#00300FHaha, if you're serious enough\x01",
            "Do not look like a real castle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FOh, it really feels like that.\x01",
            "Well as expected IBC …\x02\x03",
            "#00005FBy the way, here\x01",
            "What is \"a mirror that makes a wish come true\"\x01",
            "I was talking about being placed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FOh, when I ring the bell and stand in front of the mirror\x01",
            "It is a thing that a wish comes true.\x02\x03",
            "#00304FBecause it is on the top floor,\x01",
            "I think you can understand it as soon as you go up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FWell then, for now\x01",
            "Let's go up to the top floor and look for it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00300FOh, will you go?\x02",
    )

    CloseMessageWindow()
    Jump("loc_40F3")

    label("loc_2FBA")


    ChrTalk(
        0x109,
        (
            "#10104FAt the center planetarium,\x01",
            "He seems to produce a fantastic atmosphere.\x02\x03",
            "#10100FIf it is real full so far\x01",
            "You look like a real castle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FOh, it really feels like that.\x01",
            "Well as expected IBC …\x02\x03",
            "#00005FBy the way, here\x01",
            "What is \"a mirror that makes a wish come true\"\x01",
            "I was talking about being placed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FYes, when you ring the bell and stand in front of the mirror\x01",
            "I heard that your wish will come true.\x02\x03",
            "#10104FBecause it is on the top floor,\x01",
            "I think that you will soon see if you go up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FWell then, for now\x01",
            "Let's go up to the top floor and look for it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10100FYes, let's go.\x02",
    )

    CloseMessageWindow()
    Jump("loc_40F3")

    label("loc_31DF")


    ChrTalk(
        0x105,
        (
            "#10304FIn the central planetarium,\x01",
            "I am directing a fantastic atmosphere.\x02\x03",
            "#10302FHuh, it sounds like a fancy stuff.\x01",
            "As far as buildings are concerned\x01",
            "It seems that it costs a considerable amount of money, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FOh, I am afraid of IBC's\x01",
            "I will be amazed by the financial strength ……\x02\x03",
            "#00005FBy the way, here\x01",
            "What is \"a mirror that makes a wish come true\"\x01",
            "I was talking about being placed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FOh, when I ring the bell and stand in front of the mirror\x01",
            "It is said that the wish is coming true.\x02\x03",
            "#10304FIt is a story that it is on the top floor,\x01",
            "Do not you see it as soon as you climb?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FWell then, for now\x01",
            "Let's go up to the top floor and look for it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10300FHuh, I understand.\x02",
    )

    CloseMessageWindow()
    Jump("loc_40F3")

    label("loc_3407")


    ChrTalk(
        0x153,
        (
            "#01111FIt is spinning in the middle,\x01",
            "What is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FOh, that is a planetarium.\x01",
            "To produce a fantastic atmosphere\x01",
            "I think it's like a device.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#01105FHuh … … something is terrible.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FOh, I do not have any honest words.\x01",
            "Well as expected IBC ……\x02\x03",
            "#00005FBy the way, here\x01",
            "What is \"a mirror that makes a wish come true\"\x01",
            "I was talking about being placed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#01100FWhat is Ellie saying to Kagami?\x01",
            "Sure, it's at the top of the castle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FOh, for now\x01",
            "Let's go up to the top floor and look for it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#01109FThree!\x02",
    )

    CloseMessageWindow()
    Jump("loc_40F3")

    label("loc_361C")


    ChrTalk(
        0x156,
        (
            "#06404FAnything, with the central planetarium\x01",
            "It seems that it is directing a fantastic atmosphere ~.\x02\x03",
            "#06400FHehe, if you are serious enough\x01",
            "It seems like a real castle, is not it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FOh, it really feels like that.\x01",
            "Well as expected IBC …\x02\x03",
            "#00005FBy the way, here\x01",
            "What is \"a mirror that makes a wish come true\"\x01",
            "I was talking about being placed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x156,
        (
            "#06400FYes, when you ring the bell and stand in front of the mirror\x01",
            "It is said that the wish will come true ~.\x02\x03",
            "#06404FIt is on the top floor,\x01",
            "I think that as soon as you climb it you will understand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FWell then, for now\x01",
            "Let's go up to the top floor and look for it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x156,
        "#06409FYes! Let's go.\x02",
    )

    CloseMessageWindow()
    Jump("loc_40F3")

    label("loc_3857")


    ChrTalk(
        0x14C,
        (
            "#05904FIs there a planetarium in the center?\x01",
            "There is a very fantastic atmosphere.\x02\x03",
            "#05902FHehe, as well as the picture book that I read to Lloyd a long time ago\x01",
            "This castle has come out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000Fmy mother……\x01",
            "It certainly looks like a castle in a fairy tale.\x02\x03",
            "#00005FBy the way, here\x01",
            "What is \"a mirror that makes a wish come true\"\x01",
            "I was talking about being placed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14C,
        (
            "#05900FElly said,\x01",
            "Ringing the bell and standing in front of the mirror\x01",
            "I told you that the wish will come true.\x02\x03",
            "#05904FAnything, on the top floor of the castle\x01",
            "It seems that it is placed … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FWell then, for now\x01",
            "Let's go up to the top floor and look for it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14C,
        "#05900FYes, let's go.\x02",
    )

    CloseMessageWindow()
    Jump("loc_40F3")

    label("loc_3A73")


    ChrTalk(
        0x134,
        (
            "#01704FWith planetarium in the center,\x01",
            "Is it making a fantastic aura …?\x02\x03",
            "#01702FHmm, this time in alkane shell\x01",
            "I wonder if you can use it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FHaha … It seems to be Iria-san.\x02\x03",
            "#00005FBy the way, here\x01",
            "What is \"a mirror that makes a wish come true\"\x01",
            "I was talking about being placed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x134,
        (
            "#01700FOh, when I ring the bell and stand in front of the mirror\x01",
            "It is what a wish comes true.\x02\x03",
            "#01704FIt seems that it is on the top floor of the castle, but ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FWell then, for now\x01",
            "Let's go up to the top floor and look for it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x134,
        "#01709FOkay, let's go!\x02",
    )

    CloseMessageWindow()
    Jump("loc_40F3")

    label("loc_3C68")


    ChrTalk(
        0x135,
        (
            "#01804FIn the central meteorological observation,\x01",
            "I am making a fantastic atmosphere.\x02\x03",
            "#01802FHuhu, if Iria saw it\x01",
            "It might be wanted for the stage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FHaha … … I can imagine easily.\x02\x03",
            "#00005FBy the way, here\x01",
            "What is \"a mirror that makes a wish come true\"\x01",
            "I was talking about being placed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x135,
        (
            "#01805FOh, when I ring the bell and stand in front of the mirror\x01",
            "The wish is coming … …\x02\x03",
            "#01804FIn the story of Ellie, on the top floor of the castle\x01",
            "Although it was said that it was put.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FWell then, for now\x01",
            "Let's go up to the top floor and look for it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x135,
        "#01809FYes, let's go.\x02",
    )

    CloseMessageWindow()
    Jump("loc_40F3")

    label("loc_3E68")


    ChrTalk(
        0x166,
        (
            "#14005FIt is spinning around in the middle,\x01",
            "what's with that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FOh, that is a planetarium.\x01",
            "To produce a fantastic atmosphere\x01",
            "I think it's like a device.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x166,
        (
            "#14000FOh … … well I do not understand\x01",
            "Somehow I can not help it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FOh, I do not have any honest words.\x01",
            "Well as expected IBC ……\x02\x03",
            "#00005FBy the way, here\x01",
            "What is \"a mirror that makes a wish come true\"\x01",
            "I was talking about being placed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x166,
        (
            "#14000FOh, I was talking about it,\x01",
            "Ringing the bell and standing in front of the mirror\x01",
            "It is said that the wish will come true.\x02\x03",
            "#14003FIt seems to be on the top floor of the castle … ….\x01",
            "Do you believe such a thing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FI do not know yet ….\x01",
            "Let's go up to the top floor and look for it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x166,
        "#14000FHm, I'll go out with you.\x02",
    )

    CloseMessageWindow()
    Jump("loc_40F3")

    label("loc_40F3")

    Jump("loc_43DC")

    label("loc_40F8")

    SetChrPos(0x101, -500, -950, -51000, 0)
    SetChrPos(0xEF, 500, -950, -51000, 0)
    OP_68(0, 1050, -46000, 0)
    MoveCamera(0, 10, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(16500, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(13500, 3000)

    def lambda_415F():
        OP_9B(0x0, 0x101, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_415F)
    Sleep(50)

    def lambda_4177():
        OP_9B(0x0, 0xEF, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_4177)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0xEF, 0)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00000FWell then, we are on the top floor together\x01",
            "Let's aim for \"a mirror that will make a wish come true.\"\x02",
        )
    )

    CloseMessageWindow()
    Switch(
        (scpexpr(EXPR_23, 0x5), scpexpr(EXPR_END)),
        (0, "loc_422A"),
        (1, "loc_424E"),
        (2, "loc_4278"),
        (3, "loc_429E"),
        (4, "loc_42C8"),
        (5, "loc_42E6"),
        (6, "loc_4302"),
        (7, "loc_432E"),
        (8, "loc_4358"),
        (9, "loc_4384"),
        (10, "loc_43AE"),
        (SWITCH_DEFAULT, "loc_43DC"),
    )


    label("loc_422A")


    ChrTalk(
        0x102,
        "#00100FYes, I understand.\x02",
    )

    CloseMessageWindow()
    Jump("loc_43DC")

    label("loc_424E")


    ChrTalk(
        0x103,
        "#00200FYes, let's go.\x02",
    )

    CloseMessageWindow()
    Jump("loc_43DC")

    label("loc_4278")


    ChrTalk(
        0x104,
        "#00300FOh, will you go?\x02",
    )

    CloseMessageWindow()
    Jump("loc_43DC")

    label("loc_429E")


    ChrTalk(
        0x109,
        "#10100FYes, let's go.\x02",
    )

    CloseMessageWindow()
    Jump("loc_43DC")

    label("loc_42C8")


    ChrTalk(
        0x105,
        "#10300FHuh, I understand.\x02",
    )

    CloseMessageWindow()
    Jump("loc_43DC")

    label("loc_42E6")


    ChrTalk(
        0x153,
        "#01109FThree!\x02",
    )

    CloseMessageWindow()
    Jump("loc_43DC")

    label("loc_4302")


    ChrTalk(
        0x156,
        "#06409FYes! Let's go.\x02",
    )

    CloseMessageWindow()
    Jump("loc_43DC")

    label("loc_432E")


    ChrTalk(
        0x14C,
        "#05900FYes, let's go.\x02",
    )

    CloseMessageWindow()
    Jump("loc_43DC")

    label("loc_4358")


    ChrTalk(
        0x134,
        "#01709FOkay, let's go!\x02",
    )

    CloseMessageWindow()
    Jump("loc_43DC")

    label("loc_4384")


    ChrTalk(
        0x135,
        "#01802FYes, let's go.\x02",
    )

    CloseMessageWindow()
    Jump("loc_43DC")

    label("loc_43AE")


    ChrTalk(
        0x166,
        "#14000FHm, I'll go out with you.\x02",
    )

    CloseMessageWindow()
    Jump("loc_43DC")

    label("loc_43DC")

    SetChrPos(0x0, 0, -1000, -46000, 0)
    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_17_271A end

    def Function_18_43F2(): pass

    label("Function_18_43F2")

    EventBegin(0x0)
    OP_E2(0x3)
    FadeToDark(0, 0, -1)
    SetChrPos(0x101, 0, 40500, -10450, 180)
    SetChrPos(0xEF, 0, 40500, -10450, 180)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xEF, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearMapObjFlags(0x4, 0x10)
    OP_70(0x4, 0x0)
    OP_68(0, 41500, -10450, 0)
    MoveCamera(0, 30, 0, 0)
    OP_6E(640, 0)
    SetCameraDistance(18000, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(118, 0, 100, 0)
    OP_71(0x4, 0x0, 0x1E, 0x0, 0x8)
    OP_79(0x4)
    OP_68(0, 41500, -15400, 3000)
    SetCameraDistance(14000, 3000)

    def lambda_44AE():
        OP_9B(0x1, 0xFE, 0xFFFA, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_44AE)

    def lambda_44C3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_44C3)
    Sleep(700)

    def lambda_44D7():
        OP_9B(0x1, 0xFE, 0x6, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_44D7)

    def lambda_44EC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xEF, 2, lambda_44EC)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x101, 2)
    WaitChrThread(0xEF, 1)
    WaitChrThread(0xEF, 2)
    Sound(118, 0, 100, 0)
    OP_71(0x4, 0x1E, 0x0, 0x0, 0x8)
    OP_79(0x4)
    SetMapObjFlags(0x4, 0x10)
    OP_6F(0x79)
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4B50")

    ChrTalk(
        0x101,
        "#00000FIs this the top floor of the \"mirror castle\" …?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(0, 42700, -27500, 0)
    MoveCamera(27, 12, 0, 0)
    OP_6E(640, 0)
    SetCameraDistance(19500, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00005FApparently it's over there,\x01",
            "It seems like a \"bell\" that I was talking about.\x02",
        )
    )

    CloseMessageWindow()
    Switch(
        (scpexpr(EXPR_23, 0x5), scpexpr(EXPR_END)),
        (0, "loc_462A"),
        (1, "loc_4698"),
        (2, "loc_4704"),
        (3, "loc_4742"),
        (4, "loc_4780"),
        (5, "loc_47EA"),
        (6, "loc_4852"),
        (7, "loc_4894"),
        (8, "loc_490A"),
        (9, "loc_497A"),
        (10, "loc_49E8"),
        (SWITCH_DEFAULT, "loc_4A54"),
    )


    label("loc_462A")


    ChrTalk(
        0x102,
        (
            "#00100FPimp to ring\x01",
            "It's about left and right.\x02\x03",
            "#00104FIn what I was listening to\x01",
            "There is no mistake.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_4A54")

    label("loc_4698")


    ChrTalk(
        0x103,
        (
            "#00200FPimp to ring\x01",
            "It is attached to the left and right.\x02\x03",
            "#00204FIn what I was listening to\x01",
            "There is no mistake.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_4A54")

    label("loc_4704")


    ChrTalk(
        0x104,
        (
            "#00300FOh, there are also strings for ringing\x01",
            "I'll have it on the left and right.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_4A54")

    label("loc_4742")


    ChrTalk(
        0x109,
        (
            "#10100FYeah, a pimp for ringing too\x01",
            "I am attached to the left and right.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_4A54")

    label("loc_4780")


    ChrTalk(
        0x105,
        (
            "#10300FPimp to ring\x01",
            "It's on the left and right.\x02\x03",
            "#10304FIn what I was listening to\x01",
            "It looks like no mistake.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_4A54")

    label("loc_47EA")


    ChrTalk(
        0x153,
        (
            "#01105FPimp to ring\x01",
            "I'm stuck on the left and right.\x02\x03",
            "#01111FEli was saying\x01",
            "I wonder if that?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_4A54")

    label("loc_4852")


    ChrTalk(
        0x156,
        (
            "#06400FYeah, a pimp for ringing too\x01",
            "It is attached to the left and right ~.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_4A54")

    label("loc_4894")


    ChrTalk(
        0x14C,
        (
            "#05900FPimp to ring\x01",
            "It's about left and right.\x02\x03",
            "#05904FIn what I was listening to\x01",
            "I wonder if there is no mistake.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_4A54")

    label("loc_490A")


    ChrTalk(
        0x134,
        (
            "#01700FPimp to ring\x01",
            "It's about left and right.\x02\x03",
            "#01704FIn what I was listening to\x01",
            "Is not there a mistake?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_4A54")

    label("loc_497A")


    ChrTalk(
        0x135,
        (
            "#01802FPimp to ring\x01",
            "It is attached to the left and right.\x02\x03",
            "#01804FIn what I was listening to\x01",
            "I do not think he will make a mistake.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_4A54")

    label("loc_49E8")


    ChrTalk(
        0x166,
        (
            "#14000FPimp to ring\x01",
            "I have it on the left and right … ….\x02\x03",
            "#14003FBecause I was listening to the story\x01",
            "Is not there a mistake?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_4A54")

    label("loc_4A54")


    def lambda_4A59():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4A59)
    Sleep(50)

    def lambda_4A69():
        OP_93(0xEF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_4A69)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0xEF, 0)
    Fade(500)
    OP_68(0, 45500, -12000, 0)
    MoveCamera(30, 12, 0, 0)
    OP_6E(640, 0)
    SetCameraDistance(30000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00002FThen, that big mirror\x01",
            "\"Mirror that wishes will come true\"?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(0, 41500, -15400, 0)
    MoveCamera(0, 30, 0, 0)
    OP_6E(640, 0)
    SetCameraDistance(14000, 0)
    OP_0D()

    def lambda_4B28():
        OP_93(0x101, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4B28)
    Sleep(50)

    def lambda_4B38():
        OP_93(0xEF, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_4B38)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0xEF, 0)
    Jump("loc_4B75")

    label("loc_4B50")


    ChrTalk(
        0x101,
        "#00000FWell, I arrived at the top floor.\x02",
    )

    CloseMessageWindow()

    label("loc_4B75")

    Switch(
        (scpexpr(EXPR_23, 0x5), scpexpr(EXPR_END)),
        (0, "loc_4BC0"),
        (1, "loc_4C37"),
        (2, "loc_4CAC"),
        (3, "loc_4D20"),
        (4, "loc_4D98"),
        (5, "loc_4E02"),
        (6, "loc_4E6E"),
        (7, "loc_4EE2"),
        (8, "loc_4F4E"),
        (9, "loc_4FB4"),
        (10, "loc_501A"),
        (SWITCH_DEFAULT, "loc_5074"),
    )


    label("loc_4BC0")


    ChrTalk(
        0x102,
        (
            "#00100FRinging the bell and standing in front of the mirror\x01",
            "It seems that the wish will come true … ….\x02\x03",
            "#00104FAt the outset,\x01",
            "I feel nervous somehow.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5074")

    label("loc_4C37")


    ChrTalk(
        0x103,
        (
            "#00200FRinging the bell and standing in front of the mirror\x01",
            "It seems that my wish will come true … …\x02\x03",
            "#00204FAt the outset,\x01",
            "I feel nervous somehow.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5074")

    label("loc_4CAC")


    ChrTalk(
        0x104,
        (
            "#00300FRinging the bell and standing in front of the mirror\x01",
            "It is told that the wish will come true … …\x02\x03",
            "#00304FWell, what kind of wish will it be?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5074")

    label("loc_4D20")


    ChrTalk(
        0x109,
        (
            "#10100FRinging the bell and standing in front of the mirror\x01",
            "It is told that my wish will come true, but …\x02\x03",
            "#10104FWell, what would you like to ask?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5074")

    label("loc_4D98")


    ChrTalk(
        0x105,
        (
            "#10300FRinging the bell and standing in front of the mirror\x01",
            "My wish is coming true … …\x02\x03",
            "#10304FWell, what will happen.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5074")

    label("loc_4E02")


    ChrTalk(
        0x153,
        (
            "#01100FRinging the bell and standing in front of the mirror\x01",
            "The wish will come true.\x02\x03",
            "#01109FKaoru, what shall I ask?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5074")

    label("loc_4E6E")


    ChrTalk(
        0x156,
        (
            "#06400FRinging the bell and standing in front of the mirror\x01",
            "I am told that my wish will come true ~.\x02\x03",
            "#06409FI wonder what I should ask this time ~.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5074")

    label("loc_4EE2")


    ChrTalk(
        0x14C,
        (
            "#05900FRinging the bell and standing in front of the mirror\x01",
            "My wish is coming true … …\x02\x03",
            "#05904FHuhu, what should I ask?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5074")

    label("loc_4F4E")


    ChrTalk(
        0x134,
        (
            "#01700FRinging the bell and standing in front of the mirror\x01",
            "Your wish will come true.\x02\x03",
            "#01702FI wonder what you should ask.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5074")

    label("loc_4FB4")


    ChrTalk(
        0x135,
        (
            "#01803FRinging the bell and standing in front of the mirror\x01",
            "It seems that your wish will come true.\x02\x03",
            "#01808F(But … what a wish.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5074")

    label("loc_501A")


    ChrTalk(
        0x166,
        (
            "#14003FRinging the bell and standing in front of the mirror\x01",
            "Wishes come true … …\x02\x03",
            "#14008F…… Is it true?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5074")

    label("loc_5074")

    Jc((scpexpr(EXPR_23, 0x5), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_50C9")

    ChrTalk(
        0x101,
        (
            "#00000FWell then, for the first time with two people\x01",
            "Let's ring that bell.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5107")

    label("loc_50C9")


    ChrTalk(
        0x101,
        (
            "#00000FWell then, for the first time with two people\x01",
            "Let's ring that bell.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5107")

    OP_D2(0x4, (scpexpr(EXPR_PUSH_LONG, 0x40000000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    SetChrPos(0x0, 0, 40550, -15500, 180)
    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_18_43F2 end

    def Function_19_5126(): pass

    label("Function_19_5126")

    TalkBegin(0xFF)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Sound a bell\x01",      # 0
            "quit\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Sleep(200)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5164")
    Call(0, 20)
    Jump("loc_5164")

    label("loc_5164")

    TalkEnd(0xFF)
    Return()

    # Function_19_5126 end

    def Function_20_5168(): pass

    label("Function_20_5168")

    EventBegin(0x0)
    Fade(500)
    OP_68(0, 42000, -27500, 0)
    MoveCamera(48, 28, 0, 0)
    OP_6E(640, 0)
    SetCameraDistance(13500, 0)
    SetCameraDistance(18500, 5000)
    SetChrPos(0x101, -2450, 40500, -27300, 0)
    SetChrPos(0xEF, 2090, 40500, -28590, 0)
    BeginChrThread(0xC, 1, 0, 21)
    SetMapObjFrame(0xFF, "Null_bell", 0x2, "move")
    OP_6F(0x79)
    OP_0D()
    TurnDirection(0x101, 0xEF, 500)

    ChrTalk(
        0x101,
        (
            "#00000F#6P…… OK, next is on\x01",
            "Let's go before \"Mirror\".\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xEF, 0x101, 500)
    Switch(
        (scpexpr(EXPR_23, 0x5), scpexpr(EXPR_END)),
        (0, "loc_5277"),
        (1, "loc_52A4"),
        (2, "loc_52D1"),
        (3, "loc_52FA"),
        (4, "loc_531F"),
        (5, "loc_5348"),
        (6, "loc_5371"),
        (7, "loc_539C"),
        (8, "loc_53C9"),
        (9, "loc_53F4"),
        (10, "loc_5425"),
        (SWITCH_DEFAULT, "loc_5452"),
    )


    label("loc_5277")


    ChrTalk(
        0x102,
        "#00100FYeah, let's go.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_5452")

    label("loc_52A4")


    ChrTalk(
        0x103,
        "#00200FYes, let's go.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_5452")

    label("loc_52D1")


    ChrTalk(
        0x104,
        "#00300FHaha, it is finally here.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_5452")

    label("loc_52FA")


    ChrTalk(
        0x109,
        "#10100FIt is finally time.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_5452")

    label("loc_531F")


    ChrTalk(
        0x105,
        "#10300FHuh, it's about time.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_5452")

    label("loc_5348")


    ChrTalk(
        0x153,
        "#01109FYes, let's go!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_5452")

    label("loc_5371")


    ChrTalk(
        0x156,
        "#06400FHehe, I'm looking forward to it ~.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_5452")

    label("loc_539C")


    ChrTalk(
        0x14C,
        "#05900FI wonder what will happen.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_5452")

    label("loc_53C9")


    ChrTalk(
        0x134,
        "#01700FYes, let's go.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_5452")

    label("loc_53F4")


    ChrTalk(
        0x135,
        "#01802F…… Yeah, let's go.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_5452")

    label("loc_5425")


    ChrTalk(
        0x166,
        "#14000F… … Hun, why do not you go.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_5452")

    label("loc_5452")

    OP_D2(0x4, (scpexpr(EXPR_PUSH_LONG, 0x80000000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    OP_65(0x3, 0x1)
    OP_65(0x4, 0x1)
    SetScenarioFlags(0x0, 0)
    OP_1B(0xC, 0x0, 0x2A)
    SetChrPos(0x0, -7700, 40550, -25000, 315)
    EventEnd(0x5)
    Return()

    # Function_20_5168 end

    def Function_21_547F(): pass

    label("Function_21_547F")

    Sound(918, 0, 100, 0)
    Sleep(2000)
    Sound(918, 0, 80, 0)
    Sleep(2000)
    Sound(918, 0, 60, 0)

    label("loc_5497")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_54B0")
    Sleep(2000)
    Sound(918, 0, 40, 0)
    Jump("loc_5497")

    label("loc_54B0")

    Return()

    # Function_21_547F end

    def Function_22_54B1(): pass

    label("Function_22_54B1")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x80000000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5505")

    ChrTalk(
        0x101,
        (
            "#00000FOops ……\x01",
            "I have to bell the underlying bell first.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_55BA")

    label("loc_5505")

    Switch(
        (scpexpr(EXPR_23, 0x5), scpexpr(EXPR_END)),
        (0, "loc_5550"),
        (1, "loc_5558"),
        (2, "loc_5560"),
        (3, "loc_5568"),
        (4, "loc_5570"),
        (5, "loc_5578"),
        (6, "loc_5580"),
        (7, "loc_5588"),
        (8, "loc_5590"),
        (9, "loc_5598"),
        (10, "loc_55A0"),
        (SWITCH_DEFAULT, "loc_55A8"),
    )


    label("loc_5550")

    Call(0, 28)
    Jump("loc_55A8")

    label("loc_5558")

    Call(0, 29)
    Jump("loc_55A8")

    label("loc_5560")

    Call(0, 30)
    Jump("loc_55A8")

    label("loc_5568")

    Call(0, 32)
    Jump("loc_55A8")

    label("loc_5570")

    Call(0, 33)
    Jump("loc_55A8")

    label("loc_5578")

    Call(0, 34)
    Jump("loc_55A8")

    label("loc_5580")

    Call(0, 36)
    Jump("loc_55A8")

    label("loc_5588")

    Call(0, 37)
    Jump("loc_55A8")

    label("loc_5590")

    Call(0, 38)
    Jump("loc_55A8")

    label("loc_5598")

    Call(0, 39)
    Jump("loc_55A8")

    label("loc_55A0")

    Call(0, 40)
    Jump("loc_55A8")

    label("loc_55A8")

    StopBGM(0xFA0)
    WaitBGM()
    SetScenarioFlags(0x22, 1)
    NewScene("t1400", 0, 0, 0)
    IdleLoop()

    label("loc_55BA")

    TalkEnd(0xFF)
    Return()

    # Function_22_54B1 end

    def Function_23_55BE(): pass

    label("Function_23_55BE")

    SetChrPos(0x101, -500, 44550, -2500, 0)
    SetChrPos(0xEF, 500, 44550, -2500, 0)
    Fade(500)
    OP_68(0, 47500, -1500, 0)
    OP_68(0, 46000, -1500, 4000)
    MoveCamera(0, 15, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(15700, 0)
    OP_6F(0x79)
    OP_0D()
    Return()

    # Function_23_55BE end

    def Function_24_5628(): pass

    label("Function_24_5628")

    Fade(800)
    EndChrThread(0xC, 0x1)
    SetMapObjFrame(0xFF, "Null_bell", 0x2, "stop")
    OP_0D()
    Sleep(2500)
    Return()

    # Function_24_5628 end

    def Function_25_5648(): pass

    label("Function_25_5648")


    def lambda_564D():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_564D)
    OP_93(0xFE, 0x10E, 0x1F4)
    WaitChrThread(0x101, 2)
    Return()

    # Function_25_5648 end

    def Function_26_5661(): pass

    label("Function_26_5661")


    def lambda_5666():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5666)
    OP_93(0xFE, 0x0, 0x1F4)
    WaitChrThread(0x101, 2)
    Return()

    # Function_26_5661 end

    def Function_27_567A(): pass

    label("Function_27_567A")

    SetCameraDistance(14700, 3000)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Jc((scpexpr(EXPR_23, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_56BA")
    OP_63(0xFE, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_56CC")

    label("loc_56BA")

    OP_63(0xFE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_56CC")

    Sleep(2500)
    OP_64(0x101)
    OP_64(0xFE)
    OP_6F(0x79)
    Return()

    # Function_27_567A end

    def Function_28_56D8(): pass

    label("Function_28_56D8")

    EventBegin(0x0)
    Call(0, 23)
    BeginChrThread(0x102, 3, 0, 25)
    WaitChrThread(0x102, 3)
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_57D4")

    ChrTalk(
        0x101,
        (
            "#00000FWell then,\x01",
            "Let's make a wish.\x02\x03",
            "#00005FEr … … in front of this mirror\x01",
            "Should I wish for a wish?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FPerhaps, I wish a wish in my head\x01",
            "I think that it is enough to imagine it.\x02\x03",
            "Then let's do it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_583D")

    label("loc_57D4")


    ChrTalk(
        0x101,
        (
            "#00000FThen I wish a wish in front of this mirror\x01",
            "You should be remembered.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FYeah, let's do it.\x02",
    )

    CloseMessageWindow()

    label("loc_583D")

    BeginChrThread(0x102, 3, 0, 26)
    WaitChrThread(0x102, 3)

    ChrTalk(
        0x101,
        "#00003F……………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00103F……………………………………\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x102, 3, 0, 27)
    WaitChrThread(0x102, 3)
    Call(0, 24)
    BeginChrThread(0x102, 3, 0, 25)
    WaitChrThread(0x102, 3)

    ChrTalk(
        0x101,
        "#00000F…… It is such a place.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104FYes, I have finished.\x02\x03",
            "#00100Fby the way……\x01",
            "What did Lloyd ask?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5A6F")

    ChrTalk(
        0x101,
        (
            "#00000FHaha, well ordinary too\x01",
            "I am a bit shy … …\x02\x03",
            "#00004F\"Crossbells will continue to be\x01",
            "May I protect you. \"\x02\x03",
            "#00000FOf course, Ka'aa and Eli\x01",
            "Including the associates of the support department.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FHuh, it seems to be you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FWell, thanks.\x02\x03",
            "#00000FEli like that,\x01",
            "What did you ask?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5B88")

    label("loc_5A6F")


    ChrTalk(
        0x101,
        (
            "#00000FWhen I first came\x01",
            "I did the best wish.\x02\x03",
            "#00004FI do not have to do the same wish,\x01",
            "\"May Erie's wish come true\"\x01",
            "I asked for it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FHuh, thank you Lloyd.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHaha, you are welcome.\x02\x03",
            "#00000FSo, Eli is\x01",
            "What did you ask?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5B88")

    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x102)

    ChrTalk(
        0x102,
        (
            "#00103FI … … \"My father and mother are happy\x01",
            "I wish you were spending time. \"\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005FEllie's parents … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F…… Hehe, I told you before.\x01",
            "Divorced 10 years ago, each\x01",
            "I live in the Republic and the Empire.\x02\x03",
            "#00104FEven now letters and conducting communication\x01",
            "Sometimes I keep in touch,\x01",
            "I can hardly see my face.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008F…… I feel lonely.\x02\x03",
            "#00003FI also lost my parents when I was young,\x01",
            "Because I have big brother and Cecil elder sister\x01",
            "I did not miss that much … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FHehe, my grandfather too\x01",
            "He was near me,\x01",
            "It is not a lonely translation.\x02\x03",
            "#00103F……If anything……\x01",
            "I wonder whether worrying is correct.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005Fworry……?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FMy father and mother, sometimes my situation\x01",
            "I am worried and will contact you, but ….\x02\x03",
            "#00108FThat is what left me leaving\x01",
            "If it is still a regret action,\x01",
            "I think that is too painful.\x02\x03",
            "They are so serious,\x01",
            "To forget the past and to live\x01",
            "It is a type you can never do.\x02\x03",
            "#00104FIt's been ten years since then,\x01",
            "I am about to walk a new life,\x01",
            "I thought that I wanted to be happy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008FForget the past and have a new life ……\x02\x03",
            "#00001FBut, that is correct\x01",
            "You can not say it unconditionally, do you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FYeah … I know.\x01",
            "Because there is a past,\x01",
            "I have my present.\x02\x03",
            "#00104FBut to my father and mother\x01",
            "Because any shape can be used\x01",
            "I want you to be happy …\x02\x03",
            "#00100F…… Hehe, I'm sorry.\x01",
            "I did a strange story.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FNo … not that at all.\x02\x03",
            "#00000FEli's parents' happiness ……\x01",
            "I suppose I will make you wish.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00109FHehe, Thank you.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_28_56D8 end

    def Function_29_615B(): pass

    label("Function_29_615B")

    EventBegin(0x0)
    Call(0, 23)
    BeginChrThread(0x103, 3, 0, 25)
    WaitChrThread(0x103, 3)
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6257")

    ChrTalk(
        0x101,
        (
            "#00000FWell then,\x01",
            "Let's make a wish.\x02\x03",
            "#00005FEr … … in front of this mirror\x01",
            "Should I wish for a wish?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FPerhaps, I wish a wish in my head\x01",
            "I think that it is enough to think of it.\x02\x03",
            "Let's do it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_62C0")

    label("loc_6257")


    ChrTalk(
        0x101,
        (
            "#00000FThen I wish a wish in front of this mirror\x01",
            "You should be remembered.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00200FYes, let's do it.\x02",
    )

    CloseMessageWindow()

    label("loc_62C0")

    BeginChrThread(0x103, 3, 0, 26)
    WaitChrThread(0x103, 3)

    ChrTalk(
        0x101,
        "#00003F……………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00203F……………………………………\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x103, 3, 0, 27)
    WaitChrThread(0x103, 3)
    Call(0, 24)
    BeginChrThread(0x103, 3, 0, 25)
    WaitChrThread(0x103, 3)

    ChrTalk(
        0x101,
        "#00000F…… It is such a place.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00204F…… Yes, I am also.\x02\x03",
            "#00200FI'd like to ask the reference level,\x01",
            "What kind of wish do Lloyd wants?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6515")

    ChrTalk(
        0x101,
        (
            "#00000FHaha, well ordinary too\x01",
            "I am a bit shy … …\x02\x03",
            "#00004F\"Crossbells will continue to be\x01",
            "May I protect you. \"\x02\x03",
            "#00000FOf course, Kia and Tio\x01",
            "Including the associates of the support department.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FI see……\x01",
            "It seems like Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FWell, thanks.\x02\x03",
            "#00000FSuch Tio,\x01",
            "What did you ask?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_663F")

    label("loc_6515")


    ChrTalk(
        0x101,
        (
            "#00000FWhen I first came\x01",
            "I did the best wish.\x02\x03",
            "#00004FI do not have to do the same wish,\x01",
            "\"May your wishes come true\"\x01",
            "I asked for it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FI see……\x01",
            "Thank you for that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHaha, you are welcome.\x02\x03",
            "#00000FSuch Tio,\x01",
            "What did you ask?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_663F")


    ChrTalk(
        0x103,
        (
            "#00203F…… \"The Rozu's supervisor's uselessness\x01",
            "I hope that it will be a little better.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00012FWell, it's truly poor ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00202F……just kidding.\x02\x03",
            "#00203FActually……\x01",
            "\"The meaning of my life\x01",
            "As you can find \".\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x103,
        (
            "#00200FPreviously, also to Mr. Lloyd\x01",
            "I had something to talk about.\x02\x03",
            "#00203FThree years ago, I tried to ask Mr. Guy\x01",
            "Answer to a question that I could not ask …\x02\x03",
            "#00208FIt surpassed the cult incident\x01",
            "I still can not find it yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F… … Tio, did you say?\x01",
            "A human who knows such a thing\x01",
            "I do not have that.\x02\x03",
            "#00000FThere is no need to be impatient to search for an answer,\x01",
            "You do not have to search alone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00204FYes, of course I know.\x02\x03",
            "#00200FI have not been impatient,\x01",
            "Everyone helps you\x01",
            "Because I understand it now.\x02\x03",
            "#00203FBut this is my life\x01",
            "It is a question that can be said as a proposition.\x02\x03",
            "#00200FSo, someday you will find the answer.\x01",
            "…… With such intention display,\x01",
            "I asked for \"mirror\".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FIs that so?\x01",
            "It sounds bad, it was unnecessary worry.\x02\x03",
            "#00004FIf that is the case, I will rejoin\x01",
            "I think I will show my will.\x02\x03",
            "#00000FTio someday answer that\x01",
            "To be found ……\x01",
            "We will also lend the power.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00209FHehu ……\x01",
            "Thank you.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_29_615B end

    def Function_30_6B01(): pass

    label("Function_30_6B01")

    EventBegin(0x0)
    Call(0, 23)
    BeginChrThread(0x104, 3, 0, 25)
    WaitChrThread(0x104, 3)
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6BF7")

    ChrTalk(
        0x101,
        (
            "#00000FWell then,\x01",
            "Let's make a wish.\x02\x03",
            "#00005FEr … … in front of this mirror\x01",
            "Should I wish for a wish?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FPerhaps, I wish a wish in my head\x01",
            "I think that it is enough to imagine it.\x02\x03",
            "Then, why do not you try.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6C60")

    label("loc_6BF7")


    ChrTalk(
        0x101,
        (
            "#00000FThen I wish a wish in front of this mirror\x01",
            "You should be remembered.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00300FThen, why do not you try.\x02",
    )

    CloseMessageWindow()

    label("loc_6C60")

    BeginChrThread(0x104, 3, 0, 26)
    WaitChrThread(0x104, 3)

    ChrTalk(
        0x101,
        "#00003F……………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00303F……………………………………\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x104, 3, 0, 27)
    WaitChrThread(0x104, 3)
    Call(0, 24)
    BeginChrThread(0x104, 3, 0, 25)
    WaitChrThread(0x104, 3)

    ChrTalk(
        0x101,
        "#00000F…… It is such a place.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00304FI, too, ended.\x02\x03",
            "#00309FAnd, Lloyd.\x01",
            "What kind of wish did you do?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6EE5")

    ChrTalk(
        0x101,
        (
            "#00000FHaha, well ordinary too\x01",
            "I am a bit shy … …\x02\x03",
            "#00004F\"Crossbells will continue to be\x01",
            "May I protect you. \"\x02\x03",
            "#00000FOf course, Ka'aa and Randy\x01",
            "Including the associates of the support department.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FHaha, you are right\x01",
            "It is a serious guy.\x02\x03",
            "#00306FA little more to my desire\x01",
            "Even if you make an honest wish,\x01",
            "I guess the bee is an angel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FThat kind of Randy\x01",
            "What kind of wish did you do?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7032")

    label("loc_6EE5")


    ChrTalk(
        0x101,
        (
            "#00000FWhen I first came\x01",
            "I did the best wish.\x02\x03",
            "#00004FI do not have to do the same wish,\x01",
            "\"May Randy's wish come true\"\x01",
            "I asked for it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00305FOh, seriously! Is it?\x02\x03",
            "#00309FWell ~ as expected is Lloyd,\x01",
            "It's a good timing guy!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00005FEr … … Randy is\x01",
            "What kind of wish did you do?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7032")


    ChrTalk(
        0x104,
        (
            "#00304FAm I? Oh yeah, of course,\x01",
            "\"In the crossbell, with your sisters\x01",
            "Ha ha ha ha ha ─ ─ ─ \"\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F─ ─ I understood, it's okay.\x01",
            "I was stupid I heard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00305FHey, every man anyone\x01",
            "Is it a dreaming situation?\x02\x03",
            "#00304FMs. Cecil and Ms. Nurse,\x01",
            "Mr. Eolia, a prime minister … …\x02\x03",
            "#00309FI like the crossbell\x01",
            "You are a lot of big sisters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FWell … that kind of delusion\x01",
            "Do not let Cecil elder sister get involved.\x02\x03",
            "#00002F… Well, in a sense I was relieved.\x01",
            "It is a wish that will never come true.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x104,
        (
            "#00306FSquirrel\x01",
            "Please tell me ….\x02\x03",
            "#00300F…… Haha, well you,\x01",
            "Do you envy me?\x02\x03",
            "#00304FBe safe,\x01",
            "Akatsuki when the wish has come true\x01",
            "I also have a good feeling ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00011FWhen, who\x01",
            "I was worried about that! Is it?\x02\x03",
            "#00006F… … Ha, absolutely.\x01",
            "I wish a wish and I will go quickly.\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x101, 3, 0, 31)
    OP_93(0x104, 0xE1, 0x1F4)
    Sleep(1500)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    WaitChrThread(0x101, 3)
    OP_64(0x104)

    ChrTalk(
        0x104,
        (
            "#00308F(A wish that never comes true … ….?\x02\x03",
            "#00303F(\"As always this way, as a friend\" … …\x01",
            "Mushi is too good for me. )\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_93(0x104, 0xE1, 0x1F4)
    OP_9B(0x0, 0x104, 0x0, 0x7D0, 0x7D0, 0x0)
    OP_0D()
    Return()

    # Function_30_6B01 end

    def Function_31_7409(): pass

    label("Function_31_7409")

    OP_93(0xFE, 0xE1, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
    Return()

    # Function_31_7409 end

    def Function_32_7420(): pass

    label("Function_32_7420")

    EventBegin(0x0)
    Call(0, 23)
    BeginChrThread(0x109, 3, 0, 25)
    WaitChrThread(0x109, 3)
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_751E")

    ChrTalk(
        0x101,
        (
            "#00000FWell then,\x01",
            "Let's make a wish.\x02\x03",
            "#00005FEr … … in front of this mirror\x01",
            "Should I wish for a wish?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FPerhaps, I wish a wish in my head\x01",
            "I think that it is enough to think of it.\x02\x03",
            "Then let's do it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_75A4")

    label("loc_751E")


    ChrTalk(
        0x101,
        (
            "#00000FWell then,\x01",
            "Let's make a wish.\x02\x03",
            "In front of this mirror, make a wish\x01",
            "You should be remembered.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10100FYeah, let's do it.\x02",
    )

    CloseMessageWindow()

    label("loc_75A4")

    BeginChrThread(0x109, 3, 0, 26)
    WaitChrThread(0x109, 3)

    ChrTalk(
        0x101,
        "#00003F……………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10103F……………………………………\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x109, 3, 0, 27)
    WaitChrThread(0x109, 3)
    Call(0, 24)
    BeginChrThread(0x109, 3, 0, 25)
    WaitChrThread(0x109, 3)

    ChrTalk(
        0x101,
        "#00000F…… It is such a place.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10104FYes, I am done.\x02\x03",
            "#10100FWell, Mr. Lloyd is\x01",
            "What kind of wish do you have?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_77DB")

    ChrTalk(
        0x101,
        (
            "#00000FHaha, well ordinary too\x01",
            "I am a bit shy … …\x02\x03",
            "#00004F\"Crossbells will continue to be\x01",
            "May I protect you. \"\x02\x03",
            "#00000FOf course, guards people\x01",
            "Including the associates of the support department.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10100FIndeed, it seems to be Mr. Lloyd.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FWell, thanks.\x02\x03",
            "For Noel,\x01",
            "What kind of wish did you do?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7905")

    label("loc_77DB")


    ChrTalk(
        0x101,
        (
            "#00000FWhen I first came\x01",
            "I did the best wish.\x02\x03",
            "#00004FI do not have to do the same wish,\x01",
            "\"May Noel's wish come true\"\x01",
            "I asked for it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FHaha ……\x01",
            "Thank you very much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHaha, you are welcome.\x02\x03",
            "#00000FSo, for Noel,\x01",
            "What kind of wish did you do?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7905")


    ChrTalk(
        0x109,
        (
            "#10100FI am simple, but ……\x01",
            "\"I want to become a fine security guard\"\x01",
            "Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009Fmy mother……\x01",
            "Noel 's frank wish.\x02\x03",
            "#00000FAfter all, your father\x01",
            "Is it a target?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FHaha … …. I mentioned before,\x01",
            "There is not much awareness about that.\x02\x03",
            "#10104FI was a child,\x01",
            "The thing about the tough father of disgrace\x01",
            "It was rather weak.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FWell, was that so.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10102FYeah, it was a really tough person.\x02\x03",
            "#10104FI and Fran\x01",
            "Doing something wrong,\x01",
            "People who mindfully fly a fist … …\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x109,
        (
            "#10103FBy the way, brought to my mother\x01",
            "A father who works once at the border gate\x01",
            "I went to see it.\x02\x03",
            "#10108FDespite the distorted regime at the time,\x01",
            "As a defender of the crossbell\x01",
            "Appearing to be tough all … …\x02\x03",
            "#10100FThinking now … ….\x01",
            "I respect respect to that figure\x01",
            "Perhaps it was holding him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FI see……\x01",
            "Noel's strict personality is\x01",
            "After all it seems to have an impact.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10109FHaha, is not it.\x02\x03",
            "#10103FThat's it, why the franc\x01",
            "Have you become such a gentle personality\x01",
            "It is a place I do not agree with.\x02\x03",
            "#10101F…… Maybe father,\x01",
            "Actually, only franc\x01",
            "I wonder if it was Deleadere.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00012FNo, well ….\x01",
            "There is also a possibility of reactionary to severity.\x02\x03",
            "#00000F… Well then, my wish is over\x01",
            "Shall we go soon?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10100FYeah, you are right.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_32_7420 end

    def Function_33_7E1A(): pass

    label("Function_33_7E1A")

    EventBegin(0x0)
    Call(0, 23)
    BeginChrThread(0x105, 3, 0, 25)
    WaitChrThread(0x105, 3)
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7F15")

    ChrTalk(
        0x101,
        (
            "#00000FWell then,\x01",
            "Let's make a wish.\x02\x03",
            "#00005FEr … … in front of this mirror\x01",
            "Should I wish for a wish?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FPerhaps, I wish a wish in my head\x01",
            "To think about it\x01",
            "Why not?\x02\x03",
            "Let's do it then.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7FA4")

    label("loc_7F15")


    ChrTalk(
        0x101,
        (
            "#00000FWell then,\x01",
            "Let's make a wish.\x02\x03",
            "#00004FIn front of this mirror, make a wish\x01",
            "You should be remembered.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10300FLet's do it then.\x02",
    )

    CloseMessageWindow()

    label("loc_7FA4")

    BeginChrThread(0x105, 3, 0, 26)
    WaitChrThread(0x105, 3)

    ChrTalk(
        0x101,
        "#00003F……………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10303F……………………………………\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x105, 3, 0, 27)
    WaitChrThread(0x105, 3)
    Call(0, 24)
    BeginChrThread(0x105, 3, 0, 25)
    WaitChrThread(0x105, 3)

    ChrTalk(
        0x101,
        "#00000F…… It is such a place.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FI have finished.\x02\x03",
            "#10300FSo what kind of you are you?\x01",
            "Did you wish a wish?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_81CE")

    ChrTalk(
        0x101,
        (
            "#00000FHaha, well ordinary too\x01",
            "I am a bit shy … …\x02\x03",
            "#00004F\"Crossbells will continue to be\x01",
            "May I protect you. \"\x02\x03",
            "#00000FOf course, Ka'aa and the wadi\x01",
            "Including the associates of the support department.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10300FHuh, it is your wish.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FWell, thanks.\x02\x03",
            "#00000FSuch a Wadi\x01",
            "What kind of wish did you do?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_82F4")

    label("loc_81CE")


    ChrTalk(
        0x101,
        (
            "#00000FWhen I first came\x01",
            "I did the best wish.\x02\x03",
            "#00004FI do not have to do the same wish,\x01",
            "\"Wishes of wishes come true\"\x01",
            "I asked for it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FHuh, you are the one\x01",
            "You really are a good person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHaha, you are welcome.\x02\x03",
            "#00000FSuch a Wadi\x01",
            "What kind of wish did you do?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_82F4")


    ChrTalk(
        0x105,
        (
            "#10302FIf you say strongly …\x02\x03",
            "#10304F\"A former fighting opponent makes his own way\x01",
            "As if to be found \".\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00008F…… I heard it in rumors, but ….\x01",
            "Waldo, recently also to the hideout\x01",
            "You do not put out your face.\x02\x03",
            "#00003FBut, it is due to Waday ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10309FSeparately, I feel responsible\x01",
            "I am not immersed in sentiment.\x02\x03",
            "#10300FAfter that battle of that rainy day,\x01",
            "It is because he rotates and becomes scorching\x01",
            "I was able to predict to some extent.\x02\x03",
            "#10304FWill continue to decay afterwards,\x01",
            "Everything is blown away and you go on next …\x01",
            "Eventually it is Wald's own problem.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00006FThat's a cool opinion … …\x02\x03",
            "#00000FBut, if you really think so\x01",
            "Why is \"Wald do his way …?\"\x01",
            "You do not want to wish?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FHuh, it is reasonable, though …\x01",
            "This wish is also for myself.\x02\x03",
            "#10300FIf he continues to decay in the future …\x01",
            "What I should tell you on the rainy day battle\x01",
            "It will be one that has not been transmitted.\x02\x03",
            "#10303FThat's what I was barking on\x01",
            "There is no other than the fact that it was not … …\x02\x03",
            "#10309FAs expected it is not cool.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F… … Haha, boy.\x01",
            "Waddies are not honest.\x02\x03",
            "#00000FBut, Walds and\x01",
            "Viper guys find a way ……\x01",
            "I hope for that too.\x02\x03",
            "I hope the truth will come true.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303FHuh, you really are a good person.\x02\x03",
            "#10309FI love this place unbearably.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00006FOh no, it's pretty\x01",
            "I was trying to keep it ……\x01",
            "Do not make it brown!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_33_7E1A end

    def Function_34_884C(): pass

    label("Function_34_884C")

    EventBegin(0x0)
    Call(0, 23)
    BeginChrThread(0x153, 3, 0, 25)
    WaitChrThread(0x153, 3)
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8948")

    ChrTalk(
        0x101,
        (
            "#00000FWell then,\x01",
            "Let's make a wish.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#01100FIn front of this Kagami\x01",
            "Why do not you ask your wishes?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FOh, maybe I wish a wish in my head\x01",
            "I think that it is good enough to imagine it.\x02\x03",
            "… Well, let's do it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_89C9")

    label("loc_8948")


    ChrTalk(
        0x101,
        (
            "#00000FWell then,\x01",
            "Let's make a wish.\x02\x03",
            "#00004FIn front of this mirror, make a wish\x01",
            "You should be remembered.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#01100FI understood.\x02",
    )

    CloseMessageWindow()

    label("loc_89C9")

    BeginChrThread(0x153, 3, 0, 26)
    WaitChrThread(0x153, 3)

    ChrTalk(
        0x101,
        "#00003F……………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#01103F……Hmm~…………………………\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x153, 3, 0, 27)
    WaitChrThread(0x153, 3)
    Call(0, 24)
    BeginChrThread(0x153, 3, 0, 25)
    WaitChrThread(0x153, 3)

    ChrTalk(
        0x101,
        "#00000F…… It is such a place.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#01109FYeah, Ka'aa is over!\x02\x03",
            "#01105FHey, what is Lloyd?\x01",
            "Did you make a wish?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8BFF")

    ChrTalk(
        0x101,
        (
            "#00000FHaha, well ordinary too\x01",
            "I am a bit shy … …\x02\x03",
            "#00004F\"Crossbells will continue to be\x01",
            "May I protect you. \"\x02\x03",
            "#00000FOf course, Keaers\x01",
            "Including the associates of the support department.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#01109FEh … … as expected Lloyd.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FWell, thanks.\x02\x03",
            "#00000FKa'a's way\x01",
            "What kind of wish did you do?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8D16")

    label("loc_8BFF")


    ChrTalk(
        0x101,
        (
            "#00000FWhen I first came\x01",
            "I did the best wish.\x02\x03",
            "#00004FI do not have to do the same wish,\x01",
            "\"Wish of Ka'ah come true\"\x01",
            "I asked for it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#01109FErr …… Thank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHaha, you are welcome.\x02\x03",
            "#00000FKa'a's way\x01",
            "What kind of wish did you do?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8D16")


    ChrTalk(
        0x153,
        (
            "#01106FWell, what I would like to ask\x01",
            "There were a variety of things ……\x02\x03",
            "#01100FAs I thought, the most important thing is \"the eyes of Shizuku\x01",
            "I wish you well. \"\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00003F…… Oh, I hope it gets really well.\x02\x03",
            "#00008FSizuku's eye's surgery\x01",
            "After all it seems to be quite difficult, but …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#01111FBut to this Kagami\x01",
            "Does it come true if you ask?\x02\x03",
            "#01101FWell then,\x01",
            "Do as many times as possible!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FHaha … oh.\x01",
            "I will seriously ask you too.\x02\x03",
            "#00004F(Really … … even a miracle\x01",
            "I hope it will happen. )\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x153, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x153, 0x0, 0x1F4)

    ChrTalk(
        0x153,
        "#01111F… …………………………?\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005FWhat 's wrong, Kea?\x02",
    )

    CloseMessageWindow()
    OP_93(0x153, 0x10E, 0x1F4)

    ChrTalk(
        0x153,
        (
            "#01103F……, I have nothing.\x02\x03",
            "#01109FMore than that, Lloyd,\x01",
            "Ring more bells!\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x153, 3, 0, 35)
    OP_93(0x101, 0x87, 0x1F4)
    WaitChrThread(0x153, 3)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00009Fmy mother……\x01",
            "I do not have much energy.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_34_884C end

    def Function_35_9037(): pass

    label("Function_35_9037")

    OP_93(0xFE, 0x87, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x1F40, 0xFA0, 0x0)
    Return()

    # Function_35_9037 end

    def Function_36_904E(): pass

    label("Function_36_904E")

    EventBegin(0x0)
    Call(0, 23)
    BeginChrThread(0x156, 3, 0, 25)
    WaitChrThread(0x156, 3)
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_914F")

    ChrTalk(
        0x101,
        (
            "#00000FWell then,\x01",
            "Let's make a wish.\x02\x03",
            "#00005FEr … … in front of this mirror\x01",
            "Should I wish for a wish?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x156,
        (
            "#06400FPerhaps, I wish a wish in my head\x01",
            "To think about it\x01",
            "I think that is good ~.\x02\x03",
            "Let's do it then!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_91E0")

    label("loc_914F")


    ChrTalk(
        0x101,
        (
            "#00000FWell then,\x01",
            "Let's make a wish.\x02\x03",
            "#00004FIn front of this mirror, make a wish\x01",
            "You should be remembered.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x156,
        "#06400FLet's do it then!\x02",
    )

    CloseMessageWindow()

    label("loc_91E0")

    BeginChrThread(0x156, 3, 0, 26)
    WaitChrThread(0x156, 3)

    ChrTalk(
        0x101,
        "#00003F……………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x156,
        "#06403F……………………………………\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x156, 3, 0, 27)
    WaitChrThread(0x156, 3)
    Call(0, 24)
    BeginChrThread(0x156, 3, 0, 25)
    WaitChrThread(0x156, 3)

    ChrTalk(
        0x101,
        "#00000F…… It is such a place.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x156,
        (
            "#06400FYes, I also asked for it ~.\x02\x03",
            "#06409FBy the way, Mr. Lloyd is\x01",
            "What kind of wish did you wish ~?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_942A")

    ChrTalk(
        0x101,
        (
            "#00000FHaha, well ordinary too\x01",
            "I am a bit shy … …\x02\x03",
            "#00004F\"Crossbells will continue to be\x01",
            "May I protect you. \"\x02\x03",
            "#00000FOf course, the francs\x01",
            "Include police members as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x156,
        "#06402FHehe he seems to be Lloyd.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FWell, thanks.\x02\x03",
            "#00000FSuch a franc\x01",
            "What kind of wish did you do?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9551")

    label("loc_942A")


    ChrTalk(
        0x101,
        (
            "#00000FWhen I first came\x01",
            "I did the best wish.\x02\x03",
            "#00004FI do not have to do the same wish,\x01",
            "\"May Franc's wish come true\"\x01",
            "I asked for it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x156,
        "#06402FHehe, thank you for that ~.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHaha, you are welcome.\x02\x03",
            "#00000FSuch a franc\x01",
            "What kind of wish did you do?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9551")


    ChrTalk(
        0x156,
        (
            "#06409FHuhu, I thought\x01",
            "\"I want to be like an older sister\"\x01",
            "Is not it ~.\x02\x03",
            "#06401FShe looks like an older sister.\x01",
            "A cool woman who can depend on it,\x01",
            "Because it is my eternal goal!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FA woman like Noel ……\x01",
            "Haha, it is my sister's frankly wish.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00005FBy the way it is a simple doubt ….\x01",
            "Did not Frang aim for the guard?\x02\x03",
            "#00000FIf you long for Noel,\x01",
            "Even though I would like to work for the same guard\x01",
            "I do not think it's strange.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x156,
        (
            "#06400FHaha, that is it ~.\x01",
            "After all, people\x01",
            "There is a suitable place, is not it?\x02\x03",
            "#06403FI am a police school rather than a training\x01",
            "Because the results of the administrative system were good …\x02\x03",
            "#06400FIn a way that suits me,\x01",
            "I want to protect the crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FCertainly, only people working in the field\x01",
            "You do not protect the crossbell.\x02\x03",
            "#00004FOperations headquarters and operator's work\x01",
            "It is only when we can also be active ……\x02\x03",
            "#00009FIn that sense, Fran\x01",
            "I'm in the receptionist is comfortable … …\x01",
            "After all it was probably qualified.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x156,
        (
            "#06409FErr …\x01",
            "When it is said so\x01",
            "I'm blushy.\x02\x03",
            "#06400F\"I want to be like an older sister\"\x01",
            "Also wishfully,\x01",
            "It is that it is within that range.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FHaha, I see.\x02\x03",
            "#00000FWell then, then\x01",
            "I also wished for a wish,\x01",
            "Shall we go soon?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x156,
        "#06409FYes, let's go ~!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_36_904E end

    def Function_37_9A36(): pass

    label("Function_37_9A36")

    EventBegin(0x0)
    Call(0, 23)
    BeginChrThread(0x14C, 3, 0, 25)
    WaitChrThread(0x14C, 3)
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9B3B")

    ChrTalk(
        0x101,
        (
            "#00000FWell then,\x01",
            "Let's make a wish.\x02\x03",
            "#00005FEr … … in front of this mirror\x01",
            "Should I wish for a wish?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14C,
        (
            "#05900FPerhaps, I wish a wish in my head\x01",
            "To think about it\x01",
            "I wonder if it is ok.\x02\x03",
            "Then let's do it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9BC8")

    label("loc_9B3B")


    ChrTalk(
        0x101,
        (
            "#00000FWell then,\x01",
            "Let's make a wish.\x02\x03",
            "#00004FIn front of this mirror, make a wish\x01",
            "You should be remembered.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14C,
        "#05900FYeah, let's do it.\x02",
    )

    CloseMessageWindow()

    label("loc_9BC8")

    BeginChrThread(0x14C, 3, 0, 26)
    WaitChrThread(0x14C, 3)

    ChrTalk(
        0x101,
        "#00003F……………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14C,
        "#05903F……………………………………\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x14C, 3, 0, 27)
    WaitChrThread(0x14C, 3)
    Call(0, 24)
    BeginChrThread(0x14C, 3, 0, 25)
    WaitChrThread(0x14C, 3)

    ChrTalk(
        0x101,
        "#00000F…… It is such a place.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14C,
        (
            "#05904FYes, I am OK.\x02\x03",
            "#05900FWhat kind of wish does Lloyd wish for?\x01",
            "I wonder?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9DF4")

    ChrTalk(
        0x101,
        (
            "#00000FHaha, well ordinary too\x01",
            "I am a bit shy … …\x02\x03",
            "#00004F\"Crossbells will continue to be\x01",
            "May I protect you. \"\x02\x03",
            "#00000FOf course, Cecil elder sister and\x01",
            "Including the members of the support department.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14C,
        "#05902FHehe he seems to be Lloyd.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FWell, thanks.\x02\x03",
            "#00000FSuch Cecil elder sister\x01",
            "What kind of wish did you do?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9F13")

    label("loc_9DF4")


    ChrTalk(
        0x101,
        (
            "#00000FWhen I first came\x01",
            "I did the best wish.\x02\x03",
            "#00004FI do not have to do the same wish,\x01",
            "\"May your Cecil's wish come true\"\x01",
            "I asked for it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14C,
        "#05902FHehe, Thank you Lloyd.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHaha, you are welcome.\x02\x03",
            "#00000FSuch Cecil elder sister\x01",
            "What kind of wish did you do?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9F13")


    ChrTalk(
        0x14C,
        (
            "#05900FAs I expected after all …\x01",
            "\"Lloyd's forever\x01",
            "I wish you were healthy. \"\x02\x03",
            "#05904FFor me,\x01",
            "That is the best wish.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FI see … Thank you Cecil elder sister.\x02\x03",
            "#00000FHe was brought to the hospital with serious injury\x01",
            "As it is not to be done,\x01",
            "Let's be careful enough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14C,
        (
            "#05909FHehe, please do so.\x02\x03",
            "#05901FIf that's the case,\x01",
            "I have a painful injection as tears get out\x01",
            "Because I stab a lot of it.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00006F(That is, per Randy\x01",
            "It looks pretty jealous … …)\x02\x03",
            "#00000F…… Cecil's elder sister,\x01",
            "Do not force yourself to work\x01",
            "Sometimes take a day off?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14C,
        (
            "#05905FWell, considering the patient\x01",
            "As much as possible,\x01",
            "I want to get to work.\x02\x03",
            "#05909FBesides, sometimes like this\x01",
            "I am taking a day off and it's okay.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FNo, in the case of Cecil's older sister\x01",
            "Really only sometimes\x01",
            "It seems not to be absent … …\x02\x03",
            "#00001FEven me, Cecil's older sister\x01",
            "I'm worried.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14C,
        (
            "#05904FYeah … well, I understand.\x01",
            "Do not push yourself.\x01",
            "I suppose I should be careful.\x02\x03",
            "#05909FHuhu, even so\x01",
            "I worry about your sister ……\x01",
            "Lloyd also became an adult.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00006FAlso doing that like a child …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14C,
        "#05902FHehe, I'm sorry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F(…… Cecil's older sister is still,\x01",
            "What is \"Cecil elder sister\" anywhere. )\x02\x03",
            "#00006F(… … I feel lonely a little bit.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_37_9A36 end

    def Function_38_A400(): pass

    label("Function_38_A400")

    EventBegin(0x0)
    Call(0, 23)
    BeginChrThread(0x134, 3, 0, 25)
    WaitChrThread(0x134, 3)
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A500")

    ChrTalk(
        0x101,
        (
            "#00000FWell then,\x01",
            "Let's make a wish.\x02\x03",
            "#00005FEr … … in front of this mirror\x01",
            "Should I wish for a wish?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x134,
        (
            "#01700FPerhaps, I wish a wish in my head\x01",
            "Do not you think about it so much?\x02\x03",
            "Let's do it then.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A597")

    label("loc_A500")


    ChrTalk(
        0x101,
        (
            "#00000FWell then,\x01",
            "Let's make a wish.\x02\x03",
            "#00004FIn front of this mirror, make a wish\x01",
            "You should think about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x134,
        "#01700FOkay, let's do it.\x02",
    )

    CloseMessageWindow()

    label("loc_A597")

    BeginChrThread(0x134, 3, 0, 26)
    WaitChrThread(0x134, 3)

    ChrTalk(
        0x101,
        "#00003F……………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x134,
        "#01703F……………………………………\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x134, 3, 0, 27)
    WaitChrThread(0x134, 3)
    Call(0, 24)
    BeginChrThread(0x134, 3, 0, 25)
    WaitChrThread(0x134, 3)

    ChrTalk(
        0x101,
        "#00000F…… It is such a place.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x134,
        (
            "#01704FYes, I am fine.\x02\x03",
            "#01700FBy the way, my brother\x01",
            "What kind of wish did you do?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A7F4")

    ChrTalk(
        0x101,
        (
            "#00000FHaha, well ordinary too\x01",
            "I am a bit shy ……\x02\x03",
            "#00004F\"Crossbells will continue to be\x01",
            "May I protect you. \"\x02\x03",
            "#00000FOf course, Iria's\x01",
            "Including Alcan Shell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x134,
        (
            "#01702FHuh, I see.\x01",
            "It's hard to say good things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FWell, thanks.\x02\x03",
            "#00000FIria's way is\x01",
            "What kind of wish did you do?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A938")

    label("loc_A7F4")


    ChrTalk(
        0x101,
        (
            "#00000FWhen I first came\x01",
            "I did the best wish … …\x02\x03",
            "#00004FI also do the same wish,\x01",
            "\"May Irier's wish come true\"\x01",
            "I asked for it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x134,
        (
            "#01702FOh, my younger brother\x01",
            "It's quite disgusting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHaha, you are welcome.\x02\x03",
            "#00000FIria's way is\x01",
            "What kind of wish did you do?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A938")


    ChrTalk(
        0x134,
        (
            "#01704FOf course I\x01",
            "\"No matter what happens,\x01",
            "I hope to continue dancing. \"\x02\x03",
            "#01700FWell, no need to bother,\x01",
            "I do not get off the stage\x01",
            "Absolutely impossible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FHaha, as expected, Iria.\x01",
            "If you are obsessed with the stage\x01",
            "It is momentum not to be defeated by anyone.\x02\x03",
            "#00009FThe power to that,\x01",
            "Where do you come from?\x01",
            "It will always be amazing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x134,
        (
            "#01703FWell, yeah.\x01",
            "If it says strongly …\x02\x03",
            "#01700FI am more than anyone else\x01",
            "\"I like to dance on the stage,\x01",
            "I wonder why.\x02\x03",
            "Regarding that point,\x01",
            "I have confidence that I will not lose to anyone ……\x02\x03",
            "#01709FAs long as that feeling,\x01",
            "I will continue dancing until I die.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F\"Do you like……\x01",
            "It's very simple,\x01",
            "I also understand it.\x02\x03",
            "#00004FIn a way that seems so strong,\x01",
            "Perhaps it is a terrible thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x134,
        (
            "#01700FHuh, it's not a big deal.\x01",
            "I do not care whether I like it or not\x01",
            "It is an emotional feeling to everyone.\x02\x03",
            "#01709FIf younger brother also for the important person\x01",
            "You can bet on life, do not you bet?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00000FYeah … I really think so.\x02\x03",
            "#00004F(It was also able to solve that cult character case,\x01",
            "He says he wants to protect Kia.\x01",
            "Because there was a strong feeling … …)\x02\x03",
            "(If you are for a precious thing,\x01",
            "I wonder how strong I can become. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x134,
        (
            "#01700FHeh, he seems to be convinced.\x02\x03",
            "#01709F…… Sure, I wish for a wish\x01",
            "Let's say we are about to go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYeah, you are right.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_38_A400 end

    def Function_39_AE2D(): pass

    label("Function_39_AE2D")

    EventBegin(0x0)
    Call(0, 23)
    BeginChrThread(0x135, 3, 0, 25)
    WaitChrThread(0x135, 3)
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AF3B")

    ChrTalk(
        0x101,
        (
            "#00000FWell then,\x01",
            "Let's make a wish.\x02\x03",
            "#00005FEr … … in front of this mirror\x01",
            "Should I wish for a wish?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x135,
        (
            "#01802FPerhaps, I wish a wish in my head\x01",
            "To think about it\x01",
            "Is not it okay?\x02\x03",
            "#01803F… … Let's do it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AFCC")

    label("loc_AF3B")


    ChrTalk(
        0x101,
        (
            "#00000FWell then,\x01",
            "Let's make a wish.\x02\x03",
            "#00004FIn front of this mirror, make a wish\x01",
            "You should be remembered.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x135,
        "#01803F…… Yes, let's do it.\x02",
    )

    CloseMessageWindow()

    label("loc_AFCC")

    BeginChrThread(0x135, 3, 0, 26)
    WaitChrThread(0x135, 3)

    ChrTalk(
        0x101,
        "#00003F……………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x135,
        "#01803F……………………………………\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x135, 3, 0, 27)
    WaitChrThread(0x135, 3)
    Call(0, 24)
    BeginChrThread(0x135, 3, 0, 25)
    WaitChrThread(0x135, 3)

    ChrTalk(
        0x101,
        "#00000F…… It is such a place.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x135,
        (
            "#01804FYes, I am also fine.\x02\x03",
            "#01802FEr, Mr. Lloyd\x01",
            "What kind of wish did you do?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B21F")

    ChrTalk(
        0x101,
        (
            "#00000FHaha, well ordinary too\x01",
            "I am a bit shy … …\x02\x03",
            "#00004F\"Crossbells will continue to be\x01",
            "May I protect you. \"\x02\x03",
            "#00000FOf course, Lisha\x01",
            "Including people of alkane shell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x135,
        (
            "#01802F……Is that so.\x01",
            "He seems to be Mr. Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FWell, thanks.\x02\x03",
            "#00000FSuch Lisha\x01",
            "What kind of wish did you do?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B353")

    label("loc_B21F")


    ChrTalk(
        0x101,
        (
            "#00000FWhen I first came\x01",
            "I did the best wish.\x02\x03",
            "#00004FI do not have to do the same wish,\x01",
            "\"Lisha's wishes will come true\"\x01",
            "I asked for it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x135,
        (
            "#01802F……Is that so.\x01",
            "Hehe, thank you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHaha, you are welcome.\x02\x03",
            "#00000FSuch Lisha\x01",
            "What kind of wish did you do?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B353")

    OP_63(0x135, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x135)

    ChrTalk(
        0x135,
        (
            "#01803FMy wish is …\x01",
            "\"Like Iria-san\x01",
            "I want to be an artist. \"\x02\x03",
            "#01802FHuhu, I'm still a newcomer\x01",
            "You may be obstinate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FDisagreeable……\x01",
            "Is not it such a thing?\x02\x03",
            "#00003FAlcan Shell's performances also\x01",
            "It seems pretty popular ……\x02\x03",
            "#00000FMore than anything, you Mr. Iria\x01",
            "I am recognized for talent.\x02\x03",
            "#00009FIf you continue your efforts in this way,\x01",
            "Surely the future seems to be Iria\x01",
            "I feel like even a big star.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x135, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(
        0x135,
        (
            "#01809FSounds like that … ….\x01",
            "I really have a lot more to do.\x02\x03",
            "#01804FShuri is better than me,\x01",
            "I think that there is much talent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FWell, even with a little more confidence\x01",
            "I do not think so.\x02\x03",
            "#00000FWell, Lisha's wish will come true\x01",
            "I support you too … ….\x01",
            "Please continue to do your best in the future.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x135,
        "#01809FThank you, yes.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FHahaha, also to say to face\x01",
            "I'm pretty shy.\x02\x03",
            "#00000F… Well then my wish has finished\x01",
            "Shall we go soon?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x135,
        "#01802FYeah, you are right.\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x101, 3, 0, 31)
    Sleep(150)
    OP_93(0x135, 0xE1, 0x1F4)
    Sleep(650)
    OP_9B(0x0, 0x135, 0x0, 0x4B0, 0x7D0, 0x0)
    OP_63(0x135, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x135)

    ChrTalk(
        0x135,
        (
            "#01803F#11P(Wish not to come true\x01",
            "Even if it is … …)\x02\x03",
            "#01808F(If you only think\x01",
            "You will be forgiven … ….? )\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_9B(0x0, 0x135, 0x0, 0x7D0, 0x7D0, 0x0)
    OP_0D()
    EndChrThread(0x101, 0x3)
    Return()

    # Function_39_AE2D end

    def Function_40_B7D8(): pass

    label("Function_40_B7D8")

    EventBegin(0x0)
    Call(0, 23)
    BeginChrThread(0x166, 3, 0, 25)
    WaitChrThread(0x166, 3)
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B8D5")

    ChrTalk(
        0x101,
        (
            "#00000FWell then,\x01",
            "Let's make a wish.\x02\x03",
            "#00005FEr … … in front of this mirror\x01",
            "Should I wish for a wish?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x166,
        (
            "#14000FAbout thinking about my wish in my head\x01",
            "That's not good.\x02\x03",
            "#14003FLet's do it quickly if you do.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B973")

    label("loc_B8D5")


    ChrTalk(
        0x101,
        (
            "#00000FWell then,\x01",
            "Let's make a wish.\x02\x03",
            "#00004FIn front of this mirror, make a wish\x01",
            "You should be remembered.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x166,
        (
            "#14003FWait a minute, if you do\x01",
            "Let's do it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B973")

    BeginChrThread(0x166, 3, 0, 26)
    WaitChrThread(0x166, 3)

    ChrTalk(
        0x101,
        "#00003F……………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x166,
        "#14008F……………………………………\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x166, 3, 0, 27)
    WaitChrThread(0x166, 3)
    Call(0, 24)
    BeginChrThread(0x166, 3, 0, 25)
    WaitChrThread(0x166, 3)

    ChrTalk(
        0x101,
        "#00000F…… It is such a place.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x166,
        (
            "#14003FI am also good.\x02\x03",
            "#14000F…… So, what kind of person are you?\x01",
            "Did you do a wish?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BBAE")

    ChrTalk(
        0x101,
        (
            "#00000FHaha, well ordinary too\x01",
            "I am a bit shy … …\x02\x03",
            "#00004F\"Crossbells will continue to be\x01",
            "May I protect you. \"\x02\x03",
            "#00000FOf course, the shrimps\x01",
            "Including people of alkane shell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x166,
        (
            "#14000FHmmm …\x01",
            "Well, it's not good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FWell, thanks.\x02\x03",
            "#00000FSuch a shri\x01",
            "What kind of wish did you do?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BCD2")

    label("loc_BBAE")


    ChrTalk(
        0x101,
        (
            "#00000FWhen I first came\x01",
            "I did the best wish.\x02\x03",
            "#00004FI do not have to do the same wish,\x01",
            "\"As wishes of Shuri come true\"\x01",
            "I asked for it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x166,
        "#14006FWell, it's extra care.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000Fmy mother……\x01",
            "I wonder if it was a meddling.\x02\x03",
            "#00000FSuch a shri\x01",
            "What kind of wish did you do?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BCD2")

    OP_63(0x166, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x166)

    ChrTalk(
        0x166,
        (
            "#14003FI am……\x01",
            "I have not done anything wish.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FGokutama ……\x01",
            "Why, let me tell people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x166,
        (
            "#14006F…… Originally, wishing things\x01",
            "Oh yeah it does not come true.\x02\x03",
            "#14008FI guess the slum that I was was like.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x166,
        (
            "#14000F…… In the slums of my hometown,\x01",
            "I guess you are my\x01",
            "There were many more.\x02\x03",
            "#14003FI came down to the cross bell,\x01",
            "Iria got picked up by him … …\x01",
            "It was simply a luck.\x02\x03",
            "#14008FEven so,\x01",
            "I do not wish any more\x01",
            "I guess the mushi is too good.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00004FShuri …\x01",
            "… … You are kind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x166,
        "#14005F……Huh……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FFor someone else,\x01",
            "Those who can think so much\x01",
            "I think that it is not easy.\x02\x03",
            "#00004FThat is because you are very kind,\x01",
            "Because I have a mind to think people.\x02\x03",
            "#00000FBut … That's why\x01",
            "You must not be happy\x01",
            "What is not it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x166,
        "#14008FBut,\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYou do not have to think hard so much.\x01",
            "In short, as long as I have a wish\x01",
            "That's good.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x166, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x166,
        (
            "#14006FAh, I already understood ……\x01",
            "Preaching smelly and annoying older brother.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006FWow, that was bad, preaching smelly.\x02",
    )

    CloseMessageWindow()
    OP_63(0x166, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x166)

    ChrTalk(
        0x166,
        (
            "#14003F…… I do not know about the future,\x01",
            "Surely there is something I want to achieve.\x02\x03",
            "#14000F\"Success of this next renewal performance\" …\x01",
            "Anyway I just want to make it so.\x02\x03",
            "#14009F…… Is this alright?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FOh, is not it enough?\x02\x03",
            "I also do things that it will come true\x01",
            "I will make you wish from the bottom of my heart.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x166,
        (
            "#14012F, Towards the face\x01",
            "Do not say embarrassing things.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_40_B7D8 end

    def Function_41_C29F(): pass

    label("Function_41_C29F")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000FI aim for the top floor.\x01",
            "Let's go now.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 0, -950, -53650, 0)
    EventEnd(0x4)
    Return()

    # Function_41_C29F end

    def Function_42_C2EC(): pass

    label("Function_42_C2EC")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000FBefore the \"mirror\" above\x01",
            "Let's make a wish.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 0, 40550, -13830, 180)
    EventEnd(0x4)
    Return()

    # Function_42_C2EC end

    def Function_43_C339(): pass

    label("Function_43_C339")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    StopEffect(0x9, 0x0)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '塞姆里亚石碎片'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('塞姆里亚石碎片', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x18A, 4)
    OP_65(0x6, 0x1)
    EventEnd(0x3)
    Return()

    # Function_43_C339 end

    SaveToFile()

Try(main)
