from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "m2000.bin",                # FileName
        "m2000",                    # MapName
        "m2000",                    # Location
        0x0077,                     # MapIndex
        "ed7303",
        0x00080000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x23,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 119, 0, 0, 0, 1],
    )

    BuildStringList((
        "m2000",                  # 0
        "bm2000",                 # 1
    ))

    ATBonus("ATBonus_258", 100, 5, 1, 5, 1, 5, 1, 5, 5, 5, 5, 5, 5, 0, 0, 0)

    Sepith("Sepith_1CE6", 0,   0,   12,  0,   8,   8,   0)

    MonsterBattlePostion("MonsterBattlePostion_2A8", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_2AC", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_2B0", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_2B4", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_2B8", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_2BC", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_2C0", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_2C4", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_308", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_30C", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_310", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_314", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_318", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_31C", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_320", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_324", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_288", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_28C", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_290", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_294", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_298", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_29C", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_2A0", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_2A4", 2, 13, 180)

    # monster count: 3

    BattleInfo(
        "BattleInfo_328", 0x0000, 63, 6, 60, 6, 1, 30, 0, "bm2000", "Sepith_1CE6", 40, 30, 20, 10,
        (
            ("ms73400.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_2A8", "MonsterBattlePostion_308", "ed7450", "ed7453", "ATBonus_258"),
            ("ms73400.dat", "ms73400.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_288", "MonsterBattlePostion_308", "ed7450", "ed7453", "ATBonus_258"),
            ("ms73400.dat", "ms73400.dat", "ms73400.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_2A8", "MonsterBattlePostion_308", "ed7450", "ed7453", "ATBonus_258"),
            ("ms73400.dat", "ms73400.dat", "ms73400.dat", "ms73400.dat", 0, 0, 0, 0, "MonsterBattlePostion_288", "MonsterBattlePostion_308", "ed7450", "ed7453", "ATBonus_258"),
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
        "monster/ch73450.itc",               # 10
        "monster/ch73450.itc",               # 11
    ))

    DeclMonster(112650,  4294966936, 0,       0x1010000,    "BattleInfo_328", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(111370,  4294950586, 0,       0x1010000,    "BattleInfo_328", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(110950,  10260,   0,       0x1010000,    "BattleInfo_328", 0,   16,  0xFFFF, 0,  1)

    DeclActor(113500,  9630,    8130,    1200,    113500,  10630,   8130,    0x007C, 0,  6,  0x0000)
    DeclActor(113500,  9650,    4294959136, 1200,    113500,  10650,   4294959136, 0x007C, 0,  7,  0x0000)
    DeclActor(34000,   0,       4000,    1200,    34000,   1500,    4000,    0x007C, 0,  2,  0x0000)
    DeclActor(4294963796, 0,       0,       1200,    4294963796, 1000,    0,       0x007C, 0,  8,  0x0000)
    DeclActor(132500,  0,       16000,   1200,    132500,  1000,    16000,   0x007C, 0,  9,  0x0000)
    DeclActor(130300,  500,     4294965396, 1200,    130300,  1500,    4294965396, 0x007C, 0,  3,  0x0000)
    DeclActor(130300,  500,     1900,    1200,    130300,  1500,    1900,    0x007C, 0,  4,  0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5, 6, 7])             # 0
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 5, 6, 7])             # 1

    ScpFunction((
        "Function_0_43C",          # 00, 0
        "Function_1_498",          # 01, 1
        "Function_2_BF8",          # 02, 2
        "Function_3_CEC",          # 03, 3
        "Function_4_EE4",          # 04, 4
        "Function_5_10DC",         # 05, 5
        "Function_6_114C",         # 06, 6
        "Function_7_1324",         # 07, 7
        "Function_8_14F9",         # 08, 8
        "Function_9_15EF",         # 09, 9
        "Function_10_161B",        # 0A, 10
        "Function_11_1BB2",        # 0B, 11
        "Function_12_1C38",        # 0C, 12
    ))


    def Function_0_43C(): pass

    label("Function_0_43C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_44F")
    Jump("loc_44F")

    label("loc_44F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_46E")
    SetMapFlags(0x10000000)
    Event(0, 10)

    label("loc_46E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_482")
    ClearScenarioFlags(0x22, 0)
    Event(0, 12)
    Jump("loc_491")

    label("loc_482")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_491")
    ClearScenarioFlags(0x22, 1)
    Event(0, 11)

    label("loc_491")

    SetScenarioFlags(0x150, 4)
    SetScenarioFlags(0x150, 5)
    Return()

    # Function_0_43C end

    def Function_1_498(): pass

    label("Function_1_498")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 5)), scpexpr(EXPR_END)), "loc_4AA")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x130), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4AA")

    OP_52(0x8, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    PlayEffect(0x2F, 0x0, 0x8, 0x41, 0, 0, 0, 0, 0, 0, 1250, 750, 1250, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2F, 0x1, 0x9, 0x41, 0, 0, 0, 0, 0, 0, 1250, 750, 1250, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2F, 0x2, 0xA, 0x41, 0, 0, 0, 0, 0, 0, 1250, 750, 1250, 0xFF, 0, 0, 0, 0)
    SetMapObjFrame(0xFF, "glow02", 0x0, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7C2")
    SetMapObjFlags(0xD, 0x4)
    SetMapObjFlags(0xE, 0x4)
    SetMapObjFlags(0xF, 0x4)
    SetMapObjFlags(0x10, 0x4)
    SetMapObjFlags(0x11, 0x4)
    OP_65(0x5, 0x1)
    OP_65(0x6, 0x1)

    label("loc_7C2")

    SetBarrier(0x0, 0x0, 0x1, 0x0, 120500, 9000, 9800, 3000, 2000, 90000)
    SetBarrier(0x0, 0x1, 0x1, 0x0, 115000, 9000, 9800, 3000, 2000, 90000)
    SetBarrier(0x0, 0x4, 0x1, 0x0, 132500, 9000, 5000, 2000, 2000, 90000)
    SetBarrier(0x0, 0x5, 0x1, 0x0, 132500, 9000, -5000, 2000, 2000, 90000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x150, 4)), scpexpr(EXPR_END)), "loc_897")
    SetMapObjFrame(0x6, "root", 0x2, "on")
    SetMapObjFrame(0x4, "root", 0x2, "on")
    SetMapObjFrame(0x9, "root", 0x2, "on")
    SetBarrier(0x2, 0x0, 0x1)
    SetBarrier(0x2, 0x1, 0x1)
    SetBarrier(0x2, 0x4, 0x1)
    SetBarrier(0x2, 0x5, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_892")
    SetMapObjFrame(0x9, "root", 0x2, "off")
    SetBarrier(0x3, 0x0, 0x1)
    SetBarrier(0x3, 0x1, 0x1)

    label("loc_892")

    Jump("loc_8CB")

    label("loc_897")

    SetMapObjFrame(0x6, "root", 0x2, "off")
    SetMapObjFrame(0x4, "root", 0x2, "off")
    SetMapObjFrame(0x9, "root", 0x2, "off")
    SetBarrier(0x3, 0x0, 0x1)
    SetBarrier(0x3, 0x1, 0x1)
    SetBarrier(0x3, 0x4, 0x1)
    SetBarrier(0x3, 0x5, 0x1)

    label("loc_8CB")

    SetBarrier(0x0, 0x2, 0x1, 0x0, 120500, 9000, -9800, 3000, 2000, 90000)
    SetBarrier(0x0, 0x3, 0x1, 0x0, 115000, 9000, -9800, 3000, 2000, 90000)
    SetBarrier(0x0, 0x6, 0x1, 0x0, 136950, 9000, 2160, 3000, 2000, 150000)
    SetBarrier(0x0, 0x7, 0x1, 0x0, 136950, 9000, -2160, 3000, 2000, 30000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x150, 5)), scpexpr(EXPR_END)), "loc_9A0")
    SetMapObjFrame(0x7, "root", 0x2, "on")
    SetMapObjFrame(0x5, "root", 0x2, "on")
    SetMapObjFrame(0xA, "root", 0x2, "on")
    SetBarrier(0x2, 0x2, 0x1)
    SetBarrier(0x2, 0x3, 0x1)
    SetBarrier(0x2, 0x6, 0x1)
    SetBarrier(0x2, 0x7, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_99B")
    SetMapObjFrame(0xA, "root", 0x2, "off")
    SetBarrier(0x3, 0x2, 0x1)
    SetBarrier(0x3, 0x3, 0x1)

    label("loc_99B")

    Jump("loc_9D4")

    label("loc_9A0")

    SetMapObjFrame(0x7, "root", 0x2, "off")
    SetMapObjFrame(0x5, "root", 0x2, "off")
    SetMapObjFrame(0xA, "root", 0x2, "off")
    SetBarrier(0x3, 0x2, 0x1)
    SetBarrier(0x3, 0x3, 0x1)
    SetBarrier(0x3, 0x6, 0x1)
    SetBarrier(0x3, 0x7, 0x1)

    label("loc_9D4")

    SetBarrier(0x0, 0x8, 0x1, 0x0, -3000, 0, 0, 6000, 3000, 90000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x150, 6)), scpexpr(EXPR_END)), "loc_A18")
    SetMapObjFrame(0xC, "root", 0x2, "on")
    ClearMapObjFlags(0xC, 0x2)
    SetBarrier(0x2, 0x8, 0x1)
    OP_65(0x3, 0x1)
    Jump("loc_A2E")

    label("loc_A18")

    SetMapObjFrame(0xC, "root", 0x2, "off")
    SetMapObjFlags(0xC, 0x2)
    SetBarrier(0x3, 0x8, 0x1)

    label("loc_A2E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A47")
    ClearMapObjFlags(0x1, 0x10)
    Jump("loc_A4B")

    label("loc_A47")

    OP_65(0x4, 0x1)

    label("loc_A4B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_BF1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B7, 0)), scpexpr(EXPR_END)), "loc_A7B")
    ClearMapObjFlags(0x10, 0x4)
    SetMapObjFrame(0x10, "b_bace", 0x0, 0x1)
    Jump("loc_ACC")

    label("loc_A7B")

    SetMapObjFrame(0x10, "b_bace", 0x0, 0x1)
    SetMapObjFrame(0x10, "b_in", 0x0, 0x1)
    SetMapObjFrame(0x10, "b_in2", 0x0, 0x1)
    SetMapObjFrame(0x10, "b_out", 0x0, 0x1)
    SetMapObjFrame(0x10, "b_out2", 0x0, 0x1)
    SetMapObjFrame(0x10, "b_light", 0x0, 0x1)

    label("loc_ACC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B7, 1)), scpexpr(EXPR_END)), "loc_AEE")
    ClearMapObjFlags(0x11, 0x4)
    SetMapObjFrame(0x11, "b_bace", 0x0, 0x1)
    Jump("loc_B3F")

    label("loc_AEE")

    SetMapObjFrame(0x11, "b_bace", 0x0, 0x1)
    SetMapObjFrame(0x11, "b_in", 0x0, 0x1)
    SetMapObjFrame(0x11, "b_in2", 0x0, 0x1)
    SetMapObjFrame(0x11, "b_out", 0x0, 0x1)
    SetMapObjFrame(0x11, "b_out2", 0x0, 0x1)
    SetMapObjFrame(0x11, "b_light", 0x0, 0x1)

    label("loc_B3F")

    SetBarrier(0x0, 0x9, 0x1, 0x0, 138100, 9000, 0, 8000, 3000, 90000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B7, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B7, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B73")
    SetMapObjFlags(0xF, 0x4)
    SetBarrier(0x2, 0x9, 0x1)

    label("loc_B73")

    SetBarrier(0x0, 0xA, 0x1, 0x0, 131000, 0, -15500, 6000, 3000, 90000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B7, 2)), scpexpr(EXPR_END)), "loc_BA8")
    SetMapObjFlags(0xD, 0x4)
    SetBarrier(0x2, 0xA, 0x1)
    Jump("loc_BB2")

    label("loc_BA8")

    ClearMapObjFlags(0xD, 0x4)
    SetBarrier(0x3, 0xA, 0x1)

    label("loc_BB2")

    SetBarrier(0x0, 0xB, 0x1, 0x0, 131000, 0, 15500, 6000, 3000, 90000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B7, 3)), scpexpr(EXPR_END)), "loc_BE7")
    SetMapObjFlags(0xE, 0x4)
    SetBarrier(0x2, 0xB, 0x1)
    Jump("loc_BF1")

    label("loc_BE7")

    ClearMapObjFlags(0xE, 0x4)
    SetBarrier(0x3, 0xB, 0x1)

    label("loc_BF1")

    Sound(129, 1, 100, 0)
    Return()

    # Function_1_498 end

    def Function_2_BF8(): pass

    label("Function_2_BF8")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CDD")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_74(0xB, 0x1E)
    Sound(7, 0, 100, 0)
    OP_70(0xB, 0x0)
    OP_71(0xB, 0x0, 0x1E, 0x0, 0x0)
    OP_79(0xB)
    OP_71(0xB, 0x1F, 0x186, 0x0, 0x20)
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
    OP_70(0xB, 0x0)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_CDD")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_2_BF8 end

    def Function_3_CEC(): pass

    label("Function_3_CEC")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B7, 0)), scpexpr(EXPR_END)), "loc_D32")
    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A pearl is on the\x01",
            "pedestal.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Jump("loc_EE3")

    label("loc_D32")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x33E, 0x0)"), scpexpr(EXPR_END)), "loc_EB8")
    EventBegin(0x1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A pedestal is here.\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Place Pearl\x01",      # 0
            "Refuse\x01",           # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EAC")
    Fade(500)
    SetChrPos(0x0, 128500, 0, -1900, 90)
    SetChrPos(0x1, 127500, 0, -2700, 90)
    SetChrPos(0x2, 127500, 0, -1100, 90)
    SetChrPos(0x3, 126500, 0, -1900, 90)
    OP_68(128889, 2500, -2580, 0)
    MoveCamera(59, 21, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(15390, 0)
    OP_E2(0x3)
    OP_0D()
    Sleep(500)
    Sleep(1000)
    Sound(802, 0, 100, 0)
    Fade(200)
    ClearMapObjFlags(0x10, 0x4)
    SetMapObjFrame(0x10, "b_bace", 0x0, 0x1)
    SetMapObjFrame(0x10, "b_in", 0x1, 0x1)
    SetMapObjFrame(0x10, "b_in2", 0x1, 0x1)
    SetMapObjFrame(0x10, "b_out", 0x1, 0x1)
    SetMapObjFrame(0x10, "b_out2", 0x1, 0x1)
    SetMapObjFrame(0x10, "b_light", 0x1, 0x1)
    OP_0D()
    Sleep(500)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Placed the pearl on the\x01",
            "pedestal.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SubItemNumber(0x33E, 1)
    SetScenarioFlags(0x1B7, 0)
    Call(0, 5)
    OP_E2(0x2)

    label("loc_EAC")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Jump("loc_EE3")

    label("loc_EB8")

    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A pedestal is here.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)

    label("loc_EE3")

    Return()

    # Function_3_CEC end

    def Function_4_EE4(): pass

    label("Function_4_EE4")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B7, 1)), scpexpr(EXPR_END)), "loc_F2A")
    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A pearl is on the\x01",
            "pedestal.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Jump("loc_10DB")

    label("loc_F2A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x33E, 0x0)"), scpexpr(EXPR_END)), "loc_10B0")
    EventBegin(0x1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A pedestal is here.\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Place Pearl\x01",      # 0
            "Refuse\x01",           # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10A4")
    Fade(500)
    SetChrPos(0x0, 128500, 0, 1900, 90)
    SetChrPos(0x1, 127500, 0, 2700, 90)
    SetChrPos(0x2, 127500, 0, 1100, 90)
    SetChrPos(0x3, 126500, 0, 1900, 90)
    OP_68(127770, 2550, 720, 0)
    MoveCamera(48, 28, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(14620, 0)
    OP_E2(0x3)
    OP_0D()
    Sleep(500)
    Sleep(1000)
    Sound(802, 0, 100, 0)
    Fade(200)
    ClearMapObjFlags(0x11, 0x4)
    SetMapObjFrame(0x11, "b_bace", 0x0, 0x1)
    SetMapObjFrame(0x11, "b_in", 0x1, 0x1)
    SetMapObjFrame(0x11, "b_in2", 0x1, 0x1)
    SetMapObjFrame(0x11, "b_out", 0x1, 0x1)
    SetMapObjFrame(0x11, "b_out2", 0x1, 0x1)
    SetMapObjFrame(0x11, "b_light", 0x1, 0x1)
    OP_0D()
    Sleep(500)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Placed the pearl on the\x01",
            "pedestal.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SubItemNumber(0x33E, 1)
    SetScenarioFlags(0x1B7, 1)
    Call(0, 5)
    OP_E2(0x2)

    label("loc_10A4")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Jump("loc_10DB")

    label("loc_10B0")

    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A pedestal is here.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)

    label("loc_10DB")

    Return()

    # Function_4_EE4 end

    def Function_5_10DC(): pass

    label("Function_5_10DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B7, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B7, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_114B")
    Fade(500)
    OP_68(139400, 10850, 780, 0)
    MoveCamera(69, 7, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(21990, 0)
    OP_0D()
    Sleep(500)
    Sleep(1000)
    Sound(202, 0, 100, 0)
    Sound(223, 0, 100, 0)
    Fade(1000)
    SetMapObjFlags(0xF, 0x4)
    SetBarrier(0x2, 0x9, 0x1)
    SetCameraDistance(20990, 1000)
    OP_0D()
    Sleep(3000)

    label("loc_114B")

    Return()

    # Function_5_10DC end

    def Function_6_114C(): pass

    label("Function_6_114C")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x150, 4)), scpexpr(EXPR_END)), "loc_119B")
    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The switch has already\x01",
            "been pressed.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Jump("loc_1323")

    label("loc_119B")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_131C")
    Fade(500)
    SetChrPos(0x0, 113260, 9000, 9260, 180)
    SetChrPos(0x1, 110400, 9000, 9300, 90)
    SetChrPos(0x2, 108400, 9000, 9300, 90)
    SetChrPos(0x3, 106400, 9000, 9300, 90)
    OP_68(113920, 11500, 9260, 0)
    MoveCamera(35, 27, 0, 0)
    OP_6E(570, 0)
    SetCameraDistance(18000, 0)
    OP_0D()
    Sleep(500)
    SetMapObjFrame(0x6, "root", 0x2, "on")
    Sleep(1200)
    Sound(155, 2, 100, 0)
    SetMapObjFrame(0x9, "root", 0x2, "move")
    Sleep(2000)
    OP_24(0x9B)
    Sound(149, 0, 100, 0)
    OP_82(0x0, 0x64, 0x3E8, 0x64)
    Sleep(500)
    Fade(500)
    OP_68(133890, 11500, -180, 0)
    MoveCamera(64, 21, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(18000, 0)
    OP_0D()
    Sleep(500)
    Sound(155, 2, 100, 0)
    SetMapObjFrame(0x4, "root", 0x2, "move")
    Sleep(1000)
    OP_24(0x9B)
    Sound(149, 0, 100, 0)
    OP_82(0x0, 0x64, 0x3E8, 0x64)
    Sleep(1000)
    SetBarrier(0x2, 0x0, 0x1)
    SetBarrier(0x2, 0x1, 0x1)
    SetBarrier(0x2, 0x4, 0x1)
    SetBarrier(0x2, 0x5, 0x1)
    SetScenarioFlags(0x150, 4)

    label("loc_131C")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)

    label("loc_1323")

    Return()

    # Function_6_114C end

    def Function_7_1324(): pass

    label("Function_7_1324")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x150, 5)), scpexpr(EXPR_END)), "loc_1373")
    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The switch has already\x01",
            "been pressed.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Jump("loc_14F8")

    label("loc_1373")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14F1")
    Fade(500)
    SetChrPos(0x0, 113660, 9000, -9380, 0)
    SetChrPos(0x1, 110400, 9000, -10100, 90)
    SetChrPos(0x2, 108400, 9000, -10100, 90)
    SetChrPos(0x3, 106400, 9000, -10100, 90)
    OP_68(114150, 11500, -10180, 0)
    MoveCamera(50, 31, 0, 0)
    OP_6E(630, 0)
    SetCameraDistance(15500, 0)
    OP_0D()
    SetMapObjFrame(0x7, "root", 0x2, "on")
    Sleep(1200)
    Sound(155, 2, 100, 0)
    SetMapObjFrame(0xA, "root", 0x2, "move")
    Sleep(2000)
    OP_24(0x9B)
    Sound(149, 0, 100, 0)
    OP_82(0x0, 0x64, 0x3E8, 0x64)
    Sleep(500)
    Fade(500)
    OP_68(133890, 11500, -180, 0)
    MoveCamera(64, 21, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(18000, 0)
    OP_0D()
    Sleep(500)
    Sound(155, 2, 100, 0)
    SetMapObjFrame(0x5, "root", 0x2, "move")
    Sleep(2000)
    OP_24(0x9B)
    Sound(149, 0, 100, 0)
    OP_82(0x0, 0x64, 0x3E8, 0x64)
    Sleep(1000)
    SetBarrier(0x2, 0x2, 0x1)
    SetBarrier(0x2, 0x3, 0x1)
    SetBarrier(0x2, 0x6, 0x1)
    SetBarrier(0x2, 0x7, 0x1)
    SetScenarioFlags(0x150, 5)

    label("loc_14F1")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)

    label("loc_14F8")

    Return()

    # Function_7_1324 end

    def Function_8_14F9(): pass

    label("Function_8_14F9")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x150, 6)), scpexpr(EXPR_END)), "loc_153A")
    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's already unlocked.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Jump("loc_15EE")

    label("loc_153A")

    EventBegin(0x1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The door is locked.\x01",
            "Unlock it?\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15E7")
    Fade(500)
    OP_68(-3250, 600, 40, 0)
    MoveCamera(55, 27, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(18000, 0)
    OP_0D()
    Sleep(1000)
    Sound(119, 0, 100, 0)
    SetMapObjFrame(0xC, "root", 0x2, "move")
    Sleep(1500)
    ClearMapObjFlags(0xC, 0x2)
    SetBarrier(0x2, 0x8, 0x1)
    OP_65(0x3, 0x1)
    SetScenarioFlags(0x150, 6)

    label("loc_15E7")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)

    label("loc_15EE")

    Return()

    # Function_8_14F9 end

    def Function_9_15EF(): pass

    label("Function_9_15EF")

    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The door is firmly shut.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_9_15EF end

    def Function_10_161B(): pass

    label("Function_10_161B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    ClearMapFlags(0x10000000)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, 104000, 0, 0, 90)
    SetChrPos(0x102, 103000, 0, 600, 90)
    SetChrPos(0x103, 103000, 0, -600, 90)
    SetChrPos(0x104, 102000, 0, -100, 90)
    SetChrPos(0xF4, 101300, 0, 600, 90)
    SetChrPos(0xF5, 100700, 0, -600, 90)
    OP_68(100000, 6700, -3000, 0)
    MoveCamera(67, 26, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(18000, 0)
    PlaceName2(340, 200, "c_plac29", 0x0, 1500)
    FadeToBright(1000, 0)
    OP_68(100000, 4700, -3000, 5000)

    def lambda_1706():
        OP_9B(0x0, 0x101, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1706)
    Sleep(50)

    def lambda_171E():
        OP_9B(0x0, 0x102, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_171E)
    Sleep(50)

    def lambda_1736():
        OP_9B(0x0, 0x103, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1736)
    Sleep(50)

    def lambda_174E():
        OP_9B(0x0, 0x104, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_174E)
    Sleep(50)

    def lambda_1766():
        OP_9B(0x0, 0xF4, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_1766)
    Sleep(50)

    def lambda_177E():
        OP_9B(0x0, 0xF5, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_177E)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)
    OP_6F(0x79)
    OP_0D()
    Fade(1000)
    OP_68(110000, 1400, 0, 0)
    MoveCamera(67, 26, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(14500, 0)
    SetCameraDistance(13500, 2500)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x101,
        "#00005F#6PThose are...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(1000)
    OP_68(131500, 3000, 16000, 0)
    MoveCamera(60, 13, 0, 0)
    MoveCamera(45, 6, 0, 5000)
    OP_6E(700, 0)
    SetCameraDistance(29500, 0)
    OP_6F(0x79)
    OP_0D()
    Fade(1000)
    OP_68(131500, 2000, -3000, 0)
    OP_68(131500, 2000, -8300, 5000)
    MoveCamera(65, 12, 0, 0)
    MoveCamera(55, 12, 0, 5000)
    OP_6E(700, 0)
    SetCameraDistance(29500, 0)
    OP_6F(0x79)
    OP_0D()
    Fade(1000)
    OP_68(125000, 11200, 0, 0)
    OP_68(135500, 11200, 0, 7500)
    MoveCamera(67, 6, 0, 0)
    MoveCamera(67, 13, 0, 7500)
    OP_6E(700, 0)
    SetCameraDistance(20000, 0)
    OP_6F(0x79)
    OP_0D()
    Fade(1000)
    OP_68(110000, 2100, 0, 0)
    OP_68(110000, 1400, 0, 2000)
    MoveCamera(67, 26, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(13500, 0)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x103,
        (
            "#00208F#6PAs expected, they seem to\x01",
            "have been sealed using\x01",
            "some sort of trick.\x02\x03",
            "#00201FIt looks like there are\x01",
            "several of them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#6PThe sealed doors on\x01",
            "either side seem to be\x01",
            "from Ouroboros, but...\x02\x03",
            "#00101FThe sealed secret door\x01",
            "seems to have the Cult's\x01",
            "eye crest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00013F#6PYeah. What in the world\x01",
            "is he planning?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1AD5")

    ChrTalk(
        0x109,
        (
            "#10101F#6PAnyhow, all we can do is\x01",
            "start investigating!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B1B")

    label("loc_1AD5")


    ChrTalk(
        0x106,
        (
            "#10701F#6PAnyhow, our only choice\x01",
            "is to start our\x01",
            "investigation.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B1B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1B52")

    ChrTalk(
        0x105,
        "#10400F#6PThen, shall we go?\x02",
    )

    CloseMessageWindow()
    Jump("loc_1B70")

    label("loc_1B52")


    ChrTalk(
        0x106,
        "#10701F#6PYes, let's go.\x02",
    )

    CloseMessageWindow()

    label("loc_1B70")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 105500, 0, 0, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x1A4, 4)
    OP_29(0xB0, 0x1, 0x2)
    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_10_161B end

    def Function_11_1BB2(): pass

    label("Function_11_1BB2")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(130310, 2500, -16730, 0)
    MoveCamera(50, 13, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(15530, 0)
    FadeToBright(500, 0)
    OP_0D()
    Sleep(1000)
    Sound(202, 0, 100, 0)
    Sound(223, 0, 100, 0)
    Fade(1000)
    SetMapObjFlags(0xD, 0x4)
    SetCameraDistance(16990, 1000)
    OP_0D()
    Sleep(3000)
    SetScenarioFlags(0x1B7, 2)
    FadeToDark(500, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 0)
    NewScene("m2050", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_11_1BB2 end

    def Function_12_1C38(): pass

    label("Function_12_1C38")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(129740, 2500, 12880, 0)
    MoveCamera(41, 17, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(15530, 0)
    FadeToBright(500, 0)
    OP_0D()
    Sleep(1000)
    Sound(202, 0, 100, 0)
    Sound(223, 0, 100, 0)
    Fade(1000)
    SetMapObjFlags(0xE, 0x4)
    SetCameraDistance(16990, 1000)
    OP_0D()
    Sleep(3000)
    SetScenarioFlags(0x1B7, 3)
    FadeToDark(500, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 0)
    NewScene("m2020", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_12_1C38 end

    SaveToFile()

Try(main)
