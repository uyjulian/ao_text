from ScenarioHelper import *

def main():
    CreateScenaFile(
        "m4010.bin",                # FileName
        "m4010",                    # MapName
        "m4010",                    # Location
        0x007B,                     # MapIndex
        "ed7350",
        0x00000000,                 # Flags
        ("m4010", "r0000_1", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x2B,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 123, 0, 2, 0, 3],
    )

    BuildStringList((
        "m4010",                  # 0
        "Dudley investigator",         # 1
        "Arios",               # 2
        "Dynaso",             # 3
        "bm4010",                 # 4
        "bm4010",                 # 5
        "bm4010",                 # 6
        "bm4010",                 # 7
    ))

    ATBonus("ATBonus_460", 100, 5, 1, 5, 1, 5, 1, 5, 5, 5, 5, 5, 5, 0, 0, 0)
    ATBonus("ATBonus_470", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    Sepith("Sepith_46A6", 2,   2,   0,   2,   2,   2,   1)
    Sepith("Sepith_469E", 0,   4,   0,   4,   1,   1,   1)
    Sepith("Sepith_4696", 3,   4,   5,   2,   0,   0,   0)

    MonsterBattlePostion("MonsterBattlePostion_490", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_494", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_498", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_49C", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_4A0", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_4A4", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_4A8", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_4AC", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_510", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_514", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_518", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_51C", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_520", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_524", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_528", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_52C", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_4B0", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_4B4", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_4B8", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_4BC", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_4C0", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_4C4", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_4C8", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_4CC", 8, 14, 180)

    # monster count: 12

    BattleInfo(
        "BattleInfo_610", 0x0000, 46, 6, 45, 6, 1, 40, 0, "bm4010", "Sepith_46A6", 60, 25, 10, 0,
        (
            ("ms83800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_490", "MonsterBattlePostion_510", "ed7450", "ed7453", "ATBonus_460"),
            ("ms83800.dat", "ms83800.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_490", "MonsterBattlePostion_510", "ed7450", "ed7453", "ATBonus_460"),
            ("ms83800.dat", "ms83800.dat", "ms83800.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_4B0", "MonsterBattlePostion_510", "ed7450", "ed7453", "ATBonus_460"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_574", 0x0000, 46, 6, 60, 6, 1, 20, 0, "bm4010", "Sepith_469E", 60, 25, 10, 0,
        (
            ("ms83600.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_490", "MonsterBattlePostion_510", "ed7450", "ed7453", "ATBonus_460"),
            ("ms83600.dat", "ms83600.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_490", "MonsterBattlePostion_510", "ed7450", "ed7453", "ATBonus_460"),
            ("ms83600.dat", "ms83600.dat", "ms83600.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_4B0", "MonsterBattlePostion_510", "ed7450", "ed7453", "ATBonus_460"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_530", 0x0000, 46, 6, 45, 6, 1, 40, 0, "bm4010", "Sepith_4696", 100, 0, 0, 0,
        (
            ("ms86200.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_4B0", "MonsterBattlePostion_510", "ed7450", "ed7453", "ATBonus_460"),
            (),
            (),
            (),
        )
    )

    # event battle count: 1

    BattleInfo(
        "BattleInfo_6AC", 0x0000, 50, 6, 45, 0, 1, 0, 0, "bm4010", 0x00000000, 100, 0, 0, 0,
        (
            ("ms86200.dat", "ms86200.dat", "ms86200.dat", "ms86200.dat", 0, 0, 0, 0, "MonsterBattlePostion_490", "MonsterBattlePostion_510", "ed7451", "ed7453", "ATBonus_470"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch00900.itc",                   # 00
        "chr/ch02400.itc",                   # 01
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
        "monster/ch86250.itc",               # 10
        "monster/ch86251.itc",               # 11
        "monster/ch83650.itc",               # 12
        "monster/ch83650.itc",               # 13
        "monster/ch83850.itc",               # 14
        "monster/ch83851.itc",               # 15
    ))

    DeclNpc(0,       4294959296, 4294965796, 90,   389,  0x0, 0,   0,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(0,       4294959296, 4294964796, 90,   389,  0x0, 0,   1,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(39580,   9550,    221570,  0,    484,  0x0, 0,   16,  0,   0,   1,   255, 255, 255,  0)

    DeclMonster(15760,   72320,   0,       0x101008C,    "BattleInfo_610", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(13220,   87760,   0,       0x101008C,    "BattleInfo_574", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(45940,   109370,  4294962296, 0x10100B9,    "BattleInfo_530", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(253530,  97490,   4294962296, 0x10100E6,    "BattleInfo_610", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(152730,  20290,   4294962296, 0x10100E6,    "BattleInfo_530", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(4294866436, 90780,   0,       0x101008C,    "BattleInfo_574", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(4294859516, 100190,  0,       0x10100B9,    "BattleInfo_574", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(4294852136, 88000,   0,       0x101005F,    "BattleInfo_610", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(4294857176, 126890,  3500,    0x10100E6,    "BattleInfo_530", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(4294844146, 151900,  9000,    0x10100B9,    "BattleInfo_574", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(4294828186, 159700,  9000,    0x101005F,    "BattleInfo_530", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(31000,   219940,  9000,    0x10100A0,    "BattleInfo_530", 0,   16,  0xFFFF, 0,  1)

    DeclEvent(0x0000, 0, 19,  2.7699999809265137,    7.920000076293945,     -9.0,                  2304.0,                [0.03125,              -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000001788139343,   0.0,                   -0.08656249940395355,  -2.640000104904175,    1.8000001907348633,    1.0])

    DeclActor(4294966196, 0,       78900,   2000,    4294966196, 1500,    78900,   0x007C, 0,  16, 0x0000)
    DeclActor(36110,   3200,    223690,  2000,    36110,   4700,    223690,  0x007C, 0,  17, 0x0000)
    DeclActor(147320,  4294962296, 22180,   1200,    147320,  4294963296, 22180,   0x007C, 0,  4,  0x0000)
    DeclActor(39580,   9050,    221570,  1200,    39580,   10050,   221570,  0x007C, 0,  5,  0x0000)
    DeclActor(259510,  4294962346, 97890,   1200,    259510,  4294963346, 97890,   0x007C, 0,  6,  0x0000)
    DeclActor(4294825116, 9000,    178130,  1200,    4294825116, 10000,   178130,  0x007C, 0,  7,  0x0000)
    DeclActor(247980,  9000,    234020,  1200,    247980,  10000,   234020,  0x007C, 0,  8,  0x0000)
    DeclActor(4294963026, 4294959396, 2580,    1200,    4294963026, 4294960896, 2580,    0x007C, 0,  12, 0x0000)

    ChipFrameInfo(699, 0, [0, 1, 2, 3, 4, 3, 2, 1])              # 0
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 1
    ChipFrameInfo(699, 0, [0, 1, 2, 3, 4, 5, 6])                 # 2
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5, 6])                # 3
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 4
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4])                      # 5

    ScpFunction((
        "Function_0_788",          # 00, 0
        "Function_1_838",          # 01, 1
        "Function_2_857",          # 02, 2
        "Function_3_89F",          # 03, 3
        "Function_4_DDD",          # 04, 4
        "Function_5_F2E",          # 05, 5
        "Function_6_1145",         # 06, 6
        "Function_7_12AC",         # 07, 7
        "Function_8_13FD",         # 08, 8
        "Function_9_154E",         # 09, 9
        "Function_10_1552",        # 0A, 10
        "Function_11_15EF",        # 0B, 11
        "Function_12_169A",        # 0C, 12
        "Function_13_1796",        # 0D, 13
        "Function_14_2BEA",        # 0E, 14
        "Function_15_37F8",        # 0F, 15
        "Function_16_3FC4",        # 10, 16
        "Function_17_4287",        # 11, 17
        "Function_18_442C",        # 12, 18
        "Function_19_45B9",        # 13, 19
    ))


    def Function_0_788(): pass

    label("Function_0_788")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_7C0"),
        (1, "loc_7CC"),
        (2, "loc_7D8"),
        (3, "loc_7E4"),
        (4, "loc_7F0"),
        (5, "loc_7FC"),
        (6, "loc_808"),
        (SWITCH_DEFAULT, "loc_814"),
    )


    label("loc_7C0")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_820")

    label("loc_7CC")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_820")

    label("loc_7D8")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_820")

    label("loc_7E4")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_820")

    label("loc_7F0")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_820")

    label("loc_7FC")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_820")

    label("loc_808")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_820")

    label("loc_814")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_820")

    label("loc_820")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_837")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_820")

    label("loc_837")

    Return()

    # Function_0_788 end

    def Function_1_838(): pass

    label("Function_1_838")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_856")
    OP_A1(0xFE, 0x2BC, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_1_838")

    label("loc_856")

    Return()

    # Function_1_838 end

    def Function_2_857(): pass

    label("Function_2_857")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x120, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x120, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_86F")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)

    label("loc_86F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_884")
    ClearScenarioFlags(0x22, 0)
    SetScenarioFlags(0x0, 0)
    SetScenarioFlags(0x0, 1)
    Event(0, 13)

    label("loc_884")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x120, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x120, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_89E")
    Event(0, 15)

    label("loc_89E")

    Return()

    # Function_2_857 end

    def Function_3_89F(): pass

    label("Function_3_89F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_8B4")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 0)

    label("loc_8B4")

    OP_52(0xD, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_65(0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x120, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CDB")
    OP_66(0x0, 0x1)

    label("loc_CDB")

    OP_1B(0x0, 0x0, 0x12)
    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x120, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CF4")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_CF4")

    ClearMapObjFlags(0x5, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x120, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D11")
    OP_70(0x5, 0x0)
    OP_70(0x6, 0x0)
    Jump("loc_D19")

    label("loc_D11")

    OP_70(0x5, 0x14)
    OP_70(0x6, 0x14)

    label("loc_D19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D2C")
    OP_70(0x0, 0x0)
    Jump("loc_D30")

    label("loc_D2C")

    OP_70(0x0, 0x1E)

    label("loc_D30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D43")
    OP_70(0x1, 0x0)
    Jump("loc_D47")

    label("loc_D43")

    OP_70(0x1, 0x1E)

    label("loc_D47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D5A")
    OP_70(0x2, 0x0)
    Jump("loc_D5E")

    label("loc_D5A")

    OP_70(0x2, 0x1E)

    label("loc_D5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D71")
    OP_70(0x3, 0x0)
    Jump("loc_D75")

    label("loc_D71")

    OP_70(0x3, 0x1E)

    label("loc_D75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D88")
    OP_70(0x4, 0x0)
    Jump("loc_D8C")

    label("loc_D88")

    OP_70(0x4, 0x1E)

    label("loc_D8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_DA0")
    OP_24(0x81)
    ClearScenarioFlags(0x0, 1)
    Jump("loc_DA6")

    label("loc_DA0")

    Sound(129, 1, 100, 0)

    label("loc_DA6")

    OP_1C(0x0, 0x8, 0x0, 0x32, 0x0, 0x9, 0x0, 0x0)
    OP_1C(0x0, 0x9, 0x0, 0x32, 0x0, 0x9, 0x0, 0x0)
    OP_1C(0x0, 0xA, 0x0, 0x32, 0x0, 0x9, 0x0, 0x0)
    LoadEffect(0x10, "event\\eva00_00.eff")
    Return()

    # Function_3_89F end

    def Function_4_DDD(): pass

    label("Function_4_DDD")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EDD")
    Sound(14, 0, 100, 0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('复苏药', 1)"), scpexpr(EXPR_END)), "loc_E66")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '复苏药'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1E0, 0)
    OP_E0(0x5, 0x0)
    Jump("loc_ED8")

    label("loc_E66")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            "In the treasure box",
            scpstr(SCPSTR_CODE_ITEM, '复苏药'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Is contained.\x01",
            "Because my belongings are full,",
            scpstr(SCPSTR_CODE_ITEM, '复苏药'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I gave up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x0, 0x1E, 0x0, 0x0, 0x0)

    label("loc_ED8")

    Jump("loc_F22")

    label("loc_EDD")

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

    label("loc_F22")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_DDD end

    def Function_5_F2E(): pass

    label("Function_5_F2E")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10FF")
    Sound(14, 0, 100, 0)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21A, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_102D")
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0xA, 0x0, 0)
    OP_98(0xA, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_F8B():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_F8B)

    def lambda_FA5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_FA5)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A monster appeared!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    WaitChrThread(0xA, 1)
    Battle("BattleInfo_6AC", 0x0, 0x0, 0x0, 0xB, 0xFF)
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xA, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_100E"),
        (2, "loc_101D"),
        (1, "loc_102A"),
        (SWITCH_DEFAULT, "loc_102D"),
    )


    label("loc_100E")

    SetScenarioFlags(0x21A, 6)
    OP_70(0x1, 0x1E)
    Sleep(500)
    Jump("loc_102D")

    label("loc_101D")

    OP_70(0x1, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_102A")

    OP_B9(0x0)
    Return()

    label("loc_102D")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('ＨＰ１', 1)"), scpexpr(EXPR_END)), "loc_108A")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 'ＨＰ１'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1E0, 1)
    OP_E0(0x5, 0x0)
    Jump("loc_10FA")

    label("loc_108A")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0x3E7,
        (
            "In the treasure box",
            scpstr(SCPSTR_CODE_ITEM, 'ＨＰ１'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Is contained.\x01",
            "Because my belongings are full,",
            scpstr(SCPSTR_CODE_ITEM, 'ＨＰ１'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I gave up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x1, 0x1E, 0x0, 0x0, 0x0)

    label("loc_10FA")

    Jump("loc_1139")

    label("loc_10FF")

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

    label("loc_1139")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_F2E end

    def Function_6_1145(): pass

    label("Function_6_1145")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1275")
    Sound(14, 0, 100, 0)
    OP_74(0x2, 0x1E)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    OP_70(0x2, 0x1E)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddSepith(0x0, 30)
    AddSepith(0x1, 30)
    AddSepith(0x2, 30)
    AddSepith(0x3, 30)
    AddSepith(0x4, 30)
    AddSepith(0x5, 30)
    AddSepith(0x6, 30)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#56ISepis of the earth × 30\x01\x07\x02",
            "#57IWater sepis × 30\x01\x07\x02",
            "#58IFire sepis × 30\x01\x07\x02",
            "#59IWind sepice × 30\x01\x07\x02",
            "#60ITime sepis × 30\x01\x07\x02",
            "#61IEmpty Sepis × 30\x01\x07\x02",
            "#62IPhantom Sepis × 30\x01\x07\x00",
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x1E0, 2)
    OP_E0(0x5, 0x0)
    Jump("loc_129A")

    label("loc_1275")


    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is nothing in the treasure box.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_129A")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_1145 end

    def Function_7_12AC(): pass

    label("Function_7_12AC")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13AC")
    Sound(14, 0, 100, 0)
    OP_74(0x3, 0x1E)
    OP_71(0x3, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('打火机', 1)"), scpexpr(EXPR_END)), "loc_1335")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '打火机'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1E0, 3)
    OP_E0(0x5, 0x0)
    Jump("loc_13A7")

    label("loc_1335")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            "In the treasure box",
            scpstr(SCPSTR_CODE_ITEM, '打火机'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Is contained.\x01",
            "Because my belongings are full,",
            scpstr(SCPSTR_CODE_ITEM, '打火机'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I gave up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x3, 0x1E, 0x0, 0x0, 0x0)

    label("loc_13A7")

    Jump("loc_13F1")

    label("loc_13AC")

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

    label("loc_13F1")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_12AC end

    def Function_8_13FD(): pass

    label("Function_8_13FD")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14FD")
    Sound(14, 0, 100, 0)
    OP_74(0x4, 0x1E)
    OP_71(0x4, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('痊愈之药', 1)"), scpexpr(EXPR_END)), "loc_1486")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '痊愈之药'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1E0, 4)
    OP_E0(0x5, 0x0)
    Jump("loc_14F8")

    label("loc_1486")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            "In the treasure box",
            scpstr(SCPSTR_CODE_ITEM, '痊愈之药'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Is contained.\x01",
            "Because my belongings are full,",
            scpstr(SCPSTR_CODE_ITEM, '痊愈之药'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I gave up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x4, 0x1E, 0x0, 0x0, 0x0)

    label("loc_14F8")

    Jump("loc_1542")

    label("loc_14FD")

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

    label("loc_1542")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_13FD end

    def Function_9_154E(): pass

    label("Function_9_154E")

    Call(1, 6)
    Return()

    # Function_9_154E end

    def Function_10_1552(): pass

    label("Function_10_1552")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_BF(0x0, 0x63)"), scpexpr(EXPR_EXEC_OP, "OP_BF(0x8, 0x63)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_157F")
    FadeToDark(500, 0, -1)
    OP_0D()
    TalkEnd(0xFE)
    EventBegin(0x0)
    OP_E2(0x3)
    Call(0, 14)
    Return()

    label("loc_157F")


    ChrTalk(
        0x8,
        (
            "#00603FFor each \"Enigma\"\x01",
            "Master Quartz I gave you now\x01",
            "Set it.\x02\x03",
            "#00600FFirst off from then.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_10_1552 end

    def Function_11_15EF(): pass

    label("Function_11_15EF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_BF(0x0, 0x63)"), scpexpr(EXPR_EXEC_OP, "OP_BF(0x8, 0x63)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_161C")
    FadeToDark(500, 0, -1)
    OP_0D()
    TalkEnd(0xFE)
    EventBegin(0x0)
    OP_E2(0x3)
    Call(0, 14)
    Return()

    label("loc_161C")


    ChrTalk(
        0x9,
        (
            "#01403FEven so, in this place\x01",
            "I will never step on … …\x02\x03",
            "#01400FAnyways--\x01",
            "I will detain two people as soon as possible.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_11_15EF end

    def Function_12_169A(): pass

    label("Function_12_169A")

    OP_F4(0x2)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There are devices that can recover the orbment.\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "To take a break here\x01",      # 0
            "quit\x01",              # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1787")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_74(0x7, 0x1E)
    Sound(7, 0, 100, 0)
    OP_70(0x7, 0x0)
    OP_71(0x7, 0x0, 0x1E, 0x0, 0x0)
    OP_79(0x7)
    OP_71(0x7, 0x1F, 0x186, 0x0, 0x20)
    Sleep(1000)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    Sound(13, 0, 100, 0)
    OP_0D()
    OP_32(0xFF, 0xFE, 0x0)
    OP_6A(0x0, 0x0)
    OP_31(0x1)
    Sleep(3500)
    OP_70(0x7, 0x0)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_1787")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_12_169A end

    def Function_13_1796(): pass

    label("Function_13_1796")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    LoadChrToIndex("apl/ch50011.itc", 0x1E)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis090.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis091.itp")
    CreatePortrait(2, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis230.itp")
    OP_68(3000, -7900, -6000, 0)
    MoveCamera(317, 36, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x101, 3000, -8000, -17200, 0)
    SetChrPos(0x10A, 4700, -8000, -18400, 0)
    SetChrPos(0x108, 1600, -8000, -18200, 0)
    SetChrPos(0x109, 3300, -8000, -19100, 0)
    OP_C9(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            "#30W──When we visited this place\x01",
            "Contact by the Imperial Government triggered me.\x02\x03",
            "A few months have gone by since the cult incident--\x02\x03",
            "I was confused by brawl and exiled to the empire\x01",
            "Former chairman Hartmann and former Mayor's secretary Ernesto\x01",
            "It was banished from the empire.\x02\x03",
            "For some reason, the two of us as a new hiding place\x01",
            "I chose Altair City at the westernmost point of the Republic ……\x02\x03",
            "In a hurry#4REmbarrassment#, By the new Mayor\x01",
            "Consultation with the republic government was kept secretly,\x01",
            "Two foreign arrests were to be executed.\x02\x03",
            "However, because it has extremely political problems,\x01",
            "Arrest is out of regular command system\x01",
            "It becomes a form to be left to \"the affairs support section\" … …\x02\x03",
            "In addition, the investigation division, the guard, the guild cooperate\x01",
            "An unusual investigation system was prepared.\x02\x03",
            "After several days investigating in Altair City\x02\x03",
            "We are both Hartmann and Ernest\x01",
            "I found out that I headed to the old lodge site of the cult.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x800)

    def lambda_1B96():
        OP_97(0x101, 0x0, 0x0, 0x4E20, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1B96)
    Sleep(100)

    def lambda_1BB3():
        OP_97(0x108, 0x0, 0x0, 0x4E20, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 0, lambda_1BB3)
    Sleep(100)

    def lambda_1BD0():
        OP_97(0x10A, 0x0, 0x0, 0x4E20, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_1BD0)
    Sleep(100)

    def lambda_1BED():
        OP_97(0x109, 0x0, 0x0, 0x4E20, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1BED)
    OP_68(3000, -7900, 6000, 7000)
    SetCameraDistance(35500, 7000)
    PlayBGM("ed7350", 0)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x15E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(129, 1, 100, 0)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)
    PlaceName2(340, 200, "c_plac50", 0x0, 0)
    OP_6F(0x79)
    Fade(500)
    OP_68(3000, -7000, 2500, 0)
    MoveCamera(323, 17, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(17000, 0)
    SetCameraDistance(15000, 3000)
    OP_0D()
    WaitChrThread(0x101, 0)
    OP_93(0x101, 0x2D, 0x190)
    Sleep(500)
    OP_93(0x101, 0x13B, 0x190)
    Sleep(750)
    OP_93(0x101, 0x0, 0x190)
    Sleep(300)
    OP_6F(0x79)
    Sound(2079, 255, 100, 0)

    ChrTalk(
        0x101,
        "#00005F#30WThis is…\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    WaitChrThread(0x109, 0)
    Sleep(150)

    ChrTalk(
        0x109,
        (
            "#6P#10108FIs it a limestone cave …?\x01",
            "But, there are people's hands in hand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#01403FOriginally used hundreds of years ago\x01",
            "It seems it was a cave temple trace.\x02\x03",
            "It was repaired by \"D∴G Church\"\x01",
            "We used it as a \"liturgy\" lodge.\x02\x03",
            "#01401FUntil that day six years ago.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(1000)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    Sleep(500)

    AnonymousTalk(
        0x101,
        (
            "#00006F…… The section chief and Arios,\x01",
            "And it is when my older brother suppressed it.\x02\x03",
            "#00001FAnd the big brother here, only one person\x01",
            "I rescued the surviving Tio … …\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x108,
        (
            "#01403FOh, honestly that's it.\x01",
            "In a disaster like that hell\x01",
            "It was the only consolation.\x02\x03",
            "#01400FNow also its traces\x01",
            "It is almost gone.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x101,
        "#00008F……………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(300)

    ChrTalk(
        0x109,
        (
            "#6P#10106FI can not believe it …\x01",
            "It was such a thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#6P#00603FHun, everywhere\x01",
            "It seems they were the worst guys.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10A, 0x108, 500)
    Sleep(300)

    ChrTalk(
        0x10A,
        (
            "#12P#00600FAt that time, the republican army could not move\x01",
            "Some officers have a weak flavor to cults\x01",
            "It seems to be because it was held … …?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x108, 0x10A, 500)

    ChrTalk(
        0x108,
        (
            "#01402F#5POh, that is why I'm in Sergei\x01",
            "That is why I was given control of this place.\x02\x03",
            "#01404FFor now,\x01",
            "The guild is also said to be pure blue\x01",
            "It was a brute force way of intervention.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#12P#00602FHun, truly a bad name\x01",
            "Is it such as the Sergei group?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(150)

    ChrTalk(
        0x101,
        (
            "#11P#00004FHaha … … something at the time the sight\x01",
            "I feel that it appears to the eyes.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x108, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#11P#00001F── Arios.\x01",
            "If two people are going\x01",
            "Where is the lodge?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_21FB():
        TurnDirection(0xFE, 0x108, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_21FB)
    Sleep(100)

    ChrTalk(
        0x108,
        (
            "#01403F#5PStill in the back\x01",
            "The possibility of \"during the ceremony\" is high.\x02\x03",
            "It seems that it was in \"Fort of the Sun\"\x01",
            "A mysterious altar is left.\x02\x03",
            "#01401FApart from Hartmann ……\x01",
            "Even though Ernest aims for that\x01",
            "It is not surprising.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#00003FThat's true…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10113FPossibly,\x01",
            "That medicine \"Gnostic\" is also\x01",
            "Is it related?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#12P#00606FWe can't deny that possibility.\x02\x03",
            "Apparently Ernst is\x01",
            "\"Gnostic\" from Joachim\x01",
            "It seems that it received as it was.\x02\x03",
            "#00601FAnd it wasn't the blue pills, but the red ones, to make matters worse\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x109, 0x10A, 600)

    ChrTalk(
        0x109,
        (
            "#5P#10107FWell, that is ….\x01",
            "It turns people into things! Is it?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x109, 500)

    ChrTalk(
        0x101,
        (
            "#11P#00003FOh, in some cases\x01",
            "The body of Hartmann who is accompanying\x01",
            "It may be dangerous.\x02\x03",
            "#00001FBefore the repatriation ceases\x01",
            "Let's detain two people at all costs.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x101, 500)

    ChrTalk(
        0x109,
        (
            "#6P#10101FRight!\x02\x03",
            "#10106FAhh, but this is a problem..\x02\x03",
            "At such timing\x01",
            "Enigma's version upgrade\x01",
            "I can not do it …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#00006FI know, right?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    Sleep(500)

    ChrTalk(
        0x101,
        "#11P#00001F\"Enigma 嘦\" ……\x02",
    )

    CloseMessageWindow()
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)
    Sleep(300)

    AnonymousTalk(
        0x109,
        (
            "#10108FIt puts it in the center.\x01",
            "New type \"Master Quartz\" … …\x02\x03",
            "Because it did not make it.\x01",
            "After all, we are in a state where we can not use Arts.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x101,
        (
            "#00006FEpstein foundation every time\x01",
            "Switching too suddenly.\x02\x03",
            "Tio's place of belonging\x01",
            "I do not want to say it badly ….\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x10A,
        (
            "#00603FHun, how much is the timing\x01",
            "Even though it is bad, do not break whine.\x02\x03",
            "#00600FIf you are prepared properly\x01",
            "I will be able to prepare this much.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)

    def lambda_27CE():
        OP_9A(0xFE, 0x101, 0x384, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_27CE)
    WaitChrThread(0x10A, 1)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    TurnDirection(0x101, 0x10A, 500)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '力量'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Got FORCE from Dudley\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('力量', 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        "#00005FUh…\x02",
    )

    CloseMessageWindow()

    def lambda_285F():
        OP_96(0xFE, 0x125C, 0xFFFFE0C0, 0x640, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_285F)

    ChrTalk(
        0x108,
        (
            "#01404F#5PHuh, if you're also from me\x01",
            "Let's provide one spare.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_28B8():
        OP_9A(0xFE, 0x109, 0x384, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_28B8)
    WaitChrThread(0x108, 1)
    TurnDirection(0x109, 0x108, 500)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '盾牌'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Got FORCE from Dudley\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('盾牌', 1)
    SetMessageWindowPos(14, 280, 60, 3)

    def lambda_2924():
        OP_96(0xFE, 0x640, 0xFFFFE0C0, 0x708, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_2924)
    WaitChrThread(0x108, 1)
    WaitChrThread(0x10A, 1)

    ChrTalk(
        0x109,
        (
            "#12P#10105Fthis……\x01",
            "Is it Master Quartz?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FYou're letting us have these…?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#12P#00601FHun, in your feet\x01",
            "It's just a matter of being embarrassed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#01402F#5PIn the center of \"Enigma 嘦\"\x01",
            "You can set whichever you like.\x02\x03",
            "As soon as both are attached\x01",
            "You should be able to use multiple arts.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x108, 600)

    ChrTalk(
        0x101,
        "#11P#00002FRoger!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10102FUnderstood!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    Sound(814, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※ The new type of \"enigma 嘦\"\x01",
            "Master quartz in the middle slot\x01",
            "It can be set.\x02\x03",
            "※ Open [ORBMENT] from the camp menu,\x01",
            "By selecting [QUARTZ]\x01",
            "You can set master quartz.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(100)
    OP_D7(0x1E)
    OP_37()
    OP_CC(0x1, 0xFF, 0x0)
    OP_32(0xFF, 0xF9, 0x0)
    RemoveParty(0x9, 0x0)
    RemoveParty(0x7, 0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x0, 2460, -8000, -200, 180)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x120, 0)
    OP_29(0xA0, 0x4, 0x2)
    OP_29(0xA0, 0x1, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BE2")
    SetScenarioFlags(0x21, 0)

    label("loc_2BE2")

    OP_E2(0x2)
    Sleep(400)
    EventEnd(0x5)
    Return()

    # Function_13_1796 end

    def Function_14_2BEA(): pass

    label("Function_14_2BEA")

    AddParty(0x9, 0xFF, 0xFF)
    AddParty(0x7, 0xFF, 0xFF)
    OP_37()
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    OP_68(3000, -7000, 2500, 0)
    MoveCamera(323, 17, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(15000, 0)
    SetChrPos(0x101, 3000, -8000, 2800, 180)
    SetChrPos(0x10A, 4700, -8000, 1600, 270)
    SetChrPos(0x108, 1600, -8000, 1800, 90)
    SetChrPos(0x109, 3300, -8000, 900, 0)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu00001.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu10100.itp")
    CreatePortrait(2, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu00600.itp")
    CreatePortrait(3, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu01400.itp")
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x10A,
        "#12P#00600FGood, so preparations are complete?\x02",
    )

    CloseMessageWindow()

    def lambda_2D51():
        TurnDirection(0xFE, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2D51)
    Sleep(100)

    def lambda_2D61():
        TurnDirection(0xFE, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_2D61)
    WaitChrThread(0x101, 2)

    ChrTalk(
        0x101,
        (
            "#00000FYes, sorry for the wait.\x02\x03",
            "#00002FThat……\x01",
            "Have you bother to prepare\x01",
            "It really helped me.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(2558, 255, 100, 0)
    Sleep(100)
    OP_63(0x10A, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(800)

    ChrTalk(
        0x10A,
        (
            "#12P#00605FBeside, for you\x01",
            "I did not prepare.\x02\x03",
            "#00606FBannings than that.\x01",
            "You know what I mean?\x02\x03",
            "#00601FThis mission is for you\x01",
            "It is also the finish of the training in one department.\x02\x03",
            "#00607FIn case of emergency#2RFurther#if you do\x01",
            "Keep it in mind as you redo!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(3317, 255, 100, 0)

    ChrTalk(
        0x101,
        "#00000F#30WRoger..!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10112F#6P(Haha ……\x01",
            "He is not a honest person. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#01404F#5P(Hu, than it looks\x01",
            "It's a much hotter tough man. )\x02\x03",
            "#01402F(… with Guy in one department\x01",
            "There seems to be a competing match. )\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0xB4, 0x1F4)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x101,
        "Alright, let's do it.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)

    def lambda_3071():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_3071)
    Sleep(50)

    def lambda_3081():

        label("loc_3081")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_3081")

    QueueWorkItem2(0x10A, 2, lambda_3081)
    Sleep(50)

    def lambda_3096():

        label("loc_3096")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_3096")

    QueueWorkItem2(0x108, 2, lambda_3096)
    WaitChrThread(0x109, 2)
    OP_93(0x101, 0x0, 0x1F4)

    def lambda_30B3():
        OP_98(0xFE, 0x0, 0x0, 0x7D0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_30B3)
    Sleep(500)
    Fade(500)
    OP_68(3000, -7100, 3900, 0)
    MoveCamera(0, 19, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14500, 0)
    SetCameraDistance(15500, 1500)
    SetChrPos(0x10A, 4500, -8000, 1600, 270)
    SetChrPos(0x108, 1500, -8000, 1600, 90)
    SetChrPos(0x109, 3000, -8000, 900, 0)
    OP_0D()
    WaitChrThread(0x101, 1)
    EndChrThread(0x10A, 0x2)
    EndChrThread(0x108, 0x2)
    OP_93(0x101, 0xB4, 0x1F4)
    OP_6F(0x79)
    Sleep(150)

    ChrTalk(
        0x101,
        (
            "#00003FCrossbell Police, belonging to investigation department 1,\x01",
            "Alex Dudley Chief Investigator.\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(150)
    Sound(4115, 255, 100, 0)

    AnonymousTalk(
        0x10A,
        "#30WYes.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)

    ChrTalk(
        0x101,
        (
            "#00000FCrossbell Guard belongs,\x01",
            "Noel Seoker, sergeant.\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(150)
    Sound(3514, 255, 100, 0)

    AnonymousTalk(
        0x109,
        "#30WRoger!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)

    ChrTalk(
        0x101,
        (
            "#00004FAnd as special assistant\x01",
            "Association of Association of Shogunsha Associations Crossbell Section affiliation,\x01",
            "Arios McClein.\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x3, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x3, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x3, 0x3)
    OP_CC(0x0, 0x3, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(150)
    Sound(4022, 255, 100, 0)

    AnonymousTalk(
        0x108,
        "#30WYes.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x3, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x3, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x3, 0x3)
    OP_CC(0x0, 0x3, 0x0)

    ChrTalk(
        0x101,
        (
            "#00003FFrom this, Crossbell Police,\x01",
            "Forced search by the Special Affairs Support Division,\x01",
            "And the arresting mission.\x02\x03",
            "#00013FThe subjects of arrest are former Hartmann chairman,\x01",
            "And Ernest former mayor's secretary.\x02\x03",
            "#00007FThe deadline today is 17: 00 -\x01",
            "Please do your best with everyone!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    Sound(2506, 255, 100, 0)

    ChrTalk(
        0x10A,
        "#00607F#12PAlright!\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    Sound(4024, 255, 100, 1)

    ChrTalk(
        0x108,
        "#01407F#6PUnderstood!\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    Sound(2481, 255, 100, 2)

    ChrTalk(
        0x109,
        "#6P#10107F#6PRoger that!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    Sound(814, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "About the investigator notebook\x02\x03",
            "* \"Investigation notebook\"\x01",
            "Various events that occurred during the game\x01",
            "It will be recorded automatically.\x02\x03",
            "* Open [ITEMS] from the camp menu\x01",
            "Use \"investigation notebook\"\x01",
            "With \"△ button + direction key left\" on the field\x01",
            "You can see the contents.\x02\x03",
            "* Since you can also check the manual etc.,\x01",
            "Please use it.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Sound(814, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "About the battle notebook\x02\x03",
            "※ \"Battle notebook\"\x01",
            "The information of the opponent who fought in battle\x01",
            "It will be recorded automatically.\x02\x03",
            "※ As with the investigation notebook,\x01",
            "Using the item's \"Battle Diary\"\x01",
            "Or press \"△ button + direction key right\"\x01",
            "You can see the contents.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrPos(0x0, 3000, -8000, 0, 0)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x120, 1)
    OP_29(0xA0, 0x1, 0x1)
    ModifyEventFlags(0, 0, 0x80)
    OP_CC(0x1, 0xFF, 0x0)
    OP_E2(0x2)
    OP_E0(0x19, 0x0)
    Sleep(300)
    OP_E0(0x80, 0x0)
    EventEnd(0x5)
    Return()

    # Function_14_2BEA end

    def Function_15_37F8(): pass

    label("Function_15_37F8")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    SoundLoad(814)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis091.itp")
    OP_68(164900, -3800, -2200, 0)
    MoveCamera(325, 24, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17000, 0)
    SetChrPos(0x101, 169900, -5000, -2200, 270)
    SetChrPos(0x109, 172300, -5000, -2200, 270)
    SetChrFlags(0x109, 0x40)
    SetChrPos(0x10A, 171300, -5000, -1100, 270)
    SetChrPos(0x108, 171300, -5000, -3300, 270)

    def lambda_38B1():
        OP_97(0x101, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_38B1)
    Sleep(50)

    def lambda_38CE():
        OP_97(0x108, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 0, lambda_38CE)
    Sleep(50)

    def lambda_38EB():
        OP_97(0x10A, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_38EB)
    Sleep(50)

    def lambda_3908():
        OP_97(0x109, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3908)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x101, 0)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    WaitChrThread(0x10A, 0)
    OP_63(0x10A, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    WaitChrThread(0x109, 0)
    ClearChrFlags(0x109, 0x40)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x109,
        "#12P#10105FIs this…\x02",
    )

    CloseMessageWindow()
    OP_68(147900, -2800, -2200, 3500)
    MoveCamera(303, 17, 0, 3500)
    SetCameraDistance(25000, 3500)
    Sleep(500)

    def lambda_39BF():
        OP_97(0x101, 0xFFFFD8F0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_39BF)
    Sleep(100)

    def lambda_39DC():
        OP_97(0x108, 0xFFFFD8F0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 0, lambda_39DC)
    Sleep(100)

    def lambda_39F9():
        OP_97(0x10A, 0xFFFFD8F0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_39F9)
    Sleep(100)

    def lambda_3A16():
        OP_97(0x109, 0xFFFFD8F0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3A16)
    OP_6F(0x79)
    Sleep(1000)
    Fade(500)
    OP_68(154400, -3700, -2200, 0)
    MoveCamera(325, 24, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(18500, 0)
    SetCameraDistance(17500, 1500)
    OP_0D()
    WaitChrThread(0x109, 0)
    OP_6F(0x79)
    TurnDirection(0x101, 0x108, 500)

    ChrTalk(
        0x101,
        "#00010F#5PArios is this…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#6P#01403FAh……\x01",
            "\"Sensitivity#4RFight#Power Reinforcement Experiment \".\x02\x03",
            "#01401FChildren who received Gnostic\x01",
            "Five senses and inspiration in all sorts of ways\x01",
            "It was a victim of an experiment to raise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        "#00608FTch… Damn heretics \x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10110FThe D∴G Cult…\x02\x03",
            "#10103FI guess it was already crushed\x01",
            "To be honest, I can not forgive ……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x10E, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        "#00008F#11P………….\x02",
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(1000)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)

    ChrTalk(
        0x101,
        (
            "#00003F#11P… … Ernest\x01",
            "What are you trying to do?\x01",
            "I do not know but …\x02\x03",
            "#00001FOnce again, this place will be used\x01",
            "I can not afford it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        "#6P#01403FYes. Of course.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#4P#10107FLet's stop them at any cost!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        "#00607FAlright, let's move forward!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    Sound(814, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "About Monster Analysis\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※ other than Dudley with quartz \"information\"\x01",
            "The character can not see the monster's information.\x02\x03",
            "※ However the item \"Battle Scope\" and\x01",
            "Using auxiliary arts \"Analyze\" with phantom attribute\x01",
            "You can acquire information on monsters and enemies.\x02\x03",
            "Attributes of Arts that the monsters are not good at\x01",
            "To know what kind of condition anomaly works\x01",
            "It will be possible to fight efficiently.\x02\x03",
            "※ The information on the acquired monsters and enemies\x01",
            "If it is the same type, move the cursor to\x01",
            "You can check it at any time by pressing \"□ button\".\x02\x03",
            "※ By the way auxiliary anatom \"Analyze\"\x01",
            "At present it is possible for Dudley to use.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(100)
    OP_CC(0x1, 0xFF, 0x0)
    SetChrPos(0x0, 155000, -5000, -2200, 270)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x120, 2)
    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_15_37F8 end

    def Function_16_3FC4(): pass

    label("Function_16_3FC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x120, 3)), scpexpr(EXPR_END)), "loc_404A")
    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The rock door is closed up.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x108,
        (
            "#01400F- There is a switch in the back of the right hand.\x01",
            "I will head for the release in a hurry.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Return()

    label("loc_404A")

    EventBegin(0x0)
    OP_E2(0x3)
    Fade(500)
    OP_68(1100, 1300, 77900, 0)
    MoveCamera(320, 24, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(19500, 0)
    SetChrPos(0x101, 1100, 0, 77900, 270)
    SetChrPos(0x109, 2800, 0, 76300, 270)
    SetChrPos(0x10A, 3400, 0, 77400, 270)
    SetChrPos(0x108, 3300, 0, 78900, 230)
    OP_0D()

    ChrTalk(
        0x101,
        "#11P#00005FThis is…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10105FA stone door?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#01401F#4PIt's a gate that goes to the back.\x01",
            "It should have been released six years ago … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#12P#00603FHun and Ernest per it\x01",
            "Perhaps he or she may have tried again.\x02\x03",
            "#00600FAny way to open it?\x02",
        )
    )

    CloseMessageWindow()
    OP_68(2500, 1300, 79260, 1000)
    OP_93(0x108, 0x5A, 0x190)
    OP_6F(0x1)

    ChrTalk(
        0x108,
        (
            "#5P#01400FThere is a switch in the back of the right hand.\x01",
            "You should open it.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_420A():
        OP_93(0x101, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_420A)
    Sleep(50)

    def lambda_421A():
        OP_93(0x10A, 0x32, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_421A)
    Sleep(50)

    def lambda_422A():
        OP_93(0x109, 0x32, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_422A)
    Sleep(50)
    WaitChrThread(0x10A, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x101, 1)

    ChrTalk(
        0x101,
        "#00001F#5POk let's check it out\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x120, 3)
    SetChrPos(0x0, 2100, 0, 77900, 90)
    OP_69(0xFF, 0x0)
    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_16_3FC4 end

    def Function_17_4287(): pass

    label("Function_17_4287")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x120, 4)), scpexpr(EXPR_END)), "loc_42C9")
    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It does not seem to move anymore.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapFlags(0x8000000)
    EventEnd(0x3)
    Jump("loc_442B")

    label("loc_42C9")

    EventBegin(0x1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a switch.\x01",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4424")
    Fade(500)
    OP_68(36110, 4130, 221300, 0)
    MoveCamera(0, 38, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(18000, 0)
    SetChrPos(0x0, 36200, 2830, 221010, 360)
    SetChrPos(0x1, 37050, 2320, 219590, 360)
    SetChrPos(0x2, 35320, 2330, 219560, 360)
    SetChrPos(0x3, 36200, 2009, 218660, 360)
    OP_0D()
    Sleep(500)
    Sound(143, 0, 100, 0)
    OP_71(0x6, 0x0, 0x14, 0x0, 0x0)
    Sleep(1000)
    Fade(500)
    OP_68(-1090, 1360, 78640, 0)
    MoveCamera(291, 30, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(19000, 0)
    OP_0D()
    Sleep(500)
    Sound(155, 2, 100, 0)
    OP_74(0x5, 0xF)
    OP_71(0x5, 0x0, 0x14, 0x0, 0x0)
    Sleep(1300)
    OP_24(0x9B)
    Sound(149, 0, 100, 0)
    OP_82(0x64, 0x0, 0x3E8, 0x64)
    Sleep(1000)
    SetScenarioFlags(0x120, 4)
    OP_65(0x0, 0x1)

    label("loc_4424")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)

    label("loc_442B")

    Return()

    # Function_17_4287 end

    def Function_18_442C(): pass

    label("Function_18_442C")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_449E")

    ChrTalk(
        0x101,
        (
            "#00003FI can not turn back.\x02\x03",
            "#00001FAnyhow, Ernest\x01",
            "I have to catch it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_45A5")

    label("loc_449E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_44FC")

    ChrTalk(
        0x109,
        (
            "#10101FIn such a place\x01",
            "I can not stay -\x01",
            "I have to aim for the back in a hurry.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_45A5")

    label("loc_44FC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4559")

    ChrTalk(
        0x10A,
        (
            "#00603FErnesto and Hartmann are back.\x01",
            "- I will chase after quickly.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_45A5")

    label("loc_4559")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_45A5")

    ChrTalk(
        0x108,
        (
            "#01401FThere is no time to turn back.\x01",
            "- I will hurry and follow you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_45A5")

    SetChrPos(0x0, 2860, -8000, -8020, 0)
    EventEnd(0x4)
    Return()

    # Function_18_442C end

    def Function_19_45B9(): pass

    label("Function_19_45B9")

    EventBegin(0x1)
    OP_4B(0x8, 0xFF)
    TurnDirection(0x8, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#00603FBannings,\x01",
            "Where am I supposed to go?\x02\x03",
            "#00601FArbitrary actions are acceptable.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        "#00003FI'm sorry, I will prepare it soon.\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x0, 2430, -8000, 3380, 180)
    OP_93(0x8, 0x5A, 0x0)
    OP_4C(0x8, 0xFF)
    EventEnd(0x4)
    Return()

    # Function_19_45B9 end

    SaveToFile()

Try(main)
