from ScenarioHelper import *

def main():
    CreateScenaFile(
        "t0500.bin",                # FileName
        "t0500",                    # MapName
        "t0500",                    # Location
        0x003C,                     # MapIndex
        "ed7121",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x05,                       # PlaceNameNumber
        0x18,                       # PreInitFunctionIndex
        b'\x00\xff\x03',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 60, 0, 4, 0, 5],
    )

    BuildStringList((
        "t0500",                  # 0
        "Ami",                 # 1
        "Carlos",               # 2
        "Alec",                 # 3
        "Miner rosie",           # 4
        "Kimi",                 # 5
        "Miner Gantz",             # 6
        "Miners Mallo",             # 7
        "Wrestler Wenzel",     # 8
        "Chiluru",                 # 9
        "bus",                   # 10
        "A security guard",               # 11
        "A security guard",               # 12
        "A security guard",               # 13
        "A security guard",               # 14
        "A security guard",               # 15
        "Lieutenant Mireille",           # 16
        "car",                     # 17
        "Zeit",               # 18
        "Mayor of Vixen",           # 19
        "Mrs. Anna",             # 20
        "Miner Max",           # 21
        "Mining head Hoffman",         # 22
        "SE control",                 # 23
        "Mainz Mountain Road",           # 24
        "Mainz Mine",           # 25
    ))

    AddCharChip((
        "chr/ch23700.itc",                   # 00
        "chr/ch23600.itc",                   # 01
        "chr/ch23000.itc",                   # 02
        "chr/ch26200.itc",                   # 03
        "chr/ch23900.itc",                   # 04
        "chr/ch20500.itc",                   # 05
        "chr/ch30700.itc",                   # 06
        "chr/ch27300.itc",                   # 07
    ))

    DeclNpc(6739,    0,       42729,   0,    261,  0x0, 0,   0,   0,   0,   2,   0,   10,  255,  0)
    DeclNpc(10399,   0,       55259,   90,   261,  0x0, 0,   1,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(28329,   4294964296, 62000,   180,  261,  0x0, 0,   2,   0,   0,   1,   0,   12,  255,  0)
    DeclNpc(899,     6000,    77779,   0,    389,  0x0, 0,   3,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(400,     6000,    77779,   0,    389,  0x0, 0,   4,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(1980,    6000,    77930,   45,   389,  0x0, 0,   6,   0,   0,   0,   0,   16,  255,  0)
    DeclNpc(19,      6000,    77889,   0,    389,  0x0, 0,   3,   0,   0,   0,   0,   17,  255,  0)
    DeclNpc(1980,    6000,    77930,   45,   389,  0x0, 0,   7,   0,   0,   0,   0,   18,  255,  0)
    DeclNpc(1980,    6000,    77930,   45,   389,  0x0, 0,   5,   0,   0,   0,   0,   19,  255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
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
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(4294962696, 4294965296, 28700,   1500,    4294962696, 4294966796, 28700,   0x007C, 0,  21, 0x0000)
    DeclActor(4850,    4294965296, 26210,   1500,    4850,    0,       26210,   0x007C, 0,  20, 0x0000)
    DeclActor(5390,    4294965296, 26160,   1500,    5390,    0,       26160,   0x007C, 0,  20, 0x0000)
    DeclActor(4294941396, 11440,   56000,   1500,    4294941396, 12940,   56000,   0x007C, 0,  68, 0x0000)

    PlaceName(11.0, 0.0, -23.0, 0x0000, 0x0000, "Mainz Mountain Road")
    PlaceName(-32.0, 0.0, 62.0, 0x0000, 0x0000, "Mainz Mine")
    PlaceName(-19.75, 0.0, 45.75, 0x0000, 0x0053, "")
    PlaceName(-3.0, 0.0, 49.0, 0x0000, 0x0052, "")
    PlaceName(-4.5, 0.0, 28.600000381469727, 0x0000, 0x0055, "")

    ChipFrameInfo(1344, 0)                                       # 0

    ScpFunction((
        "Function_0_540",          # 00, 0
        "Function_1_5F8",          # 01, 1
        "Function_2_623",          # 02, 2
        "Function_3_64E",          # 03, 3
        "Function_4_681",          # 04, 4
        "Function_5_E0A",          # 05, 5
        "Function_6_1027",         # 06, 6
        "Function_7_11AB",         # 07, 7
        "Function_8_12DE",         # 08, 8
        "Function_9_132F",         # 09, 9
        "Function_10_13C3",        # 0A, 10
        "Function_11_215C",        # 0B, 11
        "Function_12_2EAB",        # 0C, 12
        "Function_13_37F7",        # 0D, 13
        "Function_14_38CB",        # 0E, 14
        "Function_15_3CFA",        # 0F, 15
        "Function_16_3F03",        # 10, 16
        "Function_17_4011",        # 11, 17
        "Function_18_415D",        # 12, 18
        "Function_19_4483",        # 13, 19
        "Function_20_457F",        # 14, 20
        "Function_21_48C2",        # 15, 21
        "Function_22_490E",        # 16, 22
        "Function_23_4EAA",        # 17, 23
        "Function_24_4EBA",        # 18, 24
        "Function_25_4F55",        # 19, 25
        "Function_26_4F56",        # 1A, 26
        "Function_27_4F57",        # 1B, 27
        "Function_28_4F58",        # 1C, 28
        "Function_29_4F96",        # 1D, 29
        "Function_30_5019",        # 1E, 30
        "Function_31_50A3",        # 1F, 31
        "Function_32_512E",        # 20, 32
        "Function_33_51B1",        # 21, 33
        "Function_34_52A9",        # 22, 34
        "Function_35_534D",        # 23, 35
        "Function_36_538A",        # 24, 36
        "Function_37_53EC",        # 25, 37
        "Function_38_54CD",        # 26, 38
        "Function_39_58A2",        # 27, 39
        "Function_40_5902",        # 28, 40
        "Function_41_5912",        # 29, 41
        "Function_42_5925",        # 2A, 42
        "Function_43_5938",        # 2B, 43
        "Function_44_594B",        # 2C, 44
        "Function_45_607F",        # 2D, 45
        "Function_46_6099",        # 2E, 46
        "Function_47_6108",        # 2F, 47
        "Function_48_6171",        # 30, 48
        "Function_49_61AF",        # 31, 49
        "Function_50_61F0",        # 32, 50
        "Function_51_6231",        # 33, 51
        "Function_52_62A4",        # 34, 52
        "Function_53_62BD",        # 35, 53
        "Function_54_6A6C",        # 36, 54
        "Function_55_6AA4",        # 37, 55
        "Function_56_6B4B",        # 38, 56
        "Function_57_6BDA",        # 39, 57
        "Function_58_8355",        # 3A, 58
        "Function_59_8385",        # 3B, 59
        "Function_60_83DB",        # 3C, 60
        "Function_61_842E",        # 3D, 61
        "Function_62_8498",        # 3E, 62
        "Function_63_84F8",        # 3F, 63
        "Function_64_8558",        # 40, 64
        "Function_65_8766",        # 41, 65
        "Function_66_87B3",        # 42, 66
        "Function_67_8800",        # 43, 67
        "Function_68_8825",        # 44, 68
    ))


    def Function_0_540(): pass

    label("Function_0_540")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_580"),
        (1, "loc_58C"),
        (2, "loc_598"),
        (3, "loc_5A4"),
        (4, "loc_5B0"),
        (5, "loc_5BC"),
        (6, "loc_5C8"),
        (SWITCH_DEFAULT, "loc_5D4"),
    )


    label("loc_580")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_5E0")

    label("loc_58C")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_5E0")

    label("loc_598")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_5E0")

    label("loc_5A4")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_5E0")

    label("loc_5B0")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_5E0")

    label("loc_5BC")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_5E0")

    label("loc_5C8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_5E0")

    label("loc_5D4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_5E0")

    label("loc_5E0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5F7")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_5E0")

    label("loc_5F7")

    Return()

    # Function_0_540 end

    def Function_1_5F8(): pass

    label("Function_1_5F8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_622")
    OP_94(0xFE, 0x648C, 0xEA38, 0x727E, 0xF488, 0x3E8)
    Sleep(300)
    Jump("Function_1_5F8")

    label("loc_622")

    Return()

    # Function_1_5F8 end

    def Function_2_623(): pass

    label("Function_2_623")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_64D")
    OP_94(0xFE, 0x1C98, 0x8EDA, 0x1F40, 0xB72A, 0x3E8)
    Sleep(300)
    Jump("Function_2_623")

    label("loc_64D")

    Return()

    # Function_2_623 end

    def Function_3_64E(): pass

    label("Function_3_64E")

    SetMapObjFlags(0xC, 0x2000000)
    SetMapObjFlags(0xD, 0x2000000)
    SetMapObjFlags(0xE, 0x2000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x166, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_680")
    ClearMapObjFlags(0xC, 0x2000000)
    ClearMapObjFlags(0xD, 0x2000000)
    ClearMapObjFlags(0xE, 0x2000000)

    label("loc_680")

    Return()

    # Function_3_64E end

    def Function_4_681(): pass

    label("Function_4_681")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_694")
    ClearChrFlags(0xF, 0x80)
    Jump("loc_81E")

    label("loc_694")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_6C2")
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 18450, -8990, 41770, 270)
    Jump("loc_81E")

    label("loc_6C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_6E6")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 18450, -8990, 41770, 270)
    Jump("loc_81E")

    label("loc_6E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_6F4")
    Jump("loc_81E")

    label("loc_6F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_702")
    Jump("loc_81E")

    label("loc_702")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_71F")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    Jump("loc_81E")

    label("loc_71F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_72D")
    Jump("loc_81E")

    label("loc_72D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_772")
    SetChrPos(0xA, 1400, 6000, 77780, 0)
    BeginChrThread(0xA, 0, 0, 0)
    SetChrFlags(0xA, 0x10)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 400, 6000, 77780, 0)
    SetChrFlags(0xC, 0x10)
    Jump("loc_81E")

    label("loc_772")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_785")
    ClearChrFlags(0x10, 0x80)
    Jump("loc_81E")

    label("loc_785")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_7C0")
    BeginChrThread(0xA, 0, 0, 0)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xA, 1850, 0, 69850, 270)
    SetChrPos(0xC, 850, 0, 69850, 90)
    Jump("loc_81E")

    label("loc_7C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_7CE")
    Jump("loc_81E")

    label("loc_7CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_7E1")
    SetChrFlags(0x8, 0x80)
    Jump("loc_81E")

    label("loc_7E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_7F4")
    SetChrFlags(0xA, 0x80)
    Jump("loc_81E")

    label("loc_7F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_807")
    ClearChrFlags(0xB, 0x80)
    Jump("loc_81E")

    label("loc_807")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_815")
    Jump("loc_81E")

    label("loc_815")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_81E")

    label("loc_81E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_842")
    SetMapFlags(0x10000000)
    Event(0, 38)
    Jump("loc_879")

    label("loc_842")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_861")
    Event(0, 44)
    Jump("loc_879")

    label("loc_861")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_879")
    ClearScenarioFlags(0x3E, 0)
    Event(0, 53)

    label("loc_879")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_890")
    ClearScenarioFlags(0x22, 0)
    SetScenarioFlags(0x0, 0)
    Event(0, 22)
    Jump("loc_8DB")

    label("loc_890")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_8A4")
    ClearScenarioFlags(0x22, 1)
    Event(0, 44)
    Jump("loc_8DB")

    label("loc_8A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_8B8")
    ClearScenarioFlags(0x22, 2)
    Event(0, 53)
    Jump("loc_8DB")

    label("loc_8B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_8CC")
    ClearScenarioFlags(0x22, 3)
    Event(0, 57)
    Jump("loc_8DB")

    label("loc_8CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 4)), scpexpr(EXPR_END)), "loc_8DB")
    ClearScenarioFlags(0x22, 4)
    Event(0, 64)

    label("loc_8DB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D7F")
    ClearScenarioFlags(0x38, 0)
    ClearScenarioFlags(0x38, 1)
    ClearScenarioFlags(0x38, 2)
    ClearScenarioFlags(0x38, 3)
    ClearScenarioFlags(0x38, 4)
    ClearScenarioFlags(0x38, 5)
    ClearScenarioFlags(0x38, 6)
    ClearScenarioFlags(0x38, 7)
    ClearScenarioFlags(0x39, 0)
    ClearScenarioFlags(0x39, 1)
    ClearScenarioFlags(0x39, 2)
    ClearScenarioFlags(0x39, 3)
    ClearScenarioFlags(0x39, 4)
    ClearScenarioFlags(0x39, 5)
    ClearScenarioFlags(0x39, 6)
    ClearScenarioFlags(0x39, 7)
    ClearScenarioFlags(0x3A, 0)
    ClearScenarioFlags(0x3A, 1)
    ClearScenarioFlags(0x3A, 2)
    ClearScenarioFlags(0x3A, 3)
    ClearScenarioFlags(0x3A, 4)
    ClearScenarioFlags(0x3A, 5)
    ClearScenarioFlags(0x3A, 6)
    ClearScenarioFlags(0x3A, 7)
    ClearScenarioFlags(0x3B, 0)
    ClearScenarioFlags(0x3B, 1)
    ClearScenarioFlags(0x3B, 2)
    ClearScenarioFlags(0x3B, 3)
    ClearScenarioFlags(0x3B, 4)
    ClearScenarioFlags(0x3B, 5)
    ClearScenarioFlags(0x3B, 6)
    ClearScenarioFlags(0x3B, 7)
    ClearScenarioFlags(0x3D, 5)
    ClearScenarioFlags(0x3D, 6)
    ClearScenarioFlags(0x3D, 7)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_968")
    SetScenarioFlags(0x38, 0)

    label("loc_968")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_97E")
    SetScenarioFlags(0x38, 1)

    label("loc_97E")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_994")
    SetScenarioFlags(0x38, 2)

    label("loc_994")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9AA")
    SetScenarioFlags(0x38, 3)

    label("loc_9AA")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9C0")
    SetScenarioFlags(0x38, 4)

    label("loc_9C0")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9D6")
    SetScenarioFlags(0x38, 5)

    label("loc_9D6")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9EC")
    SetScenarioFlags(0x38, 6)

    label("loc_9EC")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A02")
    SetScenarioFlags(0x38, 7)

    label("loc_A02")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A18")
    SetScenarioFlags(0x39, 0)

    label("loc_A18")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A2E")
    SetScenarioFlags(0x39, 1)

    label("loc_A2E")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A44")
    SetScenarioFlags(0x39, 2)

    label("loc_A44")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A5A")
    SetScenarioFlags(0x39, 3)

    label("loc_A5A")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A70")
    SetScenarioFlags(0x39, 4)

    label("loc_A70")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A86")
    SetScenarioFlags(0x39, 5)

    label("loc_A86")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A9C")
    SetScenarioFlags(0x39, 6)

    label("loc_A9C")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AB2")
    SetScenarioFlags(0x39, 7)

    label("loc_AB2")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AC8")
    SetScenarioFlags(0x3A, 0)

    label("loc_AC8")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ADE")
    SetScenarioFlags(0x3A, 1)

    label("loc_ADE")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AF4")
    SetScenarioFlags(0x3A, 2)

    label("loc_AF4")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B0A")
    SetScenarioFlags(0x3A, 3)

    label("loc_B0A")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B20")
    SetScenarioFlags(0x3A, 4)

    label("loc_B20")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B36")
    SetScenarioFlags(0x3A, 5)

    label("loc_B36")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B4C")
    SetScenarioFlags(0x3A, 6)

    label("loc_B4C")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B62")
    SetScenarioFlags(0x3A, 7)

    label("loc_B62")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B78")
    SetScenarioFlags(0x3B, 0)

    label("loc_B78")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B8E")
    SetScenarioFlags(0x3B, 1)

    label("loc_B8E")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BA4")
    SetScenarioFlags(0x3B, 2)

    label("loc_BA4")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BBA")
    SetScenarioFlags(0x3B, 3)

    label("loc_BBA")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BD0")
    SetScenarioFlags(0x3B, 4)

    label("loc_BD0")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BE6")
    SetScenarioFlags(0x3B, 5)

    label("loc_BE6")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BFC")
    SetScenarioFlags(0x3B, 6)

    label("loc_BFC")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C12")
    SetScenarioFlags(0x3B, 7)

    label("loc_C12")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C28")
    SetScenarioFlags(0x3D, 5)

    label("loc_C28")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C3E")
    SetScenarioFlags(0x3D, 6)

    label("loc_C3E")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C54")
    SetScenarioFlags(0x3D, 7)

    label("loc_C54")

    ClearScenarioFlags(0x3C, 0)
    ClearScenarioFlags(0x3C, 1)
    ClearScenarioFlags(0x3C, 2)
    ClearScenarioFlags(0x3C, 3)
    ClearScenarioFlags(0x3C, 4)
    ClearScenarioFlags(0x3C, 5)
    ClearScenarioFlags(0x3C, 6)
    ClearScenarioFlags(0x3C, 7)
    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C8F")
    SetScenarioFlags(0x3C, 0)
    Jump("loc_D7F")

    label("loc_C8F")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CB2")
    SetScenarioFlags(0x3C, 1)
    Jump("loc_D7F")

    label("loc_CB2")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CD5")
    SetScenarioFlags(0x3C, 2)
    Jump("loc_D7F")

    label("loc_CD5")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CF8")
    SetScenarioFlags(0x3C, 3)
    Jump("loc_D7F")

    label("loc_CF8")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D1B")
    SetScenarioFlags(0x3C, 4)
    Jump("loc_D7F")

    label("loc_D1B")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D3E")
    SetScenarioFlags(0x3C, 5)
    Jump("loc_D7F")

    label("loc_D3E")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D61")
    SetScenarioFlags(0x3C, 6)
    Jump("loc_D7F")

    label("loc_D61")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D7F")
    SetScenarioFlags(0x3C, 7)

    label("loc_D7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x37, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D95")
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D95")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DC7")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DC7")
    SetChrPos(0x0, 2750, -2000, 25500, 270)
    OP_31(0x1)
    OP_69(0xFF, 0x0)
    Event(0, 9)

    label("loc_DC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_DFA")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DFA")
    SetChrPos(0x0, 2750, -2000, 25500, 270)
    OP_31(0x1)
    OP_69(0xFF, 0x0)
    ClearMapFlags(0x8000000)

    label("loc_DFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E, 0)), scpexpr(EXPR_END)), "loc_E09")
    ClearScenarioFlags(0x3E, 0)
    Event(0, 8)

    label("loc_E09")

    Return()

    # Function_4_681 end

    def Function_5_E0A(): pass

    label("Function_5_E0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_E24")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 0)
    Jump("loc_E50")

    label("loc_E24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 0)), scpexpr(EXPR_END)), "loc_E3E")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x25, 0)
    Jump("loc_E50")

    label("loc_E3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_E50")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x233), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E50")

    SoundDistance(0x84, 0xFFFFF678, 0x1B4E, 0x15766, 0x2710, 0xC350, 0x64, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EE3")
    LoadEffect(0x9, "map/mprain00.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0x0, 0xC8, 0x0)
    Sound(128, 1, 100, 0)

    label("loc_EE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_EFA")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    Jump("loc_EFA")

    label("loc_EFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_F08")
    Jump("loc_FDF")

    label("loc_F08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_F29")
    ClearMapObjFlags(0xB, 0x4)
    SetMapObjFrame(0xB, "light", 0x0, 0x1)
    Jump("loc_FDF")

    label("loc_F29")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_F37")
    Jump("loc_FDF")

    label("loc_F37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_F45")
    Jump("loc_FDF")

    label("loc_F45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_F53")
    Jump("loc_FDF")

    label("loc_F53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_F61")
    Jump("loc_FDF")

    label("loc_F61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_F6F")
    Jump("loc_FDF")

    label("loc_F6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_F7D")
    Jump("loc_FDF")

    label("loc_F7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_F8B")
    Jump("loc_FDF")

    label("loc_F8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_FAC")
    ClearMapObjFlags(0xB, 0x4)
    SetMapObjFrame(0xB, "light", 0x0, 0x1)
    Jump("loc_FDF")

    label("loc_FAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_FBA")
    Jump("loc_FDF")

    label("loc_FBA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_FC8")
    Jump("loc_FDF")

    label("loc_FC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_FD6")
    Jump("loc_FDF")

    label("loc_FD6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_FDF")

    label("loc_FDF")

    MiniGame(0x2F, 0x1, 0x2, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_65(0x3, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1013")
    Jump("loc_1026")

    label("loc_1013")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_1026")
    ClearMapObjFlags(0x6, 0x10)
    OP_66(0x3, 0x1)

    label("loc_1026")

    Return()

    # Function_5_E0A end

    def Function_6_1027(): pass

    label("Function_6_1027")

    EventBegin(0x2)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12D, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10EE")
    Sound(814, 0, 100, 0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Examining the sign at the bus stop,\x01",
            "導力busに乗ることができます。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "導力carと同様に、\x01",
            "Please use it to move to various places.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x12D, 6)

    label("loc_10EE")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1Kbus停がある。\x01",
            "busで移動しますか？\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Crossbell City North Exit\x01",            # 0
            "Stop (near the puppet room)\x01",      # 1
            "quit\x01",                      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1183")
    Call(0, 7)
    ClearMapFlags(0x8000000)
    NewScene("r2000", 0, 0, 0)
    IdleLoop()
    Jump("loc_11A3")

    label("loc_1183")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11A3")
    Call(0, 7)
    ClearMapFlags(0x8000000)
    NewScene("r2030", 0, 0, 0)
    IdleLoop()

    label("loc_11A3")

    ClearMapFlags(0x8000000)
    EventEnd(0x3)
    Return()

    # Function_6_1027 end

    def Function_7_11AB(): pass

    label("Function_7_11AB")

    ClearMapFlags(0x1)
    SetEventSkip(0x0, "loc_12DA")
    Fade(500)
    OP_68(-3860, -550, 26120, 0)
    MoveCamera(315, 30, 0, 0)
    OP_6E(640, 0)
    SetCameraDistance(18500, 0)
    OP_E2(0x1)
    SetChrPos(0x0, -4540, -2000, 27710, 180)
    SetChrPos(0x1, -5300, -2000, 27570, 180)
    SetChrPos(0x2, -6100, -2000, 27430, 180)
    SetChrPos(0x3, -6860, -2000, 27250, 180)
    ClearChrFlags(0x11, 0x80)
    ClearMapObjFlags(0x8, 0x4)
    ClearMapObjFlags(0x8, 0x2)
    OP_78(0x8, 0x11)
    SetMapObjFrame(0x8, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0x11, -6320, -2000, 11640, 0)
    OP_D5(0x11, 0x0, 0x0, 0x0, 0x0)
    SetMapObjFlags(0x8, 0x1000)
    OP_74(0x8, 0x1E)
    OP_71(0x8, 0x79, 0xB4, 0x0, 0x20)

    def lambda_1291():
        OP_96(0xFE, 0xFFFFE750, 0xFFFFF830, 0x528A, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1291)
    OP_0D()
    Sound(466, 0, 100, 0)
    Sound(467, 0, 100, 0)
    WaitChrThread(0x11, 1)
    OP_71(0x8, 0x5B, 0x78, 0x0, 0x0)
    OP_79(0x8)
    Sleep(300)
    FadeToDark(500, 0, -1)
    OP_0D()
    SetEventSkip(0x1, 0x0)

    label("loc_12DA")

    SetScenarioFlags(0x3E, 0)
    Return()

    # Function_7_11AB end

    def Function_8_12DE(): pass

    label("Function_8_12DE")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    OP_0D()
    SetChrPos(0x0, -4540, -2000, 27710, 180)
    OP_31(0x1)
    OP_68(-4540, -550, 27710, 0)
    MoveCamera(315, 21, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18500, 0)
    EventEnd(0x5)
    Return()

    # Function_8_12DE end

    def Function_9_132F(): pass

    label("Function_9_132F")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    Sleep(100)
    Sound(459, 0, 100, 0)
    Sleep(2000)
    StopSound(459, 1000, 100)
    Sound(492, 0, 70, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_138A")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_137F")
    Sound(2502, 255, 100, 0)
    Jump("loc_1385")

    label("loc_137F")

    Sound(2503, 255, 100, 0)

    label("loc_1385")

    Jump("loc_13AE")

    label("loc_138A")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_13A8")
    Sound(3347, 255, 100, 0)
    Jump("loc_13AE")

    label("loc_13A8")

    Sound(3348, 255, 100, 0)

    label("loc_13AE")

    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_9_132F end

    def Function_10_13C3(): pass

    label("Function_10_13C3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_154B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14B5")

    ChrTalk(
        0x8,
        (
            "I wonder what kind of thing.\x01",
            "That pale glowing tree …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Even from the main place in Mainz\x01",
            "I can see that it is quite big.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Even a grandmother familiar with history\x01",
            "It says that I have not seen it,\x01",
            "It has become uneasy somehow.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1546")

    label("loc_14B5")


    ChrTalk(
        0x8,
        (
            "That pale glowing tree …\x01",
            "I wonder what it is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Even a grandmother familiar with history\x01",
            "It says that I have not seen it,\x01",
            "It has become uneasy somehow.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1546")

    Jump("loc_2158")

    label("loc_154B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_169E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1618")

    ChrTalk(
        0x8,
        (
            "Crossbell independence\x01",
            "Is it really invalid?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Resistance people\x01",
            "The defense forces, who had come to search,\x01",
            "I was impatiently back home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Huhun, it feels nice.\x01",
            "Justice surely win!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1699")

    label("loc_1618")


    ChrTalk(
        0x8,
        (
            "Resistance people\x01",
            "The defense forces, who had come to search,\x01",
            "I was impatiently back home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Huhun, it feels nice.\x01",
            "Justice surely win!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1699")

    Jump("loc_2158")

    label("loc_169E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_1852")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17A9")

    ChrTalk(
        0x8,
        (
            "In Mainz in the whole town\x01",
            "A security guardたちのレジスタンス活動を\x01",
            "I am helping you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I occupied Mainz\x01",
            "The President who uses hunters,\x01",
            "You can not trust it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "…… Besides, against the government\x01",
            "To penetrate our justice,\x01",
            "It's cool!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_184D")

    label("loc_17A9")


    ChrTalk(
        0x8,
        (
            "In Mainz in the whole town\x01",
            "A security guardたちのレジスタンス活動を\x01",
            "I am helping you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I can not trust the president … …\x01",
            "Resistance against it\x01",
            "It's cool!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_184D")

    Jump("loc_2158")

    label("loc_1852")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_196E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_193A")

    ChrTalk(
        0x8,
        (
            "In the meantime, the hunters\x01",
            "When it appeared in town,\x01",
            "I thought it was no good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The guard who came to help, too\x01",
            "I got carried away one after another … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "But, to people and things in town\x01",
            "I did not put out much effort.\x01",
            "I wonder what I wanted ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1969")

    label("loc_193A")


    ChrTalk(
        0x8,
        (
            "That hunters,\x01",
            "I wonder what I wanted ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1969")

    Jump("loc_2158")

    label("loc_196E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_197C")
    Jump("loc_2158")

    label("loc_197C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1B0C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A8F")

    ChrTalk(
        0x8,
        (
            "The day after tomorrow is Crossbell City\x01",
            "Of alkane shell\x01",
            "It's a renewal performance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Because I can do it only once,\x01",
            "I would like to see the stage setting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "That's why the theater is a hobbyist\x01",
            "By chance, the seats were next to each other,\x01",
            "Do not talk the story …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F(The motive is impure … …)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1B07")

    label("loc_1A8F")


    ChrTalk(
        0x8,
        (
            "Because I can do it only once,\x01",
            "I would like to see the stage setting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "That's why the theater is a hobbyist\x01",
            "I have a nice encounter.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B07")

    Jump("loc_2158")

    label("loc_1B0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1C8F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C19")

    ChrTalk(
        0x8,
        (
            "By the time the harlest guys\x01",
            "It is said that it came out to the northern mountainous area\x01",
            "I came to get rid of monsters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Although it seems that it was able to get rid of it,\x01",
            "It is not sort of funny\x01",
            "It was a funny demon beast.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Recently I talked about such monsters\x01",
            "I listen often, but ….\x01",
            "I wonder if there is a cause.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1C8A")

    label("loc_1C19")


    ChrTalk(
        0x8,
        (
            "But, such\x01",
            "A monstrous beast who might be an object\x01",
            "I can not beat them … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "After all it is Yuushishi\x01",
            "Hey, hey, hey.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C8A")

    Jump("loc_2158")

    label("loc_1C8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1E83")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DEF")

    ChrTalk(
        0x8,
        (
            "Regularly in town,\x01",
            "Sister came and Sunday school\x01",
            "I'm going on classes ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Sometimes a young priest\x01",
            "Do not you think you can come?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "That's it, then!\x01",
            "I arranged funny clothes and others\x01",
            "Be fashionable!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FEven though it is a delusion\x01",
            "It is a very bad father …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FHugh, I'm really surprised\x01",
            "You should have such a Father.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1E7E")

    label("loc_1DEF")


    ChrTalk(
        0x8,
        (
            "Sometimes a young priest\x01",
            "You can come and go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I arranged funny clothes and others\x01",
            "If it is fashionable,\x01",
            "I might fall in love.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E7E")

    Jump("loc_2158")

    label("loc_1E83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1E91")
    Jump("loc_2158")

    label("loc_1E91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1FC9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F4C")

    ChrTalk(
        0x8,
        (
            "My older brother,\x01",
            "I am working as a miner at the mine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Although I was only waving Sabo,\x01",
            "Somehow it seems I am doing my best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Hehe, my grandmother was happy too.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1FC4")

    label("loc_1F4C")


    ChrTalk(
        0x8,
        (
            "My older brother,\x01",
            "Although I was only fond of sabo\x01",
            "Recently I work properly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Hehe, my grandmother was happy too.\x02",
    )

    CloseMessageWindow()

    label("loc_1FC4")

    Jump("loc_2158")

    label("loc_1FC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_2158")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20DA")
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x8, 0x105, 500)
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    ChrTalk(
        0x8,
        "#5SFunny! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FIs it for something for me?\x01",
            "Cute little lady#8RFraulein#.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "(Nanana, what is this human!\x01",
            "I am super de strike! )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F(Well, indeed Wadi ……)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2158")

    label("loc_20DA")

    TurnDirection(0x8, 0x105, 0)

    ChrTalk(
        0x8,
        (
            "Ha, even so\x01",
            "Beautiful face …… Spray\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "(… … what?\x01",
            "boy? A girl? )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10300FHuh, you are a funny child.\x02",
    )

    CloseMessageWindow()

    label("loc_2158")

    TalkEnd(0xFE)
    Return()

    # Function_10_13C3 end

    def Function_11_215C(): pass

    label("Function_11_215C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_226D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2218")

    ChrTalk(
        0x9,
        "No way that such things appear … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "…… No, do not be bearish.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "The mine resumed so much\x01",
            "Everyone is motivated,\x01",
            "I hope that I will be positive.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2268")

    label("loc_2218")


    ChrTalk(
        0x9,
        (
            "The mine resumed so much\x01",
            "Everyone is motivated,\x01",
            "I hope that I will be positive.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2268")

    Jump("loc_2EA7")

    label("loc_226D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_23B7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2342")

    ChrTalk(
        0x9,
        (
            "The hunters who existed before\x01",
            "Since resistance hunting,\x01",
            "There is no massive strategy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Since invalid declaration came out,\x01",
            "I am worried about how they get out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "To everyone in resistance\x01",
            "I want you to be careful.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_23B2")

    label("loc_2342")


    ChrTalk(
        0x9,
        (
            "Since invalid declaration came out,\x01",
            "I am worried about how the hunters come out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "To everyone in resistance\x01",
            "I want you to be careful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23B2")

    Jump("loc_2EA7")

    label("loc_23B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_2507")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_248A")

    ChrTalk(
        0x9,
        (
            "Mireille san\x01",
            "When I first visited here,\x01",
            "We were also alarmed … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Everyone in Mainz,\x01",
            "To the President and the Defense Forces policy\x01",
            "I felt doubt.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "This place is a sticky place.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2502")

    label("loc_248A")


    ChrTalk(
        0x9,
        (
            "Like the Mireille,\x01",
            "Everyone in Mainz also to the president\x01",
            "I felt doubt.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "This place is a sticky place.\x02",
    )

    CloseMessageWindow()

    label("loc_2502")

    Jump("loc_2EA7")

    label("loc_2507")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2693")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2608")

    ChrTalk(
        0x9,
        (
            "The occupation of Mainz and the street raid,\x01",
            "To withdraw independent advocacy\x01",
            "It is a rumor that it was a work of the empire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Involving our innocent servants,\x01",
            "It also caused serious damage to the guard ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "…… To sacrifice people for politics,\x01",
            "You should never forgive them.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_268E")

    label("loc_2608")


    ChrTalk(
        0x9,
        (
            "The occupation of Mainz and the street raid,\x01",
            "It is a rumor that it was a work of an empire … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "To sacrifice people for politics,\x01",
            "You should never forgive them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_268E")

    Jump("loc_2EA7")

    label("loc_2693")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_26A1")
    Jump("loc_2EA7")

    label("loc_26A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_27ED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_277A")

    ChrTalk(
        0x9,
        (
            "I also live in Mainz,\x01",
            "About the workshop in the middle of the mountain path\x01",
            "I do not know well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Anyway, the Lord of that studio\x01",
            "It does not show up at all in the village.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Perhaps, a reasonably strange person\x01",
            "I guess she lives there.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_27E8")

    label("loc_277A")


    ChrTalk(
        0x9,
        (
            "The lord of the workshop in the middle of the mountain path\x01",
            "It does not appear at all in the human race.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Perhaps, a reasonably strange person\x01",
            "I guess she lives there.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27E8")

    Jump("loc_2EA7")

    label("loc_27ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_290F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2894")

    ChrTalk(
        0x9,
        (
            "During this time,\x01",
            "The demon that appeared in the mountainous area in the north ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "A monster who appeared on the old mine shortly ago\x01",
            "She seems to have had the same shape.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Hmm … Is there anything to do with it?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_290A")

    label("loc_2894")


    ChrTalk(
        0x9,
        (
            "With the monsters in the northern mountainous region,\x01",
            "A monster who left the old mine shortly before\x01",
            "She seems to have had the same shape.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Hmm … Is there anything to do with it?\x02",
    )

    CloseMessageWindow()

    label("loc_290A")

    Jump("loc_2EA7")

    label("loc_290F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2A3E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29D1")

    ChrTalk(
        0x9,
        (
            "Mr. Ganz, yesterday\x01",
            "I'm looking forward to seeing you at the casino.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Distraction, all the miners\x01",
            "It was exciting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I also joined from the middle.\x01",
            "No, it was quite fun.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2A39")

    label("loc_29D1")


    ChrTalk(
        0x9,
        (
            "Yesterday the miners\x01",
            "It was exciting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I also joined from the middle.\x01",
            "No, it was quite fun.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A39")

    Jump("loc_2EA7")

    label("loc_2A3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2BF8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B4B")

    ChrTalk(
        0x9,
        (
            "This morning to the town the seven raystone\x01",
            "Go on carrying.\x01",
            "In addition I also saw the unveiling ceremony.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "In the Orchest Tower's announcement,\x01",
            "Everyone, quite exciting\x01",
            "It sounds like it was showing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If it is from that height,\x01",
            "I will look around the city.\x01",
            "I would like to go up once.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2BF3")

    label("loc_2B4B")


    ChrTalk(
        0x9,
        (
            "In the Orchest Tower's announcement,\x01",
            "Everyone, quite exciting\x01",
            "It sounds like it was showing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If it is from that height,\x01",
            "I will look around the city.\x01",
            "I would like to go up once.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BF3")

    Jump("loc_2EA7")

    label("loc_2BF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2D60")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CDA")

    ChrTalk(
        0x9,
        (
            "I am at this mine\x01",
            "The mined seven giant stone\x01",
            "I'm carrying it to the city ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "The mountain road has many curves,\x01",
            "積荷を載せた運搬carを\x01",
            "It's tough to drive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "There are also many cliffs, so than anything else\x01",
            "Carefulness is required.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2D5B")

    label("loc_2CDA")


    ChrTalk(
        0x9,
        (
            "The mountain road has many curves,\x01",
            "積荷を載せた運搬carは\x01",
            "It's easy to shake left and right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "There are also many cliffs, so than anything else\x01",
            "Carefulness is required.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D5B")

    Jump("loc_2EA7")

    label("loc_2D60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_2EA7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E2F")

    ChrTalk(
        0x9,
        (
            "Mr. Gans, recently very\x01",
            "I am working fun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Apparently that\x01",
            "Triggered by a cult incident\x01",
            "It seems that it was blown out in various ways.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Everyone was worried … …\x01",
            "Anyway, it was nice.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2EA7")

    label("loc_2E2F")


    ChrTalk(
        0x9,
        (
            "ガンツさん、Triggered by a cult incident\x01",
            "It seems that it was blown out in various ways.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Everyone was worried … …\x01",
            "Anyway, it was nice.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2EA7")

    TalkEnd(0xFE)
    Return()

    # Function_11_215C end

    def Function_12_2EAB(): pass

    label("Function_12_2EAB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2FA8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F37")

    ChrTalk(
        0xA,
        (
            "Everyone's father and miners,\x01",
            "Today I joined the mine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Everyone seemed happy … …\x01",
            "Eh, I am happy too.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2FA3")

    label("loc_2F37")


    ChrTalk(
        0xA,
        (
            "That huge tree\x01",
            "It is uneasy that I came out,\x01",
            "I am glad that the mine has resumed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Dads, I hope you do your best.\x02",
    )

    CloseMessageWindow()

    label("loc_2FA3")

    Jump("loc_37F3")

    label("loc_2FA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_302B")

    ChrTalk(
        0xA,
        (
            "Recently, many wolves\x01",
            "Everyone in resistance\x01",
            "It is helping.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It is a very clever wolf.\x01",
            "Do not depend on ~.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37F3")

    label("loc_302B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_3159")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30C9")

    ChrTalk(
        0xA,
        (
            "Because this is the situation\x01",
            "Mines are on holidays too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Dad is at home\x01",
            "I'm pleased, but … after all,\x01",
            "It seems that it is kind of boring.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3154")

    label("loc_30C9")


    ChrTalk(
        0xA,
        (
            "The mine is on holiday,\x01",
            "My father seems to be boring.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I, too, as my father as a minister\x01",
            "I like to work. ……\x01",
            "I hope to resume soon.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3154")

    Jump("loc_37F3")

    label("loc_3159")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_32E5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3251")

    ChrTalk(
        0xA,
        (
            "When those bad guys came,\x01",
            "Miners to protect the town\x01",
            "I faced up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "But, after all it does not come … …\x01",
            "My father was thrust away,\x01",
            "I got hurt.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It was not a big injury,\x01",
            "I was sooo worried … …\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_32E0")

    label("loc_3251")


    ChrTalk(
        0xA,
        (
            "Dads to protect the town\x01",
            "I fought against the bad guy ….\x01",
            "I did not do it after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I did not get hurt so much,\x01",
            "I was sooo worried.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32E0")

    Jump("loc_37F3")

    label("loc_32E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_32F3")
    Jump("loc_37F3")

    label("loc_32F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3358")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_330E")
    Call(0, 13)
    Jump("loc_3353")

    label("loc_330E")


    ChrTalk(
        0xA,
        (
            "Hahaha, Yamabiko\x01",
            "Interesting, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "I'm going to shout next time.\x02",
    )

    CloseMessageWindow()

    label("loc_3353")

    Jump("loc_37F3")

    label("loc_3358")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3489")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3447")

    ChrTalk(
        0xA,
        (
            "Rosie, recently not at all\x01",
            "You did not skip work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I'm just doing yeah yeah\x01",
            "I told you in the mouth ….\x01",
            "The face looked very funny.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I can do it while enjoying my work\x01",
            "I want to become a fine minister.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3484")

    label("loc_3447")


    ChrTalk(
        0xA,
        (
            "I can do it while enjoying my work\x01",
            "I want to become a fine minister.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3484")

    Jump("loc_37F3")

    label("loc_3489")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_35D6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_354F")

    ChrTalk(
        0xA,
        (
            "Today is here\x01",
            "There was a Sunday school class.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It's a sister that always comes\x01",
            "I did not have it, but I was very kind\x01",
            "It taught me studies carefully.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Well, I want to see you again.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_35D1")

    label("loc_354F")


    ChrTalk(
        0xA,
        (
            "今日はIt's a sister that always comes\x01",
            "I did not have it, but I was very kind\x01",
            "It taught me studies carefully.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Well, I want to see you again.\x02",
    )

    CloseMessageWindow()

    label("loc_35D1")

    Jump("loc_37F3")

    label("loc_35D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_36C5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3677")

    ChrTalk(
        0xA,
        "Shun\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Yesterday, my father and mother\x01",
            "I was scolded solely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I entered the depth of the mine,\x01",
            "I wish I could not have done so much.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_36C0")

    label("loc_3677")


    ChrTalk(
        0xA,
        (
            "I entered the depth of the mine,\x01",
            "I wish I could not have done so much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Shun\x02",
    )

    CloseMessageWindow()

    label("loc_36C0")

    Jump("loc_37F3")

    label("loc_36C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_36D3")
    Jump("loc_37F3")

    label("loc_36D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_37F3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_379A")

    ChrTalk(
        0xA,
        (
            "As I saw this morning,\x01",
            "The old mine outside the town\x01",
            "Tibira was open.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "When trying to enter Kosori,\x01",
            "I was immediately found by Mr. Ganz.\x01",
            "I got scolded.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Well, I wanted to explore.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_37F3")

    label("loc_379A")


    ChrTalk(
        0xA,
        (
            "Old mine, explore from the front\x01",
            "I wanted to see it ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "I got scolded, I guess.\x02",
    )

    CloseMessageWindow()

    label("loc_37F3")

    TalkEnd(0xFE)
    Return()

    # Function_12_2EAB end

    def Function_13_37F7(): pass

    label("Function_13_37F7")

    OP_4B(0xA, 0xFF)
    OP_4B(0xC, 0xFF)

    ChrTalk(
        0xA,
        "#4SDo it! It is!\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(300, 30, -1, -1)
    SetChrName("Yamabiko")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "…… Well ……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()

    ChrTalk(
        0xC,
        "#4SI love you!\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(300, 30, -1, -1)
    SetChrName("Yamabiko")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "… … Isuzu …… Snow …\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    ClearChrFlags(0xA, 0x10)
    ClearChrFlags(0xC, 0x10)
    SetScenarioFlags(0x1, 1)
    OP_4C(0xA, 0xFF)
    OP_4C(0xC, 0xFF)
    Return()

    # Function_13_37F7 end

    def Function_14_38CB(): pass

    label("Function_14_38CB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_38DC")
    Jump("loc_3CF6")

    label("loc_38DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_3920")

    ChrTalk(
        0xB,
        "Haa ………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Mine, I do not want to resume … …\x02",
    )

    CloseMessageWindow()
    Jump("loc_3CF6")

    label("loc_3920")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_3A35")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39CA")

    ChrTalk(
        0xB,
        (
            "After becoming an independent country,\x01",
            "To the life full of like before\x01",
            "I feel I'm back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Ha ha … … Also for the work of miners\x01",
            "I must have been motivated.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3A30")

    label("loc_39CA")


    ChrTalk(
        0xB,
        (
            "Also for the work of miners\x01",
            "I must have been motivated.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "To life full of this as it is\x01",
            "I wonder whether it will go back ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A30")

    Jump("loc_3CF6")

    label("loc_3A35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3A43")
    Jump("loc_3CF6")

    label("loc_3A43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3A51")
    Jump("loc_3CF6")

    label("loc_3A51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3A5F")
    Jump("loc_3CF6")

    label("loc_3A5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3A6D")
    Jump("loc_3CF6")

    label("loc_3A6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3A7B")
    Jump("loc_3CF6")

    label("loc_3A7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3A89")
    Jump("loc_3CF6")

    label("loc_3A89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3A97")
    Jump("loc_3CF6")

    label("loc_3A97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_3CF6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x188, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BB0")

    ChrTalk(
        0xB,
        (
            "I, while sometimes sorry while before\x01",
            "I was working daddy … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Recently I have not done so,\x01",
            "I do not have time to read books.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "There is no point in having this book ……,\x01",
            "I'll do it for you.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '沐浴阳光的阿尼艾丝２卷'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('沐浴阳光的阿尼艾丝２卷', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x188, 1)
    Jump("loc_3CF6")

    label("loc_3BB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CAB")

    ChrTalk(
        0xB,
        (
            "As I used to be\x01",
            "Sometimes skipping\x01",
            "I'd like to go daradara … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Recently, everyone else is ticking\x01",
            "It is hard to skip.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "It's time to motivate you\x01",
            "I guess it may be a wrong time.\x01",
            "Haa, it is troublesome …\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3CF6")

    label("loc_3CAB")


    ChrTalk(
        0xB,
        (
            "…… Now I do not have a separate skill.\x01",
            "I got a break and it was dull.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3CF6")

    TalkEnd(0xFE)
    Return()

    # Function_14_38CB end

    def Function_15_3CFA(): pass

    label("Function_15_3CFA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3D0B")
    Jump("loc_3EFF")

    label("loc_3D0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3D19")
    Jump("loc_3EFF")

    label("loc_3D19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3DA5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D34")
    Call(0, 13)
    Jump("loc_3DA0")

    label("loc_3D34")


    ChrTalk(
        0xC,
        (
            "That's amazing,\x01",
            "The voice came back properly!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Even on that mountain side,\x01",
            "Kimiみたいな子がいるのかな？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3DA0")

    Jump("loc_3EFF")

    label("loc_3DA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3DB3")
    Jump("loc_3EFF")

    label("loc_3DB3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3EDA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E6B")

    ChrTalk(
        0xC,
        (
            "If Sister,\x01",
            "I have already returned to the church ~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "By the way, when I return home\x01",
            "The sky over there\x01",
            "It seems I was concerned … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Well, I wonder if there is something.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_3ED5")

    label("loc_3E6B")


    ChrTalk(
        0xC,
        (
            "Sister,\x01",
            "帰るときにThe sky over there\x01",
            "It seems I was concerned … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Well, I wonder if there is something.\x02",
    )

    CloseMessageWindow()

    label("loc_3ED5")

    Jump("loc_3EFF")

    label("loc_3EDA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3EE8")
    Jump("loc_3EFF")

    label("loc_3EE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3EF6")
    Jump("loc_3EFF")

    label("loc_3EF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_3EFF")

    label("loc_3EFF")

    TalkEnd(0xFE)
    Return()

    # Function_15_3CFA end

    def Function_16_3F03(): pass

    label("Function_16_3F03")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3F14")
    Jump("loc_400D")

    label("loc_3F14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_4004")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3FC4")

    ChrTalk(
        0xD,
        (
            "We want to do something, but …\x01",
            "Resister 's older sisters\x01",
            "I suppose I can not help it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "…… After all, what can be done as a miner\x01",
            "You only have to drill holes ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_3FFF")

    label("loc_3FC4")


    ChrTalk(
        0xD,
        (
            "…… After all, what can be done as a miner\x01",
            "You only have to drill holes ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3FFF")

    Jump("loc_400D")

    label("loc_4004")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_400D")

    label("loc_400D")

    TalkEnd(0xFE)
    Return()

    # Function_16_3F03 end

    def Function_17_4011(): pass

    label("Function_17_4011")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4022")
    Jump("loc_4159")

    label("loc_4022")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_4150")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_40CC")

    ChrTalk(
        0xE,
        (
            "To Lucca-chan\x01",
            "I'm forced out of a bar.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Resistance leader\x01",
            "I'm going to take a good rest,\x01",
            "Well I can not help it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_414B")

    label("loc_40CC")


    ChrTalk(
        0xE,
        (
            "…… Even so,\x01",
            "From work of mining for such a long time\x01",
            "It is the first time I left.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I can not afford to be so far\x01",
            "I never thought that … …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_414B")

    Jump("loc_4159")

    label("loc_4150")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_4159")

    label("loc_4159")

    TalkEnd(0xFE)
    Return()

    # Function_17_4011 end

    def Function_18_415D(): pass

    label("Function_18_415D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BC, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_43AF")

    ChrTalk(
        0xFE,
        (
            "Mainz Mineの再開に当たって、\x01",
            "Demon beasts with high danger of being springing up\x01",
            "I'm getting rid of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Compared to \"magic guards\" and \"phantom beasts\"\x01",
            "Although it was not a big deal,\x01",
            "The devastation of monsters by one person has been broken.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FHaha …. It is amazing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00304FTruly from the Empire Guild\x01",
            "Wonder who is an arbitrary haste fighter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Fu, I and I have a lot more.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… In the empire is a civil war,\x01",
            "What do you do in the old nest.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xFE)

    ChrTalk(
        0xFE,
        "… Well, let's stop it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Handle things in front of you as top priority …\x01",
            "To those who can not do it, look back on the past\x01",
            "Because there is no qualification that wants the future.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F(You are as hard as ever.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BC, 3)
    Jump("loc_447F")

    label("loc_43AF")


    ChrTalk(
        0xFE,
        (
            "Despite detaining the president,\x01",
            "Crossbell is also in a situation where you can not get in and out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… They are resting at the inn,\x01",
            "When physical fitness returns, variously\x01",
            "You will be asked to help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Maybe it is painful time … ….\x01",
            "Now is the cornerstone.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_447F")

    TalkEnd(0xFE)
    Return()

    # Function_18_415D end

    def Function_19_4483(): pass

    label("Function_19_4483")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4524")

    ChrTalk(
        0xFE,
        (
            "Mainz mountain range,\x01",
            "The challenge a while ago has failed … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even if it takes years to train your legs\x01",
            "I will definitely go over it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "…… Tentatively, declaration of determination.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_457B")

    label("loc_4524")


    ChrTalk(
        0xFE,
        (
            "I also made a commitment expressed … …\x01",
            "I guess I should return home soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'd like to see my friends for the first time in a while.\x02",
    )

    CloseMessageWindow()

    label("loc_457B")

    TalkEnd(0xFE)
    Return()

    # Function_19_4483 end

    def Function_20_457F(): pass

    label("Function_20_457F")

    SetMapFlags(0x80)
    SetMapFlags(0x8000000)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x31, 2)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_45B1")
    SetScenarioFlags(0x31, 2)

    label("loc_45B1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_45F7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_45F1")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_45E6")
    Sound(2499, 255, 100, 0)
    Jump("loc_45EC")

    label("loc_45E6")

    Sound(3537, 255, 100, 0)

    label("loc_45EC")

    Jump("loc_45F7")

    label("loc_45F1")

    Sound(3344, 255, 100, 0)

    label("loc_45F7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_48B4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_4670")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "Board Mercapa")
    MenuCmd(1, 0, "quit")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4650"),
        (SWITCH_DEFAULT, "loc_4661"),
    )


    label("loc_4650")

    SetScenarioFlags(0x22, 0)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Jump("loc_466B")

    label("loc_4661")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_466B")

    Jump("loc_48AF")

    label("loc_4670")

    MenuCmd(0, 0)
    MenuCmd(1, 0, "導力carで移動する")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_46A4")
    MenuCmd(1, 0, "導力carで休憩する")

    label("loc_46A4")

    MenuCmd(1, 0, "quit")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_46D8"),
        (1, "loc_47DC"),
        (2, "loc_486D"),
        (SWITCH_DEFAULT, "loc_48A5"),
    )


    label("loc_46D8")

    SetMapObjFrame(0x9, "light", 0x0, 0x1)
    OP_74(0x9, 0x1E)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_4709")
    OP_70(0x9, 0x12C)
    OP_71(0x9, 0x12C, 0x14A, 0x0, 0x0)
    Jump("loc_4719")

    label("loc_4709")

    OP_70(0x9, 0xF0)
    OP_71(0x9, 0xF0, 0x10E, 0x0, 0x0)

    label("loc_4719")

    Sound(462, 0, 100, 0)
    SoundLoad(2500)
    SoundLoad(3538)
    SoundLoad(3345)
    Sleep(700)
    FadeToDark(300, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_476F")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_476F")

    FadeToDark(0, 0, -1)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4792")
    Sound(461, 0, 100, 0)

    label("loc_4792")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_47B2")
    OP_70(0x9, 0x14A)
    OP_71(0x9, 0x14A, 0x12C, 0x0, 0x0)
    Jump("loc_47C2")

    label("loc_47B2")

    OP_70(0x9, 0x10E)
    OP_71(0x9, 0x10E, 0xF0, 0x0, 0x0)

    label("loc_47C2")

    Sleep(1000)
    OP_0D()
    SetMapObjFrame(0x9, "light", 0x1, 0x1)
    OP_70(0x9, 0x0)
    Jump("loc_45F7")

    label("loc_47DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_484E")
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 0)), scpexpr(EXPR_END)), "loc_4811")
    OP_32(0xFF, 0xFF, 0x0)
    Jump("loc_4829")

    label("loc_4811")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_4824")
    OP_32(0xFF, 0xFE, 0x0)
    Jump("loc_4829")

    label("loc_4824")

    OP_32(0xFF, 0xFA, 0x0)

    label("loc_4829")

    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4868")

    label("loc_484E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_485E")
    OP_AF(0xFB)
    Jump("loc_4868")

    label("loc_485E")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4868")

    Jump("loc_48AF")

    label("loc_486D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4886")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_48A0")

    label("loc_4886")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_4896")
    OP_AF(0xFB)
    Jump("loc_48A0")

    label("loc_4896")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_48A0")

    Jump("loc_48AF")

    label("loc_48A5")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_48AF")

    Jump("loc_45F7")

    label("loc_48B4")

    ClearMapFlags(0x8000000)
    OP_60(0x0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    # Function_20_457F end

    def Function_21_48C2(): pass

    label("Function_21_48C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_490A")
    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "導力busは運行を見合わせているようだ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Return()

    label("loc_490A")

    Call(0, 6)
    Return()

    # Function_21_48C2 end

    def Function_22_490E(): pass

    label("Function_22_490E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4A69")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "── Lloyd's who returned to Mainz\x01",
            "I explained a couple of circumstances to the town mayors.\x02\x03",
            "But destroying the door of the old mine entrance,\x01",
            "The criminal who set the explosive was not revealed,\x01",
            "There was no explanation for abnormality in the tunnel.\x02\x03",
            "Then check the neighborhood again\x01",
            "After confirming that there is no suspicious person ……\x02\x03",
            "Lloyds asked the guard for a patrol\x01",
            "I decided to return to Cros Bell City.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_4A69")

    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xCC, 0x8F, 0x85, 0x0, 0xE6, 0x0)
    LoadChrToIndex("chr/ch02702.itc", 0x1E)
    LoadChrToIndex("chr/ch23200.itc", 0x1F)
    LoadChrToIndex("chr/ch20100.itc", 0x20)
    LoadChrToIndex("chr/ch30700.itc", 0x21)
    LoadChrToIndex("chr/ch26300.itc", 0x22)
    LoadChrToIndex("chr/ch26200.itc", 0x23)
    LoadChrToIndex("chr/ch23700.itc", 0x24)
    LoadChrToIndex("chr/ch02750.itc", 0x25)
    LoadChrToIndex("chr/ch02751.itc", 0x26)
    ClearChrFlags(0x18, 0x80)
    OP_78(0x9, 0x18)
    OP_49()
    SetChrPos(0x18, -4500, -2000, 18000, 180)
    OP_D5(0x18, 0x0, 0x2BF20, 0x0, 0x0)
    ClearMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0x9, 0x1000)
    SetMapObjFrame(0x9, "light", 0x0, 0x1)
    OP_74(0x9, 0x1E)
    OP_93(0x18, 0xB4, 0x0)
    SetChrChipByIndex(0x19, 0x1E)
    SetChrSubChip(0x19, 0x0)
    ClearChrFlags(0x19, 0x80)
    SetChrFlags(0x19, 0x8000)
    SetChrChipByIndex(0x1A, 0x1F)
    SetChrSubChip(0x1A, 0x0)
    ClearChrFlags(0x1A, 0x80)
    SetChrFlags(0x1A, 0x8000)
    SetChrChipByIndex(0x1B, 0x20)
    SetChrSubChip(0x1B, 0x0)
    ClearChrFlags(0x1B, 0x80)
    SetChrFlags(0x1B, 0x8000)
    SetChrChipByIndex(0xD, 0x21)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    SetChrChipByIndex(0x1D, 0x22)
    SetChrSubChip(0x1D, 0x0)
    ClearChrFlags(0x1D, 0x80)
    SetChrFlags(0x1D, 0x8000)
    SetChrChipByIndex(0xE, 0x23)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)
    SetChrChipByIndex(0x1C, 0x23)
    SetChrSubChip(0x1C, 0x0)
    ClearChrFlags(0x1C, 0x80)
    SetChrFlags(0x1C, 0x8000)
    SetChrChipByIndex(0xB, 0x23)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrChipByIndex(0x8, 0x24)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x8000)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x8, 0x4)
    SetChrPos(0xD, -1200, -2000, 26750, 180)
    SetChrPos(0x1A, 0, -2000, 26400, 180)
    SetChrPos(0x1B, 1200, -2000, 26750, 180)
    SetChrPos(0x8, 1900, 0, 37500, 180)
    SetChrPos(0x1D, -600, -1710, 30570, 180)
    SetChrPos(0xE, -1600, -1370, 31750, 180)
    SetChrPos(0x1C, -300, -1370, 31750, 180)
    SetChrPos(0xB, 600, -1370, 31750, 180)
    SetChrPos(0x19, -2800, -2000, 23750, 30)
    OP_4B(0xD, 0xFF)
    OP_4B(0x1A, 0xFF)
    OP_4B(0x1B, 0xFF)
    OP_4B(0x8, 0xFF)
    OP_4B(0x1D, 0xFF)
    OP_4B(0xE, 0xFF)
    OP_4B(0x1C, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_52(0x19, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x101, 900, -2000, 24000, 0)
    SetChrPos(0x102, -900, -2000, 24000, 0)
    SetChrPos(0x109, -1100, -2000, 22600, 0)
    SetChrPos(0x105, 1100, -2000, 22600, 0)
    SetChrPos(0x104, 0, -2000, 23200, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_68(0, -550, 25080, 0)
    MoveCamera(306, 31, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18500, 0)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    BeginChrThread(0xD, 2, 0, 24)
    BeginChrThread(0x1A, 2, 0, 24)
    BeginChrThread(0x1B, 2, 0, 24)
    PlayBGM("ed7102", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1000, 0)
    OP_0D()
    BeginChrThread(0xD, 3, 0, 27)
    BeginChrThread(0x1A, 3, 0, 25)
    BeginChrThread(0x1B, 3, 0, 26)
    Sleep(1000)
    BeginChrThread(0x101, 3, 0, 29)
    BeginChrThread(0x102, 3, 0, 30)
    BeginChrThread(0x109, 3, 0, 31)
    BeginChrThread(0x105, 3, 0, 32)
    BeginChrThread(0x104, 3, 0, 33)
    BeginChrThread(0x19, 3, 0, 34)
    Sleep(300)
    OP_68(-4540, -350, 17850, 3500)
    Sleep(5000)
    MoveCamera(341, 18, 0, 3500)
    OP_6E(600, 3500)
    SetCameraDistance(16400, 3500)
    OP_6F(0x79)
    Sleep(500)
    Sleep(1000)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    BeginChrThread(0x8, 3, 0, 28)
    OP_68(-4540, -350, 17850, 2000)
    MoveCamera(341, 22, 0, 2000)
    OP_6E(600, 2000)
    SetCameraDistance(21360, 2000)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x109, 3)
    WaitChrThread(0x105, 3)
    WaitChrThread(0x104, 3)
    WaitChrThread(0x19, 3)
    Sound(461, 0, 100, 0)
    OP_71(0x9, 0x1F, 0x3C, 0x0, 0x0)
    OP_79(0x9)
    Sleep(1500)
    OP_68(-140, -350, 5080, 4000)
    MoveCamera(333, 15, 0, 4000)
    OP_6E(600, 4000)
    SetCameraDistance(21360, 4000)
    Sound(457, 0, 100, 0)
    Sound(494, 0, 60, 0)
    BeginChrThread(0x18, 3, 0, 36)
    OP_71(0x9, 0x3C, 0x5A, 0x0, 0x0)
    BeginChrThread(0x18, 2, 0, 23)
    WaitChrThread(0x18, 2)
    OP_6F(0x79)
    WaitChrThread(0x8, 3)
    StopSound(457, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 1)
    NewScene("r2060", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_22_490E end

    def Function_23_4EAA(): pass

    label("Function_23_4EAA")

    OP_79(0x9)
    OP_71(0x9, 0x79, 0xB4, 0x0, 0x20)
    Return()

    # Function_23_4EAA end

    def Function_24_4EBA(): pass

    label("Function_24_4EBA")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4ED5")
    Sleep(300)
    Jump("loc_4F29")

    label("loc_4ED5")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x46), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4EF0")
    Sleep(600)
    Jump("loc_4F29")

    label("loc_4EF0")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x3C), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4F0B")
    Sleep(900)
    Jump("loc_4F29")

    label("loc_4F0B")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4F26")
    Sleep(1200)
    Jump("loc_4F29")

    label("loc_4F26")

    Sleep(1500)

    label("loc_4F29")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4F54")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_64(0xFE)
    Sleep(500)
    Jump("loc_4F29")

    label("loc_4F54")

    Return()

    # Function_24_4EBA end

    def Function_25_4F55(): pass

    label("Function_25_4F55")

    Return()

    # Function_25_4F55 end

    def Function_26_4F56(): pass

    label("Function_26_4F56")

    Return()

    # Function_26_4F56 end

    def Function_27_4F57(): pass

    label("Function_27_4F57")

    Return()

    # Function_27_4F57 end

    def Function_28_4F58(): pass

    label("Function_28_4F58")

    OP_9B(0x0, 0xFE, 0x1, 0x2328, 0x7D0, 0x0)
    OP_9B(0x0, 0xFE, 0x50, 0xFA0, 0x7D0, 0x0)
    OP_93(0xFE, 0xB4, 0x0)
    OP_63(0xFE, 0x0, 1700, 0xA, 0xB, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Return()

    # Function_28_4F58 end

    def Function_29_4F96(): pass

    label("Function_29_4F96")

    Sleep(2000)
    OP_93(0xFE, 0xB4, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x11F8, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0x7D0, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0x384, 0x3E8, 0x0)
    Sleep(600)
    OP_9B(0x0, 0xFE, 0x0, 0x514, 0x3E8, 0x0)
    TurnDirection(0xFE, 0x1A, 500)
    Sleep(1000)
    OP_93(0xFE, 0x10E, 0x1F4)

    def lambda_4FF5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4FF5)
    OP_9B(0x0, 0xFE, 0x0, 0xFA, 0x3E8, 0x1)
    Sleep(500)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_29_4F96 end

    def Function_30_5019(): pass

    label("Function_30_5019")

    Sleep(2500)
    OP_93(0xFE, 0x10E, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x159, 0x1194, 0x7D0, 0x1)
    TurnDirection(0xFE, 0x1A, 500)
    Sleep(1000)
    OP_93(0xFE, 0xFF, 0x1F4)
    OP_9B(0x0, 0xFE, 0x14A, 0x1F4, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x13B, 0x1130, 0x7D0, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Sleep(200)

    def lambda_507F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_507F)
    OP_9B(0x0, 0xFE, 0x0, 0xFA, 0x3E8, 0x1)
    Sleep(500)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_30_5019 end

    def Function_31_50A3(): pass

    label("Function_31_50A3")

    OP_93(0xFE, 0x10E, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x159, 0xDAC, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x14A, 0x1F4, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x13B, 0xE10, 0x7D0, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Sleep(200)
    Sound(462, 0, 100, 0)
    OP_71(0x9, 0x1, 0x1E, 0x0, 0x0)
    Sleep(700)

    def lambda_510A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_510A)
    OP_9B(0x0, 0xFE, 0x0, 0xFA, 0x3E8, 0x1)
    Sleep(500)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_31_50A3 end

    def Function_32_512E(): pass

    label("Function_32_512E")

    Sleep(800)
    OP_93(0xFE, 0xB4, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0xDAC, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0xF, 0x1F4, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x1E, 0x3E8, 0x7D0, 0x0)
    TurnDirection(0xFE, 0x1A, 500)
    Sleep(1000)
    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(700)

    def lambda_518D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_518D)
    OP_9B(0x0, 0xFE, 0x0, 0xFA, 0x3E8, 0x1)
    Sleep(500)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_32_512E end

    def Function_33_51B1(): pass

    label("Function_33_51B1")

    Sleep(1200)
    OP_93(0xFE, 0x10E, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x13B, 0x9C4, 0xBB8, 0x1)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(500)
    OP_9B(0x1, 0xFE, 0x5A, 0x1F4, 0x3E8, 0x0)
    Sleep(500)
    OP_9B(0x1, 0xFE, 0x10E, 0x6A4, 0x7D0, 0x0)
    OP_9B(0x0, 0xFE, 0x13B, 0x4B0, 0xBB8, 0x0)
    OP_9B(0x0, 0xFE, 0x2D, 0x1450, 0xBB8, 0x0)
    OP_9B(0x0, 0xFE, 0x2D, 0x3E8, 0xBB8, 0x0)
    OP_9B(0x0, 0xFE, 0x2D, 0x320, 0xBB8, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(300)
    OP_93(0xFE, 0x13B, 0x1F4)
    Sleep(700)
    OP_93(0xFE, 0x0, 0x1F4)
    OP_9B(0x0, 0xFE, 0x2D, 0x5DC, 0xBB8, 0x0)
    OP_9B(0x0, 0xFE, 0x13B, 0x898, 0xBB8, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)

    def lambda_5285():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5285)
    OP_9B(0x0, 0xFE, 0x0, 0xFA, 0x3E8, 0x1)
    Sleep(500)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_33_51B1 end

    def Function_34_52A9(): pass

    label("Function_34_52A9")

    Sleep(1600)
    SetChrSubChip(0x19, 0x0)
    SetChrChipByIndex(0x19, 0x25)
    OP_93(0xFE, 0x10E, 0x1F4)
    BeginChrThread(0x1E, 1, 0, 35)
    SetChrChipByIndex(0x19, 0x26)
    OP_9B(0x0, 0xFE, 0x0, 0x157C, 0x1388, 0x1)
    OP_9B(0x0, 0xFE, 0x13B, 0x5DC, 0x1388, 0x1)
    SetChrChipByIndex(0x19, 0x25)
    OP_93(0xFE, 0xB4, 0x1F4)
    SetChrChipByIndex(0x19, 0x1E)
    Sleep(1700)
    OP_93(0xFE, 0x87, 0x1F4)
    Sleep(1000)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(1000)
    SetChrChipByIndex(0x19, 0x26)
    OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x1770, 0x1)
    OP_52(0x19, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChip(0x0, 0x19, 0x32, 0x2EE)
    Sound(844, 0, 60, 0)
    OP_9C(0xFE, 0x0, 0x1770, 0xFFFFD8F0, 0x1770, 0x5DC)
    Return()

    # Function_34_52A9 end

    def Function_35_534D(): pass

    label("Function_35_534D")

    Sound(845, 0, 40, 0)
    Sleep(400)
    Sound(845, 0, 40, 0)
    Sleep(400)
    Sound(845, 0, 40, 0)
    Sleep(400)
    Sound(845, 0, 40, 0)
    Sleep(400)
    Sound(845, 0, 40, 0)
    Sleep(3700)
    Sound(845, 0, 40, 0)
    Sleep(400)
    Sound(845, 0, 40, 0)
    Return()

    # Function_35_534D end

    def Function_36_538A(): pass

    label("Function_36_538A")

    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -4500, -2000, 18000)
    OP_9F(0x1, -4500, -2000, 16000)
    OP_9F(0x1, -4000, -2000, 12000)
    OP_9F(0x1, -1500, -2000, 6000)
    OP_9F(0x1, 500, -2000, 0)
    OP_9F(0x1, 500, -2000, -12000)
    OP_9F(0x2, 0xFE, 4500, 0x6)
    Return()

    # Function_36_538A end

    def Function_37_53EC(): pass

    label("Function_37_53EC")

    OP_68(-43420, -550, 73000, 0)
    MoveCamera(316, 21, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(71020, 0)
    Fade(500)
    OP_68(-10650, -4950, 66450, 7500)
    MoveCamera(305, 21, 0, 7500)
    OP_6E(600, 7500)
    SetCameraDistance(63120, 7500)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    OP_68(-14770, -4950, 77970, 0)
    MoveCamera(324, 21, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(69590, 0)
    Fade(500)
    OP_68(-6010, -4950, 47080, 7000)
    MoveCamera(332, 15, 0, 7000)
    OP_6E(600, 7000)
    SetCameraDistance(69590, 7000)
    Sleep(1000)
    PlaceName2(340, 200, "c_plac17", 0x0, 0)
    OP_6F(0x79)
    Return()

    # Function_37_53EC end

    def Function_38_54CD(): pass

    label("Function_38_54CD")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x101, -100, -2000, 6950, 0)
    SetChrPos(0x102, 1140, -2000, 6260, 0)
    SetChrPos(0x109, -500, -2000, 5130, 0)
    SetChrPos(0x105, 770, -2000, 4350, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    BeginChrThread(0x101, 3, 0, 39)
    Call(0, 37)
    Fade(500)
    OP_68(490, -550, 19950, 0)
    MoveCamera(335, 17, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15430, 0)
    OP_0D()
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    Sleep(300)
    OP_93(0x101, 0x87, 0x1F4)
    Sound(2092, 255, 80, 0)

    ChrTalk(
        0x101,
        (
            "#00006F#5PFuu …\x01",
            "Were you walking all this way after all?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x102, 0xE1, 0x1F4)

    ChrTalk(
        0x102,
        "#00100F#11PNoel, Wazy, are you all right?\x02",
    )

    CloseMessageWindow()
    OP_93(0x109, 0x2D, 0x1F4)

    ChrTalk(
        0x109,
        "#10102F#6PYeah, do not worry.\x02",
    )

    CloseMessageWindow()
    OP_93(0x105, 0x13B, 0x1F4)
    Sleep(150)

    ChrTalk(
        0x105,
        (
            "#10306F#6PI am fine, though ….\x01",
            "The support department is really drunk.\x02\x03",
            "#10301F素直にcarとか\x01",
            "busを使えばいいのに。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#5PHe will be training as well.\x01",
            "You two birds with one stone right?\x02\x03",
            "#00004FEven so ……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00012F#5PEllie was really stamina.\x02\x03",
            "#00000FAt first, just walking a little on the highway\x01",
            "It was a breath.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(100)

    ChrTalk(
        0x102,
        (
            "#00109F#12PHuh, thanks to someone\x01",
            "Because I was trained.\x02\x03",
            "#00100FSo what are you going to do?\x01",
            "Why do not you visit the town mayor?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#5POh, let's do that.\x02\x03",
            "#00000FThe town mayor's house enters the town\x01",
            "Do not go to the end you went straight.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 900, -2000, 20280, 0)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x129, 5)
    SetScenarioFlags(0x12A, 5)
    OP_29(0xA1, 0x1, 0x13)
    ClearMapFlags(0x10000000)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_38_54CD end

    def Function_39_58A2(): pass

    label("Function_39_58A2")

    Sleep(5500)

    def lambda_58AA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_58AA)

    def lambda_58BB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_58BB)

    def lambda_58CC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_58CC)

    def lambda_58DD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_58DD)
    BeginChrThread(0x101, 0, 0, 40)
    BeginChrThread(0x102, 0, 0, 41)
    BeginChrThread(0x109, 0, 0, 42)
    BeginChrThread(0x105, 0, 0, 43)
    Return()

    # Function_39_58A2 end

    def Function_40_5902(): pass

    label("Function_40_5902")

    OP_9B(0x0, 0xFE, 0x0, 0x36B0, 0x7D0, 0x0)
    Return()

    # Function_40_5902 end

    def Function_41_5912(): pass

    label("Function_41_5912")

    Sleep(50)
    OP_9B(0x0, 0xFE, 0x0, 0x3714, 0x7D0, 0x0)
    Return()

    # Function_41_5912 end

    def Function_42_5925(): pass

    label("Function_42_5925")

    Sleep(100)
    OP_9B(0x0, 0xFE, 0x0, 0x37DC, 0x7D0, 0x0)
    Return()

    # Function_42_5925 end

    def Function_43_5938(): pass

    label("Function_43_5938")

    Sleep(150)
    OP_9B(0x0, 0xFE, 0x0, 0x38A4, 0x7D0, 0x0)
    Return()

    # Function_43_5938 end

    def Function_44_594B(): pass

    label("Function_44_594B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x101, 3750, -2000, 26000, 270)
    SetChrPos(0x102, 3750, -2000, 26000, 270)
    SetChrPos(0x109, 3750, -2000, 26000, 270)
    SetChrPos(0x105, 3750, -2000, 26000, 270)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x18, 0x80)
    ClearMapObjFlags(0x9, 0x4)
    ClearMapObjFlags(0x9, 0x1000)
    OP_78(0x9, 0x18)
    SetMapObjFrame(0x9, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0x18, 0, -2000, -500, 0)
    OP_D5(0x18, 0x0, 0x1B58, 0x0, 0x0)
    SetMapObjFlags(0x9, 0x1000)
    OP_74(0x9, 0x1E)
    OP_71(0x9, 0x79, 0xB4, 0x0, 0x20)
    BeginChrThread(0x101, 3, 0, 45)
    Call(0, 37)
    OP_0D()
    WaitChrThread(0x101, 3)
    OP_6F(0x79)
    SetCameraDistance(55590, 5500)
    WaitChrThread(0x18, 0)
    OP_6F(0x79)
    OP_68(2740, -550, 25130, 0)
    MoveCamera(335, 26, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14100, 0)
    Fade(500)
    OP_0D()
    Sound(462, 0, 100, 0)
    OP_74(0x9, 0x1E)
    OP_71(0x9, 0xF1, 0x10E, 0x1, 0x8)
    OP_79(0x9)
    BeginChrThread(0x101, 0, 0, 48)
    BeginChrThread(0x102, 0, 0, 49)
    BeginChrThread(0x105, 0, 0, 50)
    BeginChrThread(0x109, 0, 0, 51)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)

    def lambda_5ABD():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5ABD)
    Sleep(50)

    def lambda_5ACD():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_5ACD)
    Sleep(50)

    def lambda_5ADD():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_5ADD)
    Sleep(50)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5D9D")

    ChrTalk(
        0x102,
        (
            "#00104F#5PWhatching\x01",
            "It was a blink of an eye.\x02\x03",
            "#00100FAs I heard,\x01",
            "It seems that the mountain road direction is sunny.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#11POh, the scenery of the rain\x01",
            "It was beautiful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10109F#12Pうーん、でもこのcar、\x01",
            "It's a big deal.\x02\x03",
            "#10102FEven in a place like a mountain road\x01",
            "I will not shake much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F#6PAs expected it is ZCF.\x01",
            "It will likely be sold if it is released.\x02\x03",
            "#10300FSo, in this mining town\x01",
            "Does the mayor have a story?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102F#5Pええ、Mayor of Vixenという方よ。\x02\x03",
            "I entered the town and went straight.\x01",
            "It was the house at the end.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#11POh let's go.\x02\x03",
            "#00003F(… … in the middle of the mountain path\x01",
            "Was there a way to the puppet factory? )\x02\x03",
            "#00008F(Although there is no longer a lens, …\x01",
            "I wanted to go see a little bit. )\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6046")

    label("loc_5D9D")


    ChrTalk(
        0x105,
        (
            "#10305F#6POh, this is Mainz?\x02\x03",
            "#10302FI knew only the name but\x01",
            "It is my first time to come.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#11PWell, unless it is errands,\x01",
            "I guess there will be no opportunity to come.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F#5PBy the way, Mr. Noel\x01",
            "You quite come to Mainz, are not you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10104F#12PYes, regular patrol\x01",
            "Because it is also a course.\x02\x03",
            "#10102FBy the way, with the Special Affairs Support Division\x01",
            "There is a rim in the direction of Mainz.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#5PBy the way, that's right.\x02\x03",
            "#00000FMilitary dog cases and\x01",
            "Was it together with exploring the monastery?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#5PWell, well …\x01",
            "I remembered a bad thing.\x02\x03",
            "#00100FSo what are you going to do?\x01",
            "Why do not you visit the town mayor?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#11POh, let's do that.\x02\x03",
            "#00000FThe town mayor's house enters the town\x01",
            "Do not go to the end you went straight.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6046")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 2400, -2000, 25800, 270)
    ClearMapObjFlags(0x9, 0x1000)
    SetScenarioFlags(0x129, 6)
    SetScenarioFlags(0x12A, 5)
    OP_29(0xA1, 0x1, 0x13)
    ClearMapFlags(0x8000000)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_44_594B end

    def Function_45_607F(): pass

    label("Function_45_607F")

    Sleep(5500)
    BeginChrThread(0x18, 0, 0, 46)
    WaitChrThread(0x18, 0)
    BeginChrThread(0x18, 0, 0, 47)
    BeginChrThread(0x1E, 1, 0, 52)
    Return()

    # Function_45_607F end

    def Function_46_6099(): pass

    label("Function_46_6099")

    SetChrPos(0xFE, 0, -1950, -500, 0)
    OP_9B(0x1, 0xFE, 0x0, 0x2CEC, 0xFA0, 0x0)
    OP_9E(0xFE, 0xFFFFEC78, 0x2AF8, 0xFFFEB7E0, 0xBB8, 0x1)
    OP_9E(0xFE, 0xFFFFEC78, 0x2AF8, 0xFFFFF060, 0x7D0, 0x1)
    OP_71(0x9, 0x5B, 0x78, 0x1, 0x8)
    OP_9E(0xFE, 0xFFFFEC78, 0x2AF8, 0xFFFFF830, 0x3E8, 0x1)
    Sleep(300)
    Return()

    # Function_46_6099 end

    def Function_47_6108(): pass

    label("Function_47_6108")

    OP_74(0x9, 0xA)
    OP_71(0x9, 0xB4, 0x79, 0x0, 0x20)
    OP_9E(0xFE, 0xFFFFEC78, 0x6590, 0xFFFFF448, 0x7D0, 0x4)
    OP_9E(0xFE, 0xFFFFEC78, 0x6590, 0xFFFEC398, 0xBB8, 0x4)
    OP_9E(0xFE, 0xFFFFEC78, 0x6590, 0xFFFFF060, 0x7D0, 0x4)
    OP_9E(0xFE, 0xFFFFEC78, 0x6590, 0xFFFFF830, 0x3E8, 0x4)
    OP_70(0x9, 0x78)
    Return()

    # Function_47_6108 end

    def Function_48_6171(): pass

    label("Function_48_6171")


    def lambda_6176():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6176)
    OP_9B(0x1, 0xFE, 0x0, 0x1F4, 0x3E8, 0x0)
    OP_93(0xFE, 0x145, 0x1F4)
    OP_9B(0x1, 0xFE, 0x0, 0x546, 0x7D0, 0x0)
    OP_93(0xFE, 0x87, 0x1F4)
    Return()

    # Function_48_6171 end

    def Function_49_61AF(): pass

    label("Function_49_61AF")

    Sleep(1300)

    def lambda_61B7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_61B7)
    OP_9B(0x1, 0xFE, 0x0, 0x1F4, 0x3E8, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    OP_9B(0x1, 0xFE, 0x0, 0x6D6, 0x7D0, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_49_61AF end

    def Function_50_61F0(): pass

    label("Function_50_61F0")

    Sleep(2600)

    def lambda_61F8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_61F8)
    OP_9B(0x1, 0xFE, 0x0, 0x1F4, 0x3E8, 0x0)
    OP_93(0xFE, 0xD7, 0x1F4)
    OP_9B(0x1, 0xFE, 0x0, 0x546, 0x7D0, 0x0)
    OP_93(0xFE, 0x2D, 0x1F4)
    Return()

    # Function_50_61F0 end

    def Function_51_6231(): pass

    label("Function_51_6231")

    Sleep(3900)

    def lambda_6239():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6239)
    OP_9B(0x1, 0xFE, 0x0, 0x1F4, 0x3E8, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Sound(461, 0, 100, 0)
    OP_71(0x9, 0x10F, 0x12C, 0x1, 0x8)
    Sleep(600)
    SetChrFlags(0xFE, 0x1000)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x2)
    SetChrSubChip(0xFE, 0x1C)
    Sleep(300)
    ClearChrFlags(0xFE, 0x1000)
    ClearChrFlags(0xFE, 0x20)
    ClearChrFlags(0xFE, 0x2)
    SetChrSubChip(0xFE, 0x0)
    Sleep(300)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_51_6231 end

    def Function_52_62A4(): pass

    label("Function_52_62A4")

    Sound(494, 0, 50, 0)
    Sleep(2000)
    Sound(459, 0, 100, 0)
    Sleep(2300)
    Sound(492, 0, 60, 0)
    Return()

    # Function_52_62A4 end

    def Function_53_62BD(): pass

    label("Function_53_62BD")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x101, -1870, -2000, 27300, 180)
    SetChrPos(0x102, -1010, -2000, 26220, 270)
    SetChrPos(0x109, -2770, -2000, 26360, 90)
    SetChrPos(0x105, -2130, -2000, 25230, 0)
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0x102, 0x8)
    SetChrFlags(0x109, 0x8)
    SetChrFlags(0x105, 0x8)
    ClearChrFlags(0x11, 0x80)
    ClearMapObjFlags(0x8, 0x4)
    ClearMapObjFlags(0x8, 0x2)
    OP_78(0x8, 0x11)
    SetMapObjFrame(0x8, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0x11, 0, -1950, -2000, 0)
    OP_D5(0x11, 0x0, 0x0, 0x0, 0x0)
    SetMapObjFlags(0x8, 0x1000)
    OP_74(0x8, 0x1E)
    BeginChrThread(0x101, 3, 0, 54)
    Call(0, 37)
    WaitChrThread(0x101, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0x101, 0x8)
    ClearChrFlags(0x102, 0x8)
    ClearChrFlags(0x109, 0x8)
    ClearChrFlags(0x105, 0x8)
    SetChrPos(0x11, -6320, -1950, 21130, 180)
    OP_93(0x11, 0xB4, 0x0)

    def lambda_63BB():

        label("loc_63BB")

        TurnDirection(0xFE, 0x11, 500)
        Yield()
        Jump("loc_63BB")

    QueueWorkItem2(0x101, 2, lambda_63BB)

    def lambda_63CD():

        label("loc_63CD")

        TurnDirection(0xFE, 0x11, 500)
        Yield()
        Jump("loc_63CD")

    QueueWorkItem2(0x102, 2, lambda_63CD)

    def lambda_63DF():

        label("loc_63DF")

        TurnDirection(0xFE, 0x11, 500)
        Yield()
        Jump("loc_63DF")

    QueueWorkItem2(0x109, 2, lambda_63DF)

    def lambda_63F1():

        label("loc_63F1")

        TurnDirection(0xFE, 0x11, 500)
        Yield()
        Jump("loc_63F1")

    QueueWorkItem2(0x105, 2, lambda_63F1)
    OP_68(-1750, -550, 26120, 0)
    MoveCamera(335, 22, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15940, 0)
    Sleep(500)
    FadeToBright(1000, 0)
    Sleep(500)
    BeginChrThread(0x11, 0, 0, 56)
    OP_0D()
    Sleep(1500)
    Sleep(1500)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x105, 0x2)
    EndChrThread(0x109, 0x2)

    def lambda_645D():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_645D)
    Sleep(50)

    def lambda_646D():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_646D)
    Sleep(50)

    def lambda_647D():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_647D)
    Sleep(50)

    def lambda_648D():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_648D)
    Sleep(300)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6782")

    ChrTalk(
        0x102,
        (
            "#00104F#12PWhatching\x01",
            "It was a blink of an eye.\x02\x03",
            "#00100FAs I heard,\x01",
            "It seems that the mountain road direction is sunny.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#11POh, the scenery of the rain\x01",
            "It was beautiful.\x02\x03",
            "#00006Fしかし、せっかくcarがあるのに\x01",
            "ついbusに乗っちゃったな。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10109F#5PHeh.\x01",
            "あたしはbusも好きですよ。\x02\x03",
            "#10102FI feel relaxed\x01",
            "I do not think so.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F#6PBecause I rarely ride\x01",
            "Wonder if it was fresh.\x02\x03",
            "#10300FSo, in this mining town\x01",
            "Does the mayor have a story?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102F#12Pええ、Mayor of Vixenという方よ。\x02\x03",
            "I entered the town and went straight.\x01",
            "It was the house at the end.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#11POh let's go.\x02\x03",
            "#00003F(… … in the middle of the mountain path\x01",
            "Was there a way to the puppet factory? )\x02\x03",
            "#00008F(Although there is no longer a lens, …\x01",
            "I wanted to go see a little bit. )\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6A2D")

    label("loc_6782")


    ChrTalk(
        0x105,
        (
            "#10305F#6POh, this is Mainz?\x02\x03",
            "#10302FI knew only the name but\x01",
            "It is my first time to come.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#11PWell, unless it is errands,\x01",
            "I guess there will be no opportunity to come.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F#12PBy the way, Mr. Noel\x01",
            "You quite come to Mainz, are not you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10104F#5PYes, regular patrol\x01",
            "Because it is also a course.\x02\x03",
            "#10102FBy the way, with the Special Affairs Support Division\x01",
            "There is a rim in the direction of Mainz.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#11PBy the way, that's right.\x02\x03",
            "#00000FMilitary dog cases and\x01",
            "Was it together with exploring the monastery?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#12PWell, well …\x01",
            "I remembered a bad thing.\x02\x03",
            "#00100FSo what are you going to do?\x01",
            "Why do not you visit the town mayor?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#11POh, let's do that.\x02\x03",
            "#00000FThe town mayor's house enters the town\x01",
            "Do not go to the end you went straight.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6A2D")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrFlags(0x11, 0x80)
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x8, 0x2)
    SetChrPos(0x0, 590, -2000, 26270, 0)
    SetScenarioFlags(0x129, 7)
    SetScenarioFlags(0x12A, 5)
    OP_29(0xA1, 0x1, 0x13)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_53_62BD end

    def Function_54_6A6C(): pass

    label("Function_54_6A6C")

    Sleep(5500)
    Sleep(2200)
    Sound(473, 0, 100, 0)
    Sleep(300)
    OP_71(0x8, 0x79, 0xB4, 0x0, 0x20)
    BeginChrThread(0x11, 0, 0, 55)
    Sleep(2200)
    Sound(467, 0, 100, 0)
    Sleep(1000)
    WaitChrThread(0x11, 0)
    OP_79(0x8)
    Sleep(300)
    Return()

    # Function_54_6A6C end

    def Function_55_6AA4(): pass

    label("Function_55_6AA4")

    OP_74(0x8, 0xF)
    OP_71(0x8, 0x79, 0xB4, 0x0, 0x20)
    SetChrPos(0xFE, -850, -1950, 2000, 0)
    OP_9F(0x0, 0xFE)
    OP_93(0xFE, 0x0, 0x0)
    OP_9F(0x1, -3200, -1950, 8000)
    OP_9F(0x1, -5300, -1950, 13000)
    OP_9F(0x1, -6320, -1950, 17000)
    OP_9F(0x1, -6320, -1950, 19630)
    OP_9F(0x2, 0xFE, 4000, 0x6)
    OP_9B(0x1, 0xFE, 0x0, 0x1F4, 0xBB8, 0x1)
    OP_9B(0x1, 0xFE, 0x0, 0x1F4, 0x7D0, 0x1)
    OP_71(0x8, 0x5B, 0x78, 0x0, 0x0)
    OP_9B(0x1, 0xFE, 0x0, 0x1F4, 0x3E8, 0x1)
    Return()

    # Function_55_6AA4 end

    def Function_56_6B4B(): pass

    label("Function_56_6B4B")

    Sound(471, 0, 100, 0)
    OP_74(0x8, 0xF)
    OP_71(0x8, 0x79, 0xB4, 0x0, 0x20)
    SetChrPos(0xFE, -6320, -1950, 21130, 180)
    OP_93(0xFE, 0xB4, 0x0)
    OP_9B(0x1, 0xFE, 0x0, 0x15E, 0x3E8, 0x1)
    OP_9B(0x1, 0xFE, 0x0, 0x15E, 0x7D0, 0x1)
    OP_9B(0x1, 0xFE, 0x0, 0x15E, 0xBB8, 0x1)
    OP_9B(0x1, 0xFE, 0x0, 0x15E, 0xFA0, 0x1)
    OP_9B(0x1, 0xFE, 0x0, 0xBB8, 0x1388, 0x1)
    OP_9B(0x1, 0xFE, 0x13B, 0x1770, 0x1388, 0x1)
    ClearMapObjFlags(0x8, 0x1000)
    Return()

    # Function_56_6B4B end

    def Function_57_6BDA(): pass

    label("Function_57_6BDA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch31200.itc", 0x1E)
    LoadChrToIndex("chr/ch31300.itc", 0x1F)
    LoadChrToIndex("chr/ch32600.itc", 0x20)
    LoadChrToIndex("apl/ch51441.itc", 0x21)
    SoundLoad(803)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis409.itp")
    SetChrChipByIndex(0x12, 0x1E)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8000)
    SetChrChipByIndex(0x13, 0x1E)
    SetChrSubChip(0x13, 0x0)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8000)
    SetChrChipByIndex(0x14, 0x1F)
    SetChrSubChip(0x14, 0x0)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8000)
    SetChrChipByIndex(0x17, 0x20)
    SetChrSubChip(0x17, 0x0)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x17, 0x8000)
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_4B(0xC, 0xFF)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    ClearMapObjFlags(0xC, 0x4)
    SetMapObjFlags(0xC, 0x1000)
    SetMapObjFrame(0xC, "light", 0x0, 0x1)
    SetMapObjFrame(0xC, "mark01", 0x0, 0x1)
    ClearMapObjFlags(0xD, 0x4)
    SetMapObjFlags(0xD, 0x1000)
    SetMapObjFrame(0xD, "light", 0x0, 0x1)
    SetMapObjFrame(0xD, "mark01", 0x0, 0x1)
    ClearMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0x9, 0x1000)
    SetMapObjFrame(0x9, "light", 0x0, 0x1)
    ClearMapObjFlags(0xE, 0x4)
    SetMapObjFlags(0xE, 0x1000)
    OP_71(0xE, 0x0, 0x258, 0x0, 0x20)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xCC, 0x8F, 0x85, 0x0, 0xE6, 0x0)
    SetChrPos(0x102, -5000000, 0, 0, 0)
    SetChrPos(0x103, -5000000, 0, 0, 0)
    SetChrPos(0x104, -5000000, 0, 0, 0)
    SetChrPos(0x109, -5000000, 0, 0, 0)
    SetChrPos(0x105, -5000000, 0, 0, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x17, -5000000, 0, 0, 0)
    SetChrPos(0x12, -5000000, 0, 0, 0)
    SetChrPos(0x13, -5000000, 0, 0, 0)
    SetChrPos(0x14, -5000000, 0, 0, 0)
    SetChrPos(0x8, -5000000, 0, 0, 0)
    SetChrPos(0x9, -5000000, 0, 0, 0)
    SetChrPos(0xA, -5000000, 0, 0, 0)
    SetChrPos(0xB, -5000000, 0, 0, 0)
    SetChrPos(0xC, -5000000, 0, 0, 0)
    OP_68(-12300, -550, 22120, 0)
    MoveCamera(315, 20, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(20000, 0)
    OP_68(200, -550, 23600, 10000)
    MoveCamera(305, 15, 0, 10000)
    OP_6E(600, 10000)
    SetCameraDistance(20000, 10000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    SetChrPos(0x12, -950, 300, 54300, 270)
    SetChrPos(0xA, -2150, 450, 54300, 90)
    SetChrPos(0xC, -2150, 450, 54300, 90)
    SetChrPos(0x8, -2150, 450, 54300, 90)
    SetChrPos(0xB, -2150, 450, 54300, 90)
    SetChrPos(0x9, -2150, 450, 54300, 90)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(-1500, 900, 54300, 0)
    MoveCamera(315, 20, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18000, 0)
    OP_68(650, 600, 54300, 8000)
    SetCameraDistance(20000, 8000)
    OP_0D()
    BeginChrThread(0x12, 1, 0, 58)
    Sleep(1000)
    Sound(105, 0, 100, 0)
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x0)
    BeginChrThread(0xA, 1, 0, 59)
    Sleep(500)
    BeginChrThread(0xC, 1, 0, 60)
    Sleep(500)
    BeginChrThread(0xB, 1, 0, 62)
    Sleep(750)
    BeginChrThread(0x9, 1, 0, 63)
    Sleep(750)
    BeginChrThread(0x8, 1, 0, 61)
    WaitChrThread(0x12, 1)
    WaitChrThread(0xA, 1)
    WaitChrThread(0xC, 1)
    WaitChrThread(0x8, 1)
    WaitChrThread(0xB, 1)
    WaitChrThread(0x9, 1)
    OP_6F(0x79)
    Fade(500)
    OP_64(0xA)
    OP_64(0xC)
    OP_64(0x8)
    OP_64(0xB)
    OP_64(0x9)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrPos(0x12, -8230, 7110, 64050, 270)
    SetChrPos(0x13, -14750, 7000, 37800, 30)
    SetChrPos(0x14, -5650, 7000, 71150, 180)
    OP_68(-5650, 8000, 71150, 0)
    MoveCamera(320, 20, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(20000, 0)
    OP_68(-15500, 8100, 42800, 7000)
    MoveCamera(300, 20, 0, 7000)
    SetCameraDistance(22000, 7000)

    def lambda_70E1():
        OP_9B(0x0, 0xFE, 0x0, 0x4E20, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_70E1)
    Sleep(3000)
    OP_95(0x13, -13050, 7000, 41450, 2000, 0x0)
    OP_95(0x13, -15450, 7250, 42850, 2000, 0x0)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    SetChrFlags(0x12, 0x80)
    SetChrBattleFlags(0x12, 0x8000)
    SetChrFlags(0x13, 0x80)
    SetChrBattleFlags(0x13, 0x8000)
    SetChrFlags(0x14, 0x80)
    SetChrBattleFlags(0x14, 0x8000)
    SetChrPos(0x101, 5750, -2000, 6500, 270)
    SetChrPos(0x102, 5400, -2000, 7700, 225)
    SetChrPos(0x103, 5500, -2000, 5350, 270)
    SetChrPos(0x104, 3700, -2000, 7550, 180)
    SetChrPos(0x109, 5050, -2000, 9000, 225)
    SetChrPos(0x105, 6850, -2000, 7550, 225)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x17, 2900, -2000, 5800, 90)
    OP_68(4370, -900, 6610, 0)
    MoveCamera(301, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17000, 0)
    SetCameraDistance(16000, 1500)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x17,
        (
            "#07904F#5PApparently \"Red constellation\" also\x01",
            "It seems that we withdrew completely.\x02\x03",
            "#07902FEvidence of plundering also\x01",
            "It does not seem particularly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00004F#12PIs that so……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102F#12PWas good……\x01",
            "It is unfortunate happiness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F#11POriginally, unless necessary\x01",
            "They do not do useless looting.\x02\x03",
            "#00308FOn the contrary, whatever it is necessary\x01",
            "I wonder what I can do … ….\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x104)

    def lambda_7360():
        TurnDirection(0x17, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_7360)
    Sleep(50)

    def lambda_7370():
        TurnDirection(0x101, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_7370)
    Sleep(50)

    def lambda_7380():
        TurnDirection(0x102, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_7380)
    Sleep(50)

    def lambda_7390():
        TurnDirection(0x103, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_7390)
    Sleep(50)

    def lambda_73A0():
        TurnDirection(0x109, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_73A0)
    Sleep(50)

    def lambda_73B0():
        TurnDirection(0x105, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_73B0)
    WaitChrThread(0x17, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x109,
        "#10105F#12PRandy senior?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#07908F#5PAll right?\x01",
            "It was quite unreasonable\x01",
            "I heard it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300F#11PNo, I do not care.\x02\x03",
            "#00306FThe rifle that unlocks the seal\x01",
            "It will not be useful for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#12PTo that amazing chain saw\x01",
            "I was getting frustrated.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#6PBut, Mr. Charlie's\x01",
            "Chainsaw rifle and nice …\x02\x03",
            "#00201FA hunter of \"red constellation\"\x01",
            "You have outrageous equipment, are not you?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x103, 500)
    Sleep(100)

    ChrTalk(
        0x104,
        (
            "#00303F#5POh, to a special weapons workshop\x01",
            "I bother asking you … …\x02\x03",
            "#00302FWell, if it was the mentor of Guillaume\x01",
            "You can manage it somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002F#6POh, that's fine.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109F#12PHuhu, back to town\x01",
            "Shall I come back soon?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#07904F#5P… But it was also good.\x02\x03",
            "#07902FAlso rifle\x01",
            "You started to use it.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x104, 0xB4, 0x1F4)
    Sleep(100)

    ChrTalk(
        0x104,
        (
            "#00300F#11PHaha … … It is late.\x02\x03",
            "#00309FNo, to you also\x01",
            "I got a lot of worry about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#07906F#5PThat's right.\x01",
            "If you can use rifles from the beginning\x01",
            "Even now enrolled in the guard … …\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x17, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(500)

    def lambda_7797():
        TurnDirection(0x101, 0x17, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_7797)
    Sleep(50)

    def lambda_77A7():
        TurnDirection(0x102, 0x17, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_77A7)
    Sleep(50)

    def lambda_77B7():
        TurnDirection(0x103, 0x17, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_77B7)
    Sleep(50)

    def lambda_77C7():
        TurnDirection(0x109, 0x17, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_77C7)
    Sleep(50)

    def lambda_77D7():
        TurnDirection(0x105, 0x17, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_77D7)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    OP_63(0x17, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    TurnDirection(0x17, 0x103, 500)
    Sleep(500)
    TurnDirection(0x17, 0x104, 500)
    Sleep(500)
    TurnDirection(0x17, 0x101, 500)

    ChrTalk(
        0x17,
        (
            "#07911F#5PBecause it is different! Is it?\x02\x03",
            "That, this challenging polan man\x01",
            "I wonder if I can do it properly at others!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012F#12P(my mother……)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00102F#12P(It is somewhat funny.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00204F#6P(Randy also noticed\x01",
            "I wonder why … …)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(803, 2, 100, 0)
    Sleep(300)
    OP_64(0x17)
    OP_63(0x17, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_93(0x17, 0xB4, 0x1F4)
    Fade(250)
    Sound(802, 0, 100, 0)
    SetChrFlags(0x17, 0x2)
    SetChrChipByIndex(0x17, 0x21)
    SetChrSubChip(0x17, 0x0)
    OP_0D()
    Sleep(500)
    SetChrSubChip(0x17, 0x1)
    OP_24(0x323)
    Sound(804, 0, 100, 0)

    ChrTalk(
        0x17,
        (
            "#07903F#11PKohon ……\x01",
            "It is 01 direction square unit, Mireilleu.\x02\x03",
            "#07902FOh, thanks for your trouble.\x01",
            "So their footsteps ……\x02\x03",
            "#07905F#30W……………………………………\x02\x03",
            "#07908F……What's that?\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0x1770)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005F#12PWell, what happened?\x02",
    )

    CloseMessageWindow()
    Fade(250)
    ClearChrFlags(0x17, 0x2)
    SetChrChipByIndex(0x17, 0x20)
    SetChrSubChip(0x17, 0x0)
    Sound(804, 0, 100, 0)
    Sound(802, 0, 100, 0)
    OP_0D()
    Sleep(300)
    TurnDirection(0x17, 0x101, 500)
    Sleep(150)

    ChrTalk(
        0x17,
        (
            "#07906F#5P… … withdrawing hunters\x01",
            "It seems that it suddenly disappeared.\x02\x03",
            "#07901FFrom the way of tunnel road\x01",
            "It seems that I went to the ruins … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00201F#6P\"Monastery of the Moon\" … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#12PThat……\x01",
            "Is not she ran into the ruins?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#07903F#5PNo, the blockade in front of the ruins\x01",
            "I heard there was no evidence of breakthrough.\x02\x03",
            "#07908FWhere the hell ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F#11P…… That neighborhood\x01",
            "There are only cliffs that stand out … ….\x02\x03",
            "#10101FThere is no place to withdraw\x01",
            "Even though there should not be anywhere ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303F#12PHm, that Charlie is a child\x01",
            "Common sense seems not to pass, but …\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x104)
    Sleep(500)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7561", 0)

    ChrTalk(
        0x104,
        (
            "#00306F#11PI thought it was strange.\x02\x03",
            "#00301FThose guys who were in Mainz direction … …\x01",
            "Even though I think about it, the number is too small.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x17, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_7E13():
        TurnDirection(0x17, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_7E13)
    Sleep(50)

    def lambda_7E23():
        TurnDirection(0x101, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_7E23)
    Sleep(50)

    def lambda_7E33():
        TurnDirection(0x102, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_7E33)
    Sleep(50)

    def lambda_7E43():
        TurnDirection(0x103, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_7E43)
    Sleep(50)

    def lambda_7E53():
        TurnDirection(0x109, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_7E53)
    Sleep(50)

    def lambda_7E63():
        TurnDirection(0x105, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_7E63)
    WaitChrThread(0x17, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x101,
        "#00011F#6Pwhat……?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)
    Sleep(200)

    ChrTalk(
        0x104,
        (
            "#00303F#5PI was in Crosbell\x01",
            "A large household with around 100 people …\x02\x03",
            "But, I was in Mainz direction\x01",
            "About 20 at most.\x02\x03",
            "#00308F……More than anything\x01",
            "Sigmund Orlando ----\x02\x03",
            "#00311FThat idiot of over Charlie\x01",
            "Where did he go …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00013F#6PAh……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        "#07907F#5PWell, that is ….\x02",
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_93(0x103, 0x87, 0x1F4)

    ChrTalk(
        0x103,
        (
            "#00205F#5PAh……\x02\x03",
            "#00207F#4S── Everyone, that!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x17, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_68(13800, -900, 940, 2500)

    def lambda_80D8():
        OP_93(0x101, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_80D8)
    Sleep(20)

    def lambda_80E8():
        OP_93(0x102, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_80E8)
    Sleep(20)

    def lambda_80F8():
        OP_93(0x104, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_80F8)
    Sleep(20)

    def lambda_8108():
        OP_93(0x109, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_8108)
    Sleep(20)

    def lambda_8118():
        OP_93(0x105, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_8118)
    Sleep(20)

    def lambda_8128():
        OP_93(0x17, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_8128)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x17, 0)
    Sleep(2000)
    Fade(500)
    CancelBlur(3000)
    OP_68(68650, 0, 20750, 0)
    MoveCamera(90, 18, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(52000, 0)
    MoveCamera(90, 20, 0, 5000)
    SetCameraDistance(50000, 5000)
    OP_7D(0xB4, 0x96, 0x96, 0x0, 0x0)
    OP_11(0x16, 0x0, 0xA, 0x15, 0x34, 0x0)
    OP_0D()
    OP_6F(0x79)
    SetMessageWindowPos(-1, 280, -1, -1)

    AnonymousTalk(
        0x102,
        "#00107FOh, that is ……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(280, 280, -1, -1)

    AnonymousTalk(
        0x109,
        "#10110FWell, no way …!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(300)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)
    SetMessageWindowPos(0, 280, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#00007FCrossbell City ----\x01",
            "Are you burning! Is it?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetCameraDistance(52000, 2000)
    FadeToDark(1500, 0, -1)
    OP_0D()
    StopBGM(0x1388)
    WaitBGM()
    OP_29(0xAA, 0x1, 0x7)
    OP_29(0xAA, 0x4, 0x10)
    OP_E5(0xA)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_57(0x3)
    OP_E5(0x3)
    Sleep(100)
    MiniGame(0x2B, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_E0(0x20, 0x0)
    Sleep(100)
    OP_68(-1000000, 0, 0, 0)
    OP_C9(0x0, 0x10)
    OP_C9(0x0, 0x10000)
    SetScenarioFlags(0x25, 0)
    OP_50(0x31, (scpexpr(EXPR_PUSH_LONG, 0x9A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ShowSaveMenu()
    ClearScenarioFlags(0x25, 0)
    MiniGame(0x2B, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_49()
    OP_CC(0x1, 0xFF, 0x0)
    OP_C9(0x1, 0x10)
    OP_E5(0xB)
    ReplaceBGM("ed7301", -1)
    ReplaceBGM("ed7351", -1)
    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 3)
    NewScene("c0400", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_57_6BDA end

    def Function_58_8355(): pass

    label("Function_58_8355")

    OP_96(0xFE, 0x28A, 0x0, 0xD41C, 0x3E8, 0x0)
    OP_95(0xFE, 650, 0, 55950, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_58_8355 end

    def Function_59_8385(): pass

    label("Function_59_8385")

    ClearChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x40)

    def lambda_8394():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_8394)
    OP_95(0xFE, 3000, 0, 54800, 3000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(500)
    OP_63(0xFE, 0x0, 1700, 0x26, 0x27, 0xFA, 0x0)
    SetChrFlags(0xFE, 0x4)
    ClearChrFlags(0xFE, 0x40)
    Return()

    # Function_59_8385 end

    def Function_60_83DB(): pass

    label("Function_60_83DB")

    ClearChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x40)

    def lambda_83EA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_83EA)
    OP_95(0xFE, 3000, 0, 53800, 3000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    OP_63(0xFE, 0x0, 1700, 0x26, 0x27, 0xFA, 0x0)
    SetChrFlags(0xFE, 0x4)
    ClearChrFlags(0xFE, 0x40)
    Return()

    # Function_60_83DB end

    def Function_61_842E(): pass

    label("Function_61_842E")

    ClearChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x40)

    def lambda_843D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_843D)
    OP_95(0xFE, 650, 0, 54300, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(300)
    OP_95(0xFE, 650, 0, 54950, 2000, 0x0)
    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x0)
    SetChrFlags(0xFE, 0x4)
    ClearChrFlags(0xFE, 0x40)
    Return()

    # Function_61_842E end

    def Function_62_8498(): pass

    label("Function_62_8498")

    ClearChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x40)

    def lambda_84A7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_84A7)
    OP_95(0xFE, 650, 0, 54300, 2000, 0x0)
    OP_95(0xFE, 1150, 0, 51250, 2000, 0x0)
    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x0)
    SetChrFlags(0xFE, 0x4)
    ClearChrFlags(0xFE, 0x40)
    Return()

    # Function_62_8498 end

    def Function_63_84F8(): pass

    label("Function_63_84F8")

    ClearChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x40)

    def lambda_8507():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_8507)
    OP_95(0xFE, 650, 0, 54300, 2000, 0x0)
    OP_95(0xFE, 2400, 0, 52100, 2000, 0x0)
    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x0)
    SetChrFlags(0xFE, 0x4)
    ClearChrFlags(0xFE, 0x40)
    Return()

    # Function_63_84F8 end

    def Function_64_8558(): pass

    label("Function_64_8558")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50123.itc", 0x1E)
    LoadChrToIndex("apl/ch50124.itc", 0x1F)
    SetChrChipByIndex(0x12, 0x1E)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8000)
    SetChrChipByIndex(0x13, 0x1E)
    SetChrSubChip(0x13, 0x0)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8000)
    SetChrChipByIndex(0x14, 0x1E)
    SetChrSubChip(0x14, 0x0)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8000)
    SetChrChipByIndex(0x15, 0x1F)
    SetChrSubChip(0x15, 0x0)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x8000)
    SetChrChipByIndex(0x16, 0x1F)
    SetChrSubChip(0x16, 0x0)
    ClearChrFlags(0x16, 0x80)
    SetChrFlags(0x16, 0x8000)
    SetChrPos(0x0, 5000000, 0, 0, 0)
    SetChrPos(0x1, 5000000, 0, 0, 0)
    SetChrPos(0x2, 5000000, 0, 0, 0)
    SetChrPos(0x3, 5000000, 0, 0, 0)
    SetChrPos(0x12, -500, -2000, -1500, 180)
    SetChrPos(0x13, 1250, -2000, -1300, 180)
    SetChrPos(0x14, 4450, -2000, 1050, 135)
    SetChrPos(0x15, -2350, -2000, 9550, 270)
    SetChrPos(0x16, 850, -2000, 5500, 180)
    BeginChrThread(0x14, 1, 0, 65)
    BeginChrThread(0x15, 1, 0, 66)
    BeginChrThread(0x16, 1, 0, 67)
    OP_68(1600, 200, -4600, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(12000, 0)
    OP_68(3250, 200, 950, 6000)
    MoveCamera(315, 20, 0, 6000)
    SetCameraDistance(15000, 6000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(5000)
    Fade(500)
    EndChrThread(0x14, 0x1)
    EndChrThread(0x15, 0x1)
    EndChrThread(0x16, 0x1)
    SetChrPos(0x14, 400, 0, 52700, 90)
    SetChrPos(0x15, 400, 0, 55350, 90)
    OP_68(-1700, 2150, 54300, 0)
    MoveCamera(315, 30, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(22000, 0)
    MoveCamera(305, 25, 0, 4000)
    SetCameraDistance(19000, 4000)
    OP_0D()
    Sleep(1500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 0)
    NewScene("t0520", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_64_8558 end

    def Function_65_8766(): pass

    label("Function_65_8766")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_87B2")
    OP_95(0xFE, 4450, -2000, 1050, 2000, 0x0)
    OP_93(0xFE, 0x87, 0x1F4)
    Sleep(1500)
    OP_95(0xFE, 6000, -2000, 3050, 2000, 0x0)
    OP_93(0xFE, 0x87, 0x1F4)
    Sleep(1500)
    Jump("Function_65_8766")

    label("loc_87B2")

    Return()

    # Function_65_8766 end

    def Function_66_87B3(): pass

    label("Function_66_87B3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_87FF")
    OP_95(0xFE, -1850, -2000, 2250, 2000, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(1500)
    OP_95(0xFE, -2350, -2000, 9550, 2000, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(1500)
    Jump("Function_66_87B3")

    label("loc_87FF")

    Return()

    # Function_66_87B3 end

    def Function_67_8800(): pass

    label("Function_67_8800")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8824")
    OP_93(0xFE, 0xE1, 0x1F4)
    Sleep(2000)
    OP_93(0xFE, 0x87, 0x1F4)
    Sleep(2000)
    Jump("Function_67_8800")

    label("loc_8824")

    Return()

    # Function_67_8800 end

    def Function_68_8825(): pass

    label("Function_68_8825")

    TalkBegin(0xFF)
    Sound(807, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The door is tightly closed.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_68_8825 end

    SaveToFile()

Try(main)
