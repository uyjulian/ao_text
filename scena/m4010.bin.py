from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "Detective Dudley",       # 1
        "Arios",                  # 2
        "Dinosaur",               # 3
        "bm4010",                 # 4
        "bm4010",                 # 5
        "bm4010",                 # 6
        "bm4010",                 # 7
    ))

    ATBonus("ATBonus_460", 100, 5, 1, 5, 1, 5, 1, 5, 5, 5, 5, 5, 5, 0, 0, 0)
    ATBonus("ATBonus_470", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    Sepith("Sepith_49CF", 2,   2,   0,   2,   2,   2,   1)
    Sepith("Sepith_49C7", 0,   4,   0,   4,   1,   1,   1)
    Sepith("Sepith_49BF", 3,   4,   5,   2,   0,   0,   0)

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
        "BattleInfo_610", 0x0000, 46, 6, 45, 6, 1, 40, 0, "bm4010", "Sepith_49CF", 60, 25, 10, 0,
        (
            ("ms83800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_490", "MonsterBattlePostion_510", "ed7450", "ed7453", "ATBonus_460"),
            ("ms83800.dat", "ms83800.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_490", "MonsterBattlePostion_510", "ed7450", "ed7453", "ATBonus_460"),
            ("ms83800.dat", "ms83800.dat", "ms83800.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_4B0", "MonsterBattlePostion_510", "ed7450", "ed7453", "ATBonus_460"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_574", 0x0000, 46, 6, 60, 6, 1, 20, 0, "bm4010", "Sepith_49C7", 60, 25, 10, 0,
        (
            ("ms83600.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_490", "MonsterBattlePostion_510", "ed7450", "ed7453", "ATBonus_460"),
            ("ms83600.dat", "ms83600.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_490", "MonsterBattlePostion_510", "ed7450", "ed7453", "ATBonus_460"),
            ("ms83600.dat", "ms83600.dat", "ms83600.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_4B0", "MonsterBattlePostion_510", "ed7450", "ed7453", "ATBonus_460"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_530", 0x0000, 46, 6, 45, 6, 1, 40, 0, "bm4010", "Sepith_49BF", 100, 0, 0, 0,
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
        "Function_6_1149",         # 06, 6
        "Function_7_12B2",         # 07, 7
        "Function_8_1403",         # 08, 8
        "Function_9_1554",         # 09, 9
        "Function_10_1558",        # 0A, 10
        "Function_11_15F5",        # 0B, 11
        "Function_12_16B8",        # 0C, 12
        "Function_13_17AC",        # 0D, 13
        "Function_14_2D76",        # 0E, 14
        "Function_15_3A56",        # 0F, 15
        "Function_16_426F",        # 10, 16
        "Function_17_4581",        # 11, 17
        "Function_18_4720",        # 12, 18
        "Function_19_48C7",        # 13, 19
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_ED9")
    Sound(14, 0, 100, 0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1FB, 1)"), scpexpr(EXPR_END)), "loc_E62")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1FB),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1E0, 0)
    OP_E0(0x5, 0x0)
    Jump("loc_ED4")

    label("loc_E62")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1FB),
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

    label("loc_ED4")

    Jump("loc_F22")

    label("loc_ED9")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21A, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1031")
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
            "Monsters appeared!\x07\x00\x02",
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
        (0, "loc_1012"),
        (2, "loc_1021"),
        (1, "loc_102E"),
        (SWITCH_DEFAULT, "loc_1031"),
    )


    label("loc_1012")

    SetScenarioFlags(0x21A, 6)
    OP_70(0x1, 0x1E)
    Sleep(500)
    Jump("loc_1031")

    label("loc_1021")

    OP_70(0x1, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_102E")

    OP_B9(0x0)
    Return()

    label("loc_1031")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x64, 1)"), scpexpr(EXPR_END)), "loc_108A")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x64),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x64),
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

    label("loc_10FA")

    Jump("loc_113D")

    label("loc_10FF")

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

    label("loc_113D")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_F2E end

    def Function_6_1149(): pass

    label("Function_6_1149")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1282")
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
            "#56I Earth Sepith  x30\x01\x07\x02",
            "#57I Water Sepith  x30\x01\x07\x02",
            "#58I Fire Sepith   x30\x01\x07\x02",
            "#59I Wind Sepith   x30\x01\x07\x02",
            "#60I Time Sepith   x30\x01\x07\x02",
            "#61I Space Sepith  x30\x01\x07\x02",
            "#62I Mirage Sepith x30\x01\x07\x00",
            "obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x1E0, 2)
    OP_E0(0x5, 0x0)
    Jump("loc_12A0")

    label("loc_1282")


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

    label("loc_12A0")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_1149 end

    def Function_7_12B2(): pass

    label("Function_7_12B2")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13AE")
    Sound(14, 0, 100, 0)
    OP_74(0x3, 0x1E)
    OP_71(0x3, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x41, 1)"), scpexpr(EXPR_END)), "loc_1337")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x41),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1E0, 3)
    OP_E0(0x5, 0x0)
    Jump("loc_13A9")

    label("loc_1337")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x41),
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
    OP_71(0x3, 0x1E, 0x0, 0x0, 0x0)

    label("loc_13A9")

    Jump("loc_13F7")

    label("loc_13AE")

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

    label("loc_13F7")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_12B2 end

    def Function_8_1403(): pass

    label("Function_8_1403")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14FF")
    Sound(14, 0, 100, 0)
    OP_74(0x4, 0x1E)
    OP_71(0x4, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x20B, 1)"), scpexpr(EXPR_END)), "loc_1488")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x20B),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1E0, 4)
    OP_E0(0x5, 0x0)
    Jump("loc_14FA")

    label("loc_1488")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x20B),
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
    OP_71(0x4, 0x1E, 0x0, 0x0, 0x0)

    label("loc_14FA")

    Jump("loc_1548")

    label("loc_14FF")

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

    label("loc_1548")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_1403 end

    def Function_9_1554(): pass

    label("Function_9_1554")

    Call(1, 6)
    Return()

    # Function_9_1554 end

    def Function_10_1558(): pass

    label("Function_10_1558")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_BF(0x0, 0x63)"), scpexpr(EXPR_EXEC_OP, "OP_BF(0x8, 0x63)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1585")
    FadeToDark(500, 0, -1)
    OP_0D()
    TalkEnd(0xFE)
    EventBegin(0x0)
    OP_E2(0x3)
    Call(0, 14)
    Return()

    label("loc_1585")


    ChrTalk(
        0x8,
        (
            "#00603FSet the master quartz we\x01",
            "just gave you in each of\x01",
            "your ENIGMA Ⅱs.\x02\x03",
            "#00600FWe'll go from there.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_10_1558 end

    def Function_11_15F5(): pass

    label("Function_11_15F5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_BF(0x0, 0x63)"), scpexpr(EXPR_EXEC_OP, "OP_BF(0x8, 0x63)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1622")
    FadeToDark(500, 0, -1)
    OP_0D()
    TalkEnd(0xFE)
    EventBegin(0x0)
    OP_E2(0x3)
    Call(0, 14)
    Return()

    label("loc_1622")


    ChrTalk(
        0x9,
        (
            "#01403FTo think I'd set foot in\x01",
            "this place again after\x01",
            "what happened...\x02\x03",
            "#01400FAt any rate, let's\x01",
            "capture those two as\x01",
            "quickly as possible.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_11_15F5 end

    def Function_12_16B8(): pass

    label("Function_12_16B8")

    OP_F4(0x2)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's an orbment charging station.\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Rest Here\x01",      # 0
            "Cancel\x01",         # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_179D")
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

    label("loc_179D")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_12_16B8 end

    def Function_13_17AC(): pass

    label("Function_13_17AC")

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
            "#30W─We're here because we were contacted by the\x01",
            "Imperial government.\x02\x03",
            "A couple of months after the incident with the\x01",
            "Cult─\x02\x03",
            "Former Chairman Hartmann and the mayor's\x01",
            "secretary, Ernest, were exiled from the Empire\x01",
            "after a failed attempt to seek asylum there.\x02\x03",
            "For reasons unknown, they found a new hideout in\x01",
            "Altair City on Calvard's western border.\x02\x03",
            "On short notice, Crossbell's new mayor discussed\x01",
            "the matter with the Republican government in\x01",
            "secret and ordered the apprehension of the two.\x02\x03",
            "However, due to growing political constraints, the\x01",
            "mission to apprehend the criminals was officially\x01",
            "entrusted to the Special Support Section.\x02\x03",
            "Cooperation with Section One, the Guardian Force,\x01",
            "and the guild led to a highly unusual\x01",
            "investigation team.\x02\x03",
            "Then, after several days investigating in Altair\x01",
            "City─\x02\x03",
            "We determined that both Hartmann and Ernest headed\x01",
            "for the site of an old cult lodge.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x800)

    def lambda_1C5E():
        OP_97(0x101, 0x0, 0x0, 0x4E20, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1C5E)
    Sleep(100)

    def lambda_1C7B():
        OP_97(0x108, 0x0, 0x0, 0x4E20, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 0, lambda_1C7B)
    Sleep(100)

    def lambda_1C98():
        OP_97(0x10A, 0x0, 0x0, 0x4E20, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_1C98)
    Sleep(100)

    def lambda_1CB5():
        OP_97(0x109, 0x0, 0x0, 0x4E20, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1CB5)
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
        "#00005F#30WThis is...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    WaitChrThread(0x109, 0)
    Sleep(150)

    ChrTalk(
        0x109,
        (
            "#6P#10108FA limestone cave...?\x01",
            "But, there's traces of\x01",
            "human activity.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#01403FThis place was originally used\x01",
            "as a temple, some centuries\x01",
            "ago.\x02\x03",
            "The D∴G Cult remodeled the\x01",
            "place and used it as a lodge in\x01",
            "which to hold their Rituals.\x02\x03",
            "#01401FUntil that day 6 years ago.\x02",
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
            "#00006F...The raid you\x01",
            "conducted with chief and\x01",
            "my brother, right?\x02\x03",
            "#00001FAnd when my brother\x01",
            "managed to rescue the\x01",
            "sole survivor, Tio...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x108,
        (
            "#01403FYeah. That was the only ray of\x01",
            "sunlight within the never-ending\x01",
            "hell we witnessed that day.\x02\x03",
            "#01400FThere's hardly any traces of it\x01",
            "left now, though.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x101,
        "#00008F...............\x02",
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
            "#6P#10106FI still can't believe\x01",
            "those horrible things\x01",
            "happened...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#6P#00603FHmph. They really were\x01",
            "the scum of the world.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10A, 0x108, 500)
    Sleep(300)

    ChrTalk(
        0x10A,
        (
            "#12P#00600FI heard the Republican forces' hands\x01",
            "were tied because the cult had dirt on\x01",
            "some of its officers. Is that right?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x108, 0x10A, 500)

    ChrTalk(
        0x108,
        (
            "#01402F#5PYeah, that's why the raid\x01",
            "was left to Sergei's squad.\x02\x03",
            "#01404FIn retrospect, it was more\x01",
            "like a forceful intervention\x01",
            "of the Bracer Guild.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#12P#00602FHmph. As expected of\x01",
            "Sergei's infamous squad.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(150)

    ChrTalk(
        0x101,
        (
            "#11P#00004FHaha... I can imagine\x01",
            "what that day must've\x01",
            "been like.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x108, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#11P#00001F...Arios. Assuming those\x01",
            "two are here, where in\x01",
            "the lodge might they be?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_231A():
        TurnDirection(0xFE, 0x108, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_231A)
    Sleep(100)

    ChrTalk(
        0x108,
        (
            "#01403F#5PMost likely the Ritual\x01",
            "Chamber, deep within the\x01",
            "lodge.\x02\x03",
            "There's a mysterious altar\x01",
            "similar to the one in the\x01",
            "Fort of Sun there.\x02\x03",
            "#01401FI don't know about Hartmann,\x01",
            "but I'm sure that's where\x01",
            "Ernest would be heading.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#00003F...Indeed.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10113FBy the way, do you think\x01",
            "that what they're up to is\x01",
            "related to that Gnosis drug?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#12P#00606FWe cannot deny that\x01",
            "possibility.\x02\x03",
            "It appears that Ernest\x01",
            "received a fair amount of\x01",
            "said drug from Joachim.\x02\x03",
            "#00601FAnd to make matters\x01",
            "worse, it was the crimson\x01",
            "type, not the azure one.\x02",
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
            "#5P#10107FBut t-that's... That's\x01",
            "the one that turns\x01",
            "people into demons!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x109, 500)

    ChrTalk(
        0x101,
        (
            "#11P#00003FYeah, and if that's the\x01",
            "case, Hartmann may be in\x01",
            "danger as well.\x02\x03",
            "#00001FWe have to arrest them\x01",
            "before they're too far\x01",
            "gone.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x101, 500)

    ChrTalk(
        0x109,
        (
            "#6P#10101FRight!\x02\x03",
            "#10106FAhh, but this is a\x01",
            "problem...\x02\x03",
            "I wasn't really expecting to\x01",
            "get an upgraded ENIGMA right\x01",
            "before this mission...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#00006F*sigh*, that's right.\x02",
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
        "#11P#00001FThe ENIGMA Ⅱ, huh.\x02",
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
            "#10108FIn the center, we insert\x01",
            "these new "Master\x01",
            "Quartz"?\x02\x03",
            "If these didn't arrive in\x01",
            "time, we wouldn't have\x01",
            "been able to use arts.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x101,
        (
            "#00006FI don't want to badmouth\x01",
            "the place where Tio\x01",
            "works, of course, but...\x02\x03",
            "Once again, the Epstein\x01",
            "Foundation is late with\x01",
            "announcing upgrades...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x10A,
        (
            "#00603FHmph. Don't forget that the\x01",
            "timing could have been much\x01",
            "worse.\x02\x03",
            "#00600FWe still have time to\x01",
            "prepare ourselves, so you're\x01",
            "in no position to complain.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)

    def lambda_2989():
        OP_9A(0xFE, 0x101, 0x384, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_2989)
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
            scpstr(SCPSTR_CODE_ITEM, 0xDC),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " received.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0xDC, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        "#00005FWhoa...\x02",
    )

    CloseMessageWindow()

    def lambda_2A17():
        OP_96(0xFE, 0x125C, 0xFFFFE0C0, 0x640, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_2A17)

    ChrTalk(
        0x108,
        (
            "#01404F#5PHeh, guess I'll hand\x01",
            "over my spare as well.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2A6C():
        OP_9A(0xFE, 0x109, 0x384, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_2A6C)
    WaitChrThread(0x108, 1)
    TurnDirection(0x109, 0x108, 500)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0xDD),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " received.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0xDD, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    def lambda_2AD4():
        OP_96(0xFE, 0x640, 0xFFFFE0C0, 0x708, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_2AD4)
    WaitChrThread(0x108, 1)
    WaitChrThread(0x10A, 1)

    ChrTalk(
        0x109,
        (
            "#12P#10105FIs this... A master\x01",
            "quartz?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FThese are for us...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#12P#00601FHmph. You two would only\x01",
            "be a burden without\x01",
            "them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#01402F#5PGo ahead. Set whichever\x01",
            "you like in the center\x01",
            "of your ENIGMA Ⅱs.\x02\x03",
            "You'll be able to access\x01",
            "several arts no matter\x01",
            "which you choose.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x108, 600)

    ChrTalk(
        0x101,
        "#11P#00002FYes, sir!\x02",
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
            "※A master quartz can be set\x01",
            "in the center slot of the\x01",
            "new [ENIGMA Ⅱ] orbments.\x02\x03",
            "※Master quartz can be set\x01",
            "from [ORBMENT]->[QUARTZ] in\x01",
            "the camp menu.\x07\x00\x02",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D6E")
    SetScenarioFlags(0x21, 0)

    label("loc_2D6E")

    OP_E2(0x2)
    Sleep(400)
    EventEnd(0x5)
    Return()

    # Function_13_17AC end

    def Function_14_2D76(): pass

    label("Function_14_2D76")

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
        (
            "#12P#00600FOkay, looks like you're\x01",
            "ready.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2EE5():
        TurnDirection(0xFE, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2EE5)
    Sleep(100)

    def lambda_2EF5():
        TurnDirection(0xFE, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_2EF5)
    WaitChrThread(0x101, 2)

    ChrTalk(
        0x101,
        (
            "#00000FYes. Sorry to keep you\x01",
            "waiting.\x02\x03",
            "#00002FAnd... Thank you very\x01",
            "much for having these\x01",
            "ready for us.\x02",
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
            "#12P#00605FI-It's not like we prepared these\x01",
            "just for you or anything.\x02\x03",
            "#00606F...That aside, Bannings. I assume\x01",
            "you understand, right?\x02\x03",
            "#00601FThis mission is also part of your\x01",
            "Section One training.\x02\x03",
            "#00607FIf you screw things up, you'll have\x01",
            "to start over from the beginning\x01",
            "again. Bear that in mind!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(3317, 255, 100, 0)

    ChrTalk(
        0x101,
        "#00000F#30WYes, sir!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10112F#6P(Ahaha... He's not\x01",
            "really honest with his\x01",
            "feelings, is he?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#01404F#5P(Heh, he's much more\x01",
            "passionate than he\x01",
            "looks.)\x02\x03",
            "#01402F(...I would expect no\x01",
            "less from one who rivaled\x01",
            "Guy in Section One.)\x02",
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
        "Alright. Let's begin!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)

    def lambda_3254():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_3254)
    Sleep(50)

    def lambda_3264():

        label("loc_3264")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_3264")

    QueueWorkItem2(0x10A, 2, lambda_3264)
    Sleep(50)

    def lambda_3279():

        label("loc_3279")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_3279")

    QueueWorkItem2(0x108, 2, lambda_3279)
    WaitChrThread(0x109, 2)
    OP_93(0x101, 0x0, 0x1F4)

    def lambda_3296():
        OP_98(0xFE, 0x0, 0x0, 0x7D0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3296)
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
            "#00003FOf Crossbell Police\x01",
            "Section One, Chief\x01",
            "Detective Alex Dudley.\x02",
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
        "#30WRight.\x02",
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
            "#00000FOf the Crossbell\x01",
            "Guardian Force, Sergeant\x01",
            "Major Noｱl Seeker.\x02",
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
        "#30WYes, sir!\x02",
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
            "#00004FAnd Special Advisor and\x01",
            "Bracer of the Crossbell\x01",
            "Branch Guild, Arios MacLaine.\x02",
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
        "#30WRight.\x02",
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
            "#00003FThe Special Support Section of the\x01",
            "Crossbell Police will now commence\x01",
            "its search and capture mission.\x02\x03",
            "#00013FOur two targets are former\x01",
            "Chairman Hartmann and secretary of\x01",
            "the former mayor, Ernest Reis.\x02\x03",
            "#00007FOur deadline is 17:00 today─ Let's\x01",
            "give it our all!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    Sound(2506, 255, 100, 0)

    ChrTalk(
        0x10A,
        "#00607F#12PAll right!\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    Sound(4024, 255, 100, 1)

    ChrTalk(
        0x108,
        "#01407F#6PAcknowledged!\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    Sound(2481, 255, 100, 2)

    ChrTalk(
        0x109,
        "#6P#10107F#6PRoger!\x02",
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
            "※About the [Detective Notebook]\x02\x03",
            "※Various events in the game are automatically\x01",
            "recorded in the [Detective Notebook].\x02\x03",
            "※You can view its contents by selecting\x01",
            "[Detective Notebook] under [ITEMS] in the camp\x01",
            "menu, or by pressing [△ + Left] on field maps.\x02\x03",
            "※You can also read the manual and various\x01",
            "other content, so please make good use of it.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Sound(814, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※About the [Combat Notebook]\x02\x03",
            "※Information about the enemies you have\x01",
            "fought is automatically recorded in the\x01",
            "[Combat Notebook].\x02\x03",
            "※Similarly to the Detective Notebook, you can\x01",
            "view it by using the [Combat Notebook] item\x01",
            "or by pressing [△ + Right] on field maps.\x07\x00\x02",
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

    # Function_14_2D76 end

    def Function_15_3A56(): pass

    label("Function_15_3A56")

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

    def lambda_3B0F():
        OP_97(0x101, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3B0F)
    Sleep(50)

    def lambda_3B2C():
        OP_97(0x108, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 0, lambda_3B2C)
    Sleep(50)

    def lambda_3B49():
        OP_97(0x10A, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_3B49)
    Sleep(50)

    def lambda_3B66():
        OP_97(0x109, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3B66)
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
        "#12P#10105FA-Are these...\x02",
    )

    CloseMessageWindow()
    OP_68(147900, -2800, -2200, 3500)
    MoveCamera(303, 17, 0, 3500)
    SetCameraDistance(25000, 3500)
    Sleep(500)

    def lambda_3C1B():
        OP_97(0x101, 0xFFFFD8F0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3C1B)
    Sleep(100)

    def lambda_3C38():
        OP_97(0x108, 0xFFFFD8F0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 0, lambda_3C38)
    Sleep(100)

    def lambda_3C55():
        OP_97(0x10A, 0xFFFFD8F0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_3C55)
    Sleep(100)

    def lambda_3C72():
        OP_97(0x109, 0xFFFFD8F0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3C72)
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
        "#00010F#5PArios, are these...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#6P#01403FYeah... These are the remains of their\x01",
            ""Responsiveness Enhancement Experiments".\x02\x03",
            "#01401FFor experiments to enhance the five senses\x01",
            "and the ability to sense the supernatural,\x01",
            "the children here were dosed with Gnosis.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        "#00608FTch... Damned heretics.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10110FThe D∴G Cult...\x02\x03",
            "#10103FEven though they're\x01",
            "gone, I still can't\x01",
            "forgive them...\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x10E, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        "#00008F#11P............\x02",
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
            "#00003F#11P...I don't know what Ernest\x01",
            "and Hartmann are trying to\x01",
            "accomplish here...\x02\x03",
            "#00001FBut we can't let them make\x01",
            "use of this damned place a\x01",
            "second time.\x02",
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
        "#4P#10107FWe gotta stop 'em!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#00607FAll right. Let's make a\x01",
            "move then!\x02",
        )
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
            "※Except for Dudley, equipped with the\x01",
            "[Information] Quartz, characters will\x01",
            "not be able to see enemy information.\x02\x03",
            "※However, you can acquire this\x01",
            "information by using a [Battle Scope] or\x01",
            "using the Mirage element [Analyze] art.\x02\x03",
            "※By learning enemies' elemental\x01",
            "weaknesses and status vulnerabilities,\x01",
            "you can efficiently battle them.\x02\x03",
            "※You can view acquired enemy information\x01",
            "at any time by selecting an enemy with\x01",
            "the cursor and holding the [□ Button].\x02\x03",
            "※By the way, Dudley can currently use\x01",
            "the [Analyze] support art.\x07\x00\x02",
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

    # Function_15_3A56 end

    def Function_16_426F(): pass

    label("Function_16_426F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x120, 3)), scpexpr(EXPR_END)), "loc_430B")
    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The stone door is\x01",
            "tightly shut.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x108,
        (
            "#01400FThere's a switch deeper\x01",
            "in on the right. Let's\x01",
            "hurry there to unlock it.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Return()

    label("loc_430B")

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
        "#11P#00005FThis is...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10105FA stone door, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#01401F#4PIt's a gate leading to\x01",
            "the depths. We unlocked\x01",
            "it 6 years ago, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#12P#00603FHmph. I suspect Ernest\x01",
            "set the lock back in\x01",
            "place again.\x02\x03",
            "#00600FIs there a way to open\x01",
            "it?\x02",
        )
    )

    CloseMessageWindow()
    OP_68(2500, 1300, 79260, 1000)
    OP_93(0x108, 0x5A, 0x190)
    OP_6F(0x1)

    ChrTalk(
        0x108,
        (
            "#5P#01400FThere's a switch deeper in\x01",
            "on the right. It should\x01",
            "open if you flip it.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_44FE():
        OP_93(0x101, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_44FE)
    Sleep(50)

    def lambda_450E():
        OP_93(0x10A, 0x32, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_450E)
    Sleep(50)

    def lambda_451E():
        OP_93(0x109, 0x32, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_451E)
    Sleep(50)
    WaitChrThread(0x10A, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x101, 1)

    ChrTalk(
        0x101,
        (
            "#00001F#5PAll right, let's give it\x01",
            "a go.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x120, 3)
    SetChrPos(0x0, 2100, 0, 77900, 90)
    OP_69(0xFF, 0x0)
    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_16_426F end

    def Function_17_4581(): pass

    label("Function_17_4581")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x120, 4)), scpexpr(EXPR_END)), "loc_45CC")
    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It looks like it won't\x01",
            "budge.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapFlags(0x8000000)
    EventEnd(0x3)
    Jump("loc_471F")

    label("loc_45CC")

    EventBegin(0x1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's a switch. Operate?\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4718")
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

    label("loc_4718")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)

    label("loc_471F")

    Return()

    # Function_17_4581 end

    def Function_18_4720(): pass

    label("Function_18_4720")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4791")

    ChrTalk(
        0x101,
        (
            "#00003FWe can't turn back.\x02\x03",
            "#00001FWe have to capture\x01",
            "Ernest and Hartmann at\x01",
            "any cost.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_48B3")

    label("loc_4791")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_47F0")

    ChrTalk(
        0x109,
        (
            "#10101FWe can't just dilly-\x01",
            "dally here. Let's hurry\x01",
            "toward the depths.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_48B3")

    label("loc_47F0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_485B")

    ChrTalk(
        0x10A,
        (
            "#00603FErnest and Hartmann are\x01",
            "further inside. Let's hurry\x01",
            "and catch up with them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_48B3")

    label("loc_485B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_48B3")

    ChrTalk(
        0x108,
        (
            "#01401FWe don't have time to\x01",
            "turn back. Let's hurry\x01",
            "and pursue them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_48B3")

    SetChrPos(0x0, 2860, -8000, -8020, 0)
    EventEnd(0x4)
    Return()

    # Function_18_4720 end

    def Function_19_48C7(): pass

    label("Function_19_48C7")

    EventBegin(0x1)
    OP_4B(0x8, 0xFF)
    TurnDirection(0x8, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#00603FBannings. Where the heck\x01",
            "do you think you're\x01",
            "going?\x02\x03",
            "#00601FI won't permit any\x01",
            "actions out of line.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00003FSorry, I'll be ready\x01",
            "soon.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 2430, -8000, 3380, 180)
    OP_93(0x8, 0x5A, 0x0)
    OP_4C(0x8, 0xFF)
    EventEnd(0x4)
    Return()

    # Function_19_48C7 end

    SaveToFile()

Try(main)
