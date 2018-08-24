from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "m4050.bin",                # FileName
        "m4050",                    # MapName
        "m4050",                    # Location
        0x007D,                     # MapIndex
        "ed7350",
        0x00000000,                 # Flags
        ("m4050", "r0000_1", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x27,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 125, 0, 2, 0, 3],
    )

    BuildStringList((
        "m4050",                  # 0
        "イベント用モンスター",   # 1
        "ピンクマッシュルーム",   # 2
        "bm4010",                 # 3
        "bm4010",                 # 4
        "bm4010",                 # 5
        "bm4010",                 # 6
        "bm4010",                 # 7
        "bm4010",                 # 8
    ))

    ATBonus("ATBonus_3AC", 100, 5, 1, 5, 1, 5, 1, 5, 5, 5, 5, 5, 5, 0, 0, 0)
    ATBonus("ATBonus_3BC", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    Sepith("Sepith_2261", 0,   3,   3,   3,   0,   0,   1)
    Sepith("Sepith_2259", 2,   2,   2,   2,   0,   1,   1)
    Sepith("Sepith_2251", 2,   2,   0,   2,   2,   2,   1)
    Sepith("Sepith_2269", 3,   0,   4,   3,   3,   5,   0)

    MonsterBattlePostion("MonsterBattlePostion_3FC", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_400", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_404", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_408", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_40C", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_410", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_414", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_418", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_45C", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_460", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_464", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_468", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_46C", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_470", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_474", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_478", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_3DC", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_3E0", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_3E4", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_3E8", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_3EC", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_3F0", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_3F4", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_3F8", 2, 13, 180)

    # monster count: 14

    BattleInfo(
        "BattleInfo_5B4", 0x0000, 47, 6, 45, 6, 1, 40, 0, "bm4010", "Sepith_2261", 60, 25, 10, 0,
        (
            ("ms83900.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3FC", "MonsterBattlePostion_45C", "ed7450", "ed7453", "ATBonus_3AC"),
            ("ms83900.dat", "ms83900.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3DC", "MonsterBattlePostion_45C", "ed7450", "ed7453", "ATBonus_3AC"),
            ("ms83900.dat", "ms83900.dat", "ms83900.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_3FC", "MonsterBattlePostion_45C", "ed7450", "ed7453", "ATBonus_3AC"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_518", 0x0000, 46, 6, 45, 6, 1, 40, 0, "bm4010", "Sepith_2259", 60, 25, 10, 0,
        (
            ("ms84600.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3FC", "MonsterBattlePostion_45C", "ed7450", "ed7453", "ATBonus_3AC"),
            ("ms84600.dat", "ms84600.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3DC", "MonsterBattlePostion_45C", "ed7450", "ed7453", "ATBonus_3AC"),
            ("ms84600.dat", "ms84600.dat", "ms84600.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_3FC", "MonsterBattlePostion_45C", "ed7450", "ed7453", "ATBonus_3AC"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_47C", 0x0000, 46, 6, 45, 6, 1, 40, 0, "bm4010", "Sepith_2251", 60, 25, 10, 0,
        (
            ("ms83800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3FC", "MonsterBattlePostion_45C", "ed7450", "ed7453", "ATBonus_3AC"),
            ("ms83800.dat", "ms83800.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3DC", "MonsterBattlePostion_45C", "ed7450", "ed7453", "ATBonus_3AC"),
            ("ms83800.dat", "ms83800.dat", "ms83800.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_3FC", "MonsterBattlePostion_45C", "ed7450", "ed7453", "ATBonus_3AC"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_650", 0x0000, 47, 6, 45, 6, 1, 40, 0, "bm4010", "Sepith_2269", 100, 0, 0, 0,
        (
            ("ms82900.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3FC", "MonsterBattlePostion_45C", "ed7450", "ed7453", "ATBonus_3AC"),
            (),
            (),
            (),
        )
    )

    # event battle count: 2

    BattleInfo(
        "BattleInfo_6D8", 0x0000, 50, 6, 45, 0, 1, 0, 0, "bm4010", 0x00000000, 100, 0, 0, 0,
        (
            ("ms83800.dat", "ms83800.dat", "ms83800.dat", "ms83800.dat", 0, 0, 0, 0, "MonsterBattlePostion_3DC", "MonsterBattlePostion_45C", "ed7451", "ed7453", "ATBonus_3BC"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_694", 0x0002, 3, 6, 45, 3, 3, 30, 0, "bm4010", 0x00000000, 100, 0, 0, 0,
        (
            ("ms82900.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3DC", "MonsterBattlePostion_45C", "ed7452", "ed7453", "ATBonus_3BC"),
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
        "chr/ch00000.itc",                   # 10
        "chr/ch00000.itc",                   # 11
        "chr/ch00000.itc",                   # 12
        "chr/ch00000.itc",                   # 13
        "monster/ch83850.itc",               # 14
        "monster/ch83851.itc",               # 15
        "monster/ch84650.itc",               # 16
        "monster/ch84651.itc",               # 17
        "monster/ch83950.itc",               # 18
        "monster/ch83951.itc",               # 19
        "monster/ch82950.itc",               # 1A
        "monster/ch82950.itc",               # 1B
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(4294816177, 4294965796, 296049,  0,    484,  0x0, 0,   20,  0,   0,   1,   255, 255, 255,  0)

    DeclMonster(4294963176, 17040,   0,       0x101008C,    "BattleInfo_5B4", 0,   24,  0xFFFF, 4,  5)
    DeclMonster(4294955146, 29180,   4294967286, 0x1010004,    "BattleInfo_5B4", 0,   24,  0xFFFF, 4,  5)
    DeclMonster(16379,   6860,    4294962306, 0x1010140,    "BattleInfo_518", 0,   22,  0xFFFF, 2,  3)
    DeclMonster(6140,    24880,   4294953876, 0x101008C,    "BattleInfo_518", 0,   22,  0xFFFF, 2,  3)
    DeclMonster(14200,   47020,   4294960506, 0x1010113,    "BattleInfo_5B4", 0,   24,  0xFFFF, 4,  5)
    DeclMonster(4294824966, 38720,   0,       0x101008C,    "BattleInfo_5B4", 0,   24,  0xFFFF, 4,  5)
    DeclMonster(4294964456, 172450,  0,       0x101008C,    "BattleInfo_5B4", 0,   24,  0xFFFF, 4,  5)
    DeclMonster(3400,    202280,  4294965306, 0x101008C,    "BattleInfo_518", 0,   22,  0xFFFF, 2,  3)
    DeclMonster(4294827966, 163680,  290,     0x101005F,    "BattleInfo_5B4", 0,   24,  0xFFFF, 4,  5)
    DeclMonster(4294649876, 241230,  0,       0x10100F2,    "BattleInfo_47C", 0,   20,  0xFFFF, 0,  1)
    DeclMonster(4294638966, 231170,  0,       0x1010032,    "BattleInfo_650", 0,   26,  0xFFFF, 6,  7)
    DeclMonster(4294822196, 295770,  4294965296, 0x101008C,    "BattleInfo_47C", 0,   20,  0xFFFF, 0,  1)
    DeclMonster(151540,  170840,  150,     0x10100E6,    "BattleInfo_650", 0,   26,  0xFFFF, 6,  7)
    DeclMonster(151750,  166820,  0,       0x1010140,    "BattleInfo_47C", 0,   20,  0xFFFF, 0,  1)

    DeclActor(25270,   4294952446, 19240,   1200,    25270,   4294953446, 19240,   0x007C, 0,  4,  0x0000)
    DeclActor(4294818086, 100,     41670,   1200,    4294818086, 1100,    41670,   0x007C, 0,  5,  0x0000)
    DeclActor(4294634006, 0,       231480,  1200,    4294634006, 1000,    231480,  0x007C, 0,  6,  0x0000)
    DeclActor(4294816176, 4294965296, 296050,  1200,    4294816176, 4294966296, 296050,  0x007C, 0,  7,  0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 0
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4])                      # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 2
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4])                      # 3
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 4
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4])                      # 5
    ChipFrameInfo(800, 0, [0, 1, 2, 3, 4])                       # 6
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 7

    ScpFunction((
        "Function_0_7B4",          # 00, 0
        "Function_1_7D1",          # 01, 1
        "Function_2_7ED",          # 02, 2
        "Function_3_808",          # 03, 3
        "Function_4_EE7",          # 04, 4
        "Function_5_1038",         # 05, 5
        "Function_6_1189",         # 06, 6
        "Function_7_12DA",         # 07, 7
        "Function_8_14F5",         # 08, 8
        "Function_9_14F9",         # 09, 9
        "Function_10_1732",        # 0A, 10
        "Function_11_1760",        # 0B, 11
        "Function_12_178E",        # 0C, 12
        "Function_13_18E3",        # 0D, 13
    ))


    def Function_0_7B4(): pass

    label("Function_0_7B4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7D0")
    OP_A1(0xFE, 0x3E8, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Jump("Function_0_7B4")

    label("loc_7D0")

    Return()

    # Function_0_7B4 end

    def Function_1_7D1(): pass

    label("Function_1_7D1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7EC")
    OP_A1(0xFE, 0x3E8, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_1_7D1")

    label("loc_7EC")

    Return()

    # Function_1_7D1 end

    def Function_2_7ED(): pass

    label("Function_2_7ED")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x120, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x120, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_807")
    Event(0, 9)

    label("loc_807")

    Return()

    # Function_2_7ED end

    def Function_3_808(): pass

    label("Function_3_808")

    OP_52(0xA, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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
    OP_52(0xE, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E61")
    OP_70(0x0, 0x0)
    Jump("loc_E65")

    label("loc_E61")

    OP_70(0x0, 0x1E)

    label("loc_E65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E78")
    OP_70(0x1, 0x0)
    Jump("loc_E7C")

    label("loc_E78")

    OP_70(0x1, 0x1E)

    label("loc_E7C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E8F")
    OP_70(0x2, 0x0)
    Jump("loc_E93")

    label("loc_E8F")

    OP_70(0x2, 0x1E)

    label("loc_E93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EA6")
    OP_70(0x3, 0x0)
    Jump("loc_EAA")

    label("loc_EA6")

    OP_70(0x3, 0x1E)

    label("loc_EAA")

    Sound(129, 1, 100, 0)
    OP_1C(0x0, 0x4, 0x0, 0x32, 0x0, 0x8, 0x0, 0x0)
    OP_1C(0x0, 0x5, 0x0, 0x32, 0x0, 0x8, 0x0, 0x0)
    OP_1C(0x0, 0x6, 0x0, 0x32, 0x0, 0x8, 0x0, 0x0)
    LoadEffect(0x10, "event\\eva00_00.eff")
    Return()

    # Function_3_808 end

    def Function_4_EE7(): pass

    label("Function_4_EE7")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FE3")
    Sound(14, 0, 100, 0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1FB, 1)"), scpexpr(EXPR_END)), "loc_F6C")
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
    SetScenarioFlags(0x1E1, 1)
    OP_E0(0x5, 0x0)
    Jump("loc_FDE")

    label("loc_F6C")

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

    label("loc_FDE")

    Jump("loc_102C")

    label("loc_FE3")

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

    label("loc_102C")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_EE7 end

    def Function_5_1038(): pass

    label("Function_5_1038")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1134")
    Sound(14, 0, 100, 0)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1F5, 1)"), scpexpr(EXPR_END)), "loc_10BD")
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
    SetScenarioFlags(0x1E1, 2)
    OP_E0(0x5, 0x0)
    Jump("loc_112F")

    label("loc_10BD")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1F5),
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

    label("loc_112F")

    Jump("loc_117D")

    label("loc_1134")

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

    label("loc_117D")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_1038 end

    def Function_6_1189(): pass

    label("Function_6_1189")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1285")
    Sound(14, 0, 100, 0)
    OP_74(0x2, 0x1E)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x20B, 1)"), scpexpr(EXPR_END)), "loc_120E")
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
    SetScenarioFlags(0x1E1, 3)
    OP_E0(0x5, 0x0)
    Jump("loc_1280")

    label("loc_120E")

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
    OP_71(0x2, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1280")

    Jump("loc_12CE")

    label("loc_1285")

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

    label("loc_12CE")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_1189 end

    def Function_7_12DA(): pass

    label("Function_7_12DA")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14AB")
    Sound(14, 0, 100, 0)
    OP_74(0x3, 0x1E)
    OP_71(0x3, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21A, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13DD")
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0x9, 0x0, 0)
    OP_98(0x9, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_1337():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1337)

    def lambda_1351():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1351)
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
    Battle("BattleInfo_6D8", 0x0, 0x0, 0x0, 0xB, 0xFF)
    SetChrFlags(0x9, 0x80)
    ClearChrFlags(0x9, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_13BE"),
        (2, "loc_13CD"),
        (1, "loc_13DA"),
        (SWITCH_DEFAULT, "loc_13DD"),
    )


    label("loc_13BE")

    SetScenarioFlags(0x21A, 7)
    OP_70(0x3, 0x1E)
    Sleep(500)
    Jump("loc_13DD")

    label("loc_13CD")

    OP_70(0x3, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_13DA")

    OP_B9(0x0)
    Return()

    label("loc_13DD")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x92, 1)"), scpexpr(EXPR_END)), "loc_1436")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x92),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1E1, 4)
    OP_E0(0x5, 0x0)
    Jump("loc_14A6")

    label("loc_1436")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x92),
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

    label("loc_14A6")

    Jump("loc_14E9")

    label("loc_14AB")

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

    label("loc_14E9")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_12DA end

    def Function_8_14F5(): pass

    label("Function_8_14F5")

    Call(1, 6)
    Return()

    # Function_8_14F5 end

    def Function_9_14F9(): pass

    label("Function_9_14F9")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    LoadChrToIndex("monster/ch82950.itc", 0x1E)
    LoadChrToIndex("monster/ch82952.itc", 0x1F)
    LoadChrToIndex("chr/ch00050.itc", 0x20)
    LoadChrToIndex("chr/ch00051.itc", 0x21)
    LoadChrToIndex("chr/ch02950.itc", 0x22)
    LoadChrToIndex("chr/ch02951.itc", 0x23)
    LoadChrToIndex("chr/ch00056.itc", 0x24)
    LoadChrToIndex("chr/ch0295F.itc", 0x25)
    OP_68(4000, 1000, 154400, 0)
    MoveCamera(315, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(20500, 0)
    SetChrPos(0x101, 4500, 0, 150500, 0)
    SetChrPos(0x109, 3200, 0, 150300, 0)
    SetChrFlags(0x8, 0x20)
    SetChrChipByIndex(0x8, 0x1F)
    SetChrPos(0x8, 4000, 0, 162500, 180)
    OP_A7(0x8, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_52(0x8, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(4000, 1000, 160400, 5000)
    SetCameraDistance(18500, 5000)

    def lambda_15EC():
        OP_97(0x101, 0x0, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_15EC)
    Sleep(50)

    def lambda_1609():
        OP_97(0x109, 0x0, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1609)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x101, 0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    WaitChrThread(0x109, 0)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(3500, 900, 159500, 800)
    MoveCamera(323, 21, 0, 800)
    SetCameraDistance(18000, 800)
    BeginChrThread(0x101, 3, 0, 10)
    Sound(809, 0, 100, 0)
    Sleep(50)
    BeginChrThread(0x109, 3, 0, 11)
    Sleep(50)
    ClearChrFlags(0x8, 0x80)
    Sound(601, 0, 100, 0)
    BeginChrThread(0x8, 3, 0, 12)
    WaitChrThread(0x8, 3)
    Sleep(1500)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetCameraDistance(15000, 500)

    def lambda_16D2():
        OP_96(0xFE, 0x1068, 0x0, 0x2867C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_16D2)
    Sleep(30)

    def lambda_16EF():
        OP_96(0xFE, 0xDAC, 0x0, 0x2867C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_16EF)
    Sleep(470)
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x109, 0xFF)
    Battle("BattleInfo_694", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x8, 0x80)
    Call(0, 13)
    Return()

    # Function_9_14F9 end

    def Function_10_1732(): pass

    label("Function_10_1732")

    SetChrChipByIndex(0x101, 0x24)
    SetChrSubChip(0x101, 0x2)
    OP_9D(0x101, 0x11F8, 0x0, 0x26228, 0x2BC, 0xFA0)
    SetChrChipByIndex(0x101, 0x20)
    SetChrSubChip(0x101, 0x0)
    Sound(805, 0, 100, 0)
    Return()

    # Function_10_1732 end

    def Function_11_1760(): pass

    label("Function_11_1760")

    SetChrChipByIndex(0x109, 0x25)
    SetChrSubChip(0x109, 0x2)
    OP_9D(0x109, 0xCE4, 0x0, 0x26034, 0x2BC, 0xFA0)
    SetChrChipByIndex(0x109, 0x22)
    SetChrSubChip(0x109, 0x0)
    Sound(531, 0, 100, 0)
    Return()

    # Function_11_1760 end

    def Function_12_178E(): pass

    label("Function_12_178E")

    OP_82(0xC8, 0x0, 0xBB8, 0x5DC)

    def lambda_17A4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x64)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_17A4)
    OP_52(0x8, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x12C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x12C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x12C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrSubChip(0xFE, 0x1)
    Sleep(130)
    OP_52(0x8, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x1F4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x1F4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x1F4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrSubChip(0xFE, 0x2)
    Sleep(130)
    OP_52(0x8, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x2BC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x2BC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x2BC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrSubChip(0xFE, 0x3)
    Sleep(130)
    OP_52(0x8, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrSubChip(0xFE, 0x4)
    Sleep(130)
    OP_52(0x8, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrSubChip(0xFE, 0x5)

    def lambda_187A():
        OP_A6(0xFE, 0x64, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_187A)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0x8, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x8, 0, 0, 0)
    Return()

    # Function_12_178E end

    def Function_13_18E3(): pass

    label("Function_13_18E3")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch02950.itc", 0x1F)
    SoundLoad(2667)
    SoundLoad(2749)
    SoundLoad(3384)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis227.itp")
    OP_68(4050, 1100, 159750, 0)
    MoveCamera(317, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18000, 0)
    SetChrPos(0x101, 4300, 0, 160000, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrPos(0x109, 3000, 0, 159700, 0)
    SetChrChipByIndex(0x109, 0x1F)
    SetChrSubChip(0x109, 0x0)
    SetCameraDistance(17000, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#6P#00008FPhew...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F#5PIt's a lot harder with\x01",
            "just the two of us...\x02",
        )
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

    def lambda_1A24():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1A24)
    Sleep(100)
    TurnDirection(0x109, 0x101, 500)
    Sleep(200)

    ChrTalk(
        0x101,
        (
            "#12P#00004FYeah, but we'll manage...\x02\x03",
            "#00002FRandy's the same, of course,\x01",
            "but you Guardian Force\x01",
            "members sure are reliable.\x02\x03",
            "Your training must've been\x01",
            "completely different from an\x01",
            "ordinary policeman.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(800)

    ChrTalk(
        0x109,
        (
            "#10112F#5PAhaha... Don't flatter me,\x01",
            "please.\x02\x03",
            "#10102FIf pushed, I'd say we rely\x01",
            "in turn on our powerful\x01",
            "weapons and equipment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00004FBut mastery of those\x01",
            "weapons is itself the\x01",
            "result of training.\x02\x03",
            "#00000FI mean, we're the same\x01",
            "age and you're already\x01",
            "so good at driving!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10104F#5PWell, that's because I've\x01",
            "trained daily ever since\x01",
            "enlisting when I was 15.\x02\x03",
            "#10100FI also owe a lot to\x01",
            "Commander Sonya. Her\x01",
            "guidance has been excellent.\x02\x03",
            "#10106F...Even if the drills were\x01",
            "gruesome.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00002FHaha, Vice Commander\x01",
            "Sonya... No, Commander\x01",
            "Sonya...\x02\x03",
            "#00004FIf she was in charge, it\x01",
            "must've been good\x01",
            "training.\x02\x03",
            "#00000FRandy mentioned that even\x01",
            "he had a really hard time\x01",
            "with his training.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10112F#5PYeah, seems like it, huh?\x02\x03",
            "#10100FRandy, huh... He's in the\x01",
            "middle of rehabilitation\x01",
            "training right now, isn't he?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FYeah, he is.\x02\x03",
            "#00006FIf only Randy were\x01",
            "here... Or Elie and Tio\x01",
            "for that matter.\x02\x03",
            "#00008FWith them around,\x01",
            "there'd be nothing to\x01",
            "worry about.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10104F#5PEhehe, agreed.\x02\x03",
            "#10102FCome to think of it, the\x01",
            "Special Support Section really\x01",
            "does have a good balance.\x02\x03",
            "With your roles defined so\x01",
            "clearly, you're able to handle\x01",
            "anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FYeah, they really help me\x01",
            "out a lot.\x02\x03",
            "Even out of battle, their\x01",
            "different specialities were\x01",
            "so helpful in many ways...\x02",
        )
    )

    CloseMessageWindow()
    VolumeBGM(0x46, 0x3E8)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(300)
    OP_C9(0x0, 0x800)
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(250, 120, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#2749V#30WBye then. I'll leave\x01",
            "things to you.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(30, 130, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#3384V#30WPlease take care of KeA\x01",
            "for me.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, 150, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#2667V#30WMake sure you look after\x01",
            "Zeit and Koppe, too.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x800)
    OP_C9(0x1, 0x80000000)
    OP_24(0xA6B)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    VolumeBGM(0x64, 0x3E8)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#12P#00004F(Elie, Tio, Randy...)\x02\x03",
            "#00000F(It's already been a month\x01",
            "since then. I wonder how\x01",
            "everyone's doing.)\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_37()
    OP_CC(0x1, 0xFF, 0x0)
    SetChrPos(0x0, 4000, 0, 160000, 0)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x120, 7)
    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_13_18E3 end

    SaveToFile()

Try(main)
