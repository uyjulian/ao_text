from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "m0100.bin",                # FileName
        "m0100",                    # MapName
        "m0100",                    # Location
        0x0068,                     # MapIndex
        "ed7300",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 104, 0, 0, 0, 1],
    )

    BuildStringList((
        "m0100",                  # 0
        "bm0101",                 # 1
        "bm0101",                 # 2
        "bm0101",                 # 3
        "bm0101",                 # 4
        "bm0100",                 # 5
        "bm0100",                 # 6
        "bm0100",                 # 7
        "bm0100",                 # 8
    ))

    ATBonus("ATBonus_35C", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_2058", 6,   0,   11,  0,   0,   4,   6)
    Sepith("Sepith_2060", 11,  1,   8,   0,   3,   7,   0)
    Sepith("Sepith_2068", 0,   0,   0,   8,   6,   6,   6)
    Sepith("Sepith_2050", 0,   10,  5,   0,   6,   2,   4)

    MonsterBattlePostion("MonsterBattlePostion_3FC", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_400", 6, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_404", 10, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_408", 7, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_40C", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_410", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_414", 10, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_418", 6, 15, 180)
    MonsterBattlePostion("MonsterBattlePostion_43C", 8, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_440", 8, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_444", 5, 6, 45)
    MonsterBattlePostion("MonsterBattlePostion_448", 11, 10, 225)
    MonsterBattlePostion("MonsterBattlePostion_44C", 11, 6, 315)
    MonsterBattlePostion("MonsterBattlePostion_450", 5, 10, 135)
    MonsterBattlePostion("MonsterBattlePostion_454", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_458", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_3DC", 7, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_3E0", 9, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_3E4", 6, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_3E8", 10, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_3EC", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_3F0", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_3F4", 7, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_3F8", 9, 15, 180)
    MonsterBattlePostion("MonsterBattlePostion_3BC", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_3C0", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_3C4", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_3C8", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_3CC", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_3D0", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_3D4", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_3D8", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_41C", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_420", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_424", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_428", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_42C", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_430", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_434", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_438", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_39C", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_3A0", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_3A4", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_3A8", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_3AC", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_3B0", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_3B4", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_3B8", 2, 13, 180)

    # monster count: 9

    BattleInfo(
        "BattleInfo_524", 0x0000, 62, 6, 60, 6, 1, 30, 0, "bm0101", "Sepith_2058", 30, 45, 20, 5,
        (
            ("ms68700.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3FC", "MonsterBattlePostion_43C", "ed7450", "ed7453", "ATBonus_35C"),
            ("ms68700.dat", "ms68700.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3DC", "MonsterBattlePostion_43C", "ed7450", "ed7453", "ATBonus_35C"),
            ("ms68700.dat", "ms63800.dat", "ms68700.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_3FC", "MonsterBattlePostion_43C", "ed7450", "ed7453", "ATBonus_35C"),
            ("ms68700.dat", "ms68700.dat", "ms63800.dat", "ms68700.dat", 0, 0, 0, 0, "MonsterBattlePostion_3DC", "MonsterBattlePostion_43C", "ed7450", "ed7453", "ATBonus_35C"),
        )
    )

    BattleInfo(
        "BattleInfo_90C", 0x0000, 62, 6, 60, 6, 1, 25, 0, "bm0100", "Sepith_2060", 30, 45, 20, 5,
        (
            ("ms75800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3BC", "MonsterBattlePostion_41C", "ed7450", "ed7453", "ATBonus_35C"),
            ("ms75800.dat", "ms75800.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_39C", "MonsterBattlePostion_41C", "ed7450", "ed7453", "ATBonus_35C"),
            ("ms75800.dat", "ms68700.dat", "ms75800.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_3BC", "MonsterBattlePostion_41C", "ed7450", "ed7453", "ATBonus_35C"),
            ("ms75800.dat", "ms75800.dat", "ms68700.dat", "ms75800.dat", 0, 0, 0, 0, "MonsterBattlePostion_39C", "MonsterBattlePostion_41C", "ed7450", "ed7453", "ATBonus_35C"),
        )
    )

    BattleInfo(
        "BattleInfo_6B4", 0x0000, 62, 6, 60, 6, 1, 40, 0, "bm0101", "Sepith_2068", 30, 45, 20, 5,
        (
            ("ms60500.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3FC", "MonsterBattlePostion_43C", "ed7450", "ed7453", "ATBonus_35C"),
            ("ms60500.dat", "ms60500.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3DC", "MonsterBattlePostion_43C", "ed7450", "ed7453", "ATBonus_35C"),
            ("ms60500.dat", "ms60500.dat", "ms60500.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_3FC", "MonsterBattlePostion_43C", "ed7450", "ed7453", "ATBonus_35C"),
            ("ms60500.dat", "ms60500.dat", "ms60500.dat", "ms60500.dat", 0, 0, 0, 0, "MonsterBattlePostion_3DC", "MonsterBattlePostion_43C", "ed7450", "ed7453", "ATBonus_35C"),
        )
    )

    BattleInfo(
        "BattleInfo_77C", 0x0000, 62, 6, 60, 6, 1, 40, 0, "bm0100", "Sepith_2050", 30, 45, 20, 5,
        (
            ("ms63800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3BC", "MonsterBattlePostion_41C", "ed7450", "ed7453", "ATBonus_35C"),
            ("ms63800.dat", "ms63800.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_39C", "MonsterBattlePostion_41C", "ed7450", "ed7453", "ATBonus_35C"),
            ("ms63800.dat", "ms75800.dat", "ms63800.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_3BC", "MonsterBattlePostion_41C", "ed7450", "ed7453", "ATBonus_35C"),
            ("ms63800.dat", "ms63800.dat", "ms75800.dat", "ms63800.dat", 0, 0, 0, 0, "MonsterBattlePostion_39C", "MonsterBattlePostion_41C", "ed7450", "ed7453", "ATBonus_35C"),
        )
    )

    BattleInfo(
        "BattleInfo_844", 0x0000, 62, 6, 60, 6, 1, 30, 0, "bm0100", "Sepith_2058", 30, 45, 20, 5,
        (
            ("ms68700.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3BC", "MonsterBattlePostion_41C", "ed7450", "ed7453", "ATBonus_35C"),
            ("ms68700.dat", "ms68700.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_39C", "MonsterBattlePostion_41C", "ed7450", "ed7453", "ATBonus_35C"),
            ("ms68700.dat", "ms63800.dat", "ms68700.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_3BC", "MonsterBattlePostion_41C", "ed7450", "ed7453", "ATBonus_35C"),
            ("ms68700.dat", "ms68700.dat", "ms63800.dat", "ms68700.dat", 0, 0, 0, 0, "MonsterBattlePostion_39C", "MonsterBattlePostion_41C", "ed7450", "ed7453", "ATBonus_35C"),
        )
    )

    BattleInfo(
        "BattleInfo_5EC", 0x0000, 62, 6, 60, 6, 1, 25, 0, "bm0101", "Sepith_2060", 30, 45, 20, 5,
        (
            ("ms75800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3FC", "MonsterBattlePostion_43C", "ed7450", "ed7453", "ATBonus_35C"),
            ("ms75800.dat", "ms75800.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3DC", "MonsterBattlePostion_43C", "ed7450", "ed7453", "ATBonus_35C"),
            ("ms75800.dat", "ms68700.dat", "ms75800.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_3FC", "MonsterBattlePostion_43C", "ed7450", "ed7453", "ATBonus_35C"),
            ("ms75800.dat", "ms75800.dat", "ms68700.dat", "ms75800.dat", 0, 0, 0, 0, "MonsterBattlePostion_3DC", "MonsterBattlePostion_43C", "ed7450", "ed7453", "ATBonus_35C"),
        )
    )

    BattleInfo(
        "BattleInfo_9D4", 0x0000, 62, 6, 60, 6, 1, 40, 0, "bm0100", "Sepith_2068", 30, 45, 20, 5,
        (
            ("ms60500.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3BC", "MonsterBattlePostion_41C", "ed7450", "ed7453", "ATBonus_35C"),
            ("ms60500.dat", "ms60500.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_39C", "MonsterBattlePostion_41C", "ed7450", "ed7453", "ATBonus_35C"),
            ("ms60500.dat", "ms60500.dat", "ms60500.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_3BC", "MonsterBattlePostion_41C", "ed7450", "ed7453", "ATBonus_35C"),
            ("ms60500.dat", "ms60500.dat", "ms60500.dat", "ms60500.dat", 0, 0, 0, 0, "MonsterBattlePostion_39C", "MonsterBattlePostion_41C", "ed7450", "ed7453", "ATBonus_35C"),
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
        "monster/ch63850.itc",               # 10
        "monster/ch63851.itc",               # 11
        "monster/ch68750.itc",               # 12
        "monster/ch68750.itc",               # 13
        "monster/ch75850.itc",               # 14
        "monster/ch75851.itc",               # 15
        "monster/ch60550.itc",               # 16
        "monster/ch60550.itc",               # 17
    ))

    DeclMonster(194920,  60,      0,       0x1010000,    "BattleInfo_524", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(399500,  10,      0,       0x1010000,    "BattleInfo_90C", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(199710,  4294866946, 0,       0x1010000,    "BattleInfo_6B4", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(199570,  4294764116, 0,       0x1010000,    "BattleInfo_77C", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(300340,  4294867256, 4000,    0x1010000,    "BattleInfo_844", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(214950,  4294951086, 4000,    0x1010000,    "BattleInfo_5EC", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(199840,  4294964146, 4000,    0x1010000,    "BattleInfo_6B4", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(199810,  199380,  0,       0x1010000,    "BattleInfo_77C", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(299660,  303250,  0,       0x1010000,    "BattleInfo_9D4", 0,   22,  0xFFFF, 6,  7)

    DeclEvent(0x0000, 0, 12,  32.0,                  7.900000095367432,     -8.850000381469727,    225.0,                 [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.10000000149011612,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -10.666666984558105,   -0.7900000214576721,   1.7700001001358032,    1.0])

    DeclActor(200000,  0,       4294767296, 1200,    200000,  1000,    4294767296, 0x007C, 0,  2,  0x0000)
    DeclActor(300000,  0,       300000,  1200,    300000,  1000,    300000,  0x007C, 0,  3,  0x0000)
    DeclActor(0,       0,       102000,  1200,    0,       1000,    102500,  0x007C, 0,  5,  0x0000)
    DeclActor(100000,  0,       202000,  1200,    100000,  1000,    202500,  0x007C, 0,  7,  0x0000)
    DeclActor(402000,  0,       200000,  1200,    402500,  1000,    200000,  0x007C, 0,  9,  0x0000)
    DeclActor(27500,   4294959296, 11700,   1200,    27500,   4294960296, 11700,   0x007C, 0,  4,  0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 0
    ChipFrameInfo(2000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 2
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 5])                   # 3
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 4
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4, 5])                   # 5
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 6
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 7

    ScpFunction((
        "Function_0_B30",          # 00, 0
        "Function_1_B97",          # 01, 1
        "Function_2_1009",         # 02, 2
        "Function_3_115B",         # 03, 3
        "Function_4_12AD",         # 04, 4
        "Function_5_130D",         # 05, 5
        "Function_6_149D",         # 06, 6
        "Function_7_15E4",         # 07, 7
        "Function_8_1774",         # 08, 8
        "Function_9_18BB",         # 09, 9
        "Function_10_1A4B",        # 0A, 10
        "Function_11_1B92",        # 0B, 11
        "Function_12_1F9D",        # 0C, 12
    ))


    def Function_0_B30(): pass

    label("Function_0_B30")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B96")
    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B5D")
    OP_D2(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 6)
    Jump("loc_B96")

    label("loc_B5D")

    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B7C")
    OP_D2(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 8)
    Jump("loc_B96")

    label("loc_B7C")

    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B96")
    OP_D2(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 10)

    label("loc_B96")

    Return()

    # Function_0_B30 end

    def Function_1_B97(): pass

    label("Function_1_B97")

    SetMapFlags(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x85), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BB0")
    VolumeBGM(0x64, 0x64)

    label("loc_BB0")

    ClearMapObjFlags(0x14, 0x10)
    SetMapObjFrame(0xF, "m00ele00", 0x2, "up_kp")
    SetMapObjFrame(0x10, "m00ele00", 0x2, "up_kp")
    SetMapObjFrame(0x11, "m00ele00", 0x2, "up_kp")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6D), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6E), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x70), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x72), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x74), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x75), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x77), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C3B")
    Sound(122, 1, 100, 0)
    Jump("loc_C3E")

    label("loc_C3B")

    OP_24(0x7A)

    label("loc_C3E")

    SetMapObjFrame(0x0, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x0, "light01", 0x0, 0x1)
    SetMapObjFrame(0x1, "sign00", 0x0, 0x1)
    SetMapObjFrame(0x1, "light00", 0x0, 0x1)
    SetMapObjFrame(0x1, "sign01", 0x1, 0x1)
    SetMapObjFrame(0x1, "light01", 0x1, 0x1)
    ClearMapObjFlags(0x1, 0x10)
    SetMapObjFrame(0x2, "sign00", 0x0, 0x1)
    SetMapObjFrame(0x2, "light00", 0x0, 0x1)
    SetMapObjFrame(0x2, "sign01", 0x1, 0x1)
    SetMapObjFrame(0x2, "light01", 0x1, 0x1)
    ClearMapObjFlags(0x2, 0x10)
    SetMapObjFrame(0x3, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x3, "light01", 0x0, 0x1)
    SetMapObjFrame(0x4, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x4, "light01", 0x0, 0x1)
    SetMapObjFrame(0x5, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x5, "light01", 0x0, 0x1)
    SetMapObjFrame(0x6, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x6, "light01", 0x0, 0x1)
    SetMapObjFrame(0x7, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x7, "light01", 0x0, 0x1)
    SetMapObjFrame(0x8, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x8, "light01", 0x0, 0x1)
    SetMapObjFrame(0x9, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x9, "light01", 0x0, 0x1)
    SetMapObjFrame(0xA, "sign01", 0x0, 0x1)
    SetMapObjFrame(0xA, "light01", 0x0, 0x1)
    SetMapObjFrame(0xB, "sign01", 0x0, 0x1)
    SetMapObjFrame(0xB, "light01", 0x0, 0x1)
    SetMapObjFrame(0xC, "sign01", 0x0, 0x1)
    SetMapObjFrame(0xC, "light01", 0x0, 0x1)
    SetMapObjFrame(0xD, "sign01", 0x0, 0x1)
    SetMapObjFrame(0xD, "light01", 0x0, 0x1)
    SetMapObjFrame(0xE, "sign01", 0x0, 0x1)
    SetMapObjFrame(0xE, "light01", 0x0, 0x1)
    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E4F")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_E4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E6E")
    OP_10(0x1E, 0x0)
    OP_10(0x28, 0x1)
    OP_10(0x1F, 0x0)
    OP_10(0x29, 0x1)
    Jump("loc_E7A")

    label("loc_E6E")

    OP_10(0x1E, 0x1)
    OP_10(0x28, 0x0)
    OP_10(0x1F, 0x1)
    OP_10(0x29, 0x0)

    label("loc_E7A")

    OP_52(0xB, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EF, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FED")
    OP_70(0x12, 0x0)
    Jump("loc_FF1")

    label("loc_FED")

    OP_70(0x12, 0x1E)

    label("loc_FF1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EF, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1004")
    OP_70(0x13, 0x0)
    Jump("loc_1008")

    label("loc_1004")

    OP_70(0x13, 0x1E)

    label("loc_1008")

    Return()

    # Function_1_B97 end

    def Function_2_1009(): pass

    label("Function_2_1009")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EF, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1105")
    Sound(14, 0, 100, 0)
    OP_74(0x12, 0x1E)
    OP_71(0x12, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x3E, 1)"), scpexpr(EXPR_END)), "loc_108E")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x3E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1EF, 2)
    OP_E0(0x5, 0x0)
    Jump("loc_1100")

    label("loc_108E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x3E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " is inside the chest.\x01",
            "Since you have too many, you gave it up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x12, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1100")

    Jump("loc_114F")

    label("loc_1105")

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

    label("loc_114F")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_1009 end

    def Function_3_115B(): pass

    label("Function_3_115B")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EF, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1257")
    Sound(14, 0, 100, 0)
    OP_74(0x13, 0x1E)
    OP_71(0x13, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1F9, 1)"), scpexpr(EXPR_END)), "loc_11E0")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1F9),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1EF, 3)
    OP_E0(0x5, 0x0)
    Jump("loc_1252")

    label("loc_11E0")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1F9),
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

    label("loc_1252")

    Jump("loc_12A1")

    label("loc_1257")

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

    label("loc_12A1")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_115B end

    def Function_4_12AD(): pass

    label("Function_4_12AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12BF")
    Call(0, 11)
    Jump("loc_130C")

    label("loc_12BF")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    Sound(807, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a sturdy padlock\x01",
            "at the duct entrance.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)

    label("loc_130C")

    Return()

    # Function_4_12AD end

    def Function_5_130D(): pass

    label("Function_5_130D")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1495")
    Fade(500)
    SetChrPos(0x0, 600, 0, 100600, 0)
    SetChrPos(0x1, -600, 0, 100600, 0)
    SetChrPos(0x2, -600, 0, 99400, 0)
    SetChrPos(0x3, 600, 0, 99400, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13F3")
    SetChrPos(0x4, -600, 0, 98200, 0)
    SetChrPos(0x5, 600, 0, 98200, 0)
    Jump("loc_1412")

    label("loc_13F3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1412")
    SetChrPos(0x4, 0, 0, 98200, 0)

    label("loc_1412")

    OP_68(0, 1000, 100000, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(30000, 0)
    OP_0D()
    Sleep(500)
    Sound(144, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_68(0, -4000, 100000, 2000)
    SetMapObjFrame(0xF, "m00ele00", 0x2, "down")
    Sleep(1000)
    OP_D2(0x0, (scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("m0110", 0, 0, 0)
    IdleLoop()

    label("loc_1495")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_5_130D end

    def Function_6_149D(): pass

    label("Function_6_149D")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    OP_6F(0x1)
    OP_69(0x1, 0x0)
    SetMapObjFrame(0xF, "m00ele00", 0x2, "down_kp")
    Sleep(1)
    OP_68(0, -4000, 100000, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(30000, 0)
    OP_90(0x0, 600, -10000, 100600, 0)
    OP_90(0x1, -600, -10000, 100600, 0)
    OP_90(0x2, -600, -10000, 99400, 0)
    OP_90(0x3, 600, -10000, 99400, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1572")
    OP_90(0x4, -600, -10000, 98200, 0)
    OP_90(0x5, 600, -10000, 98200, 0)
    Jump("loc_1591")

    label("loc_1572")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1591")
    OP_90(0x4, 0, -10000, 98200, 0)

    label("loc_1591")

    Sound(145, 0, 100, 0)
    OP_68(0, 1000, 100000, 3000)
    SetMapObjFrame(0xF, "m00ele00", 0x2, "up")
    FadeToBright(500, 0)
    Sleep(3400)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_79(0xF)
    OP_6F(0x1)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_6_149D end

    def Function_7_15E4(): pass

    label("Function_7_15E4")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_176C")
    Fade(500)
    SetChrPos(0x0, 100600, 0, 200600, 0)
    SetChrPos(0x1, 99400, 0, 200600, 0)
    SetChrPos(0x2, 99400, 0, 199400, 0)
    SetChrPos(0x3, 100600, 0, 199400, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_16CA")
    SetChrPos(0x4, 99400, 0, 198200, 0)
    SetChrPos(0x5, 100600, 0, 198200, 0)
    Jump("loc_16E9")

    label("loc_16CA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_16E9")
    SetChrPos(0x4, 100000, 0, 198200, 0)

    label("loc_16E9")

    OP_68(100000, 1000, 200000, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(30000, 0)
    OP_0D()
    Sleep(500)
    Sound(144, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_68(100000, -4000, 200000, 2000)
    SetMapObjFrame(0x10, "m00ele00", 0x2, "down")
    Sleep(1000)
    OP_D2(0x0, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("m0113", 0, 0, 0)
    IdleLoop()

    label("loc_176C")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_7_15E4 end

    def Function_8_1774(): pass

    label("Function_8_1774")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    OP_6F(0x1)
    OP_69(0x1, 0x0)
    SetMapObjFrame(0x10, "m00ele00", 0x2, "down_kp")
    Sleep(1)
    OP_68(100000, -4000, 200000, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(30000, 0)
    OP_90(0x0, 100600, -10000, 200600, 0)
    OP_90(0x1, 99400, -10000, 200600, 0)
    OP_90(0x2, 99400, -10000, 199400, 0)
    OP_90(0x3, 100600, -10000, 199400, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1849")
    OP_90(0x4, 99400, -10000, 198200, 0)
    OP_90(0x5, 100600, -10000, 198200, 0)
    Jump("loc_1868")

    label("loc_1849")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1868")
    OP_90(0x4, 100000, -10000, 198200, 0)

    label("loc_1868")

    Sound(145, 0, 100, 0)
    OP_68(100000, 1000, 200000, 3000)
    SetMapObjFrame(0x10, "m00ele00", 0x2, "up")
    FadeToBright(500, 0)
    Sleep(3400)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_79(0x10)
    OP_6F(0x1)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_8_1774 end

    def Function_9_18BB(): pass

    label("Function_9_18BB")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A43")
    Fade(500)
    SetChrPos(0x0, 400600, 0, 200600, 90)
    SetChrPos(0x1, 400600, 0, 199400, 90)
    SetChrPos(0x2, 399400, 0, 199400, 90)
    SetChrPos(0x3, 399400, 0, 200600, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_19A1")
    SetChrPos(0x4, 398200, 0, 199400, 90)
    SetChrPos(0x5, 398200, 0, 200600, 90)
    Jump("loc_19C0")

    label("loc_19A1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_19C0")
    SetChrPos(0x4, 398200, 0, 200000, 90)

    label("loc_19C0")

    OP_68(400000, 1000, 200000, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(30000, 0)
    OP_0D()
    Sleep(500)
    Sound(144, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_68(400000, -4000, 200000, 2000)
    SetMapObjFrame(0x11, "m00ele00", 0x2, "down")
    Sleep(1000)
    OP_D2(0x0, (scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("m0101", 0, 0, 0)
    IdleLoop()

    label("loc_1A43")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_9_18BB end

    def Function_10_1A4B(): pass

    label("Function_10_1A4B")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    OP_6F(0x1)
    OP_69(0x1, 0x0)
    SetMapObjFrame(0x11, "m00ele00", 0x2, "down_kp")
    Sleep(1)
    OP_68(400000, -4000, 200000, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(30000, 0)
    OP_90(0x0, 400600, -10000, 200600, 90)
    OP_90(0x1, 400600, -10000, 199400, 90)
    OP_90(0x2, 399400, -10000, 199400, 90)
    OP_90(0x3, 399400, -10000, 200600, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B20")
    OP_90(0x4, 398200, 0, 199400, 90)
    OP_90(0x5, 398200, 0, 200600, 90)
    Jump("loc_1B3F")

    label("loc_1B20")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B3F")
    OP_90(0x4, 398200, 0, 200000, 90)

    label("loc_1B3F")

    Sound(145, 0, 100, 0)
    OP_68(400000, 1000, 200000, 3000)
    SetMapObjFrame(0x11, "m00ele00", 0x2, "up")
    FadeToBright(500, 0)
    Sleep(3400)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_79(0x11)
    OP_6F(0x1)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_10_1A4B end

    def Function_11_1B92(): pass

    label("Function_11_1B92")

    EventBegin(0x0)
    Fade(500)
    OP_68(28000, -7100, 10800, 0)
    MoveCamera(49, 27, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(24500, 0)
    SetChrPos(0x101, 27500, -8000, 10300, 0)
    SetChrPos(0x102, 28600, -8000, 10300, 0)
    SetChrPos(0x104, 28600, -8000, 9000, 0)
    SetChrPos(0x109, 27500, -8000, 9000, 0)
    SetChrPos(0x105, 26000, -8000, 9600, 45)
    SetChrPos(0x10A, 26000, -8000, 8500, 45)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_0D()
    Sound(807, 0, 100, 0)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a sturdy padlock\x01",
            "at the duct entrance.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    OP_0D()

    ChrTalk(
        0x104,
        "#00305FWhat?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#11P#00108FWhen did such a thing...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#6P#00606F...Perhaps the city management\x01",
            "in charge has locked it in order\x01",
            "to prevent crimes.\x02\x03",
            "#00600FPadlocks are typically used by the\x01",
            "people of the city utilities section.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1D90():
        TurnDirection(0x101, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1D90)
    Sleep(50)

    def lambda_1DA0():
        TurnDirection(0x102, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1DA0)
    Sleep(50)

    def lambda_1DB0():
        TurnDirection(0x109, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1DB0)
    Sleep(50)

    def lambda_1DC0():
        TurnDirection(0x104, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1DC0)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x104, 0)

    ChrTalk(
        0x101,
        (
            "#00003FAnd that means it probably\x01",
            "wasn't set up by that hacker.\x02\x03",
            "#00001FWhat do we do, break it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#6P#00603FNo, it'd make a loud noise and we can't\x01",
            "afford the other party to notice us.\x02\x03",
            "#00601FLet's proceed onward like this\x01",
            "until we reach that runt's room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FRoger.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10306FOh boy, I guess it's become\x01",
            "a digestion exercise, hm?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x105, 500)

    ChrTalk(
        0x109,
        "#11P#10112FGeez, don't complain.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 28000, -8000, 9500, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x141, 2)
    ModifyEventFlags(0, 0, 0x80)
    EventEnd(0x5)
    Return()

    # Function_11_1B92 end

    def Function_12_1F9D(): pass

    label("Function_12_1F9D")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000FOops, I'm sure that using the duct was\x01",
            "a shortcut to go to the terminal room.\x02\x03",
            "Let's check that before.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 29310, -8000, 8060, 270)
    EventEnd(0x4)
    Return()

    # Function_12_1F9D end

    SaveToFile()

Try(main)
