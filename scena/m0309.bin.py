from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "m0309.bin",                # FileName
        "m0309",                    # MapName
        "m0309",                    # Location
        0x00A8,                     # MapIndex
        "ed7300",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 168, 0, 0, 0, 1],
    )

    BuildStringList((
        "m0309",                  # 0
        "新型装甲車",             # 1
        "Terrorist Leader",       # 2
        "Terrorist",              # 3
        "Terrorist",              # 4
        "Terrorist",              # 5
        "Terrorist",              # 6
        "Terrorist",              # 7
        "Terrorist",              # 8
        "Terrorist",              # 9
        "Ogre Sigmund",           # 10
        "Shirley",                # 11
        "Jaeger Gareth",          # 12
        "新型装甲車",             # 13
        "通信機",                 # 14
        "イベント用モンスター",   # 15
        "イベント用モンスター",   # 16
        "イベント用モンスター",   # 17
        "イベント用モンスター",   # 18
        "Jaeger",                 # 19
        "Jaeger",                 # 20
        "Jaeger",                 # 21
        "Jaeger",                 # 22
        "Jaeger",                 # 23
        "ダミー影",               # 24
        "SE制御",                 # 25
        "bm0320",                 # 26
        "bm0320",                 # 27
        "bm0320",                 # 28
    ))

    ATBonus("ATBonus_4D8", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)
    ATBonus("ATBonus_4B8", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_4F8", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_4FC", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_500", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_504", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_508", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_50C", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_510", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_514", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_578", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_57C", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_580", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_584", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_588", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_58C", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_590", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_594", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_598", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_59C", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_5A0", 11, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_5A4", 6, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_5A8", 2, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_5AC", 10, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_5B0", 14, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_5B4", 8, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_5B8", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_5BC", 2, 8, 135)
    MonsterBattlePostion("MonsterBattlePostion_5C0", 4, 10, 135)
    MonsterBattlePostion("MonsterBattlePostion_5C4", 0, 9, 135)
    MonsterBattlePostion("MonsterBattlePostion_5C8", 2, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_5CC", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_5D0", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_5D4", 0, 0, 180)

    # monster count: 1

    BattleInfo(
        "BattleInfo_660", 0x0C00, 255, 6, 0, 0, 0, 0, 0, "bm0320", 0x00000000, 100, 0, 0, 0,
        (
            ("ms66100.dat", "ms66100.dat", "ms66100.dat", "ms66100.dat", "ms66100.dat", "ms66100.dat", 0, 0, "MonsterBattlePostion_4F8", "MonsterBattlePostion_578", "ed7451", "ed7453", "ATBonus_4D8"),
            (),
            (),
            (),
        )
    )

    # event battle count: 3

    BattleInfo(
        "BattleInfo_5D8", 0x0042, 3, 6, 45, 3, 3, 30, 0, "bm0320", 0x00000000, 100, 0, 0, 0,
        (
            ("ms42200.dat", "ms42200.dat", "ms42200.dat", "ms42300.dat", "ms42300.dat", "ms42300.dat", "ms42300.dat", "ms42200.dat", "MonsterBattlePostion_598", "MonsterBattlePostion_578", "ed7452", "ed7453", "ATBonus_4B8"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_61C", 0x0052, 3, 6, 45, 3, 3, 30, 0, "bm0320", 0x00000000, 100, 0, 0, 0,
        (
            ("ms88600.dat", "ms84100.dat", "ms84100.dat", "ms84300.dat", "ms84300.dat", 0, "ms84300.dat", 0, "MonsterBattlePostion_5B8", "MonsterBattlePostion_578", "ed7586", "ed7453", "ATBonus_4B8"),
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
        "monster/ch66150.itc",               # 10
        "monster/ch66150.itc",               # 11
    ))

    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    503,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(0,       0,       750,     0x185005A,    "BattleInfo_660", 0,   16,  0xFFFF, 0,  1)

    DeclEvent(0x0040, 0, 54,  0.0,                   0.0,                   -1.0,                  16.0,                  [0.125,                -0.0,                  0.0,                   0.0,                   -0.0,                  0.125,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.25,                  0.0,                   -0.0,                  -0.0,                  0.25,                  1.0])

    DeclActor(5800,    50,      398500,  1200,    5800,    1050,    398500,  0x007C, 0,  3,  0x0000)
    DeclActor(4294671796, 0,       500,     1200,    4294671796, 1000,    500,     0x007C, 0,  5,  0x0000)
    DeclActor(301800,  0,       19500,   1200,    301800,  1000,    19500,   0x007C, 0,  7,  0x0000)
    DeclActor(4294832796, 0,       3000,    1200,    4294832796, 1500,    3000,    0x007C, 0,  2,  0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 0
    ChipFrameInfo(1000, 0, [0, 1, 2, 3])                         # 1

    ScpFunction((
        "Function_0_79C",          # 00, 0
        "Function_1_83C",          # 01, 1
        "Function_2_B2A",          # 02, 2
        "Function_3_C1E",          # 03, 3
        "Function_4_D83",          # 04, 4
        "Function_5_E92",          # 05, 5
        "Function_6_FF7",          # 06, 6
        "Function_7_1106",         # 07, 7
        "Function_8_1259",         # 08, 8
        "Function_9_1368",         # 09, 9
        "Function_10_2633",        # 0A, 10
        "Function_11_267E",        # 0B, 11
        "Function_12_26B8",        # 0C, 12
        "Function_13_26E6",        # 0D, 13
        "Function_14_271A",        # 0E, 14
        "Function_15_2748",        # 0F, 15
        "Function_16_277C",        # 10, 16
        "Function_17_27AA",        # 11, 17
        "Function_18_27E4",        # 12, 18
        "Function_19_2812",        # 13, 19
        "Function_20_2822",        # 14, 20
        "Function_21_3830",        # 15, 21
        "Function_22_3863",        # 16, 22
        "Function_23_38A2",        # 17, 23
        "Function_24_38E1",        # 18, 24
        "Function_25_3910",        # 19, 25
        "Function_26_393F",        # 1A, 26
        "Function_27_3981",        # 1B, 27
        "Function_28_39C3",        # 1C, 28
        "Function_29_39F9",        # 1D, 29
        "Function_30_3A4E",        # 1E, 30
        "Function_31_3AA3",        # 1F, 31
        "Function_32_3AF8",        # 20, 32
        "Function_33_3B50",        # 21, 33
        "Function_34_3B98",        # 22, 34
        "Function_35_3BE0",        # 23, 35
        "Function_36_3C28",        # 24, 36
        "Function_37_3C70",        # 25, 37
        "Function_38_3CB8",        # 26, 38
        "Function_39_3D06",        # 27, 39
        "Function_40_43FF",        # 28, 40
        "Function_41_6778",        # 29, 41
        "Function_42_6E45",        # 2A, 42
        "Function_43_71F4",        # 2B, 43
        "Function_44_73B0",        # 2C, 44
        "Function_45_73DE",        # 2D, 45
        "Function_46_740B",        # 2E, 46
        "Function_47_7431",        # 2F, 47
        "Function_48_7475",        # 30, 48
        "Function_49_74C7",        # 31, 49
        "Function_50_750B",        # 32, 50
        "Function_51_755D",        # 33, 51
        "Function_52_75A1",        # 34, 52
        "Function_53_75C0",        # 35, 53
        "Function_54_75E7",        # 36, 54
        "Function_55_7A72",        # 37, 55
    ))


    def Function_0_79C(): pass

    label("Function_0_79C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x143, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x143, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7B6")
    Event(0, 9)

    label("loc_7B6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x143, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7D0")
    Event(0, 40)

    label("loc_7D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_7E7")
    ClearScenarioFlags(0x22, 0)
    SetScenarioFlags(0x0, 0)
    Event(0, 20)
    Jump("loc_7F6")

    label("loc_7E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_7F6")
    ClearScenarioFlags(0x22, 1)
    Event(0, 39)

    label("loc_7F6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_ADD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_80D")
    Event(0, 4)

    label("loc_80D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_ADD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_824")
    Event(0, 6)

    label("loc_824")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_ADD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_83B")
    Event(0, 8)

    label("loc_83B")

    Return()

    # Function_0_79C end

    def Function_1_83C(): pass

    label("Function_1_83C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_868")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_863")
    ClearChrFlags(0x21, 0x80)
    ModifyEventFlags(1, 0, 0x80)
    SetChrFlags(0x21, 0x8000)

    label("loc_863")

    Jump("loc_872")

    label("loc_868")

    SetChrFlags(0x21, 0x80)
    ModifyEventFlags(0, 0, 0x80)

    label("loc_872")

    OP_52(0x21, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrBattleFlags(0x21, 0x100)
    OP_52(0x21, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_10(0x0, 0x0)
    OP_10(0x7, 0x0)
    OP_10(0x8, 0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_ADD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8D4")
    SetMapObjFrame(0x3, "Null_color", 0x0, 0x1)
    SetMapObjFrame(0x3, "Null_color2", 0x1, 0x1)
    Jump("loc_8F9")

    label("loc_8D4")

    SetMapObjFrame(0x3, "Null_color", 0x1, 0x1)
    SetMapObjFrame(0x3, "Null_color2", 0x0, 0x1)

    label("loc_8F9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_ADD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_937")
    SetMapObjFrame(0x4, "Null_color", 0x0, 0x1)
    SetMapObjFrame(0x4, "Null_color2", 0x1, 0x1)
    Jump("loc_95C")

    label("loc_937")

    SetMapObjFrame(0x4, "Null_color", 0x1, 0x1)
    SetMapObjFrame(0x4, "Null_color2", 0x0, 0x1)

    label("loc_95C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_ADD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_99A")
    SetMapObjFrame(0x5, "Null_color", 0x1, 0x1)
    SetMapObjFrame(0x5, "Null_color2", 0x0, 0x1)
    Jump("loc_9BF")

    label("loc_99A")

    SetMapObjFrame(0x5, "Null_color", 0x0, 0x1)
    SetMapObjFrame(0x5, "Null_color2", 0x1, 0x1)

    label("loc_9BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A17")
    SetMapObjFrame(0x3, "Null_color", 0x0, 0x1)
    SetMapObjFrame(0x3, "Null_color2", 0x0, 0x1)
    SetMapObjFrame(0x4, "Null_color", 0x0, 0x1)
    SetMapObjFrame(0x4, "Null_color2", 0x0, 0x1)

    label("loc_A17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x143, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A7C")
    ClearMapObjFlags(0x9, 0x4)
    OP_78(0x9, 0x8)
    SetMapObjFlags(0x9, 0x1000)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 2000, 0, 1000, 180)
    OP_D5(0x8, 0x0, 0x222E0, 0x0, 0x0)
    OP_74(0x9, 0x1E)
    OP_71(0x9, 0x79, 0xF0, 0x0, 0x20)
    SetMapObjFrame(0x9, "mark00", 0x1, 0x1)

    label("loc_A7C")

    SetMapObjFlags(0x8, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_AD6")
    LoadEffect(0x9, "event\\ev12003.eff")
    PlayEffect(0x9, 0xFF, 0xFF, 0x0, 169200, 0, 13900, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    label("loc_AD6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x143, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B29")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x70), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B0C")
    Sound(863, 1, 50, 0)
    Sound(864, 1, 50, 0)
    Jump("loc_B29")

    label("loc_B0C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B29")
    OP_24(0x35F)
    OP_24(0x360)

    label("loc_B29")

    Return()

    # Function_1_83C end

    def Function_2_B2A(): pass

    label("Function_2_B2A")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C0F")
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

    label("loc_C0F")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_2_B2A end

    def Function_3_C1E(): pass

    label("Function_3_C1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C30")
    Call(0, 55)
    Return()

    label("loc_C30")

    SetMapFlags(0x8000000)
    EventBegin(0x1)
    SoundLoad(144)
    SoundLoad(150)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's a lift control\x01",
            "panel. Operate?\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D7B")
    Fade(500)
    SetChrPos(0x0, 5200, 50, 397000, 0)
    SetChrPos(0x1, 6200, 50, 397000, 0)
    SetChrPos(0x2, 5200, 50, 396000, 0)
    SetChrPos(0x3, 6200, 50, 396000, 0)
    OP_68(5200, 1550, 392980, 0)
    MoveCamera(24, 45, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(25000, 0)
    OP_0D()
    Sleep(500)
    Sound(144, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_71(0x3, 0xA, 0xC8, 0x0, 0x0)
    Sleep(200)
    OP_68(6000, 2000, 410000, 3800)
    MoveCamera(22, 49, 0, 3800)
    Sleep(1800)
    Sound(150, 2, 100, 0)
    Sleep(200)
    FadeToDark(500, 0, -1)
    Sleep(4000)
    StopSound(150, 1000, 100)
    Sleep(1000)
    OP_0D()
    NewScene("m0300", 101, 0, 0)
    IdleLoop()

    label("loc_D7B")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_3_C1E end

    def Function_4_D83(): pass

    label("Function_4_D83")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    OP_6F(0x1)
    OP_70(0x3, 0x64)
    Sleep(1)
    OP_68(4710, 4300, 403470, 0)
    MoveCamera(23, 36, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(25000, 0)
    OP_90(0x0, 3500, 2800, 409000, 270)
    OP_90(0x1, 3500, 2800, 408000, 270)
    OP_90(0x2, 4500, 2800, 409000, 270)
    OP_90(0x3, 4500, 2800, 408000, 270)
    Sound(145, 0, 100, 0)
    OP_68(4830, 50, 394970, 3200)
    MoveCamera(45, 44, 0, 3200)
    OP_71(0x3, 0x64, 0xA, 0x0, 0x0)
    FadeToBright(500, 0)
    Sleep(3400)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_79(0x3)
    OP_6F(0x1)
    Sleep(500)
    SetMapObjFrame(0x3, "Null_color", 0x1, 0x1)
    SetMapObjFrame(0x3, "Null_color2", 0x0, 0x1)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_4_D83 end

    def Function_5_E92(): pass

    label("Function_5_E92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EA4")
    Call(0, 55)
    Return()

    label("loc_EA4")

    SetMapFlags(0x8000000)
    EventBegin(0x1)
    SoundLoad(144)
    SoundLoad(150)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's a lift control\x01",
            "panel. Operate?\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FEF")
    Fade(500)
    SetChrPos(0x0, -296500, 0, 0, 90)
    SetChrPos(0x1, -296500, 0, 1000, 90)
    SetChrPos(0x2, -297500, 0, 0, 90)
    SetChrPos(0x3, -297500, 0, 1000, 90)
    OP_68(-300940, 1500, 840, 0)
    MoveCamera(58, 54, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(25000, 0)
    OP_0D()
    Sleep(500)
    Sound(144, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_71(0x4, 0xA, 0xC8, 0x0, 0x0)
    Sleep(200)
    OP_68(-282200, 3500, 820, 3200)
    MoveCamera(50, 20, 0, 3200)
    Sleep(1800)
    Sound(150, 2, 100, 0)
    Sleep(200)
    FadeToDark(500, 0, -1)
    Sleep(4000)
    StopSound(150, 1000, 100)
    Sleep(1000)
    OP_0D()
    NewScene("m0301", 121, 0, 0)
    IdleLoop()

    label("loc_FEF")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_5_E92 end

    def Function_6_FF7(): pass

    label("Function_6_FF7")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    OP_6F(0x1)
    OP_70(0x4, 0x64)
    Sleep(1)
    OP_68(-287810, 4250, 240, 0)
    MoveCamera(70, 33, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(25000, 0)
    OP_90(0x0, -285000, 2750, -1500, 180)
    OP_90(0x1, -286000, 2750, -1500, 180)
    OP_90(0x2, -285000, 2750, -500, 180)
    OP_90(0x3, -286000, 2750, -500, 180)
    Sound(145, 0, 100, 0)
    OP_68(-299340, 1500, -3660, 3200)
    MoveCamera(32, 46, 0, 3200)
    OP_71(0x4, 0x64, 0xA, 0x0, 0x0)
    FadeToBright(500, 0)
    Sleep(3400)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_79(0x4)
    OP_6F(0x1)
    Sleep(500)
    SetMapObjFrame(0x4, "Null_color", 0x1, 0x1)
    SetMapObjFrame(0x4, "Null_color2", 0x0, 0x1)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_6_FF7 end

    def Function_7_1106(): pass

    label("Function_7_1106")

    SetMapFlags(0x8000000)
    EventBegin(0x1)
    SoundLoad(144)
    SoundLoad(150)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's a lift control\x01",
            "panel. Operate?\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1251")
    Fade(500)
    SetChrPos(0x0, 301300, 0, 20500, 180)
    SetChrPos(0x1, 302300, 0, 20500, 180)
    SetChrPos(0x2, 301300, 0, 21500, 180)
    SetChrPos(0x3, 302300, 0, 21500, 180)
    OP_68(300400, 1500, 21470, 0)
    MoveCamera(37, 51, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(25000, 0)
    OP_0D()
    Sleep(500)
    Sound(144, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_71(0x5, 0x2F8, 0x3B6, 0x0, 0x0)
    Sleep(200)
    OP_68(301740, -1000, 14430, 3200)
    MoveCamera(33, 42, 0, 3200)
    Sleep(1800)
    Sound(150, 2, 100, 0)
    Sleep(200)
    FadeToDark(500, 0, -1)
    Sleep(4000)
    StopSound(150, 1000, 100)
    Sleep(1000)
    OP_0D()
    NewScene("m0302", 115, 0, 0)
    IdleLoop()

    label("loc_1251")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_7_1106 end

    def Function_8_1259(): pass

    label("Function_8_1259")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    OP_6F(0x1)
    OP_70(0x5, 0x352)
    Sleep(1)
    OP_68(299320, -1000, 7960, 0)
    MoveCamera(24, 27, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(25000, 0)
    OP_90(0x0, 299500, -2500, 9500, 270)
    OP_90(0x1, 299500, -2500, 8500, 270)
    OP_90(0x2, 300500, -2500, 9500, 270)
    OP_90(0x3, 300500, -2500, 8500, 270)
    Sound(145, 0, 100, 0)
    OP_68(299490, 1500, 24190, 3200)
    MoveCamera(60, 27, 0, 3200)
    OP_71(0x5, 0x352, 0x2F8, 0x0, 0x0)
    FadeToBright(500, 0)
    Sleep(3400)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_79(0x5)
    OP_6F(0x1)
    Sleep(500)
    SetMapObjFrame(0x5, "Null_color", 0x0, 0x1)
    SetMapObjFrame(0x5, "Null_color2", 0x1, 0x1)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_8_1259 end

    def Function_9_1368(): pass

    label("Function_9_1368")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    LoadChrToIndex("chr/ch42200.itc", 0x1E)
    LoadChrToIndex("chr/ch42250.itc", 0x1F)
    LoadChrToIndex("chr/ch42251.itc", 0x20)
    LoadChrToIndex("chr/ch42300.itc", 0x21)
    LoadChrToIndex("chr/ch42350.itc", 0x22)
    LoadChrToIndex("chr/ch42351.itc", 0x23)
    LoadChrToIndex("chr/ch42352.itc", 0x24)
    LoadChrToIndex("chr/ch00050.itc", 0x25)
    LoadChrToIndex("chr/ch00051.itc", 0x26)
    LoadChrToIndex("chr/ch00150.itc", 0x27)
    LoadChrToIndex("chr/ch00151.itc", 0x28)
    LoadChrToIndex("chr/ch00250.itc", 0x29)
    LoadChrToIndex("chr/ch00251.itc", 0x2A)
    LoadChrToIndex("chr/ch00350.itc", 0x2B)
    LoadChrToIndex("chr/ch00351.itc", 0x2C)
    LoadChrToIndex("chr/ch02950.itc", 0x2D)
    LoadChrToIndex("chr/ch02951.itc", 0x2E)
    LoadChrToIndex("chr/ch03050.itc", 0x2F)
    LoadChrToIndex("chr/ch03051.itc", 0x30)
    LoadChrToIndex("apl/ch51243.itc", 0x31)
    LoadChrToIndex("apl/ch50014.itc", 0x32)
    LoadChrToIndex("chr/ch42254.itc", 0x33)
    LoadEffect(0x1, "event/ev10016.eff")
    SetChrPos(0x101, -38000, -8000, -600, 90)
    SetChrPos(0x102, -38000, -8000, 600, 90)
    SetChrPos(0x103, -39000, -8000, -1000, 90)
    SetChrPos(0x104, -39200, -8000, 1000, 90)
    SetChrPos(0x109, -40200, -8000, -600, 90)
    SetChrPos(0x105, -40200, -8000, 600, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x9, 0x31)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 900, 0, 900, 225)
    SetChrChipByIndex(0xA, 0x1E)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, -1700, 0, -200, 90)
    SetChrChipByIndex(0xB, 0x21)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, -200, 0, -1700, 0)
    SetChrChipByIndex(0xC, 0x21)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, -1200, 0, 1200, 135)
    SetChrChipByIndex(0xD, 0x21)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    SetChrPos(0xD, 1200, 0, -1200, 315)
    SetChrChipByIndex(0xE, 0x1E)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)
    SetChrPos(0xE, -1300, 0, -1300, 45)
    SetChrChipByIndex(0xF, 0x1E)
    SetChrSubChip(0xF, 0x0)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xF, -2600, 0, 300, 90)
    SetChrChipByIndex(0x10, 0x21)
    SetChrSubChip(0x10, 0x0)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x8000)
    SetChrPos(0x10, 300, 0, -2600, 0)
    ClearChrFlags(0x15, 0x80)
    OP_78(0x8, 0x15)
    OP_49()
    ClearMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x8, 0x1000)
    SetChrPos(0x15, 400, 150, 400, 0)
    OP_D5(0x15, 0x0, 0x36EE8, 0x0, 0x0)
    OP_68(-34500, -7100, 0, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(660, 0)
    SetCameraDistance(16500, 0)
    OP_68(-30500, -7100, 0, 4000)
    FadeToBright(2000, 0)

    def lambda_1669():
        OP_97(0x101, 0x1F40, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1669)
    Sleep(150)

    def lambda_1686():
        OP_97(0x102, 0x1F40, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1686)
    Sleep(150)

    def lambda_16A3():
        OP_97(0x103, 0x1F40, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_16A3)
    Sleep(150)

    def lambda_16C0():
        OP_97(0x104, 0x1F40, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_16C0)
    Sleep(150)

    def lambda_16DD():
        OP_97(0x109, 0x1F40, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_16DD)
    Sleep(150)

    def lambda_16FA():
        OP_97(0x105, 0x1F40, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_16FA)
    Sleep(500)

    def lambda_1717():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1717)
    Sleep(300)

    def lambda_172B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_172B)
    Sleep(500)

    def lambda_173F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_173F)
    Sleep(300)

    def lambda_1753():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1753)
    Sleep(500)

    def lambda_1767():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1767)
    Sleep(300)

    def lambda_177B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_177B)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
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
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x101,
        "#6P#00007F(That's...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00201F(Looks like we managed\x01",
            "to catch up with them.)\x02",
        )
    )

    CloseMessageWindow()
    OP_68(0, 900, 0, 4000)
    MoveCamera(45, 33, 0, 4000)
    SetCameraDistance(15500, 4000)
    BeginChrThread(0x15, 3, 0, 10)
    OP_6F(0x79)
    Sound(867, 0, 100, 0)

    ChrTalk(
        0x9,
        "Tch, I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "So they prevented us\x01",
            "from blowing up the\x01",
            "tower, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#3PTch, damn it all...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#4POur chance to erase that\x01",
            "detestable Blood and Iron\x01",
            "Chancellor slipped away!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#6PAnd after we went to the\x01",
            "trouble of joining forces with\x01",
            "those Republican guys, too.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    Sound(812, 0, 100, 0)
    EndChrThread(0x15, 0x3)
    SetChrChipByIndex(0x9, 0x1E)
    SetChrSubChip(0x9, 0x0)
    OP_0D()
    Sleep(300)
    OP_82(0x32, 0x0, 0xBB8, 0xC8)

    ChrTalk(
        0x9,
        (
            "Don't lose heart,\x01",
            "comrades!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Our allies are many! Starting\x01",
            "with Duke Cayenne, they will\x01",
            "help us once again!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If we can just get out\x01",
            "of here, another\x01",
            "opportunity will...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    Sound(2090, 255, 100, 0)

    NpcTalk(
        0x101,
        "Lloyd's Voice",
        "Freeze!\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_1BC6():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1BC6)

    def lambda_1BD3():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_1BD3)
    Sleep(50)

    def lambda_1BE3():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1BE3)

    def lambda_1BF0():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_1BF0)
    Sleep(50)

    def lambda_1C00():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_1C00)

    def lambda_1C0D():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_1C0D)
    Sleep(50)

    def lambda_1C1D():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_1C1D)

    def lambda_1C2A():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_1C2A)
    WaitChrThread(0x10, 2)
    Fade(500)
    OP_68(-9800, -300, -700, 0)
    MoveCamera(50, 17, 0, 0)
    OP_6E(660, 0)
    SetCameraDistance(18000, 0)
    SetChrFlags(0x15, 0x80)
    SetMapObjFlags(0x8, 0x4)
    ClearMapObjFlags(0x8, 0x1000)
    OP_68(-4800, 700, 0, 2500)
    SetCameraDistance(16000, 2500)
    SetChrChipByIndex(0x101, 0x25)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x27)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x29)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x2B)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x2D)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x2F)
    SetChrSubChip(0x105, 0x0)
    OP_90(0x101, -17200, 0, 0, 90)
    OP_90(0x102, -18000, 0, -1700, 90)
    OP_90(0x103, -19500, 0, 1300, 90)
    OP_90(0x104, -18000, 0, 1700, 90)
    OP_90(0x109, -19500, 0, -1300, 90)
    OP_90(0x105, -18900, 0, 0, 90)

    def lambda_1D2F():
        OP_97(0x101, 0x2710, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1D2F)
    Sleep(100)

    def lambda_1D4C():
        OP_97(0x104, 0x2710, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1D4C)
    Sleep(100)

    def lambda_1D69():
        OP_97(0x102, 0x2710, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1D69)
    Sleep(100)

    def lambda_1D86():
        OP_97(0x105, 0x2710, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_1D86)
    Sleep(100)

    def lambda_1DA3():
        OP_97(0x109, 0x2710, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1DA3)
    Sleep(100)

    def lambda_1DC0():
        OP_97(0x103, 0x2710, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1DC0)
    BeginChrThread(0x20, 1, 0, 19)
    BeginChrThread(0xF, 3, 0, 17)
    Sleep(100)
    BeginChrThread(0xA, 3, 0, 12)
    Sleep(100)
    BeginChrThread(0xE, 3, 0, 16)
    Sleep(400)
    BeginChrThread(0xB, 3, 0, 13)
    Sleep(100)
    BeginChrThread(0xC, 3, 0, 14)
    Sleep(100)
    BeginChrThread(0xD, 3, 0, 15)
    Sleep(100)
    BeginChrThread(0x10, 3, 0, 18)
    Sleep(400)
    BeginChrThread(0x9, 3, 0, 11)
    WaitChrThread(0x9, 3)

    ChrTalk(
        0xA,
        "#11PWha...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11PThe brats from back\x01",
            "there!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Impossible! We took out\x01",
            "the only way through!\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x103, 0)

    ChrTalk(
        0x104,
        (
            "#00304F#6PWe found another route\x01",
            "though. Too bad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00202FI don't know what kind of\x01",
            "data you acquired, but it\x01",
            "seems it wasn't accurate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#11PGuh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11PWho the fuck are you\x01",
            "guys anyway!? You brats\x01",
            "are...\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    Sound(802, 0, 100, 0)
    Sound(805, 0, 50, 0)
    SetChrChipByIndex(0x101, 0x32)
    SetChrSubChip(0x101, 0x0)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#6P#00003FCrossbell Police, Special Support Section.\x02\x03",
            "#00013FYou've been caught red-handed for terrorism and\x01",
            "subversive activities. You're also under arrest\x01",
            "for attempted assassination and mass murder.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x50, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0xA,
        "#11PPolice, you say!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11PAs if mere state police\x01",
            "could stand in the way\x01",
            "of our great cause!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x109,
        (
            "#6P#10107F#4SD-Don't joke around!\x02\x03",
            "#10110FHow many people were you\x01",
            "planning to involve!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10306FMan, so they really do\x01",
            "exist.\x02\x03",
            "#10300FGuys who get caught up in a\x01",
            ""just cause" and can't even\x01",
            "see what's around them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#11PTch, shut up!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "You idiots! You forgot\x01",
            "your pride and indulge\x01",
            "only in empty prosperity!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00108F...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00203FLooks like they have zero\x01",
            "intention to reflect on\x01",
            "what they did.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopBGM(0xFA0)
    OP_63(0x9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Fade(250)
    Sound(805, 0, 80, 0)
    SetChrChipByIndex(0x101, 0x25)
    SetChrSubChip(0x101, 0x0)
    OP_0D()
    Sleep(1750)
    OP_64(0x9)
    Sleep(300)

    ChrTalk(
        0x9,
        (
            "#11P─It was not our\x01",
            "intention to involve\x01",
            "outsiders.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PHowever, if we leave that man\x01",
            "alone any longer, the Empire\x01",
            "will become a giant mess...\x02",
        )
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7452", 0)
    SetChrSubChip(0x9, 0x3)
    Sleep(100)
    SetChrSubChip(0x9, 0x4)
    Sound(802, 0, 100, 0)
    Sound(534, 0, 60, 0)
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x9,
        (
            "#11PAnd we won't forgive\x01",
            "anyone who gets in our\x01",
            "way!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00013FUgh!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00307FNo use talkin'! Anyway,\x01",
            "let's beat 'em up!\x02",
        )
    )

    CloseMessageWindow()
    BlurSwitch(0x190, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetCameraDistance(13500, 400)

    def lambda_2504():
        OP_98(0xFE, 0xFFFFD8F0, 0x0, 0x0, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_2504)
    SetChrChipByIndex(0xA, 0x20)
    SetChrSubChip(0xA, 0x0)
    Sleep(30)

    def lambda_2529():
        OP_98(0xFE, 0xFFFFD8F0, 0x0, 0x0, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_2529)
    SetChrChipByIndex(0xE, 0x20)
    SetChrSubChip(0xE, 0x0)

    def lambda_254B():
        OP_98(0xFE, 0xFFFFD8F0, 0x0, 0x0, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_254B)
    SetChrChipByIndex(0xF, 0x20)
    SetChrSubChip(0xF, 0x0)
    Sleep(30)

    def lambda_2570():
        OP_98(0xFE, 0xFFFFD8F0, 0x0, 0x0, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2570)
    SetChrChipByIndex(0xB, 0x23)
    SetChrSubChip(0xB, 0x0)

    def lambda_2592():
        OP_98(0xFE, 0xFFFFD8F0, 0x0, 0x0, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_2592)
    SetChrChipByIndex(0xD, 0x23)
    SetChrSubChip(0xD, 0x0)
    Sleep(30)

    def lambda_25B7():
        OP_98(0xFE, 0xFFFFD8F0, 0x0, 0x0, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_25B7)
    SetChrChipByIndex(0xC, 0x23)
    SetChrSubChip(0xC, 0x0)

    def lambda_25D9():
        OP_98(0xFE, 0xFFFFD8F0, 0x0, 0x0, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_25D9)
    SetChrChipByIndex(0x10, 0x23)
    SetChrSubChip(0x10, 0x0)
    Sleep(310)
    EndChrThread(0xA, 0x1)
    EndChrThread(0xE, 0x1)
    EndChrThread(0xF, 0x1)
    EndChrThread(0xB, 0x1)
    EndChrThread(0xD, 0x1)
    EndChrThread(0xC, 0x1)
    EndChrThread(0x10, 0x1)
    Battle("BattleInfo_5D8", 0x0, 0x0, 0x100, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    Call(0, 20)
    Return()

    # Function_9_1368 end

    def Function_10_2633(): pass

    label("Function_10_2633")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_267D")
    PlayEffect(0x1, 0xFF, 0x15, 0x1, -600, 1150, 0, 0, 0, 0, 200, 200, 200, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    Jump("Function_10_2633")

    label("loc_267D")

    Return()

    # Function_10_2633 end

    def Function_11_267E(): pass

    label("Function_11_267E")


    def lambda_2683():
        OP_95(0xFE, 700, 0, -500, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2683)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Sound(531, 0, 70, 0)
    Sound(540, 0, 50, 0)
    SetChrChipByIndex(0x9, 0x33)
    SetChrSubChip(0x9, 0x0)
    Return()

    # Function_11_267E end

    def Function_12_26B8(): pass

    label("Function_12_26B8")


    def lambda_26BD():
        OP_95(0xFE, -3000, 0, 0, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_26BD)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    SetChrChipByIndex(0xA, 0x1F)
    SetChrSubChip(0xA, 0x0)
    Return()

    # Function_12_26B8 end

    def Function_13_26E6(): pass

    label("Function_13_26E6")


    def lambda_26EB():
        OP_95(0xFE, -1500, 0, 700, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_26EB)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0xB, 0x24)
    SetChrSubChip(0xB, 0x2)
    Return()

    # Function_13_26E6 end

    def Function_14_271A(): pass

    label("Function_14_271A")


    def lambda_271F():
        OP_95(0xFE, -900, 0, 2500, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_271F)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    SetChrChipByIndex(0xC, 0x24)
    SetChrSubChip(0xC, 0x2)
    Return()

    # Function_14_271A end

    def Function_15_2748(): pass

    label("Function_15_2748")


    def lambda_274D():
        OP_95(0xFE, -1500, 0, -700, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_274D)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0xD, 0x24)
    SetChrSubChip(0xD, 0x2)
    Return()

    # Function_15_2748 end

    def Function_16_277C(): pass

    label("Function_16_277C")


    def lambda_2781():
        OP_95(0xFE, -2700, 0, -1900, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2781)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    SetChrChipByIndex(0xE, 0x1F)
    SetChrSubChip(0xE, 0x0)
    Return()

    # Function_16_277C end

    def Function_17_27AA(): pass

    label("Function_17_27AA")


    def lambda_27AF():
        OP_95(0xFE, -2700, 0, 1900, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_27AF)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Sound(531, 0, 70, 0)
    Sound(540, 0, 50, 0)
    SetChrChipByIndex(0xF, 0x1F)
    SetChrSubChip(0xF, 0x0)
    Return()

    # Function_17_27AA end

    def Function_18_27E4(): pass

    label("Function_18_27E4")


    def lambda_27E9():
        OP_95(0xFE, -900, 0, -2500, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_27E9)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    SetChrChipByIndex(0x10, 0x24)
    SetChrSubChip(0x10, 0x2)
    Return()

    # Function_18_27E4 end

    def Function_19_2812(): pass

    label("Function_19_2812")

    Sleep(2000)
    Sound(531, 0, 100, 0)
    Sound(805, 0, 100, 0)
    Return()

    # Function_19_2812 end

    def Function_20_2822(): pass

    label("Function_20_2822")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    LoadChrToIndex("chr/ch42200.itc", 0x1E)
    LoadChrToIndex("chr/ch42250.itc", 0x1F)
    LoadChrToIndex("chr/ch42251.itc", 0x20)
    LoadChrToIndex("chr/ch42300.itc", 0x21)
    LoadChrToIndex("chr/ch42350.itc", 0x22)
    LoadChrToIndex("chr/ch42351.itc", 0x23)
    LoadChrToIndex("chr/ch42353.itc", 0x24)
    LoadChrToIndex("chr/ch00050.itc", 0x25)
    LoadChrToIndex("chr/ch00051.itc", 0x26)
    LoadChrToIndex("chr/ch00150.itc", 0x27)
    LoadChrToIndex("chr/ch00151.itc", 0x28)
    LoadChrToIndex("chr/ch00250.itc", 0x29)
    LoadChrToIndex("chr/ch00251.itc", 0x2A)
    LoadChrToIndex("chr/ch00350.itc", 0x2B)
    LoadChrToIndex("chr/ch00351.itc", 0x2C)
    LoadChrToIndex("chr/ch02950.itc", 0x2D)
    LoadChrToIndex("chr/ch02951.itc", 0x2E)
    LoadChrToIndex("chr/ch03050.itc", 0x2F)
    LoadChrToIndex("chr/ch03051.itc", 0x30)
    LoadChrToIndex("chr/ch42253.itc", 0x31)
    LoadChrToIndex("monster/ch84150.itc", 0x32)
    LoadChrToIndex("monster/ch84350.itc", 0x33)
    LoadChrToIndex("chr/ch00056.itc", 0x34)
    LoadChrToIndex("chr/ch00156.itc", 0x35)
    LoadChrToIndex("chr/ch00256.itc", 0x36)
    LoadChrToIndex("chr/ch00356.itc", 0x37)
    LoadChrToIndex("chr/ch0295F.itc", 0x38)
    LoadChrToIndex("chr/ch0305F.itc", 0x39)
    LoadEffect(0x1, "event/ev12036.eff")
    LoadEffect(0x2, "event/eva03_01.eff")
    SoundLoad(943)
    SetChrChipByIndex(0x101, 0x25)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x27)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x29)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x2B)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x2D)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x2F)
    SetChrSubChip(0x105, 0x0)
    SetChrPos(0x101, -200, 0, 0, 90)
    SetChrPos(0x102, -1000, 0, -1700, 90)
    SetChrPos(0x103, -2500, 0, 1300, 90)
    SetChrPos(0x104, -1000, 0, 1700, 90)
    SetChrPos(0x109, -2500, 0, -1300, 90)
    SetChrPos(0x105, -1900, 0, 0, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 3100, 0, 0, 270)
    SetChrChipByIndex(0xA, 0x31)
    SetChrSubChip(0xA, 0x3)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 3600, 0, 1900, 270)
    SetChrChipByIndex(0xB, 0x24)
    SetChrSubChip(0xB, 0x3)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, 7200, 0, -1300, 270)
    SetChrChipByIndex(0xC, 0x22)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, 7200, 0, 1300, 270)
    SetChrChipByIndex(0xD, 0x24)
    SetChrSubChip(0xD, 0x3)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    SetChrPos(0xD, 5200, 0, 2700, 270)
    SetChrChipByIndex(0xE, 0x31)
    SetChrSubChip(0xE, 0x3)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)
    SetChrPos(0xE, 3600, 0, -1900, 270)
    SetChrChipByIndex(0xF, 0x31)
    SetChrSubChip(0xF, 0x3)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xF, 6200, 0, 0, 270)
    SetChrChipByIndex(0x10, 0x22)
    SetChrSubChip(0x10, 0x0)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x8000)
    SetChrPos(0x10, 5200, 0, -2700, 270)
    SetChrChipByIndex(0x16, 0x32)
    SetChrSubChip(0x16, 0x0)
    SetChrFlags(0x16, 0x8000)
    SetChrPos(0x16, 0, 0, 30000, 180)
    OP_A7(0x16, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x17, 0x32)
    SetChrSubChip(0x17, 0x0)
    SetChrFlags(0x17, 0x8000)
    SetChrPos(0x17, 0, 0, 30000, 180)
    OP_A7(0x17, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x18, 0x33)
    SetChrSubChip(0x18, 0x0)
    SetChrFlags(0x18, 0x8000)
    SetChrPos(0x18, 0, 0, 30000, 180)
    OP_A7(0x18, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x19, 0x33)
    SetChrSubChip(0x19, 0x0)
    SetChrFlags(0x19, 0x8000)
    SetChrPos(0x19, 0, 0, 30000, 180)
    OP_A7(0x19, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x14, 0x80)
    OP_78(0x6, 0x14)
    OP_49()
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x6, 0x1000)
    SetMapObjFrame(0x6, "light", 0x0, 0x1)
    SetMapObjFrame(0x6, "mark00", 0x1, 0x1)
    OP_74(0x6, 0x1E)
    OP_71(0x6, 0xB5, 0xF0, 0x0, 0x20)
    SetChrPos(0x14, 0, 0, 35000, 180)
    OP_D5(0x14, 0x0, 0x2BF20, 0x0, 0x0)
    OP_68(1800, 900, 0, 0)
    MoveCamera(53, 19, 0, 0)
    OP_6E(660, 0)
    SetCameraDistance(15500, 0)
    SetCameraDistance(16500, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_63(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    SetChrChipByIndex(0x9, 0x20)
    SetChrSubChip(0x9, 0x0)

    def lambda_2C2F():
        OP_96(0xFE, 0x1004, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2C2F)
    WaitChrThread(0x9, 1)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)
    OP_64(0x9)

    def lambda_2C58():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_2C58)
    Sleep(500)

    ChrTalk(
        0xA,
        "Tch... Impossible!\x02",
    )

    CloseMessageWindow()

    def lambda_2C8C():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_2C8C)
    Sleep(500)

    ChrTalk(
        0xB,
        (
            "To think we'd be done in\x01",
            "by mere state police!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00006F─It may be true that Crossbell enjoys\x01",
            "prosperity.\x02\x03",
            "#00013FHowever, we're not so drenched in it that\x01",
            "we've forgotten our pride!\x02\x03",
            "#00007FWe have various obligations and pressures...\x01",
            "And although we're squashed by them, we\x01",
            "struggle to try to get over those barriers!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00102FLloyd...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10100FLloyd...\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0xA, 3, 0, 22)
    Sleep(200)
    BeginChrThread(0xB, 3, 0, 23)
    Sleep(200)
    BeginChrThread(0xD, 3, 0, 23)
    Sleep(200)
    Sound(540, 0, 20, 0)
    BeginChrThread(0xE, 3, 0, 22)
    Sleep(200)
    BeginChrThread(0xF, 3, 0, 22)
    Sound(531, 0, 30, 0)
    WaitChrThread(0xF, 3)
    Sleep(300)

    ChrTalk(
        0x9,
        (
            "#11PIt seems we didn't take\x01",
            "you seriously enough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PI admit that trying to\x01",
            "blow up the tower was\x01",
            "going too far.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00000FIn that case...\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x9,
        (
            "#11P─However, we can't allow ourselves\x01",
            "to be captured until we've killed\x01",
            "the Blood and Iron Chancellor!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_93(0x103, 0x0, 0x1F4)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x103,
        "#12P#00207FEveryone!\x02",
    )

    CloseMessageWindow()
    OP_93(0x104, 0x0, 0x1F4)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x104,
        "#00307F#11PIncoming! Get down!\x02",
    )

    CloseMessageWindow()
    OP_68(0, 900, 17000, 1500)
    MoveCamera(37, 15, 0, 1500)
    SetCameraDistance(14500, 1500)

    def lambda_302C():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_302C)
    BeginChrThread(0x9, 3, 0, 24)
    Sleep(50)

    def lambda_3042():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3042)
    BeginChrThread(0xA, 3, 0, 24)
    Sleep(50)

    def lambda_3058():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_3058)
    BeginChrThread(0xE, 3, 0, 24)
    Sleep(50)

    def lambda_306E():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_306E)
    BeginChrThread(0xD, 3, 0, 25)
    BeginChrThread(0x10, 3, 0, 25)
    Sleep(50)
    BeginChrThread(0xF, 3, 0, 24)
    BeginChrThread(0xB, 3, 0, 25)
    BeginChrThread(0xC, 3, 0, 25)
    OP_6F(0x79)
    StopBGM(0x1388)
    Sound(598, 0, 50, 0)
    Sound(623, 0, 100, 0)
    PlayEffect(0x1, 0x1, 0xFF, 0x0, 0, 1000, 30000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0x2, 0xFF, 0x0, 1000, 1500, 30000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0x3, 0xFF, 0x0, -1000, 1500, 30000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    BeginChrThread(0x14, 3, 0, 21)
    Sleep(500)
    Sound(869, 0, 50, 0)
    OP_68(-2600, 900, 0, 1000)
    MoveCamera(53, 19, 0, 1000)
    SetCameraDistance(17500, 1000)
    Sleep(200)
    BeginChrThread(0x103, 3, 0, 38)
    Sleep(50)
    BeginChrThread(0x104, 3, 0, 35)
    BeginChrThread(0x105, 3, 0, 36)
    Sleep(50)
    BeginChrThread(0x101, 3, 0, 33)
    BeginChrThread(0x109, 3, 0, 37)
    Sleep(50)
    BeginChrThread(0x102, 3, 0, 34)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x14, 3)
    Sleep(500)

    ChrTalk(
        0x101,
        "#00007F#6P#NWha...!?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x109,
        "#10110F#6P#NA s-smart missile!?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7586", 0)
    Fade(250)
    OP_68(0, 1000, 25000, 0)
    MoveCamera(25, 25, 21, 0)
    OP_6E(700, 0)
    SetCameraDistance(13500, 0)
    OP_68(1500, 1250, 1000, 3000)
    MoveCamera(50, 15, 11, 3000)
    SetCameraDistance(15500, 3000)
    Sound(486, 0, 100, 0)
    Sound(494, 0, 100, 0)
    ClearMapObjFlags(0x6, 0x4)
    PlayEffect(0x2, 0x4, 0x14, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x5, 0x14, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x6, 0x14, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_3325():
        OP_96(0xFE, 0x0, 0x0, 0x0, 0x2AF8, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_3325)
    Sleep(2500)

    def lambda_3342():
        OP_D5(0xFE, 0x0, 0x30D40, 0x0, 0x2BC)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_3342)
    OP_71(0x6, 0x5B, 0x78, 0x0, 0x0)
    Sound(487, 0, 100, 0)
    WaitChrThread(0x14, 1)
    StopEffect(0x4, 0x2)
    StopEffect(0x5, 0x2)
    StopEffect(0x6, 0x2)
    OP_82(0x64, 0x64, 0xBB8, 0x1F4)
    OP_79(0x6)
    OP_6F(0x79)
    Sleep(1000)
    Fade(500)
    OP_68(-2300, 1100, 0, 0)
    MoveCamera(50, 19, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(14500, 0)
    OP_68(-4300, 1100, 0, 1500)
    SetCameraDistance(16000, 1500)
    OP_0D()
    Sound(145, 2, 100, 0)
    OP_74(0x6, 0xF)
    OP_71(0x6, 0xF1, 0xFD, 0x0, 0x0)
    OP_79(0x6)
    OP_24(0x91)
    Sound(143, 0, 100, 0)
    OP_74(0x6, 0x1E)
    OP_6F(0x79)

    ChrTalk(
        0x109,
        "#6P#N#10111FAh...\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x102,
        (
            "#6P#N#00101FIt's one of the Guardian\x01",
            "Force's!?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#00307F#6P#NBastards... Where the\x01",
            "heck did you get that\x01",
            "from!?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0xE,
        (
            "#12PHaha, we have quite the\x01",
            "useful comrade, you see!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "You can play with that\x01",
            "as much as you want!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6PNo further questions!\x01",
            "We're out of here!\x02",
        )
    )

    CloseMessageWindow()
    Sound(943, 2, 50, 0)
    BeginChrThread(0x16, 0, 0, 28)
    BeginChrThread(0xB, 3, 0, 27)
    BeginChrThread(0xC, 3, 0, 27)
    Sleep(100)
    BeginChrThread(0xF, 3, 0, 26)
    Sleep(100)
    BeginChrThread(0xD, 3, 0, 27)
    BeginChrThread(0x10, 3, 0, 27)
    Sleep(100)
    BeginChrThread(0x9, 3, 0, 26)
    Sleep(100)
    BeginChrThread(0xA, 3, 0, 26)
    BeginChrThread(0xE, 3, 0, 26)
    WaitChrThread(0x16, 3)

    def lambda_3583():
        OP_A6(0xFE, 0x0, 0x32, 0x2EE, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3583)
    Sleep(50)

    def lambda_359F():
        OP_A6(0xFE, 0x0, 0x32, 0x2EE, 0xBB8)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_359F)
    Sleep(50)

    def lambda_35BB():
        OP_A6(0xFE, 0x0, 0x32, 0x2EE, 0xBB8)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_35BB)
    Sleep(50)

    def lambda_35D7():
        OP_A6(0xFE, 0x0, 0x32, 0x2EE, 0xBB8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_35D7)
    Sleep(50)

    def lambda_35F3():
        OP_A6(0xFE, 0x0, 0x32, 0x2EE, 0xBB8)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_35F3)
    Sleep(50)

    def lambda_360F():
        OP_A6(0xFE, 0x0, 0x32, 0x2EE, 0xBB8)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_360F)
    Sleep(250)
    Fade(250)
    Sound(805, 0, 100, 0)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0x101, 0x25)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x27)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x29)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x2B)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x2D)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x2F)
    SetChrSubChip(0x105, 0x0)
    OP_0D()
    WaitChrThread(0x19, 3)

    ChrTalk(
        0x101,
        (
            "#6P#00010FTch... Everyone, can you\x01",
            "move!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#N#00107FYes... Somehow!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x103,
        "#00201F#6PI'm good here, too!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10304FIf we're lucky, we might\x01",
            "be able to beat it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#N#10107FAnyway, it's armored!\x01",
            "It's resistant to arts\x01",
            "too!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#00307F#6PLet's move and watch for\x01",
            "our chance!\x02",
        )
    )

    CloseMessageWindow()
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetCameraDistance(14000, 500)
    Sleep(500)
    EndChrThread(0x9, 0xFF)
    EndChrThread(0xA, 0xFF)
    EndChrThread(0xB, 0xFF)
    EndChrThread(0xC, 0xFF)
    EndChrThread(0xD, 0xFF)
    EndChrThread(0xE, 0xFF)
    EndChrThread(0xF, 0xFF)
    EndChrThread(0x10, 0xFF)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    OP_24(0x91)
    OP_24(0x3AF)
    Battle("BattleInfo_61C", 0x0, 0x0, 0x100, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    Call(0, 39)
    Return()

    # Function_20_2822 end

    def Function_21_3830(): pass

    label("Function_21_3830")

    Sleep(1500)
    OP_82(0x1F4, 0x1F4, 0xBB8, 0x3E8)
    Sound(196, 0, 100, 0)
    Sound(598, 0, 80, 0)
    Sleep(250)
    Sound(556, 0, 100, 0)
    Sound(250, 0, 100, 0)
    Sleep(750)
    Return()

    # Function_21_3830 end

    def Function_22_3863(): pass

    label("Function_22_3863")


    def lambda_3868():
        OP_A6(0xFE, 0x0, 0x32, 0x384, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3868)
    Sleep(500)
    SetChrSubChip(0xFE, 0x2)
    Sleep(80)
    SetChrSubChip(0xFE, 0x1)
    Sleep(80)
    Fade(250)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    OP_0D()
    Return()

    # Function_22_3863 end

    def Function_23_38A2(): pass

    label("Function_23_38A2")


    def lambda_38A7():
        OP_A6(0xFE, 0x0, 0x32, 0x384, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_38A7)
    Sleep(500)
    SetChrSubChip(0xFE, 0x2)
    Sleep(80)
    SetChrSubChip(0xFE, 0x1)
    Sleep(80)
    Fade(250)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    OP_0D()
    Return()

    # Function_23_38A2 end

    def Function_24_38E1(): pass

    label("Function_24_38E1")

    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)

    def lambda_38EE():
        OP_98(0xFE, 0x7D0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_38EE)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_24_38E1 end

    def Function_25_3910(): pass

    label("Function_25_3910")

    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x0)

    def lambda_391D():
        OP_98(0xFE, 0x7D0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_391D)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_25_3910 end

    def Function_26_393F(): pass

    label("Function_26_393F")

    OP_93(0xFE, 0x5A, 0x1F4)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)

    def lambda_3953():
        OP_98(0xFE, 0x9C40, 0x0, 0x0, 0x157C, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3953)
    Sleep(5000)

    def lambda_3970():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3970)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_26_393F end

    def Function_27_3981(): pass

    label("Function_27_3981")

    OP_93(0xFE, 0x5A, 0x1F4)
    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x0)

    def lambda_3995():
        OP_98(0xFE, 0x9C40, 0x0, 0x0, 0x157C, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3995)
    Sleep(5000)

    def lambda_39B2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_39B2)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_27_3981 end

    def Function_28_39C3(): pass

    label("Function_28_39C3")

    ClearChrFlags(0x16, 0x80)
    BeginChrThread(0x16, 3, 0, 29)
    Sleep(500)
    ClearChrFlags(0x18, 0x80)
    BeginChrThread(0x18, 3, 0, 31)
    Sleep(500)
    ClearChrFlags(0x17, 0x80)
    BeginChrThread(0x17, 3, 0, 30)
    Sleep(500)
    ClearChrFlags(0x19, 0x80)
    BeginChrThread(0x19, 3, 0, 32)
    Return()

    # Function_28_39C3 end

    def Function_29_39F9(): pass

    label("Function_29_39F9")


    def lambda_39FE():
        OP_96(0xFE, 0x0, 0x0, 0x2710, 0x157C, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_39FE)

    def lambda_3A18():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3A18)
    WaitChrThread(0xFE, 1)

    def lambda_3A2D():
        OP_95(0xFE, -1500, 0, 5300, 5500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3A2D)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xE1, 0x1F4)
    Return()

    # Function_29_39F9 end

    def Function_30_3A4E(): pass

    label("Function_30_3A4E")


    def lambda_3A53():
        OP_96(0xFE, 0x0, 0x0, 0x2710, 0x157C, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3A53)

    def lambda_3A6D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3A6D)
    WaitChrThread(0xFE, 1)

    def lambda_3A82():
        OP_95(0xFE, -2700, 0, 6700, 5500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3A82)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xE1, 0x1F4)
    Return()

    # Function_30_3A4E end

    def Function_31_3AA3(): pass

    label("Function_31_3AA3")


    def lambda_3AA8():
        OP_96(0xFE, 0x0, 0x0, 0x2710, 0x157C, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3AA8)

    def lambda_3AC2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3AC2)
    WaitChrThread(0xFE, 1)

    def lambda_3AD7():
        OP_95(0xFE, 400, 0, 6000, 5500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3AD7)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xE1, 0x1F4)
    Return()

    # Function_31_3AA3 end

    def Function_32_3AF8(): pass

    label("Function_32_3AF8")


    def lambda_3AFD():
        OP_96(0xFE, 0x0, 0x0, 0x2710, 0x157C, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3AFD)

    def lambda_3B17():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3B17)
    WaitChrThread(0xFE, 1)

    def lambda_3B2C():
        OP_95(0xFE, -800, 0, 7400, 5500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3B2C)
    WaitChrThread(0xFE, 1)
    OP_24(0x3AF)
    OP_93(0xFE, 0xE1, 0x1F4)
    Return()

    # Function_32_3AF8 end

    def Function_33_3B50(): pass

    label("Function_33_3B50")


    def lambda_3B55():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3B55)
    Sleep(200)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0x101, 0x34)
    SetChrSubChip(0x101, 0x2)

    def lambda_3B72():
        OP_9C(0xFE, 0xFFFFE69C, 0x0, 0x0, 0x258, 0x7D0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3B72)
    WaitChrThread(0x101, 1)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0xFE, 0x20)
    Return()

    # Function_33_3B50 end

    def Function_34_3B98(): pass

    label("Function_34_3B98")


    def lambda_3B9D():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3B9D)
    Sleep(200)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0x102, 0x35)
    SetChrSubChip(0x102, 0x2)

    def lambda_3BBA():
        OP_9C(0xFE, 0xFFFFE958, 0x0, 0xFFFFFCE0, 0x258, 0x7D0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3BBA)
    WaitChrThread(0x102, 1)
    SetChrSubChip(0x102, 0x0)
    ClearChrFlags(0xFE, 0x20)
    Return()

    # Function_34_3B98 end

    def Function_35_3BE0(): pass

    label("Function_35_3BE0")


    def lambda_3BE5():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3BE5)
    Sleep(200)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0x104, 0x37)
    SetChrSubChip(0x104, 0x2)

    def lambda_3C02():
        OP_9C(0xFE, 0xFFFFE958, 0x0, 0x320, 0x258, 0x7D0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3C02)
    WaitChrThread(0x104, 1)
    SetChrSubChip(0x104, 0x0)
    ClearChrFlags(0xFE, 0x20)
    Return()

    # Function_35_3BE0 end

    def Function_36_3C28(): pass

    label("Function_36_3C28")


    def lambda_3C2D():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3C2D)
    Sleep(200)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0x105, 0x39)
    SetChrSubChip(0x105, 0x2)

    def lambda_3C4A():
        OP_9C(0xFE, 0xFFFFE570, 0x0, 0x0, 0x258, 0x7D0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3C4A)
    WaitChrThread(0x105, 1)
    SetChrSubChip(0x105, 0x0)
    ClearChrFlags(0xFE, 0x20)
    Return()

    # Function_36_3C28 end

    def Function_37_3C70(): pass

    label("Function_37_3C70")


    def lambda_3C75():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3C75)
    Sleep(200)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0x109, 0x38)
    SetChrSubChip(0x109, 0x2)

    def lambda_3C92():
        OP_9C(0xFE, 0xFFFFEA20, 0x0, 0xFFFFFE70, 0x258, 0x7D0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3C92)
    WaitChrThread(0x109, 1)
    SetChrSubChip(0x109, 0x0)
    ClearChrFlags(0xFE, 0x20)
    Return()

    # Function_37_3C70 end

    def Function_38_3CB8(): pass

    label("Function_38_3CB8")


    def lambda_3CBD():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_3CBD)
    Sleep(200)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0x103, 0x36)
    SetChrSubChip(0x103, 0x2)
    Sound(809, 0, 100, 0)

    def lambda_3CE0():
        OP_9C(0xFE, 0xFFFFEA20, 0x0, 0x190, 0x258, 0x7D0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3CE0)
    WaitChrThread(0x103, 1)
    SetChrSubChip(0x103, 0x0)
    ClearChrFlags(0xFE, 0x20)
    Return()

    # Function_38_3CB8 end

    def Function_39_3D06(): pass

    label("Function_39_3D06")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    LoadChrToIndex("chr/ch02950.itc", 0x22)
    LoadChrToIndex("chr/ch03050.itc", 0x23)
    LoadEffect(0x0, "battle\\ms00103.eff ")
    SoundLoad(863)
    SoundLoad(864)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x22)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x23)
    SetChrSubChip(0x105, 0x0)
    SetChrPos(0x101, -4700, 0, 0, 90)
    SetChrPos(0x102, -4800, 0, -2500, 90)
    SetChrPos(0x103, -6100, 0, 1700, 90)
    SetChrPos(0x104, -4800, 0, 2500, 90)
    SetChrPos(0x109, -6100, 0, -1700, 90)
    SetChrPos(0x105, -6700, 0, 0, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrFlags(0x14, 0x80)
    SetMapObjFlags(0x6, 0x4)
    ClearMapObjFlags(0x6, 0x1000)
    SetChrFlags(0x8, 0x80)
    OP_78(0x9, 0x8)
    OP_49()
    ClearMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0x9, 0x1000)
    OP_74(0x9, 0x1E)
    OP_71(0x9, 0x79, 0xF0, 0x0, 0x20)
    SetMapObjFrame(0x9, "mark00", 0x1, 0x1)
    SetChrPos(0x8, 2000, 0, 1000, 180)
    OP_D5(0x8, 0x0, 0x222E0, 0x0, 0x0)
    OP_68(1500, 2100, 500, 0)
    MoveCamera(33, 37, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(14500, 0)
    FadeToBright(1000, 0)
    OP_0D()
    SetCameraDistance(15500, 2000)
    OP_82(0x12C, 0x12C, 0xBB8, 0x5DC)
    Sound(196, 0, 100, 0)
    Sound(598, 0, 100, 0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    PlayEffect(0x0, 0x0, 0xFF, 0x0, 2000, 1500, 1500, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    CancelBlur(1500)
    Sleep(200)
    Sound(556, 0, 100, 0)
    Sound(200, 0, 100, 0)
    Sleep(1300)
    OP_6F(0x79)
    OP_68(-2300, 900, 0, 2000)
    MoveCamera(50, 19, 0, 2000)
    SetCameraDistance(16000, 2000)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#6P#00013FAlright... Did we beat\x01",
            "it!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00107FWe've got to hurry and\x01",
            "save those on board!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x103,
        (
            "#6P#00206FNo. No lifeforms\x01",
            "detected inside.\x02\x03",
            "#00201FIt seems that it was\x01",
            "being controlled by an\x01",
            "autopilot.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x109,
        "#6P#N#10111FWhaaat!?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    Sound(531, 0, 100, 0)
    Sound(805, 0, 100, 0)
    OP_0D()

    def lambda_4084():
        TurnDirection(0x109, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_4084)
    Sleep(50)

    def lambda_4094():
        TurnDirection(0x102, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_4094)
    Sleep(50)

    def lambda_40A4():
        TurnDirection(0x101, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_40A4)
    Sleep(50)

    def lambda_40B4():
        TurnDirection(0x104, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_40B4)
    Sleep(50)

    def lambda_40C4():
        TurnDirection(0x105, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_40C4)
    Sleep(50)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x104,
        "#00306F#5PWhoa, seriously?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10301FThey had those archaisms\x01",
            "too. They've certainly\x01",
            "got some strange allies.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)
    Sleep(150)

    ChrTalk(
        0x101,
        (
            "#5P#00003FWe'll talk later!\x02\x03",
            "#00013FWe've gotta chase after\x01",
            "those─\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0x1770)
    Sound(863, 2, 50, 0)
    Sleep(300)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_425B():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_425B)

    def lambda_4268():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_4268)

    def lambda_4275():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_4275)

    def lambda_4282():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_4282)

    def lambda_428F():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_428F)
    OP_68(32500, 900, 0, 3000)
    OP_6F(0x79)
    MoveCamera(55, 23, 0, 4500)
    SetCameraDistance(19500, 4000)
    Sound(864, 2, 60, 0)
    OP_82(0x32, 0x32, 0xBB8, 0x1F4)
    Sleep(1500)
    OP_82(0x32, 0x32, 0xBB8, 0x1F4)
    Sleep(1500)
    OP_82(0x32, 0x32, 0xBB8, 0x1F4)
    Sleep(1500)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#00010F#6P#N!?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x103,
        "#00210F#6P#N......\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x109,
        "#10107F#6P#NGunfire!?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        "#00108F#6P#NWhat in the world...?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        "#00307F#6P#N...Anyway, let's go!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrFlags(0x14, 0x80)
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    OP_D7(0x22)
    OP_D7(0x23)
    OP_37()
    SetChrPos(0x0, -4000, 0, 0, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x143, 7)
    OP_29(0xA4, 0x1, 0x9)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7561", 0)
    ReplaceBGM("ed7300", "ed7561")
    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_39_3D06 end

    def Function_40_43FF(): pass

    label("Function_40_43FF")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch42300.itc", 0x1E)
    LoadChrToIndex("chr/ch42351.itc", 0x1F)
    LoadChrToIndex("chr/ch42352.itc", 0x20)
    LoadChrToIndex("chr/ch42353.itc", 0x21)
    LoadChrToIndex("chr/ch03300.itc", 0x22)
    LoadChrToIndex("chr/ch03400.itc", 0x23)
    LoadChrToIndex("chr/ch41900.itc", 0x24)
    LoadChrToIndex("chr/ch41950.itc", 0x25)
    LoadChrToIndex("chr/ch41951.itc", 0x26)
    LoadChrToIndex("chr/ch41952.itc", 0x27)
    LoadChrToIndex("apl/ch51244.itc", 0x28)
    LoadChrToIndex("apl/ch51217.itc", 0x29)
    LoadChrToIndex("apl/ch51221.itc", 0x2A)
    LoadChrToIndex("chr/ch02952.itc", 0x2B)
    LoadChrToIndex("chr/ch42253.itc", 0x2C)
    LoadChrToIndex("apl/ch51246.itc", 0x2D)
    LoadChrToIndex("apl/ch51247.itc", 0x2E)
    LoadChrToIndex("apl/ch51248.itc", 0x2F)
    LoadChrToIndex("apl/ch51249.itc", 0x30)
    LoadChrToIndex("apl/ch51250.itc", 0x31)
    LoadChrToIndex("apl/ch51251.itc", 0x32)
    LoadChrToIndex("apl/ch51252.itc", 0x33)
    LoadChrToIndex("apl/ch51253.itc", 0x34)
    LoadChrToIndex("apl/ch51254.itc", 0x35)
    LoadChrToIndex("apl/ch51219.itc", 0x36)
    LoadEffect(0x0, "event/ev12000.eff")
    LoadEffect(0x1, "battle/btgun00.eff")
    LoadEffect(0x2, "event/ev606_00.eff")
    LoadEffect(0x3, "event/eva00_00.eff")
    LoadEffect(0x4, "event/ev12002.eff")
    SoundLoad(860)
    SoundLoad(861)
    SoundLoad(2754)
    SoundLoad(2755)
    SoundLoad(4117)
    SoundLoad(3950)
    SoundLoad(3951)
    SoundLoad(3952)
    SetChrPos(0x101, 116000, 0, -700, 90)
    SetChrPos(0x102, 114900, 0, 1300, 90)
    SetChrPos(0x103, 114900, 0, -1200, 90)
    SetChrPos(0x104, 116000, 0, 600, 90)
    SetChrPos(0x109, 113800, 0, -700, 90)
    SetChrPos(0x105, 113800, 0, 600, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x9, 0x2C)
    SetChrSubChip(0x9, 0x3)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 171200, 0, 10000, 180)
    SetChrChipByIndex(0xA, 0x28)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 168700, 0, 12900, 270)
    OP_52(0xA, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xB, 0x28)
    SetChrSubChip(0xB, 0x2)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, 167800, 0, 10200, 150)
    OP_52(0xB, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xC, 0x28)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, 169900, 0, 11400, 170)
    OP_52(0xC, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xD, 0x28)
    SetChrSubChip(0xD, 0x1)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    SetChrPos(0xD, 173000, 0, 10800, 305)
    OP_52(0xD, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xE, 0x28)
    SetChrSubChip(0xE, 0x1)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)
    SetChrPos(0xE, 173400, 0, 12700, 90)
    OP_52(0xE, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xF, 0x28)
    SetChrSubChip(0xF, 0x3)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xF, 166300, 0, 12100, 90)
    OP_52(0xF, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x10, 0x1E)
    SetChrSubChip(0x10, 0x0)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x8000)
    SetChrPos(0x10, 178800, 0, 12500, 180)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8000)
    SetChrChipByIndex(0x11, 0x22)
    SetChrSubChip(0x11, 0x0)
    SetChrPos(0x11, 170300, 0, 2300, 0)
    OP_52(0x11, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8000)
    SetChrChipByIndex(0x12, 0x23)
    SetChrSubChip(0x12, 0x0)
    SetChrPos(0x12, 171400, 0, 1500, 0)
    OP_52(0x12, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8000)
    SetChrChipByIndex(0x13, 0x24)
    SetChrSubChip(0x13, 0x0)
    SetChrPos(0x13, 169200, 0, 1100, 0)
    ClearChrFlags(0x1A, 0x80)
    SetChrFlags(0x1A, 0x8000)
    SetChrChipByIndex(0x1A, 0x27)
    SetChrSubChip(0x1A, 0x1)
    SetChrPos(0x1A, 171200, 0, 5400, 0)
    ClearChrFlags(0x1B, 0x80)
    SetChrFlags(0x1B, 0x8000)
    SetChrChipByIndex(0x1B, 0x27)
    SetChrSubChip(0x1B, 0x1)
    SetChrPos(0x1B, 167900, 0, 4800, 0)
    ClearChrFlags(0x1C, 0x80)
    SetChrFlags(0x1C, 0x8000)
    SetChrChipByIndex(0x1C, 0x27)
    SetChrSubChip(0x1C, 0x1)
    SetChrPos(0x1C, 172000, 0, 3900, 0)
    ClearChrFlags(0x1D, 0x80)
    SetChrFlags(0x1D, 0x8000)
    SetChrChipByIndex(0x1D, 0x27)
    SetChrSubChip(0x1D, 0x1)
    SetChrPos(0x1D, 169200, 0, 3700, 0)
    ClearChrFlags(0x1E, 0x80)
    SetChrFlags(0x1E, 0x8000)
    SetChrChipByIndex(0x1E, 0x27)
    SetChrSubChip(0x1E, 0x1)
    SetChrPos(0x1E, 173700, 0, 5300, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 169200, 0, 13900, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0x0, 0x1A, 0x3, -100, 1100, 1150, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0x1, 0x1B, 0x3, -100, 1100, 1150, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0x2, 0x1C, 0x3, -100, 1100, 1150, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0x3, 0x1D, 0x3, -100, 1100, 1150, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0x4, 0x1E, 0x3, -100, 1100, 1150, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_68(121500, 1300, 0, 0)
    MoveCamera(35, 19, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(17500, 0)

    def lambda_49B5():
        OP_97(0xFE, 0x2EE0, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_49B5)
    Sleep(200)

    def lambda_49D2():
        OP_97(0x101, 0x2710, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_49D2)
    Sleep(150)

    def lambda_49EF():
        OP_97(0x102, 0x2710, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_49EF)
    Sleep(150)

    def lambda_4A0C():
        OP_97(0x103, 0x2710, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_4A0C)
    Sleep(150)

    def lambda_4A29():
        OP_97(0x105, 0x2710, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_4A29)
    Sleep(150)

    def lambda_4A46():
        OP_97(0x109, 0x2710, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_4A46)
    OP_68(126500, 1300, 0, 2000)
    SetCameraDistance(16500, 2000)
    BeginChrThread(0x20, 1, 0, 53)
    FadeToBright(1000, 0)
    StopBGM(0x7D0)
    WaitChrThread(0x104, 1)

    ChrTalk(
        0x104,
        "#5P#00305F...!\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x103,
        "#6P#00210F...Ah...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00007F#6PWha!?\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7582", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x246), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    StopSound(863, 2000, 100)
    OP_68(146500, 1300, 0, 3000)
    Sleep(2000)
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_68(169500, 900, 11500, 0)
    MoveCamera(65, 15, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(14000, 0)
    MoveCamera(50, 30, 0, 9000)
    SetCameraDistance(17000, 9000)
    FadeToBright(2000, 0)
    OP_6F(0x79)
    Fade(1000)
    OP_68(170500, 700, 9000, 0)
    MoveCamera(0, 17, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(14000, 0)
    SetCameraDistance(21000, 4000)
    OP_6F(0x79)
    Sleep(1000)
    Fade(500)
    OP_68(171160, 900, 8200, 0)
    MoveCamera(45, 17, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(19500, 0)
    BeginChrThread(0xF, 3, 0, 52)
    OP_68(171200, 900, 7200, 1500)
    OP_0D()
    OP_6F(0x79)

    def lambda_4BE8():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_4BE8)
    Sleep(500)

    ChrTalk(
        0x9,
        (
            "#5P#50W#2S...*gah*... *cough,\x01",
            "cough*...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P#50W#2SRed Constellation!? Why\x01",
            "are you here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#11P#04504FWell, this is in the\x01",
            "contract too.\x02\x03",
            "#04502FWe've already sent the\x01",
            "guys who destroyed the\x01",
            "anti-air radar to Aidios.\x02\x03",
            "Die without worry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P#60W#2S...Damn...... Too...\x01",
            "bad...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4D28():
        OP_A6(0xFE, 0x0, 0x32, 0x2EE, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_4D28)
    Sleep(500)
    Fade(250)
    Sound(514, 0, 100, 0)
    SetChrChipByIndex(0x9, 0x28)
    SetChrSubChip(0x9, 0x2)
    OP_52(0x9, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1000)

    ChrTalk(
        0x11,
        (
            "#11P#04504FShirley. You can kill\x01",
            "whoever's left.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x12, 0x11, 500)

    ChrTalk(
        0x12,
        "#04602F#11PEhehe, can I?\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x10,
        "Voice",
        "#2SEek!\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x10, 3, 0, 45)
    OP_68(178800, 1100, 9750, 3000)
    MoveCamera(13, 13, 0, 3000)
    SetCameraDistance(19000, 3000)
    OP_92(0x12, 0x2BA70, 0x1770, 0x1F4)

    def lambda_4E0B():
        OP_95(0xFE, 178800, 0, 6000, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_4E0B)
    Sleep(1000)
    BeginChrThread(0x1E, 3, 0, 44)
    WaitChrThread(0x12, 1)

    def lambda_4E32():
        OP_95(0xFE, 178800, 0, 7000, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_4E32)
    WaitChrThread(0x12, 1)
    OP_6F(0x79)
    SetChrChipByIndex(0x1A, 0x24)
    SetChrSubChip(0x1A, 0x0)
    SetChrPos(0x1A, 170200, 0, 5400, 90)
    SetChrChipByIndex(0x1C, 0x24)
    SetChrSubChip(0x1C, 0x0)
    SetChrPos(0x1C, 171000, 0, 3900, 90)
    Sound(859, 0, 100, 0)
    Sound(802, 0, 100, 0)
    PlayEffect(0x3, 0x0, 0x12, 0x3, 600, 1000, 100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrFlags(0x12, 0x2)
    SetChrFlags(0x12, 0x10)
    SetChrFlags(0x12, 0x20)
    SetChrChipByIndex(0x12, 0x2D)
    SetChrSubChip(0x12, 0x0)
    Sleep(500)
    StopEffect(0x0, 0x2)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x12,
        (
            "#12P#04611F#3950V#30WHaha, how do ya like\x01",
            "that!?\x02\x03",
            "#04602F#3951VI'll take all of you\x01",
            "myself. Why don't you\x01",
            "show me what you've got?\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xF6F)
    OP_C9(0x1, 0x80000000)

    ChrTalk(
        0x10,
        "#5PU-Uuuh...\x02",
    )

    CloseMessageWindow()
    EndChrThread(0x10, 0x3)
    Sleep(500)
    SetChrChipByIndex(0x10, 0x20)
    SetChrSubChip(0x10, 0x0)
    Sleep(100)
    Sound(531, 0, 100, 0)
    SetChrSubChip(0x10, 0x1)
    Sleep(100)
    SetChrSubChip(0x10, 0x2)
    OP_82(0xC8, 0x0, 0xBB8, 0x1F4)

    ChrTalk(
        0x10,
        "#4S#5PUwaaaah!!!\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x11, 3, 0, 42)
    BeginChrThread(0x10, 3, 0, 41)
    BeginChrThread(0x12, 3, 0, 43)
    WaitChrThread(0x10, 3)
    WaitChrThread(0x12, 3)
    Sound(859, 0, 100, 0)
    PlayEffect(0x3, 0x0, 0x12, 0x3, 300, 900, 800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    StopEffect(0x0, 0x2)

    ChrTalk(
        0x10,
        "#12PAh─\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(14000, 500)
    Sleep(200)
    Sound(802, 0, 100, 0)
    SetChrSubChip(0x12, 0x1)
    OP_6F(0x79)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x12,
        "#04609F#3952V#5P#40WHaha. Bye bye, then.\x02",
    )

    CloseMessageWindow()
    OP_24(0xF70)
    OP_57(0x0)
    OP_5A()
    OP_82(0xC8, 0x0, 0xBB8, 0x1F4)

    ChrTalk(
        0x104,
        "#00310F#2754V#4S#6P#NStooop!!\x02",
    )

    CloseMessageWindow()
    OP_24(0xAC2)
    OP_C9(0x1, 0x80000000)
    OP_63(0x12, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Fade(500)
    OP_68(158000, 1100, 2500, 0)
    MoveCamera(43, 21, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(15500, 0)
    SetChrChipByIndex(0x1A, 0x24)
    SetChrSubChip(0x1A, 0x0)
    SetChrChipByIndex(0x1B, 0x24)
    SetChrSubChip(0x1B, 0x0)
    SetChrChipByIndex(0x1C, 0x24)
    SetChrSubChip(0x1C, 0x0)
    SetChrChipByIndex(0x1D, 0x24)
    SetChrSubChip(0x1D, 0x0)
    SetChrChipByIndex(0x1E, 0x24)
    SetChrSubChip(0x1E, 0x0)
    SetChrPos(0x1A, 171200, 0, 5400, 0)
    SetChrPos(0x1B, 168400, 0, 4800, 0)
    SetChrPos(0x1C, 172000, 0, 3900, 0)
    SetChrPos(0x1D, 169700, 0, 3700, 0)
    SetChrPos(0x1E, 173200, 0, 5300, 0)

    def lambda_5196():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_5196)

    def lambda_51A3():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1B, 2, lambda_51A3)

    def lambda_51B0():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1C, 2, lambda_51B0)

    def lambda_51BD():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1D, 2, lambda_51BD)

    def lambda_51CA():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1E, 2, lambda_51CA)
    SetChrSubChip(0x12, 0x2)
    SetChrPos(0x101, 150000, 0, 2000, 90)
    SetChrPos(0x102, 150000, 0, 4000, 90)
    SetChrPos(0x103, 150000, 0, 3800, 90)
    SetChrPos(0x104, 150000, 0, 2600, 90)
    SetChrPos(0x109, 150000, 0, 5100, 90)
    SetChrPos(0x105, 150000, 0, 4600, 90)
    OP_68(166000, 1100, 4500, 4000)
    MoveCamera(43, 16, 0, 4000)
    SetCameraDistance(16500, 4000)

    def lambda_5266():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_5266)

    def lambda_5273():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_5273)
    BeginChrThread(0x104, 3, 0, 46)
    Sleep(600)
    BeginChrThread(0x101, 3, 0, 47)
    Sleep(200)
    BeginChrThread(0x109, 3, 0, 49)

    def lambda_5298():
        OP_96(0xFE, 0x28E4C, 0x0, 0xA28, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_5298)
    Sleep(400)
    BeginChrThread(0x102, 3, 0, 48)
    Sleep(400)
    BeginChrThread(0x105, 3, 0, 50)
    Sleep(400)
    BeginChrThread(0x103, 3, 0, 51)

    def lambda_52CD():
        OP_96(0xFE, 0x29234, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_52CD)
    Sleep(1600)

    ChrTalk(
        0x12,
        (
            "#04605F#12PMy, it seems we've been\x01",
            "interrupted.\x02",
        )
    )

    WaitChrThread(0x103, 3)
    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    WaitChrThread(0x13, 1)

    ChrTalk(
        0x13,
        "#11PYoung master...\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x11, 1)

    ChrTalk(
        0x11,
        (
            "#04504F#11PHehe, took you long\x01",
            "enough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00311F#30WUncle... Shirley...\x02\x03",
            "#30WWhat the heck are you\x01",
            "doin' here!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5P#00108FI-It's no use...\x02",
    )

    CloseMessageWindow()

    def lambda_53E2():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_53E2)
    Sleep(50)

    def lambda_53F2():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_53F2)

    ChrTalk(
        0x105,
        (
            "#5P#10303FLooks like they're all\x01",
            "dead.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#00210F......\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10110F#12PGuh...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x11, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        "#6P#00015F#30WWhat's with you guys...\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0xC8, 0x0, 0xBB8, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#6P#00007F#4SWhy do such a cruel\x01",
            "thing!?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_54CF():
        TurnDirection(0xFE, 0x11, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_54CF)

    def lambda_54DC():
        TurnDirection(0xFE, 0x11, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_54DC)

    ChrTalk(
        0x11,
        (
            "#04504F#11PI told you before, didn't I?\x01",
            "It's just business.\x02\x03",
            "Execute the terrorists\x01",
            "attempting to kill the\x01",
            "chancellor and royal family...\x02\x03",
            "#04502FThat was the order we received\x01",
            "from the Imperial government\x01",
            "this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00011F...!?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)

    def lambda_55E7():
        TurnDirection(0xFE, 0x11, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_55E7)
    Sound(812, 0, 100, 0)
    Sleep(100)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    TurnDirection(0x105, 0x11, 500)

    ChrTalk(
        0x102,
        "#5P#00107FI-Impossible...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#04609F#12PNope, we even got this\x01",
            "authorization letter from\x01",
            "the Imperial government.\x02\x03",
            "#04611FSince we've got it, you\x01",
            "guys can't interfere,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x109,
        "#10108F#5PN-No way...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#00108FState code, article 19, paragraph 3...\x02\x03",
            "#00110FThe right of the Imperial and Republican\x01",
            "governments to perform official duties\x01",
            "in Crossbell is hereby recognized...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#04504FHehe, exactly.\x02\x03",
            "#04500FIn short, we're agents of\x01",
            "the Imperial government with\x01",
            "regard to this matter...\x02\x03",
            "We're official executioners.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00010FUgh!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#5P#10301FYou guys are crazy\x01",
            "prepared...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0xC8, 0x0, 0xBB8, 0x1F4)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x104,
        "#6P#00310F#2755V#4S#10A...Uncle!!\x02",
    )

    Sleep(500)
    OP_68(167150, 1100, 2600, 1000)
    MoveCamera(34, 19, 0, 1000)
    SetCameraDistance(14000, 1000)

    def lambda_58CD():
        OP_95(0xFE, 166800, 0, 2600, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_58CD)
    WaitChrThread(0x104, 1)
    Sound(802, 0, 100, 0)
    Fade(100)
    Sound(811, 0, 100, 0)
    SetChrFlags(0x104, 0x2)
    SetChrFlags(0x104, 0x10)
    SetChrFlags(0x104, 0x20)
    SetChrChipByIndex(0x104, 0x30)
    SetChrSubChip(0x104, 0x0)
    SetChrFlags(0x11, 0x2)
    SetChrFlags(0x11, 0x10)
    SetChrFlags(0x11, 0x20)
    SetChrChipByIndex(0x11, 0x31)
    SetChrSubChip(0x11, 0x0)

    def lambda_592A():

        label("loc_592A")

        TurnDirection(0xFE, 0x104, 500)
        Yield()
        Jump("loc_592A")

    QueueWorkItem2(0x101, 2, lambda_592A)

    def lambda_593C():

        label("loc_593C")

        TurnDirection(0xFE, 0x104, 500)
        Yield()
        Jump("loc_593C")

    QueueWorkItem2(0x102, 2, lambda_593C)

    def lambda_594E():

        label("loc_594E")

        TurnDirection(0xFE, 0x104, 500)
        Yield()
        Jump("loc_594E")

    QueueWorkItem2(0x103, 2, lambda_594E)

    def lambda_5960():

        label("loc_5960")

        TurnDirection(0xFE, 0x104, 500)
        Yield()
        Jump("loc_5960")

    QueueWorkItem2(0x109, 2, lambda_5960)

    def lambda_5972():

        label("loc_5972")

        TurnDirection(0xFE, 0x104, 500)
        Yield()
        Jump("loc_5972")

    QueueWorkItem2(0x105, 2, lambda_5972)

    def lambda_5984():

        label("loc_5984")

        TurnDirection(0xFE, 0x104, 500)
        Yield()
        Jump("loc_5984")

    QueueWorkItem2(0x13, 2, lambda_5984)
    OP_0D()
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
    OP_6F(0x79)
    OP_C9(0x1, 0x80000000)

    ChrTalk(
        0x104,
        (
            "#6P#00307FWhy did you kill them!?\x01",
            "Why the fuck did you\x01",
            "kill them!?\x02\x03",
            "You could've easily\x01",
            "incapacitated them\x01",
            "instead!\x02\x03",
            "Why!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#11P#04501F...............\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(13000, 800)
    OP_57(0x0)
    OP_5A()
    Fade(300)
    Sound(802, 0, 100, 0)
    Sound(3824, 255, 100, 0)
    SetChrChipByIndex(0x11, 0x32)
    SetChrSubChip(0x11, 0x0)
    OP_6F(0x79)
    Sleep(150)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    Sound(534, 0, 100, 0)
    SetChrSubChip(0x11, 0x1)
    Sleep(60)
    Sound(815, 0, 100, 0)
    SetChrSubChip(0x11, 0x2)
    OP_82(0xC8, 0xC8, 0xBB8, 0x12C)
    OP_68(165800, 1100, 2600, 500)
    SetCameraDistance(14500, 500)
    SetChrChipByIndex(0x104, 0x33)
    SetChrSubChip(0x104, 0x2)
    Sound(809, 0, 100, 0)

    def lambda_5B46():
        OP_9D(0xFE, 0x28104, 0x0, 0x8FC, 0x12C, 0x5DC)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5B46)
    WaitChrThread(0x104, 1)
    Sound(862, 0, 100, 0)
    CancelBlur(0)
    SetChrChipByIndex(0x1F, 0x33)
    SetChrSubChip(0x1F, 0x0)
    SetChrPos(0x1F, 164400, -50, 2800, 0)
    OP_52(0x1F, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x1F, 0x80)
    SetChrFlags(0x1F, 0x8000)
    SetChrSubChip(0x104, 0x0)
    OP_52(0x104, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x104, 0x1)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x109, 0x2)
    EndChrThread(0x105, 0x2)
    EndChrThread(0x13, 0x2)

    def lambda_5BF8():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_5BF8)
    Sleep(50)
    Sound(811, 0, 100, 0)
    Sleep(150)
    Sound(2764, 255, 100, 0)

    ChrTalk(
        0x104,
        "#6P#8AGah!\x02",
    )

    CloseMessageWindow()

    def lambda_5C33():
        OP_95(0xFE, 164000, 0, 3900, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5C33)
    Sleep(100)

    def lambda_5C50():
        OP_95(0xFE, 162800, 0, 3000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5C50)
    WaitChrThread(0x101, 1)

    def lambda_5C6E():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5C6E)
    WaitChrThread(0x103, 1)
    TurnDirection(0x103, 0x104, 500)

    ChrTalk(
        0x101,
        "#00007F#5PRandy!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#5P#10111FRandy!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#5P#00201FRandy!\x02",
    )

    CloseMessageWindow()
    Sound(802, 0, 100, 0)

    def lambda_5CCE():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_5CCE)
    Sleep(500)
    SetChrSubChip(0x104, 0x1)
    Sleep(500)
    Fade(250)
    SetChrChipByIndex(0x11, 0x22)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x11, 0x2)
    ClearChrFlags(0x11, 0x10)
    ClearChrFlags(0x11, 0x20)
    OP_0D()

    ChrTalk(
        0x11,
        (
            "#04503F#11PI just told you. The\x01",
            "contract was for an\x01",
            ""execution".\x02\x03",
            "#04501FAnd besides, this level\x01",
            "of killing isn't so rare\x01",
            "for you, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00310F......\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#04503F#11PAnd, if you guys had caught\x01",
            "them in the first place, it\x01",
            "wouldn't have ended this way.\x02\x03",
            "#04502F─This result will be used\x01",
            "politically for the Blood and\x01",
            "Iron as well.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5E68():
        TurnDirection(0x101, 0x11, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_5E68)
    Sleep(50)

    def lambda_5E78():
        TurnDirection(0x102, 0x11, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_5E78)
    Sleep(50)

    def lambda_5E88():
        TurnDirection(0x109, 0x11, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_5E88)
    Sleep(50)

    def lambda_5E98():
        TurnDirection(0x103, 0x11, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_5E98)
    Sleep(50)

    def lambda_5EA8():
        TurnDirection(0x105, 0x11, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_5EA8)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x105, 0)
    OP_82(0x32, 0x0, 0xBB8, 0xC8)

    ChrTalk(
        0x101,
        "#00007F#5P!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5P#N#00108FNo... There's no way..\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x11,
        (
            "#04504F#11PHaha, well I have a\x01",
            "minimum of compassion, so\x01",
            "I'll let one of them go.\x02\x03",
            "#04500FLet 'em go, Shirley.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#04606FAww, what a waste.\x02\x03",
            "#04600FWell, whatever. It's no\x01",
            "fun playing with small\x01",
            "fry.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(174300, 1100, 7300, 0)
    MoveCamera(47, 21, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(18500, 0)
    ClearChrFlags(0x12, 0x2)
    ClearChrFlags(0x12, 0x10)
    ClearChrFlags(0x12, 0x20)
    SetChrChipByIndex(0x12, 0x23)
    SetChrSubChip(0x12, 0x0)
    SetChrChipByIndex(0x10, 0x1E)
    SetChrSubChip(0x10, 0x0)
    OP_A7(0x10, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrPos(0x10, 177000, 0, 6500, 180)

    def lambda_605A():

        label("loc_605A")

        TurnDirection(0xFE, 0x12, 500)
        Yield()
        Jump("loc_605A")

    QueueWorkItem2(0x109, 2, lambda_605A)

    def lambda_606C():

        label("loc_606C")

        TurnDirection(0xFE, 0x12, 500)
        Yield()
        Jump("loc_606C")

    QueueWorkItem2(0x102, 2, lambda_606C)

    def lambda_607E():

        label("loc_607E")

        TurnDirection(0xFE, 0x12, 500)
        Yield()
        Jump("loc_607E")

    QueueWorkItem2(0x105, 2, lambda_607E)
    OP_0D()
    OP_68(169300, 1100, 7600, 3500)
    SetCameraDistance(20500, 3500)

    def lambda_60AB():
        OP_9E(0xFE, 0x2B368, 0x1C84, 0x15F90, 0x1388, 0x3)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_60AB)

    def lambda_60C6():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_60C6)
    Sound(802, 0, 100, 0)
    WaitChrThread(0x10, 1)

    def lambda_60DD():
        OP_98(0xFE, 0xFFFFE890, 0x0, 0x12C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_60DD)

    def lambda_60F7():
        OP_98(0xFE, 0xFFFFE890, 0x0, 0x12C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_60F7)
    WaitChrThread(0x10, 1)
    WaitChrThread(0x12, 1)
    OP_52(0x10, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TurnDirection(0x10, 0x12, 0)
    SetChrChipByIndex(0x10, 0x21)
    SetChrSubChip(0x10, 0x0)
    Sound(809, 0, 100, 0)
    Sound(811, 0, 100, 0)

    def lambda_613F():
        OP_9D(0xFE, 0x28AC8, 0x0, 0x1E14, 0x2BC, 0x7D0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_613F)
    WaitChrThread(0x10, 1)
    Sound(862, 0, 80, 0)
    OP_82(0x64, 0x64, 0xBB8, 0x12C)
    OP_93(0x10, 0x10E, 0x0)
    SetChrChipByIndex(0x10, 0x28)
    SetChrSubChip(0x10, 0x3)
    OP_52(0x10, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x578), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x578), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)

    ChrTalk(
        0x12,
        (
            "#11P#04612FHere, take him. Don't\x01",
            "run away, ok?\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x10, 0x2)
    SetChrFlags(0x10, 0x10)
    SetChrFlags(0x10, 0x20)
    SetChrChipByIndex(0x10, 0x34)
    SetChrSubChip(0x10, 0x0)

    def lambda_61F5():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_61F5)

    ChrTalk(
        0x10,
        "#5PE-Eeek...\x02",
    )

    CloseMessageWindow()

    def lambda_6220():
        OP_96(0xFE, 0x288D4, 0x0, 0x1964, 0x1388, 0x1)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6220)
    WaitChrThread(0x109, 1)

    def lambda_623E():
        OP_96(0xFE, 0x28EB0, 0x0, 0x1D4C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_623E)
    WaitChrThread(0x109, 1)

    def lambda_625C():

        label("loc_625C")

        TurnDirection(0xFE, 0x12, 500)
        Yield()
        Jump("loc_625C")

    QueueWorkItem2(0x109, 2, lambda_625C)

    ChrTalk(
        0x109,
        "#6P#10110FUgh!\x02",
    )

    CloseMessageWindow()
    OP_68(165800, 1500, 2600, 2000)
    MoveCamera(34, 19, 0, 2000)
    OP_6E(650, 2000)
    SetCameraDistance(14500, 2000)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#00013F#6P............\x02",
    )

    CloseMessageWindow()
    OP_93(0x11, 0x2D, 0x1F4)
    Sleep(150)

    ChrTalk(
        0x11,
        (
            "#6P#04504FAlright, we're pulling\x01",
            "out.\x02\x03",
            "#04512FWe're getting our fee\x01",
            "too, so there'll be a\x01",
            "party tonight!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6346():
        TurnDirection(0x13, 0x11, 500)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_6346)
    Sleep(50)

    def lambda_6356():
        TurnDirection(0x1A, 0x11, 500)
        ExitThread()

    QueueWorkItem(0x1A, 0, lambda_6356)
    Sleep(50)

    def lambda_6366():
        TurnDirection(0x1B, 0x11, 500)
        ExitThread()

    QueueWorkItem(0x1B, 0, lambda_6366)
    Sleep(50)

    def lambda_6376():
        TurnDirection(0x1C, 0x11, 500)
        ExitThread()

    QueueWorkItem(0x1C, 0, lambda_6376)
    Sleep(50)

    def lambda_6386():
        TurnDirection(0x1D, 0x11, 500)
        ExitThread()

    QueueWorkItem(0x1D, 0, lambda_6386)
    Sleep(50)

    def lambda_6396():
        TurnDirection(0x1E, 0x11, 500)
        ExitThread()

    QueueWorkItem(0x1E, 0, lambda_6396)
    WaitChrThread(0x13, 0)
    WaitChrThread(0x1A, 0)
    WaitChrThread(0x1B, 0)
    WaitChrThread(0x1C, 0)
    WaitChrThread(0x1D, 0)
    WaitChrThread(0x1E, 0)
    Sleep(100)
    SetMessageWindowPos(300, 40, -1, -1)
    SetChrName("Jaegers")
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)

    AnonymousTalk(
        0xFF,
        "#4SJaー!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x12,
        "#11P#N#04609FLater, guys!\x02",
    )

    CloseMessageWindow()
    OP_93(0x13, 0x10E, 0x1F4)

    ChrTalk(
        0x13,
        "#11PExcuse us, young master.\x02",
    )

    CloseMessageWindow()
    OP_93(0x1B, 0x10E, 0x1F4)

    NpcTalk(
        0x1B,
        "Jaeger Sachs",
        (
            "#11PSee ya. Captain\x01",
            "Randolph.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_647A():

        label("loc_647A")

        TurnDirection(0xFE, 0x11, 500)
        Yield()
        Jump("loc_647A")

    QueueWorkItem2(0x101, 2, lambda_647A)

    def lambda_648C():

        label("loc_648C")

        TurnDirection(0xFE, 0x11, 500)
        Yield()
        Jump("loc_648C")

    QueueWorkItem2(0x102, 2, lambda_648C)

    def lambda_649E():

        label("loc_649E")

        TurnDirection(0xFE, 0x11, 500)
        Yield()
        Jump("loc_649E")

    QueueWorkItem2(0x103, 2, lambda_649E)

    def lambda_64B0():

        label("loc_64B0")

        TurnDirection(0xFE, 0x11, 500)
        Yield()
        Jump("loc_64B0")

    QueueWorkItem2(0x105, 2, lambda_64B0)
    OP_93(0x11, 0xB4, 0x1F4)
    OP_68(165800, 1500, -400, 5000)
    MoveCamera(23, 13, 0, 5000)

    def lambda_64E5():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFCD38, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_64E5)
    Sleep(1300)

    def lambda_6502():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFCD38, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_6502)

    def lambda_651C():
        OP_97(0x1A, 0x0, 0x0, 0xFFFFCD38, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 0, lambda_651C)
    Sleep(100)

    def lambda_6539():
        OP_97(0x1B, 0x0, 0x0, 0xFFFFCD38, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 0, lambda_6539)
    Sleep(100)

    def lambda_6556():
        OP_97(0x1C, 0x0, 0x0, 0xFFFFCD38, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 0, lambda_6556)
    Sleep(100)

    def lambda_6573():
        OP_97(0x1D, 0x0, 0x0, 0xFFFFCD38, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 0, lambda_6573)
    Sleep(100)

    def lambda_6590():
        OP_97(0x1E, 0x0, 0x0, 0xFFFFCD38, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 0, lambda_6590)

    def lambda_65AA():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFCD38, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_65AA)
    WaitChrThread(0x11, 1)
    WaitChrThread(0x13, 1)
    WaitChrThread(0x12, 1)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x109, 0x2)
    EndChrThread(0x105, 0x2)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x1D, 0x80)
    SetChrFlags(0x1E, 0x80)
    OP_68(164100, 1000, 2300, 2000)
    MoveCamera(23, 23, 0, 2000)
    SetCameraDistance(14000, 2000)
    Sleep(1750)

    def lambda_6634():
        OP_A6(0xFE, 0x0, 0x32, 0x4E2, 0xBB8)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_6634)
    Sleep(500)
    Fade(250)
    SetChrChipByIndex(0x104, 0x36)
    SetChrSubChip(0x104, 0x3)
    SetChrFlags(0x104, 0x1)
    OP_52(0x104, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x1F, 0x80)
    OP_0D()
    Sleep(500)
    Fade(500)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0x104, 0x35)
    SetChrSubChip(0x104, 0x0)

    def lambda_6689():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_6689)
    OP_0D()
    Sleep(800)

    ChrTalk(
        0x104,
        (
            "#5P#00313F#60W...Don't screw with\x01",
            "me... ...For what... did\x01",
            "I...\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x104, 2)
    SetChrSubChip(0x104, 0x1)
    SetCameraDistance(50000, 4000)
    Sleep(500)
    OP_82(0xC8, 0x0, 0xBB8, 0xBB8)
    OP_C9(0x0, 0x80000000)
    Sound(4117, 255, 100, 0)

    ChrTalk(
        0x104,
        "#5P#5S#20A#40WOOOOOOOOH!!!!\x02",
    )

    Sleep(1000)
    OP_C9(0x1, 0x80000000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    ClearChrFlags(0x104, 0x2)
    ClearChrFlags(0x104, 0x10)
    ClearChrFlags(0x104, 0x20)
    OP_24(0x35C)
    OP_24(0x35D)
    Sleep(1000)
    SetScenarioFlags(0x22, 1)
    NewScene("m0200", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_40_43FF end

    def Function_41_6778(): pass

    label("Function_41_6778")

    OP_82(0x64, 0x64, 0xBB8, 0x384)

    def lambda_678E():
        OP_A6(0xFE, 0x0, 0x1E, 0x2BC, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_678E)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1000, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1000, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1000, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1000, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1000, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1000, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1000, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1000, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1000, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_68(178300, 1100, 5650, 1300)
    MoveCamera(13, 13, -15, 1300)
    SetCameraDistance(19500, 1300)
    SetChrChipByIndex(0x10, 0x1F)
    SetChrSubChip(0x10, 0x0)

    def lambda_69DE():
        OP_95(0xFE, 178800, 0, 8500, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_69DE)
    WaitChrThread(0x10, 1)
    SetChrChipByIndex(0x10, 0x20)
    SetChrSubChip(0x10, 0x0)
    Sleep(100)
    SetChrSubChip(0x10, 0x1)
    Sleep(100)
    SetChrSubChip(0x10, 0x2)
    Sleep(100)
    OP_82(0x64, 0x64, 0xBB8, 0x1F4)

    def lambda_6A26():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6A26)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1000, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1000, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1000, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1000, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1000, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    SetChrChipByIndex(0x10, 0x1F)
    SetChrSubChip(0x10, 0x0)

    def lambda_6B69():
        OP_95(0xFE, 177200, 0, 6600, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_6B69)
    WaitChrThread(0x10, 1)
    SetChrChipByIndex(0x10, 0x20)
    SetChrSubChip(0x10, 0x0)
    Sleep(100)
    SetChrSubChip(0x10, 0x1)
    Sleep(100)
    SetChrSubChip(0x10, 0x2)
    Sleep(100)
    OP_82(0x64, 0x64, 0xBB8, 0x1F4)

    def lambda_6BB1():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6BB1)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1000, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1000, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1000, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1000, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1000, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    SetChrFlags(0xFE, 0x20)
    OP_93(0x10, 0xA0, 0x12C)
    ClearChrFlags(0xFE, 0x20)
    OP_82(0x64, 0x64, 0xBB8, 0x1F4)

    def lambda_6D0E():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6D0E)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1000, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1000, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1000, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1000, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1000, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    Return()

    # Function_41_6778 end

    def Function_42_6E45(): pass

    label("Function_42_6E45")

    Sleep(100)
    Sound(860, 2, 100, 0)
    Sound(861, 2, 100, 0)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 178800, 0, 7000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 178100, 0, 7500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 179200, 0, 7900, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 178600, 0, 7200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    StopSound(860, 500, 100)
    StopSound(861, 500, 100)
    Sleep(200)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 178200, 0, 6800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1300)
    Sound(860, 2, 100, 0)
    Sound(861, 2, 100, 0)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 179000, 0, 3000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 178500, 0, 3700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 178800, 0, 3200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    StopSound(860, 500, 100)
    StopSound(861, 500, 100)
    Sleep(800)
    Sound(860, 2, 100, 0)
    Sound(861, 2, 100, 0)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 174500, 0, 1500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 175300, 0, 2000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 175000, 0, 2300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 176600, 0, 1300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 177800, 0, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 178800, 0, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 178300, 0, 900, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    StopSound(860, 500, 100)
    StopSound(861, 500, 100)
    Return()

    # Function_42_6E45 end

    def Function_43_71F4(): pass

    label("Function_43_71F4")

    SetCameraDistance(20500, 500)
    ClearChrFlags(0x12, 0x2)
    ClearChrFlags(0x12, 0x10)
    SetChrChip(0x0, 0xFE, 0x1E, 0xC8)
    SetChrChipByIndex(0x12, 0x2E)
    SetChrSubChip(0x12, 0x3)
    Sound(844, 0, 100, 0)

    def lambda_7222():
        OP_9D(0xFE, 0x2BA70, 0x0, 0xC80, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_7222)
    WaitChrThread(0x12, 1)
    SetChrSubChip(0x12, 0x1)
    Sleep(100)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    SetChrSubChip(0x12, 0x0)
    Sleep(1500)
    SetChrChip(0x0, 0xFE, 0x1E, 0xC8)
    SetChrSubChip(0x12, 0x3)

    def lambda_7265():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_7265)
    Sound(844, 0, 100, 0)

    def lambda_7278():
        OP_9D(0xFE, 0x2A9A4, 0x0, 0x5DC, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_7278)
    WaitChrThread(0x12, 1)
    SetChrSubChip(0x12, 0x1)
    Sleep(200)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    SetChrSubChip(0x12, 0x0)
    Sleep(500)
    SetChrChip(0x0, 0xFE, 0x1E, 0xC8)
    SetChrSubChip(0x12, 0x3)

    def lambda_72BB():
        OP_93(0xFE, 0x154, 0x1F4)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_72BB)
    Sound(844, 0, 100, 0)

    def lambda_72CE():
        OP_9D(0xFE, 0x2BA70, 0x0, 0x1F4, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_72CE)
    WaitChrThread(0x12, 1)
    SetChrSubChip(0x12, 0x1)
    Sleep(100)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    SetChrSubChip(0x12, 0x0)
    Sleep(300)
    OP_68(177000, 1100, 7100, 1000)
    MoveCamera(27, 13, 5, 1000)
    SetCameraDistance(14500, 1000)
    SetChrChip(0x0, 0xFE, 0x1E, 0xC8)
    SetChrSubChip(0x12, 0x2)
    Sound(844, 0, 100, 0)

    def lambda_733C():
        OP_9D(0xFE, 0x2B368, 0x0, 0x1C84, 0xDAC, 0xFA0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_733C)
    Sleep(400)
    Sound(326, 0, 100, 0)
    OP_93(0x12, 0xA0, 0x0)
    SetChrSubChip(0x12, 0x3)
    WaitChrThread(0x12, 1)
    Sound(326, 0, 100, 0)
    SetChrSubChip(0x12, 0x1)
    Sleep(100)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Fade(250)
    Sound(802, 0, 100, 0)
    SetChrFlags(0x12, 0x2)
    SetChrFlags(0x12, 0x10)
    SetChrFlags(0x12, 0x20)
    SetChrChipByIndex(0x12, 0x2F)
    SetChrSubChip(0x12, 0x0)
    OP_A7(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_0D()
    Return()

    # Function_43_71F4 end

    def Function_44_73B0(): pass

    label("Function_44_73B0")

    SetChrChipByIndex(0x1E, 0x24)
    SetChrSubChip(0x1E, 0x0)
    OP_93(0x1E, 0x5A, 0x1F4)

    def lambda_73C4():
        OP_96(0xFE, 0x29B94, 0x0, 0x1CE8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_73C4)
    WaitChrThread(0x1E, 1)
    Return()

    # Function_44_73B0 end

    def Function_45_73DE(): pass

    label("Function_45_73DE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_740A")

    def lambda_73EE():
        OP_A6(0xFE, 0x0, 0x64, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_73EE)
    Sleep(500)
    Jump("Function_45_73DE")

    label("loc_740A")

    Return()

    # Function_45_73DE end

    def Function_46_740B(): pass

    label("Function_46_740B")


    def lambda_7410():
        OP_95(0xFE, 162900, 0, 2600, 4500, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7410)
    WaitChrThread(0x104, 1)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_46_740B end

    def Function_47_7431(): pass

    label("Function_47_7431")


    def lambda_7436():
        OP_95(0xFE, 160000, 0, 2000, 4500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7436)
    WaitChrThread(0x101, 1)

    def lambda_7454():
        OP_95(0xFE, 162900, 0, 4800, 4500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7454)
    WaitChrThread(0x101, 1)
    OP_93(0xFE, 0x87, 0x1F4)
    Return()

    # Function_47_7431 end

    def Function_48_7475(): pass

    label("Function_48_7475")


    def lambda_747A():
        OP_95(0xFE, 160000, 0, 4000, 4500, 0x1)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_747A)
    WaitChrThread(0x102, 1)

    def lambda_7498():
        OP_95(0xFE, 166600, 0, 9900, 4500, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7498)
    WaitChrThread(0x102, 1)
    OP_93(0xFE, 0x5A, 0x1F4)
    SetChrChipByIndex(0x102, 0x29)
    SetChrSubChip(0x102, 0x0)
    Sound(812, 0, 100, 0)
    Return()

    # Function_48_7475 end

    def Function_49_74C7(): pass

    label("Function_49_74C7")


    def lambda_74CC():
        OP_95(0xFE, 159000, 0, 5100, 4500, 0x1)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_74CC)
    WaitChrThread(0x109, 1)

    def lambda_74EA():
        OP_95(0xFE, 165300, 0, 7100, 4500, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_74EA)
    WaitChrThread(0x109, 1)
    OP_93(0xFE, 0x87, 0x1F4)
    Return()

    # Function_49_74C7 end

    def Function_50_750B(): pass

    label("Function_50_750B")


    def lambda_7510():
        OP_95(0xFE, 159000, 0, 4600, 4500, 0x1)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_7510)
    WaitChrThread(0x105, 1)

    def lambda_752E():
        OP_95(0xFE, 165600, 0, 11400, 4500, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_752E)
    WaitChrThread(0x105, 1)
    OP_93(0xFE, 0x5A, 0x1F4)
    SetChrChipByIndex(0x105, 0x2A)
    SetChrSubChip(0x105, 0x0)
    Sound(812, 0, 100, 0)
    Return()

    # Function_50_750B end

    def Function_51_755D(): pass

    label("Function_51_755D")


    def lambda_7562():
        OP_95(0xFE, 157000, 0, 3800, 4500, 0x1)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_7562)
    WaitChrThread(0x103, 1)

    def lambda_7580():
        OP_95(0xFE, 161800, 0, 6100, 4500, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_7580)
    WaitChrThread(0x103, 1)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_51_755D end

    def Function_52_75A1(): pass

    label("Function_52_75A1")

    Sleep(1000)
    StopEffect(0x0, 0x2)
    Sleep(1000)
    StopEffect(0x2, 0x2)
    Sleep(1000)
    StopEffect(0x4, 0x2)
    Sleep(1000)
    StopEffect(0x1, 0x2)
    Sleep(1000)
    StopEffect(0x3, 0x2)
    Return()

    # Function_52_75A1 end

    def Function_53_75C0(): pass

    label("Function_53_75C0")

    StopSound(864, 2000, 50)
    OP_25(0x35F, 0x3C)
    Sleep(100)
    OP_25(0x35F, 0x46)
    Sleep(100)
    OP_25(0x35F, 0x50)
    Sleep(100)
    OP_25(0x35F, 0x5A)
    Sleep(100)
    OP_25(0x35F, 0x64)
    Return()

    # Function_53_75C0 end

    def Function_54_75E7(): pass

    label("Function_54_75E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21C, 7)), scpexpr(EXPR_END)), "loc_75F1")
    Return()

    label("loc_75F1")

    EventBegin(0x1)
    OP_52(0x0, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x4, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x5, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x6, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x7, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrSubChip(0x0, 0x0)
    SetChrSubChip(0x1, 0x0)
    SetChrSubChip(0x2, 0x0)
    SetChrSubChip(0x3, 0x0)
    SetChrSubChip(0x4, 0x0)
    SetChrSubChip(0x5, 0x0)
    SetChrSubChip(0x6, 0x0)
    SetChrSubChip(0x7, 0x0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A large monster is\x01",
            "wandering about.\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[Exterminate]\x01",      # 0
            "[Cancel]\x01",           # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_76CF"),
        (SWITCH_DEFAULT, "loc_76E8"),
    )


    label("loc_76CF")

    Sleep(500)
    OP_E2(0x2)
    OP_90(0x0, 4970, 0, 0, 90)
    EventEnd(0x5)
    Return()

    label("loc_76E8")

    Battle("BattleInfo_660", 0x0, 0x0, 0x100, 0xC, 0xFF)
    OP_E2(0x2)
    EventBegin(0x1)
    OP_68(4970, 1000, 0, 0)
    OP_90(0x0, 4970, 0, 0, 90)
    OP_90(0x1, 4970, 0, 0, 90)
    OP_90(0x2, 4970, 0, 0, 90)
    OP_90(0x3, 4970, 0, 0, 90)
    OP_90(0x4, 4970, 0, 0, 90)
    OP_90(0x5, 4970, 0, 0, 90)
    OP_90(0x6, 4970, 0, 0, 90)
    OP_90(0x7, 4970, 0, 0, 90)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (2, "loc_77AA"),
        (1, "loc_77AF"),
        (SWITCH_DEFAULT, "loc_77B2"),
    )


    label("loc_77AA")

    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    label("loc_77AF")

    OP_B9(0x0)
    Return()

    label("loc_77B2")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(510, 0, 870, 0)
    MoveCamera(44, 39, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(13070, 0)
    SetChrFlags(0x21, 0x80)
    OP_E2(0x3)
    Sleep(400)
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Wanted monster\x01",
            "exterminated!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x11),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    AddItemNumber(0x11, 1)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, 2500, 0, 0, 270)
    SetChrPos(0x102, -2500, 0, 0, 90)
    SetChrPos(0x103, -1200, 0, -1700, 45)
    SetChrPos(0x104, 1200, 0, -1700, 0)
    SetChrPos(0x109, -1200, 0, 1700, 180)
    SetChrPos(0x105, 1200, 0, 1700, 180)
    FadeToBright(300, 0)
    OP_0D()
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#00000FA craft book... It looks\x01",
            "like Tio and Wazy can\x01",
            "handle this one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FWazy, are you ok with\x01",
            "this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10300FYeah, let's try it now.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    Sound(517, 0, 100, 0)
    AddCraft(0x2, 0x191)
    AddCraft(0x4, 0x191)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Tio and Wazy learned the\x01\x07\x02",
            ""Sigma Ascension"\x07\x05",
            " Combi\x01",
            "Craft.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "By each expending 100 CP,\x01",
            "a powerful combination\x01",
            "attack can be unleashed.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x21C, 7)
    OP_29(0x8C, 0x4, 0x10)
    OP_29(0x8C, 0x4, 0x2)
    OP_29(0x8C, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_E2(0x2)
    ModifyEventFlags(0, 0, 0x80)
    EventEnd(0x5)
    Return()

    # Function_54_75E7 end

    def Function_55_7A72(): pass

    label("Function_55_7A72")

    SetMapFlags(0x8000000)
    EventBegin(0x1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It appears that the\x01",
            "orbal energy is down.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x194, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7C1C")

    ChrTalk(
        0x101,
        (
            "#00003FIt looks like we can't\x01",
            "advance any further.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FIt appears some routes in the city\x01",
            "have been sealed off following the\x01",
            "trade conference terror incident.\x02\x03",
            "#00203FI feel it's a proper or natural\x01",
            "decision.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FWell, it's not like we have any\x01",
            "particular business further inside, so\x01",
            "shall we retrace our steps quietly?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x194, 4)

    label("loc_7C1C")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_55_7A72 end

    SaveToFile()

Try(main)
