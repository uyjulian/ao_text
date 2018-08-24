﻿from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "e4212.bin",                # FileName
        "e4212",                    # MapName
        "e4212",                    # Location
        0x00D2,                     # MapIndex
        "ed7251",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x07,                       # PreInitFunctionIndex
        b'\x00\xff\x00',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 2],
    )

    BuildStringList((
        "e4212",                  # 0
        "Estelle",                # 1
        "Joshua",                 # 2
        "Renne",                  # 3
        "アイオーン３",           # 4
        "Pater-Mater",            # 5
        "パテルマテル影",         # 6
        "短剣目標",               # 7
        "ミサイル目標",           # 8
        "ミサイル目標",           # 9
        "ミサイル目標",           # 10
        "ミサイル目標",           # 11
        "ミサイル目標",           # 12
        "ミサイル目標",           # 13
        "Estelle",                # 14
        "空",                     # 15
        "SE制御",                 # 16
        "br1060",                 # 17
    ))

    ATBonus("ATBonus_398", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_4BEB", 5,   5,   5,   5,   5,   5,   5)

    MonsterBattlePostion("MonsterBattlePostion_3F8", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_3FC", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_400", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_404", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_408", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_40C", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_410", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_414", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_458", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_45C", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_460", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_464", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_468", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_46C", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_470", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_474", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_3D8", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_3DC", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_3E0", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_3E4", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_3E8", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_3EC", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_3F0", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_3F4", 2, 13, 180)

    # monster count: 4

    BattleInfo(
        "BattleInfo_478", 0x0000, 50, 6, 60, 8, 1, 60, 0, "br1060", "Sepith_4BEB", 30, 40, 20, 10,
        (
            ("ms80800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3F8", "MonsterBattlePostion_458", "ed7450", "ed7453", "ATBonus_398"),
            ("ms80800.dat", "ms80800.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3D8", "MonsterBattlePostion_458", "ed7450", "ed7453", "ATBonus_398"),
            ("ms80800.dat", "ms80800.dat", "ms80800.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_3F8", "MonsterBattlePostion_458", "ed7450", "ed7453", "ATBonus_398"),
            ("ms80800.dat", "ms80800.dat", "ms80800.dat", "ms80800.dat", 0, 0, 0, 0, "MonsterBattlePostion_3D8", "MonsterBattlePostion_458", "ed7450", "ed7453", "ATBonus_398"),
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
        "monster/ch80850.itc",               # 10
        "monster/ch80851.itc",               # 11
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    192,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    192,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    192,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    192,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    192,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    192,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    192,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    192,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(880,     4294965516, 0,       0x10100C3,    "BattleInfo_478", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(4294936256, 4294956646, 0,       0x1010069,    "BattleInfo_478", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(4294916646, 4294943556, 10,      0x101011D,    "BattleInfo_478", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(4294881406, 4294938536, 0,       0x101004B,    "BattleInfo_478", 0,   16,  0xFFFF, 0,  1)

    DeclActor(4294894996, 0,       4294960596, 1200,    4294894996, 1000,    4294960596, 0x007C, 0,  3,  0x0000)
    DeclActor(10780,   100,     4294950946, 1200,    10780,   1100,    4294950946, 0x007C, 0,  4,  0x0000)
    DeclActor(4294924026, 0,       4294939446, 1500,    4294924026, 1500,    4294939446, 0x007C, 0,  72, 0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 0
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 1

    ScpFunction((
        "Function_0_67C",          # 00, 0
        "Function_1_6AA",          # 01, 1
        "Function_2_6CB",          # 02, 2
        "Function_3_B77",          # 03, 3
        "Function_4_CC8",          # 04, 4
        "Function_5_E19",          # 05, 5
        "Function_6_E48",          # 06, 6
        "Function_7_25DC",         # 07, 7
        "Function_8_266E",         # 08, 8
        "Function_9_269B",         # 09, 9
        "Function_10_2794",        # 0A, 10
        "Function_11_281C",        # 0B, 11
        "Function_12_290C",        # 0C, 12
        "Function_13_29EB",        # 0D, 13
        "Function_14_29FF",        # 0E, 14
        "Function_15_2A1D",        # 0F, 15
        "Function_16_2A4F",        # 10, 16
        "Function_17_2A8B",        # 11, 17
        "Function_18_2AF2",        # 12, 18
        "Function_19_2B2C",        # 13, 19
        "Function_20_2CF1",        # 14, 20
        "Function_21_2FD4",        # 15, 21
        "Function_22_308A",        # 16, 22
        "Function_23_30FC",        # 17, 23
        "Function_24_3120",        # 18, 24
        "Function_25_31DA",        # 19, 25
        "Function_26_329A",        # 1A, 26
        "Function_27_3372",        # 1B, 27
        "Function_28_3396",        # 1C, 28
        "Function_29_33B9",        # 1D, 29
        "Function_30_3493",        # 1E, 30
        "Function_31_34D0",        # 1F, 31
        "Function_32_350D",        # 20, 32
        "Function_33_3537",        # 21, 33
        "Function_34_3560",        # 22, 34
        "Function_35_361A",        # 23, 35
        "Function_36_3634",        # 24, 36
        "Function_37_3646",        # 25, 37
        "Function_38_3750",        # 26, 38
        "Function_39_377E",        # 27, 39
        "Function_40_39A7",        # 28, 40
        "Function_41_3A38",        # 29, 41
        "Function_42_3A50",        # 2A, 42
        "Function_43_3DFF",        # 2B, 43
        "Function_44_3E62",        # 2C, 44
        "Function_45_3EAD",        # 2D, 45
        "Function_46_3F80",        # 2E, 46
        "Function_47_3FEC",        # 2F, 47
        "Function_48_40A9",        # 30, 48
        "Function_49_40C9",        # 31, 49
        "Function_50_41AB",        # 32, 50
        "Function_51_4230",        # 33, 51
        "Function_52_4354",        # 34, 52
        "Function_53_436D",        # 35, 53
        "Function_54_4560",        # 36, 54
        "Function_55_474B",        # 37, 55
        "Function_56_4762",        # 38, 56
        "Function_57_4773",        # 39, 57
        "Function_58_4834",        # 3A, 58
        "Function_59_485E",        # 3B, 59
        "Function_60_48A6",        # 3C, 60
        "Function_61_48B9",        # 3D, 61
        "Function_62_4996",        # 3E, 62
        "Function_63_49AB",        # 3F, 63
        "Function_64_49CF",        # 40, 64
        "Function_65_49F3",        # 41, 65
        "Function_66_4A25",        # 42, 66
        "Function_67_4A49",        # 43, 67
        "Function_68_4A82",        # 44, 68
        "Function_69_4AA8",        # 45, 69
        "Function_70_4ABC",        # 46, 70
        "Function_71_4AE1",        # 47, 71
        "Function_72_4B06",        # 48, 72
    ))


    def Function_0_67C(): pass

    label("Function_0_67C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_697")
    SetMapObjFlags(0x0, 0x2000000)
    SetMapObjFlags(0x1, 0x2000000)
    Jump("loc_6A9")

    label("loc_697")

    SetMapObjFlags(0x7, 0x2000000)
    SetMapObjFlags(0x8, 0x2000000)
    SetMapObjFlags(0x9, 0x2000000)

    label("loc_6A9")

    Return()

    # Function_0_67C end

    def Function_1_6AA(): pass

    label("Function_1_6AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_6B5")
    OP_E2(0x1)

    label("loc_6B5")

    ClearScenarioFlags(0x0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_6CA")
    ClearScenarioFlags(0x22, 0)
    SetScenarioFlags(0x0, 0)
    Event(0, 6)

    label("loc_6CA")

    Return()

    # Function_1_6AA end

    def Function_2_6CB(): pass

    label("Function_2_6CB")

    OP_52(0x18, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6D6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6D6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6D6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6D6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_A69")
    SetMapObjFrame(0xFF, "mae00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "mae01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "mae02", 0x0, 0x1)
    SetMapObjFrame(0xFF, "maewood", 0x0, 0x1)
    SetMapObjFrame(0xFF, "maekusa00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "maekusa01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "maekusa02", 0x0, 0x1)
    SetMapObjFrame(0xFF, "maekage", 0x0, 0x1)
    Jump("loc_AC3")

    label("loc_A69")

    SetMapObjFrame(0xFF, "ato00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ato01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ato02", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ato03", 0x0, 0x1)
    SetMapObjFrame(0xFF, "atokizu_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "atokumo_add", 0x0, 0x1)

    label("loc_AC3")

    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x78, 0x0)
    LoadEffect(0x10, "event\\eva00_00.eff")
    OP_65(0x2, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18A, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B3E")
    PlayEffect(0x10, 0x9, 0xFF, 0x0, -43270, 0, -27850, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x2, 0x1)

    label("loc_B3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B76")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F6, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B5B")
    OP_70(0x7, 0x0)
    Jump("loc_B5F")

    label("loc_B5B")

    OP_70(0x7, 0x1E)

    label("loc_B5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F6, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B72")
    OP_70(0x8, 0x0)
    Jump("loc_B76")

    label("loc_B72")

    OP_70(0x8, 0x1E)

    label("loc_B76")

    Return()

    # Function_2_6CB end

    def Function_3_B77(): pass

    label("Function_3_B77")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F6, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C73")
    Sound(14, 0, 100, 0)
    OP_74(0x7, 0x1E)
    OP_71(0x7, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x20C, 1)"), scpexpr(EXPR_END)), "loc_BFC")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x20C),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1F6, 5)
    OP_E0(0x5, 0x0)
    Jump("loc_C6E")

    label("loc_BFC")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x20C),
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

    label("loc_C6E")

    Jump("loc_CBC")

    label("loc_C73")

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

    label("loc_CBC")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_B77 end

    def Function_4_CC8(): pass

    label("Function_4_CC8")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F6, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DC4")
    Sound(14, 0, 100, 0)
    OP_74(0x8, 0x1E)
    OP_71(0x8, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x5EE, 1)"), scpexpr(EXPR_END)), "loc_D4D")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x5EE),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1F6, 6)
    OP_E0(0x5, 0x0)
    Jump("loc_DBF")

    label("loc_D4D")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x5EE),
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

    label("loc_DBF")

    Jump("loc_E0D")

    label("loc_DC4")

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

    label("loc_E0D")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_CC8 end

    def Function_5_E19(): pass

    label("Function_5_E19")

    OP_8A(0x0)
    OP_8A(0x1)
    LoadEffect(0x0, "event/ev600_00.eff")
    LoadEffect(0x1, "event/ev600_01.eff")
    Return()

    # Function_5_E19 end

    def Function_6_E48(): pass

    label("Function_6_E48")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x1)
    OP_F3(100000)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    LoadChrToIndex("apl/ch50547.itc", 0x22)
    LoadChrToIndex("apl/ch50338.itc", 0x23)
    LoadChrToIndex("chr/ch00650.itc", 0x24)
    LoadChrToIndex("chr/ch00651.itc", 0x25)
    LoadChrToIndex("chr/ch00750.itc", 0x26)
    LoadChrToIndex("chr/ch00701.itc", 0x27)
    LoadChrToIndex("chr/ch00752.itc", 0x28)
    LoadChrToIndex("apl/ch50338.itc", 0x29)
    LoadChrToIndex("chr/ch09556.itc", 0x2A)
    LoadChrToIndex("chr/ch00653.itc", 0x2B)
    LoadChrToIndex("chr/ch00753.itc", 0x2C)
    LoadChrToIndex("apl/ch51724.itc", 0x2D)
    LoadChrToIndex("apl/ch51725.itc", 0x2E)
    LoadEffect(0x2, "event/ev10018.eff")
    LoadEffect(0x0, "event/eva01_01.eff")
    LoadEffect(0x3, "event/ev17045.eff")
    LoadEffect(0x4, "event/ev17043.eff")
    LoadEffect(0x5, "event/ev17040.eff")
    LoadEffect(0x6, "event/ev17041.eff")
    LoadEffect(0x7, "battle/mgaria0.eff")
    LoadEffect(0x8, "event/ev17063.eff")
    LoadEffect(0x9, "event/ev15040.eff")
    LoadEffect(0xA, "event/ev17044.eff")
    SoundLoad(852)
    SoundLoad(979)
    SoundLoad(579)
    SoundLoad(931)
    SoundLoad(904)
    SoundLoad(996)
    SoundLoad(993)
    SoundLoad(288)
    SoundLoad(902)
    SoundLoad(1042)
    SoundLoad(1043)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    ClearMapObjFlags(0x0, 0x4)
    ClearMapObjFlags(0x0, 0x1000)
    ClearMapObjFlags(0x1, 0x4)
    ClearMapObjFlags(0x1, 0x1000)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -50000, 0, -15000, 0)
    OP_74(0x1, 0x1E)
    OP_78(0x1, 0xB)
    OP_93(0xB, 0x10E, 0x0)
    SetChrFlags(0xB, 0x1)
    OP_52(0xB, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1B58), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapObjFlags(0x1, 0x1000)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x172, 0x19A, 0x0, 0x20)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, -66000, 0, -15000, 0)
    OP_74(0x0, 0x1E)
    OP_78(0x0, 0xC)
    OP_93(0xC, 0x5A, 0x0)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xC, 0x1)
    OP_52(0xC, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1388), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapObjFlags(0x0, 0x1000)
    OP_71(0x0, 0x1A5, 0x1CC, 0x1, 0x20)
    ClearChrFlags(0xD, 0x80)
    SetChrChipByIndex(0xD, 0x22)
    OP_52(0xD, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1388), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xD, 0x8)
    SetChrFlags(0xD, 0x8000)
    SetChrChipByIndex(0xA, 0x2D)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x4)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xA, 0x2)
    SetChrFlags(0xA, 0x1000)
    OP_52(0xA, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0xA, -56000, 2000, -35000, 0)
    OP_52(0xA, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x8, 0x2B)
    SetChrSubChip(0x8, 0x2)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, -54000, 2000, -37000, 0)
    OP_52(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x9, 0x2C)
    SetChrSubChip(0x9, 0x2)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x4)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, -58000, 2000, -37000, 0)
    OP_52(0x9, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0xE, 0x8)
    SetChrFlags(0xF, 0x8)
    SetChrFlags(0x10, 0x8)
    SetChrFlags(0x11, 0x8)
    SetChrFlags(0x12, 0x8)
    SetChrFlags(0x13, 0x8)
    SetChrFlags(0x14, 0x8)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x8)
    OP_11(0xD0, 0xD0, 0xFF, 0x1E, 0xC8, 0x0)
    Sound(979, 2, 40, 0)
    FadeToBright(1000, 0)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_158B")
    OP_68(-62000, 3000, -15000, 0)
    MoveCamera(38, 15, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(40380, 0)
    OP_68(-53000, 4000, -15000, 2500)
    MoveCamera(38, 11, 0, 2500)
    OP_6E(600, 2500)
    SetCameraDistance(23940, 2500)
    BeginChrThread(0xC, 0, 0, 8)
    BeginChrThread(0xB, 0, 0, 9)
    OP_6F(0x79)
    Sleep(500)
    OP_68(-57750, 5600, -5920, 700)
    MoveCamera(342, 9, 0, 700)
    OP_6E(600, 700)
    SetCameraDistance(26560, 700)
    OP_6F(0x79)
    WaitChrThread(0xB, 0)
    OP_68(-58600, 5800, -6520, 0)
    MoveCamera(315, 33, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(23030, 0)
    Fade(500)
    BeginChrThread(0xB, 0, 0, 14)
    Sleep(2500)
    OP_0D()
    EndChrThread(0xB, 0x0)
    BeginChrThread(0xB, 0, 0, 15)
    OP_68(-54000, 1000, -14000, 0)
    MoveCamera(5, 7, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(34750, 0)
    Fade(500)
    OP_68(-54000, 900, -14000, 6000)
    MoveCamera(5, 6, 0, 6000)
    OP_6E(600, 6000)
    SetCameraDistance(32750, 6000)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#00807F#12P*pant pant*... What a\x01",
            "monster!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#00901F#6PIt's being supplied with\x01",
            "infinite energy from the\x01",
            "Sept-Terrion!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#03301F#6PHe won't lose... Pater-\x01",
            "Mater won't lose to the\x01",
            "likes of you!\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0xA, 1, 0, 63)
    WaitChrThread(0xA, 1)
    Sleep(300)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0xA,
        (
            "#03307F#6P#4SWe won't lose either!\x01",
            "Renne, Estelle and\x01",
            "Joshua will never lose!!\x02",
        )
    )

    CloseMessageWindow()
    EndChrThread(0xB, 0x0)
    OP_68(-50160, 1900, 6630, 0)
    MoveCamera(13, 8, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(44520, 0)
    Fade(500)
    BlurSwitch(0x12C, 0x66FFFFFF, 0x0, 0x1, 0xA)
    EndChrThread(0xB, 0x0)
    BeginChrThread(0xB, 0, 0, 16)
    BeginChrThread(0xC, 0, 0, 17)
    Sleep(700)
    OP_68(-52350, 5000, -15600, 2800)
    MoveCamera(10, 4, 0, 2800)
    OP_6E(600, 2800)
    SetCameraDistance(18900, 2800)
    Sleep(1000)
    WaitChrThread(0xB, 0)
    Sound(955, 0, 100, 0)
    BeginChrThread(0xB, 0, 0, 18)
    OP_0D()
    OP_6F(0x79)
    CancelBlur(1000)
    OP_68(-52350, 4800, -15600, 1500)
    MoveCamera(10, -3, 0, 1500)
    OP_6E(600, 1500)
    SetCameraDistance(28620, 1500)
    Sleep(1400)

    ChrTalk(
        0xA,
        "#03305F#6P#N#8AAh!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#00813F#12P#6AGuh!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#00907F#6P#6AOhhh!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1614")

    label("loc_158B")

    OP_68(-52350, 4800, -15600, 0)
    MoveCamera(10, -3, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(28620, 0)
    SetChrPos(0xD, -59300, 0, -5200, 0)
    SetChrPos(0xC, -59300, 0, -5200, 0)
    OP_93(0xC, 0x96, 0x0)
    OP_70(0x0, 0x172)
    SetChrPos(0xB, -51790, 0, -13210, 0)
    OP_93(0xB, 0xBE, 0x0)
    BeginChrThread(0xB, 0, 0, 18)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x212, 0x23A, 0x1, 0x20)

    label("loc_1614")

    EndChrThread(0xB, 0x0)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1DEE")
    Fade(500)
    OP_68(-55340, 2300, -33310, 0)
    MoveCamera(9, 16, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15200, 0)
    BeginChrThread(0xB, 0, 0, 20)
    OP_0D()
    BeginChrThread(0x8, 0, 0, 21)
    BeginChrThread(0x9, 0, 0, 26)
    Sleep(1300)
    OP_68(-58120, 2900, -30280, 2200)
    MoveCamera(31, 14, 0, 2200)
    OP_6E(600, 2200)
    SetCameraDistance(21710, 2200)
    Sleep(3100)
    StopSound(579, 500, 50)
    SetChrFlags(0xD, 0x8)
    SetChrFlags(0xC, 0x1)
    BeginChrThread(0xC, 0, 0, 27)
    Sleep(100)
    OP_68(-52100, 1900, -4660, 2000)
    MoveCamera(24, 18, 0, 2000)
    OP_6E(600, 2000)
    SetCameraDistance(29090, 2000)
    Sleep(1000)
    EndChrThread(0xB, 0x0)
    BeginChrThread(0xB, 1, 0, 32)
    OP_6F(0x79)
    Sleep(900)
    OP_68(-54160, 4300, -12890, 2000)
    MoveCamera(18, 25, 0, 2000)
    OP_6E(600, 2000)
    SetCameraDistance(22290, 2000)
    WaitChrThread(0xB, 1)
    OP_6F(0x79)
    WaitChrThread(0xC, 0)
    Fade(500)
    OP_68(-53020, 6100, -12900, 0)
    MoveCamera(29, 0, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(11160, 0)
    OP_0D()
    BeginChrThread(0xC, 0, 0, 30)
    Sleep(150)
    Sound(833, 0, 100, 0)
    Sound(880, 0, 100, 0)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, -53870, 3600, -12640, 286, 90, 0, 1000, 1400, 1000, 0xFF, 0, 0, 0, 0)
    BeginChrThread(0xB, 0, 0, 31)
    Sleep(700)
    BeginChrThread(0xC, 0, 0, 30)
    Sleep(150)
    Sound(833, 0, 100, 0)
    Sound(880, 0, 100, 0)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, -53490, 3600, -12980, 283, 90, 0, 1000, 1400, 1000, 0xFF, 0, 0, 0, 0)
    BeginChrThread(0xB, 0, 0, 31)
    ClearMapObjFlags(0x1, 0x20)
    Sleep(700)
    Sound(655, 0, 50, 0)
    OP_87(0x8, 0xFF, 0x1, "Null_eyes(76)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    Sleep(1000)
    OP_68(-54250, 4900, -15110, 0)
    MoveCamera(40, 16, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17850, 0)
    Fade(500)
    Sound(905, 0, 100, 0)
    OP_74(0x1, 0x1E)
    OP_74(0x0, 0x1E)
    OP_71(0x1, 0x316, 0x334, 0x1, 0x0)
    OP_79(0x1)
    Sound(951, 0, 100, 0)
    OP_0D()
    Sound(833, 0, 100, 0)
    Sound(876, 0, 100, 0)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, -52750, 5300, -12960, 288, 90, 0, 1050, 2500, 1050, 0xFF, 0, 0, 0, 0)
    BlurSwitch(0x12C, 0x77FFFFFF, 0x0, 0x1, 0xA)
    BeginChrThread(0xC, 1, 0, 33)

    def lambda_1908():
        OP_93(0xFE, 0x109, 0x64)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_1908)

    def lambda_1915():
        OP_93(0xFE, 0xE1, 0xC8)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_1915)
    Sound(905, 0, 100, 0)
    OP_74(0x0, 0xF)
    OP_71(0x0, 0x28B, 0x294, 0x1, 0x0)
    WaitChrThread(0xB, 2)
    WaitChrThread(0xC, 2)
    CancelBlur(500)
    BeginChrThread(0xC, 3, 0, 34)
    OP_74(0x1, 0xF)
    OP_71(0x1, 0x334, 0x348, 0x1, 0x0)
    OP_79(0x1)
    Sound(1019, 0, 100, 0)
    OP_74(0x1, 0xF)
    OP_74(0x1, 0xF)
    OP_71(0x1, 0x348, 0x366, 0x1, 0x0)
    OP_71(0x0, 0x294, 0x2B2, 0x1, 0x0)
    Sleep(400)
    OP_68(-55920, 4900, -15970, 1000)
    MoveCamera(21, 27, 0, 1000)
    OP_6E(600, 1000)
    SetCameraDistance(17850, 1000)
    Sleep(700)
    Sound(200, 0, 100, 0)
    Sound(902, 0, 100, 0)
    OP_82(0x32, 0x32, 0xBB8, 0x4B0)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, -57750, 150, -14660, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrPos(0xD, -58930, 150, -15120, 0)
    ClearChrFlags(0xD, 0x8)
    OP_79(0x1)
    OP_79(0x0)
    OP_6F(0x79)
    Fade(500)
    SetChrChipByIndex(0x9, 0x26)
    SetChrSubChip(0x9, 0x0)
    SetChrPos(0x9, -65200, 4000, -40600, 30)
    SetChrChipByIndex(0x8, 0x24)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, -66000, 4000, -39000, 30)
    SetChrChipByIndex(0xA, 0x22)
    SetChrSubChip(0xA, 0x0)
    SetChrPos(0xA, -65750, 4000, -40000, 30)
    OP_68(-62830, 7700, -33780, 0)
    MoveCamera(26, 8, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(10200, 0)
    OP_68(-62830, 4700, -33780, 2500)
    MoveCamera(25, 8, 0, 2500)
    OP_6E(600, 2500)
    SetCameraDistance(16610, 2500)
    OP_0D()
    Sleep(2000)

    ChrTalk(
        0x8,
        "#00807F#6PAah...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#03311F#N#6PPater-Mater!?\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0x12C, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0xA,
        "#03307F#6P#5STake thiiis!\x02",
    )

    CloseMessageWindow()
    OP_68(-62830, 3300, -33780, 700)
    MoveCamera(25, 14, 0, 700)
    OP_6E(600, 700)
    SetCameraDistance(16610, 700)
    Sleep(300)
    BeginChrThread(0xA, 0, 0, 37)
    Sleep(300)
    OP_68(-62700, 2700, -34780, 2500)
    MoveCamera(29, 26, 0, 2500)
    OP_6E(600, 2500)
    SetCameraDistance(15110, 2500)
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(2400)

    ChrTalk(
        0x8,
        "#00813F#6PRenne, no!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#00907F#12PIf you go alone...!\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0xB, 1, 0, 38)
    OP_68(-54690, 2900, -20410, 0)
    MoveCamera(28, -2, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(21330, 0)
    Fade(500)
    OP_68(-54690, 2900, -20410, 2000)
    MoveCamera(28, -5, 0, 2000)
    OP_6E(600, 2000)
    SetCameraDistance(19250, 2000)
    OP_0D()
    BlurSwitch(0x2BC, 0x66FFFFFF, 0x0, 0x1, 0xA)
    WaitChrThread(0xB, 0)
    OP_A1(0xA, 0x0, 0x1, 0x0)
    EndChrThread(0xA, 0x3)
    BeginChrThread(0xA, 1, 0, 40)
    BeginChrThread(0xB, 0, 0, 18)
    Sleep(100)
    OP_68(-49300, 2600, -22900, 2200)
    MoveCamera(347, -8, 0, 2200)
    OP_6E(600, 2200)
    SetCameraDistance(14120, 2200)
    Sleep(800)
    CancelBlur(500)
    Sleep(1000)

    ChrTalk(
        0xA,
        "#03310F#11P#8AUgh!\x02",
    )

    WaitChrThread(0xA, 1)
    CloseMessageWindow()
    EndChrThread(0xB, 0x0)
    StopSound(579, 500, 50)
    BeginChrThread(0xB, 1, 0, 41)
    OP_68(-59770, 3900, -29280, 0)
    MoveCamera(27, 11, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(24150, 0)
    Fade(500)
    BeginChrThread(0xB, 0, 0, 42)
    OP_0D()
    BlurSwitch(0x12C, 0x66FFFFFF, 0x0, 0x1, 0xA)
    BeginChrThread(0x8, 0, 0, 43)
    BeginChrThread(0x9, 0, 0, 44)
    Sleep(900)
    OP_68(-62260, 1300, -36400, 800)
    MoveCamera(73, 22, 0, 800)
    OP_6E(600, 800)
    SetCameraDistance(24780, 800)
    Sleep(600)
    CancelBlur(500)

    ChrTalk(
        0x8,
        "#00806F#11PEeeek!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#00907F#12PDamn!\x02",
    )

    CloseMessageWindow()
    EndChrThread(0xB, 0x0)
    EndChrThread(0xB, 0x1)
    SetChrPos(0xB, -59000, 0, -19000, 0)
    OP_93(0xB, 0xD0, 0x0)
    Jump("loc_1EBB")

    label("loc_1DEE")

    OP_68(-62260, 1300, -36400, 0)
    MoveCamera(73, 22, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(24780, 0)
    SetChrPos(0xC, -55540, 150, -11980, 0)
    OP_93(0xC, 0xE1, 0x0)
    SetChrPos(0xB, -59000, 0, -19000, 0)
    OP_93(0xB, 0xD0, 0x0)
    SetChrPos(0xD, -58930, 150, -15120, 0)
    ClearChrFlags(0xD, 0x8)
    OP_70(0x0, 0x2B2)
    SetChrChipByIndex(0x9, 0x2C)
    SetChrSubChip(0x9, 0x1)
    SetChrPos(0x9, -55820, 2000, -42120, 120)
    SetChrChipByIndex(0x8, 0x2B)
    SetChrSubChip(0x8, 0x1)
    SetChrPos(0x8, -74450, 2000, -39430, 300)
    SetChrChipByIndex(0xA, 0x2D)
    SetChrSubChip(0xA, 0x3)
    SetChrPos(0xA, -48000, 0, -25500, 300)
    ClearChrFlags(0xA, 0x1000)
    ClearChrFlags(0xA, 0x2)

    label("loc_1EBB")

    TurnDirection(0x9, 0xA, 0)
    TurnDirection(0x8, 0xA, 0)
    OP_74(0x0, 0x1E)
    OP_74(0x1, 0x1E)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2163")
    TurnDirection(0xA, 0xB, 0)
    OP_70(0x1, 0x2B2)
    Fade(500)
    OP_68(-52720, 3400, -21490, 0)
    MoveCamera(54, 30, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(25630, 0)
    OP_68(-48000, 800, -25500, 3000)
    MoveCamera(121, 41, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(35000, 1200)
    BeginChrThread(0xB, 0, 0, 46)
    Sleep(1800)
    SetChrFlags(0xA, 0x800)
    SetCameraDistance(22300, 1200)
    OP_0D()
    WaitChrThread(0xB, 0)
    BeginChrThread(0xB, 0, 0, 47)
    OP_0D()
    WaitChrThread(0xB, 0)

    ChrTalk(
        0xA,
        "#03305F#5P#30W...Ah...\x02",
    )

    CloseMessageWindow()
    OP_68(-51660, 2400, -24100, 0)
    MoveCamera(333, 13, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(19830, 0)
    SetChrChipByIndex(0xA, 0x2D)
    SetChrFlags(0xA, 0x1000)
    SetChrFlags(0xA, 0x2)
    SetChrSubChip(0xA, 0x16)
    Fade(500)
    OP_0D()

    ChrTalk(
        0x9,
        "#00907F#6P#NNo good, I'm too far!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0xC, 0, 0, 50)
    BeginChrThread(0xB, 0, 0, 51)
    BlurSwitch(0x3E8, 0x88FFFFFF, 0x0, 0x1, 0xA)

    ChrTalk(
        0x8,
        "#00813F#6P#N#4S#12AReeeeenne!!!\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_68(-57920, 2100, -15450, 800)
    MoveCamera(331, 15, 0, 800)
    OP_6E(600, 800)
    SetCameraDistance(24100, 800)
    WaitChrThread(0xC, 0)
    WaitChrThread(0xB, 0)
    CancelBlur(0)
    FadeToDark(2500, 16777215, -1)
    OP_0D()
    ClearChrFlags(0xA, 0x800)
    Call(0, 45)
    OP_68(-56280, 3800, -20400, 0)
    MoveCamera(269, 33, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(22880, 0)
    OP_68(-53780, 4200, -21540, 2700)
    MoveCamera(170, 39, 0, 2700)
    OP_6E(600, 2700)
    SetCameraDistance(22880, 2700)
    SetChrPos(0xA, -48000, 100, -25500, 300)
    SetChrChipByIndex(0xA, 0x2D)
    SetChrFlags(0xA, 0x1000)
    SetChrFlags(0xA, 0x2)
    SetChrSubChip(0xA, 0x9)
    OP_70(0x0, 0x3C)
    BlurSwitch(0x0, 0x77FFFFFF, 0x0, 0x1, 0xA)
    FadeToBright(2000, 16777215)
    OP_0D()
    CancelBlur(1500)

    ChrTalk(
        0xA,
        "#03310F#6P#13AEeeek!\x02",
    )

    Sleep(2000)
    CloseMessageWindow()
    StopSound(931, 1000, 50)
    StopEffect(0x2, 0x2)
    StopEffect(0x3, 0x2)
    EndChrThread(0xC, 0xFF)
    EndChrThread(0xB, 0xFF)
    Jump("loc_21FF")

    label("loc_2163")

    Call(0, 45)
    OP_68(-53780, 4900, -21540, 0)
    MoveCamera(159, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(22880, 0)
    SetChrPos(0xC, -56570, 200, -20210, 0)
    OP_93(0xC, 0x128, 0x0)
    SetChrPos(0xB, -59000, 0, -19000, 0)
    OP_93(0xB, 0x78, 0x0)
    SetChrPos(0xA, -48000, 100, -25500, 300)
    OP_74(0x1, 0xF)
    OP_70(0x1, 0x3E8)
    OP_74(0x1, 0xF)
    OP_70(0x0, 0x28A)
    SetChrChipByIndex(0xA, 0x2D)
    SetChrFlags(0xA, 0x1000)
    SetChrFlags(0xA, 0x2)
    SetChrSubChip(0xA, 0x9)
    EndChrThread(0xC, 0xFF)
    EndChrThread(0xB, 0xFF)

    label("loc_21FF")

    BeginChrThread(0xC, 0, 0, 56)
    BeginChrThread(0xB, 0, 0, 58)
    BeginChrThread(0xB, 1, 0, 59)
    BeginChrThread(0x17, 1, 0, 60)
    Sound(904, 2, 80, 0)
    WaitChrThread(0xC, 0)
    OP_68(-46270, 400, -20250, 0)
    MoveCamera(69, 21, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(25140, 0)
    Fade(500)
    OP_70(0x0, 0x276)
    SetChrChipByIndex(0xA, 0x2D)
    SetChrFlags(0xA, 0x2)
    SetChrFlags(0xA, 0x1000)
    SetChrSubChip(0xA, 0xB)
    OP_0D()
    Call(0, 5)
    Sound(903, 0, 100, 0)
    Sleep(1000)
    WaitChrThread(0xC, 0)
    WaitChrThread(0xB, 0)
    Sleep(500)
    Call(0, 53)
    BeginChrThread(0xC, 3, 0, 70)
    Fade(500)
    Sleep(500)
    OP_63(0xA, 0xFFFFFF06, 1150, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xA,
        "#03311F#12PHuh─\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Call(0, 52)
    Call(0, 54)
    Fade(500)
    Sleep(2500)
    BlurSwitch(0x0, 0x55FFFFFF, 0x0, 0x1, 0xA)
    OP_68(-48240, 400, -23830, 0)
    MoveCamera(77, 31, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18880, 0)
    Fade(500)
    BeginChrThread(0xA, 1, 0, 65)
    WaitChrThread(0xA, 1)

    ChrTalk(
        0xA,
        (
            "#03316F#12P#30WPater-Mater... W-What\x01",
            "are you saying...?\x02\x03",
            "#03307F#30W...No... You can't!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(1000)
    EndChrThread(0xC, 0x3)
    Fade(500)
    OP_68(-64920, 3800, -1760, 0)
    MoveCamera(357, 16, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(35630, 0)
    SetChrChipByIndex(0xA, 0x2D)
    SetChrFlags(0xA, 0x2)
    SetChrFlags(0xA, 0x1000)
    SetChrSubChip(0xA, 0x16)
    SetChrFlags(0xC, 0x4)
    BeginChrThread(0xC, 3, 0, 71)
    OP_68(-53250, -1300, -4700, 0)
    MoveCamera(357, 12, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(40530, 0)
    OP_68(-53250, 7100, -4700, 4000)
    MoveCamera(346, 20, 0, 4000)
    OP_6E(600, 4000)
    SetCameraDistance(45990, 4000)
    Sound(994, 0, 100, 0)
    BeginChrThread(0xB, 0, 0, 61)
    BeginChrThread(0xC, 0, 0, 61)
    OP_0D()
    WaitChrThread(0xB, 0)
    WaitChrThread(0xC, 0)
    EndChrThread(0x17, 0x1)
    StopSound(904, 2000, 70)
    OP_68(-56790, 17500, -21340, 0)
    MoveCamera(55, 59, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(41970, 0)
    SetChrPos(0xC, -56880, 9000, -17240, 0)
    OP_93(0xC, 0x5A, 0x0)
    SetChrPos(0xB, -54090, 9000, -17070, 0)
    OP_93(0xB, 0x10A, 0x0)
    OP_11(0xD0, 0xD0, 0xFF, 0x32, 0x258, 0x0)
    Fade(500)
    Sound(994, 0, 100, 0)
    OP_68(-56790, 19500, -21340, 5000)
    MoveCamera(74, 67, 0, 5000)
    OP_6E(600, 5000)
    SetCameraDistance(59280, 5000)
    BeginChrThread(0xB, 0, 0, 62)
    BeginChrThread(0xC, 0, 0, 62)
    OP_0D()
    Sleep(500)
    BlurSwitch(0x7D0, 0x77FFFFFF, 0x0, 0x1, 0xA)
    OP_82(0xC8, 0x0, 0xBB8, 0x320)

    ChrTalk(
        0xA,
        "#03310F#12P#4S#20ANOOOOOOOO!!\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0xA, 1, 0, 66)
    FadeToDark(2000, 16777215, -1)
    OP_0D()
    Sleep(1000)
    StopSound(993, 3000, 90)
    Sound(200, 0, 70, 0)
    Sound(1043, 0, 100, 0)
    Sleep(3000)
    OP_68(-13920, 1200, 76150, 0)
    MoveCamera(10, 4, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18900, 0)
    FadeToBright(1000, 16777215)
    OP_0D()
    StopBGM(0x1770)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_24(0x354)
    OP_24(0x3D3)
    OP_24(0x243)
    OP_24(0x3A3)
    OP_24(0x388)
    OP_24(0x3E4)
    OP_24(0x3E1)
    SetScenarioFlags(0x22, 1)
    NewScene("c1510", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_6_E48 end

    def Function_7_25DC(): pass

    label("Function_7_25DC")

    OP_74(0x0, 0x1E)
    OP_4C(0xFE, 0x1)
    OP_71(0x0, 0x3C, 0x44, 0x1, 0x0)
    OP_79(0x0)
    OP_82(0x32, 0x32, 0xBB8, 0xC8)
    OP_4B(0xFE, 0x1)
    Sound(902, 0, 70, 0)
    OP_71(0x0, 0x45, 0x49, 0x1, 0x0)
    OP_79(0x0)
    OP_4C(0xFE, 0x1)
    OP_71(0x0, 0x4A, 0x58, 0x1, 0x0)
    OP_79(0x0)
    OP_82(0x32, 0x32, 0xBB8, 0xC8)
    OP_4B(0xFE, 0x1)
    Sound(902, 0, 70, 0)
    OP_71(0x0, 0x59, 0x5D, 0x1, 0x0)
    OP_79(0x0)
    OP_4C(0xFE, 0x1)
    OP_71(0x0, 0x5E, 0x64, 0x1, 0x0)
    OP_79(0x0)
    Return()

    # Function_7_25DC end

    def Function_8_266E(): pass

    label("Function_8_266E")

    OP_74(0x0, 0x1E)

    def lambda_2677():
        OP_9B(0x1, 0xFE, 0x0, 0x2710, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2677)

    label("loc_2687")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_269A")
    Call(0, 7)
    Jump("loc_2687")

    label("loc_269A")

    Return()

    # Function_8_266E end

    def Function_9_269B(): pass

    label("Function_9_269B")

    ClearMapObjFlags(0x1, 0x20)
    OP_79(0x1)
    Sound(905, 0, 100, 0)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x1D6, 0x1ED, 0x1, 0x0)
    OP_79(0x1)
    BlurSwitch(0x12C, 0x77FFFFFF, 0x0, 0x1, 0xA)
    Sound(902, 0, 100, 0)
    Sound(1042, 0, 100, 0)
    Sound(196, 0, 100, 0)
    OP_82(0xC8, 0x0, 0xBB8, 0x3E8)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, -54760, 5200, -17310, 149, 90, 0, 450, 850, 450, 0xFF, 0, 0, 0, 0)
    OP_FE(0x0)
    EndChrThread(0xC, 0x0)
    BeginChrThread(0xC, 0, 0, 10)
    OP_71(0x1, 0x1ED, 0x1F4, 0x1, 0x0)
    OP_79(0x1)
    CancelBlur(500)
    OP_71(0x1, 0x1F7, 0x1FE, 0x1, 0x0)
    OP_79(0x1)

    def lambda_2757():
        OP_93(0xFE, 0x141, 0x64)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2757)
    OP_71(0x1, 0x1AE, 0x1D6, 0x1, 0x0)
    OP_79(0x1)
    Sound(1019, 0, 100, 0)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x24E, 0x276, 0x1, 0x0)
    OP_9B(0x1, 0xFE, 0x0, 0xFA0, 0xFA0, 0x1)
    Return()

    # Function_9_269B end

    def Function_10_2794(): pass

    label("Function_10_2794")

    SetChrFlags(0xFE, 0x4)

    def lambda_279E():
        OP_93(0xFE, 0x96, 0x64)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_279E)
    OP_9D(0xFE, 0xFFFF185C, 0xF0A, 0xFFFFEBB0, 0xF3C, 0x3E8)
    SetChrPos(0xD, -59300, 0, -5200, 0)
    ClearChrFlags(0xFE, 0x1)
    ClearChrFlags(0xD, 0x8)
    OP_82(0x64, 0x64, 0xBB8, 0x1F4)
    Sound(833, 0, 100, 0)
    Sound(978, 0, 100, 0)
    OP_71(0x0, 0x136, 0x140, 0x1, 0x0)
    Sleep(700)
    OP_9C(0xFE, 0x0, 0xFFFFFEA2, 0x0, 0x0, 0x1E)
    Return()

    # Function_10_2794 end

    def Function_11_281C(): pass

    label("Function_11_281C")

    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x276, 0x280, 0x1, 0x0)
    Sleep(200)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, -58950, 7780, -6090, 143, 90, 0, 150, 1250, 150, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, -58950, 7780, -6090, 143, 90, 0, 1000, 2300, 1000, 0xFF, 0, 0, 0, 0)
    Sound(288, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0xC, 0x4, 0, 4200, 800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_82(0x12C, 0x12C, 0xBB8, 0xC8)
    BlurSwitch(0x12C, 0x77FFFFFF, 0x0, 0x1, 0xA)
    OP_71(0x0, 0x136, 0x140, 0x1, 0x0)
    OP_79(0x1)
    CancelBlur(500)
    Return()

    # Function_11_281C end

    def Function_12_290C(): pass

    label("Function_12_290C")

    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x276, 0x280, 0x1, 0x0)
    Sleep(200)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, -58950, 7780, -6090, 143, 90, 0, 150, 1250, 150, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, -58950, 7780, -6090, 143, 90, 0, 750, 1800, 750, 0xFF, 0, 0, 0, 0)
    Sound(288, 0, 60, 0)
    PlayEffect(0x0, 0xFF, 0xC, 0x4, 0, 4200, 800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_82(0x64, 0x64, 0xBB8, 0xC8)
    OP_71(0x0, 0x136, 0x140, 0x1, 0x0)
    OP_79(0x1)
    Return()

    # Function_12_290C end

    def Function_13_29EB(): pass

    label("Function_13_29EB")

    OP_74(0x1, 0x3C)
    OP_71(0x1, 0x280, 0x276, 0x1, 0x0)
    OP_79(0x1)
    Return()

    # Function_13_29EB end

    def Function_14_29FF(): pass

    label("Function_14_29FF")

    OP_93(0xFE, 0x13A, 0x0)
    OP_79(0x1)

    label("loc_2A09")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2A1C")
    Call(0, 11)
    Jump("loc_2A09")

    label("loc_2A1C")

    Return()

    # Function_14_29FF end

    def Function_15_2A1D(): pass

    label("Function_15_2A1D")

    Call(0, 12)
    Call(0, 13)
    Call(0, 12)
    Call(0, 13)
    Call(0, 12)
    Call(0, 13)
    Call(0, 12)
    Call(0, 13)

    label("loc_2A35")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2A4E")
    Call(0, 12)
    Sleep(800)
    Call(0, 13)
    Jump("loc_2A35")

    label("loc_2A4E")

    Return()

    # Function_15_2A1D end

    def Function_16_2A4F(): pass

    label("Function_16_2A4F")

    Call(0, 11)
    Sleep(800)
    Call(0, 13)
    Sleep(500)
    Sound(905, 0, 100, 0)
    OP_74(0x1, 0xF)
    OP_71(0x1, 0x28A, 0x2B2, 0x1, 0x0)
    Sleep(1000)
    Sound(1019, 0, 100, 0)
    OP_79(0x1)
    BeginChrThread(0xFE, 3, 0, 67)
    TurnDirection(0xFE, 0xA, 75)
    Return()

    # Function_16_2A4F end

    def Function_17_2A8B(): pass

    label("Function_17_2A8B")

    Sleep(1500)
    OP_9C(0xFE, 0x0, 0xFFFFFF06, 0x0, 0x32, 0x1F4)
    Sound(996, 2, 40, 0)
    Sleep(500)
    OP_9C(0xFE, 0x0, 0xFFFFF34E, 0x0, 0x32, 0x3E8)
    OP_24(0x3E4)
    Sound(902, 0, 100, 0)
    Sound(833, 0, 100, 0)
    OP_82(0x32, 0x32, 0xBB8, 0xC8)
    OP_71(0x0, 0x14A, 0x172, 0x1, 0x0)
    Return()

    # Function_17_2A8B end

    def Function_18_2AF2(): pass

    label("Function_18_2AF2")

    Sleep(500)
    Sound(622, 0, 70, 0)
    Sound(869, 0, 60, 0)
    Call(0, 19)
    Sleep(600)
    Sound(622, 0, 70, 0)
    Sound(869, 0, 60, 0)
    Call(0, 19)
    Sleep(600)
    Sound(622, 0, 70, 0)
    Sound(869, 0, 60, 0)
    Call(0, 19)
    Sleep(600)
    Return()

    # Function_18_2AF2 end

    def Function_19_2B2C(): pass

    label("Function_19_2B2C")

    PlayEffect(0x5, 0xFF, 0xB, 0x4, -1300, 8000, -2400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x5, 0xFF, 0xB, 0x4, 1300, 8000, -2400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    PlayEffect(0x5, 0xFF, 0xB, 0x4, -1500, 8000, -2600, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x5, 0xFF, 0xB, 0x4, 1500, 8000, -2600, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    PlayEffect(0x5, 0xFF, 0xB, 0x4, -1700, 8000, -2800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x5, 0xFF, 0xB, 0x4, 1700, 8000, -2800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    PlayEffect(0x5, 0xFF, 0xB, 0x4, -1900, 8000, -3000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x5, 0xFF, 0xB, 0x4, 1900, 8000, -3000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    Return()

    # Function_19_2B2C end

    def Function_20_2CF1(): pass

    label("Function_20_2CF1")

    Sleep(300)
    SetChrPos(0xE, -55320, 3500, -27250, 0)

    label("loc_2D05")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2FD3")
    SetChrPos(0xF, -50140, 100, -27050, 0)
    PlayEffect(0x6, 0xFF, 0xF, 0x0, 0, 0, 0, 105, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    SetChrPos(0x10, -61470, 100, -25970, 0)
    PlayEffect(0x6, 0xFF, 0x10, 0x0, 0, 0, 0, 105, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    Sound(196, 0, 80, 0)
    Sleep(200)
    SetChrPos(0xF, -51220, 2100, -37310, 0)
    PlayEffect(0x6, 0xFF, 0xF, 0x0, 0, 0, 0, 105, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    SetChrPos(0x10, -62330, 2100, -35550, 0)
    PlayEffect(0x6, 0xFF, 0x10, 0x0, 0, 0, 0, 105, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    Sleep(350)
    SetChrPos(0x12, -49830, 2100, -44340, 0)
    Sound(200, 0, 80, 0)
    PlayEffect(0x6, 0xFF, 0x12, 0x0, 0, 0, 0, 105, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    SetChrPos(0x13, -57520, 2100, -45280, 0)
    PlayEffect(0x6, 0xFF, 0x13, 0x0, 0, 0, 0, 105, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    Sleep(300)
    SetChrPos(0x11, -54760, 2100, -39810, 0)
    PlayEffect(0x6, 0xFF, 0x11, 0x0, 0, 0, 0, 105, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    Sleep(200)
    SetChrPos(0xF, -51220, 2100, -37310, 0)
    PlayEffect(0x6, 0xFF, 0xF, 0x0, 0, 0, 0, 0, 105, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    SetChrPos(0x10, -62330, 2100, -35550, 0)
    PlayEffect(0x6, 0xFF, 0x10, 0x0, 0, 0, 0, 0, 105, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    Sleep(300)
    Jump("loc_2D05")

    label("loc_2FD3")

    Return()

    # Function_20_2CF1 end

    def Function_21_2FD4(): pass

    label("Function_21_2FD4")

    Sleep(200)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    TurnDirection(0xFE, 0xA, 0)
    OP_95(0xFE, -55500, 2000, -34780, 4000, 0x1)
    OP_9B(0x0, 0xFE, 0x0, 0x64, 0x7D0, 0x1)
    BeginChrThread(0xA, 0, 0, 22)
    Sleep(30)
    OP_93(0xFE, 0xF0, 0x0)
    OP_9B(0x1, 0xFE, 0x0, 0x3E8, 0xBB8, 0x0)
    BeginChrThread(0xFE, 1, 0, 23)
    Sound(809, 0, 100, 0)
    OP_9D(0xFE, 0xFFFF1794, 0x7D0, 0xFFFF699C, 0x15E, 0x3E8)
    Sleep(100)
    BeginChrThread(0xFE, 1, 0, 23)
    Sound(809, 0, 100, 0)
    OP_9D(0xFE, 0xFFFF02E0, 0xFA0, 0xFFFF6488, 0x92E, 0x3E8)
    Sound(326, 0, 60, 0)
    EndChrThread(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_21_2FD4 end

    def Function_22_308A(): pass

    label("Function_22_308A")

    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x22)
    ClearChrFlags(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x1000)
    OP_93(0xFE, 0xF0, 0x0)
    OP_9B(0x1, 0xFE, 0x0, 0x3E8, 0xBB8, 0x0)
    BeginChrThread(0xFE, 1, 0, 23)
    OP_9D(0xFE, 0xFFFF1668, 0x7D0, 0xFFFF6870, 0x15E, 0x3E8)
    Sleep(150)
    BeginChrThread(0xFE, 1, 0, 23)
    OP_9D(0xFE, 0xFFFF0150, 0xFA0, 0xFFFF62F8, 0x92E, 0x3E8)
    Sleep(300)
    TurnDirection(0xFE, 0xC, 500)
    Return()

    # Function_22_308A end

    def Function_23_30FC(): pass

    label("Function_23_30FC")

    SetChrSubChip(0xFE, 0x0)
    Sleep(50)
    SetChrSubChip(0xFE, 0x1)
    Sleep(90)
    SetChrSubChip(0xFE, 0x2)
    Sleep(180)
    SetChrSubChip(0xFE, 0x3)
    Sleep(90)
    SetChrSubChip(0xFE, 0x4)
    Sleep(50)
    Return()

    # Function_23_30FC end

    def Function_24_3120(): pass

    label("Function_24_3120")

    PlayEffect(0x6, 0xFF, 0xE, 0x0, 0, 0, 0, 105, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    OP_4B(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x2E)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x2)
    Sleep(200)
    Sound(308, 0, 100, 0)
    Sound(533, 0, 60, 0)
    Sound(859, 0, 50, 0)
    PlayEffect(0x9, 0xFF, 0xFE, 0x4, 0, 500, 0, 0, 1, 0, 1000, 1000, 1000, 0xE, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x3)
    Sleep(350)
    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x1000)
    OP_4C(0xFE, 0x0)
    Return()

    # Function_24_3120 end

    def Function_25_31DA(): pass

    label("Function_25_31DA")

    PlayEffect(0x6, 0xFF, 0xE, 0x0, 0, 0, 0, 105, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    OP_4B(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x2E)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x0)
    Sleep(200)
    Sound(308, 0, 100, 0)
    Sound(533, 0, 60, 0)
    Sound(859, 0, 50, 0)
    PlayEffect(0x9, 0xFF, 0xFE, 0x4, 0, 500, 0, 0, 1, 0, 1000, 1000, 1000, 0xE, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x1)
    Sleep(350)
    Sound(844, 0, 70, 0)
    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x1000)
    OP_4C(0xFE, 0x0)
    Return()

    # Function_25_31DA end

    def Function_26_329A(): pass

    label("Function_26_329A")

    SetChrChip(0x0, 0xFE, 0x32, 0x12C)
    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x0)
    BeginChrThread(0xFE, 1, 0, 23)
    Sound(250, 0, 60, 0)
    OP_9D(0xFE, 0xFFFF2216, 0x7D0, 0xFFFF7C84, 0x15E, 0x5DC)
    WaitChrThread(0xFE, 1)
    SetChrSubChip(0xFE, 0x0)
    BeginChrThread(0xFE, 2, 0, 24)
    WaitChrThread(0xFE, 2)
    SetChrSubChip(0xFE, 0x0)
    Sleep(300)
    BeginChrThread(0xFE, 2, 0, 24)
    OP_9D(0xFE, 0xFFFF153C, 0x7D0, 0xFFFF6FA0, 0x15E, 0x5DC)
    WaitChrThread(0xFE, 2)
    SetChrSubChip(0xFE, 0x0)
    Sleep(300)
    SetChrPos(0xE, -59010, 4800, -28120, 0)
    TurnDirection(0xFE, 0xB, 500)
    Sleep(200)
    BeginChrThread(0xFE, 2, 0, 25)
    OP_9D(0xFE, 0xFFFF052F, 0xFA0, 0xFFFF6154, 0x92E, 0x4B0)
    Sound(326, 0, 70, 0)
    Sound(540, 0, 60, 0)
    WaitChrThread(0xFE, 2)
    SetChrSubChip(0xFE, 0x0)
    EndChrThread(0xFE, 0x1)
    SetChrChipByIndex(0x9, 0x26)
    TurnDirection(0xFE, 0xB, 500)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_26_329A end

    def Function_27_3372(): pass

    label("Function_27_3372")

    OP_74(0x0, 0xF)
    OP_71(0x0, 0x230, 0x258, 0x1, 0x0)
    OP_79(0x0)
    OP_74(0x0, 0x1E)
    BeginChrThread(0xFE, 1, 0, 29)
    Call(0, 7)
    Call(0, 7)
    Return()

    # Function_27_3372 end

    def Function_28_3396(): pass

    label("Function_28_3396")

    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x262, 0x276, 0x1, 0x0)
    OP_79(0x0)
    OP_71(0x0, 0x276, 0x28A, 0x1, 0x20)
    OP_79(0x0)
    Return()

    # Function_28_3396 end

    def Function_29_33B9(): pass

    label("Function_29_33B9")

    TurnDirection(0xFE, 0xB, 100)
    OP_9B(0x1, 0xFE, 0xF, 0xFA, 0x3E8, 0x0)
    OP_9B(0x1, 0xFE, 0xF, 0xFA, 0x7D0, 0x0)
    OP_9B(0x1, 0xFE, 0xF, 0xFA, 0xFA0, 0x0)
    OP_9B(0x1, 0xFE, 0xF, 0xFA0, 0x1770, 0x0)
    EndChrThread(0xFE, 0x0)
    BeginChrThread(0xFE, 0, 0, 28)
    OP_9D(0xFE, 0xFFFF27F2, 0x3E8, 0xFFFFD1C0, 0x41A, 0x4B0)
    Sound(288, 0, 50, 0)
    Sound(833, 0, 50, 0)
    Sound(1042, 0, 100, 0)
    OP_82(0x0, 0x1E, 0xBB8, 0x12C)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, -53870, 3600, -11890, 288, 90, 0, 1000, 1800, 1000, 0xFF, 0, 0, 0, 0)
    OP_9C(0xFE, 0x0, 0xFFFFFCAE, 0x0, 0x32, 0x2EE)
    EndChrThread(0xFE, 0x0)
    Return()

    # Function_29_33B9 end

    def Function_30_3493(): pass

    label("Function_30_3493")

    OP_9B(0x1, 0xFE, 0x0, 0xC8, 0x7D0, 0x0)
    OP_9B(0x1, 0xFE, 0x0, 0xC8, 0xBB8, 0x0)
    OP_9B(0x1, 0xFE, 0x0, 0x64, 0x3E8, 0x0)
    OP_9B(0x1, 0xFE, 0x0, 0x64, 0x1F4, 0x0)
    Return()

    # Function_30_3493 end

    def Function_31_34D0(): pass

    label("Function_31_34D0")

    OP_9B(0x1, 0xFE, 0x31, 0xFFFFFF38, 0x7D0, 0x0)
    OP_9B(0x1, 0xFE, 0x31, 0xFFFFFF38, 0xBB8, 0x0)
    OP_9B(0x1, 0xFE, 0x31, 0xFFFFFF9C, 0x3E8, 0x0)
    OP_9B(0x1, 0xFE, 0x31, 0xFFFFFF9C, 0x1F4, 0x0)
    Return()

    # Function_31_34D0 end

    def Function_32_350D(): pass

    label("Function_32_350D")

    ClearMapObjFlags(0x1, 0x20)
    OP_79(0x1)
    BeginChrThread(0xFE, 3, 0, 68)
    WaitChrThread(0xFE, 3)
    OP_79(0x1)
    OP_71(0x1, 0x1AE, 0x1D6, 0x1, 0x20)
    OP_93(0xFE, 0x113, 0x4B)
    Return()

    # Function_32_350D end

    def Function_33_3537(): pass

    label("Function_33_3537")

    OP_96(0xFE, 0xFFFF2540, 0x96, 0xFFFFD440, 0x1388, 0x1)
    OP_96(0xFE, 0xFFFF27F2, 0x96, 0xFFFFD1C0, 0x1B58, 0x1)
    Return()

    # Function_33_3537 end

    def Function_34_3560(): pass

    label("Function_34_3560")

    OP_FD(0xD, 0xFE)
    ClearChrFlags(0xD, 0x8)
    SetChrFlags(0xFE, 0x4)
    SetChrPos(0xFE, -55540, 180, -11980, 225)
    Sleep(160)
    SetChrPos(0xFE, -55540, 150, -11980, 225)
    Sleep(160)
    SetChrPos(0xFE, -55540, 180, -11980, 225)
    Sleep(160)
    SetChrPos(0xFE, -55540, 150, -11980, 225)
    Sleep(160)
    SetChrPos(0xFE, -55540, 180, -11980, 225)
    Sleep(160)
    SetChrPos(0xFE, -55540, 150, -11980, 225)
    Sleep(160)
    SetChrPos(0xFE, -55540, 180, -11980, 225)
    Sleep(160)
    SetChrPos(0xFE, -55540, 150, -11980, 225)
    Sleep(160)
    ClearChrFlags(0xFE, 0x4)
    ClearChrFlags(0xD, 0x8)
    Return()

    # Function_34_3560 end

    def Function_35_361A(): pass

    label("Function_35_361A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3633")
    OP_A1(0xFE, 0x5DC, 0x3, 0x0, 0x1, 0x2)
    Jump("Function_35_361A")

    label("loc_3633")

    Return()

    # Function_35_361A end

    def Function_36_3634(): pass

    label("Function_36_3634")

    OP_A1(0xFE, 0x5DC, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Sound(802, 0, 100, 0)
    Return()

    # Function_36_3634 end

    def Function_37_3646(): pass

    label("Function_37_3646")

    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x0)
    Sound(811, 0, 50, 0)

    def lambda_3659():
        OP_9B(0x1, 0xFE, 0x14A, 0x96, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3659)

    def lambda_366E():
        OP_A6(0xFE, 0x1E, 0x1E, 0x12C, 0x5DC)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_366E)
    OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x1388, 0x1)
    Sound(844, 0, 60, 0)
    OP_9D(0xFE, 0xFFFF07F4, 0x7D0, 0xFFFF72FC, 0x28A, 0x5DC)
    Sound(326, 0, 60, 0)
    OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0x1388, 0x1)
    Sound(809, 0, 70, 0)
    OP_9D(0xFE, 0xFFFF15A0, 0x0, 0xFFFF8A9E, 0x15E, 0x5DC)
    Sound(326, 0, 40, 0)
    OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x1388, 0x1)
    Sleep(150)
    SetChrChipByIndex(0xFE, 0x2A)
    SetChrSubChip(0xFE, 0x0)
    Sleep(100)
    Sound(357, 0, 80, 0)
    Sound(852, 2, 100, 0)
    PlayEffect(0x7, 0x0, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    BeginChrThread(0xFE, 3, 0, 35)
    Sleep(1000)
    Return()

    # Function_37_3646 end

    def Function_38_3750(): pass

    label("Function_38_3750")

    BeginChrThread(0xFE, 3, 0, 67)

    def lambda_375B():
        TurnDirection(0xFE, 0xA, 50)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_375B)
    Sleep(500)
    BeginChrThread(0xB, 0, 0, 18)
    Sleep(1200)
    EndChrThread(0xB, 0x0)
    BeginChrThread(0xB, 0, 0, 39)
    WaitChrThread(0xB, 0)
    Return()

    # Function_38_3750 end

    def Function_39_377E(): pass

    label("Function_39_377E")

    Sleep(300)
    SetChrPos(0xE, -60950, 1500, -27780, 0)
    SetChrPos(0xF, -59690, 100, -21630, 0)
    PlayEffect(0x6, 0xFF, 0xF, 0x0, 0, 0, 0, 210, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    SetChrPos(0x10, -50140, 100, -27050, 0)
    PlayEffect(0x6, 0xFF, 0x10, 0x0, 0, 0, 0, 210, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    Sound(200, 0, 80, 0)
    Sleep(150)
    SetChrPos(0x11, -63470, 100, -29700, 0)
    PlayEffect(0x6, 0xFF, 0x11, 0x0, 0, 0, 0, 210, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    SetChrPos(0x12, -56730, 100, -33430, 0)
    PlayEffect(0x6, 0xFF, 0x12, 0x0, 0, 0, 0, 210, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    Sleep(200)
    SetChrPos(0xF, -59690, 100, -21630, 0)
    PlayEffect(0x6, 0xFF, 0xF, 0x0, 0, 0, 0, 210, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    SetChrPos(0x10, -50140, 100, -27050, 0)
    PlayEffect(0x6, 0xFF, 0x10, 0x0, 0, 0, 0, 210, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    Sound(196, 0, 80, 0)
    Sleep(150)
    PlayEffect(0x6, 0xFF, 0xE, 0x0, 0, 0, 0, 210, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    Sleep(500)
    Return()

    # Function_39_377E end

    def Function_40_39A7(): pass

    label("Function_40_39A7")

    SetChrChip(0x0, 0xFE, 0x32, 0x12C)
    StopEffect(0x0, 0x2)
    SetChrChipByIndex(0xFE, 0x2D)
    SetChrSubChip(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x1000)
    ClearChrFlags(0xFE, 0x2)
    OP_93(0xFE, 0x12C, 0x0)
    Sound(255, 0, 60, 0)
    Sound(556, 0, 100, 0)
    OP_24(0x354)
    OP_9D(0xFE, 0xFFFF4098, 0x0, 0xFFFF9CC8, 0x92E, 0x1F4)
    Sound(645, 0, 80, 0)
    SetChrChipByIndex(0xFE, 0x2D)
    SetChrSubChip(0xFE, 0x3)
    ClearChrFlags(0xFE, 0x1000)
    ClearChrFlags(0xFE, 0x2)
    OP_9D(0xFE, 0xFFFF4480, 0x0, 0xFFFF9C64, 0xFA, 0x3E8)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Sound(645, 0, 80, 0)
    Sound(514, 0, 100, 0)
    Sleep(300)
    Return()

    # Function_40_39A7 end

    def Function_41_3A38(): pass

    label("Function_41_3A38")

    Sleep(700)
    OP_96(0xFE, 0xFFFF1988, 0x0, 0xFFFFB5C8, 0x7D0, 0x1)
    Return()

    # Function_41_3A38 end

    def Function_42_3A50(): pass

    label("Function_42_3A50")

    SetChrPos(0x11, -53880, 100, -21770, 0)
    Sound(200, 0, 80, 0)
    PlayEffect(0x6, 0xFF, 0x11, 0x0, 0, 0, 0, 210, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    SetChrPos(0x12, -59060, 0, -25560, 0)
    PlayEffect(0x6, 0xFF, 0x12, 0x0, 0, 0, 0, 210, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    SetChrPos(0x13, -57380, 800, -30310, 0)
    PlayEffect(0x6, 0xFF, 0x13, 0x0, 0, 0, 0, 210, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    Sleep(300)
    SetChrPos(0x11, -64760, 4200, -39250, 0)
    Sound(196, 0, 80, 0)
    PlayEffect(0x6, 0xFF, 0x11, 0x0, 0, 0, 0, 210, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    SetChrPos(0xF, -59090, 2000, -34600, 0)
    PlayEffect(0x6, 0xFF, 0xF, 0x0, 0, 0, 0, 210, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    SetChrPos(0x10, -65250, 1300, -30840, 0)
    PlayEffect(0x6, 0xFF, 0x10, 0x0, 0, 0, 0, 210, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    Sleep(300)
    SetChrPos(0x11, -64760, 4200, -39250, 0)
    Sound(200, 0, 80, 0)
    PlayEffect(0x6, 0xFF, 0x11, 0x0, 0, 0, 0, 210, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    SetChrPos(0x12, -64709, 4200, -43100, 0)
    PlayEffect(0x6, 0xFF, 0x12, 0x0, 0, 0, 0, 210, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    SetChrPos(0x13, -68160, 4200, -42540, 0)
    PlayEffect(0x6, 0xFF, 0x13, 0x0, 0, 0, 0, 210, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    Sound(196, 0, 80, 0)
    Sleep(200)
    SetChrPos(0x11, -64760, 4200, -39250, 0)
    PlayEffect(0x6, 0xFF, 0x11, 0x0, 0, 0, 0, 210, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    Sleep(200)
    SetChrPos(0x12, -64709, 4200, -43100, 0)
    PlayEffect(0x6, 0xFF, 0x12, 0x0, 0, 0, 0, 210, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    Sound(200, 0, 80, 0)
    SetChrPos(0x13, -68160, 4200, -42540, 0)
    PlayEffect(0x6, 0xFF, 0x13, 0x0, 0, 0, 0, 210, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    Return()

    # Function_42_3A50 end

    def Function_43_3DFF(): pass

    label("Function_43_3DFF")

    Sleep(600)
    SetChrChip(0x0, 0xFE, 0x32, 0x12C)
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x12C, 0x1F4)
    BeginChrThread(0xFE, 1, 0, 23)
    Sound(255, 0, 70, 0)
    Sound(200, 0, 100, 0)
    OP_9D(0xFE, 0xFFFEDD2E, 0xFA0, 0xFFFF65FA, 0x3E8, 0x5DC)
    Sound(514, 0, 100, 0)
    Sound(645, 0, 80, 0)
    SetChrChipByIndex(0xFE, 0x2B)
    SetChrSubChip(0xFE, 0x1)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Sleep(300)
    Return()

    # Function_43_3DFF end

    def Function_44_3E62(): pass

    label("Function_44_3E62")

    Sleep(500)
    SetChrChip(0x0, 0xFE, 0x32, 0x12C)
    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x78, 0x1F4)
    BeginChrThread(0xFE, 1, 0, 23)
    OP_9D(0xFE, 0xFFFF25F4, 0x7D0, 0xFFFF5B78, 0x3E8, 0x5DC)
    SetChrChipByIndex(0xFE, 0x2C)
    SetChrSubChip(0xFE, 0x1)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Sleep(300)
    Return()

    # Function_44_3E62 end

    def Function_45_3EAD(): pass

    label("Function_45_3EAD")

    SetMapObjFrame(0xFF, "ato00", 0x1, 0x1)
    SetMapObjFrame(0xFF, "ato01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "ato02", 0x1, 0x1)
    SetMapObjFrame(0xFF, "ato03", 0x1, 0x1)
    SetMapObjFrame(0xFF, "atokizu_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "atokumo_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "mae00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "mae01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "mae02", 0x0, 0x1)
    SetMapObjFrame(0xFF, "maewood", 0x0, 0x1)
    SetMapObjFrame(0xFF, "maekusa00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "maekusa01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "maekusa02", 0x0, 0x1)
    SetMapObjFrame(0xFF, "maekage", 0x0, 0x1)
    Return()

    # Function_45_3EAD end

    def Function_46_3F80(): pass

    label("Function_46_3F80")

    Sound(1040, 0, 80, 0)
    OP_70(0x1, 0xF)
    OP_71(0x1, 0x2B2, 0x2DA, 0x0, 0x0)

    def lambda_3F9B():

        label("loc_3F9B")

        TurnDirection(0xFE, 0xA, 25)
        Yield()
        Jump("loc_3F9B")

    QueueWorkItem2(0xFE, 2, lambda_3F9B)
    Sleep(2500)
    Sound(304, 0, 100, 0)
    PlayEffect(0x4, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_79(0x1)
    Return()

    # Function_46_3F80 end

    def Function_47_3FEC(): pass

    label("Function_47_3FEC")

    Sleep(2000)
    BeginChrThread(0xA, 1, 0, 64)
    OP_68(-48000, 0, -25500, 1500)
    MoveCamera(121, 44, 0, 1500)
    OP_6E(600, 1500)
    SetCameraDistance(17100, 1500)
    Sleep(1500)
    BeginChrThread(0x17, 1, 0, 48)
    OP_87(0xA, 0x0, 0x1, "Null_b_cannon_r(67)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x546, 0x546, 0x546, 0x0)
    OP_87(0xA, 0x1, 0x1, "Null_b_cannon_l(68)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x546, 0x546, 0x546, 0x0)
    WaitChrThread(0xA, 1)
    Return()

    # Function_47_3FEC end

    def Function_48_40A9(): pass

    label("Function_48_40A9")

    Sound(983, 0, 60, 0)

    label("loc_40AF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_40C8")
    Sleep(1300)
    Sound(1041, 0, 50, 0)
    Jump("loc_40AF")

    label("loc_40C8")

    Return()

    # Function_48_40A9 end

    def Function_49_40C9(): pass

    label("Function_49_40C9")

    OP_96(0xFE, 0xFFFF3C24, 0x190, 0xFFFFBD8E, 0x2710, 0x1)

    def lambda_40E2():

        label("loc_40E2")

        TurnDirection(0xFE, 0xB, 100)
        Yield()
        Jump("loc_40E2")

    QueueWorkItem2(0xFE, 2, lambda_40E2)
    OP_96(0xFE, 0xFFFF3878, 0xC8, 0xFFFFA38A, 0x2710, 0x1)
    PlayEffect(0x2, 0xFF, 0xC, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(1042, 0, 100, 0)
    Sound(833, 0, 100, 0)
    Sound(951, 0, 100, 0)
    OP_82(0xC8, 0xC8, 0xBB8, 0x3E8)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x3D4, 0x3E8, 0x0, 0x0)
    OP_9D(0xFE, 0xFFFF24E6, 0xC8, 0xFFFFB078, 0x1F4, 0x7D0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x262, 0x276, 0x1, 0x0)
    OP_9B(0x1, 0xFE, 0x0, 0x1F4, 0xBB8, 0x0)
    OP_79(0x0)
    EndChrThread(0xFE, 0x2)
    Return()

    # Function_49_40C9 end

    def Function_50_41AB(): pass

    label("Function_50_41AB")

    Sound(902, 0, 100, 0)
    Sound(905, 0, 100, 0)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, -58260, 150, -14590, 0, 0, 0, 1200, 1500, 1200, 0xFF, 0, 0, 0, 0)
    OP_71(0x0, 0x2B2, 0x294, 0x1, 0x0)
    OP_79(0x0)
    OP_82(0x32, 0x32, 0xBB8, 0xC8)

    def lambda_4213():
        OP_93(0xFE, 0x94, 0x64)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4213)
    OP_74(0x0, 0x3C)
    BeginChrThread(0xFE, 1, 0, 49)
    Call(0, 7)
    Call(0, 7)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_50_41AB end

    def Function_51_4230(): pass

    label("Function_51_4230")

    Sleep(1000)
    OP_87(0xA, 0x2, 0x1, "Null_b_cannon_r(67)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x546, 0x546, 0x546, 0x0)
    OP_87(0xA, 0x3, 0x1, "Null_b_cannon_l(68)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x546, 0x546, 0x546, 0x0)
    Sleep(2000)
    EndChrThread(0x17, 0x1)
    StopEffect(0x0, 0x2)
    StopEffect(0x1, 0x2)
    StopEffect(0x2, 0x2)
    StopEffect(0x3, 0x2)
    Sound(984, 0, 100, 0)
    Sound(931, 2, 60, 0)
    OP_87(0x3, 0x2, 0x1, "Null_b_cannon_r(67)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x546, 0x546, 0x546, 0x0)
    OP_87(0x3, 0x3, 0x1, "Null_b_cannon_l(68)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x546, 0x546, 0x546, 0x0)
    OP_82(0xC8, 0x0, 0xBB8, 0x1F4)
    Return()

    # Function_51_4230 end

    def Function_52_4354(): pass

    label("Function_52_4354")

    StopEffect(0x0, 0x0)
    StopEffect(0x1, 0x0)
    StopEffect(0x2, 0x0)
    StopEffect(0x3, 0x0)
    StopEffect(0x4, 0x0)
    StopEffect(0x5, 0x0)
    StopEffect(0x6, 0x0)
    StopEffect(0x7, 0x0)
    Return()

    # Function_52_4354 end

    def Function_53_436D(): pass

    label("Function_53_436D")

    Sound(993, 2, 80, 0)
    Sound(994, 0, 50, 0)
    StopSound(979, 500, 30)
    OP_87(0x1, 0x0, 0x0, "Null_S_jet_r0(63)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    OP_87(0x1, 0x1, 0x0, "Null_S_jet_r2(64)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    OP_87(0x1, 0x2, 0x0, "Null_S_jet_l0(66)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    OP_87(0x1, 0x3, 0x0, "Null_S_jet_l2(65)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    OP_87(0x0, 0x4, 0x0, "Null_S_jet_r1(61)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    OP_87(0x0, 0x5, 0x0, "Null_S_jet_l1(62)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    OP_87(0x0, 0x6, 0x0, "Null_kata_jet_r(53)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    OP_87(0x0, 0x7, 0x0, "Null_kata_jet_l(54)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    OP_71(0x0, 0x2BC, 0x2E4, 0x1, 0x0)
    Return()

    # Function_53_436D end

    def Function_54_4560(): pass

    label("Function_54_4560")

    OP_25(0x3E1, 0x64)
    Sound(994, 0, 100, 0)
    OP_87(0x1, 0x0, 0x0, "Null_S_jet_r0(63)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0xBB8, 0x1388, 0xBB8, 0x0)
    OP_87(0x1, 0x1, 0x0, "Null_S_jet_r2(64)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0xBB8, 0x1388, 0xBB8, 0x0)
    OP_87(0x1, 0x2, 0x0, "Null_S_jet_l0(66)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0xBB8, 0x1388, 0xBB8, 0x0)
    OP_87(0x1, 0x3, 0x0, "Null_S_jet_l2(65)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0xBB8, 0x1388, 0xBB8, 0x0)
    OP_87(0x0, 0x4, 0x0, "Null_S_jet_r1(61)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0xBB8, 0x1388, 0xBB8, 0x0)
    OP_87(0x0, 0x5, 0x0, "Null_S_jet_l1(62)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0xBB8, 0x1388, 0xBB8, 0x0)
    OP_87(0x0, 0x6, 0x0, "Null_kata_jet_r(53)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0xBB8, 0x1388, 0xBB8, 0x0)
    OP_87(0x0, 0x7, 0x0, "Null_kata_jet_l(54)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0xBB8, 0x1388, 0xBB8, 0x0)
    OP_71(0x0, 0x2BC, 0x2E4, 0x1, 0x0)
    Return()

    # Function_54_4560 end

    def Function_55_474B(): pass

    label("Function_55_474B")

    OP_93(0xFE, 0x5A, 0x20)
    OP_9B(0x1, 0xFE, 0x0, 0x1F4, 0x3E8, 0x1)
    Return()

    # Function_55_474B end

    def Function_56_4762(): pass

    label("Function_56_4762")

    BeginChrThread(0xFE, 1, 0, 55)
    OP_74(0x0, 0xA)
    Call(0, 57)
    Call(0, 57)
    Return()

    # Function_56_4762 end

    def Function_57_4773(): pass

    label("Function_57_4773")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4833")
    OP_4C(0xB, 0x0)
    OP_4C(0xB, 0x1)
    OP_4C(0xFE, 0x1)
    OP_71(0x0, 0x3C, 0x44, 0x1, 0x0)
    OP_79(0x0)
    Sound(902, 0, 70, 0)
    OP_82(0x32, 0x32, 0xBB8, 0xC8)
    OP_4B(0xB, 0x0)
    OP_4B(0xB, 0x1)
    OP_4B(0xFE, 0x1)
    OP_71(0x0, 0x45, 0x49, 0x1, 0x0)
    OP_79(0x0)
    OP_4C(0xB, 0x0)
    OP_4C(0xB, 0x1)
    OP_4C(0xFE, 0x1)
    OP_71(0x0, 0x4A, 0x58, 0x1, 0x0)
    OP_79(0x0)
    Sound(902, 0, 70, 0)
    OP_82(0x32, 0x32, 0xBB8, 0xC8)
    OP_4B(0xB, 0x0)
    OP_4B(0xB, 0x1)
    OP_4B(0xFE, 0x1)
    OP_71(0x0, 0x59, 0x5D, 0x1, 0x0)
    OP_79(0x0)
    OP_4C(0xB, 0x0)
    OP_4C(0xB, 0x1)
    OP_4C(0xFE, 0x1)
    OP_71(0x0, 0x5E, 0x64, 0x1, 0x0)
    OP_79(0x0)

    label("loc_4833")

    Return()

    # Function_57_4773 end

    def Function_58_4834(): pass

    label("Function_58_4834")

    OP_9E(0xFE, 0xFFFF2306, 0xFFFFB10E, 0x249F0, 0x5DC, 0x2)
    OP_98(0xFE, 0x1F4, 0x0, 0x0, 0x3E8, 0x1)
    Return()

    # Function_58_4834 end

    def Function_59_485E(): pass

    label("Function_59_485E")

    OP_74(0x1, 0x1E)

    label("loc_4862")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_48A5")
    OP_71(0x1, 0x3E8, 0x410, 0x0, 0x0)
    OP_79(0x1)
    Sleep(1000)
    OP_71(0x1, 0x3E8, 0x410, 0x0, 0x0)
    OP_79(0x1)
    OP_71(0x1, 0x3E8, 0x410, 0x0, 0x0)
    OP_79(0x1)
    Sleep(1000)
    Jump("loc_4862")

    label("loc_48A5")

    Return()

    # Function_59_485E end

    def Function_60_48A6(): pass

    label("Function_60_48A6")

    Sound(905, 0, 40, 0)
    Sleep(500)
    Sound(951, 0, 40, 0)
    Sleep(500)
    Return()

    # Function_60_48A6 end

    def Function_61_48B9(): pass

    label("Function_61_48B9")

    OP_98(0xFE, 0xBB8, 0x1388, 0x0, 0x7D0, 0x1)
    OP_98(0xFE, 0x12C, 0x1F4, 0x0, 0xBB8, 0x1)
    OP_98(0xFE, 0x12C, 0x1F4, 0x0, 0xFA0, 0x1)
    OP_98(0xFE, 0x12C, 0x1F4, 0x0, 0x1388, 0x1)
    OP_98(0xFE, 0x12C, 0x1F4, 0x0, 0x1770, 0x1)
    OP_98(0xFE, 0x12C, 0x1F4, 0x0, 0x1B58, 0x1)
    OP_98(0xFE, 0x12C, 0x1F4, 0x0, 0x1F40, 0x1)
    OP_98(0xFE, 0x12C, 0x1F4, 0x0, 0x2328, 0x1)
    OP_98(0xFE, 0x12C, 0x1F4, 0x0, 0x2710, 0x1)
    OP_98(0xFE, 0xE10, 0x1770, 0x0, 0x2AF8, 0x1)
    OP_98(0xFE, 0x2328, 0x3A98, 0x0, 0x2EE0, 0x1)
    Return()

    # Function_61_48B9 end

    def Function_62_4996(): pass

    label("Function_62_4996")

    OP_98(0xFE, 0x0, 0x7530, 0x0, 0x1388, 0x1)
    Return()

    # Function_62_4996 end

    def Function_63_49AB(): pass

    label("Function_63_49AB")

    SetChrChipByIndex(0xFE, 0x2D)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x0)
    Sleep(111)
    SetChrSubChip(0xFE, 0x1)
    Sleep(111)
    SetChrSubChip(0xFE, 0x2)
    Sleep(333)
    Return()

    # Function_63_49AB end

    def Function_64_49CF(): pass

    label("Function_64_49CF")

    SetChrChipByIndex(0xFE, 0x2D)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x7)
    Sleep(143)
    SetChrSubChip(0xFE, 0x8)
    Sleep(143)
    SetChrSubChip(0xFE, 0x9)
    Sleep(857)
    Return()

    # Function_64_49CF end

    def Function_65_49F3(): pass

    label("Function_65_49F3")

    SetChrChipByIndex(0xFE, 0x2D)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0xB)
    Sleep(125)
    SetChrSubChip(0xFE, 0xC)
    Sleep(125)
    SetChrSubChip(0xFE, 0xD)
    Sleep(125)
    SetChrSubChip(0xFE, 0xC)
    Sleep(125)
    SetChrSubChip(0xFE, 0xB)
    Sleep(500)
    Return()

    # Function_65_49F3 end

    def Function_66_4A25(): pass

    label("Function_66_4A25")

    SetChrChipByIndex(0xFE, 0x2D)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0xB)
    Sleep(143)
    SetChrSubChip(0xFE, 0xE)
    Sleep(143)
    SetChrSubChip(0xFE, 0xF)
    Sleep(571)
    Return()

    # Function_66_4A25 end

    def Function_67_4A49(): pass

    label("Function_67_4A49")

    ClearMapObjFlags(0x1, 0x20)
    OP_79(0x1)
    Sound(905, 0, 100, 0)
    OP_74(0x1, 0xA)
    OP_71(0x1, 0x1FE, 0x212, 0x0, 0x0)
    OP_79(0x1)
    Sound(579, 2, 60, 0)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x212, 0x23A, 0x0, 0x20)
    Return()

    # Function_67_4A49 end

    def Function_68_4A82(): pass

    label("Function_68_4A82")

    Sound(905, 0, 100, 0)
    ClearMapObjFlags(0x1, 0x20)
    OP_79(0x1)
    Sound(1019, 0, 100, 0)
    OP_74(0x1, 0xF)
    OP_71(0x1, 0x23A, 0x24E, 0x0, 0x0)
    Return()

    # Function_68_4A82 end

    def Function_69_4AA8(): pass

    label("Function_69_4AA8")

    OP_74(0x1, 0xF)
    OP_71(0x1, 0x3D4, 0x3E8, 0x0, 0x0)
    Sleep(3000)
    Return()

    # Function_69_4AA8 end

    def Function_70_4ABC(): pass

    label("Function_70_4ABC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4AE0")
    OP_82(0x32, 0x32, 0xBB8, 0x5DC)
    Sleep(1000)
    Jump("Function_70_4ABC")

    label("loc_4AE0")

    Return()

    # Function_70_4ABC end

    def Function_71_4AE1(): pass

    label("Function_71_4AE1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4B05")
    OP_82(0x64, 0x64, 0xBB8, 0x5DC)
    Sleep(1000)
    Jump("Function_71_4AE1")

    label("loc_4B05")

    Return()

    # Function_71_4AE1 end

    def Function_72_4B06(): pass

    label("Function_72_4B06")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    StopEffect(0x9, 0x0)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x394),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x394, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x18A, 1)
    OP_65(0x2, 0x1)
    EventEnd(0x3)
    Return()

    # Function_72_4B06 end

    SaveToFile()

Try(main)
