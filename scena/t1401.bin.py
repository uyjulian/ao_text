from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "Tourist",                # 1
        "Tourist",                # 2
        "Tourist",                # 3
        "Tourist",                # 4
        "SE制御",                 # 5
        "bt1410",                 # 6
        "bt1420",                 # 7
        "bt1400",                 # 8
        "bt1400",                 # 9
    ))

    ATBonus("ATBonus_37C", 100, 5, 1, 5, 1, 5, 1, 5, 5, 5, 5, 5, 5, 0, 0, 0)

    Sepith("Sepith_C847", 15,  5,   5,   5,   10,  5,   25)
    Sepith("Sepith_C83F", 10,  6,   6,   6,   1,   4,   10)

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
        "BattleInfo_6A4", 0x0000, 78, 6, 60, 6, 1, 20, 0, "bt1400", "Sepith_C847", 40, 30, 20, 10,
        (
            ("ms79600.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3CC", "MonsterBattlePostion_42C", "ed7450", "ed7453", "ATBonus_37C"),
            ("ms79600.dat", "ms82300.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3AC", "MonsterBattlePostion_42C", "ed7450", "ed7453", "ATBonus_37C"),
            ("ms79600.dat", "ms82300.dat", "ms82300.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_3CC", "MonsterBattlePostion_42C", "ed7450", "ed7453", "ATBonus_37C"),
            ("ms79600.dat", "ms82300.dat", "ms82300.dat", "ms82300.dat", 0, 0, 0, 0, "MonsterBattlePostion_3AC", "MonsterBattlePostion_42C", "ed7450", "ed7453", "ATBonus_37C"),
        )
    )

    BattleInfo(
        "BattleInfo_5DC", 0x0000, 78, 6, 45, 6, 1, 20, 0, "bt1400", "Sepith_C83F", 40, 30, 20, 10,
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
        "Function_6_149A",         # 06, 6
        "Function_7_14C8",         # 07, 7
        "Function_8_150F",         # 08, 8
        "Function_9_1550",         # 09, 9
        "Function_10_1C01",        # 0A, 10
        "Function_11_224D",        # 0B, 11
        "Function_12_225D",        # 0C, 12
        "Function_13_263D",        # 0D, 13
        "Function_14_26AC",        # 0E, 14
        "Function_15_271B",        # 0F, 15
        "Function_16_2784",        # 10, 16
        "Function_17_27F3",        # 11, 17
        "Function_18_45C4",        # 12, 18
        "Function_19_54FF",        # 13, 19
        "Function_20_5544",        # 14, 20
        "Function_21_5839",        # 15, 21
        "Function_22_586B",        # 16, 22
        "Function_23_5983",        # 17, 23
        "Function_24_59ED",        # 18, 24
        "Function_25_5A0D",        # 19, 25
        "Function_26_5A26",        # 1A, 26
        "Function_27_5A3F",        # 1B, 27
        "Function_28_5A9D",        # 1C, 28
        "Function_29_65B9",        # 1D, 29
        "Function_30_6F4A",        # 1E, 30
        "Function_31_78A4",        # 1F, 31
        "Function_32_78BB",        # 20, 32
        "Function_33_8281",        # 21, 33
        "Function_34_8D19",        # 22, 34
        "Function_35_94C0",        # 23, 35
        "Function_36_94D7",        # 24, 36
        "Function_37_9EEC",        # 25, 37
        "Function_38_A881",        # 26, 38
        "Function_39_B2AE",        # 27, 39
        "Function_40_BC53",        # 28, 40
        "Function_41_C6EC",        # 29, 41
        "Function_42_C74C",        # 2A, 42
        "Function_43_C7AA",        # 2B, 43
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1FD, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12A7")
    Sound(14, 0, 100, 0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1FD, 1)"), scpexpr(EXPR_END)), "loc_1230")
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
    SetScenarioFlags(0x1FD, 0)
    OP_E0(0x5, 0x0)
    Jump("loc_12A2")

    label("loc_1230")

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
    OP_71(0x0, 0x1E, 0x0, 0x0, 0x0)

    label("loc_12A2")

    Jump("loc_12F0")

    label("loc_12A7")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1FD, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13F8")
    Sound(14, 0, 100, 0)
    OP_74(0x2, 0x1E)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x650, 1)"), scpexpr(EXPR_END)), "loc_1381")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x650),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1FD, 1)
    OP_E0(0x5, 0x0)
    Jump("loc_13F3")

    label("loc_1381")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x650),
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

    label("loc_13F3")

    Jump("loc_1441")

    label("loc_13F8")

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
            "Aah, it's so beautiful\x01",
            "that I'm staring at it\x01",
            "unintentionally...\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_5_144D end

    def Function_6_149A(): pass

    label("Function_6_149A")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "That planetarium... How\x01",
            "pretty...\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_6_149A end

    def Function_7_14C8(): pass

    label("Function_7_14C8")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Haha. Even if we don't\x01",
            "hurry, the "mirror"\x01",
            "won't run away.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_7_14C8 end

    def Function_8_150F(): pass

    label("Function_8_150F")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Mommy, mommy, quick,\x01",
            "quick! The stairs are\x01",
            "this way!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_8_150F end

    def Function_9_1550(): pass

    label("Function_9_1550")

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

    def lambda_161A():
        OP_9B(0x0, 0x101, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_161A)
    Sleep(50)

    def lambda_1632():
        OP_9B(0x0, 0x102, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1632)
    Sleep(50)

    def lambda_164A():
        OP_9B(0x0, 0x103, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_164A)
    Sleep(50)

    def lambda_1662():
        OP_9B(0x0, 0x104, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1662)
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
        "#00101F#6PThis light is...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00201F#12PThese particles of\x01",
            "spiritual power seem to\x01",
            "be rising.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_18AB")
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
        "#00013FThe front entrance!\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(200, 140, -1, -1)

    AnonymousTalk(
        0x104,
        (
            "#00306FYeah... It's closed, is\x01",
            "it?\x02\x03",
            "#00301FInstead, entrances on\x01",
            "the left and right\x01",
            "opened up...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_1A18")

    label("loc_18AB")

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
            "#00301FTch, the interior\x01",
            "structure's changed...!\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(100, 140, -1, -1)

    AnonymousTalk(
        0x101,
        "#00005FReally?\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(200, 140, -1, -1)

    AnonymousTalk(
        0x104,
        (
            "#00303FYeah. When I came here\x01",
            "before, the frontal\x01",
            "entrance was open...\x02\x03",
            "#00301FInstead, entrances on\x01",
            "the left and right have\x01",
            "opened up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_1A18")

    Fade(1000)
    OP_68(0, 1200, -47500, 0)
    MoveCamera(0, 11, 0, 0)
    OP_6E(540, 0)
    SetCameraDistance(18000, 0)
    OP_0D()

    ChrTalk(
        0x102,
        (
            "#00106F#6PI've been here many times\x01",
            "before, but to think there\x01",
            "was such a mechanism...\x02\x03",
            "#00108FCould this be "her" doing\x01",
            "too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F#12P...I hear the sound of\x01",
            "strange machinery deeper\x01",
            "inside.\x02\x03",
            "#00201FIf we're going, we'll\x01",
            "need to be careful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#5PAnyway, we've got to do\x01",
            "whatever we have to to\x01",
            "reach the top floor.\x02\x03",
            "#00013FWe'll interrogate Arios,\x01",
            "and take back KeA!\x02",
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

    # Function_9_1550 end

    def Function_10_1C01(): pass

    label("Function_10_1C01")

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

    def lambda_1D27():
        OP_93(0x101, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1D27)
    Sleep(30)

    def lambda_1D37():
        OP_93(0x102, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1D37)
    Sleep(30)

    def lambda_1D47():
        OP_93(0x103, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1D47)
    Sleep(30)

    def lambda_1D57():
        OP_93(0x104, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1D57)
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
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E44")
    SetMessageWindowPos(50, 140, -1, -1)

    AnonymousTalk(
        0x101,
        "#00013FWe're finally here.\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(230, 140, -1, -1)

    AnonymousTalk(
        0x104,
        "#00301FYeah... The top floor.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1E9D")

    label("loc_1E44")

    SetMessageWindowPos(50, 140, -1, -1)

    AnonymousTalk(
        0x101,
        "#00013FDid we make it?\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(230, 140, -1, -1)

    AnonymousTalk(
        0x104,
        (
            "#00301FYeah... This is the top\x01",
            "floor.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E9D")

    SetMessageWindowPos(70, 140, -1, -1)

    AnonymousTalk(
        0x102,
        (
            "#00108FB-But... Neither KeA nor\x01",
            "Arios are here...\x02",
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
            "#00206F#6P...I didn't notice the\x01",
            "last time I was here,\x01",
            "but...\x02\x03",
            "#00201FIt seems there's a\x01",
            "hidden space inside that\x01",
            "large, shining mirror.\x02",
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

    def lambda_2019():
        TurnDirection(0x101, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2019)
    Sleep(50)

    def lambda_2029():
        TurnDirection(0x102, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_2029)
    Sleep(50)

    def lambda_2039():
        TurnDirection(0x104, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_2039)
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
            "#00203F#6PYes. A significant\x01",
            "amount of spiritual\x01",
            "power is flowing in.\x02\x03",
            "#00201FI think that's the end\x01",
            "of the line.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00103F#5P...I see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00304F#6P...It seems we were able\x01",
            "to track them down\x01",
            "somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#11PYeah...\x02\x03",
            "#00007FEveryone, ready your\x01",
            "gear! We'll definitely\x01",
            "rescue KeA!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_219F():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_219F)
    Sleep(50)

    def lambda_21AF():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_21AF)
    Sleep(50)

    def lambda_21BF():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_21BF)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)

    ChrTalk(
        0x102,
        "#00107F#5PRight...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00201F#6PYes...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00307F#6PGotcha!\x02",
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

    # Function_10_1C01 end

    def Function_11_224D(): pass

    label("Function_11_224D")

    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
    Return()

    # Function_11_224D end

    def Function_12_225D(): pass

    label("Function_12_225D")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2481")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Faint particles of light\x01",
            "are being sucked into\x01",
            "the mirror.\x07\x00\x02",
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
            "#00006F#6P(It looks like we can\x01",
            "enter the mirror just\x01",
            "like this...)\x02\x03",
            "#00013F(...KeA... We're\x01",
            "coming!)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x183, 3)
    Jump("loc_24FE")

    label("loc_2481")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Faint particles of light\x01",
            "are being sucked into\x01",
            "the mirror.\x02\x03",
            "It seems the mirror can\x01",
            "be entered just like\x01",
            "this.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_24FE")

    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Step inside the mirror\x01",      # 0
            "Back away\x01",                   # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2559"),
        (1, "loc_2612"),
        (SWITCH_DEFAULT, "loc_263C"),
    )


    label("loc_2559")

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
    Jump("loc_263C")

    label("loc_2612")

    FadeToDark(500, 0, -1)
    OP_0D()
    OP_D7(0x1E)
    OP_37()
    SetChrPos(0x0, 0, 44500, -4000, 180)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Jump("loc_263C")

    label("loc_263C")

    Return()

    # Function_12_225D end

    def Function_13_263D(): pass

    label("Function_13_263D")


    def lambda_2642():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2642)
    Sleep(500)
    Sound(341, 0, 100, 0)

    def lambda_2660():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2660)
    PlayEffect(0x0, 0xFF, 0xFE, 0x0, 0, 1000, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0xFE, 2)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_13_263D end

    def Function_14_26AC(): pass

    label("Function_14_26AC")


    def lambda_26B1():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_26B1)
    Sleep(1000)

    def lambda_26C9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_26C9)
    Sound(920, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0xFE, 0x0, 0, 1000, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0xFE, 2)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_14_26AC end

    def Function_15_271B(): pass

    label("Function_15_271B")


    def lambda_2720():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2720)
    Sleep(1000)

    def lambda_2738():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2738)
    PlayEffect(0x0, 0xFF, 0xFE, 0x0, 0, 1000, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0xFE, 2)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_15_271B end

    def Function_16_2784(): pass

    label("Function_16_2784")


    def lambda_2789():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2789)
    Sleep(1500)

    def lambda_27A1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_27A1)
    Sound(920, 0, 60, 0)
    PlayEffect(0x0, 0xFF, 0xFE, 0x0, 0, 1000, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0xFE, 2)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_16_2784 end

    def Function_17_27F3(): pass

    label("Function_17_27F3")

    EventBegin(0x0)
    OP_E2(0x3)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_42FF")
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

    def lambda_28FF():
        OP_9B(0x0, 0x101, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_28FF)
    Sleep(50)

    def lambda_2917():
        OP_9B(0x0, 0xEF, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_2917)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0xEF, 0)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00000FSo this is Mirror\x01",
            "Castle, huh.\x02\x03",
            "It seems to be the\x01",
            "landmark attraction of\x01",
            "the park.\x02\x03",
            "#00006FHow to put it... I can\x01",
            "only say it's amazing.\x02",
        )
    )

    CloseMessageWindow()
    Switch(
        (scpexpr(EXPR_23, 0x5), scpexpr(EXPR_END)),
        (0, "loc_2A16"),
        (1, "loc_2C6D"),
        (2, "loc_2E73"),
        (3, "loc_30D1"),
        (4, "loc_3321"),
        (5, "loc_3591"),
        (6, "loc_37A7"),
        (7, "loc_39E9"),
        (8, "loc_3C28"),
        (9, "loc_3E34"),
        (10, "loc_403D"),
        (SWITCH_DEFAULT, "loc_42FA"),
    )


    label("loc_2A16")


    ChrTalk(
        0x102,
        (
            "#00104FIt seems this magical atmosphere is\x01",
            "created by the planetarium over there.\x02\x03",
            "#00100FWe took a field trip to Grancel Castle\x01",
            "when I studied in Liberl, but I think\x01",
            "this atmosphere is on the same level.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FThat's really amazing.\x01",
            "That's IBC for you, I\x01",
            "guess.\x02\x03",
            "#00005FThat's right, they say a\x01",
            ""Wish-Granting Mirror"\x01",
            "is in here somewhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FYes. They say if you ring\x01",
            "the bell and wish before the\x01",
            "mirror, it will come true.\x02\x03",
            "#00104FI heard it was on the top\x01",
            "floor, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FIn that case, let's\x01",
            "climb to the top floor\x01",
            "and look for it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FYes, all right.\x02",
    )

    CloseMessageWindow()
    Jump("loc_42FA")

    label("loc_2C6D")


    ChrTalk(
        0x103,
        (
            "#00204FThis magical aura is\x01",
            "thanks to the planetarium\x01",
            "in the center.\x02\x03",
            "#00200FIt's like a castle out of\x01",
            "a fairytale.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah, I get that feeling\x01",
            "too. That's IBC for you,\x01",
            "I guess...\x02\x03",
            "#00005FThat's right, they say a\x01",
            ""Wish-Granting Mirror"\x01",
            "is in here somewhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FAccording to Elie, if you ring\x01",
            "the bell and wish before the\x01",
            "mirror, it will come true.\x02\x03",
            "#00204FIt seems to be on the top\x01",
            "floor...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FIn that case, let's\x01",
            "climb to the top floor\x01",
            "and look for it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00200FYes, let's go.\x02",
    )

    CloseMessageWindow()
    Jump("loc_42FA")

    label("loc_2E73")


    ChrTalk(
        0x104,
        (
            "#00304FLooks like that spinning\x01",
            "planetarium in the center is\x01",
            "producing this magical atmosphere.\x02\x03",
            "#00300FHaha. If it's this authentic, it\x01",
            "almost seems like a real castle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah, I get that feeling\x01",
            "too. That's IBC for you,\x01",
            "I guess...\x02\x03",
            "#00005FThat's right, they say a\x01",
            ""Wish-Granting Mirror"\x01",
            "is in here somewhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FYeah, it's that thing that\x01",
            "grants your wish if you ring the\x01",
            "bell and stand in front of it.\x02\x03",
            "#00304FIt's on the top floor. I'm sure\x01",
            "we'll see it if we go upstairs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FIn that case, let's\x01",
            "climb to the top floor\x01",
            "and look for it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00300FYeah, let's go.\x02",
    )

    CloseMessageWindow()
    Jump("loc_42FA")

    label("loc_30D1")


    ChrTalk(
        0x109,
        (
            "#10104FIt seems the spinning planetarium\x01",
            "in the center is creating this\x01",
            "magical atmosphere.\x02\x03",
            "#10100FIf it's this authentic, it almost\x01",
            "seems like a real castle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah, I get that feeling\x01",
            "too. That's IBC for you,\x01",
            "I guess...\x02\x03",
            "#00005FThat's right, they say a\x01",
            ""Wish-Granting Mirror"\x01",
            "is in here somewhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FYes, they say if you ring\x01",
            "the bell and wish before\x01",
            "it, it will come true.\x02\x03",
            "#10104FIt's on the top floor. I\x01",
            "think we'll recognize it\x01",
            "immediately if we go there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FIn that case, let's\x01",
            "climb to the top floor\x01",
            "and look for it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10100FYes, let's go.\x02",
    )

    CloseMessageWindow()
    Jump("loc_42FA")

    label("loc_3321")


    ChrTalk(
        0x105,
        (
            "#10304FSo this magical atmosphere is\x01",
            "produced by the planetarium in the\x01",
            "center, eh?\x02\x03",
            "#10302FHehe, amazingly elaborate, isn't it.\x01",
            "It must've taken quite a bit of mira\x01",
            "to create a structure this grand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah, IBC's capital\x01",
            "strength is frightening.\x02\x03",
            "#00005FThat's right, they say a\x01",
            ""Wish-Granting Mirror"\x01",
            "is in here somewhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FYeah, they say it grants your\x01",
            "wish if you ring the bell and\x01",
            "stand in front of it.\x02\x03",
            "#10304FI heard it's on the top\x01",
            "floor. We'll know immediately\x01",
            "if we go up there, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FIn that case, let's\x01",
            "climb to the top floor\x01",
            "and look for it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10300FHaha, roger.\x02",
    )

    CloseMessageWindow()
    Jump("loc_42FA")

    label("loc_3591")


    ChrTalk(
        0x153,
        (
            "#01111FWhat's that spinning\x01",
            "thing in the center?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FOh that's a planetarium. It\x01",
            "produces the magical\x01",
            "atmosphere you see in here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#01105FOh... That's pretty\x01",
            "cool.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah, I honestly can't\x01",
            "even describe it. That's\x01",
            "IBC for you...\x02\x03",
            "#00005FThat's right, they say a\x01",
            ""Wish-Granting Mirror"\x01",
            "is in here somewhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#01100FThat mirror Elie was talking\x01",
            "about? She said it's at the\x01",
            "top of the castle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FAlright, then let's try\x01",
            "heading to the top floor\x01",
            "and looking there for it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#01109FAgreed!\x02",
    )

    CloseMessageWindow()
    Jump("loc_42FA")

    label("loc_37A7")


    ChrTalk(
        0x156,
        (
            "#06404FI heard the planetarium\x01",
            "in the center creates\x01",
            "this magical atmosphere.\x02\x03",
            "#06400FHaha. If it's this\x01",
            "authentic, it almost\x01",
            "seems like a real castle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah, I get that feeling\x01",
            "too. That's IBC for you,\x01",
            "I guess...\x02\x03",
            "#00005FThat's right, they say a\x01",
            ""Wish-Granting Mirror"\x01",
            "is in here somewhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x156,
        (
            "#06400FYes, they say it grants your\x01",
            "wish if you ring the bell\x01",
            "and stand in front of it.\x02\x03",
            "#06404FIt's on the top floor, so I\x01",
            "think we'll see it if we go\x01",
            "there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FIn that case, let's\x01",
            "climb to the top floor\x01",
            "and look for it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x156,
        "#06409FRight! Let's go!\x02",
    )

    CloseMessageWindow()
    Jump("loc_42FA")

    label("loc_39E9")


    ChrTalk(
        0x14C,
        (
            "#05904FIs that a planetarium in the\x01",
            "center, I wonder? What a magical\x01",
            "atmosphere.\x02\x03",
            "#05902FHaha. This is almost like a castle\x01",
            "from the picture books I read you\x01",
            "when you were little, Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FHaha... It really does\x01",
            "look like it's from a\x01",
            "fairy tale.\x02\x03",
            "#00005FThat's right, they say a\x01",
            ""Wish-Granting Mirror"\x01",
            "is in here somewhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14C,
        (
            "#05900FElie said it grants your\x01",
            "wish if you ring the bell\x01",
            "and stand before it.\x02\x03",
            "#05904FI heard it was on the top\x01",
            "floor, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FIn that case, let's\x01",
            "climb to the top floor\x01",
            "and look for it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14C,
        "#05900FYes, let's go.\x02",
    )

    CloseMessageWindow()
    Jump("loc_42FA")

    label("loc_3C28")


    ChrTalk(
        0x134,
        (
            "#01704FSo the planetarium in the\x01",
            "center is producing this\x01",
            "magical aura, huh...\x02\x03",
            "#01702FHmm. I wonder if we could\x01",
            "use one at Arc-en-Ciel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FHaha... How very like\x01",
            "you, Ilya.\x02\x03",
            "#00005FBy the way, they say a\x01",
            ""Wish-Granting Mirror"\x01",
            "is in here somewhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x134,
        (
            "#01700FYeah, the one that grants your\x01",
            "wish if you ring the bell and\x01",
            "stand before it, right?\x02\x03",
            "#01704FSeems like it's on this\x01",
            "castle's top floor, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FThen for now, let's\x01",
            "climb to the top floor\x01",
            "and look for it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x134,
        "#01709FOkay, let's go!\x02",
    )

    CloseMessageWindow()
    Jump("loc_42FA")

    label("loc_3E34")


    ChrTalk(
        0x135,
        (
            "#01804FThe planetarium in the\x01",
            "center is creating this\x01",
            "magical atmosphere, right?\x02\x03",
            "#01802FHaha. If Ilya saw this,\x01",
            "she might want to use one\x01",
            "on the stage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FHaha... I can easily\x01",
            "imagine it.\x02\x03",
            "#00005FThat's right, they say a\x01",
            ""Wish-Granting Mirror"\x01",
            "is in here somewhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x135,
        (
            "#01805FAh, they say it will grant\x01",
            "your wish if you ring the\x01",
            "bell and stand before it...\x02\x03",
            "#01804FElie said it was on the top\x01",
            "floor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FIn that case, let's\x01",
            "climb to the top floor\x01",
            "and look for it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x135,
        "#01809FYes, let's go.\x02",
    )

    CloseMessageWindow()
    Jump("loc_42FA")

    label("loc_403D")


    ChrTalk(
        0x166,
        (
            "#14005FWhat's that spinning\x01",
            "thing in the center?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FOh that's a planetarium. It\x01",
            "produces the magical\x01",
            "atmosphere you see in here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x166,
        (
            "#14000FWow... I don't really\x01",
            "get it, but it's pretty\x01",
            "amazing, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah, I honestly can't\x01",
            "even describe it. That's\x01",
            "IBC for you...\x02\x03",
            "#00005FThat's right, they say a\x01",
            ""Wish-Granting Mirror"\x01",
            "is in here somewhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x166,
        (
            "#14000FOh, I heard about it. It's that think\x01",
            "that grants your wish if you ring the\x01",
            "bell and stand in front of it, huh.\x02\x03",
            "#14003FI heard it's on the top floor... Do\x01",
            "you believe in stuff like that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FHaha, I'm not sure yet,\x01",
            "but... Let's climb to the\x01",
            "top floor and look for it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x166,
        (
            "#14000FHmph, well I'll tag\x01",
            "along.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_42FA")

    label("loc_42FA")

    Jump("loc_45AE")

    label("loc_42FF")

    SetChrPos(0x101, -500, -950, -51000, 0)
    SetChrPos(0xEF, 500, -950, -51000, 0)
    OP_68(0, 1050, -46000, 0)
    MoveCamera(0, 10, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(16500, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(13500, 3000)

    def lambda_4366():
        OP_9B(0x0, 0x101, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4366)
    Sleep(50)

    def lambda_437E():
        OP_9B(0x0, 0xEF, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_437E)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0xEF, 0)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00000FIn that case, let's set our\x01",
            "sights on the "Wish-Granting\x01",
            "Mirror" on the top floor.\x02",
        )
    )

    CloseMessageWindow()
    Switch(
        (scpexpr(EXPR_23, 0x5), scpexpr(EXPR_END)),
        (0, "loc_4446"),
        (1, "loc_4467"),
        (2, "loc_4487"),
        (3, "loc_44A8"),
        (4, "loc_44C8"),
        (5, "loc_44E6"),
        (6, "loc_44FF"),
        (7, "loc_4521"),
        (8, "loc_4541"),
        (9, "loc_4562"),
        (10, "loc_4582"),
        (SWITCH_DEFAULT, "loc_45AE"),
    )


    label("loc_4446")


    ChrTalk(
        0x102,
        "#00100FYes, all right.\x02",
    )

    CloseMessageWindow()
    Jump("loc_45AE")

    label("loc_4467")


    ChrTalk(
        0x103,
        "#00200FYes, let's go.\x02",
    )

    CloseMessageWindow()
    Jump("loc_45AE")

    label("loc_4487")


    ChrTalk(
        0x104,
        "#00300FYeah, let's go.\x02",
    )

    CloseMessageWindow()
    Jump("loc_45AE")

    label("loc_44A8")


    ChrTalk(
        0x109,
        "#10100FYes, let's go.\x02",
    )

    CloseMessageWindow()
    Jump("loc_45AE")

    label("loc_44C8")


    ChrTalk(
        0x105,
        "#10300FHehe, roger.\x02",
    )

    CloseMessageWindow()
    Jump("loc_45AE")

    label("loc_44E6")


    ChrTalk(
        0x153,
        "#01109FAgreed!\x02",
    )

    CloseMessageWindow()
    Jump("loc_45AE")

    label("loc_44FF")


    ChrTalk(
        0x156,
        "#06409FRight! Let's go!\x02",
    )

    CloseMessageWindow()
    Jump("loc_45AE")

    label("loc_4521")


    ChrTalk(
        0x14C,
        "#05900FYes, let's go.\x02",
    )

    CloseMessageWindow()
    Jump("loc_45AE")

    label("loc_4541")


    ChrTalk(
        0x134,
        "#01709FOkay, let's go!\x02",
    )

    CloseMessageWindow()
    Jump("loc_45AE")

    label("loc_4562")


    ChrTalk(
        0x135,
        "#01802FYes, let's go.\x02",
    )

    CloseMessageWindow()
    Jump("loc_45AE")

    label("loc_4582")


    ChrTalk(
        0x166,
        (
            "#14000FHmph, well I'll tag\x01",
            "along.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_45AE")

    label("loc_45AE")

    SetChrPos(0x0, 0, -1000, -46000, 0)
    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_17_27F3 end

    def Function_18_45C4(): pass

    label("Function_18_45C4")

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

    def lambda_4680():
        OP_9B(0x1, 0xFE, 0xFFFA, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4680)

    def lambda_4695():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4695)
    Sleep(700)

    def lambda_46A9():
        OP_9B(0x1, 0xFE, 0x6, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_46A9)

    def lambda_46BE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xEF, 2, lambda_46BE)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x101, 2)
    WaitChrThread(0xEF, 1)
    WaitChrThread(0xEF, 2)
    Sound(118, 0, 100, 0)
    OP_71(0x4, 0x1E, 0x0, 0x0, 0x8)
    OP_79(0x4)
    SetMapObjFlags(0x4, 0x10)
    OP_6F(0x79)
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4D57")

    ChrTalk(
        0x101,
        (
            "#00000FThe top floor of Mirror\x01",
            "Castle, huh...\x02",
        )
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
            "#00005FThat must be the "bell"\x01",
            "he was talking about\x01",
            "earlier.\x02",
        )
    )

    CloseMessageWindow()
    Switch(
        (scpexpr(EXPR_23, 0x5), scpexpr(EXPR_END)),
        (0, "loc_4802"),
        (1, "loc_4871"),
        (2, "loc_48E0"),
        (3, "loc_4921"),
        (4, "loc_4961"),
        (5, "loc_49D8"),
        (6, "loc_4A4F"),
        (7, "loc_4A93"),
        (8, "loc_4B05"),
        (9, "loc_4B79"),
        (10, "loc_4BE0"),
        (SWITCH_DEFAULT, "loc_4C4C"),
    )


    label("loc_4802")


    ChrTalk(
        0x102,
        (
            "#00100FThere are ringing cords\x01",
            "on either side.\x02\x03",
            "#00104FI'm certain this is the\x01",
            "one I heard about.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_4C4C")

    label("loc_4871")


    ChrTalk(
        0x103,
        (
            "#00200FThere are ringing cords\x01",
            "on either side.\x02\x03",
            "#00204FI'm certain this is the\x01",
            "one I heard about.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_4C4C")

    label("loc_48E0")


    ChrTalk(
        0x104,
        (
            "#00300FYeah, there're ringin'\x01",
            "cords on either side.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_4C4C")

    label("loc_4921")


    ChrTalk(
        0x109,
        (
            "#10100FYes, there're ringing\x01",
            "cords on either side.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_4C4C")

    label("loc_4961")


    ChrTalk(
        0x105,
        (
            "#10300FThere are ringing cords\x01",
            "on either side.\x02\x03",
            "#10304FThere's no mistake. This\x01",
            "is the one I heard\x01",
            "about.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_4C4C")

    label("loc_49D8")


    ChrTalk(
        0x153,
        (
            "#01105FThere's ringing cords on\x01",
            "either side, see?\x02\x03",
            "#01111FI wonder if that's what\x01",
            "Elie was talking about.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_4C4C")

    label("loc_4A4F")


    ChrTalk(
        0x156,
        (
            "#06400FYes, there's ringing\x01",
            "cords on either side,\x01",
            "see?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_4C4C")

    label("loc_4A93")


    ChrTalk(
        0x14C,
        (
            "#05900FThere are ringing cords\x01",
            "on either side.\x02\x03",
            "#05904FI believe this must be\x01",
            "the one I heard about.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_4C4C")

    label("loc_4B05")


    ChrTalk(
        0x134,
        (
            "#01700FThere are ringing cords\x01",
            "on either side.\x02\x03",
            "#01704FThis is the one I heard\x01",
            "about, don't you think?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_4C4C")

    label("loc_4B79")


    ChrTalk(
        0x135,
        (
            "#01802FThere're ringing cords\x01",
            "on either side.\x02\x03",
            "#01804FThis must be the one I\x01",
            "heard about.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_4C4C")

    label("loc_4BE0")


    ChrTalk(
        0x166,
        (
            "#14000FThere are ringing cords\x01",
            "on either side...\x02\x03",
            "#14003FThis is the one I heard\x01",
            "about, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_4C4C")

    label("loc_4C4C")


    def lambda_4C51():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4C51)
    Sleep(50)

    def lambda_4C61():
        OP_93(0xEF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_4C61)
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
            "#00002FIn that case, that huge\x01",
            "mirror is the "Wish-\x01",
            "Granting Mirror".\x02",
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

    def lambda_4D2F():
        OP_93(0x101, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4D2F)
    Sleep(50)

    def lambda_4D3F():
        OP_93(0xEF, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_4D3F)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0xEF, 0)
    Jump("loc_4D86")

    label("loc_4D57")


    ChrTalk(
        0x101,
        (
            "#00000FPhew, we've reached the\x01",
            "top floor.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D86")

    Switch(
        (scpexpr(EXPR_23, 0x5), scpexpr(EXPR_END)),
        (0, "loc_4DD1"),
        (1, "loc_4E6E"),
        (2, "loc_4F0B"),
        (3, "loc_4FA2"),
        (4, "loc_5035"),
        (5, "loc_50C5"),
        (6, "loc_514F"),
        (7, "loc_51F3"),
        (8, "loc_5290"),
        (9, "loc_5325"),
        (10, "loc_53C6"),
        (SWITCH_DEFAULT, "loc_544F"),
    )


    label("loc_4DD1")


    ChrTalk(
        0x102,
        (
            "#00100FIf we ring the bell and stand\x01",
            "before the mirror, our wishes\x01",
            "will be granted, but...\x02\x03",
            "#00104FNow that I'm here, I'm\x01",
            "getting kind of nervous.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_544F")

    label("loc_4E6E")


    ChrTalk(
        0x103,
        (
            "#00200FIf we ring the bell and stand\x01",
            "before the mirror, our wishes\x01",
            "will be granted, but...\x02\x03",
            "#00204FNow that I'm here, I'm\x01",
            "getting kind of nervous.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_544F")

    label("loc_4F0B")


    ChrTalk(
        0x104,
        (
            "#00300FIf we ring the bell and stand\x01",
            "before the mirror, they say our\x01",
            "wishes will be granted, but...\x02\x03",
            "#00304FWhat should I wish for,\x01",
            "exactly?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_544F")

    label("loc_4FA2")


    ChrTalk(
        0x109,
        (
            "#10100FIf we ring the bell and stand\x01",
            "before the mirror, they say our\x01",
            "wishes will be granted, but...\x02\x03",
            "#10104FHmm, what should I wish for?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_544F")

    label("loc_5035")


    ChrTalk(
        0x105,
        (
            "#10300FIf we ring the bell and stand\x01",
            "before the mirror, it seems our\x01",
            "wishes will be granted, but...\x02\x03",
            "#10304FHmm, I wonder about that.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_544F")

    label("loc_50C5")


    ChrTalk(
        0x153,
        (
            "#01100FOur wishes will come true if\x01",
            "we ring the bell and stand in\x01",
            "front of the mirror, right?\x02\x03",
            "#01109FWhat should KeA wish for?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_544F")

    label("loc_514F")


    ChrTalk(
        0x156,
        (
            "#06400FThey say your wish will come true\x01",
            "if you stand in front of the\x01",
            "mirror and ring the bell, right?\x02\x03",
            "#06409FI wonder what I should wish for\x01",
            "this time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_544F")

    label("loc_51F3")


    ChrTalk(
        0x14C,
        (
            "#05900FIf we ring the bell and stand\x01",
            "before the mirror, it seems our\x01",
            "wishes will be granted, but...\x02\x03",
            "#05904FHaha, I wonder what I should\x01",
            "wish for.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_544F")

    label("loc_5290")


    ChrTalk(
        0x134,
        (
            "#01700FIt seems our wishes will be\x01",
            "granted if we ring the bell\x01",
            "and stand before the mirror.\x02\x03",
            "#01702FHuhu, I wonder what I should\x01",
            "wish for.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_544F")

    label("loc_5325")


    ChrTalk(
        0x135,
        (
            "#01803FIt seems our wishes will be\x01",
            "granted if we ring the bell\x01",
            "and stand before the mirror.\x02\x03",
            "#01808F(But... I can hardly believe\x01",
            "I actually have one.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_544F")

    label("loc_53C6")


    ChrTalk(
        0x166,
        (
            "#14003FIf you ring the bell and stand\x01",
            "in front of the mirror, your\x01",
            "wish will be granted, huh...\x02\x03",
            "#14008FI wonder if it's true.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_544F")

    label("loc_544F")

    Jc((scpexpr(EXPR_23, 0x5), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_54A1")

    ChrTalk(
        0x101,
        (
            "#00000FAlright then, let's try\x01",
            "ringing the bell\x01",
            "together.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_54E0")

    label("loc_54A1")


    ChrTalk(
        0x101,
        (
            "#00000FAlright then, let's try\x01",
            "ringing the bell\x01",
            "together.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_54E0")

    OP_D2(0x4, (scpexpr(EXPR_PUSH_LONG, 0x40000000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    SetChrPos(0x0, 0, 40550, -15500, 180)
    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_18_45C4 end

    def Function_19_54FF(): pass

    label("Function_19_54FF")

    TalkBegin(0xFF)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Ring the bell\x01",      # 0
            "Cancel\x01",             # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Sleep(200)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5540")
    Call(0, 20)
    Jump("loc_5540")

    label("loc_5540")

    TalkEnd(0xFF)
    Return()

    # Function_19_54FF end

    def Function_20_5544(): pass

    label("Function_20_5544")

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
            "#00000F#6P...Alright. Next, let's\x01",
            "stand before the\x01",
            ""mirror".\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xEF, 0x101, 500)
    Switch(
        (scpexpr(EXPR_23, 0x5), scpexpr(EXPR_END)),
        (0, "loc_565A"),
        (1, "loc_567D"),
        (2, "loc_56A0"),
        (3, "loc_56C3"),
        (4, "loc_56EA"),
        (5, "loc_570D"),
        (6, "loc_5731"),
        (7, "loc_5759"),
        (8, "loc_578F"),
        (9, "loc_57B3"),
        (10, "loc_57D6"),
        (SWITCH_DEFAULT, "loc_580C"),
    )


    label("loc_565A")


    ChrTalk(
        0x102,
        "#00100FYes, let's go.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_580C")

    label("loc_567D")


    ChrTalk(
        0x103,
        "#00200FYes, let's go.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_580C")

    label("loc_56A0")


    ChrTalk(
        0x104,
        "#00300FHaha, finally.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_580C")

    label("loc_56C3")


    ChrTalk(
        0x109,
        "#10100FIt's finally time.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_580C")

    label("loc_56EA")


    ChrTalk(
        0x105,
        "#10300FHehe, finally.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_580C")

    label("loc_570D")


    ChrTalk(
        0x153,
        "#01109FYeah, let's go!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_580C")

    label("loc_5731")


    ChrTalk(
        0x156,
        "#06400FHaha, I can't wait!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_580C")

    label("loc_5759")


    ChrTalk(
        0x14C,
        (
            "#05900FHaha. What will happen,\x01",
            "I wonder?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_580C")

    label("loc_578F")


    ChrTalk(
        0x134,
        "#01700FYeah, let's go.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_580C")

    label("loc_57B3")


    ChrTalk(
        0x135,
        "#01802FYes, let's go.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_580C")

    label("loc_57D6")


    ChrTalk(
        0x166,
        (
            "#14000FHmph, I guess I'll give\x01",
            "it a try.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_580C")

    label("loc_580C")

    OP_D2(0x4, (scpexpr(EXPR_PUSH_LONG, 0x80000000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    OP_65(0x3, 0x1)
    OP_65(0x4, 0x1)
    SetScenarioFlags(0x0, 0)
    OP_1B(0xC, 0x0, 0x2A)
    SetChrPos(0x0, -7700, 40550, -25000, 315)
    EventEnd(0x5)
    Return()

    # Function_20_5544 end

    def Function_21_5839(): pass

    label("Function_21_5839")

    Sound(918, 0, 100, 0)
    Sleep(2000)
    Sound(918, 0, 80, 0)
    Sleep(2000)
    Sound(918, 0, 60, 0)

    label("loc_5851")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_586A")
    Sleep(2000)
    Sound(918, 0, 40, 0)
    Jump("loc_5851")

    label("loc_586A")

    Return()

    # Function_21_5839 end

    def Function_22_586B(): pass

    label("Function_22_586B")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x80000000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_58CA")

    ChrTalk(
        0x101,
        (
            "#00000FWhoops... We've got to\x01",
            "first ring the bell\x01",
            "downstairs.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_597F")

    label("loc_58CA")

    Switch(
        (scpexpr(EXPR_23, 0x5), scpexpr(EXPR_END)),
        (0, "loc_5915"),
        (1, "loc_591D"),
        (2, "loc_5925"),
        (3, "loc_592D"),
        (4, "loc_5935"),
        (5, "loc_593D"),
        (6, "loc_5945"),
        (7, "loc_594D"),
        (8, "loc_5955"),
        (9, "loc_595D"),
        (10, "loc_5965"),
        (SWITCH_DEFAULT, "loc_596D"),
    )


    label("loc_5915")

    Call(0, 28)
    Jump("loc_596D")

    label("loc_591D")

    Call(0, 29)
    Jump("loc_596D")

    label("loc_5925")

    Call(0, 30)
    Jump("loc_596D")

    label("loc_592D")

    Call(0, 32)
    Jump("loc_596D")

    label("loc_5935")

    Call(0, 33)
    Jump("loc_596D")

    label("loc_593D")

    Call(0, 34)
    Jump("loc_596D")

    label("loc_5945")

    Call(0, 36)
    Jump("loc_596D")

    label("loc_594D")

    Call(0, 37)
    Jump("loc_596D")

    label("loc_5955")

    Call(0, 38)
    Jump("loc_596D")

    label("loc_595D")

    Call(0, 39)
    Jump("loc_596D")

    label("loc_5965")

    Call(0, 40)
    Jump("loc_596D")

    label("loc_596D")

    StopBGM(0xFA0)
    WaitBGM()
    SetScenarioFlags(0x22, 1)
    NewScene("t1400", 0, 0, 0)
    IdleLoop()

    label("loc_597F")

    TalkEnd(0xFF)
    Return()

    # Function_22_586B end

    def Function_23_5983(): pass

    label("Function_23_5983")

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

    # Function_23_5983 end

    def Function_24_59ED(): pass

    label("Function_24_59ED")

    Fade(800)
    EndChrThread(0xC, 0x1)
    SetMapObjFrame(0xFF, "Null_bell", 0x2, "stop")
    OP_0D()
    Sleep(2500)
    Return()

    # Function_24_59ED end

    def Function_25_5A0D(): pass

    label("Function_25_5A0D")


    def lambda_5A12():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5A12)
    OP_93(0xFE, 0x10E, 0x1F4)
    WaitChrThread(0x101, 2)
    Return()

    # Function_25_5A0D end

    def Function_26_5A26(): pass

    label("Function_26_5A26")


    def lambda_5A2B():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5A2B)
    OP_93(0xFE, 0x0, 0x1F4)
    WaitChrThread(0x101, 2)
    Return()

    # Function_26_5A26 end

    def Function_27_5A3F(): pass

    label("Function_27_5A3F")

    SetCameraDistance(14700, 3000)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Jc((scpexpr(EXPR_23, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5A7F")
    OP_63(0xFE, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_5A91")

    label("loc_5A7F")

    OP_63(0xFE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_5A91")

    Sleep(2500)
    OP_64(0x101)
    OP_64(0xFE)
    OP_6F(0x79)
    Return()

    # Function_27_5A3F end

    def Function_28_5A9D(): pass

    label("Function_28_5A9D")

    EventBegin(0x0)
    Call(0, 23)
    BeginChrThread(0x102, 3, 0, 25)
    WaitChrThread(0x102, 3)
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5B94")

    ChrTalk(
        0x101,
        (
            "#00000FAlright, let's make a\x01",
            "wish.\x02\x03",
            "#00005FUmm... I wonder if we\x01",
            "should say our wishes in\x01",
            "front of the mirror.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FJust thinking of our\x01",
            "wishes will be fine, I\x01",
            "think.\x02\x03",
            "Then, let's give it a\x01",
            "try.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5BF7")

    label("loc_5B94")


    ChrTalk(
        0x101,
        (
            "#00000FWe need only think of\x01",
            "our wishes before the\x01",
            "mirror.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FAlright, let's try it.\x02",
    )

    CloseMessageWindow()

    label("loc_5BF7")

    BeginChrThread(0x102, 3, 0, 26)
    WaitChrThread(0x102, 3)

    ChrTalk(
        0x101,
        "#00003F...............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00103F...............\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x102, 3, 0, 27)
    WaitChrThread(0x102, 3)
    Call(0, 24)
    BeginChrThread(0x102, 3, 0, 25)
    WaitChrThread(0x102, 3)

    ChrTalk(
        0x101,
        "#00000F...That should do it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104FYes, I'm finished as\x01",
            "well.\x02\x03",
            "#00100FBy the way... What did\x01",
            "you wish for, Lloyd?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5E23")

    ChrTalk(
        0x101,
        (
            "#00000FHaha, well I'm a little\x01",
            "embarrassed 'cause it's so\x01",
            "normal.\x02\x03",
            "#00004FThat I can keep protecting\x01",
            "Crossbell, I guess.\x02\x03",
            "#00000FKeA, you and the other\x01",
            "Support Section members are\x01",
            "included in that, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FHaha, how very like you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHaha, thanks.\x02\x03",
            "#00000FSo, what did you wish\x01",
            "for, Elie?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5F39")

    label("loc_5E23")


    ChrTalk(
        0x101,
        (
            "#00000FI made my greatest wish when I\x01",
            "first came here, you see.\x02\x03",
            "#00004FRather than wishing for the\x01",
            "same thing again, I wished for\x01",
            "your wish to come true, Elie.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FHaha. Thank you, Lloyd.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHaha, you're welcome.\x02\x03",
            "#00000FAnd, what did you wish\x01",
            "for, Elie?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5F39")

    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x102)

    ChrTalk(
        0x102,
        (
            "#00103FFor my mother and father\x01",
            "to live happily, I\x01",
            "guess.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005FYour parents...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F...*giggle*, I told you about them\x01",
            "before, right? They divorced ten\x01",
            "years ago, and they each live in the\x01",
            "Republic and Empire, respectively.\x02\x03",
            "#00104FEven now I stay in touch through\x01",
            "letters and orbal communication, but\x01",
            "I hardly ever see them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008FThat must be lonely.\x02\x03",
            "#00003FI lost my parents when I was little,\x01",
            "but my brother and Cecil were there\x01",
            "for me so I wasn't that lonely...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FHaha. My grandfather is here in\x01",
            "Crossbell with me, so it isn't\x01",
            "the case that I've been lonely.\x02\x03",
            "#00103FIf pushed, it might be more\x01",
            "accurate to say that I'm\x01",
            "worried.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FWorried?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FMy mother and father contact me\x01",
            "sometimes because they worry about\x01",
            "how I'm doing, but...\x02\x03",
            "#00108FIf that is because they still regret\x01",
            "having left me behind, well, I think\x01",
            "it's a very painful thing.\x02\x03",
            "Those two are very serious. They're\x01",
            "the type that can't forget the past\x01",
            "and go on living.\x02\x03",
            "#00104FIt's been 10 years since then. It is\x01",
            "time. I want them each to begin to\x01",
            "walk new paths in life and be happy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008FForget the past and\x01",
            "start new lives, huh?\x02\x03",
            "#00001FBut, you can't say that\x01",
            "was a good thing\x01",
            "unconditionally, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FYes, I know. It's precisely\x01",
            "because of that past that I'm\x01",
            "here now.\x02\x03",
            "#00104FBut, I just want mother and\x01",
            "father to be happy, no matter\x01",
            "what form that takes...\x02\x03",
            "#00100FHaha, sorry. This\x01",
            "conversation was rather\x01",
            "strange, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FNo... That's not true.\x02\x03",
            "#00000FFor your parents to be\x01",
            "happy... That's what I\x01",
            "wish for, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00109F*giggle*, thank you.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_28_5A9D end

    def Function_29_65B9(): pass

    label("Function_29_65B9")

    EventBegin(0x0)
    Call(0, 23)
    BeginChrThread(0x103, 3, 0, 25)
    WaitChrThread(0x103, 3)
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_66BD")

    ChrTalk(
        0x101,
        (
            "#00000FAlright, let's make a\x01",
            "wish.\x02\x03",
            "#00005FUmm... I wonder if we\x01",
            "should say our wishes in\x01",
            "front of the mirror.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FI think just thinking of\x01",
            "our wishes will probably\x01",
            "be fine.\x02\x03",
            "Well then, let's give it\x01",
            "a try.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6723")

    label("loc_66BD")


    ChrTalk(
        0x101,
        (
            "#00000FWe need only think of\x01",
            "our wishes before the\x01",
            "mirror.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FYes, let's give it a\x01",
            "try.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6723")

    BeginChrThread(0x103, 3, 0, 26)
    WaitChrThread(0x103, 3)

    ChrTalk(
        0x101,
        "#00003F...............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00203F...............\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x103, 3, 0, 27)
    WaitChrThread(0x103, 3)
    Call(0, 24)
    BeginChrThread(0x103, 3, 0, 25)
    WaitChrThread(0x103, 3)

    ChrTalk(
        0x101,
        "#00000F...That should do it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00204F...Yes, I finished as\x01",
            "well.\x02\x03",
            "#00200FJust for reference, what\x01",
            "did you wish for, Lloyd?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6961")

    ChrTalk(
        0x101,
        (
            "#00000FHaha, well I'm a little\x01",
            "embarrassed 'cause it's so\x01",
            "normal.\x02\x03",
            "#00004FThat I can keep protecting\x01",
            "Crossbell, I guess.\x02\x03",
            "#00000FKeA, you and the other\x01",
            "Support Section members are\x01",
            "included in that, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FI see... That's very\x01",
            "like you, Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHaha, thanks.\x02\x03",
            "#00000FSo Tio, what did you\x01",
            "wish for?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6A78")

    label("loc_6961")


    ChrTalk(
        0x101,
        (
            "#00000FI made my greatest wish when I\x01",
            "first came here, you see.\x02\x03",
            "#00004FRather than wishing for the\x01",
            "same thing again, I wished for\x01",
            "your wish to come true, Tio.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FI see... Thank you for\x01",
            "that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHaha, you're welcome.\x02\x03",
            "#00000FSo Tio, what did you\x01",
            "wish for?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6A78")


    ChrTalk(
        0x103,
        (
            "#00203F...For Chief Roberts'\x01",
            "annoyances to lighten up\x01",
            "a little.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00012FI-I feel bad for the\x01",
            "chief.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00202F...That was a joke.\x02\x03",
            "#00203FActually... I wished to\x01",
            "find meaning in being\x01",
            "alive.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x103,
        (
            "#00200FI've spoken with you and\x01",
            "the others before about\x01",
            "it.\x02\x03",
            "#00203FThe answer to the question\x01",
            "I tried to but couldn't\x01",
            "ask Guy three years ago.\x02\x03",
            "#00208FI still haven't found it,\x01",
            "even after overcoming the\x01",
            "cult incident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FI told you, right Tio?\x01",
            "There aren't that many\x01",
            "people who know the answer.\x02\x03",
            "#00000FThere is no need to rush to\x01",
            "find an answer, and no need\x01",
            "to find it by yourself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00204FYes, naturally I know that.\x02\x03",
            "#00200FI am not rushing. And I understand now\x01",
            "that everyone can help me.\x02\x03",
            "#00203FHowever, this problem can be said to be\x01",
            "the challenge of my life.\x02\x03",
            "#00200FThat is why, someday, I will definitely\x01",
            "find the answer. With that intent in my\x01",
            "heart, I wished on the mirror.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FHaha, I see. Sorry, it\x01",
            "seems I worried\x01",
            "needlessly.\x02\x03",
            "#00004FIn that case, I guess I'll\x01",
            "express my intentions to\x01",
            "you once again.\x02\x03",
            "#00000FSo that you may one day\x01",
            "find that answer... we\x01",
            "will support you too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00209FHaha... I'll be counting\x01",
            "on you.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_29_65B9 end

    def Function_30_6F4A(): pass

    label("Function_30_6F4A")

    EventBegin(0x0)
    Call(0, 23)
    BeginChrThread(0x104, 3, 0, 25)
    WaitChrThread(0x104, 3)
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7047")

    ChrTalk(
        0x101,
        (
            "#00000FAlright, let's make a\x01",
            "wish.\x02\x03",
            "#00005FUmm... I wonder if we\x01",
            "should say our wishes in\x01",
            "front of the mirror.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FIt'll probably be fine\x01",
            "if we just think of our\x01",
            "wishes.\x02\x03",
            "Alright then, let's do\x01",
            "this.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_70B0")

    label("loc_7047")


    ChrTalk(
        0x101,
        (
            "#00000FWe need only think of\x01",
            "our wishes before the\x01",
            "mirror.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FAlright then, let's do\x01",
            "this.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_70B0")

    BeginChrThread(0x104, 3, 0, 26)
    WaitChrThread(0x104, 3)

    ChrTalk(
        0x101,
        "#00003F...............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00303F...............\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x104, 3, 0, 27)
    WaitChrThread(0x104, 3)
    Call(0, 24)
    BeginChrThread(0x104, 3, 0, 25)
    WaitChrThread(0x104, 3)

    ChrTalk(
        0x101,
        "#00000F...That should do it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00304FYeah, I'm done too.\x02\x03",
            "#00309FSo, Lloyd. What stuff\x01",
            "did you wish for?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_734B")

    ChrTalk(
        0x101,
        (
            "#00000FHaha, well I'm a little\x01",
            "embarrassed 'cause it's so\x01",
            "normal.\x02\x03",
            "#00004FThat I can keep protecting\x01",
            "Crossbell, I guess.\x02\x03",
            "#00000FKeA, you and the other\x01",
            "Support Section members are\x01",
            "included in that, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FHaha. You're one serious guy, you\x01",
            "know that?\x02\x03",
            "#00306FYou weren't gonna get punished if you\x01",
            "wished for something a little more\x01",
            "true to your own desires, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FA-And so, what did you\x01",
            "wish for, Randy?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_74A7")

    label("loc_734B")


    ChrTalk(
        0x101,
        (
            "#00000FI made my greatest wish when I\x01",
            "first came here, you see.\x02\x03",
            "#00004FRather than wishing for the\x01",
            "same thing again, I wished for\x01",
            "your wish to come true, Randy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00305FWhoa, seriously!?\x02\x03",
            "#00309FMan, that's why you're\x01",
            "you. Your timing couldn't\x01",
            "have been better!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00005FUmm... What did you wish\x01",
            "for, Randy?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_74A7")


    ChrTalk(
        0x104,
        (
            "#00304FMe? Of course, it was to\x01",
            "build a happy harem with\x01",
            "the babes of Crossbell─\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F─Yeah, that's enough.\x01",
            "I'm a fool for even\x01",
            "asking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00305FHey now, isn't that what\x01",
            "every man dreams of?\x02\x03",
            "#00304FCecil and the other\x01",
            "nurses, Bracer Eolia...\x02\x03",
            "#00309FThere's a lot of girls I\x01",
            "like here in Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FNow look here... I won't\x01",
            "let you include Cecil those\x01",
            "delusions of yours.\x02\x03",
            "#00002FWell, in a way, I'm\x01",
            "relieved. Since it's a wish\x01",
            "that will never come true.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x104,
        (
            "#00306FW-Why do you gotta be such a\x01",
            "downer?\x02\x03",
            "#00300F...Oh, I get it. You jealous?\x02\x03",
            "#00304FYou can rest easy, all right.\x01",
            "When it does come true, I'll\x01",
            "give you some good...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00011FW-Who would be worried\x01",
            "about something like\x01",
            "that!?\x02\x03",
            "#00006F...*sigh*, honestly. We\x01",
            "made our wishes. Let's\x01",
            "just go.\x02",
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
            "#00308F(A wish that'll never\x01",
            "come true, huh.)\x02\x03",
            "#00303F(That we can stay friends\x01",
            "forever... It's too good\x01",
            "for a fool like me.)\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_93(0x104, 0xE1, 0x1F4)
    OP_9B(0x0, 0x104, 0x0, 0x7D0, 0x7D0, 0x0)
    OP_0D()
    Return()

    # Function_30_6F4A end

    def Function_31_78A4(): pass

    label("Function_31_78A4")

    OP_93(0xFE, 0xE1, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
    Return()

    # Function_31_78A4 end

    def Function_32_78BB(): pass

    label("Function_32_78BB")

    EventBegin(0x0)
    Call(0, 23)
    BeginChrThread(0x109, 3, 0, 25)
    WaitChrThread(0x109, 3)
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_79BA")

    ChrTalk(
        0x101,
        (
            "#00000FAlright, let's make a\x01",
            "wish.\x02\x03",
            "#00005FUmm... I wonder if we\x01",
            "should say our wishes in\x01",
            "front of the mirror.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FI think just thinking of\x01",
            "our wishes will probably\x01",
            "be fine.\x02\x03",
            "Then, let's give it a\x01",
            "try.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7A47")

    label("loc_79BA")


    ChrTalk(
        0x101,
        (
            "#00000FAlright, let's wish for\x01",
            "something.\x02\x03",
            "Just stand in front of\x01",
            "the mirror and think of\x01",
            "your wish.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10100FAlright, let's try it.\x02",
    )

    CloseMessageWindow()

    label("loc_7A47")

    BeginChrThread(0x109, 3, 0, 26)
    WaitChrThread(0x109, 3)

    ChrTalk(
        0x101,
        "#00003F...............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10103F...............\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x109, 3, 0, 27)
    WaitChrThread(0x109, 3)
    Call(0, 24)
    BeginChrThread(0x109, 3, 0, 25)
    WaitChrThread(0x109, 3)

    ChrTalk(
        0x101,
        "#00000F...That should do it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10104FYes, I finished too.\x02\x03",
            "#10100F...Umm, what did you\x01",
            "wish for, Lloyd?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7C71")

    ChrTalk(
        0x101,
        (
            "#00000FHaha, well I'm a little\x01",
            "embarrassed 'cause it's so\x01",
            "normal.\x02\x03",
            "#00004FThat I can keep protecting\x01",
            "Crossbell, I guess.\x02\x03",
            "#00000FThe other Guardian Force and\x01",
            "Support Section members are\x01",
            "included in that, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FI see. That's very like\x01",
            "you, Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHaha, thanks.\x02\x03",
            "So, what did you wish\x01",
            "for, Noｱl?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7D8C")

    label("loc_7C71")


    ChrTalk(
        0x101,
        (
            "#00000FI made my greatest wish when I\x01",
            "first came here, you see.\x02\x03",
            "#00004FRather than wishing for the\x01",
            "same thing again, I wished for\x01",
            "your wish to come true, Noｱl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FAhaha... Thank you very\x01",
            "much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHaha, you're welcome.\x02\x03",
            "#00000FSo, what did you wish\x01",
            "for, Noｱl?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7D8C")


    ChrTalk(
        0x109,
        (
            "#10100FMine's simple. "To be a\x01",
            "wonderful guardsman."\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHaha... A direct wish.\x01",
            "That's just like you,\x01",
            "Noｱl.\x02\x03",
            "#00000FYou must be aiming to be\x01",
            "as great as your father,\x01",
            "then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FAhaha... I said it\x01",
            "before, but I'm self-\x01",
            "conscious about that.\x02\x03",
            "#10104FI was a kid too, once,\x01",
            "and I almost hated my\x01",
            "strict father.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FOh, I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10102FYeah, he was really\x01",
            "strict.\x02\x03",
            "#10104FIf Fran or I ever did\x01",
            "anything bad, he'd beat\x01",
            "us with his bare fists.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x109,
        (
            "#10103FBut I remember my mom took us to a\x01",
            "border gate so I could see my dad\x01",
            "working.\x02\x03",
            "#10108FAt that time there was a corrupt command\x01",
            "structure, and all those protecting\x01",
            "Crossbell's borders had it tough...\x02\x03",
            "#10100FThinking about it now... That might have\x01",
            "been when I first felt respect toward\x01",
            "the idea of protecting one's home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FI see... So your father\x01",
            "influenced your own\x01",
            "strict personality.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10109FAhaha, that's right.\x02\x03",
            "#10103FBut for the life of me, I\x01",
            "can't understand why Fran has\x01",
            "such a cheerful personality.\x02\x03",
            "#10101FCould it be that dad only\x01",
            "loved Fran?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00012FWell, it's possible that\x01",
            "it was a reaction to the\x01",
            "strictness.\x02\x03",
            "#00000FWell then, we made our\x01",
            "wishes. We should be\x01",
            "going.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10100FYes, I agree.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_32_78BB end

    def Function_33_8281(): pass

    label("Function_33_8281")

    EventBegin(0x0)
    Call(0, 23)
    BeginChrThread(0x105, 3, 0, 25)
    WaitChrThread(0x105, 3)
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_838B")

    ChrTalk(
        0x101,
        (
            "#00000FAlright, let's make a\x01",
            "wish.\x02\x03",
            "#00005FUmm... I wonder if we\x01",
            "should say our wishes in\x01",
            "front of the mirror.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FIt'll probably be fine\x01",
            "if we just think of our\x01",
            "wishes, right?\x02\x03",
            "Alright then, let's give\x01",
            "it a try.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_842B")

    label("loc_838B")


    ChrTalk(
        0x101,
        (
            "#00000FAlright, let's wish for\x01",
            "something.\x02\x03",
            "#00004FJust stand in front of\x01",
            "the mirror and think of\x01",
            "your wish.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FAlright then, let's give\x01",
            "it a try.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_842B")

    BeginChrThread(0x105, 3, 0, 26)
    WaitChrThread(0x105, 3)

    ChrTalk(
        0x101,
        "#00003F...............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10303F...............\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x105, 3, 0, 27)
    WaitChrThread(0x105, 3)
    Call(0, 24)
    BeginChrThread(0x105, 3, 0, 25)
    WaitChrThread(0x105, 3)

    ChrTalk(
        0x101,
        "#00000F...That should do it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FI've finished too.\x02\x03",
            "#10300FAnd, what did you wish\x01",
            "for?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8643")

    ChrTalk(
        0x101,
        (
            "#00000FHaha, well I'm a little\x01",
            "embarrassed 'cause it's so\x01",
            "normal.\x02\x03",
            "#00004FThat I can keep protecting\x01",
            "Crossbell, I guess.\x02\x03",
            "#00000FKeA, you and the other\x01",
            "Support Section members are\x01",
            "included in that, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10300FHehe, how very like you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHaha, thanks.\x02\x03",
            "#00000FAnd so, what did you\x01",
            "wish for, Wazy?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_876A")

    label("loc_8643")


    ChrTalk(
        0x101,
        (
            "#00000FI made my greatest wish when I\x01",
            "first came here, you see.\x02\x03",
            "#00004FRather than wishing for the\x01",
            "same thing again, I wished for\x01",
            "your wish to come true, Wazy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FHehe, you're really\x01",
            "softhearted, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHaha, you're welcome.\x02\x03",
            "#00000FAnd so, what did you\x01",
            "wish for, Wazy?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_876A")


    ChrTalk(
        0x105,
        (
            "#10302FHehe. If I had to say...\x02\x03",
            "#10304FFor my former brawl\x01",
            "enemy to find his own\x01",
            "path, I guess.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00008FI heard the rumors, but... They\x01",
            "say Wald hasn't been showing up\x01",
            "at his base recently.\x02\x03",
            "#00003FNot that it's your fault or\x01",
            "anything...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10309FI'm not sentimental enough to\x01",
            "feel any responsibility for that.\x02\x03",
            "#10300FI anticipated he'd be discouraged\x01",
            "and desperate to some degree\x01",
            "after our duel on that rainy day.\x02\x03",
            "#10304FWhether he'd stay depressed or\x01",
            "get over it and move on? That's\x01",
            "Wald's problem.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00006FThat's an, umm, cool point of\x01",
            "view, huh...\x02\x03",
            "#00000FBut if you really felt that way,\x01",
            "you wouldn't have wished for Wald\x01",
            "to find his own path, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FHehe. You're quite right about\x01",
            "that. But, I didn't make that\x01",
            "wish for me, you see.\x02\x03",
            "#10300FIf he stays depressed... it\x01",
            "will mean I taught him nothing\x01",
            "in our duel that rainy day.\x02\x03",
            "#10303FIf that happens, I'll have no\x01",
            "choice but to take\x01",
            "responsibility for it...\x02\x03",
            "#10309FWouldn't that be really lame?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F*sigh*, oh man. I know how\x01",
            "you really feel.\x02\x03",
            "#00000FBut, for Wald and the other\x01",
            "Vipers to find their own\x01",
            "paths... I wish for that too.\x02\x03",
            "I really hope it comes true.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303FHehe. You really are\x01",
            "softhearted, aren't you.\x02\x03",
            "#10309FI can't get enough of\x01",
            "that side of you.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00006FAh, that's enough out of you.\x01",
            "I wrapped it up so nicely, and\x01",
            "you had to make fun of me!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_33_8281 end

    def Function_34_8D19(): pass

    label("Function_34_8D19")

    EventBegin(0x0)
    Call(0, 23)
    BeginChrThread(0x153, 3, 0, 25)
    WaitChrThread(0x153, 3)
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8DFE")

    ChrTalk(
        0x101,
        (
            "#00000FAlright, let's make a\x01",
            "wish.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#01100FShould we say it in\x01",
            "front of the mirror?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FI think it's fine if you\x01",
            "just think of your wish.\x02\x03",
            "...Alright. Let's give\x01",
            "it a try.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8E83")

    label("loc_8DFE")


    ChrTalk(
        0x101,
        (
            "#00000FAlright, let's wish for\x01",
            "something.\x02\x03",
            "#00004FJust stand in front of\x01",
            "the mirror and think of\x01",
            "your wish.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#01100FGot it.\x02",
    )

    CloseMessageWindow()

    label("loc_8E83")

    BeginChrThread(0x153, 3, 0, 26)
    WaitChrThread(0x153, 3)

    ChrTalk(
        0x101,
        "#00003F...............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#01103F...Mmm...\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x153, 3, 0, 27)
    WaitChrThread(0x153, 3)
    Call(0, 24)
    BeginChrThread(0x153, 3, 0, 25)
    WaitChrThread(0x153, 3)

    ChrTalk(
        0x101,
        "#00000F...That should do it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#01109FYep, KeA's done too.\x02\x03",
            "#01105FHey Lloyd. What did you\x01",
            "wish for?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_90A4")

    ChrTalk(
        0x101,
        (
            "#00000FHaha, well I'm a little\x01",
            "embarrassed 'cause it's so\x01",
            "normal.\x02\x03",
            "#00004FThat I can keep protecting\x01",
            "Crossbell, I guess.\x02\x03",
            "#00000FYou and the other Support\x01",
            "Section members are\x01",
            "included in that, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#01109FEhehe... That sounds\x01",
            "like you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHaha, thanks.\x02\x03",
            "#00000FHow about you, KeA? What\x01",
            "did you wish for?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_91BB")

    label("loc_90A4")


    ChrTalk(
        0x101,
        (
            "#00000FI made my greatest wish when I\x01",
            "first came here, you see.\x02\x03",
            "#00004FRather than wishing for the\x01",
            "same thing again, I wished for\x01",
            "your wish to come true, KeA.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#01109FEhehe... thanks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHaha, you're welcome.\x02\x03",
            "#00000FHow about you, KeA? What\x01",
            "did you wish for?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_91BB")


    ChrTalk(
        0x153,
        (
            "#01106FUmm, there were a lot of\x01",
            "things I wanted to wish\x01",
            "for, but...\x02\x03",
            "#01100FThe most important is\x01",
            ""for Shizuku's eyes to\x01",
            "get better".\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00003F...Yeah. I hope they\x01",
            "really do.\x02\x03",
            "#00008FShizuku's eye surgery\x01",
            "looks quite difficult,\x01",
            "though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#01111FBut, wishes made before\x01",
            "this mirror will come\x01",
            "true, right?\x02\x03",
            "#01101FIf so, KeA 'll wish as\x01",
            "many times as it takes!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FHaha... Yeah, I'll do\x01",
            "the same.\x02\x03",
            "#00004F(I hope a miracle really\x01",
            "does happen.)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x153, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x153, 0x0, 0x1F4)

    ChrTalk(
        0x153,
        "#01111F...?\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005FWhat's wrong, KeA?\x02",
    )

    CloseMessageWindow()
    OP_93(0x153, 0x10E, 0x1F4)

    ChrTalk(
        0x153,
        (
            "#01103F...Mmm, it's nothing.\x02\x03",
            "#01109FBut Lloyd, let's ring\x01",
            "the bell a lot more!\x02",
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
            "#00009FHaha... She's a bundle\x01",
            "of energy.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_34_8D19 end

    def Function_35_94C0(): pass

    label("Function_35_94C0")

    OP_93(0xFE, 0x87, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x1F40, 0xFA0, 0x0)
    Return()

    # Function_35_94C0 end

    def Function_36_94D7(): pass

    label("Function_36_94D7")

    EventBegin(0x0)
    Call(0, 23)
    BeginChrThread(0x156, 3, 0, 25)
    WaitChrThread(0x156, 3)
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_95DE")

    ChrTalk(
        0x101,
        (
            "#00000FAlright, let's make a\x01",
            "wish.\x02\x03",
            "#00005FUmm... I wonder if we\x01",
            "should say our wishes in\x01",
            "front of the mirror.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x156,
        (
            "#06400FI think it's probably\x01",
            "fine if we just think of\x01",
            "our wishes.\x02\x03",
            "Alright then, let's give\x01",
            "it a try!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_967E")

    label("loc_95DE")


    ChrTalk(
        0x101,
        (
            "#00000FAlright, let's wish for\x01",
            "something.\x02\x03",
            "#00004FJust stand in front of\x01",
            "the mirror and think of\x01",
            "your wish.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x156,
        (
            "#06400FAlright then, let's give\x01",
            "it a try!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_967E")

    BeginChrThread(0x156, 3, 0, 26)
    WaitChrThread(0x156, 3)

    ChrTalk(
        0x101,
        "#00003F...............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x156,
        "#06403F...............\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x156, 3, 0, 27)
    WaitChrThread(0x156, 3)
    Call(0, 24)
    BeginChrThread(0x156, 3, 0, 25)
    WaitChrThread(0x156, 3)

    ChrTalk(
        0x101,
        "#00000F...That should do it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x156,
        (
            "#06400FYes, I've wished too.\x02\x03",
            "#06409FBy the way, what did you\x01",
            "wish for, Lloyd?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9898")

    ChrTalk(
        0x101,
        (
            "#00000FHaha, well I'm a little\x01",
            "embarrassed 'cause it's\x01",
            "so normal.\x02\x03",
            "#00004FThat I can keep\x01",
            "protecting Crossbell, I\x01",
            "guess.\x02\x03",
            "#00000FYou and the other\x01",
            "officers are included in\x01",
            "that, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x156,
        (
            "#06402FHaha, that's very like\x01",
            "you, Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHaha, thanks.\x02\x03",
            "#00000FSo Fran, what did you\x01",
            "wish for?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_99AE")

    label("loc_9898")


    ChrTalk(
        0x101,
        (
            "#00000FI made my greatest wish when I\x01",
            "first came here, you see.\x02\x03",
            "#00004FRather than wishing for the\x01",
            "same thing again, I wished for\x01",
            "your wish to come true, Fran.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x156,
        (
            "#06402FHaha, thank you for\x01",
            "that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHaha, you're welcome.\x02\x03",
            "#00000FSo Fran, what did you\x01",
            "wish for?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_99AE")


    ChrTalk(
        0x156,
        (
            "#06409FHaha. I of course wished\x01",
            "to be like my sister, you\x01",
            "know?\x02\x03",
            "#06401FAfter all, my eternal\x01",
            "goal is to be a cool and\x01",
            "reliable woman like Noｱl!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FA woman like Noｱl, you\x01",
            "say... It's a wish that's\x01",
            "very like you, I'd say.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00005FI have a simple question for you though...\x01",
            "Didn't you want to be a CGF member?\x02\x03",
            "#00000FSince you idolize Noｱl that much, it\x01",
            "wouldn't be out of the question if you\x01",
            "wanted to be a CGF member like her, I think.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x156,
        (
            "#06400FAhaha, well in that case... You know\x01",
            "that each of us has different places\x01",
            "we fit in, right?\x02\x03",
            "#06403FIn my case, I got better grades on\x01",
            "administrative systems than on drills\x01",
            "at the police academy, you see...\x02\x03",
            "#06400FAnd so, I thought to protect\x01",
            "Crossbell in a way that suited me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FIt's true that it's not only our\x01",
            "field personnel that protect\x01",
            "Crossbell, isn't it.\x02\x03",
            "#00004FIt's only because of operations\x01",
            "HQ and the work of the operators\x01",
            "there that we can do what we do.\x02\x03",
            "#00009FAnd that's why you became a\x01",
            "receptionist... You're certainly\x01",
            "qualified.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x156,
        (
            "#06409FEhehe... You'll\x01",
            "embarrass me if you say\x01",
            "that much, though.\x02\x03",
            "#06400FEven my wish, to be like\x01",
            "my sister, has certain\x01",
            "limits, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FHaha, I see.\x02\x03",
            "#00000F...Alright then, we've made\x01",
            "our wishes. Is it about\x01",
            "time for us to be going?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x156,
        "#06409FYes, let's go!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_36_94D7 end

    def Function_37_9EEC(): pass

    label("Function_37_9EEC")

    EventBegin(0x0)
    Call(0, 23)
    BeginChrThread(0x14C, 3, 0, 25)
    WaitChrThread(0x14C, 3)
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9FE9")

    ChrTalk(
        0x101,
        (
            "#00000FAlright, let's make a\x01",
            "wish.\x02\x03",
            "#00005FUmm... I wonder if we\x01",
            "should say our wishes in\x01",
            "front of the mirror.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14C,
        (
            "#05900FI wonder if just\x01",
            "thinking our wishes\x01",
            "would be all right.\x02\x03",
            "Then, let's give it a\x01",
            "try.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A07D")

    label("loc_9FE9")


    ChrTalk(
        0x101,
        (
            "#00000FAlright, let's wish for\x01",
            "something.\x02\x03",
            "#00004FJust stand in front of\x01",
            "the mirror and think of\x01",
            "your wish.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14C,
        "#05900FAlright, let's try it.\x02",
    )

    CloseMessageWindow()

    label("loc_A07D")

    BeginChrThread(0x14C, 3, 0, 26)
    WaitChrThread(0x14C, 3)

    ChrTalk(
        0x101,
        "#00003F...............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14C,
        "#05903F...............\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x14C, 3, 0, 27)
    WaitChrThread(0x14C, 3)
    Call(0, 24)
    BeginChrThread(0x14C, 3, 0, 25)
    WaitChrThread(0x14C, 3)

    ChrTalk(
        0x101,
        "#00000F...That should do it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14C,
        (
            "#05904FYes, I think so.\x02\x03",
            "#05900FI wonder what you wished\x01",
            "for, Lloyd.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A298")

    ChrTalk(
        0x101,
        (
            "#00000FHaha, well I'm a little\x01",
            "embarrassed 'cause it's so\x01",
            "normal.\x02\x03",
            "#00004FThat I can keep protecting\x01",
            "Crossbell, I guess.\x02\x03",
            "#00000FYou and the other Support\x01",
            "Section members are\x01",
            "included in that, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14C,
        "#05902FHaha, how very like you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHaha, thanks.\x02\x03",
            "#00000FAnd so, what did you\x01",
            "wish for, Cecil?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A3AF")

    label("loc_A298")


    ChrTalk(
        0x101,
        (
            "#00000FI made my greatest wish when I\x01",
            "first came here, you see.\x02\x03",
            "#00004FRather than wishing for the\x01",
            "same thing again, I wished for\x01",
            "your wish to come true, Cecil.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14C,
        "#05902FHaha, thanks Lloyd.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHaha, you're welcome.\x02\x03",
            "#00000FAnd so, what did you\x01",
            "wish for, Cecil?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A3AF")


    ChrTalk(
        0x14C,
        (
            "#05900FAs you may think, I\x01",
            "wished for you and the\x01",
            "others to always be well.\x02\x03",
            "#05904FThat is my greatest wish,\x01",
            "you see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FOh, thank you Cecil.\x02\x03",
            "#00000FWe'll take care not to\x01",
            "get seriously injured and\x01",
            "taken to the hospital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14C,
        (
            "#05909FHaha, please do.\x02\x03",
            "#05901FShould that ever happen, I'll\x01",
            "give you so many painful\x01",
            "shots, you'll cry, you hear?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00006F(That seems like something Randy\x01",
            "would enjoy...)\x02\x03",
            "#00000FYou too Cecil. Don't force yourself\x01",
            "to work all the time and take breaks\x01",
            "every now and then, will you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14C,
        (
            "#05905FHmm. When I think about the\x01",
            "patients, I want to work as\x01",
            "much as I can, you know.\x02\x03",
            "#05909FAnd, I'll take vacations\x01",
            "like this sometimes, so it\x01",
            "will be all right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FWell in your case, you\x01",
            "take vacations only\x01",
            "rarely...\x02\x03",
            "#00001FEven I worry about you,\x01",
            "you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14C,
        (
            "#05904FHmm... Yes, I know. I'll\x01",
            "take care not to force\x01",
            "myself, ok?\x02\x03",
            "#05909FHaha. Even so, to worry\x01",
            "about your sister... You've\x01",
            "grown up too, haven't you.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00006FThere you go treating me\x01",
            "like a kid again...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14C,
        "#05902FHaha, sorry, sorry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F(As I thought, I'll\x01",
            "always think of Cecil as\x01",
            "my sister.)\x02\x03",
            "#00006F(...I feel a little sad,\x01",
            "though.)\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_37_9EEC end

    def Function_38_A881(): pass

    label("Function_38_A881")

    EventBegin(0x0)
    Call(0, 23)
    BeginChrThread(0x134, 3, 0, 25)
    WaitChrThread(0x134, 3)
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A997")

    ChrTalk(
        0x101,
        (
            "#00000FThen, let's make our\x01",
            "wishes right away.\x02\x03",
            "#00005FUmm... I wonder if we\x01",
            "should say our wishes in\x01",
            "front of the mirror.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x134,
        (
            "#01700FIt'll probably be fine\x01",
            "if we just think of our\x01",
            "wishes, right?\x02\x03",
            "Alright then, let's give\x01",
            "it a try.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AA35")

    label("loc_A997")


    ChrTalk(
        0x101,
        (
            "#00000FAlright then, let's try\x01",
            "wishing for something.\x02\x03",
            "#00004FWe need only think of\x01",
            "our wishes before the\x01",
            "mirror.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x134,
        (
            "#01700FOkay, let's give it a\x01",
            "try.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AA35")

    BeginChrThread(0x134, 3, 0, 26)
    WaitChrThread(0x134, 3)

    ChrTalk(
        0x101,
        "#00003F...............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x134,
        "#01703F...............\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x134, 3, 0, 27)
    WaitChrThread(0x134, 3)
    Call(0, 24)
    BeginChrThread(0x134, 3, 0, 25)
    WaitChrThread(0x134, 3)

    ChrTalk(
        0x101,
        "#00000F...That should do it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x134,
        (
            "#01704FYeah, I'm good.\x02\x03",
            "#01700FBy the way, what did you\x01",
            "wish for little bro?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AC4E")

    ChrTalk(
        0x101,
        (
            "#00000FHaha. It's so normal it's\x01",
            "embarrassing, but...\x02\x03",
            "#00004FThat I can keep\x01",
            "protecting Crossbell, I\x01",
            "guess.\x02\x03",
            "#00000FYou and the other Arc-en-\x01",
            "Ciel members are included\x01",
            "in that, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x134,
        (
            "#01702FHuhu, I see. What a fine\x01",
            "thing to say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHaha, thanks.\x02\x03",
            "#00000FWhat did you wish for,\x01",
            "Ilya.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AD6F")

    label("loc_AC4E")


    ChrTalk(
        0x101,
        (
            "#00000FI made my greatest wish when I\x01",
            "first came here, you see.\x02\x03",
            "#00004FRather than wishing for the\x01",
            "same thing again, I wished for\x01",
            "your wish to come true, Ilya.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x134,
        (
            "#01702FMy, how considerate of\x01",
            "you, little bro.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHaha, you're welcome.\x02\x03",
            "#00000FWhat did you wish for,\x01",
            "Ilya.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AD6F")


    ChrTalk(
        0x134,
        (
            "#01704FI of course wished to continue\x01",
            "my dancing, no matter what\x01",
            "happens.\x02\x03",
            "#01700FWell even if I didn't wish for\x01",
            "it, my stepping down from the\x01",
            "stage is absolutely impossible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FHaha, just as I thought.\x01",
            "Your obsession with the\x01",
            "stage is second to none.\x02\x03",
            "#00009FI'm always surprised.\x01",
            "Where does all that\x01",
            "power come from?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x134,
        (
            "#01703FHmm, let's see. If I had to\x01",
            "say...\x02\x03",
            "#01700FIt's that more than anyone, I\x01",
            ""love" dancing on stage, I\x01",
            "guess.\x02\x03",
            "In that regard, I'm confident\x01",
            "I'll never lose to anyone, even\x01",
            "across the entire continent...\x02\x03",
            "#01709FAs long as I feel this way,\x01",
            "I'll keep dancing until the day\x01",
            "I die.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FLove, huh... Although\x01",
            "it's very simple, I feel\x01",
            "like I get it.\x02\x03",
            "#00004FSuch strong feelings\x01",
            "might be amazing in\x01",
            "their own right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x134,
        (
            "#01700FHuhu, it's no big deal. Love and hate\x01",
            "are feelings everyone has.\x02\x03",
            "#01709FYou too, little bro. If it's for\x01",
            "someone you care about, you're\x01",
            "willing to bet even your life, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00000FYes... I really think so.\x02\x03",
            "#00004F(We were able to settle the cult\x01",
            "incident because of our strong\x01",
            "desire to protect KeA as well...)\x02\x03",
            "(People can become incredibly\x01",
            "strong if it's for the sake of\x01",
            "those precious to them, huh.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x134,
        (
            "#01700FHuhu, looks like you get\x01",
            "it.\x02\x03",
            "#01709FC'mon, we've made our\x01",
            "wishes. It's time to be\x01",
            "going.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes, let's.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_38_A881 end

    def Function_39_B2AE(): pass

    label("Function_39_B2AE")

    EventBegin(0x0)
    Call(0, 23)
    BeginChrThread(0x135, 3, 0, 25)
    WaitChrThread(0x135, 3)
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B3B1")

    ChrTalk(
        0x101,
        (
            "#00000FAlright, let's make a\x01",
            "wish.\x02\x03",
            "#00005FUmm... I wonder if we\x01",
            "should say our wishes in\x01",
            "front of the mirror.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x135,
        (
            "#01802FJust thinking of our\x01",
            "wishes will be fine, I\x01",
            "suppose.\x02\x03",
            "#01803F...Then, let's give it a\x01",
            "try.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B448")

    label("loc_B3B1")


    ChrTalk(
        0x101,
        (
            "#00000FAlright, let's wish for\x01",
            "something.\x02\x03",
            "#00004FJust stand in front of\x01",
            "the mirror and think of\x01",
            "your wish.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x135,
        (
            "#01803FYes, let's give it a\x01",
            "try.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B448")

    BeginChrThread(0x135, 3, 0, 26)
    WaitChrThread(0x135, 3)

    ChrTalk(
        0x101,
        "#00003F...............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x135,
        "#01803F...............\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x135, 3, 0, 27)
    WaitChrThread(0x135, 3)
    Call(0, 24)
    BeginChrThread(0x135, 3, 0, 25)
    WaitChrThread(0x135, 3)

    ChrTalk(
        0x101,
        "#00000F...That should do it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x135,
        (
            "#01804FYes, I'm finished as\x01",
            "well.\x02\x03",
            "#01802FUmm, what did you wish\x01",
            "for, Lloyd?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B66E")

    ChrTalk(
        0x101,
        (
            "#00000FHaha, well I'm a little\x01",
            "embarrassed 'cause it's\x01",
            "so normal.\x02\x03",
            "#00004FThat I can keep\x01",
            "protecting Crossbell, I\x01",
            "guess.\x02\x03",
            "#00000FYou and the other Arc-en-\x01",
            "Ciel members are included\x01",
            "in that, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x135,
        (
            "#01802FI see. That's very like\x01",
            "you, Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHaha, thanks.\x02\x03",
            "#00000FSo Rixia, what did you\x01",
            "wish for?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B784")

    label("loc_B66E")


    ChrTalk(
        0x101,
        (
            "#00000FI made my greatest wish when I\x01",
            "first came here, you see.\x02\x03",
            "#00004FRather than wishing for the\x01",
            "same thing again, I wished for\x01",
            "your wish to come true, Rixia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x135,
        "#01802FI see. Haha, thank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHaha, you're welcome.\x02\x03",
            "#00000FSo Rixia, what did you\x01",
            "wish for?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B784")

    OP_63(0x135, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x135)

    ChrTalk(
        0x135,
        (
            "#01803FMy wish was "I want to\x01",
            "become an artist like\x01",
            "Ilya."\x02\x03",
            "#01802FHaha. That might sound\x01",
            "ridiculous coming from a\x01",
            "novice like me, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FNo... That can't be true,\x01",
            "can it?\x02\x03",
            "#00003FIt seems you're quite\x01",
            "popular in the Arc-en-Ciel\x01",
            "performances...\x02\x03",
            "#00000FAnd most of all, your\x01",
            "talents were recognised by\x01",
            "Ilya.\x02\x03",
            "#00009FIf you keep up your hard\x01",
            "work, I feel you will surely\x01",
            "become a big star like Ilya.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x135, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(
        0x135,
        (
            "#01809FN-No way... Someone like\x01",
            "me really has a long way\x01",
            "to go.\x02\x03",
            "#01804FI think Sully has far\x01",
            "greater talent than\x01",
            "someone like me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FHmm. I think it'd be all right\x01",
            "if you were a little more\x01",
            "confident, though.\x02\x03",
            "#00000FWell I'll root for you so your\x01",
            "wish comes true... So please\x01",
            "do your best from now on, ok?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x135,
        (
            "#01809FR-Right. Thank you very\x01",
            "much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FHaha. It was a little\x01",
            "embarrassing saying that\x01",
            "to your face, though.\x02\x03",
            "#00000FWell then, we're finished\x01",
            "with our wishes, so is it\x01",
            "time to be going?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x135,
        "#01802FYes, let's go.\x02",
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
            "#01803F#11P(Even if it's a wish\x01",
            "that will never come\x01",
            "true...)\x02\x03",
            "#01808F(I can be forgiven just\x01",
            "for thinking about it,\x01",
            "right?)\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_9B(0x0, 0x135, 0x0, 0x7D0, 0x7D0, 0x0)
    OP_0D()
    EndChrThread(0x101, 0x3)
    Return()

    # Function_39_B2AE end

    def Function_40_BC53(): pass

    label("Function_40_BC53")

    EventBegin(0x0)
    Call(0, 23)
    BeginChrThread(0x166, 3, 0, 25)
    WaitChrThread(0x166, 3)
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BD4C")

    ChrTalk(
        0x101,
        (
            "#00000FAlright, let's make a\x01",
            "wish.\x02\x03",
            "#00005FUmm... I wonder if we\x01",
            "should say our wishes in\x01",
            "front of the mirror.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x166,
        (
            "#14000FJust thinking of our\x01",
            "wishes is fine, isn't\x01",
            "it?\x02\x03",
            "#14003FLet's get this over\x01",
            "with.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BDE9")

    label("loc_BD4C")


    ChrTalk(
        0x101,
        (
            "#00000FAlright, let's wish for\x01",
            "something.\x02\x03",
            "#00004FJust stand in front of\x01",
            "the mirror and think of\x01",
            "your wish.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x166,
        (
            "#14003FWell, let's get this\x01",
            "over with.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BDE9")

    BeginChrThread(0x166, 3, 0, 26)
    WaitChrThread(0x166, 3)

    ChrTalk(
        0x101,
        "#00003F...............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x166,
        "#14008F...............\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x166, 3, 0, 27)
    WaitChrThread(0x166, 3)
    Call(0, 24)
    BeginChrThread(0x166, 3, 0, 25)
    WaitChrThread(0x166, 3)

    ChrTalk(
        0x101,
        "#00000F...That should do it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x166,
        (
            "#14003FYeah, I'm good too.\x02\x03",
            "#14000FSo, what did you wish\x01",
            "for?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BFFD")

    ChrTalk(
        0x101,
        (
            "#00000FHaha, well I'm a little\x01",
            "embarrassed 'cause it's\x01",
            "so normal.\x02\x03",
            "#00004FThat I can keep\x01",
            "protecting Crossbell, I\x01",
            "guess.\x02\x03",
            "#00000FYou and the other Arc-en-\x01",
            "Ciel members are included\x01",
            "in that, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x166,
        (
            "#14000FHmm... Well I guess\x01",
            "that's fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHaha, thanks.\x02\x03",
            "#00000FSo Sully, what did you\x01",
            "wish for?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C11E")

    label("loc_BFFD")


    ChrTalk(
        0x101,
        (
            "#00000FI made my greatest wish when I\x01",
            "first came here, you see.\x02\x03",
            "#00004FRather than wishing for the\x01",
            "same thing again, I wished for\x01",
            "your wish to come true, Sully.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x166,
        (
            "#14006FTch. I don't need your\x01",
            "help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FHaha... I guess I was\x01",
            "nosy.\x02\x03",
            "#00000FSo Sully, what did you\x01",
            "wish for?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C11E")

    OP_63(0x166, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x166)

    ChrTalk(
        0x166,
        (
            "#14003FI... didn't wish for\x01",
            "anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F*shock*... Hey, explain\x01",
            "that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x166,
        (
            "#14006FWishes are stuff that\x01",
            "really don't come true\x01",
            "in the first place.\x02\x03",
            "#14008FThe slum I lived in was\x01",
            "like that.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x166,
        (
            "#14000FThere were so many guys like\x01",
            "me in the slum I'm from.\x02\x03",
            "#14003FI drifted to Crossbell and\x01",
            "Miss Ilya picked me up, but...\x01",
            "that was just sheer luck.\x02\x03",
            "#14008FAnd so, wishing for more than\x01",
            "that would be too much to ask\x01",
            "for.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        "#00004FSully... You're kind.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x166,
        "#14005F...Huh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FThere's not that many\x01",
            "people who think so much\x01",
            "of others, I think.\x02\x03",
            "#00004FYou are kind and have a\x01",
            "sympathetic heart, you\x01",
            "see.\x02\x03",
            "#00000FBut... Do you have to\x01",
            "deny your own happiness\x01",
            "just because of that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x166,
        "#14008FB-But...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYou don't have to think so hard\x01",
            "about it. Just having something\x01",
            "to wish for is fine, isn't it?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x166, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x166,
        (
            "#14006FAh, jeez, I got it... You're\x01",
            "a preachy and annoying guy,\x01",
            "you know that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FS-Sorry for being\x01",
            "preachy.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x166, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x166)

    ChrTalk(
        0x166,
        (
            "#14003FI don't know what the future holds,\x01",
            "but there is something I want to\x01",
            "come true.\x02\x03",
            "#14000FFor the Arc-en-Ciel renewal\x01",
            "performance to be a success... For\x01",
            "now, that's all I want to come true.\x02\x03",
            "#14009FThat ok?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FYeah, why not?\x02\x03",
            "I will wish, from the\x01",
            "bottom of my heart, for\x01",
            "it to come true as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x166,
        (
            "#14012FD-Don't say embarrassing\x01",
            "stuff like that straight\x01",
            "to my face, jeez!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_40_BC53 end

    def Function_41_C6EC(): pass

    label("Function_41_C6EC")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000FWe're aiming for the top\x01",
            "floor. Let's head there\x01",
            "right away.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 0, -950, -53650, 0)
    EventEnd(0x4)
    Return()

    # Function_41_C6EC end

    def Function_42_C74C(): pass

    label("Function_42_C74C")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000FLet's try making a wish\x01",
            "in front of the "mirror"\x01",
            "upstairs.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 0, 40550, -13830, 180)
    EventEnd(0x4)
    Return()

    # Function_42_C74C end

    def Function_43_C7AA(): pass

    label("Function_43_C7AA")

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
            scpstr(SCPSTR_CODE_ITEM, 0x394),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x394, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x18A, 4)
    OP_65(0x6, 0x1)
    EventEnd(0x3)
    Return()

    # Function_43_C7AA end

    SaveToFile()

Try(main)
