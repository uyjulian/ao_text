from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "m1060.bin",                # FileName
        "m1060",                    # MapName
        "m1060",                    # Location
        0x006F,                     # MapIndex
        "ed7304",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x21,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 111, 0, 0, 0, 1],
    )

    BuildStringList((
        "m1060",                  # 0
        "Ennea the Chiron",       # 1
        "Vanguard",               # 2
        "Vanguard",               # 3
        "SE制御",                 # 4
        "汎用ダミー",             # 5
        "bm1020",                 # 6
        "bm1020",                 # 7
        "bm1061",                 # 8
    ))

    ATBonus("ATBonus_258", 100, 5, 1, 5, 1, 5, 1, 5, 5, 5, 5, 5, 5, 0, 0, 0)
    ATBonus("ATBonus_268", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    Sepith("Sepith_24A4", 9,   9,   9,   21,  4,   4,   4)
    Sepith("Sepith_247C", 19,  0,   0,   10,  10,  8,   8)

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
    MonsterBattlePostion("MonsterBattlePostion_328", 8, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_32C", 4, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_330", 12, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_334", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_338", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_33C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_340", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_344", 0, 0, 180)

    # monster count: 4

    BattleInfo(
        "BattleInfo_410", 0x0000, 90, 6, 60, 6, 1, 30, 0, "bm1020", "Sepith_24A4", 60, 25, 10, 5,
        (
            ("ms75200.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_2A8", "MonsterBattlePostion_308", "ed7450", "ed7453", "ATBonus_258"),
            ("ms75200.dat", "ms62700.dat", "ms62700.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_288", "MonsterBattlePostion_308", "ed7450", "ed7453", "ATBonus_258"),
            ("ms75200.dat", "ms62700.dat", "ms62700.dat", "ms62700.dat", 0, 0, 0, 0, "MonsterBattlePostion_2A8", "MonsterBattlePostion_308", "ed7450", "ed7453", "ATBonus_258"),
            ("ms75200.dat", "ms62700.dat", "ms62700.dat", "ms62700.dat", "ms62700.dat", 0, 0, 0, "MonsterBattlePostion_288", "MonsterBattlePostion_308", "ed7450", "ed7453", "ATBonus_258"),
        )
    )

    BattleInfo(
        "BattleInfo_348", 0x0000, 90, 6, 60, 6, 1, 25, 0, "bm1020", "Sepith_247C", 60, 25, 10, 5,
        (
            ("ms63300.dat", "ms63300.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_2A8", "MonsterBattlePostion_308", "ed7450", "ed7453", "ATBonus_258"),
            ("ms63300.dat", "ms64600.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_288", "MonsterBattlePostion_308", "ed7450", "ed7453", "ATBonus_258"),
            ("ms63300.dat", "ms64600.dat", "ms62800.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_2A8", "MonsterBattlePostion_308", "ed7450", "ed7453", "ATBonus_258"),
            ("ms63300.dat", "ms64600.dat", "ms62800.dat", "ms64600.dat", 0, 0, 0, 0, "MonsterBattlePostion_288", "MonsterBattlePostion_308", "ed7450", "ed7453", "ATBonus_258"),
        )
    )

    # event battle count: 1

    BattleInfo(
        "BattleInfo_4D8", 0x0042, 255, 6, 0, 0, 3, 0, 0, "bm1061", 0x00000000, 100, 0, 0, 0,
        (
            ("ms43300.dat", "ms80000.dat", "ms80000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_328", "MonsterBattlePostion_308", "ed7452", "ed7453", "ATBonus_268"),
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
        "monster/ch63350.itc",               # 10
        "monster/ch63351.itc",               # 11
        "monster/ch75250.itc",               # 12
        "monster/ch75250.itc",               # 13
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(4294966106, 4294948996, 4294949616, 0x1010000,    "BattleInfo_410", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(24240,   4294960546, 4294947496, 0x1010000,    "BattleInfo_348", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(4294935266, 940,     4294951736, 0x1010000,    "BattleInfo_410", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(4294967026, 17540,   4294953866, 0x1010000,    "BattleInfo_348", 0,   16,  0xFFFF, 0,  1)

    DeclActor(25500,   4294947496, 0,       1200,    25500,   4294948496, 0,       0x007C, 0,  2,  0x0000)
    DeclActor(0,       4294953846, 25400,   1200,    0,       4294954846, 25400,   0x007C, 0,  3,  0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 0
    ChipFrameInfo(800, 0, [0, 1, 2, 3, 4, 5])                    # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 2
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4])                      # 3

    ScpFunction((
        "Function_0_590",          # 00, 0
        "Function_1_5A7",          # 01, 1
        "Function_2_97B",          # 02, 2
        "Function_3_ACD",          # 03, 3
        "Function_4_C1F",          # 04, 4
        "Function_5_194B",         # 05, 5
        "Function_6_1967",         # 06, 6
        "Function_7_1982",         # 07, 7
        "Function_8_19C8",         # 08, 8
        "Function_9_19DB",         # 09, 9
        "Function_10_1A25",        # 0A, 10
        "Function_11_1A50",        # 0B, 11
        "Function_12_1A78",        # 0C, 12
        "Function_13_1AA3",        # 0D, 13
        "Function_14_1ACB",        # 0E, 14
        "Function_15_1AF6",        # 0F, 15
        "Function_16_244A",        # 10, 16
    ))


    def Function_0_590(): pass

    label("Function_0_590")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5A6")
    SetMapFlags(0x10000000)
    Event(0, 4)

    label("loc_5A6")

    Return()

    # Function_0_590 end

    def Function_1_5A7(): pass

    label("Function_1_5A7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5BE")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x15F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5BE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5F4")
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x4)
    OP_65(0x0, 0x1)
    OP_65(0x1, 0x1)

    label("loc_5F4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_608")
    SetMapObjFlags(0x2, 0x4)

    label("loc_608")

    OP_52(0xE, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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
    OP_52(0xE, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F7, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_95F")
    OP_70(0x0, 0x0)
    Jump("loc_963")

    label("loc_95F")

    OP_70(0x0, 0x1E)

    label("loc_963")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F7, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_976")
    OP_70(0x1, 0x0)
    Jump("loc_97A")

    label("loc_976")

    OP_70(0x1, 0x1E)

    label("loc_97A")

    Return()

    # Function_1_5A7 end

    def Function_2_97B(): pass

    label("Function_2_97B")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F7, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A77")
    Sound(14, 0, 100, 0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x462, 1)"), scpexpr(EXPR_END)), "loc_A00")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x462),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1F7, 3)
    OP_E0(0x5, 0x0)
    Jump("loc_A72")

    label("loc_A00")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x462),
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

    label("loc_A72")

    Jump("loc_AC1")

    label("loc_A77")

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

    label("loc_AC1")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_97B end

    def Function_3_ACD(): pass

    label("Function_3_ACD")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F7, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BC9")
    Sound(14, 0, 100, 0)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x5EF, 1)"), scpexpr(EXPR_END)), "loc_B52")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x5EF),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1F7, 4)
    OP_E0(0x5, 0x0)
    Jump("loc_BC4")

    label("loc_B52")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x5EF),
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

    label("loc_BC4")

    Jump("loc_C13")

    label("loc_BC9")

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

    label("loc_C13")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_ACD end

    def Function_4_C1F(): pass

    label("Function_4_C1F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00051.itc", 0x1F)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00151.itc", 0x21)
    LoadChrToIndex("chr/ch00250.itc", 0x22)
    LoadChrToIndex("chr/ch00251.itc", 0x23)
    LoadChrToIndex("chr/ch00350.itc", 0x24)
    LoadChrToIndex("chr/ch00351.itc", 0x25)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C81")
    LoadChrToIndex("chr/ch02950.itc", 0x26)
    LoadChrToIndex("chr/ch02951.itc", 0x27)
    LoadChrToIndex("chr/ch0295F.itc", 0x36)

    label("loc_C81")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CA5")
    LoadChrToIndex("chr/ch03150.itc", 0x26)
    LoadChrToIndex("chr/ch03151.itc", 0x27)
    LoadChrToIndex("chr/ch0315F.itc", 0x36)

    label("loc_CA5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CC9")
    LoadChrToIndex("chr/ch03250.itc", 0x26)
    LoadChrToIndex("chr/ch03251.itc", 0x27)
    LoadChrToIndex("chr/ch0325A.itc", 0x36)

    label("loc_CC9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CED")
    LoadChrToIndex("chr/ch02950.itc", 0x28)
    LoadChrToIndex("chr/ch02951.itc", 0x29)
    LoadChrToIndex("chr/ch0295F.itc", 0x37)

    label("loc_CED")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D11")
    LoadChrToIndex("chr/ch03150.itc", 0x28)
    LoadChrToIndex("chr/ch03151.itc", 0x29)
    LoadChrToIndex("chr/ch0315F.itc", 0x37)

    label("loc_D11")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D35")
    LoadChrToIndex("chr/ch03250.itc", 0x28)
    LoadChrToIndex("chr/ch03251.itc", 0x29)
    LoadChrToIndex("chr/ch0325A.itc", 0x37)

    label("loc_D35")

    LoadChrToIndex("chr/ch43350.itc", 0x2A)
    LoadChrToIndex("chr/ch43354.itc", 0x2E)
    LoadChrToIndex("monster/ch80050.itc", 0x30)
    LoadChrToIndex("monster/ch80051.itc", 0x31)
    LoadChrToIndex("chr/ch00056.itc", 0x32)
    LoadChrToIndex("chr/ch00156.itc", 0x33)
    LoadChrToIndex("chr/ch00256.itc", 0x34)
    LoadChrToIndex("chr/ch00356.itc", 0x35)
    LoadEffect(0x0, "event/ev10007.eff")
    LoadEffect(0x1, "event/ev17023.eff")
    LoadEffect(0x2, "battle\\mgaria0.eff")
    SoundLoad(832)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, 0, -17680, -40500, 0)
    SetChrPos(0x102, -780, -17680, -41420, 0)
    SetChrPos(0x103, 440, -17680, -41710, 0)
    SetChrPos(0x104, 1500, -17680, -42230, 0)
    SetChrPos(0xF4, -1340, -17680, -42430, 0)
    SetChrPos(0xF5, -150, -17680, -42790, 0)
    SetChrChipByIndex(0x8, 0x2A)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 0, -14150, -10850, 180)
    ClearChrFlags(0x9, 0x80)
    SetChrChipByIndex(0x9, 0x30)
    SetChrSubChip(0x9, 0x0)
    OP_52(0x9, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x7, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x9, 0, 0, 5)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 3500, -17180, -23500, 180)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xA, 0x30)
    SetChrSubChip(0xA, 0x0)
    OP_52(0xA, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xA, 0, 0, 5)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, -3500, -17180, -23500, 180)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(0, -16500, -32000, 0)
    MoveCamera(48, 30, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(32000, 0)
    SetCameraDistance(30000, 4000)
    FadeToBright(1000, 0)

    def lambda_F1B():
        OP_9B(0x0, 0xFE, 0x0, 0x38A4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F1B)
    Sleep(30)

    def lambda_F33():
        OP_9B(0x0, 0xFE, 0x0, 0x38A4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_F33)
    Sleep(30)

    def lambda_F4B():
        OP_9B(0x0, 0xFE, 0x0, 0x38A4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_F4B)
    Sleep(30)

    def lambda_F63():
        OP_9B(0x0, 0xFE, 0x0, 0x38A4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_F63)
    Sleep(30)

    def lambda_F7B():
        OP_9B(0x0, 0xFE, 0x0, 0x38A4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_F7B)
    Sleep(30)

    def lambda_F93():
        OP_9B(0x0, 0xFE, 0x0, 0x38A4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_F93)
    OP_6F(0x79)
    OP_0D()
    Fade(500)
    OP_68(0, -16280, -25500, 0)
    OP_68(0, -16780, -25500, 3000)
    MoveCamera(48, 27, 0, 0)
    OP_6E(590, 0)
    SetCameraDistance(17000, 0)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0xF4, 1)
    WaitChrThread(0xF5, 1)
    OP_6F(0x79)
    OP_0D()

    NpcTalk(
        0x8,
        "Girl's Voice",
        "#4P──Uh uh, good day to you all.\x02",
    )

    CloseMessageWindow()
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
    Fade(500)
    BlurSwitch(0xFA, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_68(0, -16780, -25000, 700)
    Sleep(300)
    BeginChrThread(0x101, 3, 0, 9)
    BeginChrThread(0x102, 3, 0, 10)
    BeginChrThread(0x103, 3, 0, 11)
    BeginChrThread(0x104, 3, 0, 12)
    BeginChrThread(0xF4, 3, 0, 13)
    BeginChrThread(0xF5, 3, 0, 14)
    OP_82(0x32, 0x32, 0x1388, 0x12C)
    Sound(551, 0, 50, 0)
    Sound(296, 0, 70, 0)
    Sound(308, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 1320, -17680, -24200, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    Sound(296, 0, 60, 0)
    Sound(308, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -1070, -17680, -24910, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    Sound(296, 0, 60, 0)
    Sound(308, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 70, -17680, -23040, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    WaitChrThread(0xF4, 3)
    WaitChrThread(0xF5, 3)
    OP_6F(0x79)
    CancelBlur(500)
    OP_0D()

    ChrTalk(
        0x101,
        "#00010F#12PWha...!?\x02",
    )

    CloseMessageWindow()
    OP_68(0, -13250, -10850, 2500)
    MoveCamera(45, 30, 0, 2500)
    OP_6E(590, 2500)
    SetCameraDistance(15500, 2500)
    OP_6F(0x79)

    NpcTalk(
        0x8,
        "Knight Dressed Girl",
        (
            "#5PI am a soldier of the Stahlritter,\x01",
            "Ennea the "Chiron".\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Knight Dressed Girl",
        "#5PI will make you leave this place.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(0, -15280, -15500, 0)
    OP_68(0, -16280, -27000, 3000)
    MoveCamera(135, 30, 0, 0)
    OP_6E(590, 0)
    SetCameraDistance(16500, 0)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x102,
        "#00107F#11PThe second walkｸre...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00311F#11PTch, a bow user?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(0, -13250, -10850, 0)
    MoveCamera(0, 30, 0, 0)
    OP_6E(590, 0)
    SetCameraDistance(15500, 0)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#5PYou are quite good to\x01",
            "have beaten Aines.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PI wonder if I can refrain\x01",
            "to go easy on you...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00007F...Going easy is unnecessary!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_14FD")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1484")
    OP_FC(0xB)
    Jump("loc_1499")

    label("loc_1484")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1499")
    OP_FC(0x5)

    label("loc_1499")

    OP_FD(0xC, 0x109)
    OP_FD(0x109, 0x101)

    ChrTalk(
        0x109,
        (
            "#10107F#13PIf you stand on our way, we'll\x01",
            "crush you with all our might!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_FD(0x109, 0xC)
    Jump("loc_1595")

    label("loc_14FD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1517")
    OP_FC(0xB)
    Jump("loc_152C")

    label("loc_1517")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_152C")
    OP_FC(0x5)

    label("loc_152C")

    OP_FD(0xC, 0x106)
    OP_FD(0x106, 0x101)

    ChrTalk(
        0x106,
        (
            "#10707F#13PIf you stand on our way, you'll have\x01",
            "a lot of trouble to deal with...!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_FD(0x106, 0xC)

    label("loc_1595")


    ChrTalk(
        0x8,
        "#5PUh uh, nice disposition.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopBGM(0xFA0)
    Fade(500)
    SetCameraDistance(15000, 200)
    Sound(357, 0, 80, 0)
    Sound(832, 2, 100, 0)
    PlayEffect(0x2, 0x0, 0x8, 0x5, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0x8, 0x2E)
    OP_A1(0x8, 0x3E8, 0x4, 0x0, 0x1, 0x2, 0x1)
    OP_A1(0x8, 0x3E8, 0x4, 0x0, 0x1, 0x2, 0x1)
    OP_A1(0x8, 0x4B0, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Sound(802, 0, 100, 0)
    StopEffect(0x0, 0x2)
    OP_6F(0x79)
    OP_0D()
    OP_68(0, -17200, -17500, 2000)
    MoveCamera(0, 10, 0, 2000)
    OP_6E(590, 2000)
    SetCameraDistance(25650, 2000)
    Sleep(1200)
    Sound(817, 0, 100, 0)
    BeginChrThread(0xB, 1, 0, 8)
    StopSound(832, 1000, 100)
    BeginChrThread(0x9, 3, 0, 7)
    BeginChrThread(0xA, 3, 0, 7)
    Sleep(1000)
    SetChrChipByIndex(0x8, 0x2A)
    SetChrSubChip(0x8, 0x0)
    WaitChrThread(0x9, 3)
    WaitChrThread(0xA, 3)
    OP_6F(0x79)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7452", 0)

    ChrTalk(
        0x8,
        "#6PCome now, show me...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6PIf you can slip through my battle\x01",
            "array and be qualified to reach\x01",
            "my Lord, Arianrhod!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00312F#11PHah! Fine with me...!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_17CD")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1775")
    OP_FC(0xB)
    Jump("loc_178A")

    label("loc_1775")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_178A")
    OP_FC(0x5)

    label("loc_178A")


    ChrTalk(
        0x105,
        (
            "#10407F#13PThat bow is a pain!\x01",
            "Pay the utmost attention!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1845")

    label("loc_17CD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_17E7")
    OP_FC(0xB)
    Jump("loc_17FC")

    label("loc_17E7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_17FC")
    OP_FC(0x5)

    label("loc_17FC")


    ChrTalk(
        0x106,
        (
            "#10707F#13PThat bow is dangerous!\x01",
            "Please, pay the utmost attention!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1845")


    ChrTalk(
        0x103,
        (
            "#00207F#11P──Roger that! I will be on the \x01",
            "lookout for sniping from above.\x02",
        )
    )

    CloseMessageWindow()
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_68(0, -18400, -17500, 700)
    SetCameraDistance(20000, 700)
    SetChrFlags(0x9, 0x20)
    SetChrChipByIndex(0x9, 0x31)
    SetChrSubChip(0x9, 0x0)
    BeginChrThread(0x9, 0, 0, 6)

    def lambda_18D5():
        OP_9B(0x1, 0xFE, 0x14, 0x1F40, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_18D5)
    SetChrFlags(0xA, 0x20)
    SetChrChipByIndex(0xA, 0x31)
    SetChrSubChip(0xA, 0x0)
    BeginChrThread(0xA, 0, 0, 6)

    def lambda_18FD():
        OP_9B(0x1, 0xFE, 0xFFEC, 0x1F40, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_18FD)
    Sleep(500)
    EndChrThread(0x9, 0x1)
    EndChrThread(0xA, 0x1)
    EndChrThread(0x9, 0x0)
    EndChrThread(0xA, 0x0)
    OP_24(0x340)
    Battle("BattleInfo_4D8", 0x30200011, 0x0, 0x100, 0x19, 0xFF)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    Call(0, 15)
    Return()

    # Function_4_C1F end

    def Function_5_194B(): pass

    label("Function_5_194B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1966")
    OP_A1(0xFE, 0x7D0, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_5_194B")

    label("loc_1966")

    Return()

    # Function_5_194B end

    def Function_6_1967(): pass

    label("Function_6_1967")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1981")
    OP_A1(0xFE, 0x7D0, 0x4, 0x0, 0x1, 0x2, 0x3)
    Jump("Function_6_1967")

    label("loc_1981")

    Return()

    # Function_6_1967 end

    def Function_7_1982(): pass

    label("Function_7_1982")

    PlayEffect(0x0, 0xFF, 0xFE, 0x5, 0, 100, 0, 0, 0, 0, 1650, 1650, 1650, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x7D0)
    Return()

    # Function_7_1982 end

    def Function_8_19C8(): pass

    label("Function_8_19C8")

    Sleep(900)
    Sound(223, 0, 100, 0)
    Sleep(600)
    Sound(936, 0, 70, 0)
    Return()

    # Function_8_19C8 end

    def Function_9_19DB(): pass

    label("Function_9_19DB")

    SetChrChipByIndex(0xFE, 0x32)
    SetChrSubChip(0xFE, 0x2)
    OP_9C(0xFE, 0x0, 0x0, 0xFFFFFA24, 0x2BC, 0xFA0)
    Sound(805, 0, 100, 0)
    Sound(531, 0, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1A1C")
    Sound(540, 0, 50, 0)

    label("loc_1A1C")

    SetChrChipByIndex(0xFE, 0x1E)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_9_19DB end

    def Function_10_1A25(): pass

    label("Function_10_1A25")

    Sleep(100)
    SetChrChipByIndex(0xFE, 0x33)
    SetChrSubChip(0xFE, 0x2)
    OP_9C(0xFE, 0x0, 0x0, 0xFFFFFA24, 0x2BC, 0xFA0)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_10_1A25 end

    def Function_11_1A50(): pass

    label("Function_11_1A50")

    SetChrChipByIndex(0xFE, 0x34)
    SetChrSubChip(0xFE, 0x2)
    OP_9C(0xFE, 0x0, 0x0, 0xFFFFFA24, 0x2BC, 0xFA0)
    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_11_1A50 end

    def Function_12_1A78(): pass

    label("Function_12_1A78")

    Sleep(100)
    SetChrChipByIndex(0xFE, 0x35)
    SetChrSubChip(0xFE, 0x2)
    OP_9C(0xFE, 0x0, 0x0, 0xFFFFFA24, 0x2BC, 0xFA0)
    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_12_1A78 end

    def Function_13_1AA3(): pass

    label("Function_13_1AA3")

    SetChrChipByIndex(0xFE, 0x36)
    SetChrSubChip(0xFE, 0x2)
    OP_9C(0xFE, 0x0, 0x0, 0xFFFFFA24, 0x2BC, 0xFA0)
    SetChrChipByIndex(0xFE, 0x26)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_13_1AA3 end

    def Function_14_1ACB(): pass

    label("Function_14_1ACB")

    Sleep(100)
    SetChrChipByIndex(0xFE, 0x37)
    SetChrSubChip(0xFE, 0x2)
    OP_9C(0xFE, 0x0, 0x0, 0xFFFFFA24, 0x2BC, 0xFA0)
    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_14_1ACB end

    def Function_15_1AF6(): pass

    label("Function_15_1AF6")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1B34")
    LoadChrToIndex("chr/ch02950.itc", 0x22)

    label("loc_1B34")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1B4C")
    LoadChrToIndex("chr/ch03150.itc", 0x22)

    label("loc_1B4C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1B64")
    LoadChrToIndex("chr/ch03250.itc", 0x22)

    label("loc_1B64")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1B7C")
    LoadChrToIndex("chr/ch02950.itc", 0x23)

    label("loc_1B7C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1B94")
    LoadChrToIndex("chr/ch03150.itc", 0x23)

    label("loc_1B94")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1BAC")
    LoadChrToIndex("chr/ch03250.itc", 0x23)

    label("loc_1BAC")

    LoadChrToIndex("chr/ch43350.itc", 0x24)
    LoadChrToIndex("chr/ch43353.itc", 0x25)
    LoadChrToIndex("chr/ch43354.itc", 0x26)
    LoadChrToIndex("chr/ch43300.itc", 0x27)
    LoadEffect(0x0, "event/ev10006.eff")
    LoadEffect(0x1, "event/ev10007.eff")
    SoundLoad(832)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, 0, -17680, -28500, 0)
    SetChrPos(0x102, 830, -17680, -29320, 0)
    SetChrPos(0x103, -440, -17680, -29610, 0)
    SetChrPos(0x104, -1500, -17680, -30030, 0)
    SetChrPos(0xF4, 1490, -17680, -30130, 0)
    SetChrPos(0xF5, 150, -17680, -30490, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0xF4, 0x22)
    SetChrSubChip(0xF4, 0x0)
    SetChrChipByIndex(0xF5, 0x23)
    SetChrSubChip(0xF5, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 0x25)
    SetChrSubChip(0x8, 0x3)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 0, -17680, -23000, 180)
    OP_68(0, -16780, -26000, 0)
    OP_68(0, -16780, -25000, 2500)
    MoveCamera(45, 25, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(18700, 0)
    FadeToBright(1000, 0)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x8,
        "#5P*sigh*...I surrender.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PIt seems I will be scolded\x01",
            "by Duvalie later...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(400)
    SetCameraDistance(18200, 800)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0x8, 0x24)
    SetChrSubChip(0x8, 0x0)
    OP_0D()
    Sleep(100)
    SetChrChipByIndex(0x8, 0x26)
    OP_A1(0x8, 0x3E8, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Sound(812, 0, 100, 0)
    Fade(500)
    SetCameraDistance(17800, 0)
    Sound(832, 2, 100, 0)
    Sound(357, 0, 100, 0)
    PlayEffect(0x0, 0x0, 0x8, 0x5, 0, 100, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    SetChrChipByIndex(0x8, 0x24)
    SetChrSubChip(0x8, 0x0)
    OP_0D()
    OP_6F(0x79)
    OP_0D()
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
        0x8,
        "#5PWell then── Only one remains.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PAs you might expect from being\x01",
            "our head, her strength is the real deal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PBe very well prepared.\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(16800, 2000)
    BeginChrThread(0xB, 1, 0, 16)
    StopEffect(0x0, 0x2)
    PlayEffect(0x1, 0x0, 0x8, 0x5, 0, 100, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_6F(0x79)
    Fade(500)
    SetCameraDistance(18700, 1000)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    Sound(936, 0, 100, 0)
    StopSound(832, 500, 100)

    def lambda_1F9A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0xFA)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1F9A)
    WaitChrThread(0x8, 2)
    CancelBlur(1000)
    OP_6F(0x79)
    OP_0D()
    SetChrFlags(0x8, 0x80)
    Sleep(700)
    OP_68(0, -16780, -27000, 2500)
    OP_6F(0x79)
    Fade(250)
    Sound(805, 0, 100, 0)
    Sound(531, 0, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1FF4")
    Sound(540, 0, 50, 0)

    label("loc_1FF4")

    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0xF4, 0xFF)
    SetChrSubChip(0xF4, 0x0)
    SetChrChipByIndex(0xF5, 0xFF)
    SetChrSubChip(0xF5, 0x0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_206E")

    ChrTalk(
        0x109,
        (
            "#10106F#12P*haah*...\x01",
            "We bested her, somehow...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20A0")

    label("loc_206E")


    ChrTalk(
        0x105,
        (
            "#10406F#12POh boy...\x01",
            "We bested her, somehow?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20A0")


    ChrTalk(
        0x104,
        (
            "#00306F#12PYeah...\x01",
            "That was quite the close one.\x02\x03",
            "#00301FI'd never thought someone could snipe\x01",
            "with the bow like Gareth does.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F#12PHowever, I thought she would have\x01",
            "only sniped at us from above, but...\x02\x03",
            "#00200FShe even honestly came down.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_21ED")

    ChrTalk(
        0x106,
        (
            "#10704F#12PIt could be that she\x01",
            "esteemed her pride.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_222B")

    label("loc_21ED")


    ChrTalk(
        0x105,
        (
            "#10404F#12PAs I thought, she seemed\x01",
            "to esteem her pride.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_222B")


    ChrTalk(
        0x102,
        (
            "#00106F#12PRight, like an old style,\x01",
            "rare for these days...\x02\x03",
            "#00108FIt's like she put in real practice\x01",
            "the Middle Ages chivalry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F#12PYeah, now that you mention it...\x02\x03",
            "#00006F"Ouroboros"...\x01",
            "It's really an unfathomable group.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F#12PWell, at any rate the next 'ne\x01",
            "appears to be the last underling.\x02\x03",
            "#00301FIt seems she'll be a formidable opponent...\x01",
            "We can only do our best, I guess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00013F#12PYeah...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00201F#12PLet's go.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    OP_D7(0x22)
    OP_D7(0x23)
    OP_D7(0x24)
    OP_D7(0x25)
    OP_D7(0x26)
    OP_D7(0x27)
    OP_37()
    SetChrPos(0x0, 0, -17680, -25500, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x1A5, 0)
    OP_24(0x340)
    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_15_1AF6 end

    def Function_16_244A(): pass

    label("Function_16_244A")

    Sleep(1100)
    Sound(222, 0, 80, 0)
    Return()

    # Function_16_244A end

    SaveToFile()

Try(main)
