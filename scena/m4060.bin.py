from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "m4060.bin",                # FileName
        "m4060",                    # MapName
        "m4060",                    # Location
        0x007D,                     # MapIndex
        "ed7350",
        0x00000000,                 # Flags
        ("m4060", "r0000_1", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x27,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 125, 0, 2, 0, 3],
    )

    BuildStringList((
        "m4060",                  # 0
        "イベント用モンスター",   # 1
        "ロックドミナ",           # 2
        "bm4010",                 # 3
        "bm4010",                 # 4
        "bm4010",                 # 5
        "bm4010",                 # 6
        "bm4010",                 # 7
        "bm4010",                 # 8
        "bm4010",                 # 9
    ))

    ATBonus("ATBonus_3AC", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)
    ATBonus("ATBonus_39C", 100, 5, 1, 5, 1, 5, 1, 5, 5, 5, 5, 5, 5, 0, 0, 0)

    Sepith("Sepith_2BB5", 4,   4,   2,   0,   2,   2,   4)
    Sepith("Sepith_2BA5", 0,   3,   3,   3,   0,   0,   1)
    Sepith("Sepith_2B8D", 0,   4,   0,   4,   1,   1,   1)
    Sepith("Sepith_2BAD", 3,   0,   4,   3,   3,   5,   0)

    MonsterBattlePostion("MonsterBattlePostion_3EC", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_3F0", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_3F4", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_3F8", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_3FC", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_400", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_404", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_408", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_44C", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_450", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_454", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_458", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_45C", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_460", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_464", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_468", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_3CC", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_3D0", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_3D4", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_3D8", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_3DC", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_3E0", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_3E4", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_3E8", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_46C", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_470", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_474", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_478", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_47C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_480", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_484", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_488", 0, 0, 180)

    # monster count: 8

    BattleInfo(
        "BattleInfo_6A4", 0x0010, 48, 6, 45, 6, 1, 30, 0, "bm4010", "Sepith_2BB5", 100, 0, 0, 0,
        (
            ("ms80700.dat", "ms84600.dat", 0, 0, 0, 0, "ms84600.dat", 0, "MonsterBattlePostion_3EC", "MonsterBattlePostion_44C", "ed7450", "ed7453", "ATBonus_3AC"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_5C4", 0x0000, 47, 6, 45, 6, 1, 40, 0, "bm4010", "Sepith_2BA5", 60, 25, 10, 0,
        (
            ("ms83900.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3EC", "MonsterBattlePostion_44C", "ed7450", "ed7453", "ATBonus_39C"),
            ("ms83900.dat", "ms83900.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3CC", "MonsterBattlePostion_44C", "ed7450", "ed7453", "ATBonus_39C"),
            ("ms83900.dat", "ms83900.dat", "ms83900.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_3EC", "MonsterBattlePostion_44C", "ed7450", "ed7453", "ATBonus_39C"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_528", 0x0000, 46, 6, 45, 6, 1, 40, 0, "bm4010", "Sepith_2B8D", 60, 25, 10, 0,
        (
            ("ms83600.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3EC", "MonsterBattlePostion_44C", "ed7450", "ed7453", "ATBonus_39C"),
            ("ms83600.dat", "ms83600.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3CC", "MonsterBattlePostion_44C", "ed7450", "ed7453", "ATBonus_39C"),
            ("ms83600.dat", "ms83600.dat", "ms83600.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_3EC", "MonsterBattlePostion_44C", "ed7450", "ed7453", "ATBonus_39C"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_660", 0x0000, 47, 6, 45, 6, 1, 40, 0, "bm4010", "Sepith_2BAD", 100, 0, 0, 0,
        (
            ("ms82900.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3EC", "MonsterBattlePostion_44C", "ed7450", "ed7453", "ATBonus_39C"),
            (),
            (),
            (),
        )
    )

    # event battle count: 2

    BattleInfo(
        "BattleInfo_72C", 0x0000, 255, 6, 45, 0, 1, 0, 0, "bm4010", 0x00000000, 100, 0, 0, 0,
        (
            ("ms80700.dat", "ms80700.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_46C", "MonsterBattlePostion_44C", "ed7451", "ed7453", "ATBonus_3AC"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_6E8", 0x0012, 48, 6, 45, 3, 3, 30, 0, "bm4010", 0x00000000, 100, 0, 0, 0,
        (
            ("ms80700.dat", "ms84600.dat", "ms84600.dat", 0, 0, 0, "ms84600.dat", 0, "MonsterBattlePostion_3EC", "MonsterBattlePostion_44C", "ed7452", "ed7453", "ATBonus_3AC"),
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
        "monster/ch80750.itc",               # 10
        "monster/ch80750.itc",               # 11
        "monster/ch83650.itc",               # 12
        "monster/ch83650.itc",               # 13
        "chr/ch00000.itc",                   # 14
        "chr/ch00000.itc",                   # 15
        "chr/ch00000.itc",                   # 16
        "chr/ch00000.itc",                   # 17
        "monster/ch83950.itc",               # 18
        "monster/ch83951.itc",               # 19
        "monster/ch82950.itc",               # 1A
        "monster/ch82950.itc",               # 1B
        "chr/ch00000.itc",                   # 1C
        "chr/ch00000.itc",                   # 1D
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(4294967057, 10500,   32380,   0,    484,  0x0, 0,   16,  0,   0,   1,   255, 255, 255,  0)

    DeclMonster(4294800666, 161730,  5000,    0x10100B9,    "BattleInfo_6A4", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(4294802866, 188750,  5000,    0x10100B9,    "BattleInfo_5C4", 0,   24,  0xFFFF, 4,  5)
    DeclMonster(4294668376, 165910,  5000,    0x10100B9,    "BattleInfo_528", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(168220,  172490,  5000,    0x10100E6,    "BattleInfo_5C4", 0,   24,  0xFFFF, 4,  5)
    DeclMonster(154890,  187560,  5000,    0x101005F,    "BattleInfo_660", 0,   26,  0xFFFF, 6,  7)
    DeclMonster(299310,  190630,  5000,    0x10100E8,    "BattleInfo_528", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(302640,  192150,  5000,    0x10100E8,    "BattleInfo_528", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(302320,  185940,  5000,    0x10100E8,    "BattleInfo_528", 0,   18,  0xFFFF, 2,  3)

    DeclEvent(0x0000, 0, 9,   0.0,                   14.0,                  -1.0,                  182.25,                [0.1111111119389534,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333134651184,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.0,                  -4.666666507720947,    0.20000000298023224,   1.0])

    DeclActor(4294967056, 10000,   32870,   1200,    4294967056, 11000,   32870,   0x007C, 0,  4,  0x0000)
    DeclActor(296180,  5000,    193510,  1200,    296180,  6000,    193510,  0x007C, 0,  5,  0x0000)
    DeclActor(4294667666, 5000,    160570,  1200,    4294667666, 6000,    160570,  0x007C, 0,  6,  0x0000)
    DeclActor(220,     5250,    324370,  2000,    220,     6750,    324370,  0x007C, 0,  12, 0x0000)
    DeclActor(4294965446, 200,     4294965866, 1200,    4294965446, 1700,    4294965866, 0x007C, 0,  8,  0x0000)
    DeclActor(190,     160,     31000,   2000,    190,     2160,    31000,   0x007C, 0,  13, 0x0000)

    ChipFrameInfo(699, 0, [0, 1, 2, 3, 4, 3, 2, 1])              # 0
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 1
    ChipFrameInfo(699, 0, [0, 1, 2, 3, 4, 5, 6])                 # 2
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5, 6])                # 3
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 4
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4])                      # 5
    ChipFrameInfo(800, 0, [0, 1, 2, 3, 4])                       # 6
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 7

    ScpFunction((
        "Function_0_808",          # 00, 0
        "Function_1_85F",          # 01, 1
        "Function_2_87E",          # 02, 2
        "Function_3_89D",          # 03, 3
        "Function_4_C91",          # 04, 4
        "Function_5_EAD",          # 05, 5
        "Function_6_FFF",          # 06, 6
        "Function_7_1151",         # 07, 7
        "Function_8_1155",         # 08, 8
        "Function_9_124B",         # 09, 9
        "Function_10_1DAB",        # 0A, 10
        "Function_11_1FCB",        # 0B, 11
        "Function_12_2995",        # 0C, 12
        "Function_13_2B21",        # 0D, 13
    ))


    def Function_0_808(): pass

    label("Function_0_808")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_85E")
    SetChrSubChip(0xFE, 0x0)
    Sleep(100)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    SetChrSubChip(0xFE, 0x3)
    Sleep(100)
    SetChrSubChip(0xFE, 0x4)
    Sleep(100)
    SetChrSubChip(0xFE, 0x5)
    Sleep(100)
    SetChrSubChip(0xFE, 0x4)
    Sleep(100)
    SetChrSubChip(0xFE, 0x3)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    Jump("Function_0_808")

    label("loc_85E")

    Return()

    # Function_0_808 end

    def Function_1_85F(): pass

    label("Function_1_85F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_87D")
    OP_A1(0xFE, 0x2BC, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_1_85F")

    label("loc_87D")

    Return()

    # Function_1_85F end

    def Function_2_87E(): pass

    label("Function_2_87E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6E), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x125, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x121, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x121, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_89C")
    Event(0, 10)

    label("loc_89C")

    Return()

    # Function_2_87E end

    def Function_3_89D(): pass

    label("Function_3_89D")

    OP_52(0xA, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xC3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xC3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xC3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xC3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xC3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xC3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xC3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xC3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x120, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x121, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BD8")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_BD8")

    OP_65(0x5, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x125, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BEA")
    OP_66(0x5, 0x1)

    label("loc_BEA")

    ClearMapObjFlags(0x3, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x125, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C07")
    OP_70(0x3, 0x0)
    OP_70(0x4, 0x0)
    Jump("loc_C0F")

    label("loc_C07")

    OP_70(0x3, 0x14)
    OP_70(0x4, 0x14)

    label("loc_C0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C22")
    OP_70(0x0, 0x0)
    Jump("loc_C26")

    label("loc_C22")

    OP_70(0x0, 0x1E)

    label("loc_C26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C39")
    OP_70(0x1, 0x0)
    Jump("loc_C3D")

    label("loc_C39")

    OP_70(0x1, 0x1E)

    label("loc_C3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C50")
    OP_70(0x2, 0x0)
    Jump("loc_C54")

    label("loc_C50")

    OP_70(0x2, 0x1E)

    label("loc_C54")

    Sound(129, 1, 100, 0)
    OP_1C(0x0, 0x6, 0x0, 0x32, 0x0, 0x7, 0x0, 0x0)
    OP_1C(0x0, 0x7, 0x0, 0x32, 0x0, 0x7, 0x0, 0x0)
    OP_1C(0x0, 0x8, 0x0, 0x32, 0x0, 0x7, 0x0, 0x0)
    LoadEffect(0x10, "event\\eva00_00.eff")
    Return()

    # Function_3_89D end

    def Function_4_C91(): pass

    label("Function_4_C91")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E62")
    Sound(14, 0, 100, 0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21B, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D94")
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0x9, 0x0, 0)
    OP_98(0x9, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_CEE():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_CEE)

    def lambda_D08():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_D08)
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
    Battle("BattleInfo_72C", 0x0, 0x0, 0x0, 0xB, 0xFF)
    SetChrFlags(0x9, 0x80)
    ClearChrFlags(0x9, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_D75"),
        (2, "loc_D84"),
        (1, "loc_D91"),
        (SWITCH_DEFAULT, "loc_D94"),
    )


    label("loc_D75")

    SetScenarioFlags(0x21B, 0)
    OP_70(0x0, 0x1E)
    Sleep(500)
    Jump("loc_D94")

    label("loc_D84")

    OP_70(0x0, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_D91")

    OP_B9(0x0)
    Return()

    label("loc_D94")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x96, 1)"), scpexpr(EXPR_END)), "loc_DED")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x96),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1E1, 5)
    OP_E0(0x5, 0x0)
    Jump("loc_E5D")

    label("loc_DED")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x96),
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

    label("loc_E5D")

    Jump("loc_EA1")

    label("loc_E62")

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

    label("loc_EA1")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_C91 end

    def Function_5_EAD(): pass

    label("Function_5_EAD")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FA9")
    Sound(14, 0, 100, 0)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1F5, 1)"), scpexpr(EXPR_END)), "loc_F32")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1F5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1E1, 6)
    OP_E0(0x5, 0x0)
    Jump("loc_FA4")

    label("loc_F32")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1F5),
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

    label("loc_FA4")

    Jump("loc_FF3")

    label("loc_FA9")

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

    label("loc_FF3")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_EAD end

    def Function_6_FFF(): pass

    label("Function_6_FFF")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10FB")
    Sound(14, 0, 100, 0)
    OP_74(0x2, 0x1E)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1F8, 1)"), scpexpr(EXPR_END)), "loc_1084")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1F8),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1E1, 7)
    OP_E0(0x5, 0x0)
    Jump("loc_10F6")

    label("loc_1084")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1F8),
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

    label("loc_10F6")

    Jump("loc_1145")

    label("loc_10FB")

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

    label("loc_1145")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_FFF end

    def Function_7_1151(): pass

    label("Function_7_1151")

    Call(1, 6)
    Return()

    # Function_7_1151 end

    def Function_8_1155(): pass

    label("Function_8_1155")

    OP_F4(0x2)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is an orbment charging station.\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Rest Here\x01",      # 0
            "Quit\x01",           # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_123C")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_74(0x5, 0x1E)
    Sound(7, 0, 100, 0)
    OP_70(0x5, 0x0)
    OP_71(0x5, 0x0, 0x1E, 0x0, 0x0)
    OP_79(0x5)
    OP_71(0x5, 0x1F, 0x186, 0x0, 0x20)
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
    OP_70(0x5, 0x0)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_123C")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_8_1155 end

    def Function_9_124B(): pass

    label("Function_9_124B")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    OP_E2(0x3)
    CreatePortrait(0, 224, 0, 480, 256, 0, 16, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu01903.itp")
    CreatePortrait(1, 224, 0, 480, 256, 0, 16, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu01001.itp")
    CreatePortrait(2, 224, 0, 480, 256, 0, 16, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu01201.itp")
    CreatePortrait(3, 224, 0, 480, 256, 0, 16, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu01105.itp")
    SoundLoad(2707)
    SoundLoad(4125)
    SoundLoad(3593)
    SoundLoad(3594)
    OP_68(0, 1000, 18350, 0)
    MoveCamera(317, 22, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(19000, 0)
    SetChrPos(0x101, 500, 0, 13500, 0)
    SetChrPos(0x109, -800, 0, 13200, 0)

    def lambda_137A():
        OP_97(0x101, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_137A)
    Sleep(100)

    def lambda_1397():
        OP_97(0x109, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1397)
    SetCameraDistance(17000, 2500)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x109, 0)
    OP_6F(0x79)

    ChrTalk(
        0x109,
        "#10111F#6PThat's...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00013F#6PAnother door...\x02",
    )

    CloseMessageWindow()
    OP_68(-710, 1000, 28570, 5000)

    def lambda_1413():
        OP_97(0x101, 0x0, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1413)
    Sleep(100)

    def lambda_1430():
        OP_97(0x109, 0x0, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1430)
    WaitChrThread(0x109, 0)
    OP_6F(0x79)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The stone door is shut tight.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#6P#00003FNo good, huh...\x02\x03",
            "#00008FThere should be a switch around here\x01",
            "like the door near the entrance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10101F#6PYes, let's look around.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x109,
        (
            "#10113F#5PAnyway...\x01",
            "I wonder how Mr. Dudley and Mr.\x01",
            "Arios are holding up on their side.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x109, 500)
    Sleep(100)

    ChrTalk(
        0x101,
        (
            "#12P#00006FI'm pretty sure that those two\x01",
            "aren't capable of slowing down...\x02\x03",
            "#00008FThough the enemy is still in possession\x01",
            "of Gnosis and those dangerous dolls.\x02\x03",
            "#00001FWe shouldn't get too optimistic now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10108F#5PRight...\x02\x03",
            "#10106F*sigh*, at times like this, it would be helpful\x01",
            "if we could contact them with our ENIGMAs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00006FYeah. But that's still only possible within the\x01",
            "borders of Crossbell and in the autonomous state\x01",
            "of Leman where the Foundation is established.\x02\x03",
            "#00000FBut now that you mention it, having that\x01",
            "functionality sure came in handy.\x02\x03",
            "We were also able to receive Fran's support.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10112F#5PAhaha... It would be nice\x01",
            "if she was really of help.\x02\x03",
            "#10100FI'm worried about if she's properly\x01",
            "working, considering how she is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00009FHa ha, are you talking about when she came\x01",
            "to see us off at the station with KeA before\x01",
            "we departed to Altair City, right?\x02\x03",
            "#00002FIsn't that alright?\x01",
            "She was worried about you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F#5PBut it's not enough reason for skipping\x01",
            "during working hours to come see me...\x02\x03",
            "#10101FAfter all, she did try to board\x01",
            "the train together with KeA.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00004FHa ha. This time KeA too was\x01",
            "throwing one of her rare tantrums.\x02",
        )
    )

    CloseMessageWindow()
    VolumeBGM(0x46, 0x3E8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(300)
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(14, 280, 35, 3)
    SetChrName("Fran")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xC),
            "#2707V#30WBig sis, Mr. Lloyd!\x01",
            "Please be very careful, okay!?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    OP_24(0xA93)
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(300)
    SetChrName("Chief Sergei")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xC),
            "#30WWell, don't let your guard down.\x02\x03",
            "Even though they're fugitives right \x01",
            "now, they still are affiliated with \x01",
            "the Cult.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    Sleep(300)
    OP_C9(0x0, 0x80000000)
    SetChrName("Zeit")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xC),
            "#4125V#30WWoof.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0x101D)
    OP_57(0x0)
    OP_5A()
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CB(0x3, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x3, 0x3)
    Sleep(500)
    SetChrName("KeA")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xC),
            "#3593V#30WLloyd...\x01",
            "Come back safely, ok?\x02\x03",
            "#3594VKeA will be a good girl\x01",
            "and wait for you...!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xE0A)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x80000000)
    FadeToBright(800, 0)
    OP_CB(0x3, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x3, 0x3)
    VolumeBGM(0x64, 0x3E8)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#12P#00004FPeople important to us\x01",
            "are waiting in Crossbell...\x02\x03",
            "#00000FWhatever happens, let's make this \x01",
            "mission a success and head back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10102F#5P...Yes!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    SetChrPos(0x0, 530, 0, 27590, 180)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x121, 0)
    ModifyEventFlags(0, 0, 0x80)
    OP_E2(0x2)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_9_124B end

    def Function_10_1DAB(): pass

    label("Function_10_1DAB")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    LoadChrToIndex("monster/ch80750.itc", 0x1E)
    LoadChrToIndex("chr/ch00050.itc", 0x1F)
    LoadChrToIndex("chr/ch00051.itc", 0x20)
    LoadChrToIndex("chr/ch02950.itc", 0x21)
    LoadChrToIndex("chr/ch02951.itc", 0x22)
    OP_68(0, 6000, 201500, 0)
    MoveCamera(323, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(19000, 0)
    SetChrPos(0x101, 800, 5000, 205100, 180)
    SetChrPos(0x109, -600, 5000, 205500, 180)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x8000)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, 0, 5000, 191500, 0)
    OP_52(0x8, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xC7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_1E75():
        OP_97(0x101, 0x0, 0x0, 0xFFFFE4A8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1E75)
    Sleep(50)

    def lambda_1E92():
        OP_97(0x109, 0x0, 0x0, 0xFFFFE4A8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1E92)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x101, 0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    WaitChrThread(0x109, 0)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_6F(0x79)
    Fade(250)
    SetChrChipByIndex(0x101, 0x1F)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x109, 0x21)
    SetChrSubChip(0x109, 0x0)
    Sound(531, 0, 100, 0)
    Sound(805, 0, 100, 0)
    OP_0D()
    BeginChrThread(0x8, 0, 0, 0)
    OP_68(0, 6100, 195000, 2000)
    MoveCamera(311, 21, 0, 2000)
    SetCameraDistance(17500, 2000)
    OP_6F(0x79)
    Sleep(800)
    BlurSwitch(0x258, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_68(0, 6300, 193700, 600)
    SetCameraDistance(15000, 600)

    def lambda_1F6B():
        OP_96(0xFE, 0x320, 0x0, 0x2E824, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1F6B)
    Sleep(50)

    def lambda_1F88():
        OP_96(0xFE, 0xFFFFFDA8, 0x0, 0x2E824, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1F88)
    Sleep(550)
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x109, 0xFF)
    Battle("BattleInfo_6E8", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x8, 0x80)
    Call(0, 11)
    Return()

    # Function_10_1DAB end

    def Function_11_1FCB(): pass

    label("Function_11_1FCB")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch02950.itc", 0x1F)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis221.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis222.itp")
    OP_68(150, 6100, 196150, 0)
    MoveCamera(320, 21, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16000, 0)
    OP_F0(0x0, 0x1)
    SetChrPos(0x101, 800, 5000, 196000, 180)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrPos(0x109, -700, 5000, 196300, 180)
    SetChrChipByIndex(0x109, 0x1F)
    SetChrSubChip(0x109, 0x0)
    SetCameraDistance(15000, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#11P#00000FAll right...!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    Sound(531, 0, 100, 0)
    Sound(805, 0, 100, 0)
    OP_0D()

    def lambda_20FE():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_20FE)
    Sleep(100)
    TurnDirection(0x101, 0x109, 500)
    Sleep(150)

    ChrTalk(
        0x109,
        (
            "#10109F#5PUh uh, good job.\x02\x03",
            "#10106FEven so...\x01",
            "What could be the real purpose\x01",
            "of that Ernest to come here?\x02\x03",
            "#10101FIt didn't look like the former Chairman\x01",
            "tagged along voluntarily...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003F...I have no idea.\x02\x03",
            "#00001FBut it looks like he's trying\x01",
            "to obtain a power similar to\x01",
            "the one Joachim had.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105F#5PThe same as the Cult's mastermind...\x02\x03",
            "#10101FYou mean, the power he used to control\x01",
            "the mafia and the Bellguard Gate unit?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00006FYeah... What's worse though is that it\x01",
            "also allows him to "look" into...\x02\x03",
            "#00013FThe hearts and memories of people.\x02",
        )
    )

    CloseMessageWindow()
    VolumeBGM(0x46, 0x3E8)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    FadeToDark(0, 0, -1)
    Sleep(500)
    OP_CB(0x0, 0x3, 0xAAFFFFFF, 0x12C, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_C9(0x0, 0x800)
    SetMessageWindowPos(30, 60, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#30WThis guy...\x01",
            "He's peeking into our memories!?\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(100, 110, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#30WCould it be that...\x01",
            "He's recreating them!?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x800)
    FadeToBright(800, 0)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    Sleep(500)
    VolumeBGM(0x64, 0x3E8)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x109,
        (
            "#10107F#5PT-That's...\x01",
            "That's all kinds of horrible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003FYeah. The ways in which you can abuse\x01",
            "that power are pretty much limitless.\x02\x03",
            "#00008FAnd to make things worse──\x02",
        )
    )

    CloseMessageWindow()
    VolumeBGM(0x46, 0x3E8)
    Sound(824, 0, 100, 0)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    FadeToDark(0, 0, -1)
    Sleep(500)
    OP_CB(0x1, 0x3, 0xAAFFFFFF, 0x12C, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    FadeToDark(0, 0, -1)
    Sound(1005, 0, 80, 0)
    OP_C9(0x0, 0x800)
    SetMessageWindowPos(-1, 120, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xB),
            "#60WI CAN SEE EVERYTHING...\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xB),
            "#60WTHE TRICK BEHIND MASTER KeA'S DISAPPEARANCE...\x01",
            "THE TRUTH BEHIND YOUR OLDER BROTHER'S DEATH...\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xB),
            "#60WAND THE INEVITABLE FATE OF CROSSBELL...\x07\x00\x01\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x800)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    FadeToBright(800, 0)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    VolumeBGM(0x64, 0x3E8)
    Sleep(1000)

    ChrTalk(
        0x109,
        "#10105F#5PMr. Lloyd...?\x02",
    )

    CloseMessageWindow()
    OP_64(0x101)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#12P#00003F...No, it's nothing.\x02\x03",
            "#00008FAt any rate, we have to stop \x01",
            "Ernest before he ends up \x01",
            "the same way Joachim did.\x02\x03",
            "#00013FDefinitely...\x01",
            "We have to catch him alive.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x109,
        (
            "#10113F#5PMr. Lloyd...\x02\x03",
            "#10106FUhmm, don't blame yourself\x01",
            "for Joachim's death...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00006FBut still...\x01",
            "I was just thinking... I could've\x01",
            "caught him without him dying...\x02\x03",
            "#00008FBut... I know it's far too late for that now...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10108F#5P...........\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00004FHa ha. If I keep moping around like this,\x01",
            "Randy will surely yell at me again.\x02\x03",
            "#00000F──Let's go. We need to meet up with \x01",
            "Mr. Arios and Mr. Dudley.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10100F#5PYes...!\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(15250, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_37()
    OP_CC(0x1, 0xFF, 0x0)
    SetChrPos(0x0, 0, 5000, 196600, 180)
    OP_69(0xFF, 0x0)
    OP_F0(0x0, 0xA)
    SetScenarioFlags(0x121, 1)
    OP_E2(0x2)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_11_1FCB end

    def Function_12_2995(): pass

    label("Function_12_2995")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x125, 1)), scpexpr(EXPR_END)), "loc_29E8")
    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It looks like it will not budge anymore.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Jump("loc_2B20")

    label("loc_29E8")

    EventBegin(0x1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a switch.\x01",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B19")
    Fade(500)
    OP_68(290, 6300, 321960, 0)
    MoveCamera(330, 35, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17000, 0)
    SetChrPos(0x0, 910, 5000, 322080, 1)
    SetChrPos(0x1, -220, 5000, 322120, 1)
    OP_0D()
    Sleep(500)
    Sound(143, 0, 100, 0)
    OP_71(0x4, 0x0, 0x14, 0x0, 0x0)
    Sleep(1000)
    Fade(500)
    OP_68(-1250, 1300, 28830, 0)
    MoveCamera(336, 28, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(20000, 0)
    OP_0D()
    Sleep(500)
    Sound(155, 2, 100, 0)
    OP_74(0x3, 0xF)
    OP_71(0x3, 0x0, 0x14, 0x0, 0x0)
    Sleep(1300)
    OP_24(0x9B)
    Sound(149, 0, 100, 0)
    OP_82(0x64, 0x0, 0x3E8, 0x64)
    Sleep(1000)
    SetScenarioFlags(0x125, 1)
    OP_65(0x5, 0x1)

    label("loc_2B19")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)

    label("loc_2B20")

    Return()

    # Function_12_2995 end

    def Function_13_2B21(): pass

    label("Function_13_2B21")

    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The stone door is shut tight.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_13_2B21 end

    SaveToFile()

Try(main)
