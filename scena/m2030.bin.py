﻿from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "m2030.bin",                # FileName
        "m2030",                    # MapName
        "m2030",                    # Location
        0x0075,                     # MapIndex
        "ed7303",
        0x00080000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x23,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 117, 0, 0, 0, 1],
    )

    BuildStringList((
        "m2030",                  # 0
        "bm2000",                 # 1
        "bm2000",                 # 2
    ))

    ATBonus("ATBonus_32C", 100, 5, 1, 5, 1, 5, 1, 5, 5, 5, 5, 5, 5, 0, 0, 0)

    Sepith("Sepith_1111", 6,   6,   0,   4,   6,   0,   6)
    Sepith("Sepith_1109", 9,   6,   2,   5,   3,   0,   3)

    MonsterBattlePostion("MonsterBattlePostion_35C", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_360", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_364", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_368", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_36C", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_370", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_374", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_378", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_3DC", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_3E0", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_3E4", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_3E8", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_3EC", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_3F0", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_3F4", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_3F8", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_37C", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_380", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_384", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_388", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_38C", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_390", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_394", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_398", 8, 14, 180)

    # monster count: 6

    BattleInfo(
        "BattleInfo_4C4", 0x0000, 63, 6, 60, 4, 1, 30, 0, "bm2000", "Sepith_1111", 40, 30, 20, 10,
        (
            ("ms74400.dat", "ms74400.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_35C", "MonsterBattlePostion_3DC", "ed7450", "ed7453", "ATBonus_32C"),
            ("ms74400.dat", "ms74400.dat", "ms74400.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_37C", "MonsterBattlePostion_3DC", "ed7450", "ed7453", "ATBonus_32C"),
            ("ms74400.dat", "ms74400.dat", "ms74400.dat", "ms74400.dat", 0, 0, 0, 0, "MonsterBattlePostion_35C", "MonsterBattlePostion_3DC", "ed7450", "ed7453", "ATBonus_32C"),
            ("ms74400.dat", "ms74400.dat", "ms74400.dat", "ms74400.dat", "ms74400.dat", 0, 0, 0, "MonsterBattlePostion_37C", "MonsterBattlePostion_3DC", "ed7450", "ed7453", "ATBonus_32C"),
        )
    )

    BattleInfo(
        "BattleInfo_3FC", 0x0000, 63, 6, 60, 4, 1, 30, 0, "bm2000", "Sepith_1109", 40, 30, 20, 10,
        (
            ("ms74300.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_37C", "MonsterBattlePostion_3DC", "ed7450", "ed7453", "ATBonus_32C"),
            ("ms74300.dat", "ms74300.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_35C", "MonsterBattlePostion_3DC", "ed7450", "ed7453", "ATBonus_32C"),
            ("ms74300.dat", "ms74300.dat", "ms74300.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_37C", "MonsterBattlePostion_3DC", "ed7450", "ed7453", "ATBonus_32C"),
            ("ms74300.dat", "ms74300.dat", "ms74300.dat", "ms74300.dat", 0, 0, 0, 0, "MonsterBattlePostion_35C", "MonsterBattlePostion_3DC", "ed7450", "ed7453", "ATBonus_32C"),
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
        "monster/ch74350.itc",               # 10
        "monster/ch74350.itc",               # 11
        "monster/ch74450.itc",               # 12
        "monster/ch74450.itc",               # 13
    ))

    DeclMonster(19660,   4294966666, 4294963296, 0x1010000,    "BattleInfo_4C4", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(10620,   4294959886, 4294955296, 0x1010000,    "BattleInfo_3FC", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(4294858096, 4294966806, 0,       0x1010000,    "BattleInfo_4C4", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(4294857076, 3280,    0,       0x1010000,    "BattleInfo_4C4", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(170,     4294883386, 0,       0x1010000,    "BattleInfo_3FC", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(4294766986, 4294882336, 0,       0x1010000,    "BattleInfo_3FC", 0,   16,  0xFFFF, 0,  1)

    DeclActor(4294767296, 800,     88400,   1200,    4294767296, 1800,    88400,   0x007C, 0,  2,  0x0000)
    DeclActor(4294767296, 0,       4294880296, 1200,    4294767296, 1000,    4294880296, 0x007C, 0,  3,  0x0000)
    DeclActor(14000,   4294955296, 4294957796, 1200,    14000,   4294956296, 4294957796, 0x007C, 0,  4,  0x0000)
    DeclActor(4294881296, 0,       8000,    1200,    4294881296, 1000,    8000,    0x007C, 0,  5,  0x0000)
    DeclActor(4294865296, 0,       8000,    1200,    4294865296, 1000,    8000,    0x007C, 0,  5,  0x0000)
    DeclActor(4294849296, 0,       8000,    1200,    4294849296, 1000,    8000,    0x007C, 0,  5,  0x0000)
    DeclActor(4294881296, 0,       4294959296, 1200,    4294881296, 1000,    4294959296, 0x007C, 0,  5,  0x0000)
    DeclActor(4294865296, 0,       4294959296, 1200,    4294865296, 1000,    4294959296, 0x007C, 0,  5,  0x0000)
    DeclActor(4294849296, 0,       4294959296, 1200,    4294849296, 1000,    4294959296, 0x007C, 0,  5,  0x0000)
    DeclActor(4294867296, 0,       89000,   1200,    4294867296, 1500,    89000,   0x007C, 0,  6,  0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 0
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4])                      # 1
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 5])                   # 2
    ChipFrameInfo(3000, 0, [0, 1, 2, 3, 4, 5])                   # 3

    ScpFunction((
        "Function_0_5D8",          # 00, 0
        "Function_1_5D9",          # 01, 1
        "Function_2_AF4",          # 02, 2
        "Function_3_C46",          # 03, 3
        "Function_4_D98",          # 04, 4
        "Function_5_EF2",          # 05, 5
        "Function_6_F1E",          # 06, 6
    ))


    def Function_0_5D8(): pass

    label("Function_0_5D8")

    Return()

    # Function_0_5D8 end

    def Function_1_5D9(): pass

    label("Function_1_5D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 5)), scpexpr(EXPR_END)), "loc_5EB")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x130), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5EB")

    Sound(129, 1, 100, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_605")
    SetMapObjFlags(0xA, 0x4)

    label("loc_605")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B7, 4)), scpexpr(EXPR_END)), "loc_651")
    SetMapObjFrame(0xA, "b_in", 0x0, 0x1)
    SetMapObjFrame(0xA, "b_in2", 0x0, 0x1)
    SetMapObjFrame(0xA, "b_out", 0x0, 0x1)
    SetMapObjFrame(0xA, "b_out2", 0x0, 0x1)
    SetMapObjFrame(0xA, "b_light", 0x0, 0x1)

    label("loc_651")

    OP_52(0x9, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xA7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xA7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xA7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xA7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xA7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xA7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xA7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xA7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xA7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xA7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xA7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xA7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xA7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xA7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xA7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xA7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xA7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xA7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xA7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xA7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xA7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xA7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xA7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xA7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    PlayEffect(0x2F, 0x0, 0x8, 0x41, 0, 0, 0, 0, 0, 0, 1250, 750, 1250, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2F, 0x1, 0x9, 0x41, 0, 0, 0, 0, 0, 0, 1250, 750, 1250, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2F, 0x2, 0xA, 0x41, 0, 0, 0, 0, 0, 0, 1250, 750, 1250, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2F, 0x3, 0xB, 0x41, 0, 0, 0, 0, 0, 0, 1250, 750, 1250, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2F, 0x4, 0xC, 0x41, 0, 0, 0, 0, 0, 0, 1250, 750, 1250, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2F, 0x5, 0xD, 0x41, 0, 0, 0, 0, 0, 0, 1250, 750, 1250, 0xFF, 0, 0, 0, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A96")
    SetBarrier(0x0, 0x0, 0x1, 0x0, -86000, 0, 8000, 6000, 3000, 0)
    SetBarrier(0x3, 0x0, 0x1)
    ClearMapObjFlags(0x1, 0x10)
    SetBarrier(0x0, 0x1, 0x1, 0x0, -102000, 0, 8000, 6000, 3000, 0)
    SetBarrier(0x3, 0x1, 0x1)
    ClearMapObjFlags(0x2, 0x10)
    SetBarrier(0x0, 0x2, 0x1, 0x0, -118000, 0, 8000, 6000, 3000, 0)
    SetBarrier(0x3, 0x2, 0x1)
    ClearMapObjFlags(0x3, 0x10)
    SetBarrier(0x0, 0x3, 0x1, 0x0, -86000, 0, -8000, 6000, 3000, 0)
    SetBarrier(0x3, 0x3, 0x1)
    SetBarrier(0x0, 0x4, 0x1, 0x0, -102000, 0, -8000, 6000, 3000, 0)
    SetBarrier(0x3, 0x4, 0x1)
    SetBarrier(0x0, 0x5, 0x1, 0x0, -118000, 0, -8000, 6000, 3000, 0)
    SetBarrier(0x3, 0x5, 0x1)
    Jump("loc_AAE")

    label("loc_A96")

    OP_65(0x3, 0x1)
    OP_65(0x4, 0x1)
    OP_65(0x5, 0x1)
    OP_65(0x6, 0x1)
    OP_65(0x7, 0x1)
    OP_65(0x8, 0x1)

    label("loc_AAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EE, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AC1")
    OP_70(0x7, 0x0)
    Jump("loc_AC5")

    label("loc_AC1")

    OP_70(0x7, 0x1E)

    label("loc_AC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EE, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AD8")
    OP_70(0x8, 0x0)
    Jump("loc_ADC")

    label("loc_AD8")

    OP_70(0x8, 0x1E)

    label("loc_ADC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EE, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AEF")
    OP_70(0x9, 0x0)
    Jump("loc_AF3")

    label("loc_AEF")

    OP_70(0x9, 0x1E)

    label("loc_AF3")

    Return()

    # Function_1_5D9 end

    def Function_2_AF4(): pass

    label("Function_2_AF4")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EE, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BF0")
    Sound(14, 0, 100, 0)
    OP_74(0x7, 0x1E)
    OP_71(0x7, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x653, 1)"), scpexpr(EXPR_END)), "loc_B79")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x653),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1EE, 3)
    OP_E0(0x5, 0x0)
    Jump("loc_BEB")

    label("loc_B79")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x653),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " is inside the chest.\x01",
            "Since you have too many, you gave it up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x7, 0x1E, 0x0, 0x0, 0x0)

    label("loc_BEB")

    Jump("loc_C3A")

    label("loc_BF0")

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

    label("loc_C3A")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_AF4 end

    def Function_3_C46(): pass

    label("Function_3_C46")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EE, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D42")
    Sound(14, 0, 100, 0)
    OP_74(0x8, 0x1E)
    OP_71(0x8, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1F7, 1)"), scpexpr(EXPR_END)), "loc_CCB")
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
    SetScenarioFlags(0x1EE, 4)
    OP_E0(0x5, 0x0)
    Jump("loc_D3D")

    label("loc_CCB")

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
    OP_71(0x8, 0x1E, 0x0, 0x0, 0x0)

    label("loc_D3D")

    Jump("loc_D8C")

    label("loc_D42")

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

    label("loc_D8C")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_C46 end

    def Function_4_D98(): pass

    label("Function_4_D98")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EE, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EC2")
    Sound(14, 0, 100, 0)
    OP_74(0x9, 0x1E)
    OP_71(0x9, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    OP_70(0x9, 0x1E)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddSepith(0x0, 80)
    AddSepith(0x1, 80)
    AddSepith(0x2, 80)
    AddSepith(0x3, 80)
    AddSepith(0x4, 80)
    AddSepith(0x5, 80)
    AddSepith(0x6, 80)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#56IEarth Sepith x80\x01\x07\x02",
            "#57IWater Sepith x80\x01\x07\x02",
            "#58IFire Sepith x80\x01\x07\x02",
            "#59IWind Sepith x80\x01\x07\x02",
            "#60ITime Sepith x80\x01\x07\x02",
            "#61ISpace Sepith x80\x01\x07\x02",
            "#62IMirage Sepith x80\x01\x07\x00",
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x1EE, 5)
    OP_E0(0x5, 0x0)
    Jump("loc_EE0")

    label("loc_EC2")


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

    label("loc_EE0")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_D98 end

    def Function_5_EF2(): pass

    label("Function_5_EF2")

    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The gate is firmly shut.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_5_EF2 end

    def Function_6_F1E(): pass

    label("Function_6_F1E")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B7, 4)), scpexpr(EXPR_END)), "loc_F5C")
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
    Jump("loc_10D8")

    label("loc_F5C")

    EventBegin(0x1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A pearl is on the pedestal.\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Take Pearl\x01",      # 0
            "Cancel\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10D1")
    Fade(500)
    SetChrPos(0x0, -100000, 0, 87500, 0)
    SetChrPos(0x1, -99000, 0, 86500, 0)
    SetChrPos(0x2, -101000, 0, 86500, 0)
    SetChrPos(0x3, -100000, 0, 85500, 0)
    OP_68(-100380, 600, 88360, 0)
    MoveCamera(35, 26, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(20150, 0)
    OP_0D()
    Sleep(500)
    Sleep(1000)
    Sound(802, 0, 100, 0)
    Fade(200)
    SetMapObjFrame(0xA, "b_in", 0x0, 0x1)
    SetMapObjFrame(0xA, "b_in2", 0x0, 0x1)
    SetMapObjFrame(0xA, "b_out", 0x0, 0x1)
    SetMapObjFrame(0xA, "b_out2", 0x0, 0x1)
    SetMapObjFrame(0xA, "b_light", 0x0, 0x1)
    OP_0D()
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x33E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x33E, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x1B7, 4)
    OP_E2(0x2)

    label("loc_10D1")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)

    label("loc_10D8")

    Return()

    # Function_6_F1E end

    SaveToFile()

Try(main)
