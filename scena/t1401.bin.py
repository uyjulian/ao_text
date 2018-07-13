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

    Sepith("Sepith_CD30", 15,  5,   5,   5,   10,  5,   25)
    Sepith("Sepith_CD28", 10,  6,   6,   6,   1,   4,   10)

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
        "BattleInfo_6A4", 0x0000, 78, 6, 60, 6, 1, 20, 0, "bt1400", "Sepith_CD30", 40, 30, 20, 10,
        (
            ("ms79600.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3CC", "MonsterBattlePostion_42C", "ed7450", "ed7453", "ATBonus_37C"),
            ("ms79600.dat", "ms82300.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3AC", "MonsterBattlePostion_42C", "ed7450", "ed7453", "ATBonus_37C"),
            ("ms79600.dat", "ms82300.dat", "ms82300.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_3CC", "MonsterBattlePostion_42C", "ed7450", "ed7453", "ATBonus_37C"),
            ("ms79600.dat", "ms82300.dat", "ms82300.dat", "ms82300.dat", 0, 0, 0, 0, "MonsterBattlePostion_3AC", "MonsterBattlePostion_42C", "ed7450", "ed7453", "ATBonus_37C"),
        )
    )

    BattleInfo(
        "BattleInfo_5DC", 0x0000, 78, 6, 45, 6, 1, 20, 0, "bt1400", "Sepith_CD28", 40, 30, 20, 10,
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
        "Function_4_12FD",         # 04, 4
        "Function_5_144F",         # 05, 5
        "Function_6_149C",         # 06, 6
        "Function_7_14CA",         # 07, 7
        "Function_8_1512",         # 08, 8
        "Function_9_154D",         # 09, 9
        "Function_10_1C1C",        # 0A, 10
        "Function_11_2287",        # 0B, 11
        "Function_12_2297",        # 0C, 12
        "Function_13_266A",        # 0D, 13
        "Function_14_26D9",        # 0E, 14
        "Function_15_2748",        # 0F, 15
        "Function_16_27B1",        # 10, 16
        "Function_17_2820",        # 11, 17
        "Function_18_4702",        # 12, 18
        "Function_19_5680",        # 13, 19
        "Function_20_56C3",        # 14, 20
        "Function_21_59C8",        # 15, 21
        "Function_22_59FA",        # 16, 22
        "Function_23_5B0A",        # 17, 23
        "Function_24_5B74",        # 18, 24
        "Function_25_5B94",        # 19, 25
        "Function_26_5BAD",        # 1A, 26
        "Function_27_5BC6",        # 1B, 27
        "Function_28_5C24",        # 1C, 28
        "Function_29_675D",        # 1D, 29
        "Function_30_7166",        # 1E, 30
        "Function_31_7B41",        # 1F, 31
        "Function_32_7B58",        # 20, 32
        "Function_33_856D",        # 21, 33
        "Function_34_9035",        # 22, 34
        "Function_35_9812",        # 23, 35
        "Function_36_9829",        # 24, 36
        "Function_37_A218",        # 25, 37
        "Function_38_AC90",        # 26, 38
        "Function_39_B70C",        # 27, 39
        "Function_40_C108",        # 28, 40
        "Function_41_CBE3",        # 29, 41
        "Function_42_CC34",        # 2A, 42
        "Function_43_CC93",        # 2B, 43
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
            "Since you have too many, you gave it up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x0, 0x1E, 0x0, 0x0, 0x0)

    label("loc_12A2")

    Jump("loc_12F1")

    label("loc_12A7")

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

    label("loc_12F1")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_11AB end

    def Function_4_12FD(): pass

    label("Function_4_12FD")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1FD, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13F9")
    Sound(14, 0, 100, 0)
    OP_74(0x2, 0x1E)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x650, 1)"), scpexpr(EXPR_END)), "loc_1382")
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
    Jump("loc_13F4")

    label("loc_1382")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x650),
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

    label("loc_13F4")

    Jump("loc_1443")

    label("loc_13F9")

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

    label("loc_1443")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_12FD end

    def Function_5_144F(): pass

    label("Function_5_144F")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Aah, it's so beautiful that\x01",
            "I'm staring at it unintentionally...\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_5_144F end

    def Function_6_149C(): pass

    label("Function_6_149C")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "That planetarium...\x01",
            "How pretty...\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_6_149C end

    def Function_7_14CA(): pass

    label("Function_7_14CA")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Uh uh, even if we don't hurry,\x01",
            "the "mirror" won't run away.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_7_14CA end

    def Function_8_1512(): pass

    label("Function_8_1512")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Mamaaa, quick, quick!\x01",
            "The stairs are this way!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_8_1512 end

    def Function_9_154D(): pass

    label("Function_9_154D")

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

    def lambda_1617():
        OP_9B(0x0, 0x101, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1617)
    Sleep(50)

    def lambda_162F():
        OP_9B(0x0, 0x102, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_162F)
    Sleep(50)

    def lambda_1647():
        OP_9B(0x0, 0x103, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1647)
    Sleep(50)

    def lambda_165F():
        OP_9B(0x0, 0x104, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_165F)
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
            "#00201F#12PIt seems these particles of\x01",
            "spiritual energy are going up...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_18B5")
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
        "#00013FThe front entrance...!\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(200, 140, -1, -1)

    AnonymousTalk(
        0x104,
        (
            "#00306FYeah... So it's closed, is it?\x02\x03",
            "#00301FInstead, entrances on the\x01",
            "left and right opened up...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_1A2F")

    label("loc_18B5")

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
            "#00301FTch, the interior's\x01",
            "structure has changed...!\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(100, 140, -1, -1)

    AnonymousTalk(
        0x101,
        "#00005FIs that so...?\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(200, 140, -1, -1)

    AnonymousTalk(
        0x104,
        (
            "#00303FYeah. When I came in here before,\x01",
            "the frontal entrance was opened...\x02\x03",
            "#00301FInstead, entrances on the\x01",
            "left and right opened up...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_1A2F")

    Fade(1000)
    OP_68(0, 1200, -47500, 0)
    MoveCamera(0, 11, 0, 0)
    OP_6E(540, 0)
    SetCameraDistance(18000, 0)
    OP_0D()

    ChrTalk(
        0x102,
        (
            "#00106F#6PI came here some times before, but I don't\x01",
            "remember seeing anything that could cause that...\x02\x03",
            "#00108FCould this be "her" doing too...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F#12P...I hear the sound of\x01",
            "machinery deeper inside.\x02\x03",
            "#00201FIf we are going, we will need to be careful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#5PWe'll do whatever it\x01",
            "takes to reach the top...\x02\x03",
            "#00013FTo interrogate Mr. Arios,\x01",
            "and to take back KeA too...!\x02",
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

    # Function_9_154D end

    def Function_10_1C1C(): pass

    label("Function_10_1C1C")

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

    def lambda_1D42():
        OP_93(0x101, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1D42)
    Sleep(30)

    def lambda_1D52():
        OP_93(0x102, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1D52)
    Sleep(30)

    def lambda_1D62():
        OP_93(0x103, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1D62)
    Sleep(30)

    def lambda_1D72():
        OP_93(0x104, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1D72)
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
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E61")
    SetMessageWindowPos(50, 140, -1, -1)

    AnonymousTalk(
        0x101,
        "#00013FWe're finally here...\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(230, 140, -1, -1)

    AnonymousTalk(
        0x104,
        "#00301FYeah... The top floor.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1EBE")

    label("loc_1E61")

    SetMessageWindowPos(50, 140, -1, -1)

    AnonymousTalk(
        0x101,
        "#00013FDid we arrive...?\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(230, 140, -1, -1)

    AnonymousTalk(
        0x104,
        (
            "#00301FYeah...  \x01",
            "This is the top floor.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EBE")

    SetMessageWindowPos(70, 140, -1, -1)

    AnonymousTalk(
        0x102,
        (
            "#00108FB-But... \x01",
            "Neither KeA nor Mr.\x01",
            "Arios seem to be here...\x02",
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
            "#00206F#6P...I didn't notice the last\x01",
            "time I was here, but...\x02\x03",
            "#00201FIt seems there is a hidden space\x01",
            "inside that large, shining mirror.\x02",
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

    def lambda_2047():
        TurnDirection(0x101, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2047)
    Sleep(50)

    def lambda_2057():
        TurnDirection(0x102, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_2057)
    Sleep(50)

    def lambda_2067():
        TurnDirection(0x104, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_2067)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)

    ChrTalk(
        0x101,
        "#00005F#11PSeriously...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F#6PYes. A significant amount of\x01",
            "spiritual energy is flowing in.\x02\x03",
            "#00201FI think that is the end of the line.\x02",
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
            "to track them down somehow...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#11PYeah...\x02\x03",
            "#00007FEveryone──ready your gear!\x01",
            "We'll definitely take back KeA!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_21D9():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_21D9)
    Sleep(50)

    def lambda_21E9():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_21E9)
    Sleep(50)

    def lambda_21F9():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_21F9)
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

    # Function_10_1C1C end

    def Function_11_2287(): pass

    label("Function_11_2287")

    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
    Return()

    # Function_11_2287 end

    def Function_12_2297(): pass

    label("Function_12_2297")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24BF")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Faint particles of light are being sucked into the mirror.\x07\x00\x02",
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
            "#00006F#6P(It looks like we can enter\x01",
            "the mirror just like this...)\x02\x03",
            "#00013F(...KeA... We're coming now!)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x183, 3)
    Jump("loc_252B")

    label("loc_24BF")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Faint particles of light are being sucked into the mirror.\x02\x03",
            "It seems we can enter the mirror.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_252B")

    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Step Inside the Mirror\x01",      # 0
            "Back Away\x01",                   # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2586"),
        (1, "loc_263F"),
        (SWITCH_DEFAULT, "loc_2669"),
    )


    label("loc_2586")

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
    Jump("loc_2669")

    label("loc_263F")

    FadeToDark(500, 0, -1)
    OP_0D()
    OP_D7(0x1E)
    OP_37()
    SetChrPos(0x0, 0, 44500, -4000, 180)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Jump("loc_2669")

    label("loc_2669")

    Return()

    # Function_12_2297 end

    def Function_13_266A(): pass

    label("Function_13_266A")


    def lambda_266F():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_266F)
    Sleep(500)
    Sound(341, 0, 100, 0)

    def lambda_268D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_268D)
    PlayEffect(0x0, 0xFF, 0xFE, 0x0, 0, 1000, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0xFE, 2)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_13_266A end

    def Function_14_26D9(): pass

    label("Function_14_26D9")


    def lambda_26DE():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_26DE)
    Sleep(1000)

    def lambda_26F6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_26F6)
    Sound(920, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0xFE, 0x0, 0, 1000, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0xFE, 2)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_14_26D9 end

    def Function_15_2748(): pass

    label("Function_15_2748")


    def lambda_274D():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_274D)
    Sleep(1000)

    def lambda_2765():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2765)
    PlayEffect(0x0, 0xFF, 0xFE, 0x0, 0, 1000, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0xFE, 2)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_15_2748 end

    def Function_16_27B1(): pass

    label("Function_16_27B1")


    def lambda_27B6():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_27B6)
    Sleep(1500)

    def lambda_27CE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_27CE)
    Sound(920, 0, 60, 0)
    PlayEffect(0x0, 0xFF, 0xFE, 0x0, 0, 1000, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0xFE, 2)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_16_27B1 end

    def Function_17_2820(): pass

    label("Function_17_2820")

    EventBegin(0x0)
    OP_E2(0x3)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_443E")
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

    def lambda_292C():
        OP_9B(0x0, 0x101, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_292C)
    Sleep(50)

    def lambda_2944():
        OP_9B(0x0, 0xEF, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_2944)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0xEF, 0)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00000FSo this is "Mirror Castle"?\x02\x03",
            "It seems to be the landmark\x01",
            "attraction of the park...\x02\x03",
            "#00006F...How to put it, I can\x01",
            "only say it's amazing.\x02",
        )
    )

    CloseMessageWindow()
    Switch(
        (scpexpr(EXPR_23, 0x5), scpexpr(EXPR_END)),
        (0, "loc_2A43"),
        (1, "loc_2CF9"),
        (2, "loc_2F3E"),
        (3, "loc_3194"),
        (4, "loc_33F5"),
        (5, "loc_364A"),
        (6, "loc_3869"),
        (7, "loc_3AE4"),
        (8, "loc_3D2B"),
        (9, "loc_3F4A"),
        (10, "loc_4183"),
        (SWITCH_DEFAULT, "loc_4439"),
    )


    label("loc_2A43")


    ChrTalk(
        0x102,
        (
            "#00104FIt seems that a fantastical atmosphere is\x01",
            "created by the planetarium over there.\x02\x03",
            "#00100FWhen I was studying abroad in Liberl I went on a\x01",
            "field trip at Grancel Castle in the royal capital.\x01",
            "I think that it doesn't pale for atmosphere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FWell, that's really amazing.\x01",
            "What you'd expect from IBC, I'd say...\x02\x03",
            "#00005FBy the way, they say a\x01",
            ""Wish-Granting Mirror"\x01",
            "is in here somewhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FYes. It's said that if you ring the bell\x01",
            "and stand in front of the mirror,\x01",
            "it will grant you what you wish.\x02\x03",
            "#00104FAccording to what I've heard,\x01",
            "it should be at the castle's top floor...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FThen, let's go up to the\x01",
            "top floor and search.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FYes, all right.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4439")

    label("loc_2CF9")


    ChrTalk(
        0x103,
        (
            "#00204FDue to the planetarium in the center,\x01",
            "a fantastical aura is brought forth.\x02\x03",
            "#00200FIt looks just like a castle\x01",
            "out of a fairytale.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah, it feels that way for sure.\x01",
            "What you'd expect from IBC, I'd say...\x02\x03",
            "#00005FBy the way, they say a\x01",
            ""Wish-Granting Mirror"\x01",
            "is in here somewhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FAccording to what Miss Elie said,\x01",
            "if you ring the bell and stand in front of\x01",
            "the mirror, it will grant you what you wish.\x02\x03",
            "#00204FIt seems it is on the\x01",
            "castle's top floor...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FThen, let's go up to the\x01",
            "top floor and search.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00200FYes, let's go.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4439")

    label("loc_2F3E")


    ChrTalk(
        0x104,
        (
            "#00304FThanks to the planetarium in the center,\x01",
            "a fantastical mood is produced.\x02\x03",
            "#00300FHa ha, it's so full-blown that\x01",
            "this place looks like a real castle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah, it really feels that way.\x01",
            "What you'd expect from IBC, I'd say...\x02\x03",
            "#00005FBy the way, they say a\x01",
            ""Wish-Granting Mirror"\x01",
            "is in here somewhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FYeah, the story that if you ring the bell and stand\x01",
            "in front of the mirror, it grants wishes, right?\x02\x03",
            "#00304FSince it's at the top floor,\x01",
            "we'll know for sure if we go upstairs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FThen, let's go up to the\x01",
            "top floor and search.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00300FYeah, let's.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4439")

    label("loc_3194")


    ChrTalk(
        0x109,
        (
            "#10104FDue to the planetarium revolving at the centre,\x01",
            "a fantastical atmosphere is produced.\x02\x03",
            "#10100FSeeing it so full-blown makes\x01",
            "it look like a real castle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah, it really feels that way.\x01",
            "What you'd expect from IBC, I'd say...\x02\x03",
            "#00005FBy the way, they say a\x01",
            ""Wish-Granting Mirror"\x01",
            "is in here somewhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FYes. It is said that if you ring the bell and\x01",
            "stand in front of the mirror, it'll grant your wish.\x02\x03",
            "#10104FSince it's at the top floor,\x01",
            "we'll know it immediately when we go upstairs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FThen, let's go up to the\x01",
            "top floor and search.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10100FYes, let's go.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4439")

    label("loc_33F5")


    ChrTalk(
        0x105,
        (
            "#10304FDue to the central planetarium,\x01",
            "a fantastical air is produced.\x02\x03",
            "#10302FHu hu, amazingly elaborated.\x01",
            "It looks like such a building\x01",
            "has costed quite some mira.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah, I'm completely scared\x01",
            "by IBC's funds power...\x02\x03",
            "#00005FBy the way, they say a\x01",
            ""Wish-Granting Mirror"\x01",
            "is in here somewhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FYeah, the story that if you ring the bell and\x01",
            "stand in front of the mirror, it grants wishes, right?\x02\x03",
            "#10304FIt seems it's on the top floor, \x01",
            "so we'll know for sure when we go upstair.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FThen, let's go up to the\x01",
            "top floor and search.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10300FHu hu, roger.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4439")

    label("loc_364A")


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
            "#00000FOh, that's a planetarium.\x01",
            "It produces the magical\x01",
            "atmosphere you see in here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#01105FEeh... That's pretty cool.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah, I honestly can't even\x01",
            "describe it. That's IBC for you...\x02\x03",
            "#00005FBy the way, they say a\x01",
            ""Wish-Granting Mirror"\x01",
            "is in here somewhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#01100FThat mirror Elie was talking about?\x01",
            "I'm sure she said it's at the top of the castle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FAlright, then let's try heading to the\x01",
            "top floor and looking there for it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#01109FAgreed!\x02",
    )

    CloseMessageWindow()
    Jump("loc_4439")

    label("loc_3869")


    ChrTalk(
        0x156,
        (
            "#06404FIt seems that due the planetarium at the center,\x01",
            "a magical atmosphere is produced.\x02\x03",
            "#06400FUh uh, being so full-blown makes\x01",
            "you think that it's like a real castle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah, it really feels that way.\x01",
            "What you'd expect from IBC, I'd say...\x02\x03",
            "#00005FBy the way, they say a\x01",
            ""Wish-Granting Mirror"\x01",
            "is in here somewhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x156,
        (
            "#06400FYes. It's said that if you stay in\x01",
            "front of the mirror and ring the bell,\x01",
            "it'll grant what you wished for.\x02\x03",
            "#06404FIt's a the top floor, so if we go\x01",
            "upstairs we'll find it immediately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FThen, let's go up to the\x01",
            "top floor and search.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x156,
        "#06409FYes! Let's go have a look!\x02",
    )

    CloseMessageWindow()
    Jump("loc_4439")

    label("loc_3AE4")


    ChrTalk(
        0x14C,
        (
            "#05904FCould that in the center be a planetarium?\x01",
            "It has a very magical atmosphere.\x02\x03",
            "#05902FUh uh, there was such a castle in a picture\x01",
            "book I once read to you, Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FHa ha...\x01",
            "It's true it looks like a fairytale's castle.\x02\x03",
            "#00005FBy the way, they say a\x01",
            ""Wish-Granting Mirror"\x01",
            "is in here somewhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14C,
        (
            "#05900FMiss Elie said that if you ring the bell\x01",
            "and stand in front of the mirror,\x01",
            "it will grant you what you wish for.\x02\x03",
            "#05904FIt seems it is at the\x01",
            "castle's top floor...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FThen, let's go up to the\x01",
            "top floor and search.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14C,
        "#05900FYes, let's go.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4439")

    label("loc_3D2B")


    ChrTalk(
        0x134,
        (
            "#01704FBecause of the planetarium in the centre,\x01",
            "a fantastical aura is made, eh...?\x02\x03",
            "#01702FHm, maybe I could make build one\x01",
            "for the Arc-en-ciel too in the future.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FHa ha...typical of you, Miss Ilya.\x02\x03",
            "#00005FBy the way, they say a\x01",
            ""Wish-Granting Mirror"\x01",
            "is in here somewhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x134,
        (
            "#01700FYeah, if you ring the bell and stand in front of\x01",
            "the mirror, it'll grant your wish. That one, right?\x02\x03",
            "#01704FSeems it's on the castle's top floor...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FThen, let's go up to the\x01",
            "top floor and search.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x134,
        "#01709FOK, let's go!\x02",
    )

    CloseMessageWindow()
    Jump("loc_4439")

    label("loc_3F4A")


    ChrTalk(
        0x135,
        (
            "#01804FThe planetarium at the centre creates\x01",
            "a fantastical atmosphere.\x02\x03",
            "#01802FUh uh, if Miss Ilya saw it,\x01",
            "maybe she'd want it for a play.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FHa ha... I can easily picture her wanting it.\x02\x03",
            "#00005FBy the way, they say a\x01",
            ""Wish-Granting Mirror"\x01",
            "is in here somewhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x135,
        (
            "#01805FOh, the one said that if you ring the bell and stand\x01",
            "in front of the mirror, it will grant your wish...?\x02\x03",
            "#01804FAccording to what Miss Elie said,\x01",
            "it seems it's at the castle's top floor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FThen, let's go up to the\x01",
            "top floor and search.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x135,
        "#01809FYes, let's go.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4439")

    label("loc_4183")


    ChrTalk(
        0x166,
        (
            "#14005FWhat's that thing spinning\x01",
            "around at the center?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FOh, that's a planetarium.\x01",
            "It produces the magical\x01",
            "atmosphere you see in here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x166,
        (
            "#14000FEeh... I don't get it well,\x01",
            "but somehow it's cool.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah, I honestly can't even\x01",
            "describe it. That's IBC for you...\x02\x03",
            "#00005FBy the way, they say a\x01",
            ""Wish-Granting Mirror"\x01",
            "is in here somewhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x166,
        (
            "#14000FAh, the one that I was told before...?\x01",
            "If you ring the bell and stand in front\x01",
            "of the mirror, it'll grant your wish.\x02\x03",
            "#14003FSeems it's at the castle's top floor.\x01",
            "Do you believe in that stuff?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FHa ha, I don't know yet...\x01",
            "Should we go to the top floor and look?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x166,
        "#14000FHmph, well, I'll tag along.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4439")

    label("loc_4439")

    Jump("loc_46EC")

    label("loc_443E")

    SetChrPos(0x101, -500, -950, -51000, 0)
    SetChrPos(0xEF, 500, -950, -51000, 0)
    OP_68(0, 1050, -46000, 0)
    MoveCamera(0, 10, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(16500, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(13500, 3000)

    def lambda_44A5():
        OP_9B(0x0, 0x101, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_44A5)
    Sleep(50)

    def lambda_44BD():
        OP_9B(0x0, 0xEF, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_44BD)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0xEF, 0)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00000FThen, let's aim together for the \x01",
            ""Wish-Granting Mirror" at the top floor!\x02",
        )
    )

    CloseMessageWindow()
    Switch(
        (scpexpr(EXPR_23, 0x5), scpexpr(EXPR_END)),
        (0, "loc_457D"),
        (1, "loc_459E"),
        (2, "loc_45BE"),
        (3, "loc_45DC"),
        (4, "loc_45FC"),
        (5, "loc_461B"),
        (6, "loc_4634"),
        (7, "loc_4660"),
        (8, "loc_4680"),
        (9, "loc_469F"),
        (10, "loc_46BF"),
        (SWITCH_DEFAULT, "loc_46EC"),
    )


    label("loc_457D")


    ChrTalk(
        0x102,
        "#00100FYes, all right.\x02",
    )

    CloseMessageWindow()
    Jump("loc_46EC")

    label("loc_459E")


    ChrTalk(
        0x103,
        "#00200FYes, let's go.\x02",
    )

    CloseMessageWindow()
    Jump("loc_46EC")

    label("loc_45BE")


    ChrTalk(
        0x104,
        "#00300FYeah, let's.\x02",
    )

    CloseMessageWindow()
    Jump("loc_46EC")

    label("loc_45DC")


    ChrTalk(
        0x109,
        "#10100FYes, let's go.\x02",
    )

    CloseMessageWindow()
    Jump("loc_46EC")

    label("loc_45FC")


    ChrTalk(
        0x105,
        "#10300FHu hu, roger.\x02",
    )

    CloseMessageWindow()
    Jump("loc_46EC")

    label("loc_461B")


    ChrTalk(
        0x153,
        "#01109FAgreed!\x02",
    )

    CloseMessageWindow()
    Jump("loc_46EC")

    label("loc_4634")


    ChrTalk(
        0x156,
        "#06409FYes! Let's go have a look!\x02",
    )

    CloseMessageWindow()
    Jump("loc_46EC")

    label("loc_4660")


    ChrTalk(
        0x14C,
        "#05900FYes, let's go.\x02",
    )

    CloseMessageWindow()
    Jump("loc_46EC")

    label("loc_4680")


    ChrTalk(
        0x134,
        "#01709FOK, let's go!\x02",
    )

    CloseMessageWindow()
    Jump("loc_46EC")

    label("loc_469F")


    ChrTalk(
        0x135,
        "#01802FYes, let's go.\x02",
    )

    CloseMessageWindow()
    Jump("loc_46EC")

    label("loc_46BF")


    ChrTalk(
        0x166,
        "#14000FHmph, well, I'll tag along.\x02",
    )

    CloseMessageWindow()
    Jump("loc_46EC")

    label("loc_46EC")

    SetChrPos(0x0, 0, -1000, -46000, 0)
    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_17_2820 end

    def Function_18_4702(): pass

    label("Function_18_4702")

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

    def lambda_47BE():
        OP_9B(0x1, 0xFE, 0xFFFA, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_47BE)

    def lambda_47D3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_47D3)
    Sleep(700)

    def lambda_47E7():
        OP_9B(0x1, 0xFE, 0x6, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_47E7)

    def lambda_47FC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xEF, 2, lambda_47FC)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x101, 2)
    WaitChrThread(0xEF, 1)
    WaitChrThread(0xEF, 2)
    Sound(118, 0, 100, 0)
    OP_71(0x4, 0x1E, 0x0, 0x0, 0x8)
    OP_79(0x4)
    SetMapObjFlags(0x4, 0x10)
    OP_6F(0x79)
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4EF3")

    ChrTalk(
        0x101,
        "#00000FThe top floor of "Mirror Castle", eh...?\x02",
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
            "#00005FThat over there must be \x01",
            "the "bell" they talk about.\x02",
        )
    )

    CloseMessageWindow()
    Switch(
        (scpexpr(EXPR_23, 0x5), scpexpr(EXPR_END)),
        (0, "loc_4941"),
        (1, "loc_49B1"),
        (2, "loc_4A25"),
        (3, "loc_4A6B"),
        (4, "loc_4AB0"),
        (5, "loc_4B31"),
        (6, "loc_4BAF"),
        (7, "loc_4BF6"),
        (8, "loc_4C7D"),
        (9, "loc_4CF2"),
        (10, "loc_4D73"),
        (SWITCH_DEFAULT, "loc_4DE9"),
    )


    label("loc_4941")


    ChrTalk(
        0x102,
        (
            "#00100FThere're ringing cords\x01",
            "on both sides of it.\x02\x03",
            "#00104FNo doubt it's the one\x01",
            "I've heard about.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_4DE9")

    label("loc_49B1")


    ChrTalk(
        0x103,
        (
            "#00200FThere are ringing cords\x01",
            "on both sides of it.\x02\x03",
            "#00204FNo doubt it is the one\x01",
            "I have heard about.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_4DE9")

    label("loc_4A25")


    ChrTalk(
        0x104,
        (
            "#00300FYeah, there're ringin' cords\x01",
            "on both sides of it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_4DE9")

    label("loc_4A6B")


    ChrTalk(
        0x109,
        (
            "#10100FYes, there're ringing cords\x01",
            "on both sides of it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_4DE9")

    label("loc_4AB0")


    ChrTalk(
        0x105,
        (
            "#10300FThere're ringing cords\x01",
            "on both sides of it.\x02\x03",
            "#10304FIt seems there's no doubt it's\x01",
            "the one I've heard about.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_4DE9")

    label("loc_4B31")


    ChrTalk(
        0x153,
        (
            "#01105FThere're ringing cords\x01",
            "on either side of it, hm?\x02\x03",
            "#01111FI wonder if they're what\x01",
            "Elie was talking about.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_4DE9")

    label("loc_4BAF")


    ChrTalk(
        0x156,
        (
            "#06400FYes, there're ringing cords\x01",
            "on both sides of it...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_4DE9")

    label("loc_4BF6")


    ChrTalk(
        0x14C,
        (
            "#05900FThere are ringing cords\x01",
            "on both sides of it.\x02\x03",
            "#05904FI believe there is no doubt it is\x01",
            "the one I have heard about.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_4DE9")

    label("loc_4C7D")


    ChrTalk(
        0x134,
        (
            "#01700FThere are ringing cords\x01",
            "on both sides of it.\x02\x03",
            "#01704FNo doubt it's the one\x01",
            "I've heard about, eh?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_4DE9")

    label("loc_4CF2")


    ChrTalk(
        0x135,
        (
            "#01802FThere're ringing cords\x01",
            "on both sides of it.\x02\x03",
            "#01804FIt seems there's no doubt it's\x01",
            "the one I've heard about.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_4DE9")

    label("loc_4D73")


    ChrTalk(
        0x166,
        (
            "#14000FThere's ringing cords\x01",
            "on both sides of it...\x02\x03",
            "#14003FNo doubt it's the one\x01",
            "I've heard about, huh?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_4DE9")

    label("loc_4DE9")


    def lambda_4DEE():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4DEE)
    Sleep(50)

    def lambda_4DFE():
        OP_93(0xEF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_4DFE)
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
            "#00002FIn that case, that huge mirror\x01",
            "is the "Wish-Granting Mirror"?\x02",
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

    def lambda_4ECB():
        OP_93(0x101, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4ECB)
    Sleep(50)

    def lambda_4EDB():
        OP_93(0xEF, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_4EDB)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0xEF, 0)
    Jump("loc_4F24")

    label("loc_4EF3")


    ChrTalk(
        0x101,
        "#00000F*phew*, we've reached the top floor.\x02",
    )

    CloseMessageWindow()

    label("loc_4F24")

    Switch(
        (scpexpr(EXPR_23, 0x5), scpexpr(EXPR_END)),
        (0, "loc_4F6F"),
        (1, "loc_500E"),
        (2, "loc_50B1"),
        (3, "loc_5145"),
        (4, "loc_51D0"),
        (5, "loc_5266"),
        (6, "loc_52EC"),
        (7, "loc_5376"),
        (8, "loc_5414"),
        (9, "loc_54AE"),
        (10, "loc_5542"),
        (SWITCH_DEFAULT, "loc_55D0"),
    )


    label("loc_4F6F")


    ChrTalk(
        0x102,
        (
            "#00100FIf you ring the bell and stand in front of\x01",
            "the mirror, they say it grants your wish...\x02\x03",
            "#00104FNow that I'm here though,\x01",
            "I'm nervous somehow.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_55D0")

    label("loc_500E")


    ChrTalk(
        0x103,
        (
            "#00200FIf you ring the bell and stand in front of\x01",
            "the mirror, it seems it grants your wish...\x02\x03",
            "#00204FNow that I am here though,\x01",
            "I feel nervous somehow.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_55D0")

    label("loc_50B1")


    ChrTalk(
        0x104,
        (
            "#00300FIf you ring the bell and stand in front of\x01",
            "the mirror, it's said it grants your wish...\x02\x03",
            "#00304FWell then, what should I wish for?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_55D0")

    label("loc_5145")


    ChrTalk(
        0x109,
        (
            "#10100FIf you ring the bell and stand in front of\x01",
            "the mirror, it's said to grant your wish...\x02\x03",
            "#10104FHmm, what could I ask for?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_55D0")

    label("loc_51D0")


    ChrTalk(
        0x105,
        (
            "#10300FIf you ring the bell and stand in front of\x01",
            "the mirror, it seems it grants your wish...\x02\x03",
            "#10304FI wonder what will happen in the end.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_55D0")

    label("loc_5266")


    ChrTalk(
        0x153,
        (
            "#01100FIf you ring the bell and stand in front of\x01",
            "the mirror, it grants your wish, right?\x02\x03",
            "#01109FWhat should KeA wish for?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_55D0")

    label("loc_52EC")


    ChrTalk(
        0x156,
        (
            "#06400FIf you ring the bell and stand in front of\x01",
            "the mirror, they say it grants your wish, eh?\x02\x03",
            "#06409FWhat should I wish for?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_55D0")

    label("loc_5376")


    ChrTalk(
        0x14C,
        (
            "#05900FIf you ring the bell and stand in front of\x01",
            "the mirror, they say it grants your wish, but...\x02\x03",
            "#05904FUh uh, what should I wish for, I wonder?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_55D0")

    label("loc_5414")


    ChrTalk(
        0x134,
        (
            "#01700FIf you ring the bell and stand in front of\x01",
            "the mirror, they say it grants your wish, hm?\x02\x03",
            "#01702FUh uh, I wonder what should I wish for?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_55D0")

    label("loc_54AE")


    ChrTalk(
        0x135,
        (
            "#01803FIf you ring the bell and stand in front of\x01",
            "the mirror, it is said to grant your wish?\x02\x03",
            "#01808F(However...to wish for something...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_55D0")

    label("loc_5542")


    ChrTalk(
        0x166,
        (
            "#14003FIf you ring the bell and stand in front of\x01",
            "the mirror, they say it grants your wish...eh?\x02\x03",
            "#14008F...Who knows if it's true.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_55D0")

    label("loc_55D0")

    Jc((scpexpr(EXPR_23, 0x5), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5622")

    ChrTalk(
        0x101,
        (
            "#00000FAlright then, let's try\x01",
            "ringing the bell together.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5661")

    label("loc_5622")


    ChrTalk(
        0x101,
        (
            "#00000FAlright then, let's try\x01",
            "ringing the bell together.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5661")

    OP_D2(0x4, (scpexpr(EXPR_PUSH_LONG, 0x40000000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    SetChrPos(0x0, 0, 40550, -15500, 180)
    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_18_4702 end

    def Function_19_5680(): pass

    label("Function_19_5680")

    TalkBegin(0xFF)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Ring the Bell\x01",      # 0
            "Quit\x01",               # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Sleep(200)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_56BF")
    Call(0, 20)
    Jump("loc_56BF")

    label("loc_56BF")

    TalkEnd(0xFF)
    Return()

    # Function_19_5680 end

    def Function_20_56C3(): pass

    label("Function_20_56C3")

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
            "#00000F#6P...Alright. Next, let's go in front\x01",
            "of the "mirror" upstairs.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xEF, 0x101, 500)
    Switch(
        (scpexpr(EXPR_23, 0x5), scpexpr(EXPR_END)),
        (0, "loc_57E4"),
        (1, "loc_5807"),
        (2, "loc_582A"),
        (3, "loc_584E"),
        (4, "loc_5875"),
        (5, "loc_5899"),
        (6, "loc_58BF"),
        (7, "loc_58E8"),
        (8, "loc_591F"),
        (9, "loc_5942"),
        (10, "loc_5968"),
        (SWITCH_DEFAULT, "loc_599B"),
    )


    label("loc_57E4")


    ChrTalk(
        0x102,
        "#00100FYes, let's go.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_599B")

    label("loc_5807")


    ChrTalk(
        0x103,
        "#00200FYes, let's go.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_599B")

    label("loc_582A")


    ChrTalk(
        0x104,
        "#00300FHa ha, finally.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_599B")

    label("loc_584E")


    ChrTalk(
        0x109,
        "#10100FIt's finally time.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_599B")

    label("loc_5875")


    ChrTalk(
        0x105,
        "#10300FHu hu, at last.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_599B")

    label("loc_5899")


    ChrTalk(
        0x153,
        "#01109FYeah, let's gooo!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_599B")

    label("loc_58BF")


    ChrTalk(
        0x156,
        "#06400FUh uh, I can't wait!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_599B")

    label("loc_58E8")


    ChrTalk(
        0x14C,
        "#05900FUh uh, what will happen, I wonder?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_599B")

    label("loc_591F")


    ChrTalk(
        0x134,
        "#01700FYes, let's go.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_599B")

    label("loc_5942")


    ChrTalk(
        0x135,
        "#01802F...Yes, let's go.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_599B")

    label("loc_5968")


    ChrTalk(
        0x166,
        "#14000F...Hmph, let's go have a look.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_599B")

    label("loc_599B")

    OP_D2(0x4, (scpexpr(EXPR_PUSH_LONG, 0x80000000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    OP_65(0x3, 0x1)
    OP_65(0x4, 0x1)
    SetScenarioFlags(0x0, 0)
    OP_1B(0xC, 0x0, 0x2A)
    SetChrPos(0x0, -7700, 40550, -25000, 315)
    EventEnd(0x5)
    Return()

    # Function_20_56C3 end

    def Function_21_59C8(): pass

    label("Function_21_59C8")

    Sound(918, 0, 100, 0)
    Sleep(2000)
    Sound(918, 0, 80, 0)
    Sleep(2000)
    Sound(918, 0, 60, 0)

    label("loc_59E0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_59F9")
    Sleep(2000)
    Sound(918, 0, 40, 0)
    Jump("loc_59E0")

    label("loc_59F9")

    Return()

    # Function_21_59C8 end

    def Function_22_59FA(): pass

    label("Function_22_59FA")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x80000000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5A51")

    ChrTalk(
        0x101,
        (
            "#00000FOh...\x01",
            "First, we must ring the bell downstairs.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5B06")

    label("loc_5A51")

    Switch(
        (scpexpr(EXPR_23, 0x5), scpexpr(EXPR_END)),
        (0, "loc_5A9C"),
        (1, "loc_5AA4"),
        (2, "loc_5AAC"),
        (3, "loc_5AB4"),
        (4, "loc_5ABC"),
        (5, "loc_5AC4"),
        (6, "loc_5ACC"),
        (7, "loc_5AD4"),
        (8, "loc_5ADC"),
        (9, "loc_5AE4"),
        (10, "loc_5AEC"),
        (SWITCH_DEFAULT, "loc_5AF4"),
    )


    label("loc_5A9C")

    Call(0, 28)
    Jump("loc_5AF4")

    label("loc_5AA4")

    Call(0, 29)
    Jump("loc_5AF4")

    label("loc_5AAC")

    Call(0, 30)
    Jump("loc_5AF4")

    label("loc_5AB4")

    Call(0, 32)
    Jump("loc_5AF4")

    label("loc_5ABC")

    Call(0, 33)
    Jump("loc_5AF4")

    label("loc_5AC4")

    Call(0, 34)
    Jump("loc_5AF4")

    label("loc_5ACC")

    Call(0, 36)
    Jump("loc_5AF4")

    label("loc_5AD4")

    Call(0, 37)
    Jump("loc_5AF4")

    label("loc_5ADC")

    Call(0, 38)
    Jump("loc_5AF4")

    label("loc_5AE4")

    Call(0, 39)
    Jump("loc_5AF4")

    label("loc_5AEC")

    Call(0, 40)
    Jump("loc_5AF4")

    label("loc_5AF4")

    StopBGM(0xFA0)
    WaitBGM()
    SetScenarioFlags(0x22, 1)
    NewScene("t1400", 0, 0, 0)
    IdleLoop()

    label("loc_5B06")

    TalkEnd(0xFF)
    Return()

    # Function_22_59FA end

    def Function_23_5B0A(): pass

    label("Function_23_5B0A")

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

    # Function_23_5B0A end

    def Function_24_5B74(): pass

    label("Function_24_5B74")

    Fade(800)
    EndChrThread(0xC, 0x1)
    SetMapObjFrame(0xFF, "Null_bell", 0x2, "stop")
    OP_0D()
    Sleep(2500)
    Return()

    # Function_24_5B74 end

    def Function_25_5B94(): pass

    label("Function_25_5B94")


    def lambda_5B99():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5B99)
    OP_93(0xFE, 0x10E, 0x1F4)
    WaitChrThread(0x101, 2)
    Return()

    # Function_25_5B94 end

    def Function_26_5BAD(): pass

    label("Function_26_5BAD")


    def lambda_5BB2():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5BB2)
    OP_93(0xFE, 0x0, 0x1F4)
    WaitChrThread(0x101, 2)
    Return()

    # Function_26_5BAD end

    def Function_27_5BC6(): pass

    label("Function_27_5BC6")

    SetCameraDistance(14700, 3000)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Jc((scpexpr(EXPR_23, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5C06")
    OP_63(0xFE, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_5C18")

    label("loc_5C06")

    OP_63(0xFE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_5C18")

    Sleep(2500)
    OP_64(0x101)
    OP_64(0xFE)
    OP_6F(0x79)
    Return()

    # Function_27_5BC6 end

    def Function_28_5C24(): pass

    label("Function_28_5C24")

    EventBegin(0x0)
    Call(0, 23)
    BeginChrThread(0x102, 3, 0, 25)
    WaitChrThread(0x102, 3)
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5D2C")

    ChrTalk(
        0x101,
        (
            "#00000FAlright, let's try to\x01",
            "make a wish now.\x02\x03",
            "#00005FUhhm...will it be okay saying my\x01",
            "wish in front of this mirror?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FI think that maybe it's just fine\x01",
            "thinking about the wish in your head.\x02\x03",
            "Then, let's try.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5DB0")

    label("loc_5D2C")


    ChrTalk(
        0x101,
        (
            "#00000FIt seems that what remains to do is to have\x01",
            "come to mind a wish in front of this mirror.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FYes, let's try it.\x02",
    )

    CloseMessageWindow()

    label("loc_5DB0")

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
        "#00000F...I wonder if this is enough?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104FYes, I finished too.\x02\x03",
            "#00100FBy the way...\x01",
            "What did you wish for, Lloyd?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5FF8")

    ChrTalk(
        0x101,
        (
            "#00000FHa ha, well I'm a little embarrassed \x01",
            "because it's so normal.\x02\x03",
            "#00004F"That I can keep protecting\x01",
            "Crossbell from now on too", I guess.\x02\x03",
            "#00000FOf course, with KeA, Elie and the other\x01",
            "members of the Support Section too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100F*giggle*, it's typical of you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHa ha, thanks.\x02\x03",
            "#00000FSo, what did you\x01",
            "wish for, Elie?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_611A")

    label("loc_5FF8")


    ChrTalk(
        0x101,
        (
            "#00000FI already wished for my top\x01",
            "thing when I first came here.\x02\x03",
            "#00004FWishing for the same thing\x01",
            "wouldn't be nice, so I wished\x01",
            "for your wish to come true, Elie.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100F*giggle*, typical of you, Lloyd.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHa ha, you're welcome.\x02\x03",
            "#00000FSo, what did you\x01",
            "wish for, Elie?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_611A")

    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x102)

    ChrTalk(
        0x102,
        (
            "#00103FThat... My dad and mom\x01",
            "live happily, I guess.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005FIt was for your parents...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F...*giggle*, I told you about them before, right?\x01",
            "They divorced ten years ago and one is living\x01",
            "in the Republic, the other in the Empire.\x02\x03",
            "#00104FEven now we stay in contact with\x01",
            "letters and orbal phone calls,\x01",
            "but I hardly see their faces.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008F...It must be sad, as I thought.\x02\x03",
            "#00003FI lost my parents when I was little,\x01",
            "but thanks to my big brother and sister\x01",
            "Cecil I didn't feel that much sad...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F*giggle*, I had grandfather\x01",
            "by my side, so I wasn't sad.\x01\x02\x03",
            "#00103F...If pushed, I'd say that...\x01",
            "Maybe it's correct to say I was worried.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FWorried...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FEvery now and then dad and mom contact\x01",
            "me worried about my condition, but...\x02\x03",
            "#00108FIf that is because they still regret\x01",
            "to have left me behind, well, I think\x01",
            "it's a very painful thing.\x02\x03",
            "Those two are very serious persons.\x01",
            "They're the type who can't go on\x01",
            "living forgetting the past at all.\x02\x03",
            "#00104FTen years have passed since then,\x01",
            "so I wished it's time for them to walk\x01",
            "a new road in life and be happy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008FForgetting the past, a new life...?\x02\x03",
            "#00001FBut, you can't say that's a\x01",
            "right thing as a rule, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FYes...I know.\x01",
            "Because there was a past,\x01",
            "there's a me now.\x02\x03",
            "#00104FBut, I wish for dad and mom\x01",
            "to be happy, in whatever\x01",
            "way they can...\x02\x03",
            "#00100F...*giggle*, I'm sorry.\x01",
            "I said something weird.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FNo...you haven't.\x02\x03",
            "#00000FYour parents' happiness...\x01",
            "I'll pray for that too.\x02",
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

    # Function_28_5C24 end

    def Function_29_675D(): pass

    label("Function_29_675D")

    EventBegin(0x0)
    Call(0, 23)
    BeginChrThread(0x103, 3, 0, 25)
    WaitChrThread(0x103, 3)
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6866")

    ChrTalk(
        0x101,
        (
            "#00000FAlright, let's try to\x01",
            "make a wish now.\x02\x03",
            "#00005FUhhm...will it be okay saying my\x01",
            "wish in front of this mirror?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FI think that maybe it is just fine\x01",
            "thinking about the wish in your head.\x02\x03",
            "Then, let's try.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_68E7")

    label("loc_6866")


    ChrTalk(
        0x101,
        (
            "#00000FIt seems that what remains to do is to have\x01",
            "come to mind a wish in front of this mirror.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00200FYes, let's try.\x02",
    )

    CloseMessageWindow()

    label("loc_68E7")

    BeginChrThread(0x103, 3, 0, 26)
    WaitChrThread(0x103, 3)

    ChrTalk(
        0x101,
        "#00003F............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00203F............\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x103, 3, 0, 27)
    WaitChrThread(0x103, 3)
    Call(0, 24)
    BeginChrThread(0x103, 3, 0, 25)
    WaitChrThread(0x103, 3)

    ChrTalk(
        0x101,
        "#00000F...I wonder if this is enough?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00204F...Yes, I finished too.\x02\x03",
            "#00200FI would like to ask just for reference...\x01",
            "What did you wish for, Mr. Lloyd?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6B49")

    ChrTalk(
        0x101,
        (
            "#00000FHa ha, well I'm a little embarrassed \x01",
            "because it's so normal.\x02\x03",
            "#00004F"That I can keep protecting\x01",
            "Crossbell from now on too", I guess.\x02\x03",
            "#00000FOf course, with KeA, Tio and the other\x01",
            "members of the Support Section too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FI see...\x01",
            "Typical of Mr. Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHa ha, thanks.\x02\x03",
            "#00000FSo Tio, what\x01",
            "did you wish for?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6C65")

    label("loc_6B49")


    ChrTalk(
        0x101,
        (
            "#00000FI already wished for my top\x01",
            "thing when I first came here.\x02\x03",
            "#00004FWishing for the same thing\x01",
            "wouldn't be nice, so I wished\x01",
            "for your wish to come true, Tio.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FI see...\x01",
            "Thank you very much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHa ha, you're welcome.\x02\x03",
            "#00000FSo Tio, what\x01",
            "did you wish for?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6C65")


    ChrTalk(
        0x103,
        (
            "#00203F...That Chief Roberts annoyingness\x01",
            "becomes a little less objectionable.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00012FP-Poor him...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00202F...I am joking.\x02\x03",
            "#00203FActually...\x01",
            "I wished to find a\x01",
            "meaning to live.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x103,
        (
            "#00200FI spoke about this to you and\x01",
            "the others before, Mr. Lloyd.\x02\x03",
            "#00203FThree years ago, the answer to the question I\x01",
            "couldn't hear that I wanted to ask to Mr. Guy...\x02\x03",
            "#00208FI still haven't found it even now\x01",
            "that I overcame the Cult incident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F...Tio, I told you, right?\x01",
            "You won't find often people\x01",
            "who know such a thing.\x02\x03",
            "#00000FThere's no need to be impatient to find the\x01",
            "answer, not even the need to find it by yourself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00204FYes, naturally I know that.\x02\x03",
            "#00200FI am not impatient and I know\x01",
            "that everyone can help me.\x01\x02\x03",
            "#00203FBut, it is a question that can be said\x01",
            "to be the issue in my own life.\x02\x03",
            "#00200FThat is why one day I will find the answer \x01",
            "for sure. ...I wished to the "mirror" with\x01",
            "that declaration of intent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F...Ha ha, is that so?\x01",
            "Sorry, it seems I was worrying unnecessarily.\x02\x03",
            "#00004FBeing that the case, I guess\x01",
            "I'll express my will once again.\x02\x03",
            "#00000FThat you may one day\x01",
            "find the answer, Tio...\x01",
            "We'll help you out too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00209FUh uh...\x01",
            "I will count on you.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_29_675D end

    def Function_30_7166(): pass

    label("Function_30_7166")

    EventBegin(0x0)
    Call(0, 23)
    BeginChrThread(0x104, 3, 0, 25)
    WaitChrThread(0x104, 3)
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7272")

    ChrTalk(
        0x101,
        (
            "#00000FAlright, let's try to\x01",
            "make a wish now.\x02\x03",
            "#00005FUhhm...will it be okay saying my\x01",
            "wish in front of this mirror?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FI guess that maybe it's just fine\x01",
            "thinkin' about the wish in your head.\x02\x03",
            "Then, let's do this.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_72F8")

    label("loc_7272")


    ChrTalk(
        0x101,
        (
            "#00000FIt seems that what remains to do is to have\x01",
            "come to mind a wish in front of this mirror.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00300FThen, let's do this.\x02",
    )

    CloseMessageWindow()

    label("loc_72F8")

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
        "#00000F...I wonder if this is enough?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00304FHm, I'm done too.\x02\x03",
            "#00309FSo, Lloyd.\x01",
            "What stuff did you wish for?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_75AD")

    ChrTalk(
        0x101,
        (
            "#00000FHa ha, well I'm a little embarrassed\x01",
            "because it's so normal.\x02\x03",
            "#00004FThat I can keep protecting\x01",
            "Crossbell from now on too, I guess.\x02\x03",
            "#00000FOf course, with KeA, Randy and the other\x01",
            "members of the Support Section too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FHa ha, really,\x01",
            "you're a serious guy.\x02\x03",
            "#00306FYou wouldn't have been punished\x01",
            "if you had wished for something a\x01",
            "little more geared towards yourself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FS-Speaking of that, what\x01",
            "kind of thing did you wish for?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_76F5")

    label("loc_75AD")


    ChrTalk(
        0x101,
        (
            "#00000FI already wished for my top\x01",
            "thing when I first came here.\x02\x03",
            "#00004FWishing for the same thing\x01",
            "wouldn't be nice, so I wished\x01",
            "for your wish to come true, Randy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00305FOoh, you serious!?\x02\x03",
            "#00309FMan, that's Lloyd for you,\x01",
            "Great timing!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00005FH-Huh... Randy, what\x01",
            "did you wish for?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_76F5")


    ChrTalk(
        0x104,
        (
            "#00304FMe? But of course, \x01",
            "for a very merry harem\x01",
            "of babes in Crossbell──\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F──I've got it, stop now.\x01",
            "I was an idiot for asking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00305FHey now, it's something\x01",
            "every man would desire, no?\x02\x03",
            "#00304FMiss Cecil and the others,\x01",
            "the nurses, Miss Eolia the Bracer...\x02\x03",
            "#00309FThere're many girls who\x01",
            "suit my tastes in Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FListen now... Don't have sister Cecil\x01",
            "participate in such a delusion, ok?\x02\x03",
            "#00002F...Well, in a certain sense though, I'm relieved.\x01",
            "Since it's a wish that will never come true.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x104,
        (
            "#00306FL-Listen to you sayin'\x01",
            "something so frankly...\x02\x03",
            "#00300F...Hahaan, could\x01",
            "you be jealous?\x02\x03",
            "#00304FStay assured; in the\x01",
            "even it comes true,\x01",
            "I'll let you have some good...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00011FW-When and who'd ever be\x01",
            "so worried about that!?\x02\x03",
            "#00006F...*haah*, honestly.\x01",
            "We did our wishes, let's go now.\x02",
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
            "#00308F(A wish there's no way it'll come true, huh...?)\x02\x03",
            "#00303F(That we can stay comrades like this, forever...\x01",
            "That would've been too much for me to ask.)\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_93(0x104, 0xE1, 0x1F4)
    OP_9B(0x0, 0x104, 0x0, 0x7D0, 0x7D0, 0x0)
    OP_0D()
    Return()

    # Function_30_7166 end

    def Function_31_7B41(): pass

    label("Function_31_7B41")

    OP_93(0xFE, 0xE1, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
    Return()

    # Function_31_7B41 end

    def Function_32_7B58(): pass

    label("Function_32_7B58")

    EventBegin(0x0)
    Call(0, 23)
    BeginChrThread(0x109, 3, 0, 25)
    WaitChrThread(0x109, 3)
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7C60")

    ChrTalk(
        0x101,
        (
            "#00000FAlright, let's try to\x01",
            "make a wish now.\x02\x03",
            "#00005FUhhm...will it be okay saying my\x01",
            "wish in front of this mirror?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FI think that maybe it's just fine\x01",
            "thinking about the wish in your head.\x02\x03",
            "Then, let's try.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7CE9")

    label("loc_7C60")


    ChrTalk(
        0x101,
        (
            "#00000FAlright, let's wish\x01",
            "for something.\x02\x03",
            "Just stand in front of the\x01",
            "mirror and think of your wish.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10100FYes, let's try it.\x02",
    )

    CloseMessageWindow()

    label("loc_7CE9")

    BeginChrThread(0x109, 3, 0, 26)
    WaitChrThread(0x109, 3)

    ChrTalk(
        0x101,
        "#00003F............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10103F............\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x109, 3, 0, 27)
    WaitChrThread(0x109, 3)
    Call(0, 24)
    BeginChrThread(0x109, 3, 0, 25)
    WaitChrThread(0x109, 3)

    ChrTalk(
        0x101,
        "#00000F...I wonder if this is enough?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10104FYes, I finished too.\x02\x03",
            "#10100F...Umm, what did you\x01",
            "wish for, Mr. Lloyd?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7F1D")

    ChrTalk(
        0x101,
        (
            "#00000FHa ha, well I'm a little embarrassed\x01",
            "because it's so normal.\x02\x03",
            "#00004FThat I can keep protecting\x01",
            "Crossbell from now on too, I guess.\x02\x03",
            "#00000FOf course, with KeA, Noｱl and the other\x01",
            "members of the Support Section too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10100FI see, typical of Mr. Lloyd.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHa ha, thanks.\x02\x03",
            "So, what did you\x01",
            "wish for, Noｱl?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_803B")

    label("loc_7F1D")


    ChrTalk(
        0x101,
        (
            "#00000FI already wished for my top\x01",
            "thing when I first came here.\x02\x03",
            "#00004FWishing for the same thing\x01",
            "wouldn't be nice, so I wished\x01",
            "for your wish to come true, Noｱl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FAhaha... \x01",
            "Thank you so much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHa ha, you're welcome.\x02\x03",
            "#00000FSo, what did you\x01",
            "wish for, Noｱl?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_803B")


    ChrTalk(
        0x109,
        (
            "#10100FMine's simple. \x01",
            ""To be a wonderful\x01",
            "CGF member."\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHa ha... A direct wish.\x01",
            "That's just like you, Noｱl.\x02\x03",
            "#00000FYou must be aiming to be as\x01",
            "great as your father, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FAhaha... I said it before, but I'm \x01",
            "not so self-conscious about that.\x02\x03",
            "#10104FI was a kid too, once,\x01",
            "and I almost hated\x01",
            "my strict dad.\x02",
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
            "#10102FYeah, he was really strict.\x02\x03",
            "#10104FIf Fran or I ever did mischiefs, he'd\x01",
            "beat us without mercy with punches\x01",
            "that would've made a man flying...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x109,
        (
            "#10103FBut I remember my mom took\x01",
            "us to a border gate once so we\x01",
            "could see my dad working.\x02\x03",
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
            "#10103FBut for the life of me,\x01",
            "I can't understand why Fran has\x01",
            "such a cheerful personality.\x02\x03",
            "#10101F...Could it be\x01",
            "that dad only\x01",
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
            "#00012FWell, it's possible that it was\x01",
            "a reaction to the strictness too.\x02\x03",
            "#00000FWell then, we made our wishes. \x01",
            "We should be going.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10100FYes, we should.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_32_7B58 end

    def Function_33_856D(): pass

    label("Function_33_856D")

    EventBegin(0x0)
    Call(0, 23)
    BeginChrThread(0x105, 3, 0, 25)
    WaitChrThread(0x105, 3)
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8676")

    ChrTalk(
        0x101,
        (
            "#00000FAlright, let's try to\x01",
            "make a wish now.\x02\x03",
            "#00005FUhhm...will it be okay saying my\x01",
            "wish in front of this mirror?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FI think that maybe it's just\x01",
            "fine thinking about the \x01",
            "wish in your head?\x02\x03",
            "Then, let's try.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_870C")

    label("loc_8676")


    ChrTalk(
        0x101,
        (
            "#00000FThen, let's try\x01",
            "making a wish.\x02\x03",
            "#00004FIt should be all right thinking about\x01",
            "a wish in front of this mirror.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10300FThen, let's try.\x02",
    )

    CloseMessageWindow()

    label("loc_870C")

    BeginChrThread(0x105, 3, 0, 26)
    WaitChrThread(0x105, 3)

    ChrTalk(
        0x101,
        "#00003F............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10303F............\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x105, 3, 0, 27)
    WaitChrThread(0x105, 3)
    Call(0, 24)
    BeginChrThread(0x105, 3, 0, 25)
    WaitChrThread(0x105, 3)

    ChrTalk(
        0x101,
        "#00000F...I wonder if this is enough?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FI've finished too.\x02\x03",
            "#10300FSo, what did\x01",
            "you wish for?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8930")

    ChrTalk(
        0x101,
        (
            "#00000FHa ha, well I'm a little embarrassed\x01",
            "because it's so normal.\x02\x03",
            "#00004FThat I can keep protecting\x01",
            "Crossbell from now on too, I guess.\x02\x03",
            "#00000FOf course, with KeA, Wazy and the other\x01",
            "members of the Support Section too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10300FHu hu, typical of you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHa ha, thanks.\x02\x03",
            "#00000FSo, what did you\x01",
            "wish for, Wazy?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8A54")

    label("loc_8930")


    ChrTalk(
        0x101,
        (
            "#00000FI already wished for my top\x01",
            "thing when I first came here.\x02\x03",
            "#00004FWishing for the same thing\x01",
            "wouldn't be nice, so I wished\x01",
            "for your wish to come true, Wazy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FHu hu, you really\x01",
            "are softhearted.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHa ha, you're welcome.\x02\x03",
            "#00000FSo, what did you\x01",
            "wish for, Wazy?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8A54")


    ChrTalk(
        0x105,
        (
            "#10302FHu hu, so to speak...\x02\x03",
            "#10304FThat my former brawling enemy\x01",
            "will be able to find his own way.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00008F...I've heard the rumors, but...\x01",
            "It seems that recently Wald didn't\x01",
            "even show up at his base.\x02\x03",
            "#00003FBut it's not your fault at all...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10309FInfact, I'm not sentimental\x01",
            "to feel to be responsible.\x02\x03",
            "#10300FAfter the duel on that rainy day,\x01",
            "I anticipated to some extent that he\x01",
            "would've felt depressed and despaired.\x02\x03",
            "#10304FContinuing to feel depressed or\x01",
            "moving forward getting over everything...\x01",
            "In the end, that's Wald's own problem.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00006FThat's a...hmm...cool point of view...\x02\x03",
            "#00000FBut, if you really think that,\x01",
            "you wouldn't wish for him to\x01",
            ""find his own way", right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FHu hu, you're quite right, however...\x01",
            "This wish is also for my own sake.\x02\x03",
            "#10300FIf he will continue to feel depressed...\x01",
            "Then it would mean that I didn't teach\x01",
            "him anything I wanted to with that duel.\x02\x03",
            "#10303FThe only truth would be that I couldn't\x01",
            "settle things once and for all...\x02\x03",
            "#10309FWouldn't that be really lame?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F...*haah*, oh man.\x01",
            "You aren't honest with yourself.\x02\x03",
            "#00000FBut, I too will greatly wish that\x01",
            "Wald, the others and the Vipers...\x01",
            "Can find their path.\x02\x03",
            "I truly hope that wish will come true.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303FHu hu, you really are softhearted.\x02\x03",
            "#10309FI quite love that side of you.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00006FOh, jeez, I did so much to\x01",
            "wrap it up nicely and yet...\x01",
            "Don't make fun of me!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_33_856D end

    def Function_34_9035(): pass

    label("Function_34_9035")

    EventBegin(0x0)
    Call(0, 23)
    BeginChrThread(0x153, 3, 0, 25)
    WaitChrThread(0x153, 3)
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9126")

    ChrTalk(
        0x101,
        (
            "#00000FAlright, let's try to\x01",
            "make a wish now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#01100FShould we say it in\x01",
            "front of this mirror?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FI think it's fine if you\x01",
            "just think of your wish.\x02\x03",
            "...Alright. Let's give it a try.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_91B3")

    label("loc_9126")


    ChrTalk(
        0x101,
        (
            "#00000FThen, let's try\x01",
            "making a wish.\x02\x03",
            "#00004FIt should be all right thinking about\x01",
            "a wish in front of this mirror.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#01100FGot it.\x02",
    )

    CloseMessageWindow()

    label("loc_91B3")

    BeginChrThread(0x153, 3, 0, 26)
    WaitChrThread(0x153, 3)

    ChrTalk(
        0x101,
        "#00003F..................\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#01103F...Mmm.........\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x153, 3, 0, 27)
    WaitChrThread(0x153, 3)
    Call(0, 24)
    BeginChrThread(0x153, 3, 0, 25)
    WaitChrThread(0x153, 3)

    ChrTalk(
        0x101,
        "#00000F...I wonder if this is enough?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#01109FYep, KeA's done too.\x02\x03",
            "#01105FHey Lloyd. What\x01",
            "did you wish for?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_93FA")

    ChrTalk(
        0x101,
        (
            "#00000FHa ha, well I'm a little embarrassed\x01",
            "because it's so normal.\x02\x03",
            "#00004FThat I can keep protecting\x01",
            "Crossbell from now on too, I guess.\x02\x03",
            "#00000FOf course, with KeA, and all the other\x01",
            "members of the Support Section too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#01109FEhehe... That sounds like you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHa ha, thanks.\x02\x03",
            "#00000FHow about you, KeA?\x01",
            "What did you wish for?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9505")

    label("loc_93FA")


    ChrTalk(
        0x101,
        (
            "#00000FI already wished for my top\x01",
            "thing when I first came here.\x02\x03",
            "#00004FWishing for the same thing\x01",
            "wouldn't be nice, so I wished\x01",
            "for your wish to come true, KeA.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#01109FEhehe...thanks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHa ha, you're welcome.\x02\x03",
            "#00000FWhat did you\x01",
            "wish for, KeA?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9505")


    ChrTalk(
        0x153,
        (
            "#01106FUmm, there were a lot of things\x01",
            "I wanted to wish for, but...\x02\x03",
            "#01100FThe most important is "for\x01",
            "Shizuku's eyes to get better."\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00003F...Yeah. I hope they really do.\x02\x03",
            "#00008FShizuku's eye surgery looks\x01",
            "quite difficult, though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#01111FBut, wishes made before this\x01",
            "mirror will come true, right?\x02\x03",
            "#01101FIf so, KeA will wish as\x01",
            "many times as it takes!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FHa ha... Yeah,\x01",
            "I'll do the same.\x02\x03",
            "#00004F(I hope a miracle\x01",
            "really does happen.)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x153, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x153, 0x0, 0x1F4)

    ChrTalk(
        0x153,
        "#01111F......?\x02",
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
            "#00009FHa ha... She's a\x01",
            "bundle of energy.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_34_9035 end

    def Function_35_9812(): pass

    label("Function_35_9812")

    OP_93(0xFE, 0x87, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x1F40, 0xFA0, 0x0)
    Return()

    # Function_35_9812 end

    def Function_36_9829(): pass

    label("Function_36_9829")

    EventBegin(0x0)
    Call(0, 23)
    BeginChrThread(0x156, 3, 0, 25)
    WaitChrThread(0x156, 3)
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9932")

    ChrTalk(
        0x101,
        (
            "#00000FAlright, let's try to\x01",
            "make a wish now.\x02\x03",
            "#00005FUhhm...will it be okay saying my\x01",
            "wish in front of this mirror?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x156,
        (
            "#06400FI think that maybe it's just\x01",
            "fine thinking about the \x01",
            "wish in your head.\x02\x03",
            "Then, let's try!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_99C8")

    label("loc_9932")


    ChrTalk(
        0x101,
        (
            "#00000FThen, let's try\x01",
            "making a wish.\x02\x03",
            "#00004FIt should be all right thinking about\x01",
            "a wish in front of this mirror.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x156,
        "#06400FThen, let's try!\x02",
    )

    CloseMessageWindow()

    label("loc_99C8")

    BeginChrThread(0x156, 3, 0, 26)
    WaitChrThread(0x156, 3)

    ChrTalk(
        0x101,
        "#00003F............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x156,
        "#06403F............\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x156, 3, 0, 27)
    WaitChrThread(0x156, 3)
    Call(0, 24)
    BeginChrThread(0x156, 3, 0, 25)
    WaitChrThread(0x156, 3)

    ChrTalk(
        0x101,
        "#00000F...I wonder if this is enough?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x156,
        (
            "#06400FYes, I have wished too.\x02\x03",
            "#06409FIncidentally, what did you\x01",
            "wish for, Mr. Lloyd?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9C08")

    ChrTalk(
        0x101,
        (
            "#00000FHa ha, well I'm a little embarrassed\x01",
            "because it's so normal.\x02\x03",
            "#00004FThat I can keep protecting\x01",
            "Crossbell from now on too, I guess.\x02\x03",
            "#00000FOf course, with Fran, and the other\x01",
            "members of the Support Section too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x156,
        "#06402FUh uh, typical of Mr. Lloyd.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHa ha, thanks.\x02\x03",
            "#00000FSo, Fran, what\x01",
            "did you wish for?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9D25")

    label("loc_9C08")


    ChrTalk(
        0x101,
        (
            "#00000FI already wished for my top\x01",
            "thing when I first came here.\x02\x03",
            "#00004FWishing for the same thing\x01",
            "wouldn't be nice, so I wished\x01",
            "for your wish to come true, Fran.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x156,
        "#06402FUh uh, thank you very much.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHa ha, you're welcome.\x02\x03",
            "#00000FSo, Fran, what\x01",
            "did you wish for?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9D25")


    ChrTalk(
        0x156,
        (
            "#06409FUh uh, as you may\x01",
            "expect, I wished to\x01",
            "become like big sis.\x02\x03",
            "#06401FAfter all, my eternal goal is\x01",
            "to be a cool and reliable\x01",
            "woman like big sis!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FA woman like Noｱl, eh...?\x01",
            "Ha ha, typical of you who like your sister a lot.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00005FBy the way, I have a simple question...\x01",
            "Didn't you aim to be a CGF member, Fran?\x02\x03",
            "#00000FSince you so love dearly Noｱl,\x01",
            "it wouldn't be strange you'd want\x01",
            "to work as a CGF member like her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x156,
        (
            "#06400FAhaha, in some way.\x01",
            "But as you can imagine, each person\x01",
            "has its own appropriate place.\x02\x03",
            "#06403FAt Police Academy, my results were more\x01",
            "suited for a white collar than training...\x02\x03",
            "#06400FSo I thought to protect Crossbell\x01",
            "in a way that suited me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYou're right, the people protecting Crossbell\x01",
            "are not only those working on site.\x02\x03",
            "#00004FBecause there's an operation center and the\x01",
            "operator job, we can be successful too...\x02\x03",
            "#00009FIn that sense, being at the\x01",
            "reception matches you...\x01",
            "Probably you were suited for it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x156,
        (
            "#06409FEheheh...\x01",
            "If you say that much,\x01",
            "I'm going to blush.\x02\x03",
            "#06400FEven my wish of being\x01",
            "like my big sis is within\x01",
            "the compass of that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FHa ha, I see.\x02\x03",
            "#00000F...Well then, we did\x01",
            "our wishes so,\x01",
            "should we go?\x02",
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

    # Function_36_9829 end

    def Function_37_A218(): pass

    label("Function_37_A218")

    EventBegin(0x0)
    Call(0, 23)
    BeginChrThread(0x14C, 3, 0, 25)
    WaitChrThread(0x14C, 3)
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A322")

    ChrTalk(
        0x101,
        (
            "#00000FAlright, let's try to\x01",
            "make a wish now.\x02\x03",
            "#00005FUhhm...will it be okay saying my\x01",
            "wish in front of this mirror?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14C,
        (
            "#05900FI think that maybe it is just fine\x01",
            "thinking about the wish \x01",
            "in your head?\x02\x03",
            "Then, let's try.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A3BA")

    label("loc_A322")


    ChrTalk(
        0x101,
        (
            "#00000FThen, let's try\x01",
            "making a wish.\x02\x03",
            "#00004FIt should be all right thinking about\x01",
            "a wish in front of this mirror.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14C,
        "#05900FYes, let's try it.\x02",
    )

    CloseMessageWindow()

    label("loc_A3BA")

    BeginChrThread(0x14C, 3, 0, 26)
    WaitChrThread(0x14C, 3)

    ChrTalk(
        0x101,
        "#00003F............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14C,
        "#05903F............\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x14C, 3, 0, 27)
    WaitChrThread(0x14C, 3)
    Call(0, 24)
    BeginChrThread(0x14C, 3, 0, 25)
    WaitChrThread(0x14C, 3)

    ChrTalk(
        0x101,
        "#00000F...I wonder if this is enough?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14C,
        (
            "#05904FYes, I think it should be.\x02\x03",
            "#05900FLloyd, what did you\x01",
            "wish for, I wonder?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A601")

    ChrTalk(
        0x101,
        (
            "#00000FHa ha, well I'm a little embarrassed\x01",
            "because it's so normal.\x02\x03",
            "#00004FThat I can keep protecting\x01",
            "Crossbell from now on too, I guess.\x02\x03",
            "#00000FOf course, with sister Cecil and the other\x01",
            "members of the Support Section too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14C,
        "#05902FUh uh, a Lloyd-like wish.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHa ha, thanks.\x02\x03",
            "#00000FSo, sister Cecil,\x01",
            "what did you wish for?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A727")

    label("loc_A601")


    ChrTalk(
        0x101,
        (
            "#00000FI already wished for my top\x01",
            "thing when I first came here.\x02\x03",
            "#00004FWishing for the same thing\x01",
            "wouldn't be nice, so I wished for\x01",
            "sister Cecil's wish to come true.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14C,
        "#05902FUh uh, thank you, Lloyd.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHa ha, you're welcome.\x02\x03",
            "#00000FSo, sister Cecil,\x01",
            "what did you wish for?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A727")


    ChrTalk(
        0x14C,
        (
            "#05900FAs you may think...\x01",
            "I wished that Lloyd and the others\x01",
            "may always be in health.\x02\x03",
            "#05904FTo me, that is my\x01",
            "greatest desire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F...I see, thank you, sister Cecil.\x02\x03",
            "#00000FWe'll pay a lot of attention\x01",
            "to not be seriously injured and\x01",
            "get carried over to the hospital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14C,
        (
            "#05909FUh uh, please do.\x02\x03",
            "#05901FIf that were to happen,\x01",
            "I will give you so many painful\x01",
            "shots that you will cry a lot.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00006F(Well...it seems something that\x01",
            "at least Randy would enjoy...)\x02\x03",
            "#00000F...You too, sister Cecil, don't\x01",
            "force yourself and work all the time.\x01",
            "Sometimes you rest too, all right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14C,
        (
            "#05905FHmm, when I think about the patients,\x01",
            "I want to be working to do as much\x01",
            "as possible.\x02\x03",
            "#05909FAlso, every now and then I take \x01",
            "a rest like now, so don't worry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FWell, in your case, sister Cecil, \x01",
            "it really seems you only rest \x01",
            "every now and then, you see...\x02\x03",
            "#00001FThat's why I'm worried\x01",
            "about you, sister Cecil.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14C,
        (
            "#05904FYes...I understand.\x01",
            "I will be careful to\x01",
            "not exaggerate.\x02\x03",
            "#05909FUh uh, nevertheless,\x01",
            "being worried about your sister...\x01",
            "You have grown up too, hm, Lloyd?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00006FAgain, treating me like a child...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14C,
        "#05902FUh uh, sorry, I am sorry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F(...As expected, sister Cecil will\x01",
            "always be "sister Cecil" in all respects.)\x02\x03",
            "#00006F(...I feel a little sad, though.)\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_37_A218 end

    def Function_38_AC90(): pass

    label("Function_38_AC90")

    EventBegin(0x0)
    Call(0, 23)
    BeginChrThread(0x134, 3, 0, 25)
    WaitChrThread(0x134, 3)
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AD86")

    ChrTalk(
        0x101,
        (
            "#00000FThen, let's make\x01",
            "our wishes now.\x02\x03",
            "#00005FUhhm...will it be okay saying my\x01",
            "wish in front of this mirror?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x134,
        (
            "#01700FIsn't maybe just fine thinking\x01",
            "about the wish in your head?\x02\x03",
            "Then, let's try.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AE23")

    label("loc_AD86")


    ChrTalk(
        0x101,
        (
            "#00000FThen, let's make\x01",
            "our wishes now.\x02\x03",
            "#00004FIt should be all right just thinking\x01",
            "about a wish in front of this mirror.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x134,
        "#01700FOkay, let's try.\x02",
    )

    CloseMessageWindow()

    label("loc_AE23")

    BeginChrThread(0x134, 3, 0, 26)
    WaitChrThread(0x134, 3)

    ChrTalk(
        0x101,
        "#00003F............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x134,
        "#01703F............\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x134, 3, 0, 27)
    WaitChrThread(0x134, 3)
    Call(0, 24)
    BeginChrThread(0x134, 3, 0, 25)
    WaitChrThread(0x134, 3)

    ChrTalk(
        0x101,
        "#00000F...I wonder if this is enough?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x134,
        (
            "#01704FYes, I'm done too.\x02\x03",
            "#01700FBy the way, younger brother,\x01",
            "what did you wish for?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B080")

    ChrTalk(
        0x101,
        (
            "#00000FHa ha, well I'm a little embarrassed\x01",
            "because it's so normal.\x02\x03",
            "#00004FThat I can keep protecting\x01",
            "Crossbell from now on too, I guess.\x02\x03",
            "#00000FOf course, with Miss Ilya, the others\x01",
            "and everyone from Arc-en-ciel too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x134,
        (
            "#01702FUh uh, I see.\x01",
            "You've said quite the admirable thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHa ha, thanks.\x02\x03",
            "#00000FAnd what did you\x01",
            "wish for, Miss Ilya?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B1B8")

    label("loc_B080")


    ChrTalk(
        0x101,
        (
            "#00000FI already wished for my top\x01",
            "thing when I first came here.\x02\x03",
            "#00004FWishing for the same thing\x01",
            "wouldn't be nice, so I wished for\x01",
            "your wish to come true, Miss Ilya.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x134,
        (
            "#01702FMy, how considerate\x01",
            "of you, younger brother.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHa ha, you're welcome.\x02\x03",
            "#00000FAnd what did you\x01",
            "wish for, Miss Ilya?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B1B8")


    ChrTalk(
        0x134,
        (
            "#01704FOf course I wished to\x01",
            "be able to keep dancing\x01",
            "no matter what happens.\x02\x03",
            "#01700FWell, even if I didn't wish for it,\x01",
            "it will never happen for me to\x01",
            "leave the stage, absolutely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FHa ha, that's Miss Ilya for you.\x01",
            "You will never lose to anyone in\x01",
            "regards to stage tenacity.\x02\x03",
            "#00009FI'm always shocked to\x01",
            "think where all that\x01",
            "power gushes from?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x134,
        (
            "#01703FHmm, let's see.\x01",
            "If I had to say...\x02\x03",
            "#01700FI guess it's that I\x01",
            ""love" dancing on stage\x01",
            "more than anyone else.\x02\x03",
            "In that regard, I'm confident I'll never\x01",
            "lose to anyone in the entire continent...\x02\x03",
            "#01709FI'll keep dancing until I die\x01",
            "as long as I feel that way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F"Love"...?\x01",
            "It's very simple,\x01",
            "but I feel like I get it.\x02\x03",
            "#00004FThinking about it that much could be\x01",
            "amazing too, in a certain sense.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x134,
        (
            "#01700FUh uh, it's nothing so grand.\x01",
            "Loving something or not is\x01",
            "a feeling everyone has.\x02\x03",
            "#01709FYou too younger brother, wouldn't you even put\x01",
            "your life on the line for those precious to you?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00000FYes...I really think so.\x02\x03",
            "#00004F(Even the fact I could settle that\x01",
            "Cult incident was because of the\x01",
            "strong feelings to protect KeA...)\x02\x03",
            "(I guess that people can become incredibly\x01",
            "strong for the sake of those precious to them.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x134,
        (
            "#01700FUh uh, it seems you get it.\x02\x03",
            "#01709F...Well, we made our\x01",
            "wishes, so let's go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes, I agree.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_38_AC90 end

    def Function_39_B70C(): pass

    label("Function_39_B70C")

    EventBegin(0x0)
    Call(0, 23)
    BeginChrThread(0x135, 3, 0, 25)
    WaitChrThread(0x135, 3)
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B818")

    ChrTalk(
        0x101,
        (
            "#00000FAlright, let's try to\x01",
            "make a wish now.\x02\x03",
            "#00005FUhhm...will it be okay saying my\x01",
            "wish in front of this mirror?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x135,
        (
            "#01802FI wonder if it's just fine\x01",
            "thinking about the wish \x01",
            "in your head?\x02\x03",
            "#01803F...Then, let's try.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B8B0")

    label("loc_B818")


    ChrTalk(
        0x101,
        (
            "#00000FThen, let's try\x01",
            "making a wish.\x02\x03",
            "#00004FIt should be all right thinking about\x01",
            "a wish in front of this mirror.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x135,
        "#01803F...Yes, let's try.\x02",
    )

    CloseMessageWindow()

    label("loc_B8B0")

    BeginChrThread(0x135, 3, 0, 26)
    WaitChrThread(0x135, 3)

    ChrTalk(
        0x101,
        "#00003F............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x135,
        "#01803F............\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x135, 3, 0, 27)
    WaitChrThread(0x135, 3)
    Call(0, 24)
    BeginChrThread(0x135, 3, 0, 25)
    WaitChrThread(0x135, 3)

    ChrTalk(
        0x101,
        "#00000F...I wonder if this is enough?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x135,
        (
            "#01804FYes, I'm done too.\x02\x03",
            "#01802FUhhm, Mr. Lloyd,\x01",
            "what did you wish for?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BAF4")

    ChrTalk(
        0x101,
        (
            "#00000FHa ha, well I'm a little embarrassed\x01",
            "because it's so normal.\x02\x03",
            "#00004FThat I can keep protecting\x01",
            "Crossbell from now on too, I guess.\x02\x03",
            "#00000FOf course, with Rixia, the others and\x01",
            "and everyone from Arc-en-ciel too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x135,
        (
            "#01802F...Is that so?\x01",
            "Uh uh, typical of Mr. Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHa ha, thanks.\x02\x03",
            "#00000FSo, Rixia, what\x01",
            "did you wish for?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BC1E")

    label("loc_BAF4")


    ChrTalk(
        0x101,
        (
            "#00000FI already wished for my top\x01",
            "thing when I first came here.\x02\x03",
            "#00004FWishing for the same thing\x01",
            "wouldn't be nice, so I wished\x01",
            "for your wish to come true, Rixia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x135,
        (
            "#01802F...Really?\x01",
            "Uh uh, thank you very much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHa ha, you're welcome.\x02\x03",
            "#00000FSo, Rixia, what\x01",
            "did you wish for?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BC1E")

    OP_63(0x135, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x135)

    ChrTalk(
        0x135,
        (
            "#01803FMy wish is...\x01",
            ""I want to become an\x01",
            "artist like Miss Ilya."\x02\x03",
            "#01802FUh uh, maybe it's presumptuous from\x01",
            "someone like me who is still a rookie.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FNo...\x01",
            "I think that's not the case.\x02\x03",
            "#00003FYou were quite popular in the\x01",
            "Arc-en-ciel public performances too...\x02\x03",
            "#00000FAnd most of all, your talent\x01",
            "was recognised by her.\x02\x03",
            "#00009FIf you keep up your efforts like this,\x01",
            "I feel sure that in the future you'll be\x01",
            "able to become a big star like Miss Ilya.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x135, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(
        0x135,
        (
            "#01809FN-No way...\x01",
            "For me it's still far far too soon.\x02\x03",
            "#01804FI think that Sully has much more\x01",
            "talent than someone like me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FUhhm, I think you should believe\x01",
            "in yourself a little more...\x02\x03",
            "#00000FWell, I'll root for you too so\x01",
            "that your wish comes true...\x01",
            "Do your best from now on too, hm?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x135,
        "#01809FY-Yes, thank you very much.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FHa ha, somehow it was embarrassing\x01",
            "saying this right to your face.\x02\x03",
            "#00000F...Then, we're finished with our wishes,\x01",
            "so should we go now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x135,
        "#01802FYes, I agree.\x02",
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
            "#01803F#11P(Although it's a wish that\x01",
            "will never come true...)\x02\x03",
            "#01808F(I will be forgiven for only\x01",
            "thinking about it, right...?)\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_9B(0x0, 0x135, 0x0, 0x7D0, 0x7D0, 0x0)
    OP_0D()
    EndChrThread(0x101, 0x3)
    Return()

    # Function_39_B70C end

    def Function_40_C108(): pass

    label("Function_40_C108")

    EventBegin(0x0)
    Call(0, 23)
    BeginChrThread(0x166, 3, 0, 25)
    WaitChrThread(0x166, 3)
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C224")

    ChrTalk(
        0x101,
        (
            "#00000FAlright, let's try to\x01",
            "make a wish now.\x02\x03",
            "#00005FUhhm...will it be okay saying my\x01",
            "wish in front of this mirror?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x166,
        (
            "#14000FI guess that's just fine thinking\x01",
            "about the wish in your head.\x02\x03",
            "#14003FIf we're gonna do it, let's do it now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C2D9")

    label("loc_C224")


    ChrTalk(
        0x101,
        (
            "#00000FThen, let's try\x01",
            "making a wish.\x02\x03",
            "#00004FIt should be all right thinking about\x01",
            "a wish in front of this mirror.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x166,
        (
            "#14003F...Well, if we're gonna do it,\x01",
            "let's do it now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C2D9")

    BeginChrThread(0x166, 3, 0, 26)
    WaitChrThread(0x166, 3)

    ChrTalk(
        0x101,
        "#00003F............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x166,
        "#14008F............\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x166, 3, 0, 27)
    WaitChrThread(0x166, 3)
    Call(0, 24)
    BeginChrThread(0x166, 3, 0, 25)
    WaitChrThread(0x166, 3)

    ChrTalk(
        0x101,
        "#00000F...I wonder if this is enough?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x166,
        (
            "#14003FHm, I'm done here.\x02\x03",
            "#14000F...So, what did\x01",
            "you wish for?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C503")

    ChrTalk(
        0x101,
        (
            "#00000FHa ha, well I'm a little embarrassed\x01",
            "because it's so normal.\x02\x03",
            "#00004FThat I can keep protecting\x01",
            "Crossbell from now on too, I guess.\x02\x03",
            "#00000FOf course, with Sully, the others\x01",
            "and everyone from Arc-en-ciel too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x166,
        (
            "#14000FHmm...\x01",
            "Well, it's fine I guess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHa ha, thanks.\x02\x03",
            "#00000FSo, Sully, what\x01",
            "did you wish for?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C628")

    label("loc_C503")


    ChrTalk(
        0x101,
        (
            "#00000FI already wished for my top\x01",
            "thing when I first came here.\x02\x03",
            "#00004FWishing for the same thing\x01",
            "wouldn't be nice, so I wished\x01",
            "for your wish to come true, Sully.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x166,
        "#14006FTch, none of your business.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FHa ha...\x01",
            "I guess I was nosy.\x02\x03",
            "#00000FSo, Sully, what\x01",
            "did you wish for?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C628")

    OP_63(0x166, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x166)

    ChrTalk(
        0x166,
        (
            "#14003FI...\x01",
            "Didn't wish for anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F*shock*...\x01",
            "Hey, try to explain that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x166,
        (
            "#14006F...First of all, wishes are stuff\x01",
            "that really don't come true.\x02\x03",
            "#14008FThe slums where I lived were like that.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x166,
        (
            "#14000F...In the slums I'm from,\x01",
            "there were so many guys\x01",
            "like me.\x02\x03",
            "#14003FI drifted to Crossbell and\x01",
            "Miss Ilya picked me up...\x01",
            "But that was just sheer luck.\x02\x03",
            "#14008FThat's why wishing for more\x01",
            "than that would really be\x01",
            "too much to ask for.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00004FSully...\x01",
            "...You're kind.\x02",
        )
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
            "#00002FI think there's hardly\x01",
            "anyone who can think like\x01",
            "that for the sake of others.\x02\x03",
            "#00004FThat's because you're kind and have\x01",
            "a heart considerate of people.\x02\x03",
            "#00000FBut...that doesn't mean\x01",
            "you don't have to become\x01",
            "happy, you now?\x02",
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
            "#00000FYou don't have to think so hard.\x01",
            "In practice, it's fine to wish\x01",
            "for something.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x166, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x166,
        (
            "#14006FOh, jeez, I got it...\x01",
            "You're a preachy and annoying guy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006FS-Sorry for being preachy.\x02",
    )

    CloseMessageWindow()
    OP_63(0x166, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x166)

    ChrTalk(
        0x166,
        (
            "#14003F...I don't know the future, but it's true\x01",
            "I've got something I want to come true too.\x02\x03",
            "#14000FFor now, I somehow want that the renewal\x01",
            "public performance is a success.\x02\x03",
            "#14009F...Is such a thing ok?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FYeah, why not?\x02\x03",
            "I too will wish from my heart\x01",
            "that it becomes true.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x166,
        (
            "#14012FD-Don't say embarrassing stuff\x01",
            "right to my face, jeez!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_40_C108 end

    def Function_41_CBE3(): pass

    label("Function_41_CBE3")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000FWe're aiming for the top floor.\x01",
            "Let's go now.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 0, -950, -53650, 0)
    EventEnd(0x4)
    Return()

    # Function_41_CBE3 end

    def Function_42_CC34(): pass

    label("Function_42_CC34")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000FLet's try to make a wish in front\x01",
            "of the "mirror" upstairs.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 0, 40550, -13830, 180)
    EventEnd(0x4)
    Return()

    # Function_42_CC34 end

    def Function_43_CC93(): pass

    label("Function_43_CC93")

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

    # Function_43_CC93 end

    SaveToFile()

Try(main)
