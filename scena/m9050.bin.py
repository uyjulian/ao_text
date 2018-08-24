from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "m9050.bin",                # FileName
        "m9050",                    # MapName
        "m9050",                    # Location
        0x00C0,                     # MapIndex
        "ed7351",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x2A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 192, 0, 1, 0, 2],
    )

    BuildStringList((
        "m9050",                  # 0
        "Tyrant",                 # 1
        "Tyrant",                 # 2
        "bm9030",                 # 3
        "bm9030",                 # 4
        "bm9030",                 # 5
        "bm9030",                 # 6
        "bm9030",                 # 7
    ))

    ATBonus("ATBonus_66C", 100, 5, 1, 5, 1, 5, 1, 5, 5, 5, 5, 5, 5, 0, 0, 0)
    ATBonus("ATBonus_67C", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    Sepith("Sepith_44B0", 18,  15,  23,  12,  0,   0,   0)
    Sepith("Sepith_44B8", 9,   9,   9,   9,   6,   6,   6)
    Sepith("Sepith_44A8", 8,   11,  8,   15,  8,   6,   2)

    MonsterBattlePostion("MonsterBattlePostion_6BC", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_6C0", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_6C4", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_6C8", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_6CC", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_6D0", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_6D4", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_6D8", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_71C", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_720", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_724", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_728", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_72C", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_730", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_734", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_738", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_69C", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_6A0", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_6A4", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_6A8", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_6AC", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_6B0", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_6B4", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_6B8", 2, 13, 180)

    # monster count: 21

    BattleInfo(
        "BattleInfo_7D8", 0x0000, 103, 6, 45, 10, 1, 30, 24, "bm9030", "Sepith_44B0", 40, 30, 20, 0,
        (
            ("ms87700.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_6BC", "MonsterBattlePostion_71C", "ed7452", "ed7453", "ATBonus_66C"),
            ("ms87700.dat", "ms87700.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_69C", "MonsterBattlePostion_71C", "ed7452", "ed7453", "ATBonus_66C"),
            ("ms87700.dat", "ms87700.dat", "ms87700.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_6BC", "MonsterBattlePostion_71C", "ed7452", "ed7453", "ATBonus_66C"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_874", 0x0000, 103, 6, 45, 10, 1, 40, 24, "bm9030", "Sepith_44B8", 80, 20, 0, 0,
        (
            ("ms82003.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_6BC", "MonsterBattlePostion_71C", "ed7452", "ed7453", "ATBonus_66C"),
            ("ms82003.dat", "ms82003.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_69C", "MonsterBattlePostion_71C", "ed7452", "ed7453", "ATBonus_66C"),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_73C", 0x0000, 103, 6, 45, 10, 1, 40, 24, "bm9030", "Sepith_44A8", 40, 30, 20, 0,
        (
            ("ms78800.dat", "ms78800.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_69C", "MonsterBattlePostion_71C", "ed7452", "ed7453", "ATBonus_66C"),
            ("ms78800.dat", "ms78800.dat", "ms78800.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_6BC", "MonsterBattlePostion_71C", "ed7452", "ed7453", "ATBonus_66C"),
            ("ms78800.dat", "ms78800.dat", "ms78800.dat", "ms78800.dat", 0, 0, 0, 0, "MonsterBattlePostion_69C", "MonsterBattlePostion_71C", "ed7452", "ed7453", "ATBonus_66C"),
            (),
        )
    )

    # event battle count: 2

    BattleInfo(
        "BattleInfo_8E4", 0x0C00, 255, 6, 0, 0, 3, 0, 24, "bm9030", 0x00000000, 100, 0, 0, 0,
        (
            ("ms87700.dat", "ms87700.dat", "ms87700.dat", "ms78800.dat", "ms78800.dat", "ms87700.dat", "ms78800.dat", "ms87700.dat", "MonsterBattlePostion_69C", "MonsterBattlePostion_71C", "ed7452", "ed7453", "ATBonus_67C"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_928", 0x0C00, 255, 6, 0, 0, 3, 0, 24, "bm9030", 0x00000000, 100, 0, 0, 0,
        (
            ("ms87700.dat", "ms87700.dat", "ms87700.dat", "ms87700.dat", "ms78800.dat", "ms87700.dat", "ms78800.dat", "ms78800.dat", "MonsterBattlePostion_69C", "MonsterBattlePostion_71C", "ed7452", "ed7453", "ATBonus_67C"),
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
        "monster/ch78850.itc",               # 10
        "monster/ch78851.itc",               # 11
        "monster/ch87750.itc",               # 12
        "monster/ch87751.itc",               # 13
        "monster/ch82050.itc",               # 14
        "monster/ch82051.itc",               # 15
    ))

    DeclNpc(48000,   4500,    4294952296, 0,    484,  0x0, 0,   18,  0,   0,   0,   255, 255, 255,  0)
    DeclNpc(4294877296, 4294963796, 4294915796, 0,    484,  0x0, 0,   18,  0,   0,   0,   255, 255, 255,  0)

    DeclMonster(4294947496, 4294867816, 0,       0x101000B,    "BattleInfo_7D8", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(33470,   4294878106, 4019,    0x1010153,    "BattleInfo_874", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(30940,   4294902167, 4019,    0x10100C5,    "BattleInfo_73C", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(49150,   4294915786, 8029,    0x10100E1,    "BattleInfo_73C", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(26990,   4294852616, 30,      0x1010020,    "BattleInfo_73C", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(4294910996, 4294859876, 4294963316, 0x1010075,    "BattleInfo_874", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(4294920536, 4294888956, 4294963296, 0x10100D2,    "BattleInfo_73C", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(4294879766, 4294912036, 4294963316, 0x1010093,    "BattleInfo_7D8", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(4294902406, 4294963816, 4294963326, 0x101008E,    "BattleInfo_874", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(4294891176, 17740,   4294963296, 0x1010090,    "BattleInfo_7D8", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(4294944386, 47430,   30,      0x1010124,    "BattleInfo_73C", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(4294909686, 83990,   4294963296, 0x101004D,    "BattleInfo_874", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(3420,    67390,   30,      0x1010111,    "BattleInfo_7D8", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(33240,   68170,   0,       0x1010128,    "BattleInfo_73C", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(55460,   45270,   0,       0x1010141,    "BattleInfo_874", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(67320,   13360,   0,       0x1010089,    "BattleInfo_7D8", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(76330,   4294949226, 0,       0x101012D,    "BattleInfo_73C", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(64410,   4294876536, 0,       0x1010037,    "BattleInfo_7D8", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(43270,   4294914166, 8029,    0x1010077,    "BattleInfo_874", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(6820,    4294917496, 12000,   0x1010059,    "BattleInfo_73C", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(4294945186, 4294908836, 12030,   0x1010040,    "BattleInfo_73C", 0,   16,  0xFFFF, 0,  1)

    DeclActor(4294941296, 12000,   4294908296, 1200,    4294941296, 13000,   4294908296, 0x007C, 0,  3,  0x0000)
    DeclActor(4294944296, 0,       4294863296, 1200,    4294944296, 1000,    4294863296, 0x007C, 0,  4,  0x0000)
    DeclActor(32000,   8000,    4294922296, 1200,    32000,   9000,    4294922296, 0x007C, 0,  5,  0x0000)
    DeclActor(58000,   0,       4294887296, 1200,    58000,   1000,    4294887296, 0x007C, 0,  6,  0x0000)
    DeclActor(92000,   4000,    4294917296, 1200,    92000,   5000,    4294917296, 0x007C, 0,  7,  0x0000)
    DeclActor(55000,   0,       11000,   1200,    55000,   1000,    11000,   0x007C, 0,  8,  0x0000)
    DeclActor(48000,   4000,    4294952296, 1200,    48000,   5000,    4294952296, 0x007C, 0,  9,  0x0000)
    DeclActor(4294877296, 4294963296, 4294915796, 1200,    4294877296, 4294964296, 4294915796, 0x007C, 0,  10, 0x0000)
    DeclActor(4294895796, 4294959296, 78500,   1200,    4294895796, 4294960296, 78500,   0x007C, 0,  11, 0x0000)
    DeclActor(4294904296, 4294963296, 81000,   1200,    4294904296, 4294964296, 81000,   0x007C, 0,  12, 0x0000)
    DeclActor(4000,    0,       4294894296, 1200,    4000,    1000,    4294894296, 0x007C, 0,  13, 0x0000)
    DeclActor(4294942796, 0,       4294853296, 1200,    4294942796, 1000,    4294853296, 0x007C, 0,  14, 0x0000)
    DeclActor(4294910296, 0,       4294917296, 1200,    4294910296, 1000,    4294917296, 0x007C, 0,  15, 0x0000)
    DeclActor(4294905296, 4294963296, 40500,   1200,    4294905296, 4294964296, 40500,   0x007C, 0,  15, 0x0000)
    DeclActor(4294935296, 0,       86000,   1200,    4294935296, 1000,    86000,   0x007C, 0,  15, 0x0000)
    DeclActor(101000,  4294963296, 12000,   1200,    101000,  4294964296, 12000,   0x007C, 0,  15, 0x0000)
    DeclActor(73000,   4000,    4294924296, 1200,    73000,   4000,    4294924296, 0x007C, 0,  15, 0x0000)
    DeclActor(4294955296, 12000,   4294933296, 1200,    4294955296, 13000,   4294933296, 0x007C, 0,  15, 0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 0
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4])                      # 1
    ChipFrameInfo(800, 0, [0, 1, 2, 3, 4, 3, 2, 1])              # 2
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 3
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5, 6, 7])             # 4
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4, 5, 6, 7])             # 5

    ScpFunction((
        "Function_0_A2C",          # 00, 0
        "Function_1_A4B",          # 01, 1
        "Function_2_A7D",          # 02, 2
        "Function_3_19C1",         # 03, 3
        "Function_4_1B12",         # 04, 4
        "Function_5_1C63",         # 05, 5
        "Function_6_1DB4",         # 06, 6
        "Function_7_1E6E",         # 07, 7
        "Function_8_1FDE",         # 08, 8
        "Function_9_212F",         # 09, 9
        "Function_10_234A",        # 0A, 10
        "Function_11_2565",        # 0B, 11
        "Function_12_26B6",        # 0C, 12
        "Function_13_2807",        # 0D, 13
        "Function_14_2811",        # 0E, 14
        "Function_15_281B",        # 0F, 15
        "Function_16_28F4",        # 10, 16
        "Function_17_2E67",        # 11, 17
        "Function_18_30E5",        # 12, 18
        "Function_19_3238",        # 13, 19
        "Function_20_3279",        # 14, 20
        "Function_21_380B",        # 15, 21
        "Function_22_3875",        # 16, 22
        "Function_23_38DF",        # 17, 23
        "Function_24_3949",        # 18, 24
        "Function_25_39B3",        # 19, 25
        "Function_26_3A1D",        # 1A, 26
        "Function_27_3A87",        # 1B, 27
        "Function_28_3EAA",        # 1C, 28
        "Function_29_4297",        # 1D, 29
    ))


    def Function_0_A2C(): pass

    label("Function_0_A2C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A4A")
    OP_A1(0xFE, 0x2BC, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_0_A2C")

    label("loc_A4A")

    Return()

    # Function_0_A2C end

    def Function_1_A4B(): pass

    label("Function_1_A4B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A5C")
    Event(0, 17)

    label("loc_A5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A8, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A6D")
    Event(0, 20)

    label("loc_A6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_A7C")
    ClearScenarioFlags(0x22, 0)
    Event(0, 29)

    label("loc_A7C")

    Return()

    # Function_1_A4B end

    def Function_2_A7D(): pass

    label("Function_2_A7D")

    OP_F0(0x1, 0x320)
    OP_1B(0x0, 0x0, 0x12)
    OP_52(0xA, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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
    OP_52(0x19, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapObjFlags(0x12, 0x4)
    SetMapObjFlags(0x13, 0x4)
    SetMapObjFlags(0x14, 0x4)
    SetMapObjFlags(0x15, 0x4)
    SetMapObjFlags(0x16, 0x4)
    SetMapObjFlags(0x17, 0x4)
    SetMapObjFlags(0x18, 0x4)
    SetMapObjFlags(0x19, 0x4)
    SetMapObjFrame(0xFF, "hasira_7s", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hasira_0s", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hasira_0ss", 0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A8, 3)), scpexpr(EXPR_END)), "loc_15E6")
    SetMapObjFrame(0xFF, "pnrm02", 0x2, "day")
    SetMapObjFrame(0xFF, "CA_day", 0x1, 0x2)
    SetMapObjFrame(0xFF, "CA_night", 0x1, 0x2)
    SetMapObjFrame(0xFF, "CA_day", 0x0, 0x1)
    SetMapObjFrame(0xFF, "CA_night", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hasira_7s", 0x1, 0x1)
    SetMapObjFrame(0xFF, "hasira_0s", 0x1, 0x1)
    SetMapObjFrame(0xFF, "hasira_0ss", 0x1, 0x1)
    SetMapObjFrame(0xFF, "hasira_5d", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hasira_6n", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hasira_0d", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hasira_0n", 0x0, 0x1)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xB, 0x4)
    SetMapObjFlags(0xC, 0x4)
    SetMapObjFlags(0xD, 0x4)
    SetMapObjFlags(0xE, 0x4)
    SetMapObjFlags(0xF, 0x4)
    SetMapObjFlags(0x10, 0x4)
    SetMapObjFlags(0x11, 0x4)
    ClearMapObjFlags(0x12, 0x4)
    ClearMapObjFlags(0x13, 0x4)
    ClearMapObjFlags(0x14, 0x4)
    ClearMapObjFlags(0x15, 0x4)
    ClearMapObjFlags(0x16, 0x4)
    ClearMapObjFlags(0x17, 0x4)
    ClearMapObjFlags(0x18, 0x4)
    ClearMapObjFlags(0x19, 0x4)
    Jump("loc_18D4")

    label("loc_15E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B0, 4)), scpexpr(EXPR_END)), "loc_1777")
    SetMapObjFrame(0xA, "black_add", 0x2, "night")
    SetMapObjFrame(0xB, "black_add", 0x2, "night")
    SetMapObjFrame(0xC, "black_add", 0x2, "night")
    SetMapObjFrame(0xD, "black_add", 0x2, "night")
    SetMapObjFrame(0xE, "black_add", 0x2, "night")
    SetMapObjFrame(0xF, "black_add", 0x2, "night")
    SetMapObjFrame(0x10, "black_add", 0x2, "night")
    SetMapObjFrame(0x11, "black_add", 0x2, "night")
    SetMapObjFrame(0xA, "blue", 0x2, "night")
    SetMapObjFrame(0xB, "blue", 0x2, "night")
    SetMapObjFrame(0xC, "blue", 0x2, "night")
    SetMapObjFrame(0xD, "blue", 0x2, "night")
    SetMapObjFrame(0xE, "blue", 0x2, "night")
    SetMapObjFrame(0xF, "blue", 0x2, "night")
    SetMapObjFrame(0x10, "blue", 0x2, "night")
    SetMapObjFrame(0x11, "blue", 0x2, "night")
    SetMapObjFrame(0xFF, "hasira_5d", 0x2, "night")
    SetMapObjFrame(0xFF, "hasira_6n", 0x2, "night")
    SetMapObjFrame(0xFF, "pnrm02", 0x2, "night")
    SetMapObjFrame(0xFF, "CA_day", 0x1, 0x2)
    SetMapObjFrame(0xFF, "CA_night", 0x0, 0x2)
    SetMapObjFrame(0xFF, "CA_day", 0x0, 0x1)
    SetMapObjFrame(0xFF, "CA_night", 0x0, 0x1)
    OP_7D(0xD2, 0xDC, 0xFF, 0x0, 0x0)
    Jump("loc_18D4")

    label("loc_1777")

    SetMapObjFrame(0xA, "black_add", 0x2, "day")
    SetMapObjFrame(0xB, "black_add", 0x2, "day")
    SetMapObjFrame(0xC, "black_add", 0x2, "day")
    SetMapObjFrame(0xD, "black_add", 0x2, "day")
    SetMapObjFrame(0xE, "black_add", 0x2, "day")
    SetMapObjFrame(0xF, "black_add", 0x2, "day")
    SetMapObjFrame(0x10, "black_add", 0x2, "day")
    SetMapObjFrame(0x11, "black_add", 0x2, "day")
    SetMapObjFrame(0xA, "blue", 0x2, "day")
    SetMapObjFrame(0xB, "blue", 0x2, "day")
    SetMapObjFrame(0xC, "blue", 0x2, "day")
    SetMapObjFrame(0xD, "blue", 0x2, "day")
    SetMapObjFrame(0xE, "blue", 0x2, "day")
    SetMapObjFrame(0xF, "blue", 0x2, "day")
    SetMapObjFrame(0x10, "blue", 0x2, "day")
    SetMapObjFrame(0x11, "blue", 0x2, "day")
    SetMapObjFrame(0xFF, "hasira_5d", 0x2, "day")
    SetMapObjFrame(0xFF, "hasira_6n", 0x2, "day")
    SetMapObjFrame(0xFF, "pnrm02", 0x2, "day")
    SetMapObjFrame(0xFF, "CA_day", 0x0, 0x2)
    SetMapObjFrame(0xFF, "CA_night", 0x1, 0x2)
    SetMapObjFrame(0xFF, "CA_day", 0x0, 0x1)
    SetMapObjFrame(0xFF, "CA_night", 0x0, 0x1)
    OP_7D(0xFF, 0xFF, 0xFF, 0x0, 0x0)

    label("loc_18D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x203, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18E7")
    OP_70(0x0, 0x0)
    Jump("loc_18EB")

    label("loc_18E7")

    OP_70(0x0, 0x1E)

    label("loc_18EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x203, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18FE")
    OP_70(0x1, 0x0)
    Jump("loc_1902")

    label("loc_18FE")

    OP_70(0x1, 0x1E)

    label("loc_1902")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x203, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1915")
    OP_70(0x2, 0x0)
    Jump("loc_1919")

    label("loc_1915")

    OP_70(0x2, 0x1E)

    label("loc_1919")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x203, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_192C")
    OP_70(0x3, 0x0)
    Jump("loc_1930")

    label("loc_192C")

    OP_70(0x3, 0x1E)

    label("loc_1930")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x203, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1943")
    OP_70(0x4, 0x0)
    Jump("loc_1947")

    label("loc_1943")

    OP_70(0x4, 0x1E)

    label("loc_1947")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x203, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_195A")
    OP_70(0x5, 0x0)
    Jump("loc_195E")

    label("loc_195A")

    OP_70(0x5, 0x1E)

    label("loc_195E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x203, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1971")
    OP_70(0x6, 0x0)
    Jump("loc_1975")

    label("loc_1971")

    OP_70(0x6, 0x1E)

    label("loc_1975")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x203, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1988")
    OP_70(0x7, 0x0)
    Jump("loc_198C")

    label("loc_1988")

    OP_70(0x7, 0x1E)

    label("loc_198C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x204, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_199F")
    OP_70(0x8, 0x0)
    Jump("loc_19A3")

    label("loc_199F")

    OP_70(0x8, 0x1E)

    label("loc_19A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x204, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19B6")
    OP_70(0x9, 0x0)
    Jump("loc_19BA")

    label("loc_19B6")

    OP_70(0x9, 0x1E)

    label("loc_19BA")

    Sound(124, 1, 100, 0)
    Return()

    # Function_2_A7D end

    def Function_3_19C1(): pass

    label("Function_3_19C1")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x203, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1ABD")
    Sound(14, 0, 100, 0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1FD, 1)"), scpexpr(EXPR_END)), "loc_1A46")
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
    SetScenarioFlags(0x203, 0)
    OP_E0(0x5, 0x0)
    Jump("loc_1AB8")

    label("loc_1A46")

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

    label("loc_1AB8")

    Jump("loc_1B06")

    label("loc_1ABD")

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

    label("loc_1B06")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_19C1 end

    def Function_4_1B12(): pass

    label("Function_4_1B12")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x203, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C0E")
    Sound(14, 0, 100, 0)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1FA, 1)"), scpexpr(EXPR_END)), "loc_1B97")
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
    SetScenarioFlags(0x203, 1)
    OP_E0(0x5, 0x0)
    Jump("loc_1C09")

    label("loc_1B97")

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
    OP_71(0x1, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1C09")

    Jump("loc_1C57")

    label("loc_1C0E")

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

    label("loc_1C57")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_1B12 end

    def Function_5_1C63(): pass

    label("Function_5_1C63")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x203, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D5F")
    Sound(14, 0, 100, 0)
    OP_74(0x2, 0x1E)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0xC1, 1)"), scpexpr(EXPR_END)), "loc_1CE8")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0xC1),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x203, 2)
    OP_E0(0x5, 0x0)
    Jump("loc_1D5A")

    label("loc_1CE8")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0xC1),
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

    label("loc_1D5A")

    Jump("loc_1DA8")

    label("loc_1D5F")

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

    label("loc_1DA8")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_1C63 end

    def Function_6_1DB4(): pass

    label("Function_6_1DB4")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x203, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E3E")
    Sound(14, 0, 100, 0)
    OP_74(0x3, 0x1E)
    OP_71(0x3, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    OP_70(0x3, 0x1E)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddSepith(0x1, 2000)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#57I Water Sepith x2000\x01",
            "obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x203, 3)
    OP_E0(0x5, 0x0)
    Jump("loc_1E5C")

    label("loc_1E3E")


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

    label("loc_1E5C")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_1DB4 end

    def Function_7_1E6E(): pass

    label("Function_7_1E6E")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x203, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FAE")
    Sound(14, 0, 100, 0)
    OP_74(0x4, 0x1E)
    OP_71(0x4, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    OP_70(0x4, 0x1E)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddSepith(0x0, 200)
    AddSepith(0x1, 200)
    AddSepith(0x2, 200)
    AddSepith(0x3, 200)
    AddSepith(0x4, 200)
    AddSepith(0x5, 200)
    AddSepith(0x6, 200)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#56I Earth Sepith  x200\x01\x07\x02",
            "#57I Water Sepith  x200\x01\x07\x02",
            "#58I Fire Sepith   x200\x01\x07\x02",
            "#59I Wind Sepith   x200\x01\x07\x02",
            "#60I Time Sepith   x200\x01\x07\x02",
            "#61I Space Sepith  x200\x01\x07\x02",
            "#62I Mirage Sepith x200\x01\x07\x00",
            "obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x203, 4)
    OP_E0(0x5, 0x0)
    Jump("loc_1FCC")

    label("loc_1FAE")


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

    label("loc_1FCC")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_1E6E end

    def Function_8_1FDE(): pass

    label("Function_8_1FDE")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x203, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20DA")
    Sound(14, 0, 100, 0)
    OP_74(0x5, 0x1E)
    OP_71(0x5, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1F7, 1)"), scpexpr(EXPR_END)), "loc_2063")
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
    SetScenarioFlags(0x203, 5)
    OP_E0(0x5, 0x0)
    Jump("loc_20D5")

    label("loc_2063")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1F7),
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
    OP_71(0x5, 0x1E, 0x0, 0x0, 0x0)

    label("loc_20D5")

    Jump("loc_2123")

    label("loc_20DA")

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

    label("loc_2123")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_1FDE end

    def Function_9_212F(): pass

    label("Function_9_212F")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x203, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2300")
    Sound(14, 0, 100, 0)
    OP_74(0x6, 0x1E)
    OP_71(0x6, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x218, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2232")
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0x8, 0x0, 0)
    OP_98(0x8, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_218C():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_218C)

    def lambda_21A6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_21A6)
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
    Battle("BattleInfo_8E4", 0x0, 0x0, 0x0, 0xB, 0xFF)
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0x8, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_2213"),
        (2, "loc_2222"),
        (1, "loc_222F"),
        (SWITCH_DEFAULT, "loc_2232"),
    )


    label("loc_2213")

    SetScenarioFlags(0x218, 6)
    OP_70(0x6, 0x1E)
    Sleep(500)
    Jump("loc_2232")

    label("loc_2222")

    OP_70(0x6, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_222F")

    OP_B9(0x0)
    Return()

    label("loc_2232")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x463, 1)"), scpexpr(EXPR_END)), "loc_228B")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x463),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x203, 6)
    OP_E0(0x5, 0x0)
    Jump("loc_22FB")

    label("loc_228B")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x463),
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
    OP_71(0x6, 0x1E, 0x0, 0x0, 0x0)

    label("loc_22FB")

    Jump("loc_233E")

    label("loc_2300")

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

    label("loc_233E")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_9_212F end

    def Function_10_234A(): pass

    label("Function_10_234A")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x203, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_251B")
    Sound(14, 0, 100, 0)
    OP_74(0x7, 0x1E)
    OP_71(0x7, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x218, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_244D")
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0x9, 0x0, 0)
    OP_98(0x9, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_23A7():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_23A7)

    def lambda_23C1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_23C1)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Monsters appeared!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    WaitChrThread(0x9, 1)
    Battle("BattleInfo_928", 0x0, 0x0, 0x0, 0xB, 0xFF)
    SetChrFlags(0x9, 0x80)
    ClearChrFlags(0x9, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_242E"),
        (2, "loc_243D"),
        (1, "loc_244A"),
        (SWITCH_DEFAULT, "loc_244D"),
    )


    label("loc_242E")

    SetScenarioFlags(0x218, 7)
    OP_70(0x7, 0x1E)
    Sleep(500)
    Jump("loc_244D")

    label("loc_243D")

    OP_70(0x7, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_244A")

    OP_B9(0x0)
    Return()

    label("loc_244D")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x5F3, 1)"), scpexpr(EXPR_END)), "loc_24A6")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x5F3),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x203, 7)
    OP_E0(0x5, 0x0)
    Jump("loc_2516")

    label("loc_24A6")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x5F3),
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
    OP_71(0x7, 0x1E, 0x0, 0x0, 0x0)

    label("loc_2516")

    Jump("loc_2559")

    label("loc_251B")

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

    label("loc_2559")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_10_234A end

    def Function_11_2565(): pass

    label("Function_11_2565")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x204, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2661")
    Sound(14, 0, 100, 0)
    OP_74(0x8, 0x1E)
    OP_71(0x8, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x56, 1)"), scpexpr(EXPR_END)), "loc_25EA")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x56),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x204, 0)
    OP_E0(0x5, 0x0)
    Jump("loc_265C")

    label("loc_25EA")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x56),
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

    label("loc_265C")

    Jump("loc_26AA")

    label("loc_2661")

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

    label("loc_26AA")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_11_2565 end

    def Function_12_26B6(): pass

    label("Function_12_26B6")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x204, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27B2")
    Sound(14, 0, 100, 0)
    OP_74(0x9, 0x1E)
    OP_71(0x9, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1FA, 1)"), scpexpr(EXPR_END)), "loc_273B")
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
    SetScenarioFlags(0x204, 1)
    OP_E0(0x5, 0x0)
    Jump("loc_27AD")

    label("loc_273B")

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
    OP_71(0x9, 0x1E, 0x0, 0x0, 0x0)

    label("loc_27AD")

    Jump("loc_27FB")

    label("loc_27B2")

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

    label("loc_27FB")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_12_26B6 end

    def Function_13_2807(): pass

    label("Function_13_2807")

    SetScenarioFlags(0x0, 0)
    Call(0, 15)
    ClearScenarioFlags(0x0, 0)
    Return()

    # Function_13_2807 end

    def Function_14_2811(): pass

    label("Function_14_2811")

    SetScenarioFlags(0x0, 1)
    Call(0, 15)
    ClearScenarioFlags(0x0, 1)
    Return()

    # Function_14_2811 end

    def Function_15_281B(): pass

    label("Function_15_281B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A8, 3)), scpexpr(EXPR_END)), "loc_285F")
    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There seems to be no reaction.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Jump("loc_28EC")

    label("loc_285F")

    SetMapFlags(0x8000000)
    EventBegin(0x1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's a crystal. Touch it?\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_28EC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A8, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28D1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_28C4")
    Call(0, 27)

    label("loc_28C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_28D0")
    Call(0, 28)

    label("loc_28D0")

    Return()

    label("loc_28D1")

    Fade(500)
    SetCameraDistance(35000, 0)
    OP_0D()
    Sleep(1000)
    Sound(211, 0, 100, 0)
    Call(0, 16)

    label("loc_28EC")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_15_281B end

    def Function_16_28F4(): pass

    label("Function_16_28F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B0, 4)), scpexpr(EXPR_END)), "loc_2905")
    ClearScenarioFlags(0x1B0, 4)
    Jump("loc_2908")

    label("loc_2905")

    SetScenarioFlags(0x1B0, 4)

    label("loc_2908")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B0, 4)), scpexpr(EXPR_END)), "loc_2BD0")
    OP_7D(0xD2, 0xDC, 0xFF, 0x0, 0x1388)
    SetMapObjFrame(0xA, "black_add", 0x2, "to_n")
    SetMapObjFrame(0xB, "black_add", 0x2, "to_n")
    SetMapObjFrame(0xC, "black_add", 0x2, "to_n")
    SetMapObjFrame(0xD, "black_add", 0x2, "to_n")
    SetMapObjFrame(0xE, "black_add", 0x2, "to_n")
    SetMapObjFrame(0xF, "black_add", 0x2, "to_n")
    SetMapObjFrame(0x10, "black_add", 0x2, "to_n")
    SetMapObjFrame(0x11, "black_add", 0x2, "to_n")
    SetMapObjFrame(0xA, "blue", 0x2, "to_n")
    SetMapObjFrame(0xB, "blue", 0x2, "to_n")
    SetMapObjFrame(0xC, "blue", 0x2, "to_n")
    SetMapObjFrame(0xD, "blue", 0x2, "to_n")
    SetMapObjFrame(0xE, "blue", 0x2, "to_n")
    SetMapObjFrame(0xF, "blue", 0x2, "to_n")
    SetMapObjFrame(0x10, "blue", 0x2, "to_n")
    SetMapObjFrame(0x11, "blue", 0x2, "to_n")
    SetMapObjFrame(0xFF, "pnrm02", 0x2, "to_n")
    SetMapObjFrame(0xFF, "hasira_5d", 0x2, "to_n")
    SetMapObjFrame(0xFF, "hasira_6n", 0x2, "to_n")
    Sleep(1300)
    Sound(278, 0, 50, 0)
    Sleep(1900)
    SetMapObjFrame(0xA, "black_add", 0x2, "night")
    SetMapObjFrame(0xB, "black_add", 0x2, "night")
    SetMapObjFrame(0xC, "black_add", 0x2, "night")
    SetMapObjFrame(0xD, "black_add", 0x2, "night")
    SetMapObjFrame(0xE, "black_add", 0x2, "night")
    SetMapObjFrame(0xF, "black_add", 0x2, "night")
    SetMapObjFrame(0x10, "black_add", 0x2, "night")
    SetMapObjFrame(0x11, "black_add", 0x2, "night")
    SetMapObjFrame(0xA, "blue", 0x2, "night")
    SetMapObjFrame(0xB, "blue", 0x2, "night")
    SetMapObjFrame(0xC, "blue", 0x2, "night")
    SetMapObjFrame(0xD, "blue", 0x2, "night")
    SetMapObjFrame(0xE, "blue", 0x2, "night")
    SetMapObjFrame(0xF, "blue", 0x2, "night")
    SetMapObjFrame(0x10, "blue", 0x2, "night")
    SetMapObjFrame(0x11, "blue", 0x2, "night")
    SetMapObjFrame(0xFF, "hasira_5d", 0x2, "night")
    SetMapObjFrame(0xFF, "hasira_6n", 0x2, "night")
    SetMapObjFrame(0xFF, "pnrm02", 0x2, "night")
    SetMapObjFrame(0xFF, "CA_day", 0x1, 0x2)
    SetMapObjFrame(0xFF, "CA_night", 0x0, 0x2)
    SetMapObjFrame(0xFF, "CA_day", 0x0, 0x1)
    SetMapObjFrame(0xFF, "CA_night", 0x0, 0x1)
    Jump("loc_2E64")

    label("loc_2BD0")

    OP_7D(0xFF, 0xFF, 0xFF, 0x0, 0x1388)
    SetMapObjFrame(0xA, "black_add", 0x2, "to_d")
    SetMapObjFrame(0xB, "black_add", 0x2, "to_d")
    SetMapObjFrame(0xC, "black_add", 0x2, "to_d")
    SetMapObjFrame(0xD, "black_add", 0x2, "to_d")
    SetMapObjFrame(0xE, "black_add", 0x2, "to_d")
    SetMapObjFrame(0xF, "black_add", 0x2, "to_d")
    SetMapObjFrame(0x10, "black_add", 0x2, "to_d")
    SetMapObjFrame(0x11, "black_add", 0x2, "to_d")
    SetMapObjFrame(0xA, "blue", 0x2, "to_d")
    SetMapObjFrame(0xB, "blue", 0x2, "to_d")
    SetMapObjFrame(0xC, "blue", 0x2, "to_d")
    SetMapObjFrame(0xD, "blue", 0x2, "to_d")
    SetMapObjFrame(0xE, "blue", 0x2, "to_d")
    SetMapObjFrame(0xF, "blue", 0x2, "to_d")
    SetMapObjFrame(0x10, "blue", 0x2, "to_d")
    SetMapObjFrame(0x11, "blue", 0x2, "to_d")
    SetMapObjFrame(0xFF, "pnrm02", 0x2, "to_d")
    SetMapObjFrame(0xFF, "hasira_5d", 0x2, "to_d")
    SetMapObjFrame(0xFF, "hasira_6n", 0x2, "to_d")
    Sleep(1300)
    Sound(278, 0, 50, 0)
    Sleep(1900)
    SetMapObjFrame(0xA, "black_add", 0x2, "day")
    SetMapObjFrame(0xB, "black_add", 0x2, "day")
    SetMapObjFrame(0xC, "black_add", 0x2, "day")
    SetMapObjFrame(0xD, "black_add", 0x2, "day")
    SetMapObjFrame(0xE, "black_add", 0x2, "day")
    SetMapObjFrame(0xF, "black_add", 0x2, "day")
    SetMapObjFrame(0x10, "black_add", 0x2, "day")
    SetMapObjFrame(0x11, "black_add", 0x2, "day")
    SetMapObjFrame(0xA, "blue", 0x2, "day")
    SetMapObjFrame(0xB, "blue", 0x2, "day")
    SetMapObjFrame(0xC, "blue", 0x2, "day")
    SetMapObjFrame(0xD, "blue", 0x2, "day")
    SetMapObjFrame(0xE, "blue", 0x2, "day")
    SetMapObjFrame(0xF, "blue", 0x2, "day")
    SetMapObjFrame(0x10, "blue", 0x2, "day")
    SetMapObjFrame(0x11, "blue", 0x2, "day")
    SetMapObjFrame(0xFF, "hasira_5d", 0x2, "day")
    SetMapObjFrame(0xFF, "hasira_6n", 0x2, "day")
    SetMapObjFrame(0xFF, "pnrm02", 0x2, "day")
    SetMapObjFrame(0xFF, "CA_day", 0x0, 0x2)
    SetMapObjFrame(0xFF, "CA_night", 0x1, 0x2)
    SetMapObjFrame(0xFF, "CA_day", 0x0, 0x1)
    SetMapObjFrame(0xFF, "CA_night", 0x0, 0x1)

    label("loc_2E64")

    OP_E2(0x4)
    Return()

    # Function_16_28F4 end

    def Function_17_2E67(): pass

    label("Function_17_2E67")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    LoadEffect(0x1, "event\\evwarp.eff")
    OP_68(-2630, 1500, -103410, 0)
    MoveCamera(0, 40, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(13980, 0)
    SetChrPos(0x0, -3000, 0, -102500, 45)
    SetChrPos(0x1, -3000, 0, -102500, 45)
    SetChrPos(0x2, -3000, 0, -102500, 45)
    SetChrPos(0x3, -3000, 0, -102500, 45)
    OP_A7(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    Sound(920, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x0, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_2F75():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_2F75)

    def lambda_2F86():
        OP_95(0xFE, -860, 0, -100390, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_2F86)
    Sleep(500)
    PlayEffect(0x1, 0xFF, 0x1, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_2FDD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_2FDD)

    def lambda_2FEE():
        OP_95(0xFE, -1940, 0, -99810, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_2FEE)
    Sleep(500)
    Sound(920, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x2, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_304B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2, 2, lambda_304B)

    def lambda_305C():
        OP_95(0xFE, -440, 0, -101980, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_305C)
    Sleep(500)
    PlayEffect(0x1, 0xFF, 0x3, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_30B3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x3, 2, lambda_30B3)

    def lambda_30C4():
        OP_95(0xFE, -590, 0, -103280, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_30C4)
    WaitChrThread(0x3, 1)
    Sleep(1000)
    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_17_2E67 end

    def Function_18_30E5(): pass

    label("Function_18_30E5")

    EventBegin(0x0)
    OP_E2(0x3)
    LoadEffect(0x1, "event\\evwarp.eff")
    Sound(936, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x0, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_313E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_313E)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0x1, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_3189():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_3189)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0x2, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_31D4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2, 2, lambda_31D4)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0x3, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_321F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x3, 2, lambda_321F)
    Sleep(1000)
    NewScene("m9002", 108, 0, 0)
    IdleLoop()
    Return()

    # Function_18_30E5 end

    def Function_19_3238(): pass

    label("Function_19_3238")

    OP_CF(0x1, 0xF4, 0x5)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3250")
    OP_CF(0x1, 0xF5, 0x4)

    label("loc_3250")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3264")
    OP_CF(0x1, 0xF5, 0x8)

    label("loc_3264")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3278")
    OP_CF(0x1, 0xF5, 0x9)

    label("loc_3278")

    Return()

    # Function_19_3238 end

    def Function_20_3279(): pass

    label("Function_20_3279")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    OP_69(0x2, 0x0)
    LoadEffect(0x1, "event\\ev202_00.eff")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_32B3")
    Call(0, 19)

    label("loc_32B3")

    SetChrPos(0xF4, -3000, 0, -102500, 20)
    SetChrPos(0x101, -3000, 0, -102500, 39)
    SetChrPos(0x103, -3000, 0, -102500, 26)
    SetChrPos(0x102, -3000, 0, -102500, 2)
    SetChrPos(0x104, -3000, 0, -102500, 52)
    SetChrPos(0xF5, -3000, 0, -102500, 352)
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
    OP_68(-15370, 5300, -100130, 0)
    MoveCamera(0, 26, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18410, 0)
    OP_68(-14530, 5300, -82830, 6000)
    MoveCamera(3, 12, 0, 6000)
    OP_6E(600, 6000)
    SetCameraDistance(18410, 6000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    OP_68(-2970, 4790, -102780, 0)
    MoveCamera(9, 11, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(69700, 0)
    OP_68(-2960, 4790, -102730, 7500)
    MoveCamera(3, 11, 0, 7500)
    OP_6E(600, 7500)
    SetCameraDistance(69700, 7500)
    Sleep(1000)
    PlaceName2(340, 200, "c_plac59", 0x0, 0)
    Sleep(500)
    BeginChrThread(0xF4, 0, 0, 21)
    Sound(920, 0, 40, 0)
    Sleep(600)
    BeginChrThread(0x101, 0, 0, 22)
    Sleep(600)
    BeginChrThread(0x102, 0, 0, 23)
    Sound(920, 0, 40, 0)
    Sleep(600)
    BeginChrThread(0x103, 0, 0, 24)
    Sleep(600)
    BeginChrThread(0x104, 0, 0, 25)
    Sound(920, 0, 40, 0)
    Sleep(600)
    BeginChrThread(0xF5, 0, 0, 26)
    WaitChrThread(0xF5, 0)
    OP_6F(0x79)
    Fade(500)
    OP_68(-1400, 1300, -99100, 0)
    MoveCamera(352, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15000, 0)
    OP_68(-1290, 1300, -98150, 0)
    MoveCamera(345, 18, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15000, 0)
    OP_0D()
    Sleep(300)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_353A")

    ChrTalk(
        0x102,
        (
            "#00105F#6PThis place is a\x01",
            "Territory...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_355E")

    label("loc_353A")


    ChrTalk(
        0x102,
        "#00105F#6PAnother Territory...\x02",
    )

    CloseMessageWindow()

    label("loc_355E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_35AA")

    ChrTalk(
        0x10A,
        (
            "#00605F#6POnce again... another\x01",
            "unexpected place.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_363A")

    label("loc_35AA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_35F6")

    ChrTalk(
        0x105,
        (
            "#10405F#6POnce again... another\x01",
            "unexpected place.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_363A")

    label("loc_35F6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_363A")

    ChrTalk(
        0x109,
        (
            "#10105F#6PThis place... isn't what\x01",
            "I expected.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_363A")


    ChrTalk(
        0x103,
        (
            "#00208F#6PI can't imagine this place being\x01",
            "an amalgamation of that rowdy\x01",
            "Shirley's inner thoughts, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301F#6PIndeed... Or rather─\x01",
            "could it be?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10703F#5PYes. It seems there are\x01",
            "many different "colors"\x01",
            "inside a person...\x02\x03",
            "#10708FThis could be another of\x01",
            "her sides.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#5PI see...\x02\x03",
            "#00001F─We don't know what awaits\x01",
            "us. Let's begin a careful\x01",
            "investigation without delay.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -1700, 0, -101200, 45)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x1A8, 1)
    OP_E2(0x2)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_20_3279 end

    def Function_21_380B(): pass

    label("Function_21_380B")

    PlayEffect(0x1, 0xFF, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_384A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_384A)
    OP_9B(0x0, 0xFE, 0x0, 0x128E, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x7D0, 0x0)
    Return()

    # Function_21_380B end

    def Function_22_3875(): pass

    label("Function_22_3875")

    PlayEffect(0x1, 0xFF, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_38B4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_38B4)
    OP_9B(0x0, 0xFE, 0x0, 0x10FE, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x155, 0x3E8, 0x7D0, 0x0)
    Return()

    # Function_22_3875 end

    def Function_23_38DF(): pass

    label("Function_23_38DF")

    PlayEffect(0x1, 0xFF, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_391E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_391E)
    OP_9B(0x0, 0xFE, 0x0, 0x1036, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x12, 0x3E8, 0x7D0, 0x0)
    Return()

    # Function_23_38DF end

    def Function_24_3949(): pass

    label("Function_24_3949")

    PlayEffect(0x1, 0xFF, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_3988():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3988)
    OP_9B(0x0, 0xFE, 0x0, 0xD48, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x162, 0x3E8, 0x7D0, 0x0)
    Return()

    # Function_24_3949 end

    def Function_25_39B3(): pass

    label("Function_25_39B3")

    PlayEffect(0x1, 0xFF, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_39F2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_39F2)
    OP_9B(0x0, 0xFE, 0x0, 0xC4E, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x148, 0x3E8, 0x7D0, 0x0)
    Return()

    # Function_25_39B3 end

    def Function_26_3A1D(): pass

    label("Function_26_3A1D")

    PlayEffect(0x1, 0xFF, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_3A5C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3A5C)
    OP_9B(0x0, 0xFE, 0x0, 0xB22, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x1C, 0x3E8, 0x7D0, 0x0)
    Return()

    # Function_26_3A1D end

    def Function_27_3A87(): pass

    label("Function_27_3A87")

    EventBegin(0x0)
    OP_E2(0x3)
    OP_69(0x2, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3AA2")
    Call(0, 19)

    label("loc_3AA2")

    SetChrPos(0x101, 3300, 0, -75000, 0)
    SetChrPos(0xF4, 4700, 0, -75000, 0)
    SetChrPos(0x102, 5800, 0, -73900, 315)
    SetChrPos(0x103, 2200, 0, -74400, 45)
    SetChrPos(0x104, 5800, 0, -76000, 0)
    SetChrPos(0xF5, 2800, 0, -76300, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_68(3920, 2050, -73740, 0)
    MoveCamera(72, 17, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(21140, 0)
    OP_68(4000, 1530, -74500, 0)
    MoveCamera(356, 18, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(26000, 0)
    SetCameraDistance(35000, 0)
    Fade(500)
    OP_0D()
    Sound(211, 0, 100, 0)
    Sleep(300)
    Call(0, 16)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00011F#5PThe sky's color changed?\x02",
    )

    CloseMessageWindow()
    OP_68(6650, 130, -74490, 0)
    MoveCamera(35, 30, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(23330, 0)
    Fade(500)
    OP_0D()

    def lambda_3C8D():
        OP_93(0x102, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_3C8D)
    Sleep(50)

    def lambda_3C9D():
        OP_93(0x104, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_3C9D)
    Sleep(50)

    def lambda_3CAD():
        OP_93(0xF5, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_3CAD)
    Sleep(50)

    def lambda_3CBD():
        OP_93(0x106, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_3CBD)
    Sleep(50)

    def lambda_3CCD():
        OP_93(0x101, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3CCD)
    Sleep(50)

    def lambda_3CDD():
        OP_93(0x103, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_3CDD)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF5, 0)
    WaitChrThread(0x106, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x103, 0)

    ChrTalk(
        0x102,
        (
            "#00108F#5PIt appears the places we\x01",
            "can go have changed as\x01",
            "well...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00201F#5PIt appears we'll need to\x01",
            "do some work to proceed\x01",
            "further.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#6PAnyhow, it's like it\x01",
            "suddenly changed like\x01",
            "some moody cat...\x02\x03",
            "#00301FIt's indeed a whimsical\x01",
            "place that fits someone\x01",
            "like her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10708F#5P(...Bloody Shirley. A\x01",
            "girl of the strongest\x01",
            "jaeger corps...)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 4000, 20, -76000, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x1A8, 2)
    ClearMapFlags(0x8000000)
    OP_E2(0x2)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_27_3A87 end

    def Function_28_3EAA(): pass

    label("Function_28_3EAA")

    EventBegin(0x0)
    OP_E2(0x3)
    OP_69(0x2, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3EC5")
    Call(0, 19)

    label("loc_3EC5")

    SetChrPos(0x101, -24820, 0, -116430, 45)
    SetChrPos(0xF4, -26080, 0, -115840, 45)
    SetChrPos(0x102, -26620, 0, -114380, 90)
    SetChrPos(0x103, -23910, 0, -117300, 45)
    SetChrPos(0x104, -25620, 0, -117520, 45)
    SetChrPos(0xF5, -23350, 0, -115900, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_68(-26000, 1530, -115500, 0)
    MoveCamera(12, 18, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(35000, 0)
    Fade(500)
    OP_0D()
    Sound(211, 0, 100, 0)
    Call(0, 16)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005F#5PThe sky's color changed?\x02",
    )

    CloseMessageWindow()
    OP_68(-28110, 430, -114690, 0)
    MoveCamera(62, 18, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(26530, 0)
    Fade(500)
    OP_0D()
    Sleep(600)

    def lambda_4079():
        OP_93(0x102, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_4079)
    Sleep(50)

    def lambda_4089():
        OP_93(0x106, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_4089)
    Sleep(50)

    def lambda_4099():
        OP_93(0xF5, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_4099)
    Sleep(50)

    def lambda_40A9():
        OP_93(0x101, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_40A9)
    Sleep(50)

    def lambda_40B9():
        OP_93(0x104, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_40B9)
    Sleep(50)

    def lambda_40C9():
        OP_93(0x103, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_40C9)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x106, 0)
    WaitChrThread(0xF5, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x103, 0)

    ChrTalk(
        0x102,
        (
            "#00108F#11PIt appears the places we\x01",
            "can go have changed as\x01",
            "well...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00201F#11PIt appears we'll need to\x01",
            "do some work to proceed\x01",
            "further.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#12PAnyhow, it's like it\x01",
            "suddenly changed like\x01",
            "some moody cat...\x02\x03",
            "#00301FIt's indeed a whimsical\x01",
            "place that fits someone\x01",
            "like her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10708F#11P(...Bloody Shirley. A\x01",
            "girl of the strongest\x01",
            "jaeger corps...)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -25000, 30, -116600, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x1A8, 2)
    ClearMapFlags(0x8000000)
    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_28_3EAA end

    def Function_29_4297(): pass

    label("Function_29_4297")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    OP_69(0x2, 0x0)
    OP_68(4000, 600, -73000, 0)
    MoveCamera(355, 17, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(55000, 0)
    SetCameraDistance(50000, 6000)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1500)
    Sound(202, 0, 80, 0)
    Sound(278, 0, 50, 0)
    SetMapObjFrame(0xFF, "pnrm02", 0x2, "day")
    SetMapObjFrame(0xFF, "CA_day", 0x1, 0x2)
    SetMapObjFrame(0xFF, "CA_night", 0x1, 0x2)
    SetMapObjFrame(0xFF, "CA_day", 0x0, 0x1)
    SetMapObjFrame(0xFF, "CA_night", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hasira_7s", 0x1, 0x1)
    SetMapObjFrame(0xFF, "hasira_0s", 0x1, 0x1)
    SetMapObjFrame(0xFF, "hasira_0ss", 0x1, 0x1)
    SetMapObjFrame(0xFF, "hasira_5d", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hasira_6n", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hasira_0d", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hasira_0n", 0x0, 0x1)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xB, 0x4)
    SetMapObjFlags(0xC, 0x4)
    SetMapObjFlags(0xD, 0x4)
    SetMapObjFlags(0xE, 0x4)
    SetMapObjFlags(0xF, 0x4)
    SetMapObjFlags(0x10, 0x4)
    SetMapObjFlags(0x11, 0x4)
    ClearMapObjFlags(0x12, 0x4)
    ClearMapObjFlags(0x13, 0x4)
    ClearMapObjFlags(0x14, 0x4)
    ClearMapObjFlags(0x15, 0x4)
    ClearMapObjFlags(0x16, 0x4)
    ClearMapObjFlags(0x17, 0x4)
    ClearMapObjFlags(0x18, 0x4)
    ClearMapObjFlags(0x19, 0x4)
    Sleep(2500)
    StopSound(124, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 1)
    NewScene("m9002", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_29_4297 end

    SaveToFile()

Try(main)
