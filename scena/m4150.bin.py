from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "m4150.bin",                # FileName
        "m4150",                    # MapName
        "m4150",                    # Location
        0x00C9,                     # MapIndex
        "ed7301",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x28,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 201, 0, 1, 0, 2],
    )

    BuildStringList((
        "m4150",                  # 0
        "ゲルマー",               # 1
        "bm4150",                 # 2
        "bm4150",                 # 3
        "bm4150",                 # 4
        "bm4150",                 # 5
    ))

    ATBonus("ATBonus_3B4", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_1FFC", 4,   4,   6,   6,   4,   6,   6)
    Sepith("Sepith_200C", 6,   6,   8,   8,   8,   6,   6)
    Sepith("Sepith_2004", 12,  12,  4,   4,   4,   2,   2)

    MonsterBattlePostion("MonsterBattlePostion_3F4", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_3F8", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_3FC", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_400", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_404", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_408", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_40C", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_410", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_474", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_478", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_47C", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_480", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_484", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_488", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_48C", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_490", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_414", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_418", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_41C", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_420", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_424", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_428", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_42C", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_430", 8, 14, 180)

    # monster count: 13

    BattleInfo(
        "BattleInfo_494", 0x0000, 72, 6, 60, 10, 1, 40, 0, "bm4150", "Sepith_1FFC", 40, 30, 20, 0,
        (
            ("ms86900.dat", "ms86900.dat", "ms86900.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_3F4", "MonsterBattlePostion_474", "ed7450", "ed7453", "ATBonus_3B4"),
            ("ms86900.dat", "ms86900.dat", "ms86900.dat", "ms86900.dat", 0, 0, 0, 0, "MonsterBattlePostion_3F4", "MonsterBattlePostion_474", "ed7450", "ed7453", "ATBonus_3B4"),
            ("ms86900.dat", "ms86900.dat", "ms86900.dat", "ms86900.dat", "ms86900.dat", 0, 0, 0, "MonsterBattlePostion_3F4", "MonsterBattlePostion_474", "ed7450", "ed7453", "ATBonus_3B4"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_5CC", 0x0000, 72, 6, 60, 10, 1, 30, 0, "bm4150", "Sepith_200C", 50, 50, 0, 0,
        (
            ("ms82500.dat", "ms82500.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3F4", "MonsterBattlePostion_474", "ed7450", "ed7453", "ATBonus_3B4"),
            ("ms82500.dat", "ms86900.dat", "ms86900.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_414", "MonsterBattlePostion_474", "ed7450", "ed7453", "ATBonus_3B4"),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_530", 0x0000, 72, 6, 60, 10, 1, 20, 0, "bm4150", "Sepith_2004", 40, 30, 20, 0,
        (
            ("ms83700.dat", "ms83700.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3F4", "MonsterBattlePostion_474", "ed7450", "ed7453", "ATBonus_3B4"),
            ("ms83700.dat", "ms83700.dat", "ms83700.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_414", "MonsterBattlePostion_474", "ed7450", "ed7453", "ATBonus_3B4"),
            ("ms83700.dat", "ms83700.dat", "ms83700.dat", "ms83700.dat", 0, 0, 0, 0, "MonsterBattlePostion_3F4", "MonsterBattlePostion_474", "ed7450", "ed7453", "ATBonus_3B4"),
            (),
        )
    )

    # event battle count: 1

    BattleInfo(
        "BattleInfo_63C", 0x0000, 50, 6, 45, 0, 1, 0, 0, "bm4150", 0x00000000, 100, 0, 0, 0,
        (
            ("ms82500.dat", "ms82500.dat", "ms82500.dat", "ms82500.dat", 0, 0, 0, 0, "MonsterBattlePostion_3F4", "MonsterBattlePostion_474", "ed7451", "ed7453", "ATBonus_3B4"),
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
        "monster/ch86950.itc",               # 10
        "monster/ch86951.itc",               # 11
        "monster/ch83750.itc",               # 12
        "monster/ch83751.itc",               # 13
        "monster/ch82550.itc",               # 14
        "monster/ch82551.itc",               # 15
    ))

    DeclNpc(108000,  500,     715000,  0,    484,  0x0, 0,   20,  0,   0,   0,   255, 255, 255,  0)

    DeclMonster(4294964736, 196080,  0,       0x101009E,    "BattleInfo_494", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(19810,   382230,  0,       0x10100E1,    "BattleInfo_494", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(27390,   412520,  4294961966, 0x1010087,    "BattleInfo_494", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(4294966826, 587520,  0,       0x1010090,    "BattleInfo_494", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(94260,   720470,  0,       0x1010087,    "BattleInfo_494", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(106580,  718340,  0,       0x1010110,    "BattleInfo_494", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(99450,   716980,  0,       0x10100E1,    "BattleInfo_494", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(4294934436, 597770,  0,       0x1010073,    "BattleInfo_494", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(4294770926, 597920,  0,       0x1010060,    "BattleInfo_5CC", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(4294759026, 598290,  0,       0x1010067,    "BattleInfo_5CC", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(4294576086, 597720,  0,       0x101002D,    "BattleInfo_530", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(4294572356, 606270,  0,       0x10100E1,    "BattleInfo_530", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(4294561526, 604780,  0,       0x1010087,    "BattleInfo_530", 0,   18,  0xFFFF, 2,  3)

    DeclActor(108000,  0,       715000,  1200,    108000,  1000,    715000,  0x007C, 0,  3,  0x0000)
    DeclActor(4294955796, 0,       200000,  1200,    4294955796, 1000,    200000,  0x007C, 0,  4,  0x0000)
    DeclActor(25750,   4294967046, 379000,  1200,    25750,   750,     379000,  0x007C, 0,  5,  0x0000)
    DeclActor(99000,   0,       724000,  1200,    99000,   1000,    724000,  0x007C, 0,  6,  0x0000)
    DeclActor(4294765546, 0,       588500,  1200,    4294765546, 1000,    588500,  0x007C, 0,  7,  0x0000)
    DeclActor(4294560046, 0,       608000,  1200,    4294560046, 1000,    608000,  0x007C, 0,  8,  0x0000)
    DeclActor(11280,   0,       4294964866, 1800,    11280,   2000,    4294964866, 0x007C, 0,  11, 0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 0
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4, 5])                   # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 2
    ChipFrameInfo(800, 0, [0, 1, 2, 3, 4])                       # 3
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 4
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4, 5])                   # 5

    ScpFunction((
        "Function_0_6F8",          # 00, 0
        "Function_1_714",          # 01, 1
        "Function_2_724",          # 02, 2
        "Function_3_F5C",          # 03, 3
        "Function_4_1178",         # 04, 4
        "Function_5_12CA",         # 05, 5
        "Function_6_141C",         # 06, 6
        "Function_7_157D",         # 07, 7
        "Function_8_16CF",         # 08, 8
        "Function_9_1821",         # 09, 9
        "Function_10_1F06",        # 0A, 10
        "Function_11_1F25",        # 0B, 11
    ))


    def Function_0_6F8(): pass

    label("Function_0_6F8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_713")
    OP_A1(0xFE, 0x3E8, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_0_6F8")

    label("loc_713")

    Return()

    # Function_0_6F8 end

    def Function_1_714(): pass

    label("Function_1_714")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_723")
    ClearScenarioFlags(0x22, 0)
    Event(0, 9)

    label("loc_723")

    Return()

    # Function_1_714 end

    def Function_2_724(): pass

    label("Function_2_724")

    OP_52(0x9, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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
    OP_52(0xF, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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
    OP_52(0x11, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    LoadEffect(0x9, "map/mpcave2.eff")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EB4")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_E6(0x0, 0x7, 0xFF, 0xFF, 0xFF, 0xDC, 0x0)
    OP_11(0x0, 0x0, 0x0, 0x19, 0x28, 0x0)

    label("loc_EB4")

    OP_66(0x6, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_ED1")
    SetMapObjFrame(0xFF, "nawa", 0x0, 0x1)
    OP_65(0x6, 0x1)

    label("loc_ED1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1FB, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EE4")
    OP_70(0x0, 0x0)
    Jump("loc_EE8")

    label("loc_EE4")

    OP_70(0x0, 0x1E)

    label("loc_EE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1FB, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EFB")
    OP_70(0x1, 0x0)
    Jump("loc_EFF")

    label("loc_EFB")

    OP_70(0x1, 0x1E)

    label("loc_EFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1FB, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F12")
    OP_70(0x2, 0x0)
    Jump("loc_F16")

    label("loc_F12")

    OP_70(0x2, 0x1E)

    label("loc_F16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1FB, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F29")
    OP_70(0x3, 0x0)
    Jump("loc_F2D")

    label("loc_F29")

    OP_70(0x3, 0x1E)

    label("loc_F2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1FB, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F40")
    OP_70(0x4, 0x0)
    Jump("loc_F44")

    label("loc_F40")

    OP_70(0x4, 0x1E)

    label("loc_F44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F57")
    OP_70(0x5, 0x0)
    Jump("loc_F5B")

    label("loc_F57")

    OP_70(0x5, 0x1E)

    label("loc_F5B")

    Return()

    # Function_2_724 end

    def Function_3_F5C(): pass

    label("Function_3_F5C")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1FB, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_112D")
    Sound(14, 0, 100, 0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21B, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_105F")
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0x8, 0x0, 0)
    OP_98(0x8, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_FB9():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_FB9)

    def lambda_FD3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_FD3)
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
    Battle("BattleInfo_63C", 0x0, 0x0, 0x0, 0xB, 0xFF)
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0x8, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_1040"),
        (2, "loc_104F"),
        (1, "loc_105C"),
        (SWITCH_DEFAULT, "loc_105F"),
    )


    label("loc_1040")

    SetScenarioFlags(0x21B, 6)
    OP_70(0x0, 0x1E)
    Sleep(500)
    Jump("loc_105F")

    label("loc_104F")

    OP_70(0x0, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_105C")

    OP_B9(0x0)
    Return()

    label("loc_105F")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0xBB, 1)"), scpexpr(EXPR_END)), "loc_10B8")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0xBB),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1FB, 3)
    OP_E0(0x5, 0x0)
    Jump("loc_1128")

    label("loc_10B8")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0xBB),
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

    label("loc_1128")

    Jump("loc_116C")

    label("loc_112D")

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

    label("loc_116C")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_F5C end

    def Function_4_1178(): pass

    label("Function_4_1178")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1FB, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1274")
    Sound(14, 0, 100, 0)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x20C, 1)"), scpexpr(EXPR_END)), "loc_11FD")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x20C),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1FB, 4)
    OP_E0(0x5, 0x0)
    Jump("loc_126F")

    label("loc_11FD")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x20C),
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

    label("loc_126F")

    Jump("loc_12BE")

    label("loc_1274")

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

    label("loc_12BE")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_1178 end

    def Function_5_12CA(): pass

    label("Function_5_12CA")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1FB, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13C6")
    Sound(14, 0, 100, 0)
    OP_74(0x2, 0x1E)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x64B, 1)"), scpexpr(EXPR_END)), "loc_134F")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x64B),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1FB, 5)
    OP_E0(0x5, 0x0)
    Jump("loc_13C1")

    label("loc_134F")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x64B),
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

    label("loc_13C1")

    Jump("loc_1410")

    label("loc_13C6")

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

    label("loc_1410")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_12CA end

    def Function_6_141C(): pass

    label("Function_6_141C")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1FB, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_154D")
    Sound(14, 0, 100, 0)
    OP_74(0x3, 0x1E)
    OP_71(0x3, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    OP_70(0x3, 0x1E)
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
    SetScenarioFlags(0x1FB, 6)
    OP_E0(0x5, 0x0)
    Jump("loc_156B")

    label("loc_154D")


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

    label("loc_156B")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_141C end

    def Function_7_157D(): pass

    label("Function_7_157D")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1FB, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1679")
    Sound(14, 0, 100, 0)
    OP_74(0x4, 0x1E)
    OP_71(0x4, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x90, 1)"), scpexpr(EXPR_END)), "loc_1602")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x90),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1FB, 7)
    OP_E0(0x5, 0x0)
    Jump("loc_1674")

    label("loc_1602")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x90),
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

    label("loc_1674")

    Jump("loc_16C3")

    label("loc_1679")

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

    label("loc_16C3")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_157D end

    def Function_8_16CF(): pass

    label("Function_8_16CF")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17CB")
    Sound(14, 0, 100, 0)
    OP_74(0x5, 0x1E)
    OP_71(0x5, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1FD, 1)"), scpexpr(EXPR_END)), "loc_1754")
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
    SetScenarioFlags(0x1F1, 4)
    OP_E0(0x5, 0x0)
    Jump("loc_17C6")

    label("loc_1754")

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

    label("loc_17C6")

    Jump("loc_1815")

    label("loc_17CB")

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

    label("loc_1815")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_16CF end

    def Function_9_1821(): pass

    label("Function_9_1821")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00250.itc", 0x1E)
    LoadChrToIndex("chr/ch00254.itc", 0x1F)
    LoadEffect(0x0, "battle\\mgaria0.eff")
    LoadEffect(0x1, "event\\eva06_00.eff")
    SoundLoad(852)
    SetChrPos(0x101, 2650, 0, 1650, 345)
    SetChrPos(0x102, 1350, 0, 750, 345)
    SetChrPos(0x103, 3550, 0, 750, 345)
    SetChrPos(0x109, 7450, 0, -710, 255)
    SetChrPos(0x105, 11750, 0, -1600, 75)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_68(11850, 2500, -1400, 0)
    MoveCamera(30, 30, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21000, 0)
    OP_68(1250, 1300, 5250, 8000)
    MoveCamera(25, 13, 0, 8000)
    OP_6E(500, 8000)
    SetCameraDistance(31250, 8000)
    PlaceName2(340, 200, "c_plac72", 0x0, 3000)

    def lambda_1937():
        OP_95(0xFE, 1950, 0, -550, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1937)
    FadeToBright(1000, 0)
    OP_0D()
    OP_93(0x105, 0xFF, 0x1F4)

    def lambda_1962():
        OP_95(0xFE, 3800, 0, -700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1962)
    WaitChrThread(0x109, 1)

    def lambda_1980():
        OP_93(0xFE, 0x159, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1980)
    WaitChrThread(0x105, 1)

    def lambda_1991():
        OP_93(0xFE, 0x159, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_1991)
    OP_6F(0x79)
    Sleep(500)
    Fade(500)
    OP_68(2700, 1000, 700, 0)
    MoveCamera(30, 20, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20000, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x109,
        "#10105F#12PWhat is this place...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103F#11PIt looks like a shaft connected\x01",
            "to a very old tunnel...\x02\x03",
            "#00105FIt could be connecting to the old abandoned\x01",
            "mine area that was sealed before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#11PAs far as its position on the map,\x01",
            "that could be very possible.\x02\x03",
            "#00008FIf it goes up to the old abandoned mine,\x01",
            "it could be possible to come out on the\x01",
            "opposite side of the jaegers defense line.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F#12PIf he wants to set up a trap, \x01",
            "it could be the ideal point.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    VolumeBGM(0x50, 0x3E8)
    Sound(2278, 255, 80, 0)
    Sleep(800)
    Fade(250)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0x103, 0x1E)
    SetChrSubChip(0x103, 0x0)
    OP_0D()
    Sound(357, 0, 70, 0)
    Sound(852, 2, 100, 0)
    PlayEffect(0x0, 0x0, 0x103, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x1, 0x103, 0x5, 0, 1450, 0, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0x103, 0x1F)
    SetChrSubChip(0x103, 0x0)
    BeginChrThread(0x103, 3, 0, 10)

    def lambda_1C6D():
        TurnDirection(0x101, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1C6D)
    Sleep(50)

    def lambda_1C7D():
        TurnDirection(0x102, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1C7D)
    Sleep(50)

    def lambda_1C8D():
        TurnDirection(0x109, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1C8D)
    Sleep(50)

    def lambda_1C9D():
        TurnDirection(0x105, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_1C9D)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    Sleep(2000)
    SetChrSubChip(0x103, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x103)
    Sleep(500)
    Fade(250)
    Sound(812, 0, 100, 0)
    StopSound(852, 500, 100)
    EndChrThread(0x103, 0x3)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    StopEffect(0x0, 0x2)
    StopEffect(0x1, 0x2)
    OP_0D()
    VolumeBGM(0x64, 0x3E8)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            "#00206F#11P...I think Mr. Randy has\x01",
            "already passed through here.\x02\x03",
            "#00200FHowever, it doesn't look like\x01",
            "such a complex tunnel.\x02\x03",
            "I think we can proceed\x01",
            "without getting lost much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002F#5PI see...\x02",
    )

    CloseMessageWindow()

    def lambda_1DDA():
        OP_93(0xFE, 0xA5, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1DDA)

    def lambda_1DE7():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1DE7)
    Sleep(50)

    def lambda_1DF7():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1DF7)
    Sleep(50)

    def lambda_1E07():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1E07)
    Sleep(50)

    def lambda_1E17():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_1E17)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    Sleep(100)

    ChrTalk(
        0x101,
        (
            "#00000F#5P──Alright.\x01",
            "Let's chase Randy someway!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100F#6PYes...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10100F#6PRoger!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10302F#12P──Allons-y.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_37()
    SetChrPos(0x0, 2650, 0, 1650, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetScenarioFlags(0x166, 5)
    OP_29(0xAA, 0x1, 0x6)
    OP_C9(0x1, 0x10000)
    OP_50(0x52, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x21, 5)
    OP_24(0x354)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_9_1821 end

    def Function_10_1F06(): pass

    label("Function_10_1F06")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1F24")
    OP_A1(0x103, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    Jump("Function_10_1F06")

    label("loc_1F24")

    Return()

    # Function_10_1F06 end

    def Function_11_1F25(): pass

    label("Function_11_1F25")

    EventBegin(0x2)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Climb the Rope\x01",      # 0
            "Step Away\x01",           # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1F7F"),
        (1, "loc_1F9F"),
        (SWITCH_DEFAULT, "loc_1FAB"),
    )


    label("loc_1F7F")

    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearMapFlags(0x8000000)
    EventEnd(0x3)
    NewScene("r2030", 103, 0, 0)
    IdleLoop()
    Jump("loc_1FAB")

    label("loc_1F9F")

    ClearMapFlags(0x8000000)
    EventEnd(0x3)
    Jump("loc_1FAB")

    label("loc_1FAB")

    Return()

    # Function_11_1F25 end

    SaveToFile()

Try(main)
