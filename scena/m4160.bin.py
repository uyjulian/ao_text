from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "m4160.bin",                # FileName
        "m4160",                    # MapName
        "m4160",                    # Location
        0x00C9,                     # MapIndex
        "ed7351",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x28,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 201, 0, 2, 0, 3],
    )

    BuildStringList((
        "m4160",                  # 0
        "イベント用モンスター",   # 1
        "イベント用モンスター",   # 2
        "オルゴンスパイド",       # 3
        "ゲルマー",               # 4
        "SE制御",                 # 5
        "bm4150",                 # 6
        "bm4150",                 # 7
        "bm4150",                 # 8
        "bm4160",                 # 9
        "bm4160",                 # 10
        "bm4160",                 # 11
    ))

    ATBonus("ATBonus_340", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)
    ATBonus("ATBonus_360", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    Sepith("Sepith_278D", 6,   6,   8,   8,   8,   6,   6)
    Sepith("Sepith_277D", 4,   4,   6,   6,   4,   6,   6)
    Sepith("Sepith_2785", 12,  12,  4,   4,   4,   2,   2)

    MonsterBattlePostion("MonsterBattlePostion_380", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_384", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_388", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_38C", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_390", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_394", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_398", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_39C", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_400", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_404", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_408", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_40C", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_410", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_414", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_418", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_41C", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_3A0", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_3A4", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_3A8", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_3AC", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_3B0", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_3B4", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_3B8", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_3BC", 8, 14, 180)

    # monster count: 3

    BattleInfo(
        "BattleInfo_558", 0x0000, 72, 6, 60, 10, 1, 30, 0, "bm4150", "Sepith_278D", 50, 50, 0, 0,
        (
            ("ms82500.dat", "ms82500.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_380", "MonsterBattlePostion_400", "ed7450", "ed7453", "ATBonus_340"),
            ("ms82500.dat", "ms86900.dat", "ms86900.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_3A0", "MonsterBattlePostion_400", "ed7450", "ed7453", "ATBonus_340"),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_420", 0x0000, 72, 6, 60, 10, 1, 40, 0, "bm4150", "Sepith_277D", 40, 30, 20, 0,
        (
            ("ms86900.dat", "ms86900.dat", "ms86900.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_380", "MonsterBattlePostion_400", "ed7450", "ed7453", "ATBonus_340"),
            ("ms86900.dat", "ms86900.dat", "ms86900.dat", "ms86900.dat", 0, 0, 0, 0, "MonsterBattlePostion_380", "MonsterBattlePostion_400", "ed7450", "ed7453", "ATBonus_340"),
            ("ms86900.dat", "ms86900.dat", "ms86900.dat", "ms86900.dat", "ms86900.dat", 0, 0, 0, "MonsterBattlePostion_380", "MonsterBattlePostion_400", "ed7450", "ed7453", "ATBonus_340"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_4BC", 0x0000, 72, 6, 60, 10, 1, 20, 0, "bm4150", "Sepith_2785", 40, 30, 20, 0,
        (
            ("ms83700.dat", "ms83700.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_380", "MonsterBattlePostion_400", "ed7450", "ed7453", "ATBonus_340"),
            ("ms83700.dat", "ms83700.dat", "ms83700.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_3A0", "MonsterBattlePostion_400", "ed7450", "ed7453", "ATBonus_340"),
            ("ms83700.dat", "ms83700.dat", "ms83700.dat", "ms83700.dat", 0, 0, 0, 0, "MonsterBattlePostion_380", "MonsterBattlePostion_400", "ed7450", "ed7453", "ATBonus_340"),
            (),
        )
    )

    # event battle count: 4

    BattleInfo(
        "BattleInfo_60C", 0x0000, 85, 6, 0, 0, 1, 0, 0, "bm4160", 0x00000000, 100, 0, 0, 0,
        (
            ("ms68600.dat", "ms68600.dat", "ms68600.dat", "ms68600.dat", "ms68600.dat", "ms68600.dat", "ms68600.dat", "ms68600.dat", "MonsterBattlePostion_380", "MonsterBattlePostion_400", "ed7451", "ed7453", "ATBonus_360"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_650", 0x0000, 50, 6, 45, 0, 1, 0, 0, "bm4160", 0x00000000, 100, 0, 0, 0,
        (
            ("ms82500.dat", "ms82500.dat", "ms82500.dat", "ms82500.dat", 0, 0, 0, 0, "MonsterBattlePostion_380", "MonsterBattlePostion_400", "ed7451", "ed7453", "ATBonus_340"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_5C8", 0x0002, 3, 6, 45, 3, 3, 30, 0, "bm4160", 0x00000000, 100, 0, 0, 0,
        (
            ("ms82000.dat", "ms82000.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_380", "MonsterBattlePostion_400", "ed7453", "ed7453", "ATBonus_340"),
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
        "monster/ch68650.itc",               # 16
        "monster/ch68651.itc",               # 17
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(4294938977, 4500,    603030,  180,  484,  0x0, 0,   22,  0,   0,   0,   255, 255, 255,  0)
    DeclNpc(4294959296, 500,     2500,    0,    484,  0x0, 0,   20,  0,   0,   1,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(5340,    2500,    0,       0x1010107,    "BattleInfo_558", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(4294966446, 29010,   0,       0x10100C6,    "BattleInfo_420", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(3410,    50790,   0,       0x10100E1,    "BattleInfo_4BC", 0,   18,  0xFFFF, 2,  3)

    DeclEvent(0x0000, 0, 8,   0.0,                   290.0,                 -1.0,                  144.0,                 [0.125,                -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000001788139343,   0.0,                   -0.0,                  -96.66667175292969,    0.20000001788139343,   1.0])
    DeclEvent(0x0000, 0, 11,  2.0199999809265137,    611.0,                 3.0,                   225.0,                 [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.10000000149011612,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.6733333468437195,   -61.10000228881836,    -0.6000000238418579,   1.0])

    DeclActor(4294938976, 4000,    603030,  1200,    4294938976, 5000,    603030,  0x007C, 0,  4,  0x0000)
    DeclActor(4294959296, 0,       2500,    1200,    4294959296, 1000,    2500,    0x007C, 0,  5,  0x0000)
    DeclActor(7250,    0,       52500,   1200,    7250,    1000,    52500,   0x007C, 0,  6,  0x0000)
    DeclActor(4294938986, 4000,    619750,  1200,    4294938986, 4000,    619750,  0x007C, 0,  7,  0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 0
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4, 5])                   # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 2
    ChipFrameInfo(800, 0, [0, 1, 2, 3, 4])                       # 3
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 4
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4, 5])                   # 5

    ScpFunction((
        "Function_0_710",          # 00, 0
        "Function_1_72F",          # 01, 1
        "Function_2_74B",          # 02, 2
        "Function_3_75B",          # 03, 3
        "Function_4_C98",          # 04, 4
        "Function_5_F5B",          # 05, 5
        "Function_6_13A2",         # 06, 6
        "Function_7_14F4",         # 07, 7
        "Function_8_158D",         # 08, 8
        "Function_9_1BC1",         # 09, 9
        "Function_10_1BEF",        # 0A, 10
        "Function_11_21F6",        # 0B, 11
        "Function_12_26DB",        # 0C, 12
    ))


    def Function_0_710(): pass

    label("Function_0_710")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_72E")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x3, 0x4, 0x3)
    Jump("Function_0_710")

    label("loc_72E")

    Return()

    # Function_0_710 end

    def Function_1_72F(): pass

    label("Function_1_72F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_74A")
    OP_A1(0xFE, 0x3E8, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_1_72F")

    label("loc_74A")

    Return()

    # Function_1_72F end

    def Function_2_74B(): pass

    label("Function_2_74B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_75A")
    ClearScenarioFlags(0x22, 0)
    Event(0, 10)

    label("loc_75A")

    Return()

    # Function_2_74B end

    def Function_3_75B(): pass

    label("Function_3_75B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_792")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x12D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_79B")

    label("loc_792")

    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x15F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_79B")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x166, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x166, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7B3")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_7B3")

    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x166, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x166, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7CB")
    ModifyEventFlags(1, 1, 0x80)

    label("loc_7CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x166, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7DE")
    OP_1B(0x5, 0x0, 0xC)

    label("loc_7DE")

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
    OP_52(0xD, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1FB, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AF3")
    OP_70(0x0, 0x0)
    Jump("loc_AF7")

    label("loc_AF3")

    OP_70(0x0, 0x1E)

    label("loc_AF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B0A")
    OP_70(0x1, 0x0)
    Jump("loc_B0E")

    label("loc_B0A")

    OP_70(0x1, 0x1E)

    label("loc_B0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B21")
    OP_70(0x2, 0x0)
    Jump("loc_B25")

    label("loc_B21")

    OP_70(0x2, 0x1E)

    label("loc_B25")

    LoadEffect(0x9, "map/mpcave2.eff")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6A), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BA9")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_E6(0x0, 0x7, 0xFF, 0xFF, 0xFF, 0xDC, 0x0)
    OP_11(0x0, 0x0, 0x0, 0x19, 0x28, 0x0)

    label("loc_BA9")

    SetBarrier(0x0, 0x0, 0x1, 0x0, -4380, 4140, 611170, 8000, 5000, 90000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_BE6")
    SetMapObjFrame(0xFF, "gate00", 0x0, 0x1)
    SetBarrier(0x2, 0x0, 0x1)
    Jump("loc_BF4")

    label("loc_BE6")

    SetMapObjFrame(0xFF, "gate00", 0x1, 0x1)

    label("loc_BF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_C22")
    SetMapObjFrame(0xFF, "hasigo_a", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hasigo_b", 0x1, 0x1)
    Jump("loc_C42")

    label("loc_C22")

    SetMapObjFrame(0xFF, "hasigo_a", 0x1, 0x1)
    SetMapObjFrame(0xFF, "hasigo_b", 0x0, 0x1)

    label("loc_C42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x166, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C54")
    OP_65(0x3, 0x1)

    label("loc_C54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x166, 7)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C97")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6A), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C91")
    Sound(120, 1, 80, 0)
    Jump("loc_C97")

    label("loc_C91")

    Sound(120, 1, 50, 0)

    label("loc_C97")

    Return()

    # Function_3_75B end

    def Function_4_C98(): pass

    label("Function_4_C98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x214, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D3F")
    TalkBegin(0xFF)
    SetMapFlags(0x8000000)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "You sense the presence of powerful monsters.\x01",
            "[Estimated Monsters Level: 85]\x01",
            "Open the chest?\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D3F")
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Return()

    label("loc_D3F")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1FB, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F10")
    Sound(14, 0, 100, 0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x214, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E42")
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0xA, 0x0, 0)
    OP_98(0xA, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_D9C():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_D9C)

    def lambda_DB6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_DB6)
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
    Battle("BattleInfo_60C", 0x0, 0x0, 0x0, 0xB, 0xFF)
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xA, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_E23"),
        (2, "loc_E32"),
        (1, "loc_E3F"),
        (SWITCH_DEFAULT, "loc_E42"),
    )


    label("loc_E23")

    SetScenarioFlags(0x214, 3)
    OP_70(0x0, 0x1E)
    Sleep(500)
    Jump("loc_E42")

    label("loc_E32")

    OP_70(0x0, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_E3F")

    OP_B9(0x0)
    Return()

    label("loc_E42")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0xA8, 1)"), scpexpr(EXPR_END)), "loc_E9B")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0xA8),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1FB, 2)
    OP_E0(0x5, 0x0)
    Jump("loc_F0B")

    label("loc_E9B")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0xA8),
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

    label("loc_F0B")

    Jump("loc_F4F")

    label("loc_F10")

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

    label("loc_F4F")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_C98 end

    def Function_5_F5B(): pass

    label("Function_5_F5B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0xE9, 0x4)"), scpexpr(EXPR_END)), "loc_1186")
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1137")
    Sound(14, 0, 100, 0)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21B, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1069")
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0xB, 0x0, 0)
    OP_98(0xB, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_FC3():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_FC3)

    def lambda_FDD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_FDD)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Monsters appeared!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    WaitChrThread(0xB, 1)
    Battle("BattleInfo_650", 0x0, 0x0, 0x0, 0xB, 0xFF)
    SetChrFlags(0xB, 0x80)
    ClearChrFlags(0xB, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_104A"),
        (2, "loc_1059"),
        (1, "loc_1066"),
        (SWITCH_DEFAULT, "loc_1069"),
    )


    label("loc_104A")

    SetScenarioFlags(0x21B, 7)
    OP_70(0x1, 0x1E)
    Sleep(500)
    Jump("loc_1069")

    label("loc_1059")

    OP_70(0x1, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_1066")

    OP_B9(0x0)
    Return()

    label("loc_1069")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x7F, 1)"), scpexpr(EXPR_END)), "loc_10C2")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x7F),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1F1, 5)
    OP_E0(0x5, 0x0)
    Jump("loc_1132")

    label("loc_10C2")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x7F),
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

    label("loc_1132")

    Jump("loc_1176")

    label("loc_1137")

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

    label("loc_1176")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Jump("loc_13A1")

    label("loc_1186")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1357")
    Sound(14, 0, 100, 0)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21B, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1289")
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0xB, 0x0, 0)
    OP_98(0xB, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_11E3():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_11E3)

    def lambda_11FD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_11FD)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Monsters appeared!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    WaitChrThread(0xB, 1)
    Battle("BattleInfo_650", 0x0, 0x0, 0x0, 0xB, 0xFF)
    SetChrFlags(0xB, 0x80)
    ClearChrFlags(0xB, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_126A"),
        (2, "loc_1279"),
        (1, "loc_1286"),
        (SWITCH_DEFAULT, "loc_1289"),
    )


    label("loc_126A")

    SetScenarioFlags(0x21B, 7)
    OP_70(0x1, 0x1E)
    Sleep(500)
    Jump("loc_1289")

    label("loc_1279")

    OP_70(0x1, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_1286")

    OP_B9(0x0)
    Return()

    label("loc_1289")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0xE9, 1)"), scpexpr(EXPR_END)), "loc_12E2")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0xE9),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1F1, 5)
    OP_E0(0x5, 0x0)
    Jump("loc_1352")

    label("loc_12E2")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0xE9),
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

    label("loc_1352")

    Jump("loc_1396")

    label("loc_1357")

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

    label("loc_1396")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)

    label("loc_13A1")

    Return()

    # Function_5_F5B end

    def Function_6_13A2(): pass

    label("Function_6_13A2")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_149E")
    Sound(14, 0, 100, 0)
    OP_74(0x2, 0x1E)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1F7, 1)"), scpexpr(EXPR_END)), "loc_1427")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1F7),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1F1, 6)
    OP_E0(0x5, 0x0)
    Jump("loc_1499")

    label("loc_1427")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1F7),
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

    label("loc_1499")

    Jump("loc_14E8")

    label("loc_149E")

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

    label("loc_14E8")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_13A2 end

    def Function_7_14F4(): pass

    label("Function_7_14F4")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1567")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a ladder.\x01",
            "Climb down?\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1562")
    FadeToDark(500, 0, -1)
    OP_0D()
    EventEnd(0x5)
    NewScene("m4120", 112, 0, 0)
    IdleLoop()

    label("loc_1562")

    Jump("loc_158A")

    label("loc_1567")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a broken ladder\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_158A")

    EventEnd(0x5)
    Return()

    # Function_7_14F4 end

    def Function_8_158D(): pass

    label("Function_8_158D")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    OP_E2(0x3)
    LoadChrToIndex("monster/ch82050.itc", 0x1E)
    LoadChrToIndex("monster/ch82051.itc", 0x1F)
    LoadChrToIndex("chr/ch00050.itc", 0x20)
    LoadChrToIndex("chr/ch00150.itc", 0x21)
    LoadChrToIndex("chr/ch00250.itc", 0x22)
    LoadChrToIndex("chr/ch02950.itc", 0x23)
    LoadChrToIndex("chr/ch03050.itc", 0x24)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrChipByIndex(0x8, 0x1F)
    SetChrSubChip(0x8, 0x6)
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x6)
    OP_52(0x9, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x101, 0, 0, 293000, 0)
    SetChrPos(0x102, -1250, 0, 292500, 0)
    SetChrPos(0x103, 750, 0, 292000, 0)
    SetChrPos(0x109, -750, 0, 291250, 0)
    SetChrPos(0x105, 0, 0, 290500, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x8, 0, 7000, 289000, 0)
    SetChrPos(0x9, 0, 7000, 305000, 180)

    def lambda_16C5():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_16C5)
    Sleep(50)

    def lambda_16DD():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_16DD)
    Sleep(50)

    def lambda_16F5():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_16F5)
    Sleep(50)

    def lambda_170D():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_170D)
    Sleep(50)

    def lambda_1725():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1725)
    OP_68(0, 800, 292000, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18000, 0)
    OP_68(0, 800, 296000, 3000)
    SetCameraDistance(20000, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(948, 0, 30, 0)
    Sound(911, 0, 70, 0)
    Sleep(300)
    WaitChrThread(0x101, 1)
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)
    StopBGM(0xBB8)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#00005F#11P......?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10108F#12PFrom above...?\x02",
    )

    CloseMessageWindow()
    OP_68(0, 800, 296000, 8000)
    MoveCamera(64, 23, 0, 8000)
    OP_6E(600, 8000)
    SetCameraDistance(18050, 8000)
    Sound(844, 0, 50, 0)
    Sound(809, 0, 60, 0)

    def lambda_1898():
        OP_9D(0xFE, 0x0, 0x0, 0x493E0, 0x1F4, 0x1770)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1898)
    Sleep(300)

    def lambda_18B8():
        OP_9D(0xFE, 0x0, 0x0, 0x474A0, 0x1F4, 0x1770)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_18B8)
    WaitChrThread(0x9, 1)
    Sound(845, 0, 100, 0)
    SetChrChipByIndex(0x9, 0x1E)
    BeginChrThread(0x9, 3, 0, 9)
    WaitChrThread(0x8, 1)
    Sound(845, 0, 100, 0)
    SetChrChipByIndex(0x8, 0x1E)
    BeginChrThread(0x8, 3, 0, 9)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7453", 0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_1986():
        OP_92(0x109, 0x0, 0x474A0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1986)
    Sleep(50)

    def lambda_199C():
        OP_92(0x105, 0x0, 0x474A0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_199C)
    Sleep(50)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    Fade(250)
    Sound(805, 0, 100, 0)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0x101, 0x20)
    SetChrChipByIndex(0x102, 0x21)
    SetChrChipByIndex(0x103, 0x22)
    SetChrChipByIndex(0x109, 0x23)
    SetChrChipByIndex(0x105, 0x24)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x102, 0x0)
    SetChrSubChip(0x103, 0x0)
    SetChrSubChip(0x109, 0x0)
    SetChrSubChip(0x105, 0x0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1A42")

    ChrTalk(
        0x101,
        "#00007F#11PWha...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00101F#11PWe saw them back then...!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1A9F")

    label("loc_1A42")


    ChrTalk(
        0x101,
        "#00010F#11PWhat......!??\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00201F#11PThey don't give off a normal monsters' vibe...\x02",
    )

    CloseMessageWindow()

    label("loc_1A9F")


    ChrTalk(
        0x105,
        "#10307F#5PThey took us from both sides── Here they come!\x02",
    )

    CloseMessageWindow()
    EndChrThread(0x9, 0x3)
    EndChrThread(0x8, 0x3)
    Sound(809, 0, 100, 0)
    SetChrChipByIndex(0x8, 0x1F)
    SetChrSubChip(0x8, 0x6)
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x6)
    OP_52(0x9, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_1B2E():
        OP_9D(0xFE, 0x0, 0x320, 0x48440, 0x320, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1B2E)

    def lambda_1B4B():
        OP_9D(0xFE, 0x0, 0x320, 0x48440, 0x320, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1B4B)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x5)
    OP_68(0, 600, 296000, 200)
    SetCameraDistance(18000, 200)
    Sleep(200)
    CancelBlur(200)
    Battle("BattleInfo_5C8", 0x30200011, 0x1, 0x0, 0x26, 0xFF)
    FadeToDark(0, 0, -1)
    EndChrThread(0x8, 0x1)
    EndChrThread(0x9, 0x1)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    Call(0, 10)
    Return()

    # Function_8_158D end

    def Function_9_1BC1(): pass

    label("Function_9_1BC1")

    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1BD7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1BEE")
    OP_A0(0xFE, 1500, 0x0, 0x7)
    Jump("loc_1BD7")

    label("loc_1BEE")

    Return()

    # Function_9_1BC1 end

    def Function_10_1BEF(): pass

    label("Function_10_1BEF")

    EventBegin(0x0)
    OP_E2(0x3)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch02950.itc", 0x21)
    LoadChrToIndex("chr/ch03050.itc", 0x22)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x109, 0x21)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x22)
    SetChrSubChip(0x105, 0x0)
    SetChrPos(0x101, 0, 0, 297000, 0)
    SetChrPos(0x102, -1250, 0, 296500, 0)
    SetChrPos(0x103, 750, 0, 296000, 0)
    SetChrPos(0x109, -1000, 0, 295250, 180)
    SetChrPos(0x105, 0, 0, 294500, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_68(230, 800, 296330, 0)
    MoveCamera(41, 26, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16800, 0)
    SetCameraDistance(17800, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    Fade(250)
    Sound(805, 0, 100, 0)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    OP_0D()
    Sleep(300)

    def lambda_1D25():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1D25)

    def lambda_1D32():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1D32)
    Sleep(50)

    def lambda_1D42():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1D42)
    Sleep(50)

    def lambda_1D52():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1D52)
    Sleep(50)

    def lambda_1D62():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_1D62)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#00006F#5PKh...they were freakingly strong.\x02\x03",
            "#00013FThey looked like trained monsters\x01",
            "like the military dogs...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#6PYes, they weren't canines but\x01",
            "looked like felines...\x02\x03",
            "#00108FCould they be from the "Red Constellation"...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F#6PMaybe...\x01",
            "I heard that jaeger corps often\x01",
            "make use of military monsters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10306F#12PAlthough, as you could expect, they\x01",
            "appeared to be on a whole different\x01",
            "level from the mafia's military dogs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00211F#11PYes...they were even audacious\x01",
            "to come with a pincer attack.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2110")

    ChrTalk(
        0x102,
        (
            "#00103F#6PHowever, if that man called\x01",
            "Minneth was using them...\x02\x03",
            "#00101FIt could be that he's connected\x01",
            "to the "Red Constellation".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#5PYeah, a purveyor of the government or\x01",
            "a funds riser...maybe something like that.\x02\x03",
            "#00003F──For now, I'm glad we managed\x01",
            "to repel them in some way.\x02\x03",
            "#00013FThe terminus seems to be close,\x01",
            "so let's hurry on ahead.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_219C")

    label("loc_2110")


    ChrTalk(
        0x101,
        (
            "#00003F#5P──For now, I'm glad we managed\x01",
            "to repel them in some way.\x02\x03",
            "#00013FThe terminus seems to be close,\x01",
            "so let's hurry on ahead.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_219C")


    ChrTalk(
        0x109,
        "#10101F#6PYes...!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    OP_D7(0x22)
    OP_37()
    SetChrPos(0x0, 0, 0, 297000, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetScenarioFlags(0x166, 6)
    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(1, 1, 0x80)
    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_10_1BEF end

    def Function_11_21F6(): pass

    label("Function_11_21F6")

    EventBegin(0x0)
    OP_E2(0x3)
    OP_63(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(-3750, 6800, 611400, 2000)
    MoveCamera(50, 20, 0, 2000)
    OP_6E(600, 2000)
    SetCameraDistance(18650, 2000)

    def lambda_2248():
        OP_93(0x0, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_2248)
    Sleep(50)

    def lambda_2258():
        OP_93(0x1, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1, 0, lambda_2258)
    Sleep(50)

    def lambda_2268():
        OP_93(0x2, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2, 0, lambda_2268)
    Sleep(50)

    def lambda_2278():
        OP_93(0x3, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x3, 0, lambda_2278)
    Sleep(50)
    WaitChrThread(0x0, 0)
    WaitChrThread(0x1, 0)
    WaitChrThread(0x2, 0)
    WaitChrThread(0x3, 0)
    OP_6F(0x79)
    Sleep(500)
    Fade(500)
    OP_68(-28450, 4500, 619250, 0)
    MoveCamera(25, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(20000, 0)
    OP_68(-15450, 8000, 617750, 5000)
    MoveCamera(45, 0, 0, 5000)
    OP_6E(600, 5000)
    SetCameraDistance(22000, 5000)
    OP_0D()
    OP_6F(0x79)
    Sleep(1000)
    Fade(500)
    OP_68(1000, 5000, 611000, 0)
    MoveCamera(35, 20, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18000, 0)
    SetChrPos(0x101, -500, 4000, 611000, 270)
    SetChrPos(0x102, 750, 4000, 610500, 270)
    SetChrPos(0x103, 1000, 4000, 611950, 270)
    SetChrPos(0x109, 2000, 4000, 610900, 270)
    SetChrPos(0x105, 2500, 4000, 612750, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00002F#11PWe're... Near the old \x01",
            "abandoned mine entrance!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#11PThank goodness...\x01",
            "We reached it safely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10108F#11PHowever...\x01",
            "Where's senior Randy?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10301F#11PIf they have yet to go at it,\x01",
            "we could still catch up with him...\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0x7D0)
    OP_82(0x64, 0x0, 0xBB8, 0x3E8)
    Sound(196, 0, 30, 0)
    Sound(833, 0, 40, 0)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7586", 0)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x24A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x24A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ReplaceBGM("ed7301", "ed7586")
    ReplaceBGM("ed7351", "ed7586")

    ChrTalk(
        0x103,
        (
            "#00205F#11PSounds of explosives from the exit...!\x02\x03",
            "#00207FI can also hear sounds of a gunfight!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00107F#11PRandy...!\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x2EE)

    def lambda_25E2():
        TurnDirection(0x102, 0x101, 750)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_25E2)
    Sleep(50)

    def lambda_25F2():
        TurnDirection(0x103, 0x101, 750)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_25F2)
    Sleep(50)

    def lambda_2602():
        TurnDirection(0x109, 0x101, 750)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2602)
    Sleep(50)

    def lambda_2612():
        TurnDirection(0x105, 0x101, 750)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_2612)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x101,
        "#00010F#6PTsk, let's go too!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10107F#11PYes sir!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10308F#11P(...Will we make it in time?)\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SoundLoad(120)
    Sound(120, 2, 80, 0)
    SetChrPos(0x0, -500, 4000, 611000, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetScenarioFlags(0x166, 7)
    ModifyEventFlags(0, 1, 0x80)
    OP_1B(0x5, 0x0, 0xC)
    OP_65(0x3, 0x1)
    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_11_21F6 end

    def Function_12_26DB(): pass

    label("Function_12_26DB")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00001FThere's no time...\x01",
            "Let's hurry up to the exit!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 12800, 0, 573040, 0)
    EventEnd(0x4)
    Return()

    # Function_12_26DB end

    SaveToFile()

Try(main)
